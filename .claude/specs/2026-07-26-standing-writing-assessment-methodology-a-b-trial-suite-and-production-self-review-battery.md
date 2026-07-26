---
type: spec
title: 'Standing writing-assessment methodology: A/B trial suite and production self-review
  battery'
description: 'Two-part assessment system: a standing A/B testing suite (trials/METHODOLOGY.md)
  generalized from the 2026-07 writing-doctrine trial, and an automated self-review
  battery for the production character-card workflow, connected by a graduation rule:
  a mechanism ships in production only after the suite validates it.'
tags:
- complete
date: 2026-07-26
timestamp: 2026-07-26T15:25Z
resources:
- '[[2026-07-17-resource-review-world-forge-multi-agent-world-pipeline]]'
- '[[2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3]]'
- '[[2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja]]'
---

# Standing writing-assessment methodology: A/B trial suite and production self-review battery

## Context

This spec graduates two inbox items: the World-Forge audit patterns and dilemma test for trial methodology (2026-07-25T17:20), and the cross-model convergence metric with its validation constraints (2026-07-25T15:10). Sources: the [World-Forge resource review](../research/2026-07-17-resource-review-world-forge-multi-agent-world-pipeline.md), the [Hoplight / Character Builder v3 review](../research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md) (items 2 and 3), and the [2026-07-23 blind-trial results](../research/2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md).

**Two goals, distinguished deliberately.** They share mechanisms but are not the same system:

1. **The A/B testing suite** — internal. Tests methodologies or inputs against each other (the 2026-07 writing-doctrine trial, generalized into standing form). Exists to optimize goal 2.
2. **The production self-review battery** — the automated checks inside the character-card generation workflow that plugin users ultimately run. Shipped skill prose.

The suite is how a self-review mechanism earns its place in production; mechanisms flow from 1 to 2, never the reverse.

