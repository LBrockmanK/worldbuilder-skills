---
type: plan
title: Worldbuilder document review gate implementation
description: Implementation plan for the review gate spec — new worldbuilder-review
  skill, card-format.md review criteria section, character skill integration
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T21:19Z
resources:
- '[[2026-08-15-worldbuilder-document-review-gate]]'
- '[[2026-08-15-implementation-research-worldbuilder-document-review-gate]]'
---

# Worldbuilder document review gate implementation

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).

**Goal:** Add an adversarial review gate that fires before any worldbuilder document is marked complete — a standalone skill that reviews against format-doc-embedded criteria, auto-fixes clear violations, and escalates ambiguous findings.

**Architecture:** A new `worldbuilder-review` skill provides the review workflow. Each format document embeds a `## Review criteria` section (checks, exemptions, judgment-call guidance). Entity skills call the review skill as their final completion step. The first format doc to get criteria is `card-format.md`. Other entity skills get integration when their format documents are created or when the review is tested against their SKILL.md.

**Tech Stack:** Skill instruction documents (Markdown). No code.

**Research dossier:** [implementation-research-worldbuilder-document-review-gate.md](../research/2026-08-15-implementation-research-worldbuilder-document-review-gate.md)

## Global Constraints

- All deliverables are skill instruction documents (Markdown), not code.
- Review criteria sections reference rules by name and location — they never restate rules (D6).
- Every review criteria section must reference `docs/slop-phrases.md` and `skills/writing-style.md` as shared dependencies (D8).
- Skill instruction files follow the established `SKILL.md` naming convention.
- Follow the project's writing doctrine: plain, concrete, no filler (`skills/writing-style.md`).

---

### Task 1: Create the worldbuilder-review skill

**Spec anchors:** D1 (standalone skill), D4 (auto-fix with escalation), D5 (completion report), D7 (source-data cross-check)

**Files:**
- Create: `skills/worldbuilder-review/SKILL.md`

**Interfaces:**
- Consumes: nothing (implementation-independent of other tasks)
- Produces: the skill instruction document. Task 3 references this skill by name in the completion checklist. At runtime, the skill reads whatever review criteria section exists in the format doc passed to it.

- [ ] **Step 1: Create the skill directory**

```bash
mkdir -p skills/worldbuilder-review
```

- [ ] **Step 2: Write SKILL.md**

Write the complete skill instruction file to `skills/worldbuilder-review/SKILL.md` with the following sections and content:

**Header:** `# worldbuilder-review`, one-line description: "Pre-completion adversarial review for worldbuilder documents." Reference: governed by the [worldbuilder document review gate spec](../../.claude/specs/2026-08-15-worldbuilder-document-review-gate.md).

**Inputs section:**
- Document to review (required) — path to the worldbuilder document
- Governing format document (required) — path to the format doc (e.g., `card-format.md`)
- Reference material (required when the document was produced from Q&A or source ingestion; omitted only when no source material exists) — paths to source documents (behavioral evidence, data profiles, Q&A transcripts, or equivalent)

**Process section — five phases:**

Phase 1: Read review criteria. Open the format document's `## Review criteria` section. If it exists, use its Checks, Exempt, and Judgment calls as the review brief. If it does not exist, use the full format document as acceptance criteria — including the format document's own section-scoped rules and exemptions — but without additional review-specific exemptions or judgment-call guidance.

Phase 2: Review. Read each entry in the document. For each entry, check it against every applicable rule from the Checks list (section-scoped checks filtered by which section the entry belongs to; document-level checks applied across the whole document). Also check against `docs/slop-phrases.md` and `skills/writing-style.md`. Record each finding with: the rule violated (by name and location in the format doc or shared resource), the entry text, and the specific violation.

Phase 3: Classify findings. For each finding, apply the two-part test from D4:
- Is the violation clear? The rule text unambiguously matches the entry.
- Is the repair safe? The fix requires only mechanical restructuring (splitting sentences, removing a word, reformatting a bullet to prose) without changing semantic content. Tense changes are not inherently safe — changing past to present can turn a historical event into an ongoing behavior.
Auto-fix applies only when both are true. If either is ambiguous — the rule application is debatable, the repair requires new behavioral content, sourcing from reference material, or a characterization choice — the finding escalates. Check the Judgment calls section of the review criteria for format-specific classification guidance.

Phase 4: Apply auto-fixes. For each auto-fix finding, rewrite the entry to comply with the rule. Preserve semantic content. When reference material is provided, verify the fix preserves semantic fidelity to the source data (D7). If a fix would require inventing detail not in the source, reclassify as escalated. Check exempt content types before fixing — do not modify exempt sections or content.

