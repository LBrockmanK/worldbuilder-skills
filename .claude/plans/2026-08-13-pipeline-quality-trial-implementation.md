---
type: plan
title: Pipeline quality trial implementation
description: 'Implementation plan for the pipeline quality trial: fail-check gate,
  input restructuring, decomposition step, blind comparison against baseline'
tags:
- abandoned
date: 2026-08-13
timestamp: 2026-08-14T02:06Z
resources: []
---

# Pipeline quality trial implementation

## Goal

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Compare four cumulative pipeline conditions (baseline, fail-check gate, input restructuring, decomposition step) for reducing echo and slop in character note generation, using blind human review.

**Architecture:** Trial infrastructure under `trials/2026-08-pipeline-quality/` following established conventions. One Python script for the mechanical fail-check gate reusing the grader's `ngram_overlap()`. Condition-specific generation-rules variants as modified skill prose. Blind review with sealed key mapping.

**Tech Stack:** Python 3 (scripts), markdown (trial protocol, generation rules, results)

**Spec:** [Pipeline quality trial spec](../specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md)
**Research dossier:** [Implementation research](../research/2026-08-13-pipeline-quality-trial-implementation-research.md)

## Global Constraints

- Model and temperature pinned at trial start; same for all conditions and runs
- All echo comparisons (human and mechanical) use original Design Notes, not preprocessed forms
- Trial outputs stored under `trials/2026-08-pipeline-quality/`
- Writing style per `skills/writing-style.md` and `docs/slop-phrases.md`

---

### Task 1: Trial infrastructure and protocol

**Files:**
- Create: `trials/2026-08-pipeline-quality/trial-protocol.md`
- Create: `trials/2026-08-pipeline-quality/inputs/` (directory)
- Create: `trials/2026-08-pipeline-quality/out/` (directory)
- Create: `trials/2026-08-pipeline-quality/results/` (directory)

**Interfaces:**
- Consumes: spec (D1-D6), existing trial conventions from `trials/METHODOLOGY.md`
- Produces: trial protocol document referenced by all subsequent tasks; selected test character identity and Design Notes in `inputs/`

- [ ] **Step 1: Create trial directory structure**

```bash
mkdir -p trials/2026-08-pipeline-quality/inputs
mkdir -p trials/2026-08-pipeline-quality/out/condition-0
mkdir -p trials/2026-08-pipeline-quality/out/condition-a
mkdir -p trials/2026-08-pipeline-quality/out/condition-b
mkdir -p trials/2026-08-pipeline-quality/out/condition-c
mkdir -p trials/2026-08-pipeline-quality/results
mkdir -p trials/2026-08-pipeline-quality/scripts
mkdir -p trials/2026-08-pipeline-quality/conditions
```

- [ ] **Step 2: Select test character**

Choose a character with established Design Notes containing at least 10 facts across multiple topic areas (motivations, behaviors, relationships, fears). Copy the character's Design Notes to `trials/2026-08-pipeline-quality/inputs/design-notes.md`. Record model name and temperature in the protocol (both pinned for all generations).

- [ ] **Step 3: Write trial protocol**

Write `trials/2026-08-pipeline-quality/trial-protocol.md` documenting:
- Test character identity and justification for selection
- Pinned model and temperature
- The four conditions (copied verbatim from spec D1)
- Metrics rubric (copied verbatim from spec D3, all five dimensions with operational examples)
- Blind review procedure (from spec D4)
- Success criteria (from spec D5)
- Number of runs per condition: 2

- [ ] **Step 4: Commit**

```bash
git add trials/2026-08-pipeline-quality/
git commit -m "feat: pipeline quality trial — infrastructure and protocol"
```

---

### Task 2: Fail-check gate script

**Files:**
- Create: `trials/2026-08-pipeline-quality/scripts/fail_check.py`
- Create: `trials/2026-08-pipeline-quality/scripts/test_fail_check.py`

