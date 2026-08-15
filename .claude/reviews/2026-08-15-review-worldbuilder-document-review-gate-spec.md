---
type: review
title: 'Review: worldbuilder document review gate spec'
description: Adversarial review of the worldbuilder document review gate spec
tags:
- agent-ready
date: 2026-08-15
timestamp: 2026-08-15T20:51Z
resources: []
---

# Review: worldbuilder document review gate spec

## Rounds
## Round 1 — digest `b242e5ef…`, anchor `907dca50` (dirty), tokens 83608, 2026-08-15T15:31:43-05:00, 272s

Anchor: 907dca502067a52148b77eb32bdaecec9712f9bd (dirty tree)
Artifact digest: b242e5ef4e078807f3551873bdb462882117c4af897648ea26e44e1c2335f702 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md

1. Trial findings receive contradictory classifications
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:20-23, 133-135
   Quote:
       Of 22 major findings, 19 were genuinely useful — the autonomous Q&A
       pass produced entries too literary and interpretive for the card
       format's staging-test and action-line requirements. Three findings
       were false positives caused by missing scope exemptions (Design Notes,
       [...]
       The Adeline trial's finding breakdown (15 genuinely useful, 4
       borderline, 3 false positives)
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The Context classifies all 19 non-false-positive findings as genuinely useful, while Notes classifies only 15 that way and separates four as borderline. This changes the evidence supporting automatic enforcement: borderline findings are precisely the cases relevant to D4’s escalation boundary and cannot simultaneously be presented as unqualified successes.

2. The claimed exemptions have not yet been codified
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:23-25, 115-118
   Quote:
       Three findings
       were false positives caused by missing scope exemptions (Design Notes,
       working annotations, in-world quoted text). These exemptions have
       since been codified.
       [...]
       - card-format.md needs a `## Review criteria` section codifying the
         Adeline trial's scoping decisions (Design Notes exempt, working
         annotations exempt, in-world quoted text exempt from trait-word
         ban, Voice/Dialogue exempt from card-body writing rules).
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Context says the three exemptions already exist, but Consequences says they still need to be added. The current card format only identifies working annotations as working aids; it does not codify all the listed review exemptions. A plan cannot determine whether this work is prerequisite, already complete, or part of implementation.

3. The workflow-gap description erases existing completion checks
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:27-29
   Quote:
       No formal review step exists in the worldbuilder workflow today.
       Documents go from draft-complete to finalized without a systematic
       check against their governing format rules.
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Entity skills already have formal “Self-Check Before Marking Complete” or “Completion Checklist” gates, and the character checklist explicitly requires section-appropriate compliance with `card-format.md`. The demonstrated gap is the lack of a separate adversarial reviewer, not the lack of any systematic format check. Misstating the baseline obscures how the new gate should integrate with, replace, or remain distinct from those checks.

4. One character-card trial does not establish a cross-entity pattern
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:29-32
   Quote:
       The trial showed that a
       single review pass catches an entire class of violations that
       accumulate during Q&A — the pattern is general to any document type
       where an agent produces prose under format constraints.
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The cited evidence is one autonomous character-card Q&A trial. It establishes the failure pattern for that workflow, but no concept, event, faction, location, story, seed, ingestion, or export output was tested. The assertion of generality is an unsupported inference and is being used to justify immediate universal rollout.

5. The fallback contradicts exemptions already present in full format documents
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:56-58
   Quote:
       When a format document has no review criteria section, the review
       skill uses the full format document as acceptance criteria with no
       exemptions — the absence of exemptions is the conservative default.
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: A full governing document can itself define exemptions. The current card format exempts Background from behavioral rules, the Body appearance preamble from the staging test, and working annotations from final content conventions. “Use the full format document” therefore conflicts with “no exemptions.” Literal implementation would recreate the Adeline false positives and reject content the governing document expressly permits.

6. The auto-fix boundary conflates finding certainty with repair safety
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:66-72, 97-103
   Quote:
       Clear format violations —
       mechanically identifiable, unambiguous rule matches — are fixed
       automatically. The fix preserves semantic content while conforming
       to format rules.
       [...]
       The default: if the rule text
       unambiguously matches the entry and fixing it requires only
       reformatting (not new content), it is a clear violation. If fixing
       requires rewriting with new behavioral content, sourcing from
       reference material, or making a characterization choice, it is
       ambiguous and escalates.
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Whether a violation exists and whether its repair is safe are independent decisions. An internal-state sentence can clearly violate a rule while having no semantics-preserving mechanical repair. The text also leaves the common middle case undefined: rewriting tense, removing commentary, splitting clauses, or rewriting existing behavioral content without adding new content is neither clearly “reformatting” nor “rewriting with new behavioral content.” Implementers must make case-by-case judgments despite the acceptance criterion requiring a precise boundary.

