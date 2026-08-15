---
type: plan
title: Character card architecture implementation
description: 'Implementation plan for the character card architecture spec: card format
  definition, Q&A workflow skill rewrite, template update, intimate dynamics update,
  and generation pipeline retirement.'
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T13:26Z
resources: []
---

# Character card architecture implementation

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> core-workflow:subagent-driven-development (recommended) or
> core-workflow:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires
> the plan artifact's approval flip (see Approval Gate).

**Goal:** Replace the generation pipeline with a Q&A-into-card
workflow by rewriting the character skill files, creating a card
format reference document, and updating the character template.

**Architecture:** Three layers (card format definition, Q&A workflow
skill, export interface) per the
[approved spec](../specs/2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md).
The card format definition is a new reference document that skills
and export tools read. The Q&A workflow skill replaces the current
SKILL.md. The generation pipeline files are retired.

**Implementation research:**
[dossier](../research/2026-08-15-character-card-architecture-implementation-research.md)

**Tech Stack:** Markdown skill files, Obsidian templates, Python
build script (build-okf.py).

## Global Constraints

- Shipped content is model-neutral: never name a specific AI model
  in templates or skill instructions that reach end users.
- Skill prose follows the plugin's writing doctrine:
  `skills/writing-style.md`; phrase-level review checklist in
  `docs/slop-phrases.md`.
- OKF preset is generated: edit templates in `defaults/templates/`,
  then run `python scripts/build-okf.py`. Never hand-edit
  `defaults/okf.json`.

---

## Tasks

### Task 1: Card format definition and template update

Create the reference document that defines the block model, entry
structure, and section-scoped writing rules. Update the character
template to match. Retire the old framework, generation-rules, and
grader files. Rebuild the OKF preset.

**Spec anchor:** D1 (card format block model), D2.3 (entry
translation rules), D3 (what this replaces — retirement of
framework.md, generation-rules.md, and grader skill).

**Files:**
- Create: `skills/worldbuilder-character/card-format.md`
- Modify: `defaults/templates/character.md`
- Modify: `CONTEXT.md` (update character note type description if
  it references retired files)
- Modify: `skills/worldbuilder-character/relationships.md` (remove
  contrast declaration as mandatory coverage requirement — spec
  drops it from required doctrine)
- Delete: `skills/worldbuilder-character/framework.md`
- Delete: `skills/worldbuilder-character/generation-rules.md`
- Delete: `skills/worldbuilder-grader/` (if present — grader agent
  retired per D3)

**Interfaces:**
- Consumes: spec decisions D1.1–D1.4, D2.3, D3; existing template,
  retired files, `skills/writing-style.md`, `docs/slop-phrases.md`,
  OKF build contract
- Produces: `card-format.md`, updated `defaults/templates/character.md`,
  rebuilt `defaults/okf.json`, updated `relationships.md`, updated
  `CONTEXT.md` — all consumed by Task 2 and Task 3

- [ ] **Step 1: Write card-format.md**

Create `skills/worldbuilder-character/card-format.md` containing:

1. **Core block** — three sections (Background, Body, Soul) with
   entry format, target ranges, and entry examples per D1.1.
   Background: fact pairs, 4–8 entries. Body: stageable physical
   behavioral sentences, 3–5 entries. Soul: When/Behavior/Because
   prose, 5–8 entries.

2. **Depth-of-access grid** — the 3×3 conceptual model per D1.2.
   State explicitly that this is a Q&A coverage tool, not a
   document structure. Include the grid table from the spec.

3. **Required doctrine entries** — the six mandatory entries per
   D1.3, with provenance lines. Include the finalization gate:
   card not finalized until all present or explicitly waived.

4. **Addon blocks** — Relationships (reference relationships.md),
   Intimate Dynamics (reference intimate.md), Voice/Dialogue
   (2–4 composite snippets, situation categories, inclusion
   guidance) per D1.4. Voice/Dialogue: each snippet must include
   enough scene context to establish the situation; the working
   sheet notes which Core areas each example exercises.

5. **Section-scoped writing rules** — per D2.3. Background entries:
   Orwell co-anchor, no meta-vocabulary; staging test, action-line,
   and fact-to-manifestation do not apply (Background is factual,
   not behavioral). Body and Soul entries: action-line, staging
   test (Because clause exempt), trait-word ban, Orwell co-anchor,
   fact-to-manifestation. State these are overridable defaults.

6. **Working document conventions** — entries accumulate under
   section headings as bullet points. The document may carry
   optional annotations (grid position, coverage area) during
   creation; export strips these.

Source content from the spec decisions. Follow
`skills/writing-style.md` for the prose style. Check against
`docs/slop-phrases.md`.

