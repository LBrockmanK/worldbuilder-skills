---
type: spec
title: Writing-doctrine blind-trial kit
description: 'Portable kit a worldbuilding project runs on one pending character:
  six-arm factorial blind trial (3 doctrine levels x 2 style rule sets) gating the
  stop-slop integration and the character-doctrine fold-in.'
tags:
- complete
date: 2026-07-11
timestamp: 2026-07-11T16:05Z
resources:
- '[[2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning]]'
- https://github.com/hardikpandya/stop-slop/
---

# Writing-doctrine blind-trial kit

## Context

Two doctrine changes are gated on blind trials (inbox, 2026-07-11), and both were decided to run as one combined exercise:

1. **stop-slop integration.** Whether the stop-slop rule set replaces or augments [writing-style.md](../../skills/writing-style.md) for any register. Working hypothesis from the evaluation session: three registers — Wide specs keep current doctrine, Export prose gets stop-slop plus a hook exemption, plugin-authoring prose uses stop-slop as a review checklist.
2. **Character-doctrine fold-in.** Which principles from the [causal-character-writing reference](../research/2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md) fold into the character skills, including the two tension calls (plain style vs sensory hooks; section discipline vs anchor repetition).

This spec defines the trial instrument: a portable kit handed to an actual worldbuilding project (a player vault built by `worldbuilder-setup`), run on one pending character from that project's cast plan. The kit is the deliverable of this work; running the trial and folding in results are follow-up work.

## Decisions

### Trial design: 2x3 factorial, six arms

Two axes, fully crossed. Six independent agents each write the same character from the same frozen brief, one arm each.

| Arm | Style rules | Character doctrine |
|---|---|---|
| 1 | writing-style.md (current) | Current (framework.md as shipped) |
| 2 | writing-style.md (current) | Current + additive principles |
| 3 | writing-style.md (current) | Current + additive + tension calls |
| 4 | stop-slop | Current |
| 5 | stop-slop | Current + additive principles |
| 6 | stop-slop | Current + additive + tension calls |

Doctrine levels:

- **Current:** the shipped character-note instruction set, unchanged.
- **+Additive:** adds the reference's non-conflicting principles — trait-word poisoning, knowledge boundaries, unresolved states, specification boundary, life in motion.
- **+Additive+Tensions:** additionally resolves both tension calls in the new direction — the emotional-memory-hook exemption to plain style is on, and anchor repetition across sections is allowed.

Evaluation is a flat six-way blind read by the user (decided over a staged pairwise read, accepting the risk that the small tensions delta is harder to see among six documents).

### Instruction packets

Six self-contained packets, one per arm, built in this repo during kit construction:

- Each packet is a complete character-note instruction set: note structure, section rules, writing rules, style rules, self-check. All six share identical document structure and wording except where an axis differs. The style axis swaps the style-rules block; the doctrine axis adds the doctrine blocks.
- The stop-slop style block is derived from the stop-slop repository during kit construction and rewritten into the same format as the current style block (rule + wrong/right example), so packet form does not leak which arm is which.
- Packets replace the installed skills for the trial: the running agent uses only its packet, the frozen brief, and read access to the project vault. It must not invoke or open any installed worldbuilding skill or style reference.
- Packets are model-neutral: no AI product or model names anywhere (CLAUDE.md rule; the kit leaves this repo).
- Packets instruct the agent to produce output that does not name its own rules, so the notes cannot self-identify their arm.
- Packet files carry neutral names (`packet-1.md` … `packet-6.md`). The packet-to-arm assignment is randomized once at kit build and recorded only in the sealed key (below), so neither the user nor the downstream orchestrator knows which cell a packet is.

### Character brief

- The downstream project picks one pending character from its cast plan and runs the normal Q&A session flow with the user, exactly as the shipped skill prescribes, through Session Notes capture. No note sections are written.
- The captured Session Notes transcript is frozen as `brief.md`. All six arms receive it verbatim.
- All arms get identical read access to the project vault (seed, direction, existing notes) for relationships and world grounding.
- Packets carry a no-questions rule: where the brief and vault are silent, the agent decides per its doctrine and moves on. Asking the user is not available, and invoking any of the project's installed worldbuilding skills to fill the gap is forbidden — that would contaminate the arm with the shipped doctrine.