7. Reference material is both optional and conditionally mandatory without a routing rule
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:43-47, 105-108
   Quote:
       Inputs:
       the document to review (required), the path to its governing format
       document (required), and reference material used to produce the
       document (optional — Q&A answers, behavioral evidence, data profiles,
       or equivalent source documents).
       [...]
       When the document was produced from
       Q&A or source ingestion, the review skill also receives the
       reference material (behavioral evidence, data profile, or equivalent
       input documents).
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D1 presents reference material as optional, while D7 requires it for the main generation paths. The spec does not define how the caller determines provenance, enumerates all relevant sources, or behaves when a required source is unavailable. Consequently, semantic-fidelity checks can silently run without the evidence needed to perform them.

8. The D6 Body example invents a Because-clause exemption
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:86-91
   Quote:
       Example: "Body entries: one
       stageable sentence per entry, present tense, observable action only.
       Violation: multi-sentence entries, past tense, internal states
       outside a Because clause."
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: ADR 0004 and `card-format.md` grant the limited Because-clause staging exemption to Soul entries, not Body entries. The example scopes the check to Body and then permits internal states inside a Because clause, directly weakening the existing action-line convention.

9. D6 cannot express whole-document and cross-document checks
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:83-88
   Quote:
       D6. **Review criteria section structure.** The `## Review criteria`
       section in each format document follows this structure:

       **Checks** — a list of section-scoped rules the review enforces.
       Each check names the document section it applies to, the specific
       rule, and how a violation manifests.
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Existing gates include whole-document requirements such as mandatory-section presence, doctrine coverage or waiver, frontmatter, cross-reference consistency, and relationships checked against other notes. A structure limited to section-scoped rules has no representation for those checks, nor precedence when a section rule overlaps a content-type exemption. It is therefore not concrete enough to encode the governing criteria it is supposed to replace or supplement.

10. Reject and defer allow unresolved violations through the gate
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:78-81
   Quote:
       The user reviews the diff and can revert any
       auto-fix. Escalated findings require resolution (accept fix, reject,
       or defer with recorded reason) before the document is marked
       complete.
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: “Reject” does not distinguish rejecting a proposed repair from classifying the finding as invalid, and “defer” explicitly permits completion while the finding remains unresolved. No eligibility rule, waiver authority, recording location, or later enforcement behavior is defined. As written, any escalated format violation can pass the gate by selecting reject or defer.

11. Export outputs do not fit the gate’s required lifecycle or input model
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:60-64, 126
   Quote:
       D3. **Pre-completion gate.** The review fires as the final step
       before a document transitions to "complete" status. This applies to
       initial document creation (after Q&A produces a draft) and to
       platform-tuned export outputs (after export shapes the final form).
       A document is not marked complete until the review has run.
       [...]
       - Export skills gain the same step for platform-tuned outputs.
   Type: completeness
   Severity: major
   Effort-to-fix: large (reaches beyond the scoped change)
   Risk-of-fix: high (alters shared state, interfaces, or persisted data)
   Channel: fix
   Body: The existing export produces aggregate platform JSON and uses a structural “Self-Check Before Export Complete”; the output does not transition through the entity-note `complete` status. It is also governed by several sources—schema, field map, card assembly, and prose guidance—rather than the single required format-document path in D1. The spec defines neither the governing input nor ordering and ownership relative to the existing export quality gate.

12. Source ingestion is declared in scope but omitted from rollout
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:34-38, 119-123
   Quote:
       The worldbuilder has 8 entity types (character, concept, event,
       faction, location, story, world-foundation, source-ingestion), each
       with its own skill and format rules.
       [...]
       - Other entity format documents (concept, event, faction, location,
         story, world-foundation) need review criteria sections written as
         those formats are used and tested.
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The consequences enumerate every claimed entity type except source ingestion. That workflow produces one or more provenance-preserving reference documents and does not use the entity-note completion lifecycle. The plan therefore has no governing criteria, trigger, or exemption strategy for one of the eight types the universal design expressly includes.