Verify card-format.md contains all required sections:

```bash
for section in "Core block" "Depth-of-access" "Required doctrine" "Addon" "writing rules"; do grep -q "$section" skills/worldbuilder-character/card-format.md && echo "OK: $section" || echo "MISSING: $section"; done
```

Expected: all OK.

- [ ] **Step 2: Update character template**

Edit `defaults/templates/character.md`:

Remove the Design Notes section entirely (Session Notes, Builder
Context, Structured Doctrine). The Q&A conversation replaces this
— there is no Design Notes section in the new card format.

Keep the section headers matching the card format definition:
Background, Body, Soul. Keep the Relationships section header.
Add section headers for addon blocks: Intimate Dynamics (with a
note that it is included only when flagged), Voice / Dialogue
(with a note that it is included when relevant).

Update placeholder bullets under each section to match the new
entry format from card-format.md. Include the "For future agents"
preamble referencing the new skill and card-format.md.

- [ ] **Step 3: Update relationships.md and CONTEXT.md**

Edit `skills/worldbuilder-character/relationships.md`: remove
"Contrast declaration" from mandatory coverage requirements if
present. The spec drops it from required doctrine — it remains
good practice but is no longer gated.

Edit `CONTEXT.md`: update the character note type description to
reference `card-format.md` instead of framework.md or
generation-rules.md if those are mentioned.

- [ ] **Step 4: Retire old files**

Delete `skills/worldbuilder-character/framework.md` and
`skills/worldbuilder-character/generation-rules.md`. If
`skills/worldbuilder-grader/` exists (the grader agent skill),
delete it — the grader is retired per D3 (quality is addressed
at creation time in the Q&A workflow, not post-generation).

If `scripts/detect_input_echo.py` exists, delete it — it served
the grader agent. Deslop/deframe scripts (`scripts/deslop.py`,
`scripts/deframe.py`) stay if present — they are a separate
concern for source-material extraction.

Verify no remaining files reference retired documents:

```bash
grep -r "framework\.md\|generation-rules\.md\|worldbuilder-grader" skills/ defaults/ CONTEXT.md docs/ --include="*.md" -l
```

Expected: only SKILL.md (rewritten in Task 2). Any other hits
must be updated to reference card-format.md or removed.

- [ ] **Step 5: Rebuild OKF preset**

```bash
python scripts/build-okf.py
```

Verify the build succeeds and `defaults/okf.json` contains the
updated template content:

```bash
python -c "import json; d=json.load(open('defaults/okf.json')); c=d['types']['character']; t=c.get('template',''); ok='Background' in t and 'Design Notes' not in t and 'Voice' in t; print('OK' if ok else 'FAIL: check template content')"
```

Expected: `OK`

- [ ] **Step 6: Commit**

```bash
git add skills/worldbuilder-character/card-format.md \
  defaults/templates/character.md \
  defaults/okf.json \
  skills/worldbuilder-character/relationships.md \
  CONTEXT.md
git rm skills/worldbuilder-character/framework.md \
  skills/worldbuilder-character/generation-rules.md
# Also git rm any grader files deleted in step 4
git commit -m "feat: card format definition and template — block model, section-scoped rules

Replaces framework.md and generation-rules.md with card-format.md.
Updates character template to remove Design Notes and reflect the
block model. Retires grader agent. Removes contrast declaration
as mandatory from relationships coverage."
```

---

### Task 2: Q&A workflow skill rewrite

Rewrite SKILL.md from a generation-oversight skill to a
conversational extraction workflow skill per D2.

**Spec anchor:** D2 (Q&A workflow — D2.1 collaboration model,
D2.2 question sequencing, D2.4 coverage checking, D2.5 working
document).

**Files:**
- Rewrite: `skills/worldbuilder-character/SKILL.md`

**Interfaces:**
- Consumes: `card-format.md` (from Task 1) — references it as the
  governing document for entry format and writing rules
- Produces: the skill entry point that agents invoke when building
  a character

- [ ] **Step 1: Write the new SKILL.md**

Rewrite `skills/worldbuilder-character/SKILL.md` containing:

1. **Opening philosophy** — keep the one-sentence framing: a
   character for an LLM-powered game is a behavioral
   specification. Reference `card-format.md` as the governing
   document for entry format and writing rules.

2. **Collaboration model** — per D2.1. The AI asks targeted
   questions, the human answers, the AI translates answers into
   card-format entries, the human approves or revises. The human
   can always override: writing entries directly, editing
   AI-proposed entries, or skipping questions. Source material can
   substitute for human answers.