**Why now.** The 2026-07-23 trial exposed the central weakness: the mechanical metrics were not merely weak but misleading — independent agent graders scored all six notes near-identically and their preference ranking inverted the human one (agent's #6 was the human's #1). Everything in the trial kit is also specific to that one trial; no trial-independent methodology exists anywhere. Both problems are addressed here.

**Scope boundary (refines the 2026-07-25 decision).** Full or real play sessions are out: side-by-side live play comparison has too many uncontrolled variables and too much cost. But *simulated* play probes are in, provided they are self-contained and require no human input to run. Assessment reads notes and probe outputs generated from them. Humans may grade, but the system is designed to need as little human intervention as possible.

**Cheapness bar** (decided this session): a test is cheap if it runs without a human and stays under O(n²) in cast or content size.

## Decisions

### D1. Home: `trials/METHODOLOGY.md`

The standing methodology is a repo document next to the trial kits, versioned with the code it governs. Future kits instantiate it; the 2026-07 kit's README, brief-procedure, and rubric remain as that trial's instance. Vault documents record decisions; the methodology itself lives where a trial builder will find it.

### D2. Part 1 — the A/B testing suite

`trials/METHODOLOGY.md` generalizes the 2026-07 kit and adds the adopted audit patterns:

- **Trial protocol** (generalized from the kit): capture one brief via the normal authoring flow; build one packet per arm; generate each arm's output with a fresh agent seeing only its packet and the brief; grade blind against a rubric; decode the arm key only after all cells are filled.
- **Probe design taxonomy — scenario classes.** Probes are designed across six classes, restated as note-interrogation and simulated-probe classes (not live play): on-script, trigger collision, near-miss/false trigger, off-script pressure, coverage-void, and lull. A probe set that covers only the happy path is not a probe set.
- **Process rule — cold-read author/grader separation.** Whoever authors probe material pre-commits the expected failure and works without the answer key in view; grading happens separately, afterward. In agent terms: author-agent and grader-agent run in separate contexts. Material written to pass its own audit verifies nothing. (Adopted as critical.)
- **Metric-validation principle.** Every agent-run metric is validated *individually* against human judgment on the same material before it is trusted — a blind comparison of AI and human assessment of that one metric, not of a whole trial result. A metric that has not passed this is labeled unvalidated wherever its numbers appear. This is the standing correction for the 2026-07-23 inversion.
- **Cross-model convergence metric.** Generate the same section from two models; flag sentences produced identically or near-identically, on the rule that cross-model agreement marks a sentence as the model's voice rather than the author's. Requires paired generations, which existing packets do not have.

### D3. Convergence-metric validation path

Define now; pilot same-family now; confirm cross-provider later.

1. **Pilot (same-family):** regenerate the six 2026-07-23 arms under two different Anthropic-family model tiers, compute arm-level convergence, and correlate against the existing human preference ranks. Same-family agreement is a weaker signal (shared training makes convergence likely for reasons other than model voice), so the pilot is read as a relative measure across arms and can only *disqualify* or *provisionally support* the metric.
2. **Confirmatory (cross-provider):** rerun when cross-provider agent access lands (planned; fleet cross-provider thread). Only this pass can flip the metric to validated.

The metric carries unvalidated status until step 2 passes.

### D4. Part 2 — the production self-review battery

Defined here at mechanism level only; no `skills/` edits happen under this spec. The battery, as designed:

- **Dilemma test + anti-convergence probe.** One scenario pits the character's top value against common decency; the note alone must answer it — if the author had to decide, motive content is underwritten. Then run the same dilemma past the character this one was declared to be built against; answers must differ in substance, not accent. O(1) per note. The RoleCDE caveat carries: prompting-level mitigation is expected to be partial, so this test verifies rather than assumes the value-conflict material works.
- **Blind-line voice test, scatter-shot form.** Strip speaker names from probe-generated dialogue samples; an agent classifies lines to speakers, scored mechanically as accuracy. For large casts, sample random NPC collections rather than the full pairwise matrix (the O(n²) distinctiveness matrix is explicitly demoted, not adopted).
- **Counterfactual probe / not-binding verdict.** A PASS cites both the output line and the note line that compelled it, then asks whether that note line would equally permit the failing version; if yes, the verdict is "present but not binding" and the fix is directive language or a context qualifier. Flagged validation-pending for agent execution — it is the most judgment-laden mechanism here.
- **Convergence check** — enters the battery only if D3 validates it.

Constraints on everything in this battery: model-neutral prose (no product names in shipped text), self-contained (runs with no human input), human grading optional and minimized, bounded cost per card.

### D5. The graduation rule

A mechanism ships in the production battery only after the A/B suite has validated it under the D2 metric-validation principle. Today every Part 2 mechanism is **designed, pending validation** — nothing touches shipped skill prose yet. Adopting a mechanism ahead of measured data remains possible but is an explicit human call recorded at the time (as with the 2026-07-25 additive-doctrine adoption), never a default.

### D6. Non-goals

- Full or real play sessions, human-driven session testing, or grading live user behavior. Behavioral evidence arrives later as uncontrolled user feedback, which is not a trial arm.
- AI detectors (Pangram, GPTZero) — rejected; they measure whether prose fools a human-oriented detector, irrelevant to a note written for a model to read.
- The full cross-NPC distinctiveness matrix — replaced by scatter-shot sampling.
- Implementing the production battery in `skills/` — follow-on work gated by D5.

## Consequences

- **Deliverable of the implementation plan:** `trials/METHODOLOGY.md` containing the D2 suite, the D3 validation plan, the D4 battery designs with their validation status, and the D5 graduation rule. The 2026-07 kit stays untouched as the first instance.
- **Follow-on work, not in this spec:** running the D3 pilot; running per-metric validation for the counterfactual probe; integrating validated mechanisms into the production workflow.
- **Success criteria:** a future trial can be designed from METHODOLOGY.md alone without re-deriving process rules; every metric in use carries an explicit validated/unvalidated label; the internal/shipped boundary and graduation rule are stated in one place.
- On approval, inbox items 6 (2026-07-25T17:20) and 9 (2026-07-25T15:10) are deleted as graduated into this spec.
