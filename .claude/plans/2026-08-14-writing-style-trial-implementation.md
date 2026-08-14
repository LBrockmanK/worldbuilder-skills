---
type: plan
title: Writing style trial implementation
description: 'Implementation plan for the writing style trial: STE-100 strict, STE-100
  loose, and BLUF conditions against baseline'
tags:
- human-ready
date: 2026-08-14
timestamp: 2026-08-14T02:36Z
resources: []
---

# Writing style trial implementation

## Goal

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Compare four writing style conditions (baseline, STE-100 strict, STE-100 loose, BLUF) for Soul section generation using blind general-impression review.

**Architecture:** Trial infrastructure under `trials/2026-08-writing-style/`. Four condition-specific style instruction files replace writing-style.md for each generation run. Blind review with sealed key, general impression per condition.

**Tech Stack:** Markdown (style instructions, protocol, outputs, results)

**Spec:** [Writing style trial spec](../specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md)
**Research dossier:** [Implementation research](../research/2026-08-14-writing-style-trial-implementation-research.md)

## Global Constraints

- Each condition replaces writing-style.md entirely. No condition runs with the ban list active alongside the new style.
- All conditions use identical Design Notes, model, and prompt structure. Only the style instruction varies.
- A graduating condition is adopted for Soul only. Extension to other sections is separate.
- Do not use Kallya as test character (poor input quality in previous trial).

---

### Task 1: Trial setup and style instructions

**Files:**
- Create: `trials/2026-08-writing-style/trial-protocol.md`
- Create: `trials/2026-08-writing-style/inputs/design-notes.md`
- Create: `trials/2026-08-writing-style/conditions/style-baseline.md`
- Create: `trials/2026-08-writing-style/conditions/style-ste100-strict.md`
- Create: `trials/2026-08-writing-style/conditions/style-ste100-loose.md`
- Create: `trials/2026-08-writing-style/conditions/style-bluf.md`

**Interfaces:**
- Consumes: spec D1-D5, `skills/writing-style.md` (baseline), `skills/worldbuilder-character/SKILL.md` (style reference pattern), Nadja's Design Notes at `trials/2026-07-convergence-retest/nadja-cleaned.md`
- Produces: trial protocol, test character input, four style instruction files referenced by Task 2

- [ ] **Step 1: Create trial directory structure**

```bash
mkdir -p trials/2026-08-writing-style/inputs
mkdir -p trials/2026-08-writing-style/conditions
mkdir -p trials/2026-08-writing-style/out
mkdir -p trials/2026-08-writing-style/results
```

- [ ] **Step 2: Select test character and copy Design Notes**

Use Nadja. Copy Design Notes from `trials/2026-07-convergence-retest/nadja-cleaned.md` to `trials/2026-08-writing-style/inputs/design-notes.md`. Review the notes for quality: they should contain clear facts, not vague implications. If the notes need cleanup, clean them before copying. Do not invent new facts.

- [ ] **Step 3: Create baseline style file**

Copy `skills/writing-style.md` verbatim to `trials/2026-08-writing-style/conditions/style-baseline.md`. This is Condition 0.

- [ ] **Step 4: Create STE-100 strict style file**

Write `trials/2026-08-writing-style/conditions/style-ste100-strict.md`:

```markdown
# Writing Style: ASD-STE-100 Strict

Write all character note entries as ASD Simplified Technical English (STE-100).

## Rules

1. Use approved words only where an approved equivalent exists. Where a simpler word exists, use it.
2. Sentences must not exceed 20 words (procedural/instructional) or 25 words (descriptive).
3. Use active voice. Name the subject.
4. One instruction or one idea per sentence.
5. No figurative language. No metaphor, no simile, no personification.
6. Present tense for current state. Past tense only for completed events.
7. Write as if producing an aircraft maintenance manual entry. Each sentence is a discrete behavioral instruction an AI must follow.
8. No em-dashes. Use periods to separate ideas.
9. No hedging words (perhaps, might, somewhat, rather, quite).
10. Every sentence must describe something the AI can act on in a scene.
```

- [ ] **Step 5: Create STE-100 loose style file**

Write `trials/2026-08-writing-style/conditions/style-ste100-loose.md`:

```markdown
# Writing Style: ASD-STE-100 (Semantic Anchor)

Write in ASD-STE-100 Simplified Technical English style.
```

- [ ] **Step 6: Create BLUF style file**

Write `trials/2026-08-writing-style/conditions/style-bluf.md`:

```markdown
# Writing Style: BLUF (Bottom Line Up Front)

Structure every entry using BLUF (Bottom Line Up Front).

## Rules

1. Lead with the observable behavior. The first sentence states what the character does.
2. Follow with context. Why, when, or how the behavior manifests comes after the behavior itself.
3. No entry may begin with backstory, emotional framing, atmosphere, or implication before stating the behavior.
```

- [ ] **Step 7: Write trial protocol**

Write `trials/2026-08-writing-style/trial-protocol.md` documenting:
- Test character (Nadja) and justification
- Pinned model and temperature (same as previous trial: `claude-opus-4-6`, temperature `1.0`)
- The four conditions with file references
- Review method: blind general impression, not per-entry scoring
- Success criteria from spec D5