3. **Session opening** — determine which addon blocks to include.
   Relationships: ask whether the character is part of a cast.
   Intimate Dynamics: check the project-plan flag. Voice/Dialogue:
   recommend when the character will be exported to platforms
   supporting example dialogue or when voice distinctiveness
   matters. Record the decision.

4. **Session flow** — per D2.2. Block order: Core (Background →
   Body → Soul), then selected addon blocks (Relationships →
   Intimate Dynamics → Voice/Dialogue). Within each Core section,
   follow the depth-of-access progression (immediate → over time
   → hidden/foundational). Addon blocks follow their own coverage
   structure.

5. **Entry translation** — reference card-format.md for section-
   scoped writing rules. The AI applies the rules when translating
   a human answer into an entry. State that rules are overridable
   defaults.

6. **Coverage checking** — per D2.4. After each Core section,
   report depth-of-access observations (advisory, not
   deterministic) and suggest follow-up questions for under-
   represented columns. The user can accept the suggestion or
   mark the section as complete. After full Core block, check for
   missing mandatory doctrine entries (D1.3). Missing mandatory
   entries must be addressed before finalization or explicitly
   waived with a recorded reason.

6. **Working document** — per D2.5. Entries accumulate in the
   character note as approved. Each section is a markdown heading,
   entries are bullet points.

7. **Addon block guidance** — reference relationships.md for
   Relationships, intimate.md for Intimate Dynamics. For
   Voice/Dialogue: list the situation categories, state the user
   picks 2–4, each snippet is a composite showing pulling from
   multiple Core areas.

9. **Completion checklist** — replace the current self-check
   checklist. New checklist covers: all mandatory doctrine entries
   present or waived, each Core section has at least one entry
   (target ranges are guidance not gates), selected addon blocks
   completed, no trait adjectives, entries follow section-
   appropriate writing rules per card-format.md.

- [ ] **Step 2: Verify references**

Check that SKILL.md references only files that exist after Task 1:

```bash
grep -oP '(?<=\()[\w/.-]+\.md(?=\))' skills/worldbuilder-character/SKILL.md | while read f; do test -f "skills/worldbuilder-character/$f" || test -f "$f" || echo "MISSING: $f"; done
```

Expected: no output (all referenced files exist).

Check that no reference to framework.md or generation-rules.md
remains:

```bash
grep -c "framework\.md\|generation-rules\.md" skills/worldbuilder-character/SKILL.md
```

Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-character/SKILL.md
git commit -m "feat: Q&A workflow skill — conversational extraction replaces generation

Rewrites SKILL.md for the conversational extraction workflow:
AI asks, human answers, AI translates to card entries, human
approves. References card-format.md for entry format and
section-scoped writing rules."
```

---

### Task 3: Intimate dynamics update

Update intimate.md with entry shape guidance and depth-of-access
lens per D1.4.

**Spec anchor:** D1.4 (Intimate Dynamics addon block definition).

**Files:**
- Modify: `skills/worldbuilder-character/intimate.md`

**Interfaces:**
- Consumes: `card-format.md` (from Task 1) — consistent entry
  format and writing rules
- Produces: updated intimate.md referenced by SKILL.md (Task 2)

- [ ] **Step 1: Update intimate.md**

Edit `skills/worldbuilder-character/intimate.md`:

Add entry shape guidance: entries are behavioral prose in the same
format as Soul (When/Behavior/Because embedded naturally). Target
1–2 entries per coverage area.

Add a brief note that the depth-of-access progression applies as a
conceptual lens: immediate intimate behavior, how dynamics shift
with trust, hidden emotional needs the dynamic serves.

Keep the existing content: three coverage areas (attraction
expression, hesitation and limits, specific dynamic), mandatory
friction point, existing examples. The coverage areas and friction
point requirement are unchanged — this is additive guidance, not
a rewrite.

Remove any reference to "Design Notes" as a destination for
exploration answers — Design Notes are retired. The Q&A
conversation now captures exploration directly.

Add a reference to card-format.md as the governing document for
entry format.

- [ ] **Step 2: Verify content**

Check that intimate.md contains the required additions and no
stale references:

```bash
echo "--- Required additions ---"
grep -c "card-format" skills/worldbuilder-character/intimate.md
grep -c "depth-of-access\|immediate.*trust.*hidden\|over time" skills/worldbuilder-character/intimate.md
echo "--- Stale references ---"
grep -c "Design Notes" skills/worldbuilder-character/intimate.md
```

Expected: first two counts >= 1 each, last count = 0.

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-character/intimate.md
git commit -m "feat: intimate dynamics — entry shape and depth-of-access guidance

Adds entry shape (behavioral prose, 1-2 per coverage area) and
depth-of-access conceptual lens to intimate dynamics skill."
```
