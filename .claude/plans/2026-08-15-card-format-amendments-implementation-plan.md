---
type: plan
title: Card Format Amendments — Implementation Plan
description: Implementation plan for Body appearance preamble (D1) and Story Beats
  addon block (D2) amendments to card-format.md and related files.
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T17:36Z
resources: []
---

# Card Format Amendments — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).

**Goal:** Amend the character card format to add a Body appearance preamble and a Story Beats addon block, and propagate those changes to the skill, template, preset, and export files.

**Architecture:** Two spec decisions (D1, D2) propagated through the file dependency chain: card-format.md (source of truth) → SKILL.md (workflow) → character template (scaffolding) → OKF preset (generated) → export files (consumers). All changes are markdown content edits plus one JSON regeneration.

**Tech Stack:** Markdown, JSON (generated), Python (`scripts/build-okf.py`)

**Research dossier:** [Implementation Research](../research/2026-08-15-implementation-research-card-format-amendments.md)

**Governing spec:** [Card Format Amendments Spec](../specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md)

## Global Constraints

- All prose in card-format.md and SKILL.md follows `skills/writing-style.md`
- The OKF preset is generated: edit `defaults/templates/character.md`, then run `python scripts/build-okf.py`. Never hand-edit `defaults/okf.json`
- Shipped content is model-neutral: never name a specific AI model in templates or skill instructions

---

### Task 1: Card Format and Skill Amendments (authoritative definitions)

**Files:**
- Modify: `skills/worldbuilder-character/card-format.md:23-33` (Body section)
- Modify: `skills/worldbuilder-character/card-format.md:83-111` (addon blocks section)
- Modify: `skills/worldbuilder-character/card-format.md:139-141` (working-document conventions)
- Modify: `skills/worldbuilder-character/SKILL.md:32-41` (session opening)
- Modify: `skills/worldbuilder-character/SKILL.md:44-69` (session flow, including ordered addon list)
- Modify: `skills/worldbuilder-character/SKILL.md:123-126` (story notes)
- Modify: `skills/worldbuilder-character/SKILL.md:137-149` (completion checklist)

**Interfaces:**
- Consumes: spec decisions D1 and D2 verbatim
- Produces: updated card-format.md and SKILL.md that Task 2 reads from

- [x] **Step 1: Add Body appearance preamble to card-format.md**

In the Body section (after the `### Body` heading and before `**Entry format:**`), insert the preamble definition before the existing entry format. The section should read:

```markdown
### Body

Physical presence and habits. What you see and experience physically.

**Appearance preamble:** Body opens with short descriptive prose
(sentences or descriptive clauses) covering the character's static
physical appearance. The preamble is exempt from the staging test.
Orwell co-anchor and trait-word ban apply. No meta-vocabulary from
the builder abstraction layer. Content: hair, eyes, skin, build,
distinguishing physical features, default or seasonal clothing, and
hidden static features (scars, marks, tattoos) when relevant —
everything about what this person looks like, regardless of
depth-of-access.

**Entry format:** One stageable sentence per entry. Describes
physical behavior that can be observed.
```

Leave the existing target range and example entries unchanged.

- [x] **Step 2: Add Story Beats addon block to card-format.md**

After the Voice / Dialogue addon block section, add:

```markdown
### Story Beats

Optional. Included when the character has triggerable narrative
scenarios worth specifying. Labeled prose blocks — each entry has a
short title, a trigger/condition note, and 2-4 sentences of scenario
prose describing: the setup (where and when), the key action or
exchange, and what the event reveals about the character. Prose
follows the action-line convention. Staging test applies. Orwell
co-anchor applies. No meta-vocabulary. Condition notes are factual,
not prose-styled.

**Target range:** 3-8 entries.

**Distinction from other sections:**
- vs. Voice/Dialogue: Voice/Dialogue shows speech patterns. Story
  Beats describe specific events that could unfold.
- vs. calendar events: calendar events are recurring scheduled
  occurrences. Story Beats are one-time or progression-gated.
  A dated one-time event with character-specific narrative (e.g. a
  festival date at a milestone) is a Story Beat referencing the
  calendar context.
- vs. story notes: Story Beats are character-local hooks inside the
  card. Story notes are full arc documents outside it.
```

- [x] **Step 3: Update working-document conventions in card-format.md**

In the working-document conventions section, after the existing text about bullet points and annotations, add:

```markdown
Two recognized exceptions to the all-bullets convention: the Body
appearance preamble (prose before the first bullet point) and Story
Beats entries (labeled prose blocks with bold title, em-dash
condition, and scenario prose). Export strips working annotations
but preserves both formats.
```

- [x] **Step 4: Update SKILL.md session opening**

In the Session Opening section, after the Voice / Dialogue recommendation paragraph, add:

```markdown
**Story Beats:** Recommend when the character has progression-gated
events (relationship milestones, story involvement), when the target
platform supports future storylines or alternate greetings, or when
the source material provides rich scenario data. The user decides.
```

- [x] **Step 5: Update SKILL.md session flow — addon blocks**

In the Addon blocks subsection, update the ordered addon processing list to include Story Beats after Voice / Dialogue: "Relationships, then Intimate Dynamics, then Voice / Dialogue, then Story Beats." Then add a Story Beats paragraph after the Voice / Dialogue paragraph:

```markdown
**Story Beats:** When selected at session opening, work through Story
Beats after Voice / Dialogue (or after the last selected addon
block). Ask about narrative milestones, story events, or
progression-gated encounters. Work through them in approximate
narrative order. See `card-format.md` for entry format, writing
rules, and distinctions from other sections.
```

- [x] **Step 6: Update SKILL.md session flow — Body section guidance**

In the Core block subsection of Session Flow, after the depth-of-access progression paragraph, add a note about the Body preamble:

