# Convergence Metric Retest — Results

Date: 2026-08-09

## Pre-check: Value-Conflict Stance Effectiveness

Tested with 4 agents (sonnet-tier), each playing one character in one
condition (with/without stance entry) across 2 dilemma scenarios. Agents
unaware of comparison.

**Result: Pass.** Stance entry shows measurable behavioral influence in
3/4 scenarios (clear in 2, moderate in 1, subtle in 1). Primary effect:
specifying the behavioral channel for value-conflict — how guilt
manifests, what triggers exceptions, whether the operating code actively
engages or gets deflected. Without the entry, models default toward
alignment-consistent behavior.

## Generation

Models used: Claude Opus 4.6 (via builder dispatch), GPT-5.6 Sol, GPT-5.6 Terra.
Characters: Kallya, Nadja.
Pipeline: Full Pipeline v2 flow (deslop/deframe, route annotation, structured
doctrine, 3-variant spread, synthesis).
Output: 6 files in `out/` (2 characters x 3 models), 15-27K bytes each.

## Detection Results

### Input Echo

| Character | Model | Total entries | Input echo | Clean |
|-----------|-------|:---:|:---:|:---:|
| Kallya | Sonnet | 25 | 1 | 24 |
| Kallya | Sol | 26 | 0 | 26 |
| Kallya | Terra | 25 | 0 | 25 |
| Nadja | Sonnet | 24 | 0 | 24 |
| Nadja | Sol | 24 | 0 | 24 |
| Nadja | Terra | 22 | 0 | 22 |
| **Total** | | **146** | **1** | **145** |

Input echo rate: 0.7% (down from 61% in original experiment).

### Cross-Model Convergence

| Character | Cross-provider rate | Within-family rate | Delta |
|-----------|:---:|:---:|:---:|
| Kallya | 15.8% | 25.0% | -9.2 |
| Nadja | 17.1% | 11.4% | +5.7 |

Direction inconsistent across characters. No 10-point delta achieved.

### Within-Model Convergence

Sonnet variant spreads: 37 groups parsed, 0 low-divergence. All 3-variant
spreads diverged successfully. GPT variant format not parseable (different
output structure).

### Human Review of Convergence Findings

51 total convergence findings (31 Kallya, 20 Nadja) reviewed by entry-pair
inspection. Overlap scores ranged 0.25-0.41 (threshold 0.25), mostly
borderline.

**Finding: convergence is on shared factual content, not slop.**

- Background facts (same events described by multiple models) account for
  the majority of findings. Expected similarity.
- Body/physical descriptions converge on factual characteristics. Expected.
- Doctrine entries (core want, core fear, value-conflict stance) converge
  because they derive from the same structured input. Expected.
- Behavioral Soul entries show the LEAST convergence — the creative,
  slop-susceptible content diverges well across models.

Precision for slop detection: near zero. The metric correctly identifies
convergent text but cannot distinguish legitimate factual similarity from
generic filler.

## Graduation Assessment

### Criterion Results

| Criterion | Threshold | Result | Pass? |
|-----------|-----------|--------|:---:|
| Precision | >61% TP on filtered findings | ~0% (findings are factual similarity, not slop) | No |
| Cross-provider signal | 10-point delta, consistent | Inconsistent direction across characters | No |
| Correction value | >50% improving | Not assessed (no true-positive slop findings to correct) | N/A |
| Within-model signal | >50% TP on low-divergence flags | 0 findings (no low-divergence detected) | Pass (trivially) |
| Consistency | Same verdict both characters | Cross-provider direction disagrees | No |

### Graduation Decisions

| Component | Verdict | Rationale |
|-----------|---------|-----------|
| Input-echo detection | **Graduate** | 0.7% echo rate, down from 61%. Pipeline v2 solved the problem upstream. |
| Within-model divergence check | **Graduate** | Zero marginal cost (built into 3-variant spread). 0 false positives. The spread's divergence rule is both detection and prevention. |
| Cross-model convergence | **Do not graduate** | Cannot distinguish factual similarity from slop. Precision near zero for slop detection. Adds multi-model generation cost without reliable signal. |
| Full grader mechanism | **Partial graduation** | Restructure around input-echo detection + within-model divergence only. Drop cross-model convergence requirement. |

### What Pipeline v2 Actually Solved

The original experiment's 61% input-echo problem is gone. The remaining
"convergence" is legitimate — models describing the same character facts
with natural phrasing overlap. This is a good outcome: Pipeline v2 produces
output that is character-specific and does not converge on generic filler.

The convergence detection concept (compare across models to find slop) was
the wrong tool for this problem. The right tools were already in the
pipeline: input-echo detection at the entry level, and the divergence check
built into the 3-variant spread. Both are zero-marginal-cost and work.
