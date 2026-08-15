---
type: review
title: Review — Character Card Architecture Spec
description: Adversarial review of the character card architecture spec (Q&A workflow,
  block model, export interface replacement).
tags:
- agent-ready
date: 2026-08-15
timestamp: 2026-08-15T13:21Z
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
## Round 2 — digest `d05f59a8…`, anchor `80ec70d2` (dirty), tokens 87092, 2026-08-15T08:15:49-05:00, 499s

Anchor: 80ec70d2f4162aed6ceeab2054ffd0822367d967 (dirty tree)
Artifact digest: d05f59a8239c47130b12f1a776a6e4857a371d3d9bd4a20c5b70b1d2ad732a46 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-15-character-card-architecture-implementation.md

1. The grader agent is not retired
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:61
   Quote:
     **Spec anchor:** D1 (card format block model), D2.3 (entry
     translation rules), D3 (what this replaces — retirement of
     framework.md and generation-rules.md).
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: fix
   Body: D3 also explicitly supersedes the post-generation grader agent, but the plan reduces retirement to two character sub-files. At the anchor, `skills/worldbuilder-grader/SKILL.md` remains an auto-discovered skill that directs users to run the retired generation workflow and `scripts/detect_input_echo.py`. Task 1’s reference sweep would find this file, contradicting its stated expectation, but no task says whether to delete or rewrite it. The shipped plugin would therefore retain a reachable entry point for the architecture being retired.

2. The intimate-dynamics file retains a Design Notes dependency
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:305
   Quote:
     Keep the existing content: three coverage areas (attraction
     expression, hesitation and limits, specific dynamic), mandatory
     friction point, existing examples. The coverage areas and friction
     point requirement are unchanged — this is additive guidance, not
     a rewrite.
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored `intimate.md` says exploration answers belong in “the Q&A session and Design Notes.” D3 retires Design Notes as a separate input, while this task is explicitly additive and contains no instruction to remove that reference. The resulting skill set would direct users toward a section Task 1 removes from the template.

3. A retired mandatory contrast declaration remains in Relationships
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:65
   Quote:
     **Files:**
     - Create: `skills/worldbuilder-character/card-format.md`
     - Modify: `defaults/templates/character.md`
     - Delete: `skills/worldbuilder-character/framework.md`
     - Delete: `skills/worldbuilder-character/generation-rules.md`
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: The spec preserves the relationship archetypes but expressly drops contrast declarations as a mandatory requirement. The anchored `relationships.md` still contains “Contrast declaration (1 entry)” under Coverage Requirements, yet it is absent from every task’s modification list. Referencing that file unchanged carries forward a requirement the new architecture removes.

4. Background omits the fact-to-manifestation exemption
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:99
   Quote:
     5. **Section-scoped writing rules** — per D2.3. Background entries:
        Orwell co-anchor, no meta-vocabulary, no staging test or
        action-line. Body and Soul entries: action-line, staging test
        (Because clause exempt), trait-word ban, Orwell co-anchor,
        fact-to-manifestation. State these are overridable defaults.
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: D2.3 explicitly says fact-to-manifestation does not apply to Background entries. The task names the staging and action-line exemptions but omits this third exemption while assigning fact-to-manifestation to Body and Soul. That leaves the governing reference ambiguous about whether factual Background phrasing should be transformed behaviorally.

5. Voice/Dialogue omits required scene context and coverage annotations
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:233
   Quote:
     7. **Addon block guidance** — reference relationships.md for
        Relationships, intimate.md for Intimate Dynamics. For
        Voice/Dialogue: list the situation categories, state the user
        picks 2–4, each snippet is a composite showing pulling from
        multiple Core areas.
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: D1.4 additionally requires enough scene context in every snippet to establish its situation and requires the working sheet to record which Core areas each example exercises. Neither this instruction nor Task 1 includes those requirements, so an implementation can satisfy the plan while omitting two normative parts of the Voice/Dialogue interface.

