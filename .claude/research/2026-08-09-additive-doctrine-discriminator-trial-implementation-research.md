---
type: research
title: Additive-Doctrine Discriminator Trial — Implementation Research
description: 'Implementation research for the discriminator trial plan: detection
  script API, entry extraction patterns, prompt assembly sources, generation dispatch
  options.'
tags:
- complete
date: 2026-08-09
timestamp: 2026-08-09T22:48Z
resources:
- "[[2026-08-09-additive-doctrine-discriminator-trial]]"
---

# Additive-Doctrine Discriminator Trial — Implementation Research

## Goals

Gather implementation details for the discriminator trial plan:
detection script API, entry extraction conventions, prompt assembly
sources, and generation dispatch options.

## Results

### Detection API (`scripts/detect_input_echo.py`)

Stdlib-only Python. Three functions:
- `ngram_overlap(text_a, text_b, n=3) -> float` — Jaccard similarity
  of character trigrams. Returns 0.0–1.0.
- `categorize(output_entry, input_notes, threshold=0.35) -> dict` —
  splits input_notes into lines, finds best overlap. Returns
  `{category, matched_input, overlap}`.
- `compare_cross_model(...)` — not needed for this trial.

Import path: `sys.path.insert(0, ...)` then
`from scripts.detect_input_echo import categorize, ngram_overlap`.

### Entry extraction

The convergence retest (`run_detection.py`) uses a complex PART 1/PART
2 splitting pattern specific to variant-group outputs. Our trial
generates standard character notes — the spec defines entry extraction
as splitting by `##` headings, which is simpler.

### Prompt sources

- Base: `trials/2026-07-writing-doctrine/src/base.md`
- Additive overlay: `trials/2026-07-writing-doctrine/src/doctrine-additive.md`
- Stopslop overlay: `trials/2026-07-writing-doctrine/src/style-stopslop.md`
- Design notes: `trials/2026-07-convergence-retest/nadja-cleaned.md`,
  `trials/2026-07-convergence-retest/kallya-cleaned.md`

### Generation dispatch

No existing Claude API calling pattern in the project. Prior trials
dispatched via Claude Code subagents (human-orchestrated). The spec
requires programmatic generation via Claude API calls. The `anthropic`
Python SDK is needed.

## Consolidation

The runner script needs: anthropic SDK for generation, stdlib `re` for
entry extraction, and the existing `categorize`/`ngram_overlap` for
detection. Two independent phases (generate, detect) sharing a common
output directory.
