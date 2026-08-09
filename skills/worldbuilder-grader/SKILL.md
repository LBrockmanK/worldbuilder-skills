---
name: worldbuilder-grader
description: Use when running a post-generation quality check on character notes. Detects input-echo and within-model divergence failures.
---

# Worldbuilder Grader

Post-generation quality check for character notes. Two detection methods,
both zero marginal cost when run during the standard generation flow.

## When to use

Run after generating a character note with `worldbuilder-character`.
This skill does not modify the note. It produces a quality report.

## Flow

1. Load the generated character note, its source Design Notes, and the
   variant spreads from the generation step (PART 2 of the generation
   output).
2. **Input-echo detection:** For each synthesized entry in Background,
   Body, Soul, and Relationships, run `scripts/detect_input_echo.py`.
   Compare the entry's phrasing against the Design Notes. Categorize as
   `input_echo` (overlap above threshold) or `clean`.
3. **Within-model divergence check:** For each entry's 3-variant spread,
   compute pairwise Jaccard similarity of lowercase character trigrams
   using `ngram_overlap()` from `scripts/detect_input_echo.py`. Flag
   entries where average pairwise similarity exceeds 0.25 as
   `low_divergence`. This signals either input-forcing or generic output.
4. Report findings.

## What each finding means

- **Input-echo:** The entry's phrasing closely matches the Design Notes
  input. The fact-to-manifestation rule was not followed. The model
  reproduced input phrasing instead of transforming it into observable
  behavior. **Action:** regenerate the entry.
- **Low-divergence:** The 3-variant spread failed to produce genuinely
  different renderings. Either the input is too constraining (narrow
  fact with only one natural expression) or the model fell back on
  generic phrasing. **Action:** if the input is narrow, accept; if the
  output looks generic, regenerate with a prompt for deliberate
  divergence.
- **Clean:** Entry passed both checks. No action needed.

## Output

Produce a quality report as a markdown document listing each flagged
entry with its category, the matching input line (for echo) or pairwise
overlap scores (for divergence), and a recommendation.

## Design history

Cross-model convergence detection (comparing outputs across multiple
models to find slop) was tested in the convergence validation experiment
(2026-07-30) and retested with Pipeline v2 (2026-08-09). It did not
graduate: the metric could not distinguish legitimate factual similarity
(models describing the same character events) from generic filler.
Precision for slop detection was near zero. The two methods above
provide reliable signal at zero marginal cost without requiring
multi-model generation.

The within-model divergence check functions primarily as prevention: the
3-variant spread rule in generation-rules.md requires divergent output,
and the grader verifies compliance. The retest produced zero
low-divergence findings, which confirms prevention is working but does
not validate detection precision. Detection precision requires positive
cases from a future trial where the divergence rule is deliberately
relaxed.