13. Review criteria create a second normative copy of existing rules
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:50-55, 86-91
   Quote:
       Each format document
       includes a `## Review criteria` section listing: what the review
       checks (which format rules apply, by document section), what is
       exempt (sections or content types the review must not flag), and
       classification guidance
       [...]
       Each check names the document section it applies to, the specific
       rule, and how a violation manifests.
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: ADR 0004, `writing-style.md`, and entity formats already define the normative action-line and section rules. D6’s example restates those rules in another normative section, but the spec provides no canonical-source or conflict-precedence rule. Future edits can leave generation following one version while review enforces another, violating the requirement not to duplicate existing infrastructure.

14. The established slop-phrases review checklist is absent from the interface
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:42-48
   Quote:
       Inputs:
       the document to review (required), the path to its governing format
       document (required), and reference material used to produce the
       document (optional — Q&A answers, behavioral evidence, data profiles,
       or equivalent source documents). It does not need to know what entity
       type the document is — the format document carries all the rules.
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: `docs/slop-phrases.md` is the repository’s existing phrase-level review reference, but it is neither an input nor a required canonical dependency of Review criteria. Claiming the single format document carries all rules leaves the new gate free to omit that checklist or duplicate fragments of it into each format document. Neither outcome satisfies the required integration with existing infrastructure.

15. Completion requires only that review ran, not that repairs were revalidated
   Location: .claude/specs/2026-08-15-worldbuilder-document-review-gate.md:64, 74-81
   Quote:
       A document is not marked complete until the review has run.
       [...]
       After the review, the skill produces a
       report listing: findings auto-fixed (rule cited, before text, after
       text), findings escalated to the user (rule cited, evidence, why
       it is ambiguous), and findings scoped out by review criteria
       [...]
       Escalated findings require resolution (accept fix, reject,
       or defer with recorded reason) before the document is marked
       complete.
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Nothing requires the modified artifact to be reviewed again or to receive a clean verdict after auto-fixes and accepted fixes. A rewrite can introduce a new format violation, damage structure, or invalidate an earlier check, yet the only completion condition is that review ran and escalations received a disposition. This leaves the gate unable to verify its own output.

FINDINGS: 0 critical, 15 major, 0 minor, 0 nit

### Adjudication

| # | Verdict | Action |
|---|---------|--------|
| 1 | accept | Context aligned: "15 genuinely useful, 4 borderline, 3 false positives" |
| 2 | accept | Context corrected: exemptions identified, codification is a consequence |
| 3 | accept | "No formal review step" → "No adversarial review step"; existing self-checks acknowledged |
| 4 | accept | "The pattern is general" → "expected to generalize"; only character cards tested |
| 5 | accept | D2 fallback clarified: uses format doc's own section-scoped rules, without additional review-criteria exemptions |
| 6 | accept | D4 rewritten: violation certainty and repair safety separated; both must be clear for auto-fix |
| 7 | accept | D1 clarified: "required when produced from Q&A or ingestion; omitted only for documents with no source material" |
| 8 | accept | D6 example corrected: Because-clause exemption is Soul-only; Body example no longer references it |
| 9 | accept | D6 expanded: checks can be section-scoped or document-level (mandatory sections, doctrine coverage, frontmatter) |
| 10 | reject | User explicitly chose auto-fix with user override. Reject = finding is invalid per user's judgment. Defer with reason = explicit waiver. Gate ensures visibility and forces a decision, not compliance with every finding. |
| 11 | accept | Export integration deferred to Consequences; requires mature export format docs and lifecycle definition |
| 12 | accept | Source ingestion added to Consequences as a separate case (reference documents, not entity notes) |
| 13 | accept | D6 now references rules by name/location rather than restating them; new D8 declares shared dependencies |
| 14 | accept | New D8 requires all review criteria to reference slop-phrases.md and writing-style.md |
| 15 | accept (clarified) | D5 now states user diff review is the auto-fix quality check; second pass follows document cadence's substantial-rewrite rule |

## Round 2 — digest `65072dad…`, anchor `907dca50` (dirty), tokens 75954, 2026-08-15T15:48:05-05:00, 261s

