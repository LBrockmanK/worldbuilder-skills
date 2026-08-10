---
type: spec
title: Additive-Doctrine Discriminator Trial
description: Trial using graduated detection components (input-echo, within-model
  divergence) as mechanical discriminators to validate or challenge the additive-doctrine
  adoption. 3 arms (current, additive, stopslop) × 2 characters (Nadja, Kallya) ×
  3 runs × 2 models (Sonnet, Opus) = 36 generations, no blinding.
tags:
- complete
date: 2026-08-09
timestamp: 2026-08-10T01:20Z
resources:
- "[[2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja]]"
- "[[2026-07-26-standing-writing-assessment-methodology-a-b-trial-suite-and-production-self-review-battery]]"
---

# Additive-Doctrine Discriminator Trial

## Context

The additive doctrine was adopted (2026-07-25) on Kevin's qualitative
read of one blind-trial arm, explicitly ahead of the measured data.
The original 2x3 trial showed LLM judges could not discriminate
between arms — agent ranking completely inverted the human ranking.
The inbox item parks a revisit pending a cheap discriminator.

Two detection components graduated from the convergence validation
retest (2026-08-09): input-echo detection (trigram Jaccard similarity
against source design notes, threshold 0.35) and within-model
divergence (pairwise trigram overlap across repeated generations from
the same model). Both are mechanical and require no LLM judge. This
trial uses them as discriminators to measure whether additive doctrine
measurably changes model behavior — specifically, whether it produces
output that diverges more from the input brief and/or varies more
across repeated generations.

These metrics measure structural properties (echo, variance), not
prose quality. The human qualitative read already covers the quality
axis. A measured behavioral difference would strengthen the adoption's
evidence base; no difference would leave the adoption resting solely
on the original qualitative judgment.

## Decisions

### D1. Trial matrix

Three doctrine arms, two characters, three runs per cell, two models:

| Axis | Levels |
|---|---|
| Doctrine | current, additive, stopslop |
| Character | Nadja, Kallya |
| Runs | 3 per cell |
| Model | claude-sonnet-5, claude-opus-4-6 |

Total cells: 3 × 2 × 2 = 12. Total generations: 12 × 3 = 36.

Model IDs are pinned to prevent alias rotation during the trial.

The stopslop arm provides a reference delta for a non-doctrine
change. Stopslop alters sentence structure, voice, list length, and
word choice — surface properties that will move trigram-based metrics.
The question is not whether stopslop moves them (it will) but whether
additive moves them differently in magnitude or pattern, indicating a
doctrine-level effect beyond surface style.

### D2. Inputs

Each generation receives:

- **Design notes:** the character's frozen design notes (Nadja and
  Kallya cleaned notes from the convergence retest, already in
  `trials/2026-07-convergence-retest/`).
- **Base instructions:** the generation instructions from
  `trials/2026-07-writing-doctrine/src/base.md`.
- **Arm-specific overlay:** varies by arm (see below).

Arm composition (each receives design notes + base instructions +):

| Arm | Overlay |
|---|---|
| current | (none — base instructions only) |
| additive | `src/doctrine-additive.md` appended to base |
| stopslop | `src/style-stopslop.md` appended to base |

No arm receives both a doctrine and a style overlay. The current arm
is the pure baseline; the additive arm adds doctrine constraints; the
stopslop arm adds style constraints. This isolates doctrine from
style.

Temperature and system prompt are held constant across all cells.
The plan pins exact values; the spec requires only that they do not
vary between cells. Model is the only cross-cell variable besides
the arm overlay.

### D3. Metrics

Two graduated detection components from `scripts/detect_input_echo.py`:

**Entry extraction.** Each generated note is split into entries by
top-level markdown heading (## sections). Frontmatter and the H1
title line are excluded. Each section's body text (stripped of sub-
headings) is one entry. Empty sections are dropped. This matches the
granularity used in the convergence retest's `run_detection.py`.

**Input-echo score.** Per-entry trigram Jaccard similarity between
each entry and the full design notes text, via `categorize()`.
Reported as:
- Per-run mean overlap score (mean of all entries in one generation)
- Per-cell mean overlap score (mean of the 3 per-run means)
- Per-cell echo rate (proportion of all entries across the 3 runs
  exceeding the 0.35 threshold)

Aggregation: per-run means are averaged equally to produce the cell
mean, regardless of entry count per run.

**Within-model divergence.** Pairwise trigram overlap across the 3
runs of each cell, via `ngram_overlap()`. Comparison unit: full note
text (not per-entry). Three pairwise comparisons per cell (run1–run2,
run1–run3, run2–run3). Reported as:
- Per-cell mean pairwise overlap (mean of the 3 comparisons,
  continuous, 0.0–1.0)
- Higher overlap = less divergence = model locked into a pattern

Both metrics are directional:
- **Input-echo:** lower is better (output diverges from input).
  Additive doctrine should produce lower echo if it drives the model
  to build beyond the brief rather than restate it.
- **Within-model divergence:** lower overlap is better (more variance
  across runs). Additive doctrine should produce more varied output if
  it opens the generation space rather than funneling toward one
  rendering.

### D4. Reporting