Phase 5: Generate report. Produce a completion report with three sections:
- **Auto-fixed** — for each: rule cited (name and location), before text, after text
- **Escalated** — for each: rule cited, entry text, why it is ambiguous (which part of the two-part test failed), and a proposed repair when one can be offered without a characterization choice
- **Scoped out** — for each: rule name, exemption cited (from the Exempt list)

**Presenting results section:**
Present the report to the user. The user reviews the diff (this is the quality check on auto-fixes). The user can revert any auto-fix. Each escalated finding requires resolution before the document is marked complete:
- **Fix** — write and apply a repair (the user or agent creates the fix, using the proposed repair as a starting point when one was offered)
- **Reject** — the finding is invalid (record reason)
- **Defer** — acknowledged, not addressing now (record reason)

A second review pass is warranted only when fixes rewrote the document substantially enough that the user would otherwise approve materially unreviewed text.

- [ ] **Step 3: Verify spec coverage**

Read the written SKILL.md and verify each spec decision is present:
- D1: Three inputs listed with correct optionality (document required, format doc required, reference material required when source exists)
- D4: Two-part test stated (violation clear AND repair safe); tense changes noted as not inherently safe
- D5: Report has three sections (auto-fixed with before/after, escalated with proposed repair when possible, scoped out)
- D7: Phase 4 includes source-data fidelity check

- [ ] **Step 4: Commit**

```bash
git add skills/worldbuilder-review/SKILL.md
git commit -m "feat: add worldbuilder-review skill — pre-completion adversarial review gate"
```

---

### Task 2: Write Review criteria section in card-format.md

**Spec anchors:** D2 (format-doc-embedded criteria), D6 (section structure), D8 (shared dependencies)

**Files:**
- Modify: `skills/worldbuilder-character/card-format.md` (append after Working document conventions section, currently the last section)

**Interfaces:**
- Consumes: nothing (implementation-independent of other tasks)
- Produces: the first review criteria section in a format document

- [ ] **Step 1: Write the Review criteria section**

Append the following section to the end of `skills/worldbuilder-character/card-format.md`:

```markdown
---

## Review criteria

Rules the pre-completion review enforces, organized by scope. Each
check names the rule and its source location, then describes the
violation pattern — it does not reproduce the full rule text.

### Checks

**Document-level:**
- Required doctrine entries present or waived (this document,
  Required doctrine entries section). Violation: missing entry with
  no recorded waiver.
- Each Core section has at least one entry (this document, Core block
  section). Violation: empty section.
- Slop-phrase scan (`docs/slop-phrases.md`, full checklist).
  Violation: any listed phrase present in card prose.
- Writing doctrine compliance (`skills/writing-style.md`;
  `.claude/adr/0004-action-line-style-model.md`). Violation: any
  failure mode listed in those documents.

**Background entries:**
- Fact-pair format (this document, Background section). Violation:
  result half contains behavioral framing instead of a concrete fact.
- No meta-vocabulary (this document, Section-scoped writing rules —
  Background).
- Orwell co-anchor (this document, Section-scoped writing rules —
  Background).
- Trait-word ban (`skills/writing-style.md`, trait-word ban).
  Violation: trait adjective anywhere in a Background entry.

**Body preamble:**
- Short descriptive prose before the first bullet (this document,
  Body section — Appearance preamble). Violation: preamble formatted
  as a bullet entry.
- Staging test exempt (this document, Body section — Appearance
  preamble).
- Orwell co-anchor and trait-word ban apply.

**Body entries:**
- Entry format (this document, Body section) and action-line
  convention (Section-scoped writing rules). Violation:
  multi-sentence entries, past tense, internal states.
- Staging test (this document, Section-scoped writing rules — Body
  and Soul). Violation: entries a director cannot stage.
- Trait-word ban. Violation: adjective labels instead of behavior.

**Soul entries:**
- Entry format (this document, Soul section). Violation: missing
  When trigger, missing Behavior, missing Because reason.
- Action-line convention (Section-scoped writing rules — Body and
  Soul). Violation: internal states outside the Because clause.
- Staging test; Because clause exempt.
- Trait-word ban.

**Relationship entries:**
- Perspective-focus (`relationships.md`, perspective-focus section
  and per-entry self-review). Violation: entry describes the other
  character's actions without describing this character's behavior.
- Archetype in bold prefix (`relationships.md`, Writing Relationship
  Entries section). Violation: missing archetype.
- Pre-story characters only (this document, Addon blocks —
  Relationships). Violation: entry for a character who arrives
  during the story.
- Trait-word ban. Violation: trait adjective describing a related
  character.
- Coverage requirements (`relationships.md`, Coverage Requirements
  section). Violation: count below the minimum for the character's
  role.

**Intimate Dynamics entries (when included):**
- When/Behavior/Because format, same as Soul (this document, Addon
  blocks — Intimate Dynamics; `intimate.md`).
- Three coverage areas present with 1-2 entries each
  (`intimate.md`).
- Mandatory friction point present (`intimate.md`). Violation:
  no internal contradiction in intimate behavior.

**Voice / Dialogue (when included):**
- 2-4 composite snippets (`this document, Addon blocks — Voice /
  Dialogue`). Violation: count outside range.
- Each snippet pulls from multiple Core areas (this document, Addon
  blocks — Voice / Dialogue). Violation: snippet exercises only one
  area.
- Sufficient scene context to establish the situation.

**Story Beats entries (when included):**
- Action-line convention, staging test, Orwell co-anchor (this
  document, Addon blocks — Story Beats).
- No meta-vocabulary.
- Condition notes are factual, not prose-styled.

### Exempt

- **Design Notes:** exempt from all review checks. Design Notes are
  excluded from all exports and exist as a builder record.
- **Working annotations** (doctrine labels like `*(core want)*`,
  `*(false belief)*`): stripped at export; drafting aids, not
  meta-vocabulary violations.
- **In-world quoted text:** exempt from the trait-word ban. Text
  quoted from the source material (game dialogue, in-world documents)
  is not prose the card author chose.
- **Voice / Dialogue speech lines:** in-character dialogue follows
  the character's speech patterns, not the card-body writing rules.
  Stage directions and situation descriptions within Voice / Dialogue
  are not exempt.

### Judgment calls

The general rule (D4 of the governing spec): auto-fix when the
violation is clear AND the repair is safe (mechanical restructuring
only). Escalate when either is ambiguous.

Character-card-specific guidance:
- Splitting a multi-sentence Body entry into one sentence: auto-fix
  when the entry contains one core behavior and the extra sentences
  are elaboration. Escalate when the entry contains multiple distinct
  behaviors that each need their own entry.
- Removing an internal state from a Soul entry: auto-fix when the
  internal state can be replaced by the observable behavior already
  described in the entry. Escalate when removing it would lose the
  entry's meaning and a replacement behavior must be sourced from
  reference material.
- Reformatting a bullet preamble to prose: always auto-fix (purely
  mechanical).
- Adding a missing relationship archetype: always escalate (requires
  a characterization choice about which archetype fits).
- Rewriting a Background fact-pair result: escalate when the current
  result is a trait label or abstract interpretation and a concrete
  replacement must be sourced from reference material.
```

