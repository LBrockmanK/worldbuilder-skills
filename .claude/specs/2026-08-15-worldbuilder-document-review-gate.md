---
type: spec
title: Worldbuilder document review gate
description: Pre-completion adversarial review step for all worldbuilder documents
  — standalone review skill with format-doc-embedded acceptance criteria, auto-fix
  of clear violations, and escalation of ambiguous findings
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T20:38Z
resources: []
---

# Worldbuilder document review gate

## Context

The Adeline character card trial (2026-08-15) ran an adversarial review
against a completed card using card-format.md as acceptance criteria.
Of 22 major findings, 15 were genuinely useful, 4 were borderline
(debatable rule application), and 3 were false positives caused by
missing scope exemptions (Design Notes, working annotations, in-world
quoted text). These exemptions have been identified; their
codification in review criteria sections is part of this spec's
consequences.

Entity skills already have self-check gates (completion checklists
that verify section compliance). No adversarial review step exists —
no external check by a reviewer that did not produce the document.
The trial showed that a single adversarial pass catches an entire
class of violations that accumulate during Q&A: entries too literary
and interpretive for the format's staging-test and action-line
requirements. The pattern is expected to generalize to any document
type where an agent produces prose under format constraints, though
only character cards have been tested.

The worldbuilder has entity types (character, concept, event, faction,
location, story, world-foundation) and a source-ingestion workflow,
each with its own skill and format rules. ADR 0004 (action-line
convention) and the staging test apply across all behavioral sections.
The phrase-level review checklist (`docs/slop-phrases.md`) applies to
all prose output. A review gate must work for any document type
without per-type reimplementation.

## Decisions

D1. **Standalone review skill.** Create `worldbuilder-review` as a
skill that any entity skill calls at document completion time. Inputs:
the document to review (required), the path to its governing format
document (required), and reference material used to produce the
document (required when the document was produced from Q&A or source
ingestion; omitted only for documents with no source material, such
as hand-written notes). It does not need to know what entity type the
document is — the format document carries all the rules.

D2. **Format-doc-embedded review criteria.** Each format document
includes a `## Review criteria` section listing: what the review
checks (which rules apply), what is exempt (content types the review
must not flag), and classification guidance (what constitutes a clear
violation vs. a judgment call). The review skill reads this section
as its brief. When a format document has no review criteria section,
the review skill uses the full format document as acceptance criteria
— including the format document's own section-scoped rules and
exemptions (e.g., Background exempt from behavioral rules, Body
preamble exempt from staging test), but without the additional
review-specific exemptions and judgment-call guidance that a review
criteria section provides.

D3. **Pre-completion gate.** The review fires as the final step
before an entity document transitions to "complete" status. This
applies to initial document creation (after Q&A produces a draft).
Export integration is deferred until export format documents are
mature enough to carry review criteria and the export lifecycle's
relationship to entity-note status is defined. A document is not
marked complete until the review has run.

D4. **Auto-fix with escalation.** Whether a violation exists and
whether its repair is safe are independent decisions. A violation is
clear when the rule text unambiguously matches the entry. A repair is
safe when it requires only mechanical restructuring (splitting
sentences, removing a word, reformatting a bullet to prose) without
changing semantic content. Auto-fix applies only when both the
violation is clear and the repair is safe. If either the violation
identification or the repair is ambiguous — the rule application is
debatable, the repair requires new behavioral content, sourcing from
reference material, or a characterization choice — the finding
escalates to the user with the specific rule cited and the evidence
quoted.

D5. **Completion report.** After the review, the skill produces a
report listing: findings auto-fixed (rule cited, before text, after
text), findings escalated to the user (rule cited, evidence, why it
is ambiguous), and findings scoped out by review criteria (rule and
exemption cited). The user reviews the diff — this review is the
quality check on auto-fixes. The user can revert any auto-fix.
Escalated findings require resolution (accept fix, reject as invalid,
or defer with recorded reason) before the document is marked
complete. A second review pass follows the document cadence's
substantial-rewrite rule: warranted only when fixes rewrote the
document substantially enough that the user would otherwise approve
materially unreviewed text.

D6. **Review criteria section structure.** The `## Review criteria`
section in each format document follows this structure:

**Checks** — rules the review enforces, organized by scope. Checks
may be section-scoped (applying to a specific document section) or
document-level (applying across the whole document: mandatory section
presence, doctrine coverage, frontmatter requirements, cross-reference
consistency). Each check references the rule by name and location in
the format document or in a shared resource (`docs/slop-phrases.md`,
`writing-style.md`, ADR 0004) — it does not restate the rule. It
names the scope (section or document-level) and how a violation
manifests. Example: "Soul entries — When/Behavior/Because structure
(this document, Soul section): observable action in When and Behavior;
internal state in Because clause only. Violation: internal states
outside the Because clause."

**Exempt** — a list of content types or document sections the review
must not flag, with the reason for each exemption. Example: "Design
Notes: excluded from all exports; builder vocabulary is its purpose."

**Judgment calls** — guidance for distinguishing clear violations
from ambiguous findings, supplementing D4's general rule with
format-specific cases.

D7. **Source-data cross-check.** When reference material is provided,
auto-fixes that rewrite content must preserve semantic fidelity to the
source data. If a fix would require inventing behavioral detail not
present in the source, it escalates rather than fabricating.

D8. **Shared review dependencies.** The review criteria in every
format document must reference `docs/slop-phrases.md` as a
phrase-level check and `writing-style.md` as the prose doctrine.
These are shared resources, not per-format rules — the review
criteria section points to them rather than duplicating their content.

## Consequences

- card-format.md needs a `## Review criteria` section codifying the
  Adeline trial's scoping decisions (Design Notes exempt, working
  annotations exempt, in-world quoted text exempt from trait-word
  ban, Voice/Dialogue exempt from card-body writing rules) and
  referencing the shared dependencies (slop-phrases.md,
  writing-style.md, ADR 0004).
- Other entity format documents (concept, event, faction, location,
  story, world-foundation) need review criteria sections written as
  those formats are used and tested. Until then, the review runs
  against the full format doc with the D2 fallback behavior.
- Source ingestion produces reference documents, not entity notes with
  the standard completion lifecycle. Its review criteria will be
  defined when the ingestion format is tested; until then, source
  ingestion outputs are not gated.
- Export integration is deferred. The export workflow produces
  aggregate platform output governed by multiple sources (schema,
  field map, card assembly, prose guidance) and uses its own
  structural self-check. Defining the review gate's relationship to
  the export lifecycle requires export format documents mature enough
  to carry review criteria.
- Entity skills gain a final workflow step: call `worldbuilder-review`
  before marking a document complete.
- The review skill itself needs implementation: adversarial review
  dispatch, auto-fix logic, escalation routing, and report
  generation.

## Notes (non-normative)

The Adeline trial's finding breakdown (15 genuinely useful, 4
borderline, 3 false positives) suggests that with review criteria
properly codified, the false-positive rate drops to near zero and
the borderline rate stays low. The main value is catching the
systematic pattern where Q&A-produced prose drifts literary — the
review enforces the format discipline the format demands.
