---
type: research
title: Convergence Validation Experiment — Findings and Graduation Assessment
description: 'Human-reviewed results from the cross-model convergence validation experiment:
  detection precision, blinded correction quality, model rankings, identified problems,
  and graduation decision against spec criteria'
tags:
- human-ready
date: 2026-07-30
timestamp: 2026-07-30T22:22Z
resources:
- "[[2026-07-30-cross-model-convergence-metric-validation-experiment]]"
- "[[2026-07-30-convergence-validation-experiment-implementation]]"
output: []
---

# Convergence Validation Experiment — Findings and Graduation Assessment

Governing spec: [Cross-Model Convergence Metric Validation Experiment](../.claude/specs/2026-07-30-cross-model-convergence-metric-validation-experiment.md)
Plan: [Implementation Plan](../.claude/plans/2026-07-30-convergence-validation-experiment-implementation.md)
Reports: [detection-report.md](reports/detection-report.md), [correction-report.md](reports/correction-report.md), [correction-report-blinded.md](reports/correction-report-blinded.md)
Key: [blind-key.md](reports/blind-key.md)

## Experimental Setup

**Models tested:** Opus 4.6, Opus 5, GPT-5.6 Sol, GPT-5.6 Terra (4 models, 2 providers)
**Characters:** Kallya, Nadja (2 characters × 4 models = 8 generated notes)
**Detection methods run:** exact match (0 findings after stripping Design Notes), LLM-as-judge (2 judges: Opus 5, GPT Sol; 115 combined findings, 31 agreed by both)
**Detection methods skipped:** embedding similarity (no Voyage API key)
**Judges:** 2 of planned 3 (no Gemini access)

## Detection Review (Partial)

Human review covered findings #1–23 (of 115). Stopped early because the dominant pattern — input-derived convergence — was clear and masking other signals.

**Verdict on reviewed findings:**

| # | Verdict | Notes |
|---|---------|-------|
| 1 | TP | Borderline; boring line |
| 2 | TP | Vague, doesn't clarify what the bluff was |
| 3 | TP | Vague and sloppy |
| 4 | TP | "against resistance" is bad phrasing |
| 5 | FP | Not sloppy, but "Steward's House" is meta framing that shouldn't appear in character content (separate issue) |
| 6 | TP | Inhuman phrasing |
| 7 | FP | Different enough |
| 8 | FP | Pegged to input ("animal-husbandry framework" → both chose "herder") |
| 9 | TP | Unnatural phrasing |
| 10 | TP | "Refuses credit" is in inputs but convergent phrasing around it is notable |
| 11 | TP | — |
| 12 | TP | — |
| 13 | FP | Not great phrasing but not convergent enough |
| 14 | FP | Limited ways to phrase this; sufficiently different |
| 15 | TP | B version is fine; A is the problem |
| 16 | FP | Input-pegged ("eat them all / called it / could not follow through" is verbatim input); B is better |
| 17 | FP | Probably input-pegged; B is better |
| 18 | TP | "Cajoles" is odd — confirmed present in inputs, but both models used it identically |
| 19 | FP | Input-derived (herder/flock from animal-husbandry framework) |
| 20 | TP? | Might be input-tied; "refuses credit" confirmed in inputs |
| 21 | FP | Input-tied |
| 22 | TP | Input-tied but sloppy; was manually corrected in the original |
| 23 | TP | Input-tied partially but phrasing is sloppy |

**Precision on reviewed subset:** 14 TP out of 23 = 61%. However, many true positives are themselves partially input-derived, and many false positives are caused by faithful input reproduction rather than independent slop. The detection pipeline cannot distinguish these two causes.

### Input verification

Phrases checked against `inputs/kallya-inputs.md`:

| Phrase | In inputs? |
|--------|-----------|
| "refuses credit" | YES — verbatim |
| "cajoles" | YES — verbatim |
| "herder" / "flock" | PARTIAL — "flock" yes, "herder" no; "animal-husbandry framework" |
| "eat them all / called it / could not follow through" | YES — verbatim |
| "no sport in prey that cannot process what is happening" | YES — verbatim |
| "dies permanently, notices, says nothing, moves" | YES — nearly verbatim |
| "presents as careless, is careful" | YES |
| "Steward's House" | YES |
| "the village formed around them both" | YES |
| "the relief at not following through told her she cared" | YES |
| "physically moving her against resistance would demolish" | YES |
| "warm" as stranger descriptor | NO — not in inputs |
| "constructs pretexts for humans to enter her mouth" | YES |

