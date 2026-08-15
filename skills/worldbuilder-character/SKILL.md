---
name: worldbuilder-character
description: Use when building or developing a character for an AI-powered RPG or collaborative fiction — creating from scratch, deepening an existing character note, or fixing a character who feels flat, inconsistent, or generating repetitive LLM output.
---

# Character Blueprint

*All prose this skill produces follows `../writing-style.md`. Read it before writing.*

## Overview

A character for an LLM-powered game is not a description. It is a behavioral specification. The engine handles generic social warmth and distance; the character note supplies the specific: what this character carries privately, what they do when trust is low or high, what their contradiction is.

`card-format.md` is the governing document for entry format and section-scoped writing rules. Read it before writing any entry.

---

## Collaboration Model

The session is a conversation. The AI asks targeted questions, the human answers, the AI translates each answer into a card-format entry, and the human approves or revises the entry before it is committed.

The human can override at any point:
- Write entries directly instead of answering questions
- Edit AI-proposed entries before approving
- Skip questions
- Provide source material (existing character sheets, fiction excerpts, reference images) in place of answers

Source material substitutes for human answers. When the human provides source material, extract the behavioral content and translate it into card-format entries the same way you would translate a spoken answer.

---

## Session Opening

Before beginning the Q&A, determine which addon blocks to include. Record the decision.

**Relationships:** Ask whether the character is part of a cast. If yes, include the Relationships block.

**Intimate Dynamics:** Check the project-plan flag. If the flag is set, include the block. If absent, do not raise it or ask about it.

**Voice / Dialogue:** Recommend when the character will be exported to platforms that support example dialogue or when voice distinctiveness matters for the project. The user decides.

**Story Beats:** Recommend when the character has progression-gated
events (relationship milestones, story involvement), when the target
platform supports future storylines or alternate greetings, or when
the source material provides rich scenario data. The user decides.

---

## Session Flow

Work through blocks in order.

### Core block

Background, then Body, then Soul. Every character card has all three.

Within each section, follow the depth-of-access progression defined in `card-format.md`: immediate (what is apparent on first meeting), then over time (what emerges with familiarity), then hidden/foundational (what is rarely seen or never spoken). This progression guides question order, not document structure. Entries land flat under section headings.

For the Body section, ask about appearance first (preamble), then
physical mannerisms (entries). The preamble covers static appearance
at all depths; the depth-of-access grid guides behavioral entries
only.

Ask one question at a time. Wait for the answer before asking the next. Follow threads: when an answer implies something about a different section, surface it immediately and pursue it before changing topics.

After each answer, propose how the answer translates into a card entry. Apply the section-scoped writing rules from `card-format.md`. The rules are overridable defaults; the user can override any rule for their project.

When proposing an entry, reproduce the semantic content of the user's answer, not the phrasing. The input is the fact; the output is the staged behavior the fact produces.

### Addon blocks

After Core, work through selected addon blocks in order: Relationships, then Intimate Dynamics, then Voice / Dialogue, then Story Beats.

**Relationships:** See `relationships.md` for the 12-archetype framework, coverage requirements, and entry format. Ask about the character's named relationships, their behavioral dynamics, and what each relationship makes the character do. Follow the coverage and distribution requirements in `relationships.md`.

**Intimate Dynamics:** See `intimate.md` for coverage areas and entry format. Ask about attraction expression, hesitation and limits, and any specific dynamic. Ensure at least one friction point.

**Voice / Dialogue:** The user picks 2-4 situation categories from the list in `card-format.md`. For each chosen category, write a composite dialogue snippet showing the character pulling from multiple Core areas at the same time. Include enough scene context to establish the situation.

**Story Beats:** When selected at session opening, work through Story
Beats after Voice / Dialogue (or after the last selected addon
block). Ask about narrative milestones, story events, or
progression-gated encounters. Work through them in approximate
narrative order. See `card-format.md` for entry format, writing
rules, and distinctions from other sections.

