---
type: spec
title: Writing style trial — STE-100 and semantic anchors
description: 'Trial comparing character note generation under different writing style
  constraints: current baseline, strict STE-100, loose STE-100, and BLUF'
tags:
- complete
date: 2026-08-14
timestamp: 2026-08-14T02:27Z
resources: []
---

# Writing style trial — STE-100 and semantic anchors

## Context

Character notes (Background, Body, Soul, Relationships) are functional AI portrayal guidelines. Their purpose is to give an AI game master clear behavioral instructions it can act on during roleplay. The current writing-style.md prescribes plain, behavioral prose through a long list of banned patterns, but the pipeline quality trial (2026-08-13, negative result) showed that generation output still produces em-dashes (banned), overwrought prose, contextless entries, and language that sounds nothing like how a human would write functional instructions.

The core problem: the current style rules tell the generator what NOT to do. STE-100 (ASD Simplified Technical English) and BLUF (Bottom Line Up Front) tell the generator what TO do — positive constraints that have been shown to activate specific LLM behaviors when named as semantic anchors.

This trial tests whether naming a recognized writing standard in the generation instructions produces better functional output than the current ban-list approach.

## Decisions

### D1: Four conditions

Each condition replaces writing-style.md entirely for that run. No condition runs with the ban list active alongside the new style instruction. All conditions use identical Design Notes, model, and prompt structure. Only the style instruction varies.

**Condition 0 — Baseline.** Current writing-style.md rules as-is.

**Condition A — STE-100 strict.** Replace writing-style.md with strict ASD-STE-100 rules: approved words only where an approved equivalent exists, sentences no longer than 20 words (procedural) or 25 words (descriptive), active voice, one instruction per sentence, no figurative language, present tense for current state. The generator is told to write as if producing an aircraft maintenance manual entry — each sentence is a discrete behavioral instruction.

**Condition B — STE-100 loose.** Replace writing-style.md with a single instruction: "write in ASD-STE-100 Simplified Technical English style." No enumerated rules. Tests whether naming the standard as a semantic anchor is sufficient for the LLM to apply its conventions without a detailed rule set.

**Condition C — BLUF.** Replace writing-style.md with BLUF structure rules: each entry leads with the observable behavior (what the character does), then provides supporting context (why, when, how it manifests). No entry may begin with context, backstory, or emotional framing before stating the behavior.

### D2: Test character

Use a different character from the previous trial. Select a character with known-good Design Notes that accurately reflect the intended portrayal, or create a purpose-built test character with 10-15 clear facts spanning motivations, behaviors, relationships, and history. The character selection or creation happens during implementation, not here.

### D3: Output scope

Generate the Soul section only, 1 run per condition. This produces 4 outputs (one per condition) with approximately 8-12 entries each.

### D4: Review method

Blind the four outputs (random letter codes, sealed key). The reviewer reads all four and gives a general impression per condition — not per-entry scores. The impression should address: does this read like a functional instruction set an AI could act on? Would you have to rewrite most of it or is it usable as-is?

### D5: Success criteria

The reviewer ranks the four conditions from best to worst and states whether the best condition is good enough to adopt or whether all fail. The absolute quality gate takes precedence: a condition can rank best but still not be good enough to adopt. There is no numerical threshold. If a condition is both clearly better and good enough, it replaces writing-style.md in the generation rules for Soul. Extension to other sections (Background, Body, Relationships) is a separate decision. If multiple conditions are comparable, the simpler one wins.

## Consequences

A graduating condition replaces writing-style.md for Soul section generation as-is — exactly the style instruction tested, with no untested modifications. Whether to retain the ban list alongside the new style, or extend the style to other sections, are separate follow-up decisions that would need their own evaluation.

A negative result (all conditions fail) records that these specific style instructions did not produce usable output in this trial. It does not establish that the semantic anchor approach is fundamentally ineffective — input quality, the generation pipeline, or other factors may have contributed.

## Notes (non-normative)

STE-100 was designed for maintenance manuals — instructions that must be unambiguous to non-native English speakers maintaining aircraft. Character notes serve a structurally similar purpose: unambiguous behavioral instructions for an AI that must portray a character without misinterpretation. The hypothesis is that the same constraints that make maintenance instructions clear will make character instructions clear.

BLUF is a military communication standard. Its relevance is the "contextless entry" problem from the previous trial: entries that lead with atmosphere or implication before stating what the character actually does. BLUF structurally prevents this by requiring the behavior first.