```markdown
For the Body section, ask about appearance first (preamble), then
physical mannerisms (entries). The preamble covers static appearance
at all depths; the depth-of-access grid guides behavioral entries
only.
```

- [x] **Step 7: Update SKILL.md story notes boundary**

In the Story Notes section, after "Story possibilities for this character live in separate story notes," add:

```markdown
Story Beats (the addon block) are character-local scenario sketches —
hooks short enough to live inside the character card. A story note is
a full narrative document with arc structure, scope, and its own
lifecycle. Story Beats may reference story notes for arcs they
participate in. If a scenario needs more than 2-4 sentences to
describe, it belongs in a story note.
```

- [x] **Step 8: Update SKILL.md completion checklist**

Change the parenthetical in the "Selected addon blocks completed" item from:

```
(Relationships, Intimate Dynamics, Voice / Dialogue as determined in session opening)
```

to:

```
(Relationships, Intimate Dynamics, Voice / Dialogue, Story Beats as determined in session opening)
```

- [x] **Step 9: Verify internal consistency**

Read both files fully. Verify:
- card-format.md Body section has preamble definition before entry format
- card-format.md addon blocks lists four blocks (Relationships, Intimate Dynamics, Voice/Dialogue, Story Beats)
- card-format.md working-document conventions acknowledges both exceptions
- SKILL.md session opening lists four addon decisions
- SKILL.md session flow has Body preamble guidance and Story Beats step
- SKILL.md story notes section defines the boundary
- SKILL.md completion checklist enumerates all four addon blocks

Run: `grep -n "Story Beats" skills/worldbuilder-character/card-format.md skills/worldbuilder-character/SKILL.md`
Expected: matches in both files at the inserted locations.

Run: `grep -n "preamble" skills/worldbuilder-character/card-format.md skills/worldbuilder-character/SKILL.md`
Expected: matches in both files.

- [x] **Step 10: Commit**

```bash
git add skills/worldbuilder-character/card-format.md skills/worldbuilder-character/SKILL.md
git commit -m "feat: Body appearance preamble and Story Beats addon block — card format and skill amendments"
```

---

### Task 2: Template, Preset, and Export Updates (downstream consumers)

**Files:**
- Modify: `defaults/templates/character.md:21-25` (Body section)
- Modify: `defaults/templates/character.md` (add Story Beats heading)
- Generated: `defaults/okf.json` (via `python scripts/build-okf.py`)
- Modify: `skills/worldbuilder-ainime-export/card-assembly.md:91-101` (Future Storylines)
- Modify: `skills/worldbuilder-ainime-export/card-assembly.md:21` (Body prose)
- Modify: `skills/worldbuilder-ainime-export/SKILL.md` (Story Beats export mapping)

**Interfaces:**
- Consumes: card-format.md definitions from Task 1
- Produces: updated template, generated preset, updated export instructions

- [x] **Step 1: Update character template — Body section**

In `defaults/templates/character.md`, change the Body section stub from its current format to include a preamble placeholder:

```markdown
## Body

_Appearance preamble: short descriptive prose — hair, eyes, skin, build, distinguishing features, clothing._

_Behavioral entries below. One stageable sentence per entry._

- 
```

- [x] **Step 2: Update character template — add Story Beats heading**

After the Voice / Dialogue section in the template, add:

```markdown
## Story Beats

_Labeled prose blocks. Title, trigger/condition, 2-4 sentences of scenario prose. 3-8 entries._

```

- [x] **Step 3: Regenerate OKF preset**

Run: `python scripts/build-okf.py`
Expected: `defaults/okf.json` is regenerated without errors.

Verify: `python -c "import json; d=json.load(open('defaults/okf.json')); print('OK')"` prints `OK`.

- [x] **Step 4: Update card-assembly.md — Body preamble in export**

In `skills/worldbuilder-ainime-export/card-assembly.md`, in the section that assembles the character prose (around line 21 where "Who they are at a glance" is constructed), add a note that the Body preamble provides the physical appearance description and is included verbatim in the assembled prose.

- [x] **Step 5: Update card-assembly.md — Future Storylines from Story Beats**

In the Future Storylines section (lines 91-101), update the source reference to note that Story Beats entries from the character card are the source material. The export transforms them to possibility-style framing (present tense, "might" or "could" voice). The title becomes the storyline label; the trigger/condition becomes the storyline context; the scenario prose is reframed as a possibility.

- [x] **Step 6: Update ainime-export SKILL.md — Story Beats mapping**

In the Character Export section:

1. Update the `appearance` field source to reference the Body preamble (not a separate Appearance section).
2. Add a Story Beats field mapping:

```markdown
**Body preamble → appearance:** The Body appearance preamble provides
the character's physical description for the appearance field.

**Story Beats → Future Storylines:** Each Story Beat entry maps to
a future storyline. The export transforms definite scenario prose to
possibility-style framing. Trigger conditions that the platform
cannot mechanically enforce are woven into the storyline context as
narrative framing.
```

- [x] **Step 7: Verify export consistency**

Read card-assembly.md and ainime-export SKILL.md. Verify:
- Body preamble consumption is noted in the prose assembly section
- Future Storylines section references Story Beats as source
- SKILL.md has a Story Beats field mapping

Run: `grep -n "Story Beats\|preamble" skills/worldbuilder-ainime-export/card-assembly.md skills/worldbuilder-ainime-export/SKILL.md`
Expected: matches in both files.

- [x] **Step 8: Commit**

```bash
git add defaults/templates/character.md defaults/okf.json skills/worldbuilder-ainime-export/card-assembly.md skills/worldbuilder-ainime-export/SKILL.md
git commit -m "feat: propagate Body preamble and Story Beats to template, preset, and export"
```