The runner produces a structured JSON report and a human-readable
summary. The summary includes:

- Per-cell means for both metrics
- Cross-arm deltas (additive vs current, stopslop vs current)
- Per-model breakdown (Sonnet vs Opus)
- Per-character breakdown (Nadja vs Kallya)
- Stopslop-vs-current deltas alongside additive-vs-current deltas,
  for both metrics, so the relative magnitude of each change is
  visible

### D5. Success criteria

The trial answers two primary questions and one interpretive
comparison:

1. **Does additive doctrine reduce input echo?** Measured: additive
   arm's mean echo score is lower than current arm's, consistently
   across both characters and both models.
2. **Does additive doctrine increase generation variance?** Measured:
   additive arm's mean pairwise overlap is lower than current arm's,
   consistently across both characters and both models.
3. **Does the additive delta differ from the stopslop delta?** The
   stopslop arm provides a reference: both stopslop and additive will
   move the metrics relative to current (both change the output text).
   The interpretive question is whether additive moves them by more,
   less, or differently than stopslop — indicating a doctrine-level
   effect beyond surface style change. This is reported as a
   comparison, not a pass/fail gate.

"Consistently" means the direction holds in at least 3 of 4
character×model combinations (not required in all 4 — one reversal
is tolerable as noise).

No pre-registered effect size. The trial measures whether the
direction is consistent, not whether the magnitude meets a threshold.
Given n=3 runs per cell, statistical power is low; the trial is
designed to detect a consistent directional signal, not to prove
significance.

### D6. Infrastructure

A new standalone trial directory: `trials/2026-08-additive-discriminator/`.

Contents:
- `run_trial.py` — runner script: takes the trial matrix, dispatches
  generations, collects outputs into `out/`, runs detection over the
  full set, produces the report.
- `out/` — generated notes, named
  `{character}-{doctrine}-{model_short}-run{n}.md` where
  `model_short` strips the `claude-` prefix (e.g., `sonnet-5`,
  `opus-4-6`).
- `report.json` — structured results.
- `summary.md` — human-readable comparison report.
- `README.md` — trial description and reproduction instructions.

The runner has two phases: generation and detection. Generation
dispatches each cell's runs via Claude API calls (model ID, assembled
prompt, constant parameters). Detection imports `ngram_overlap` and
`categorize` from `scripts/detect_input_echo.py` and runs them over
the collected outputs. The two phases are independent — detection can
rerun over existing outputs without regenerating.

### D7. No blinding

Blinding is unnecessary. The original trial blinded LLM judges and
human scorers to prevent bias. This trial's metrics are mechanical
(string similarity computations) — they cannot be biased by knowledge
of which arm produced which output. The sealed-key mechanism from the
original trial kit is not used.

### D8. Outcome actions

Based on results, in precedence order:

- **Consistent improvement on both metrics (3+ of 4 cells each):**
  Record as measured evidence supporting the adoption. Update inbox
  item to reflect the adoption now has both qualitative and
  quantitative backing. Close the revisit trigger.
- **Consistent improvement on one metric, neutral on the other:**
  Record as partial measured support. The adoption gains evidence on
  one axis. Close the revisit trigger with a note that only one
  metric moved.
- **Consistent improvement on one metric, consistent worsening on
  the other:** Record as a split result. The adoption is neither
  strengthened nor weakened — the metrics pull in opposite directions.
  The revisit trigger remains open. Investigate which metric is more
  meaningful for prose quality.
- **Consistent worsening on one or both metrics:** Record as measured
  evidence against the adoption. Surface to the user as a decision
  point: the qualitative read and the quantitative signal disagree.
  Do not unilaterally reverse the adoption.
- **Inconsistent direction (2 of 4 cells):** Record as a null result
  — no consistent signal detected. The adoption stands on the
  qualitative read alone. The revisit trigger remains open.
- **No measurable difference (deltas near zero across all cells):**
  Same as inconsistent — null result, trigger stays open.

The stopslop comparison (D5 question 3) is interpretive context, not
a gate. If additive and stopslop deltas are similar in magnitude and
direction, the additive signal may be a surface effect rather than a
doctrine effect — note this in the findings but do not override the
primary outcome action.

## Consequences

- Consumes ~36 character-note generations across Sonnet and Opus.
- Produces a reproducible, mechanically-scored comparison that
  strengthens, leaves unchanged, or provides evidence against the
  additive-doctrine adoption's evidence base.
- Does not and cannot replace the human qualitative judgment — these
  metrics measure behavior, not quality.
- Reuses the graduated detection components without modification,
  validating their utility beyond the convergence-detection use case
  they were built for.

## Notes (non-normative)

The additive doctrine overlay (`src/doctrine-additive.md`) covers five
principles: Banned Trait Words (replace heavy adjectives with domain +
drive + cost), Knowledge Boundaries (per-topic depth), Unresolved
States (competing pulls), The Specification Boundary (detail lock or
leave unwritten), and A Life in Motion (independent pressures). These
are structural writing constraints that plausibly affect both echo
(they demand transformation of input) and variance (they open multiple
valid renderings). The trial tests whether that plausibility is borne
out mechanically.
