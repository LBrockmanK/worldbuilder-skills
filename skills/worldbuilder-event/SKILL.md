---
name: worldbuilder-event
description: Use when creating or deepening an event note for an AI-powered narrative game — festivals, seasonal observances, calendar events, cultural rituals, historical commemorations, or any recurring world event. Also use when an event note feels thin, generic, or is failing to generate distinctive scene behavior.
---

# Event Notes

## Overview

An event note is not a schedule entry. It is a behavioral specification for a day. The export skill handles calendar mapping and storyTrigger packaging; this skill covers writing event notes that do real work: making any scene set on this day feel different from any other day.

The event note is the Wide-phase single source of truth for a named event. Export skills derive their output from this note.

---

## Working with Vault Files

**Renaming a note:** Use Edit or Write to rename the file. Then immediately run `scripts/rename-note.ps1 -OldName "OldName" -NewName "NewName" -VaultPath <vault-root>` to update all markdown links across the vault. Do not skip this step — Obsidian's auto-rename is bypassed when files are edited directly.

---

## Note Structure

| Section | Notes |
|---|---|
| Frontmatter | YAML; see below |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| What Happens | Factual description of the event |
| Scene Effects | What the event does to scenes and social dynamics |

---

## Event Note Frontmatter

Every event note opens with:

```yaml
type: event
status: draft | complete
aliases: []           # every realistic way this event is mentioned in dialogue
last_updated: YYYY-MM-DD HH:mm
date: Spring-08                                          # plain string; calendar day
recurring: true | false
characters: ["[Name](notes/name.md)"]                    # links to character notes
location: "[Location Name](notes/location-name.md)"      # link to location note
brief: |              # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

`aliases` functions the same as in concept notes — the export skill derives keyword triggers from it. Include every realistic phrasing: "the festival," "harvest time," "the long night."

---

## Brief

The `brief` frontmatter field is the world navigation summary for this note. Write it last, after the rest of the note is complete.

Content: what this event is and what it does to the community.

**Example:** "The Spring Harvest Festival: the one day the town's usual distances relax — introductions that normally take weeks happen naturally, and the player meets the community as a whole for the first time."

1–2 sentences. Behavioral: what the event does, not what it is.

---

## Design Notes

> **Excluded from exports.**

The Design Notes section is the builder's working record. It is not export content.

Cover:

- What this event contributes that no other event does. What makes it distinctive?
- Inspirations: real festivals, cultural observances, fictional events, what was drawn from each.
- Narrative intent: what kinds of scenes does this event enable?
- Open questions.

---

## Linking

When writing any section of an event note, link to any referenced note — character, location, faction, concept, event, or story — on its first mention in each section. Use standard markdown links: `[Name](notes/name.md)`. Link even if the target file does not yet exist. See CONTEXT.md for the full link convention.

---

## What Happens

Factual description of the event.

Cover:

- **Timing:** season and rough calendar position. Exact day is an export decision. Write "early spring," not "day 8."
- **Who participates:** universal, optional, by community role, or by invitation.
- **What physically occurs:** activities, rituals, traditions.
- **Origin:** what the event commemorates or why it exists.

Vague timing is fine. Write for content, not calendar precision. The export skill assigns the specific day.

---

## Scene Effects

What the event does to scenes and social dynamics. This is the section that makes event notes worth having.

Cover:

- **Social dynamics:** what distances relax, what tensions tighten, who talks to whom that normally wouldn't.
- **Obligations and costs:** who is expected to attend, what happens socially if someone doesn't.
- **Scene logic:** what becomes natural on this day, what becomes unusual or impossible.
- **Hidden layer:** how the event touches deeper world elements, if relevant.

**The scene test:** After writing Scene Effects, ask: if the engine generates a scene set on this day with no other context, does it feel different from any other day? If not, Scene Effects is too thin.

Failing example: "It is a day of celebration. People are happy and gather in the town square." This could be any day. The event is invisible.

Passing example: "The usual rules about who approaches whom are suspended today. Characters who normally hold themselves apart from the player will initiate conversation. The player meets the full community for the first time, and relationships that normally require weeks of individual cultivation can begin here." The engine has specific behavioral direction.

---

## Layer Classification

Some events carry layer classification like concept notes. A surface festival is well-known and openly celebrated. A mid-layer observance has old stories behind it. A deep-layer ritual touches the hidden layer. Apply a `layer:` frontmatter field if relevant.

Event notes without a hidden dimension do not need layer classification.

---

## Lifecycle

Event notes can be created at any phase. Create a stub — frontmatter plus a sentence or two of What Happens — as soon as an event is named. Flesh out What Happens and Scene Effects once the cast is established. Seasonal scenes are richer when you know who is in them.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] `aliases` covers every realistic phrasing
- [ ] `date` set as a plain string
- [ ] `recurring` set

**Brief**
- [ ] Written last
- [ ] Behavioral: describes what the event does to the community

**Design Notes**
- [ ] Distinctive contribution stated
- [ ] Not padded

**What Happens**
- [ ] Timing stated (approximate is fine)
- [ ] Who participates stated
- [ ] Physical activities described

**Scene Effects**
- [ ] Scene test passes: a scene on this day feels different from any other day
- [ ] At least one social dynamic specified — what relaxes or tightens
- [ ] Obligations and costs stated if the event carries them