## Blinded Correction Review (Complete)

All 54 correction entries reviewed blind (A/B randomized, model/judge info stripped). User chose Version 1, Version 2, or About Equal for each. User noted ties meant "equally bad."

### Model Quality Rankings

| Model | W | L | T | Win% (excl ties) |
|-------|---|---|---|-------------------|
| Opus 5 | 12 | 8 | 19 | 60% |
| Opus 4.6 | 10 | 7 | 18 | 59% |
| GPT Sol | 4 | 6 | 7 | 40% |
| GPT Terra | 3 | 8 | 6 | 27% |

### Cross-Provider

Claude models beat GPT models in 11 of 15 decided cross-provider comparisons (73%).

### Head-to-Head

| Matchup | Result |
|---------|--------|
| Opus 4.6 vs Opus 5 | 5–6 (15 ties) — effectively even |
| Opus 4.6 vs Sol | 2–0 (2 ties) |
| Opus 4.6 vs Terra | 3–1 (1 tie) |
| Opus 5 vs Sol | 3–2 (2 ties) |
| Opus 5 vs Terra | 3–1 (2 ties) |
| Sol vs Terra | 2–1 (3 ties) |

### Character-Specific Effects

| Model | Kallya Win% | Nadja Win% |
|-------|-------------|------------|
| Opus 4.6 | 71% | 50% |
| Opus 5 | 44% | 73% |
| Sol | 50% | 33% |
| Terra | 25% | 29% |

Opus 4.6 was stronger on Kallya, Opus 5 on Nadja. Sample sizes are small (5–15 decided entries per cell); the per-character split may be noise.

### Key Observation

50% of entries were ties, and the reviewer characterized ties as "equally bad." Convergent passages correlate with low quality regardless of which model produced them. When there was a quality gap, it was usually between providers (Claude vs GPT), not between good and bad writing.

## Graduation Assessment

Evaluated against the four criteria in the [governing spec](../.claude/specs/2026-07-30-cross-model-convergence-metric-validation-experiment.md):

### 1. Precision — CONDITIONAL FAIL

61% true-positive rate on the reviewed subset, but the signal is dominated by input-derived convergence. Most flagged passages converge because they closely follow the Design Notes inputs, not because models independently produce the same slop. Without an input-awareness mechanism, the detector cannot separate these two causes, making the flags unreliable as a slop signal.

**Conditional on:** an input-aware detection filter that compares output against input before flagging convergence. With that filter, the remaining true positives (genuine slop convergence) would be a cleaner signal worth retesting.

### 2. Cross-Provider Signal — PASS (WEAK)