6. Coverage checking stops before prescribed follow-up behavior
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:222
   Quote:
     5. **Coverage checking** — per D2.4. After each Core section,
        report depth-of-access observations (advisory, not
        deterministic). After full Core block, check for missing
        mandatory doctrine entries (D1.3). Missing mandatory entries
        must be addressed before finalization or explicitly waived with
        a recorded reason.
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: D2.4 requires the workflow to suggest follow-up questions for under-represented columns and let the user either accept the suggestion or mark the section complete. Reporting observations alone does not implement that interaction, leaving the Q&A workflow without its normative remediation and exit behavior.

7. Working-document annotations and export stripping are omitted
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:229
   Quote:
     6. **Working document** — per D2.5. Entries accumulate in the
        character note as approved. Each section is a markdown heading,
        entries are bullet points.
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: high
   Channel: fix
   Body: D2.5 defines an interface in which the working document may carry grid-position or coverage-area labels and the export step strips them. The task specifies only headings and bullets. Because `card-format.md` is intended to govern both skills and export tools, omitting the annotation/stripping contract leaves a normative cross-layer interface unimplemented.

8. Target ranges are incorrectly converted into completion gates
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:239
   Quote:
     8. **Completion checklist** — replace the current self-check
        checklist. New checklist covers: all mandatory doctrine entries
        present or waived, each Core section within target range,
        addon blocks present per project flags, no trait adjectives,
        entries follow section-appropriate writing rules.
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: D1.1 says the entry ranges are targets, “not a rigid count.” Making “within target range” a completion-checklist condition turns them into a gate alongside genuinely mandatory doctrine entries. Valid cards outside a target range could consequently be rejected despite satisfying the spec.

9. Addon activation relies on undefined generic flags
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:210
   Quote:
     3. **Session flow** — per D2.2. Block order: Core (Background →
        Body → Soul), then addon blocks if flagged (Relationships →
        Intimate Dynamics → Voice/Dialogue). Within each Core section,
        follow the depth-of-access progression (immediate → over time
        → hidden/foundational). Addon blocks follow their own coverage
        structure.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: fix
   Body: Only Intimate Dynamics has an existing project-plan flag. The spec gives different activation rules for each addon: Relationships is relevant for cast-based work, Intimate Dynamics is a planning judgment, and Voice/Dialogue is recommended for particular export or distinctiveness needs. The plan neither defines Relationship or Voice flags nor tasks any file with setting them, so those blocks can be silently skipped or demanded without a specified decision path.

10. The OKF verification command always crashes on the real schema
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:152
   Quote:
     ```bash
     python -c "import json; d=json.load(open('defaults/okf.json')); t=[x for x in d['types'] if x.get('name')=='character']; print('OK' if t and 'Background' in t[0].get('template','') and 'Design Notes' not in t[0].get('template','') else 'FAIL')"
     ```
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: `defaults/okf.json` stores `types` as an object keyed by type name, not a list of objects with `name` fields. Iterating it produces strings, so `x.get(...)` raises `AttributeError`; this was reproducible against the anchored file. Task 1 therefore cannot reach its expected `OK` result even after a correct implementation.

11. The reference checker can pass without checking any references
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:245
   Quote:
     Check that SKILL.md references only files that exist after Task 1:

     ```bash
     grep -oP '(?<=\()[\w/.-]+\.md(?=\))' skills/worldbuilder-character/SKILL.md | while read f; do test -f "skills/worldbuilder-character/$f" || test -f "$f" || echo "MISSING: $f"; done
     ```
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The regex recognizes only `.md` destinations immediately enclosed in parentheses. The task itself instructs authors to reference files using code spans such as `` `card-format.md` ``, matching the existing skill’s convention. If all references use that permitted form, `grep` emits nothing and the command reports success without inspecting a single reference. It also provides no semantic verification of the required Q&A sections.

