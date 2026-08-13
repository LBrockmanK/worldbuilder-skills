---
type: spec
title: Cross-model convergence metric validation experiment
description: 'Validation experiment for the cross-model convergence check (METHODOLOGY.md
  4.4): parallel generation across four models (Opus 4.6, Opus 5, GPT-5.6 Sol, GPT-5.6
  Terra), three detection methods, correction pass, and human review on two characters'
tags:
- complete
date: 2026-07-30
timestamp: 2026-08-13T19:27Z
resources:
- '[[2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja]]'
output:
- "[[2026-07-30-convergence-validation-experiment-implementation]]"
---

# Cross-model convergence metric validation experiment

## Context

[METHODOLOGY.md](../../trials/METHODOLOGY.md) section 4.4 defines a
cross-model convergence check: generate the same content from two
models, flag sentences the two produce identically or near-identically.
High convergence marks model voice rather than author voice — a slop
signal.

The mechanism is designed but unvalidated (section 5 status table). The
graduation rule (section 5) requires blind comparison against human
judgment (section 2.2) before it ships in the production battery or as
an A/B testing metric. Section 6 defines a two-step validation path;
cross-provider access is now available (GPT-5.6 Sol and Terra via Codex
CLI, confirmed 2026-07-26), removing the former blocker.

This spec covers the validation experiment only. The production grader
agent and the A/B testing metric are downstream deliverables that depend
on this experiment's outcome — they are out of scope here.

## Goal

Determine whether cross-model convergence reliably identifies slop in
character notes, and whether automated corrections based on convergence
flags improve the output.

## Design

### Models

Four models, two families, two tiers within each:

| Family  | Model A       | Model B        |
|---------|---------------|----------------|
| Claude  | Opus 4.6      | Opus 5         |
| GPT     | 5.6 Sol       | 5.6 Terra      |

This yields six pairwise comparisons:

| Pair | Type           |
|------|----------------|
| Opus 4.6 ↔ Opus 5       | Within-Claude  |
| Sol ↔ Terra              | Within-GPT     |
| Opus 4.6 ↔ Sol           | Cross-provider |
| Opus 4.6 ↔ Terra         | Cross-provider |
| Opus 5 ↔ Sol             | Cross-provider |
| Opus 5 ↔ Terra           | Cross-provider |

Within-family pairs are a weak signal (shared training). Cross-provider
pairs are the strong signal. Running both lets us compare and see
whether within-family convergence overfires relative to cross-provider.

### Inputs

Each generation receives the same upstream inputs the production
pipeline uses when building a new character. The finished character
notes (nadja.md, kallya.md) are the output of that pipeline and must
not be visible to the generation models during the experiment.

Standard inputs (identical across all eight generations):

- **Skill instructions** — the production character generation skill
  (`skills/worldbuilder-character/`): framework.md section instructions,
  relationship guidelines (relationships.md), intimate dynamics rules
  (intimate.md).
- **Writing doctrine** — the current writing-style instructions
  (`skills/writing-style.md`) and slop-phrase rules
  (`docs/slop-phrases.md`).
- **World direction** — the project's direction.md, providing tone,
  setting, and style-contract context.

Per-character inputs:

- **Session Notes** — the Q&A responses capturing builder intent for the
  character's core wants, fears, behaviors, and relationships.
- **Builder Context** — narrative function, external references (real
  people or fictional characters drawn from), design decisions, open
  questions.
- **Cast/Roster Context** — named cast members and their basic
  relationships, from the project roster or plan.
- **Intimate Dynamics flag** — whether the Intimate Dynamics section
  applies to this character, from the project plan.