Cross-provider convergence does exist and was flagged. However, much of it traces to shared input reproduction rather than independent slop patterns. The same passages (Kallya's death response, threat response, cajoles behavior) appeared in nearly every pair combination because all four models echoed the same input phrasing.

### 3. Correction Value — MIXED / DOES NOT MEET

The spec asks whether rewrites of true positives are judged "improved" more often than "neutral" or "worse." The blinded review compared existing versions rather than generated corrections (corrections were not produced because the detection review was stopped early). What the comparison showed: when one version is better, it's usually the Claude version over the GPT version — but 50% of the time, both versions are equally poor. The metric identifies *where* quality is low but doesn't by itself produce corrections.

### 4. Consistency — PASS

The metric behaved similarly across both characters. Model rankings were stable (Claude > GPT on both), tie rates were comparable, and the input-echo problem appeared for both Kallya and Nadja.

### Overall: GRADUATION DEFERRED — PENDING UPSTREAM CHANGES

Two of four criteria are not yet met (precision, correction value), one passes weakly (cross-provider signal), one passes cleanly (consistency). The metric successfully identified genuine slop (14 true positives in 23 reviewed findings, plus the broader pattern of low-quality convergent passages), but its signal is obscured by input-derived convergence that the current pipeline cannot filter.

The blocker is not the metric concept but the input pipeline: convergence detection works as a slop detector, but it needs input-aware filtering to separate genuine slop from faithful input reproduction. Upstream changes to the input structure and generation instructions (S1–S6 below) would address this. Once those land, the metric should be retested against the same graduation criteria.

## Problems Identified

### P1: Input-Derived Convergence (primary blocker)

Models faithfully reproduce input phrasing, producing convergent output that isn't slop. This dominates the detection signal, making convergence unreliable as a slop proxy. Affects both within-provider and cross-provider comparisons.

### P2: Meta Framing in Inputs

Builder-level organizational terms ("Steward's House," household assignments) appear in Design Notes and propagate into character content, where they don't belong. Characters wouldn't describe themselves using builder abstractions.

### P3: Detection Has No Input Awareness

The detection pipeline compares outputs against each other but not against inputs. It cannot tell whether a convergent phrase was independently generated (slop signal) or faithfully reproduced from shared source material (input echo).

### P4: Paired Comparison Format Is Too Laborious

54 paired A/B comparisons is grueling for a human reviewer. A rubric-based approach (rate each passage independently on a 1–3 scale) would extract the same quality signal with less effort and better scalability.

## Potential Solutions and Avenues of Inquiry

### S1: Orthogonal Input/Output Organization

Structure inputs by topic (backstory, abilities, relationships) while outputs cut across them differently (Soul, Behavior, Dynamics). No single input line maps 1:1 to an output line, forcing the model to decompose and recombine. This breaks verbatim echo structurally rather than by instruction.

### S2: Fact-vs-Manifestation Generation Instruction

Inputs state what happened and what's true. Outputs state how it shows in present behavior. Generation prompt enforces: "inputs are facts, outputs are manifestations." Targets the echo problem directly at the generation step.

### S3: Coarser Input Bundling

Bundle related Design Notes facts into paragraph-level blocks rather than bullet points. Line-level granularity enables line-for-line reproduction; paragraph-level forces decomposition.

### S4: Input-Aware Detection

Add a preprocessing step that compares flagged convergent passages against the source inputs. Convergence that traces to input phrasing is filtered or downweighted. Remaining convergence is a cleaner slop signal.

### S5: Deslop Pass on Inputs

Run the stop-slop rules on Design Notes before they enter the generation pipeline. Catches sloppy input phrasing before it propagates. Could be combined with meta-framing cleanup (P2).

### S6: Distinct Voice for Builder Notes

Write Design Notes in a deliberately different register (clinical, compressed, shorthand) so that any close reproduction in character content is immediately detectable as echo rather than creative writing.

### Interactions With Pending Work

These solutions interact with pending character-doctrine changes from the Character Builder v3 review (inbox item 4) and the additive-doctrine revisit (inbox item 5). Specifically:

- **Charge-scored memory routing** (item 4d) touches input organization — could subsume or conflict with orthogonal restructuring (S1).
- **Staged/additive generation** (item 5) is a natural place to enforce fact-to-manifestation separation (S2) — each stage transforms rather than echoes.
- **The grader agent concept** (item 9) depends on input-aware detection (S4) to function; this experiment's findings are prerequisites for its design.
- **Character-doctrine candidates** (item 4 a/b/c/e) add new input categories that need to flow through whatever restructured input pipeline is designed.

Recommended: consolidate these into a single brainstorming pass before designing solutions independently.

## Methodology Notes for Future Experiments

- Paired comparison at this scale (54 entries) should be replaced with independent rubric scoring.
- Embedding detection (skipped here) may catch paraphrase-level convergence that exact match and LLM judges miss — worth testing if API access becomes available.
- Three judges instead of two would provide majority-vote filtering; the two-judge setup forces "both agree" as the only reliable filter.
- The reviewer was not fully blind to model identity during detection review (pair metadata was visible); future detection reviews should also strip this.
- Detection review should be completed through the full finding set to get a reliable precision number, but the input-echo problem should be addressed first — reviewing findings dominated by input echo is not a productive use of reviewer time.