- [ ] **Step 2: Verify checks reference rules, not restate them**

Read the written Review criteria section. For each Check entry, verify it names a source location (document section, external file, or ADR) and describes a violation pattern, without reproducing the full rule text from the source. Verify the Exempt list entries each give a reason.

- [ ] **Step 3: Verify shared dependencies referenced (D8)**

Confirm both shared resources appear in the Checks section:
`grep "slop-phrases.md" skills/worldbuilder-character/card-format.md`
`grep "writing-style.md" skills/worldbuilder-character/card-format.md`
Expected: at least one match each within the Review criteria section.

- [ ] **Step 4: Commit**

```bash
git add skills/worldbuilder-character/card-format.md
git commit -m "feat: add Review criteria section to card-format.md — checks, exemptions, judgment calls"
```

---

### Task 3: Integrate into character skill completion workflow

**Spec anchor:** D3 (pre-completion gate)

**Files:**
- Modify: `skills/worldbuilder-character/SKILL.md:161-174` (Completion Checklist section)

**Interfaces:**
- Consumes: the worldbuilder-review skill name from Task 1
- Produces: the integration that makes the review gate fire for character cards

- [ ] **Step 1: Add the review gate to the completion checklist**

In `skills/worldbuilder-character/SKILL.md`, find the Completion Checklist section (line 161). Add one new checklist item as the last item in the checklist — after all document-writing items including the `description` field. The checklist currently ends:

```markdown
- [ ] `description` field written last and reflects the completed character
```

Append after it:

```markdown
- [ ] Adversarial review gate passed — invoke `worldbuilder-review` with this document, `card-format.md` as the governing format document, and all reference material used to produce the document. Resolve all escalated findings before marking complete.
```

- [ ] **Step 2: Verify the integration**

Read the Completion Checklist in `skills/worldbuilder-character/SKILL.md`. Verify:
- The review gate item is the last item in the checklist
- It names `worldbuilder-review` as the skill to invoke
- It requires `card-format.md` as the format document
- It requires "all reference material" (not just Q&A material)

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-character/SKILL.md
git commit -m "feat: add review gate to character skill completion checklist"
```