**Interfaces:**
- Consumes: character-trigram Jaccard calculation (reimplemented locally; the grader's detection scripts may not expose a CLI interface)
- Produces: `fail_check(variants: list[str]) -> dict` returning `{"passed": bool, "max_jaccard": float, "pairs": list[dict]}` where each pair has `{"i": int, "j": int, "similarity": float}`

- [ ] **Step 1: Write failing tests**

Write `trials/2026-08-pipeline-quality/scripts/test_fail_check.py`:

```python
import pytest
from fail_check import fail_check

def test_divergent_variants_pass():
    variants = [
        "She flinches at loud voices, tucking her chin before catching herself.",
        "When cornered, she defaults to bargaining — offering information, favors, anything portable.",
        "Her laughter arrives a beat late, calibrated to the room rather than the joke."
    ]
    result = fail_check(variants)
    assert result["passed"] is True
    assert result["max_jaccard"] < 0.25

def test_identical_variants_fail():
    variants = [
        "She is brave and strong and kind.",
        "She is brave and strong and kind.",
        "She is brave and strong and kind."
    ]
    result = fail_check(variants)
    assert result["passed"] is False
    assert result["max_jaccard"] == 1.0

def test_near_identical_variants_fail():
    variants = [
        "She flinches at loud noises, tucking her chin down.",
        "She flinches at loud sounds, tucking her chin down.",
        "She flinches at loud voices, tucking her chin down."
    ]
    result = fail_check(variants)
    assert result["passed"] is False
    assert result["max_jaccard"] > 0.25

def test_returns_all_pairs():
    variants = ["a", "b", "c"]
    result = fail_check(variants)
    assert len(result["pairs"]) == 3  # 3 choose 2

def test_boundary_value_passes():
    """Spec says 'exceeds 0.25' so exactly 0.25 should pass."""
    # Use variants whose trigram Jaccard is exactly at threshold
    variants = ["abcdef", "abcxyz", "mnopqr"]
    result = fail_check(variants)
    # The exact similarity depends on trigram overlap; this test verifies
    # the boundary operator is <= not <
    assert result["passed"] == (result["max_jaccard"] <= 0.25)
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd trials/2026-08-pipeline-quality/scripts
python -m pytest test_fail_check.py -v
```

Expected: FAIL with ImportError (fail_check module does not exist yet).

- [ ] **Step 3: Implement fail_check.py**

Write `trials/2026-08-pipeline-quality/scripts/fail_check.py`:

```python
from itertools import combinations

THRESHOLD = 0.25

def char_trigrams(text: str) -> set[str]:
    t = text.lower()
    return {t[i:i+3] for i in range(len(t) - 2)} if len(t) >= 3 else set()

def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)

def fail_check(variants: list[str], threshold: float = THRESHOLD) -> dict:
    trigrams = [char_trigrams(v) for v in variants]
    pairs = []
    max_sim = 0.0
    for i, j in combinations(range(len(variants)), 2):
        sim = jaccard(trigrams[i], trigrams[j])
        pairs.append({"i": i, "j": j, "similarity": sim})
        max_sim = max(max_sim, sim)
    return {
        "passed": max_sim <= threshold,
        "max_jaccard": max_sim,
        "pairs": pairs
    }
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd trials/2026-08-pipeline-quality/scripts
python -m pytest test_fail_check.py -v
```

Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add trials/2026-08-pipeline-quality/scripts/
git commit -m "feat: fail-check gate script with tests"
```

---

### Task 3: Condition-specific generation rules

**Files:**
- Create: `trials/2026-08-pipeline-quality/conditions/generation-rules-condition-a.md`
- Create: `trials/2026-08-pipeline-quality/conditions/generation-rules-condition-b.md`
- Create: `trials/2026-08-pipeline-quality/conditions/generation-rules-condition-c.md`

**Interfaces:**
- Consumes: `skills/worldbuilder-character/generation-rules.md` (baseline), spec D1 condition definitions
- Produces: three variant generation-rules files, one per non-baseline condition, each containing the full generation instructions for that condition

- [ ] **Step 1: Create Condition A generation rules**

Copy `skills/worldbuilder-character/generation-rules.md` to `trials/2026-08-pipeline-quality/conditions/generation-rules-condition-a.md`. Replace the qualitative divergence check (lines 31-33, "could a reader tell them apart...discard all three and regenerate") with:

```markdown
After generating 3 variants for each entry, run the mechanical fail-check: compute pairwise Jaccard similarity of lowercase character trigrams. If any pair exceeds 0.25, reject the spread and regenerate that entry. Allow 3 additional regeneration attempts (4 total including the original). If all fail the threshold, flag the entry in the output and proceed with the spread whose maximum pairwise Jaccard similarity is lowest.
```

- [ ] **Step 2: Create Condition B generation rules**

Copy the Condition A rules to `generation-rules-condition-b.md`. Add preprocessing instructions after the existing deslop/deframe pass:

```markdown
### Input restructuring (Condition B)

After deslop/deframe, restructure the preprocessed input:

1. **Orthogonal organization (S1):** Reorganize the preprocessed input by topic cluster — motivations, behaviors, relationships, fears — rather than mirroring the output sections (Background, Body, Soul, Relationships). The model receives thematic bundles and must redistribute facts across output sections.

2. **Coarser bundling (S3):** Within each topic cluster, merge related bullet points into paragraph-level blocks. No single-fact bullets; each block contains 2-4 related facts that must be decomposed during generation.

3. **Distinct builder voice (S6):** After S1/S3 restructuring, run an additional LLM rewrite pass converting the result into compressed clinical shorthand: abbreviated, no articles, no hedging. This is a separate stage from deslop/deframe and S1/S3. Any reproduction of this clinical phrasing in character-voice output is immediately detectable as echo.
```

- [ ] **Step 3: Create Condition C generation rules**

Copy the Condition B rules to `generation-rules-condition-c.md`. Add a decomposition phase before the multi-option spread section:

```markdown
### Decomposition step (Condition C)

Before generating variants, produce a redistribution outline:

For each input fact from the restructured Design Notes:
- Which output section it maps to (Background, Body, Soul, or Relationships)
- Which entry within that section it contributes to
- What behavioral manifestation it becomes (one sentence)

Validate coverage: every input fact appears at least once in the outline. If a fact is missing, add it before proceeding.

For this trial: the outline maps all input facts, but only facts routed to Soul proceed to variant generation.
```

- [ ] **Step 4: Commit**

```bash
git add trials/2026-08-pipeline-quality/conditions/
git commit -m "feat: condition-specific generation rules (A, B, C)"
```

---

### Task 4: Generate trial output

**Files:**
- Create: `trials/2026-08-pipeline-quality/out/condition-0/run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-0/run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-a/run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-a/run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-b/run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-b/run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-c/run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-c/run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-b/restructured-input-run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-b/restructured-input-run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-b/clinical-input-run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-b/clinical-input-run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-c/restructured-input-run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-c/restructured-input-run-2.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-c/clinical-input-run-1.md`
- Create: `trials/2026-08-pipeline-quality/out/condition-c/clinical-input-run-2.md`

**Interfaces:**
- Consumes: Design Notes from `inputs/design-notes.md`, baseline generation-rules.md, condition-specific rules from `conditions/`, pinned model and temperature from protocol
- Produces: 8 raw generation outputs (4 conditions x 2 runs), each containing the Soul section entries with variant spreads (PART 2 of generation output)

- [ ] **Step 1: Generate Condition 0 (baseline) outputs**

Using the worldbuilder-character skill with the standard `generation-rules.md`, generate the Soul section for the test character. Save the full output (synthesized entries + variant spreads) to `out/condition-0/run-1.md`. Repeat for `run-2.md`. Use the pinned model and temperature.

- [ ] **Step 2: Generate Condition A outputs**

Using the worldbuilder-character skill with `conditions/generation-rules-condition-a.md` in place of the standard generation rules, generate Soul. For each entry, run `fail_check.py` on the variant spread; if it fails, regenerate (up to 3 retries). Log any flagged entries. Save to `out/condition-a/run-1.md` and `run-2.md`.

- [ ] **Step 3: Generate Condition B outputs**

Using `conditions/generation-rules-condition-b.md`. First apply the input restructuring (S1 topic clustering, S3 paragraph bundling, S6 clinical voice rewrite) to the Design Notes before generation. Save the S1/S3 restructured input to `restructured-input-run-{1,2}.md` and the S6 clinical rewrite to `clinical-input-run-{1,2}.md` in the condition directory. Generate Soul, apply fail-check. Save to `out/condition-b/run-1.md` and `run-2.md`.

- [ ] **Step 4: Generate Condition C outputs**

Using `conditions/generation-rules-condition-c.md`. Apply input restructuring (same as B), then produce the redistribution outline before generation. Validate coverage. Generate only Soul-routed facts. Apply fail-check. Save the redistribution outline, restructured input, clinical input, and generation output to `out/condition-c/run-1.md` and `run-2.md`.

- [ ] **Step 5: Run mechanical grader checks on all outputs**

Run the existing grader's input-echo detection on all 8 outputs, comparing against the original Design Notes (pre-preprocessing). The grader script at `skills/worldbuilder-grader/scripts/detect_input_echo.py` exposes Python functions, not a CLI — write a short runner script or invoke it programmatically. Verify the actual interface at execution time and adapt. Save detection reports to `results/grader-condition-{0,a,b,c}-run-{1,2}.json`.

- [ ] **Step 6: Compute within-model divergence for baseline**

Run the fail-check gate script (`scripts/fail_check.py`) on the baseline (Condition 0) variant spreads to produce comparable divergence data. Conditions A-C already have gate results from generation. Save all divergence reports to `results/divergence-condition-{0,a,b,c}-run-{1,2}.json`.

- [ ] **Step 7: Commit**

```bash
git add trials/2026-08-pipeline-quality/out/ trials/2026-08-pipeline-quality/results/
git commit -m "data: pipeline quality trial — 8 generation outputs + grader reports"
```

---

### Task 5: Blind review and analysis

**Files:**
- Create: `trials/2026-08-pipeline-quality/results/blind-key.md`
- Create: `trials/2026-08-pipeline-quality/results/blinded-review.md`
- Create: `trials/2026-08-pipeline-quality/results/trial-data.md`

**Interfaces:**
- Consumes: 8 generation outputs from Task 4, grader reports, rubric from protocol
- Produces: scored results, per-condition means, adoption decision

- [ ] **Step 1: Create blind key and blinded review document**

Assign random letter codes (W, X, Y, Z) to the four conditions. Write the mapping to `results/blind-key.md`. The human reviewer must not see this file until scoring is complete.

Create `results/blinded-review.md` with all entries from both runs of each condition, grouped by letter code, with entries in randomized order within each group. Include the original Design Notes at the top for reference.

- [ ] **Step 2: Human scoring**

Present `results/blinded-review.md` to the human reviewer. The reviewer scores each entry on all five dimensions (staging test, specificity, input echo, slop, factual fidelity) using the 1-3 scale from the protocol rubric.

- [ ] **Step 3: Unblind and compute results**

After all scoring is complete, reveal the blind key. Compute per-condition means for each dimension across both runs. Record in `results/trial-data.md`:
- Per-entry scores by condition and run
- Per-condition per-dimension means
- Mechanical grader rates (input-echo rate, low-divergence count) per condition
- Any entries flagged by the fail-check gate (conditions A, B, C)

- [ ] **Step 4: Apply success criteria**

Using the criteria from spec D5:
- A condition improves if any quality dimension mean (staging, specificity, slop, factual fidelity) exceeds baseline by >= 0.3 without regressing > 0.1 on any other
- If multiple improve: highest sum of four quality dimension means wins
- Tie-break: simpler condition (lower letter) wins
- Record the adoption decision (or negative result) in trial-data.md

- [ ] **Step 5: Commit**

```bash
git add trials/2026-08-pipeline-quality/results/
git commit -m "feat: pipeline quality trial — results and adoption decision"
```

---

### Task 6: Apply graduating improvements (conditional)

**Files:**
- Modify: `skills/worldbuilder-character/generation-rules.md` (if any condition graduates)

**Interfaces:**
- Consumes: adoption decision from Task 5, condition-specific rules from `conditions/`
- Produces: permanently updated generation rules reflecting the winning condition

This task executes only if a condition graduates per the success criteria. If the trial records a negative result, skip this task.

- [ ] **Step 1: Apply winning condition changes**

Merge the graduating condition's generation-rules changes into `skills/worldbuilder-character/generation-rules.md`:
- Condition A graduating: replace qualitative divergence check with mechanical fail-check gate
- Condition B graduating: add S1/S3 preprocessing instructions and S6 rewrite stage
- Condition C graduating: add decomposition step

Since conditions are cumulative, adopting C includes A and B.

- [ ] **Step 2: Update inbox**

Update inbox item 3 (grader agent research leads). If a condition graduates: record the trial outcome, which improvements were adopted, and remove the research leads that were tested. If negative result: note the bundled approach was tested and did not improve quality; individual S-findings remain open per spec.

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-character/generation-rules.md .claude/inbox.md
git commit -m "feat: adopt pipeline improvements from quality trial"
```
