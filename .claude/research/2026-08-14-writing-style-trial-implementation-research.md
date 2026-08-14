---
type: research
title: Writing style trial — implementation research
description: 'Implementation context for the writing style trial: file geography,
  style reference points, available test characters'
tags:
- complete
date: 2026-08-14
timestamp: 2026-08-14T02:29Z
resources: []
---

# Writing style trial — implementation research

## Goals

Gather implementation context for the writing style trial plan.

## Results

- **Style reference point:** `skills/worldbuilder-character/SKILL.md:8` says "All prose this skill produces follows `../writing-style.md`. Read it before writing." Also referenced at lines 96, 100, 102. Not referenced in generation-rules.md.
- **Replacement mechanism:** Each condition replaces the writing-style.md reference with condition-specific style instructions. The style file is read by the generating agent at the start of the skill flow.
- **Available test character:** Nadja (Design Notes at `trials/2026-07-convergence-validation/inputs/nadja-inputs.md` and cleaned version at `trials/2026-07-convergence-retest/nadja-cleaned.md`). Kallya excluded (poor input quality in previous trial).
- **Trial directory convention:** `trials/<date>-<name>/` with `inputs/`, `out/`, `results/` subdirectories.

## Consolidation

The trial creates 4 condition-specific style instruction files in `conditions/`, generates Soul output under each, then blinds and presents for general-impression review. No scripts or mechanical checks needed — this is a pure style comparison.
