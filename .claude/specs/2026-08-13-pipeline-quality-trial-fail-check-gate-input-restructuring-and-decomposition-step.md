---
type: spec
title: Pipeline quality trial — fail-check gate, input restructuring, and decomposition
  step
description: Experiment comparing three pipeline improvement approaches for reducing
  echo and slop in character note generation
tags:
- abandoned
date: 2026-08-13
timestamp: 2026-08-14T02:06Z
resources: []
---

# Pipeline quality trial — fail-check gate, input restructuring, and decomposition step

## Context

The character generation pipeline (Pipeline v2) produces output through four stages: deslop/deframe preprocessing, routing annotation, 3-variant multi-option generation with fact-to-manifestation transformation, and synthesis-based selection. A post-generation grader checks for input-echo (output phrasing that reproduces Design Notes) and within-model divergence (variant spreads that fail to diverge).

Pipeline v2's convergence detector flagged 61% true positives in its initial experiment, dominated by input-echo; a retest after upstream fixes found a 0.7% input-echo rate across 146 entries, though these measure different things (detector precision vs. entry-level rate). Echo and slop remain the primary failure modes reported during human review of generated output. Three unimplemented findings from the [convergence validation experiment](../../trials/2026-07-convergence-validation/2026-07-30-convergence-validation-experiment-findings-and-graduation-assessment.md) (S1, S3, S6) propose further upstream improvements, and the [Aeon's Notebook resource review](../research/2026-07-30-resource-review-aeon-s-notebook-decision-engine-and-helpful-default-convergence.md) proposes a spread-fail-check-select mechanism that the pipeline partially implements but lacks a formal fail-check gate.

Design Notes currently use bullet-point input (Session Notes, Builder Context) and short prose fields (Structured Doctrine). Output sections (Background, Body, Soul, Relationships) are also bulleted, one entry per bullet. This structural mirror between input and output format enables line-for-line reproduction.

Design principle: improvements are more effective the earlier they appear in the pipeline, and LLM compute is cheap relative to human review time.

This trial tests all three improvement approaches against the current pipeline as a baseline, using blind human review. The rubric and protocol are informed by the [selection mechanism trial](../../trials/2026-07-selection-mechanism/results/trial-data.md) but differ in structure (four scored dimensions instead of one holistic score).

## Decisions

### D1: Four experimental conditions

The trial compares four conditions, each cumulative (each adds to the previous):

**Condition 0 — Baseline.** Current Pipeline v2: deslop/deframe preprocessing, routing annotations, 3-variant generation with fact-to-manifestation, synthesis selection. No changes.

**Condition A — Fail-check gate.** Baseline plus a formal divergence gate between variant generation and synthesis. After generating 3 variants for each entry, compute pairwise Jaccard similarity of lowercase character trigrams. If any pair exceeds 0.25, reject the spread and regenerate that entry. Allow 3 additional regeneration attempts (4 total including the original). If all fail the threshold, flag the entry and proceed with the spread whose maximum pairwise Jaccard similarity is lowest. This mechanical gate replaces the existing qualitative divergence check in generation-rules.md for all conditions that include it (A, B, C).

**Condition B — Input restructuring.** Condition A plus three changes to how Design Notes are presented to the generation pipeline:

- S1 (orthogonal organization): Reorganize the preprocessed input by topic cluster (motivations, behaviors, relationships, fears) rather than mirroring the output sections (Background, Body, Soul, Relationships). The model receives thematic bundles and must redistribute facts across output sections.
- S3 (coarser bundling): Merge related bullet points within each topic cluster into paragraph-level blocks. No single-fact bullets; each block contains 2-4 related facts that must be decomposed.
- S6 (distinct builder voice): Add an LLM-driven rewrite pass after deslop/deframe that converts the preprocessed input into compressed clinical shorthand (abbreviated, no articles, no hedging). This is a new preprocessing stage, not a mechanical rule. Any reproduction of input phrasing in the character-voice output becomes immediately detectable.

**Condition C — Decomposition step.** Condition B plus an explicit decomposition phase before variant generation. The model must first produce a redistribution outline: for each input fact, which output section and entry it maps to, and what behavioral manifestation it becomes. The outline is validated for coverage (every input fact appears at least once) before generation proceeds. For this trial, the outline maps all input facts to their target sections, but only facts routed to Soul proceed to variant generation.

### D2: Test character and output section

Generate the Soul section for one test character with established Design Notes. Use the same character across all four conditions to control for input complexity. Select a character whose Design Notes contain at least 10 facts across multiple topic areas, providing enough material for quality differences to manifest. Run 2 generations per condition with the same model and temperature (pinned at the start of the trial) to control for stochastic variance. Score each run independently; report per-condition means across both runs.