12. Card-format and template requirements have no effective content verification
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:105
   Quote:
     Source content from the spec decisions. Follow
     `skills/writing-style.md` for the prose style. Check against
     `docs/slop-phrases.md`.

     - [ ] **Step 2: Update character template**
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: Step 1 ends without a verification command or expected result for its grid, six doctrine entries, ranges, addon rules, or section-scoped rules. The only later template assertion checks for `Background` and absence of `Design Notes`—and that command crashes as described above. Consequently most of Task 1 can be omitted or malformed without a planned check detecting it.

13. Intimate-dynamics verification tests keyword count, not the task
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:314
   Quote:
     Check that intimate.md's entry format guidance matches
     card-format.md's Soul entry format:

     ```bash
     grep -c "When/Behavior/Because\|behavioral prose\|card-format" skills/worldbuilder-character/intimate.md
     ```

     Expected: at least 2 matches.
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: Two unrelated lines containing any of these tokens satisfy the check. It does not verify the 1–2-per-area target, the three depth-of-access concepts, preservation of all coverage areas, the mandatory friction point, or removal of stale Design Notes guidance. A materially incomplete Task 3 therefore passes its sole verification.

14. Task 1’s interface omits most of its consumed and produced artifacts
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:71
   Quote:
     **Interfaces:**
     - Consumes: spec decisions D1.1–D1.4, D2.3
     - Produces: `card-format.md` — the reference document that Task 2's
       SKILL.md and Task 3's intimate.md reference by name
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The task also consumes D3, the existing template and retired files, two writing references, and the OKF build contract. It produces a modified character template, regenerated `defaults/okf.json`, two deletions, and potentially a modified `CONTEXT.md`. Declaring only `card-format.md` as output leaves downstream workers without a complete dependency or handoff contract, directly violating the task-interface criterion.

15. The conditional CONTEXT.md edit is absent from scope and staging
   Location: .claude/plans/2026-08-15-character-card-architecture-implementation.md:139
   Quote:
     Expected: only SKILL.md (which is rewritten in Task 2) and
     possibly CONTEXT.md. If CONTEXT.md references them, update the
     reference to point to card-format.md.
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: `CONTEXT.md` is not listed under Task 1 Files or Interfaces, and Task 1’s commit stages neither it nor a general tracked-change set. If the stated condition is true, the executor is told to modify a file that the task does not declare and then leave that modification out of the prescribed commit. “Possibly” also makes the expected reference-sweep result non-deterministic rather than providing a concrete branching verification.

FINDINGS: 0 critical, 15 major, 0 minor, 0 nit

### Adjudication — Round 2

1. **Accept.** Fixed: added grader skill and detect_input_echo.py to retirement list in Task 1.
2. **Accept.** Fixed: Task 3 now includes removing Design Notes reference from intimate.md.
3. **Accept.** Fixed: Task 1 now modifies relationships.md to remove contrast declaration as mandatory.
4. **Accept.** Fixed: card-format.md step now explicitly lists fact-to-manifestation as exempt for Background.
5. **Accept.** Fixed: Voice/Dialogue guidance now includes scene context and coverage annotation requirements.
6. **Accept.** Fixed: coverage checking in Task 2 now includes follow-up question suggestion and accept/complete exit behavior.
7. **Partial accept.** Fixed: card-format.md step now includes working document annotation conventions. Annotation syntax details are implementation decisions.
8. **Accept.** Fixed: completion checklist uses "at least one entry" not target ranges as gates.
9. **Partial accept.** Fixed: added session-opening step to Task 2 that determines which addons to include with specific criteria per block.
10. **Accept.** Fixed: OKF verification command uses dict key access matching actual schema structure.
11. **Accept.** Fixed: reference check improved; note that semantic verification of SKILL.md content is inherently human review.
12. **Partial accept.** Fixed: added section-presence verification for card-format.md.
13. **Accept.** Fixed: intimate.md verification now checks for required additions and stale references separately.
14. **Accept.** Fixed: Task 1 interfaces expanded to list all consumed and produced artifacts.
15. **Accept.** Fixed: CONTEXT.md explicitly added to Task 1 files and commit staging.

