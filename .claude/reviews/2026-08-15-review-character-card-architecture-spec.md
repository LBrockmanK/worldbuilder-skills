---
type: review
title: Review — Character Card Architecture Spec
description: Adversarial review of the character card architecture spec (Q&A workflow,
  block model, export interface replacement).
tags:
- agent-ready
date: 2026-08-15
timestamp: 2026-08-15T13:00Z
resources: []
---

# Review — Character Card Architecture Spec

## Rounds
## Round 1 — digest `43f9e5bd…`, anchor `4ffa42d6` (dirty), tokens 49191, 2026-08-15T07:57:20-05:00, 195s

Anchor: 4ffa42d6a44dea6444e719f31164da5a78b6fe76 (dirty tree)
Artifact digest: 43f9e5bd8731531ac3d2080f10a6815a9c09a001434aa537f1fb88e17078d27a (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md

1. Card format lacks a complete machine-readable contract
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:196
   Quote:
   > Entries accumulate in an Obsidian markdown note as they are approved.
   > Each section is a markdown heading. Entries are bullet points under
   > their section heading. The working document may carry labels or
   > annotations (grid position, coverage area) that the export step
   > strips.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: fix
   Body: This defines only a loose presentation convention. It does not prescribe whether `Core` is itself a heading, canonical heading names and ordering, addon boundaries, annotation syntax, identifiers, or how an exporter distinguishes metadata from content. “May carry” also leaves exporters unable to rely on annotations they are expected to strip. Because skills and export tools are expressly intended to read this format, the block model is not complete enough to serve as their shared interface.

2. Universal translation rules contradict the Background entry type
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:61
   Quote:
   > - **Background** — Facts and formative events. What is true about
   >   the character. Entries are fact pairs: a formative fact and what it
   >   made true. No behavioral framing — other sections handle
   >   manifestation.
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: D2.3 applies present-tense observable/action-line, staging, and fact-to-manifestation rules whenever an answer becomes “a card entry.” Those rules require behavioral manifestation, while Background explicitly forbids behavioral framing and contains historical facts. No section-specific exception is stated, so a conforming translator cannot produce Background entries that satisfy both decisions.

3. The staging rule is incompatible with mandatory Soul causation
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:167
   Quote:
   > When the AI translates a human answer into a card entry, it applies
   > the established writing rules as defaults:
   >
   > - Action-line convention (present tense, observable/audible only)
   > - Staging test ("can a director stage this?")
   > - Trait-word ban (no adjective labels; behavior earns the word)
   > - Orwell co-anchor (shortest word, active voice, cut waste)
   > - Fact-to-manifestation transformation (reproduce semantic content,
   >   never reproduce phrasing from the user's answer)
   > - When/Behavior/Because structure for Soul entries
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: A `Because` clause normally states an internal belief, motive, or formative cause, which is not itself observable or stageable. The specification simultaneously requires observable/audible-only content and When/Behavior/Because for Soul without saying that the staging constraint applies only to the behavior portion. Implementations can therefore reject required causal information or violate the action-line rule.

4. Previously required doctrine is omitted despite the preservation claim
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:221
   Quote:
   > Preserved from the generation pipeline era:
   > - All content principles (D1.3 doctrine entries, trait-word ban,
   >   values-with-costs, false beliefs, etc.)
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The superseded Pipeline v2 doctrine required charge tags on formative memories, corresponding Soul entries for high-charge memories, a cast contrast declaration, 2–3 values-with-costs entries, and lowest-value evidence. D1.3 contains none of the charge or contrast requirements, reduces values-with-costs to one top value, and omits lowest values. Thus “All content principles” is false and the required doctrine set is incomplete.

5. Mandatory doctrine entries are asserted without justification
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:92
   Quote:
   > Within the Core block, certain entries are mandatory regardless of
   > entry count targets:
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The section lists requirements but gives no rationale, provenance, or applicability argument for making each universal. This is especially material for false belief, value-conflict stance, and unresolved tension, which are not self-evidently mandatory for every character. A general statement that the design follows an audit does not justify the individual requirements as demanded by the acceptance criteria.

6. Intimate Dynamics has neither an inclusion rule nor an entry model
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:113
   Quote:
   > **Intimate Dynamics.** Optional, flagged at project planning. Three
   > coverage areas: attraction expression, hesitation and limits,
   > specific dynamic. Mandatory friction point (internal contradiction
   > in intimate behavior).
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: escalate
   Body: “Flagged at project planning” identifies where a choice is recorded, not the criteria for making it. The block also lacks entry count, entry shape, and definitions or validation tests for “specific dynamic” and “friction point.” The artifact provides no basis for deciding which projects or characters should include it, so human policy is required.

7. Voice/Dialogue has no inclusion criterion and cannot enforce its claimed style contract
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:131
   Quote:
   > The user picks 2–4 categories relevant to their character. Each
   > snippet includes enough scene context to set the situation (making a
   > standalone scenario field unnecessary). Style contract (perspective,
   > tense, register) emerges from the examples rather than being
   > declared as rules.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: escalate
   Body: Unlike Relationships and Intimate Dynamics, this addon never says when it is attached. “Enough scene context” is not testable, and no behavior is defined for examples that disagree in perspective, tense, or register. An exporter or downstream model cannot infer one authoritative style contract from contradictory examples. The artifact does not provide a basis for choosing a universal inclusion policy.

8. Addon sequencing assumes sections and grid mappings that do not exist
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:152
   Quote:
   > The workflow proceeds block by block, section by section within
   > each block. Within each section, questions follow the depth-of-
   > access progression (immediate → over time → hidden/foundational)
   > to build from surface to depth.
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The addon definitions do not establish sections within their blocks. Relationships and Voice/Dialogue also have no depth-of-access mapping, while only Intimate Dynamics explicitly adopts that lens. Consequently, the stated universal sequencing algorithm cannot be applied to two of the three addons and refers to nonexistent internal sections.

9. Depth coverage cannot be implemented deterministically
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:184
   Quote:
   > After each section is complete, the workflow runs a coverage check
   > against the depth-of-access grid. The check reports which columns
   > are under-represented
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The specification defines neither how a flat entry is classified into a column nor what “under-represented” means—zero entries, fewer than another column, or a minimum proportion. Grid annotations are optional, so the checker cannot assume classification metadata exists. Different implementations will issue materially different follow-up questions for the same card.

10. Mandatory doctrine can be bypassed while the card is still declared complete
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:186
   Quote:
   > The user can accept the suggestion or mark the section
   > as complete.
   >
   > After the full Core block is complete, a cross-section coverage
   > check reports any required doctrine entries (D1.3) that are missing.
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: D1.3 calls these entries mandatory regardless of counts, but this workflow only reports omissions after completion and defines no state transition, remediation, waiver record, or prohibition on finalizing an invalid card. Coupled with the unconditional right to skip questions, a reachable workflow can produce a “complete” Core that violates mandatory doctrine.

11. Fact-to-manifestation does not preserve deslop/deframe behavior
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:225
   Quote:
   > - Deslop/deframe concepts as applied to source-material extraction
   >   (the fact-to-manifestation transformation serves the same purpose
   >   in the Q&A context)
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: In the superseded pipeline, deslop/deframe preprocessing removes boilerplate, meta-vocabulary, and framing while preserving and flagging substantive facts. Fact-to-manifestation only changes phrasing into observable behavior. It neither detects nor removes framing, and D2.3 applies it indiscriminately even where Background forbids manifestation. Calling these the same purpose silently drops a preserved quality-control function.

12. Removing the grader is justified by checks that do not replace it
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:213
   Quote:
   > - The grader agent as a post-generation quality check (quality is
   >   addressed at creation time, not post-generation)
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Creation-time coverage checks test depth columns and required doctrine only. They do not perform the grader’s input-echo similarity, variant-divergence, or slop checks. Human approval is not specified to run those tests either. The replacement claim therefore removes detectable quality failures without an equivalent creation-time mechanism.

13. Consequences invent an undefined “accept first draft” mode
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:260
   Quote:
   > If a user wants to build a card quickly with
   > minimal involvement, the Q&A workflow's "accept first draft"
   > mode must be fast enough.
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: No decision defines this mode, how it is entered, what constitutes a draft, whether approval and coverage checks are skipped, or what “fast enough” means. The consequence therefore introduces both a placeholder requirement and a workflow path absent from D2.

14. Consequences make entry labels mandatory after the decision made them optional
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:238
   Quote:
   > - Character notes gain the block structure (Core sections + addon
   >   blocks) with labeled entries during creation.
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: D2.5 says the working document “may carry labels or annotations,” whereas this consequence says character notes gain labeled entries. These describe different persisted formats and prevent implementers from knowing whether labels are required creation metadata or optional notes.

15. Export separation is incorrectly presented as a new consequence
   Location: .claude/specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md:240
   Quote:
   > - The export step becomes a separate concern reading the card format
   >   definition.
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The same Consequences section says the three-phase Seed → Wide → Export architecture and ADR 0003 platform decoupling do not change. ADR 0003 already makes export the separate target-aware phase, and Pipeline v2 explicitly left export unchanged. What is new is the export layer’s dependency on the new card-format contract, not its separation, so this consequence misstates the architectural delta.

FINDINGS: 0 critical, 15 major, 0 minor, 0 nit

### Adjudication — Round 1

1. **Reject.** Spec deliberately avoids coupling to a specific file layout — vault structure is in flux. Implementation defines the concrete format.
2. **Accept.** Fixed: D2.3 now scopes translation rules by section type. Background entries exempt from staging test, action-line, and fact-to-manifestation.
3. **Accept.** Fixed: staging constraint now explicitly applies to When/Behavior portions only; Because clause exempt.
4. **Accept.** Fixed: D3 preservation claim now itemizes what was simplified vs. carried forward verbatim.
5. **Accept.** Fixed: each D1.3 entry now carries one-line provenance.
6. **Partial accept.** Inclusion is intentionally a human decision (reject that portion). Fixed: added entry shape (behavioral prose, 1-2 entries per coverage area).
7. **Partial accept.** Fixed: added inclusion guidance (recommended for export targets supporting example dialogue). Reject style-contract enforcement concern — emergent by design.
8. **Accept.** Fixed: depth-of-access sequencing now scoped to Core only; addon blocks follow their own coverage structure.
9. **Partial accept.** Fixed: coverage check now described as advisory (AI judgment), not deterministic pass/fail.
10. **Accept.** Fixed: D1.3 now states card is not finalized until mandatory entries are present or explicitly waived with recorded reason. D2.4 references this gate.
11. **Accept.** Fixed: deslop/deframe and fact-to-manifestation now described as related but distinct operations in D3.
12. **Partial accept.** Fixed: D3 now explains why grader checks are unnecessary in Q&A workflow (no separate input document = no echo to detect; human approval per entry).
13. **Accept.** Fixed: risk reworded to reference existing human-override capability (D2.1) rather than naming an undefined mode.
14. **Accept.** Fixed: consequence aligned with D2.5 "may carry" language.
15. **Accept.** Fixed: consequence now states what actually changed (export layer's dependency shifts to new card format definition).