Characters, both from the Viralys project
(`D:\Sync\Collective Consciousness\Games\Ainime\WIP\Viralys\`):

1. **Nadja** — previously used in the 2026-07-23 writing-doctrine
   trial; human preference ranks exist for comparison.
2. **Kallya** — second character for generalizability testing.

The plan must locate each character's session notes, builder context,
and roster context in the Viralys project before the experiment runs.

### Generation

For each character, generate one full character note under each of the
four models using the current production skill and writing doctrine.
Same upstream inputs, same skill instructions, same doctrine — only the
model differs.

Output: 4 notes per character, 8 notes total.

### Detection methods

All three methods run on every pairwise comparison (6 pairs × 2
characters = 12 comparison sets). Each method produces a set of flagged
sentences per comparison.

**Method 1: Exact match.** Normalize whitespace, then flag sentences
that appear verbatim in both outputs of a pair. Zero false positives by
construction; misses paraphrased convergence.

**Method 2: Embedding similarity.** Embed each sentence, compute cosine
similarity across all sentence pairs between two outputs. Flag pairs
above a threshold. The threshold is a parameter to calibrate during the
experiment — start at 0.92 and adjust based on the human review. Catches
paraphrased convergence; requires an embedding model (choose one not
from either generation family to avoid circularity).

**Method 3: LLM-as-judge.** A model reads sentence pairs flagged by
methods 1 or 2 (not all-pairs — that is O(n²) and expensive) plus a
sample of unflagged pairs, and judges whether they express the same idea
in the same phrasing. The judge model should not be from either
generation family. This method runs on the union of flags from methods
1 and 2 plus a random sample of unflagged pairs to estimate false
negatives.

Each method produces per-sentence flags. The experiment records all
three independently; the human review compares them.

### Correction pass

For each sentence flagged by any method, generate a rewrite that
preserves the semantic content while eliminating the convergent
phrasing. The correction agent sees: the flagged sentence, which pair(s)
flagged it, and the surrounding paragraph for context. It does not see
the other model's output — it rewrites from the character brief and
note context alone.

Output: a corrected version of each note alongside the original, with
flagged sentences marked and their rewrites shown.

### Human review

The reviewer (Kevin) receives:

1. **Detection report** — every flag from every method, grouped by
   sentence. For each flag: which method(s) caught it, which pair(s)
   produced it, the convergent sentences side by side.
2. **Correction report** — each flagged sentence paired with its
   rewrite.

The reviewer judges:

- **Detection precision**: for each flag, is this actually slop?
  (true positive / false positive)
- **Correction quality**: for each rewrite, is it better than the
  original? (improved / neutral / worse)

This is not fully blind — the reviewer sees what the metric flagged
rather than independently marking every sentence. This measures
precision and correction quality, not recall. Acceptable for a first
validation pass; recall can be tested in a follow-up if the metric
earns it.

### Success criteria

The metric is validated if:

1. **Precision**: at least one detection method achieves a true-positive
   rate the reviewer considers acceptable (no preset numeric threshold —
   this is a human judgment call on whether the flags are useful).
2. **Cross-provider signal**: cross-provider pairs produce a
   meaningfully different convergence pattern than within-family pairs.
   If within-family and cross-provider flag the same things at the same
   rate, the metric is detecting shared training artifacts, not slop.
3. **Correction value**: rewrites of true-positive flags are judged
   "improved" more often than "neutral" or "worse."
4. **Consistency**: the metric behaves similarly across both characters.
   A method that works for Nadja but not the second character is
   suspect.

All four criteria must hold for the metric to graduate. The reviewer may
graduate individual detection methods (e.g., exact match passes,
LLM-as-judge doesn't) rather than the mechanism as a whole.

### What this experiment does not test

- **Recall** — slop the metric misses entirely. Deferred to a follow-up.
- **Production integration** — how the grader agent fits into the
  generation pipeline. Out of scope; depends on this experiment's
  outcome.
- **A/B testing metric** — using convergence scores to compare
  instruction methods. Out of scope; same dependency.
- **The other battery mechanisms** (dilemma test, blind-line voice test,
  counterfactual probe) — separate validation experiments.

## Consequences

- If the metric validates: the production grader and A/B metric become
  specifiable. The convergence check moves to `validated` in the
  METHODOLOGY.md section 5 status table (or individual methods move
  independently).
- If the metric fails: the grader agent concept survives (section 2.1
  author/grader separation is a standing rule) but needs a different
  slop-detection mechanism. This experiment's data informs what to try
  next.
- The experiment produces 8 character notes as a side effect. These are
  experiment artifacts, not production output.
