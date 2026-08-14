---
type: review
title: 'Review: writing style trial spec'
description: Adversarial review of the writing style trial spec (STE-100 and semantic
  anchors)
tags:
- agent-ready
date: 2026-08-14
timestamp: 2026-08-14T02:20Z
resources: []
---

# Review: writing style trial spec

## Rounds
## Round 1 — digest `915915c6…`, anchor `0ad6e882` (dirty), tokens 26384, 2026-08-13T21:19:29-05:00, 123s

Anchor: 0ad6e8827ff2fc6732fad6ce2bb16ed464f5ab70 (dirty tree)
Artifact digest: 915915c6d7350d78c017c34cc22c9984eb83f3ef327c1e493b17f0e974f95ab9 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md

1. Loose STE-100 and BLUF do not specify whether baseline rules remain active
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:29-33
   Quote: |
     **Condition A — STE-100 strict.** Replace writing-style.md instructions with strict ASD-STE-100 rules: approved words only where an approved equivalent exists, sentences no longer than 20 words (procedural) or 25 words (descriptive), active voice, one instruction per sentence, no figurative language, present tense for current state. The generator is told to write as if producing an aircraft maintenance manual entry — each sentence is a discrete behavioral instruction.

     **Condition B — STE-100 loose.** Tell the generator to "write in ASD-STE-100 Simplified Technical English style" without enumerating specific rules. Tests whether naming the standard as a semantic anchor is sufficient for the LLM to apply its conventions without a detailed rule set.

     **Condition C — BLUF.** Each entry leads with the observable behavior (what the character does), then provides supporting context (why, when, how it manifests). No entry may begin with context, backstory, or emotional framing before stating the behavior. The generator is told to "use BLUF (Bottom Line Up Front) structure for every entry."
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: Condition A explicitly replaces writing-style.md, while B and C merely add an instruction without saying whether they replace or supplement it. Both readings are plausible and produce materially different treatments. Consequently, the conditions are not well-defined or reproducible and any comparison could measure retention of the ban list rather than the named style.

2. Baseline and strict STE-100 are not frozen to reproducible inputs
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:27-29
   Quote: |
     **Condition 0 — Baseline.** Current writing-style.md rules as-is.

     **Condition A — STE-100 strict.** Replace writing-style.md instructions with strict ASD-STE-100 rules: approved words only where an approved equivalent exists, sentences no longer than 20 words (procedural) or 25 words (descriptive), active voice, one instruction per sentence, no figurative language, present tense for current state.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: escalate
   Body: “Current” does not identify the exact writing-style.md bytes used, and “approved words” does not identify an STE-100 edition or controlled vocabulary. A later implementation can therefore construct different baseline and strict conditions while claiming conformance to this spec. The human must select the authoritative STE-100 version; the baseline and resulting prompts then need immutable versions or exact captured text.

3. The generation protocol does not hold non-style variables constant
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:37-41
   Quote: |
     Use a different character from the previous trial. Select a character with known-good Design Notes that accurately reflect the intended portrayal, or create a purpose-built test character with 10-15 clear facts spanning motivations, behaviors, relationships, and history. The character selection or creation happens during implementation, not here.

     Generate the Soul section only, 1 run per condition. This produces 4 outputs (one per condition) with approximately 8-12 entries each.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The protocol does not require the four runs to use identical Design Notes, model/version, surrounding prompt, sampling settings, context, or output budget. Differences in any of those variables can be mistaken for effects of the writing-style condition. A valid comparison must freeze them and vary only the condition text.

4. One run per condition cannot separate style effects from sampling noise
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:41
   Quote: |
     Generate the Soul section only, 1 run per condition. This produces 4 outputs (one per condition) with approximately 8-12 entries each.
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: Generative output varies between runs. With one sample per treatment, a lucky or poor sample can determine the entire ranking, and the proposed review has no way to detect that failure. This does not support the stated causal conclusion that naming a standard produces better output.

5. The review does not measure the defects or mechanism named by the trial
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:17,31,45
   Quote: |
     The current writing-style.md prescribes plain, behavioral prose through a long list of banned patterns, but the pipeline quality trial (2026-08-13, negative result) showed that generation output still produces em-dashes (banned), overwrought prose, contextless entries, and language that sounds nothing like how a human would write functional instructions.

     **Condition B — STE-100 loose.** Tell the generator to "write in ASD-STE-100 Simplified Technical English style" without enumerating specific rules. Tests whether naming the standard as a semantic anchor is sufficient for the LLM to apply its conventions without a detailed rule set.

     Blind the four outputs (random letter codes, sealed key). The reviewer reads all four and gives a general impression per condition — not per-entry scores. The impression should address: does this read like a functional instruction set an AI could act on? Would you have to rewrite most of it or is it usable as-is?
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The required impression neither checks the four known failure modes nor tests whether the loose condition actually applied STE-100 conventions. It can rank perceived usability, but it cannot answer the stated mechanism question or identify which target defects improved. The review method therefore does not match the trial’s stated goals.