Anchor: 907dca502067a52148b77eb32bdaecec9712f9bd (dirty tree)
Artifact digest: 65072dadacaca94beed17ebb42cff9dbf2adb8c89c47834996bef75ef0771b5e (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md

1. D3 is implemented only for character cards
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:272-281
   Quote: `### Task 3: Integrate into character skill completion workflow`
   
   `- Produces: the integration that makes the review gate fire for character cards`
   Type: completeness
   Severity: major
   Effort-to-fix: large (reaches beyond the scoped change)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: D3 applies the pre-completion gate to entity documents generally, and the plan’s own architecture says entity skills call the review skill. The repository has concept, event, faction, location, story, and world-foundation entity skills, but the plan adds a gate only to `worldbuilder-character`. D2’s fallback specifically permits those skills to use their full governing documents before dedicated Review criteria sections exist, so the absence of those integration tasks leaves reachable entity-document completion paths ungated.

2. The review is inserted before later document content is written
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:285-303
   Quote: `Add one new checklist item as the last item before the final `description` field item.`
   
   `- [ ] Adversarial review gate passed — invoke `worldbuilder-review` with this document, `card-format.md` as the governing format document, and any Q&A reference material. Resolve all escalated findings before proceeding.`
   
   `- [ ] `description` field written last and reflects the completed character`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: D3 requires the review to be the final step before completion. This sequence explicitly runs the review, then proceeds to write the `description` field. That field therefore bypasses the adversarial review, and the gate is not the final pre-completion step. The review item must follow all document-writing checklist items, including `description`.

3. Reference-material optionality is weakened and the caller passes only Q&A material
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:60-63,294-295
   Quote: `- Reference material (required when document was produced from Q&A or source ingestion; omitted for hand-written documents) — paths to source documents (behavioral evidence, data profiles, Q&A transcripts)`
   
   `- [ ] Adversarial review gate passed — invoke `worldbuilder-review` with this document, `card-format.md` as the governing format document, and any Q&A reference material. Resolve all escalated findings before proceeding.`
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: D1 allows omission only when no source material exists; being hand-written does not establish that condition. Task 3 then narrows the supplied material to “Q&A reference material,” even though the character workflow also accepts source documents in place of answers. Source-ingested character cards can therefore omit the evidence D7 needs for semantic-fidelity checks.

4. Tense changes are incorrectly classified as mechanically safe
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:71-74
   Quote: `- Is the repair safe? The fix requires only mechanical restructuring (splitting sentences, removing a word, reformatting a bullet to prose, correcting tense) without changing semantic content.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Changing past tense to present tense can turn a one-time historical event into an ongoing or habitual behavior. That changes semantic content and is not inherently mechanical. Including it unconditionally in the safe-repair examples permits an auto-fix that D4 requires the reviewer to escalate whenever semantic preservation is uncertain.

5. The new skill’s required frontmatter is not specified
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:54-58
   Quote: `Write the complete skill instruction file to `skills/worldbuilder-review/SKILL.md` with the following sections and content:`
   
   `**Header:** Skill name, one-line description ("Pre-completion adversarial review for worldbuilder documents"), reference to the governing spec.`
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Repository skills use YAML frontmatter with concrete `name` and `description` fields. “Header” does not require frontmatter delimiters, the exact `name: worldbuilder-review` field, or a precise governing-spec path. An executor can follow this instruction with a Markdown heading and produce a file that does not follow the established skill interface or cannot be discovered as intended.

6. Task 2 directly restates the rules it claims only to reference
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:165-181
   Quote: `- One stageable sentence per entry, present tense, observable action`
   
   `  only (this document, Body section — Entry format; Section-scoped`
   
   `  writing rules — Body and Soul). Violation: multi-sentence entries,`
   
   `  past tense, internal states`
   
   `- When/Behavior/Because structure embedded naturally (this document,`
   
   `  Soul section — Entry format). Violation: missing trigger, missing`
   
   `  behavior, missing reason`
   
   `- Observable action in When and Behavior; internal state in Because`
   
   `  clause only (this document, Section-scoped writing rules — Body`
   
   `  and Soul). Violation: internal states outside the Because clause`
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: These bullets reproduce the substantive rule text before their citations. The same pattern occurs for fact pairs, preamble format, relationship perspective, and Story Beats. This contradicts the plan’s global constraint and Acceptance Criterion 5, which require the section to reference existing format rules rather than create a second copy that can drift.

7. The Body preamble check strengthens “prose” into an unsupported paragraph requirement
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:156-159
   Quote: `- Prose paragraph before the first bullet (this document, Body`
   
   `  section — Appearance preamble). Violation: preamble formatted as a`
   
   `  bullet entry`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The cited Appearance preamble rule allows short descriptive prose consisting of sentences or descriptive clauses; it does not require a paragraph. The planned check would flag an allowed non-bulleted clause or other short prose form merely because it is not a paragraph.

8. The Background citation does not support all of its stated violations
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:146-149
   Quote: `- Fact-pair format: formative fact and what it made true (this`
   
   `  document, Background section). Violation: trait labels, behavioral`
   
   `  framing, abstract interpretation in the result half`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The cited Background section defines fact pairs and excludes behavioral framing, but it does not establish a Background-specific trait-label ban or an “abstract interpretation in the result half” rule. The note-wide trait restriction comes from `skills/writing-style.md` and the character completion checklist. This check therefore attributes requirements to the wrong location and invents a more specific result-half rule than the cited section contains.

9. Relationship checks cite the wrong rules and invent note-wide scope
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:187-199
   Quote: `- Perspective-focused: what this character does, not what the other`
   
   `  person does (`relationships.md`, core rule). Violation: entry`
   
   `  describes the other character's actions without describing this`
   
   `  character's behavior`
   
   `- Archetype declared in bold prefix (`relationships.md`, archetype`
   
   `  framework). Violation: missing archetype`
   
   `- Trait-word ban applies to descriptions of related characters (this`
   
   `  document, Section-scoped writing rules — Body and Soul, applied`
   
   `  note-wide)`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The perspective rule is developed in the perspective-focus and per-entry self-review text, not the document’s labeled “core rule.” The required bold archetype prefix is in “Writing Relationship Entries,” not the archetype framework. Most importantly, the cited Body-and-Soul section is explicitly section-scoped and never says “applied note-wide”; that scope comes from the shared writing doctrine or completion checklist. These inaccurate references defeat the intended single-source-of-truth design.

10. Entire addon rule sets are omitted from the Review criteria
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:187-208
   Quote: `**Relationship entries:**`
   
   `- Perspective-focused: what this character does, not what the other`
   
   `  person does (`relationships.md`, core rule). Violation: entry`
   
   `  describes the other character's actions without describing this`
   
   `  character's behavior`
   
   `- Archetype declared in bold prefix (`relationships.md`, archetype`
   
   `  framework). Violation: missing archetype`
   
   `- Only characters present before the story begins (this document,`
   
   `  Addon blocks — Relationships). Violation: entry for a character`
   
   `  who arrives during the story`
   
   `- Trait-word ban applies to descriptions of related characters (this`
   
   `  document, Section-scoped writing rules — Body and Soul, applied`
   
   `  note-wide)`
   
   ``
   
   `**Story Beats entries:**`
   
   `- Action-line convention, staging test, Orwell co-anchor apply (this`
   
   `  document, Addon blocks — Story Beats)`
   
   `- No meta-vocabulary (this document, Addon blocks — Story Beats)`
   
   `- Condition notes are factual, not prose-styled (this document,`
   
   `  Addon blocks — Story Beats)`
   
   ``
   
   `### Exempt`
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The Checks section ends without any checks for Intimate Dynamics, Voice/Dialogue structure, or most relationship requirements. Existing rules require Intimate Dynamics coverage and a friction point; Voice/Dialogue count, context, and Core-area coverage; and relationship counts, distribution, cast-web coverage, archetype fit, and Desire complications. Because Task 1 uses only the Review criteria brief whenever that section exists, these omissions prevent the adversarial review from enforcing those existing rules.

11. The Design Notes exemption is narrower than the stated trial decision
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:208-212
   Quote: `- **Design Notes:** excluded from all exports; builder vocabulary is`
   
   `  its purpose. Do not flag meta-vocabulary, builder terms, or`
   
   `  informal prose in Design Notes.`
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The governing scoping decision says Design Notes are exempt, while this text expressly exempts only three categories. It leaves unclear whether the reviewer should still apply trait-word, action-line, slop-phrase, and other document-level prose checks to Design Notes. That ambiguity can recreate the Adeline false positives the exemption is meant to eliminate.

12. “Accept fix” consumes a proposed repair the report never produces
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:78-86
   Quote: `- **Escalated** — for each: rule cited, entry text, why it is ambiguous (which part of the two-part test failed)`
   
   ``
   
   `**Presenting results section:**`
   
   `Present the report to the user. The user reviews the diff (this is the quality check on auto-fixes). The user can revert any auto-fix. Each escalated finding requires resolution before the document is marked complete:`
   
   `- **Accept fix** — apply the proposed repair`
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The Escalated report schema contains no proposed repair, yet the first resolution action requires one. A consumer cannot “apply the proposed repair” from the specified output. Either the report contract must include a proposal where one can safely be offered, or the resolution action must solicit a repair rather than assuming one exists.

13. The task interface declarations contradict the runtime dependency
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:44-46,118-120
   Quote: `- Consumes: nothing from other tasks`
   
   `- Produces: the skill instruction document that Tasks 2 and 3 depend on`
   
   ``
   
   `- Consumes: nothing`
   
   `- Produces: the first review criteria section, which the worldbuilder-review skill (Task 1) reads at runtime`
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Task 1 says it consumes nothing, while Task 2 explicitly produces the criteria Task 1 consumes at runtime. Task 1 also claims Task 2 depends on its output, but Task 2 declares no input and does not use the new skill artifact. These contracts cannot both describe the same task interface, making dependency and execution-order reasoning unreliable.

14. The verification commands cannot prove the properties they claim
   Location: .claude/plans/2026-08-15-worldbuilder-document-review-gate-implementation.md:91-100,250-261,306-309
   Quote: `Run: `grep -c "auto-fix\|escalat\|reference material\|semantic fidelity\|two-part\|scoped out" skills/worldbuilder-review/SKILL.md``
   
   `Expected: at least 6 matches confirming all key concepts are present.`
   
   ``
   
   `- [ ] **Step 2: Verify the section references rules, not restates them**`
   
   ``
   
   `Each check should name its source. Run:`
   
   ``grep -c "this document\|relationships.md\|slop-phrases.md\|writing-style.md\|adr/0004" skills/worldbuilder-character/card-format.md``
   
   `Expected: at least 15 matches (one per check plus shared dependencies).`
   
   ``
   
   ``grep "worldbuilder-review" skills/worldbuilder-character/SKILL.md``
   
   `Expected: one match in the Completion Checklist.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Counting lines containing broad keywords does not establish D1–D7 coverage; repeated mentions can satisfy the threshold while an input, report field, or decision is absent. Counting citations cannot detect rule restatement and the threshold is lower than the number of planned checks. The shared-dependency searches are not scoped to `### Checks`, so an existing occurrence elsewhere can pass. Finally, a repository-wide grep for the skill name cannot prove that the invocation is in the Completion Checklist or is the final pre-completion step. These commands can all emit their expected output while the acceptance criteria remain violated.

FINDINGS: 0 critical, 14 major, 0 minor, 0 nit

### Adjudication

| # | Verdict | Action |
|---|---------|--------|
| 1 | accept (partial) | Architecture note added: character-first, other skills get integration when format docs exist |
| 2 | accept | Review gate moved to last checklist item (after description field) |
| 3 | accept | Reference material wording fixed: "all reference material used to produce the document"; input description: "omitted only when no source material exists" |
| 4 | accept | "Correcting tense" removed from safe-repair examples; note added that tense changes are not inherently safe |
| 5 | accept (partial) | Header format specified concretely (heading + description + spec reference) |
| 6 | accept | Check entries trimmed: rule name + source location + violation pattern only |
| 7 | accept | "Prose paragraph" → "Short descriptive prose" |
| 8 | accept | Background trait-label citation corrected: sourced from writing-style.md, not Background section |
| 9 | accept | Relationship citations corrected: perspective-focus section, Writing Relationship Entries section |
| 10 | accept | Intimate Dynamics, Voice/Dialogue, and relationship coverage checks added |
| 11 | accept | Design Notes exemption broadened: "exempt from all review checks" |
| 12 | accept | "Accept fix" → "Fix — write and apply a repair"; escalated report now includes proposed repair when one can be offered |
| 13 | accept (partial) | Interface declarations clarified: "implementation-independent" for Tasks 1-2; runtime dependency is inherent, not a task interface |
| 14 | accept | Verification steps changed from grep-counting to explicit read-and-verify checklists |