- [ ] **Step 8: Commit**

```bash
git add trials/2026-08-writing-style/
git commit -m "feat: writing style trial — setup, style instructions, and protocol"
```

---

### Task 2: Generate Soul section under each condition

**Files:**
- Create: `trials/2026-08-writing-style/out/condition-0.md`
- Create: `trials/2026-08-writing-style/out/condition-a.md`
- Create: `trials/2026-08-writing-style/out/condition-b.md`
- Create: `trials/2026-08-writing-style/out/condition-c.md`

**Interfaces:**
- Consumes: Design Notes from `inputs/design-notes.md`, generation rules from `skills/worldbuilder-character/generation-rules.md`, framework from `skills/worldbuilder-character/framework.md`, condition-specific style files from `conditions/`
- Produces: 4 Soul section outputs for blinding in Task 3

All conditions are generated in the same session using the same model (claude-opus-4-6). Only the style instruction file changes between conditions.

- [ ] **Step 1: Generate Condition 0 (baseline)**

Read the baseline style file (`conditions/style-baseline.md`) as the writing style instruction. Read the Design Notes, framework, and generation rules. Generate the Soul section for Nadja following the standard generation flow (deslop/deframe, routing, 3-variant spread with fact-to-manifestation, synthesis). Save the synthesized entries to `out/condition-0.md`. Include variant spreads as a second section for reference. Aim for 8-12 synthesized entries.

- [ ] **Step 2: Generate Condition A (STE-100 strict)**

Same generation flow, but read `conditions/style-ste100-strict.md` instead of the baseline style. The style rules replace writing-style.md entirely. Save to `out/condition-a.md`. Aim for 8-12 synthesized entries.

- [ ] **Step 3: Generate Condition B (STE-100 loose)**

Same generation flow, but read `conditions/style-ste100-loose.md` instead. This is a single-line semantic anchor instruction. Save to `out/condition-b.md`. Aim for 8-12 synthesized entries.

- [ ] **Step 4: Generate Condition C (BLUF)**

Same generation flow, but read `conditions/style-bluf.md` instead. Save to `out/condition-c.md`. Aim for 8-12 synthesized entries.

- [ ] **Step 5: Commit**

```bash
git add trials/2026-08-writing-style/out/
git commit -m "data: writing style trial — 4 Soul generation outputs"
```

---

### Task 3: Blind review preparation

**Files:**
- Create: `trials/2026-08-writing-style/results/blind-key.md`
- Create: `trials/2026-08-writing-style/results/blinded-review.md`

**Interfaces:**
- Consumes: 4 generation outputs from Task 2
- Produces: blinded review document for human scoring

- [ ] **Step 1: Create blind key**

Randomly assign letter codes W, X, Y, Z to the four conditions (0, A, B, C). Write the mapping to `results/blind-key.md`. Use a genuinely random assignment, not alphabetical. The human reviewer must not access this file until all scoring is complete.

- [ ] **Step 2: Create blinded review document**

Write `results/blinded-review.md`:
- Include the original Design Notes at the top for reference
- For each letter code, include only the synthesized entries (not variant spreads)
- Label entries sequentially within each group (W-1, W-2, etc.)
- After each group, add a space for general impression:

```markdown
**General impression:**
Does this read like a functional instruction set an AI could act on?
Would you have to rewrite most of it or is it usable as-is?
Ranking (best to worst across all groups): ___
Is the best group good enough to adopt, or do all groups fail? ___

```

- [ ] **Step 3: Commit**

```bash
git add trials/2026-08-writing-style/results/
git commit -m "data: blind key and blinded review document for writing style trial"
```

---

### Task 4: Record results (after human review)

**Files:**
- Create: `trials/2026-08-writing-style/results/trial-data.md`

**Interfaces:**
- Consumes: human reviewer's general impressions and ranking from Task 3
- Produces: trial results with adoption decision

- [ ] **Step 1: Record impressions and ranking**

After the human reviewer provides general impressions for each letter group and a ranking, unblind the results. Write `results/trial-data.md` with:
- The blind key mapping
- Each condition's general impression (quoted from reviewer)
- The ranking (best to worst)
- The reviewer's adoption judgment (provided while still blind, before unblinding)
- Tie-break: if multiple conditions are comparable, the simpler one (fewer rules) wins

- [ ] **Step 2: Commit results**

```bash
git add trials/2026-08-writing-style/results/trial-data.md
git commit -m "feat: writing style trial — results and adoption decision"
```

- [ ] **Step 3: Apply graduating condition (conditional)**

If a condition graduated: copy its style instruction file from `conditions/` to `skills/writing-style.md`, replacing the current content. This is the exact style instruction that was tested — no modifications. Commit the change.

If no condition graduated (negative result), skip this step.

- [ ] **Step 4: Commit adoption (conditional)**

```bash
git add skills/writing-style.md
git commit -m "feat: adopt graduating writing style condition for Soul"
```