6. The success criteria are non-operational
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:49
   Quote: |
     The reviewer ranks the four conditions from best to worst and states whether the best condition is good enough to adopt or whether all fail. There is no numerical threshold. If a condition is clearly better, it replaces writing-style.md in the generation rules. If multiple conditions are comparable, the simpler one wins.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: “Good enough,” “clearly better,” “comparable,” and “simpler” have no definitions, evidence requirements, or tie rules. Different reviewers can reach different deployment decisions from the same outputs while following the spec. Choosing an adoption threshold and defining simplicity require a human product decision before the result can be actionable.

7. Relative superiority and the absolute adoption gate prescribe conflicting outcomes
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:49
   Quote: |
     The reviewer ranks the four conditions from best to worst and states whether the best condition is good enough to adopt or whether all fail. There is no numerical threshold. If a condition is clearly better, it replaces writing-style.md in the generation rules.
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: A condition can be clearly better than the others yet still not be good enough to adopt. The first sentence classifies that case as failure, while the last requires replacement. The spec must establish that the absolute quality gate takes precedence, or otherwise define the intended outcome for this reachable case.

8. “All fail” does not establish that semantic anchors failed to improve quality
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:55
   Quote: |
     A negative result (all conditions fail) records that these semantic anchors do not improve output quality for this use case and the current approach stands.
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: All outputs can fall below the adoption threshold while an anchor still improves substantially over baseline. Conversely, baseline itself is included among “all conditions,” so its absolute failure says nothing about relative improvement by an anchor. The proposed record would assert a conclusion that the review result does not support.

9. The rollout may deploy an untested hybrid condition
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:53
   Quote: |
     A graduating condition replaces the writing-style.md rules referenced by the character generation skill. The current ban-list may be retained as a supplement (a "do not" layer on top of the positive style anchor) or dropped entirely, depending on whether the graduating style already covers the banned patterns.
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Retaining the ban list creates a style-anchor-plus-ban-list configuration that the explicitly replacement-based strict condition does not test. The spec also supplies no review for deciding whether a style “covers” the banned patterns. Shipping either configuration after evaluating only the other makes the trial result inapplicable to the deployed behavior.

10. A single Soul sample is used to justify rules for all character-note sections
   Location: .claude/specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md:17,41,53
   Quote: |
     Character notes (Background, Body, Soul, Relationships) are functional AI portrayal guidelines.

     Generate the Soul section only, 1 run per condition. This produces 4 outputs (one per condition) with approximately 8-12 entries each.

     A graduating condition replaces the writing-style.md rules referenced by the character generation skill.
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Background, Body, Soul, and Relationships contain different kinds of material, but the trial observes only Soul and then changes the shared generation rules. A style that works for behavioral Soul entries may damage historical, physical, or relational notes. This exceeds what an appropriately scoped single trial can establish; the conclusion or rollout must be limited to the tested section unless broader evidence is collected.

FINDINGS: 0 critical, 10 major, 0 minor, 0 nit

### Round 1 adjudication

1. **ACCEPT.** Clarify: all conditions replace writing-style.md entirely. No condition runs with the ban list active alongside the new style.
2. **REJECT.** The baseline is a git-tracked file; the LLM's understanding of STE-100 IS the thing being tested, not a specific edition. This is an exploratory trial, not a reproducibility study.
3. **ACCEPT in part.** Add that all conditions use identical Design Notes, model, and prompt structure — only the style instruction varies.
4. **REJECT.** The user explicitly chose 1 run and general impression. The previous trial's attempt at multiple runs and structured metrics was rejected as unusable. This is exploratory.
5. **REJECT.** The user explicitly asked for general impression over structured defect measurement. The previous trial's multi-dimensional scoring was called "completely useless."
6. **REJECT.** The success criteria are deliberately qualitative — the human makes a judgment call. This is intentional.
7. **ACCEPT.** Clarify: the absolute quality gate takes precedence. A condition can rank best but still not be good enough to adopt.
8. **ACCEPT.** Soften the negative-result language. A blanket failure could reflect input quality or the generation pipeline, not the style anchors.
9. **ACCEPT.** Simplify: a graduating condition replaces writing-style.md as-is. No untested hybrid. Retaining the ban list alongside is a separate follow-up decision.
10. **ACCEPT in part.** A graduating style is adopted for Soul initially. Extension to other sections is a separate decision.