### Output and blinding

- Each agent writes one complete character note body — Background, Body, Soul, Relationships, and Intimate Dynamics only if the character is flagged — to `out/note-<packet number>.md`. No Design Notes section; the brief is shared and would be identical.
- Because packet-to-arm assignment was shuffled at build, output filenames are already blind. The key file (`key.md`) maps packet numbers to arms, base64-encoded with a do-not-open warning, so an accidental glance does not unblind.
- The user reads and scores all six notes, records scores on the results sheet, and only then decodes the key.
- Rerun caveat: the shuffle is baked at build time. Rerunning the kit on another character reuses the same assignment; rebuild the kit for a fresh shuffle if the user has seen the key.

### Evaluation

Flat six-way blind read by the user against a fixed rubric. Per note:

- Behavioral specificity: entries describe enactable behavior, not labels (1–5).
- Stageability: a director could stage the sentences (1–5).
- Liveliness: the present state contains live, competing pulls a scene could pick up (1–5).
- Trait-word leakage: count of heavy trait adjectives of the poisoning class (count).
- Slop density: hits against [docs/slop-phrases.md](../../docs/slop-phrases.md) (count).
- Coverage: required elements present — contradiction, irrational behavior with root, self-image gap, relationship anchors (checklist).
- Length: word count (mechanical, recorded not scored).
- Overall preference: forced rank 1–6 across the six notes.

The rubric sheet doubles as the results record: scores first, then key decode, then the decision notes are written on the same sheet.

### Kit packaging

A self-contained folder in this repo: `trials/2026-07-writing-doctrine/`.

```
trials/2026-07-writing-doctrine/
  README.md        ← runner instructions for the downstream orchestrating agent
  packet-1.md … packet-6.md
  brief-procedure.md  ← how to run and freeze the shared Q&A
  rubric.md        ← scoring sheet + results record template
  key.md           ← base64 packet→arm map, do-not-open warning
```

The downstream project copies the folder in (e.g. to a scratch directory in the project), and the orchestrating agent follows README.md: freeze the brief, dispatch six independent agents (one packet each, no cross-visibility), collect outputs to `out/`, hand the user the rubric.

### Decision mapping

The read feeds three gated decisions, recorded on the results sheet and carried back to this repo:

- **Style axis** (arms 1–3 vs 4–6): does stop-slop beat current doctrine on Wide-phase character notes? This tests the register hypothesis directly instead of assuming it. Export-prose and plugin-authoring registers are not tested by this trial; their calls remain judgment calls informed by this result.
- **Doctrine axis, additive step** (1,4 vs 2,5): which additive principles earn fold-in. The read is holistic; fold-in still cherry-picks per principle using the notes as evidence.
- **Doctrine axis, tensions step** (2,5 vs 3,6): the two tension calls — hook exemption and anchor repetition.
- Interactions (e.g. stop-slop only helping under new doctrine) are noted if visible; with one character per cell they are suggestive, not conclusive.

Results return as a reflection document in this vault linking the completed rubric; doctrine edits then proceed as normal follow-up work. Inbox items 1 and 2 graduate to this spec.

## Consequences

- Six full character notes of the same character is the accepted cost of the factorial; n=1 character means results guide judgment rather than prove anything.
- The flat six-way read risks washing out the two-rule tensions delta; accepted explicitly during design.
- The trial produces scratch notes, not the character's real note. The winning arm's output may seed the real note afterwards, but that is the project's call and outside this trial.
- The stop-slop extraction happens at kit build, pinning the tested rule set to the repository state at that date.
- Battle-test roleplay probes and agent-judge scoring were considered and dropped; if the read proves insufficient, either can be added to a rerun without changing the kit's shape.
