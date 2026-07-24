---
type: research
title: Writing-Doctrine Blind Trial Results (Viralys, Nadja)
description: Results of the 2x3 blind A/B trial crossing stopslop vs current style
  with current/additive/tensions doctrine, run on the Nadja character note in the
  Viralys project
tags:
- human-ready
date: 2026-07-23
timestamp: 2026-07-23T02:03Z
resources: []
---

# Writing-Doctrine Blind Trial Results (Viralys, Nadja)

## Goals

Determine whether stopslop style and/or additive/tensions doctrine
settings improve Wide-phase character note quality, measured by blind
scoring and human qualitative assessment.

## Trial design

Blind A/B/.../F trial crossing two axes:

- **Style axis (2 levels):** stopslop vs current
- **Doctrine axis (3 levels):** current, additive, tensions

Six cells, one packet per combination, each generating a full character
note for the same character (Nadja, fox-giantess kitchen forewoman) from
the same frozen brief. Packet-to-arm assignment randomized and
base64-encoded; decoded only after all scoring complete.

| Packet | Style | Doctrine |
|---|---|---|
| packet-1 | stopslop | additive |
| packet-2 | stopslop | current |
| packet-3 | current | current |
| packet-4 | stopslop | tensions |
| packet-5 | current | tensions |
| packet-6 | current | additive |

## Results

### Scores

| Packet | Style | Doctrine | BS (1-5) | St (1-5) | Li (1-5) | TW | Slop | Cov (n/4) | Length | Agent rank | Human rank |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | stopslop | additive | 4 | 4 | 5 | 0 | 2 | 3/4 | 1427 | 6 | **1** |
| 2 | stopslop | current | 5 | 4 | 5 | 0 | 0 | 3/4 | 1503 | 5 | ~2 |
| 3 | current | current | 4 | 4 | 5 | 0 | 1 | 4/4 | 1743 | 3 | below 1 |
| 4 | stopslop | tensions | 4 | 4 | 5 | 0 | 0 | 4/4 | 1750 | **1** | below 1 |
| 5 | current | tensions | 5 | 4 | 5 | 0 | 2 | 4/4 | 1591 | 2 | below 1 |
| 6 | current | additive | 4 | 4 | 5 | 0 | 1 | 4/4 | 1650 | 4 | below 1 |

BS = Behavioral specificity, St = Stageability, Li = Liveliness, TW =
Trait-word leakage, Slop = Slop density, Cov = Coverage.

Scoring method: six independent agents (one per note, no cross-note
contamination), forced ranking by a seventh agent. Human qualitative
ranking performed independently before seeing agent scores.

### Style axis: stopslop vs current

Slop density directionally lower in stopslop arms (total 2 vs 4; one
stopslop hit borderline per human review). Trait-word leakage 0 across
both. Craft scales identical. Consistent with expectation: surface
normalization works, craft unchanged.

**Decision:** Weak positive for stopslop. Insufficient signal alone;
feeds the stopslop-vs-humanizer comparison as one data point.

### Doctrine additive step: current vs additive

Indistinguishable on craft scales and coverage. Human preferred one
additive arm (packet-1) but not the other (packet-6).

**Decision:** No fold-in earnable from this trial.

### Doctrine tensions step: additive vs tensions

Indistinguishable on all measured criteria.

**Decision:** Reject both tension calls (hook exemption, anchor
repetition) — unnecessary complexity per pre-registered bar.

### Interactions

None visible. Human preference for packet-1 (stopslop+additive) does
not generalize to other stopslop or additive arms — likely execution
variance.

## Methodological findings

### LLM-judge ceiling confirmed

Independent agent scoring gave all six notes Liveliness 5 and
Stageability 4 — unable to discriminate where the human found clear
quality differences in prose, body, and soul quality. Agent ranking
inverted human ranking completely (agent's #6 was human's #1).

**Implication:** do not use LLM judges as sole evaluator for character
note quality. Human qualitative assessment is the binding signal; LLM
scoring is useful only for surface counts (slop, trait-word leakage)
and structural coverage checks.

### Relationship label misapplication (systematic)

All six notes consistently misoriented relationship role labels:

- Strelitzia labelled "Authority" — should be "Charge" (Nadja is the
  authority figure, Liza is the charge)
- Ataraxia labelled "Obligation" — inaccurate framing
- "Ideological Counterpart" misused in several cases

The orientation is backwards: the label describes the other character's
role relative to the subject, not the subject's role relative to them.
Packet-level/instruction-level issue (all six arms did it). The
relationship label instructions in the generation packets need
revision.

### Coverage gaps are noise

Packets 1 and 2 both omitted Jaro Jerab (Coverage 3/4). Both are
stopslop arms; the omission is random.

## Scope and limitations

- One character per cell — all conclusions provisional until replicated
  on a second character.
- Human ranking partial: Note 1 clearly first, remaining five not fully
  rank-ordered.
- Trial tests doctrine settings, not the generation model or
  temperature (held constant).

## Source files

Trial materials in the Viralys project at `scratch/trial/`: brief.md,
packet-1.md through packet-6.md, out/note-1.md through out/note-6.md,
rubric.md (full results record), key.md (encoded arm map).