---

## Coverage Checking

### After each Core section

Report depth-of-access observations: which columns (immediate, over time, hidden/foundational) have entries, and which are thin or empty. This is advisory, not deterministic. Suggest follow-up questions for under-represented columns. The user can accept the suggestion or mark the section as complete.

### After the full Core block

Check for missing required doctrine entries (defined in `card-format.md`). The required entries are:

1. Core want (behavioral, Soul)
2. Core fear (behavioral, Soul)
3. False belief the character acts on (Soul)
4. Value-conflict stance (Soul)
5. At least one unresolved tension or competing pull (Soul)
6. Values with costs (Background or Soul)

Missing required entries must be addressed before finalization or explicitly waived by the user with a recorded reason.

---

## Working Document

Entries accumulate in the character note as the user approves them. Each section is a markdown heading. Entries are bullet points under their section heading. The Body appearance preamble (prose before the first bullet) and Story Beats (labeled prose blocks) are recognized exceptions.

The document may carry optional annotations (grid position, coverage area) during creation. These are a working aid; export strips them.

---

## Design Notes

Design Notes is the builder record. It is excluded from all exports. Two H3 subheadings:

### Session Notes

Q&A capture: what the user said they wanted this character to be. Written during the Q&A phase, before entries are drafted. Raw intent, plain language, bullet points. Future agents revisiting this character read Session Notes first to understand original intent.

### Builder Context

Narrative function, external references, design decisions, open questions. Bullet points. Leave blank if there is nothing worth capturing. Do not pad.

---

## Frontmatter and File Naming

Frontmatter is defined by the project's OKF registry; `new_doc.py` stamps it at creation. The script produces a date-prefixed filename; rename the fresh note to the character's name (e.g. `notes/Maren Holt.md`) before adding content.

**Description field:** the cast navigation summary. Who this character is in the world, their key traits, their place in the social ecosystem. Described, not prescribed: no relationship recommendations, no design rationale. Written last, after the full blueprint is complete.

---

## Story Notes

Story possibilities for this character live in separate story notes, not in the character note. When you have enough clarity on a character's arc, create a story note with intention scope and link it back. See `worldbuilder-story` for story note structure.

Story Beats (the addon block) are character-local scenario sketches —
hooks short enough to live inside the character card. A story note is
a full narrative document with arc structure, scope, and its own
lifecycle. Story Beats may reference story notes for arcs they
participate in. If a scenario needs more than 2-4 sentences to
describe, it belongs in a story note.

The introduction note is also a story note (introduction scope). Create it when you have enough character clarity to know where and how the player first meets this character.

---

## Post-Group Sync Pass

After completing a household group or batch of characters, run a relationship sync pass before moving on. Characters develop during the blueprinting sequence. A character written later may shift in ways that make an earlier character's relationship entry inaccurate. Check the group's notes against each other: are named relationships still consistent? Update when the sequence reveals something that changes the picture.

---

## Completion Checklist

The note stays on an open status tag while work is in progress. Mark it `complete` when every item below passes.

- [ ] All required doctrine entries present or explicitly waived with a recorded reason
- [ ] Each Core section (Background, Body, Soul) has at least one entry. Target ranges in `card-format.md` are guidance, not gates
- [ ] Selected addon blocks completed (Relationships, Intimate Dynamics, Voice / Dialogue, Story Beats as determined in session opening)
- [ ] No trait adjectives anywhere in the note. Each replaced by the behavior that earned it
- [ ] Entries follow section-appropriate writing rules per `card-format.md`
- [ ] `### Session Notes` present with Q&A capture
- [ ] `### Builder Context` present as applicable; not padded
- [ ] Story notes created or flagged as pending for any known character arcs
- [ ] `description` field written last and reflects the completed character
- [ ] Adversarial review gate passed — invoke `worldbuilder-review` with this document, `card-format.md` as the governing format document, and all reference material used to produce the document. Resolve all escalated findings before marking complete.