### D3: Metrics

Score each entry on five dimensions (1-3 scale):

1. **Staging test** — Does the entry show observable behavior rather than stating an internal quality? (1 = tells: "she is brave"; 2 = mixed: names the quality but includes a behavioral example; 3 = shows: describes what she does, a reader infers the quality)
2. **Specificity** — Is the behavior concrete and particular to this character, or generic? (1 = generic: could describe anyone; 2 = moderate: somewhat particular but common pattern; 3 = specific: this behavior distinguishes this character)
3. **Input echo** — Does the phrasing reproduce Design Notes input? (1 = clear echo: a phrase of 4+ words appears verbatim or near-verbatim from the original Design Notes; 2 = partial overlap: recognizable rewording of input phrasing; 3 = fully transformed: expresses the same fact in unrelated phrasing)
4. **Slop** — Does the entry contain filler, hedging, or cliche phrasing? (1 = sloppy: hedges, qualifiers, or stock phrases dominate; 2 = some filler: one or two weak phrases in otherwise clean prose; 3 = clean: every word earns its place)
5. **Factual fidelity** — Does the entry accurately reflect the Design Notes facts it draws from, without omission, distortion, or invention? (1 = factually wrong or invented: states something unsupported by Design Notes; 2 = partially accurate: the core fact is present but details are altered or missing; 3 = faithful: the fact is preserved and nothing is added)

Additionally, run the existing grader checks (input-echo detection, within-model divergence) mechanically on all conditions, comparing against the original Design Notes (pre-preprocessing), and report rates alongside the human scores. Human echo scoring also uses the original Design Notes as the reference, not any intermediate preprocessed form.

### D4: Blind review protocol

1. Generate output for all four conditions.
2. The generating agent strips condition labels, assigns random letter codes (W, X, Y, Z), and seals the mapping. The human reviewer does not have access to the code-to-condition mapping until all scoring is complete.
3. Randomize entry order within each condition's output.
4. Present all entries to the human reviewer grouped by letter code, with the Design Notes visible for reference.
5. Reviewer scores each entry on all five dimensions before unblinding.
6. Unblind and compute per-condition means.

### D5: Success criteria

A condition is an improvement over baseline if its mean score exceeds the baseline mean by at least 0.3 on any dimension (staging, specificity, slop, or factual fidelity — the four quality dimensions; input echo is reported but not weighted for adoption since the baseline rate is already low) without regressing by more than 0.1 on any other dimension. If multiple conditions improve, adopt the one with the highest sum of per-dimension means (equal weight across all four dimensions). If no condition improves over baseline, the current pipeline stands and the trial is recorded as a negative result. Tie-break: if two conditions produce the same sum, prefer the simpler one (lower condition letter).

### D6: Adoption rule

Improvements that graduate are implemented permanently in the pipeline. Input restructuring changes modify generation-rules.md: S1 and S3 alter the preprocessing instructions; S6 adds a new LLM-driven rewrite stage that runs after deslop/deframe. The fail-check gate is added to the generation flow in the worldbuilder-character skill (generation-rules.md). The decomposition step, if it graduates, is added to generation-rules.md as a required pre-generation phase.

## Consequences

Graduating improvements shift quality enforcement earlier in the pipeline, reducing the fraction of output that requires human correction. The grader's existing checks remain as a post-generation safety net.

Input restructuring (Condition B) changes how Design Notes are preprocessed but not how users write them. S1 and S3 alter the existing preprocessing instructions; S6 adds a new LLM-driven rewrite stage after deslop/deframe. None of these change the Design Notes template.

The S6 LLM rewrite introduces a nondeterministic transformation that could alter facts. The factual fidelity dimension (D3) guards against graduating a condition that produces factually wrong output. If a condition scores well on other dimensions but poorly on fidelity, it does not graduate.

The decomposition step (Condition C) adds one LLM call per generation, increasing compute cost. This is acceptable given the design principle that LLM time is cheap relative to human review time, but should be measured and reported.

Negative results are valuable: if the bundled approach does not improve overall quality, that records the combination as ineffective. Individual S-findings (S1, S3, S6) remain open for future separate testing, since a bundled null result cannot establish that each lead is individually ineffective.

## Notes (non-normative)

The trial design is informed by the selection mechanism trial (2026-08-08) but differs: that trial used one holistic 1-3 score combining staging, specificity, echo, and slop, with 0.3 as a tie range among mechanisms. This trial uses five separate dimensions and 0.3 as an improvement-over-baseline threshold — a different rubric and a different decision rule. The cumulative condition structure (each builds on the previous) means the trial measures marginal improvement at each stage, not independent effects — this is deliberate, since the approaches are designed to compound.
