---
type: research
title: Pipeline quality trial — implementation research
description: 'Implementation context for the pipeline quality trial plan: file geography,
  existing patterns, trial conventions'
tags:
- complete
date: 2026-08-13
timestamp: 2026-08-13T22:00Z
resources: []
---

# Pipeline quality trial — implementation research

## Goals

Gather implementation context for the pipeline quality trial plan: file geography, existing patterns, pipeline mechanics, trial conventions.

## Results

### Character generation pipeline

- **Skill files:** `skills/worldbuilder-character/` contains SKILL.md, framework.md, generation-rules.md, relationships.md, intimate.md
- **Generation flow:** Q&A session, Design Notes capture, then generation-rules.md governs: deslop/deframe preprocessing (strips meta-vocabulary, flags stop-slop), routing annotations ([B]/[Bo]/[S]/[R] tags), 3-variant spread with fact-to-manifestation, synthesis selection, post-group sync pass, self-check
- **Qualitative divergence check** (generation-rules.md:31-33): "could a reader tell them apart without comparing word by word? If not, discard all three and regenerate" — one retry; this is the check the mechanical gate replaces
- **Synthesis rules** (generation-rules.md:46): combine strongest elements from all three variants; must pass staging test and avoid input phrasing

### Grader mechanics

- **Skill files:** `skills/worldbuilder-grader/SKILL.md` + `scripts/detect_input_echo.py`
- **Input-echo detection:** compares entry phrasing against Design Notes; categorizes as input_echo or clean
- **Within-model divergence:** Jaccard similarity of lowercase character trigrams; threshold 0.25; flags entries as low_divergence
- **Output:** markdown quality report with category, matching input line or pairwise scores, and recommendation

### Trial conventions

- **Directory structure:** `trials/<date>-<name>/` with protocol, inputs/, out/, results/ subdirectories
- **Prior trials:** writing-doctrine, selection-mechanism, convergence-validation, convergence-retest, additive-discriminator
- **Trial data format:** markdown tables with entries per character per section; blind-key.md in results/
- **Blinding:** selection mechanism trial used blind-key.md mapping codes to conditions; entries presented by letter code

## Consolidation

The trial implementation requires: (1) a Python script for the mechanical fail-check gate using the existing `ngram_overlap()` function from the grader, (2) condition-specific generation-rules variants as modified skill prose, (3) trial infrastructure following the established `trials/` directory convention. The human-driven scoring steps follow the selection-mechanism trial's blinding pattern. No new dependencies are needed.
