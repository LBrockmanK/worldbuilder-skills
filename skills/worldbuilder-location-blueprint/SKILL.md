---
name: worldbuilder-location-blueprint
description: Use when creating or deepening a location note for an AI-powered narrative game — building a named place from scratch, giving depth to a location that feels like a backdrop, or fixing a location that generates repetitive or atmospheric-only output.
---

# Location Blueprint

## Overview

A location for an LLM-powered narrative game is not a description — it is a behavioral specification. The engine handles generic scene-setting; the location note supplies the specific: who comes here and why, what the place does to the people in it, how it reads differently at different moments. A location that only answers "what does it look like?" is a backdrop. One that answers "what happens here, and how does this place push back on a scene?" is an actor.

The location note is the comprehensive Wide-phase single source of truth for a named place. It covers everything true about the location that shapes how the engine writes scenes set there. Export skills derive their output from this note.

---

## Location Note Structure

Work through sections in order. Do not skip sections because the location seems simple — every section exists to catch what the others miss.

| Section | Notes |
|---|---|
| Frontmatter | YAML; see below |
| Preamble | 2–3 sentences; see below |
| Concept | Narrative purpose; see below |
| Physical Form | Scale, condition, one vivid specific detail — not a floor plan |
| Social Life | Who comes here, why, what they want, what tensions exist |
| Behavioral Register | How this place reads across time, observer type, circumstances |
| History & Meaning | Why it exists, what it implies, secrets if any |

---

## Frontmatter

Every location note opens with YAML frontmatter. Required fields:

```yaml
type: location
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
region: "[[The Valley]]"           # link to region note
function: one phrase (plain text)
primary-characters: ["[[Name]]"]   # links to character notes
```

`region` and `primary-characters` use `[[wikilinks]]`. `function` stays plain text — it is usually too specific per location to warrant a navigable link.

---

## Preamble

2–3 sentences at the top of the note body (after frontmatter). Answers: what is this place, and when should this note be used?

> *The grain mill sits at the northern edge of the village and has been out of operation for fifteen years. Use this note whenever the player approaches the mill, asks about it, or encounters anyone connected to the Harrow family. It is the setting's primary location of unresolved guilt.*

Write it as if briefing a reader who needs to use the location correctly right now, without reading the full note.

---

## Concept

The narrative purpose of the location — not a description of what it looks like or what happened there. 3–5 sentences covering:

- What does this location bring to the setting that no other location does?
- What kinds of scenes can only happen here?
- What tension or theme does it anchor?

The concept drives all other section decisions. If two sections pull in different directions, the concept is the tiebreaker.

---

## Physical Form

1–3 sentences. Scale, age, condition, environment, one vivid specific detail.

Not a floor plan. The engine needs to know what kind of place this is, not where the furniture is. One concrete detail beats three paragraphs of layout.

> *The mill is a two-storey stone building with a collapsed east wall, open to the sky. The water wheel still turns sometimes when there's no wind.*

A room-by-room layout is not this section.

---

## Social Life

The ecosystem layer. Who comes here and why. What they do when they arrive. What they want that they might not get. What tensions exist between different regular visitors, or between visitors and whoever maintains the place.

Written as who-does-what, not who-is-there. Every fact in this section is a decision — "various locals may visit for various reasons" is not a Social Life entry.

Cover:
- The main types of people who come here and their reasons
- What they want that the place does or doesn't provide
- At least one tension — between visitor types, between regulars, or between the place and its visitors

---

## Behavioral Register

The section that turns a backdrop into an actor. How this place reads across variations:

- **Time:** day vs. night, busy periods vs. quiet, seasonal rhythm if relevant
- **Observer:** how an insider or regular experiences it differently from a stranger or first-timer — if that distinction would produce meaningfully different scenes
- **Circumstances:** normal operation vs. disrupted, crisis, or changed state

Not all axes apply to every location. Cover the variations that would produce different scenes; skip those that wouldn't. A remote ruin probably does not need an insider/stranger distinction. A village market square likely needs all three.

**The push-back test:** after writing this section, ask — *can this place act on the people in it?* A place that reads identically no matter who is present or what is happening is a backdrop. One that changes tone, creates friction, or imposes its own logic on a scene is a behavioral spec.

---

## History & Meaning

Why this place exists. What it carries from the past. What it implies about the world. Secrets if it has them.

Not required to be long — a sentence or two is often enough — but the "what it implies" question must be answered. A place that exists for no reason is a prop.

If the location is the subject of concept notes at different knowledge layers, link to those notes here rather than duplicating their content.

---

## Key Principles

**Make decisions, don't hedge.** Every fact in the note is a decision. "The mill burned under disputed circumstances" is a decision. "Something may have happened to the mill at some point" is an incomplete note.

**Note register is functional, not literary.** Plain, direct language throughout. "Locals avoid the east wing after dark" is correct. "Shadows cling to its ancient stones like a shroud of forgotten memory" belongs in prose, not a note. If a sentence sounds like it belongs in a novel, rewrite it as a direct statement.

**Physical Form is not the point.** A location note that is mostly Physical Form and thin on Social Life and Behavioral Register is description masquerading as specification. The behavioral sections carry more weight.

**Asymmetry is normal.** Not every location needs every axis of Behavioral Register. Write only what is true and useful.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] All required fields present
- [ ] `region` and `primary-characters` use `[[wikilinks]]`
- [ ] `status` is `draft` or `complete`

**Preamble**
- [ ] 2–3 sentences; answers what this place is and when to use this note
- [ ] Usable without reading the full note

**Concept**
- [ ] States what narrative function this location serves
- [ ] Names what kinds of scenes can only happen here

**Physical Form**
- [ ] 1–3 sentences; one vivid specific detail
- [ ] No floor plan

**Social Life**
- [ ] Names who comes here and why
- [ ] At least one tension in the ecosystem
- [ ] Written as who-does-what, not who-is-there

**Behavioral Register**
- [ ] At least one meaningful variation specified
- [ ] Push-back test passes: the place can act on the scene, not just contain it

**History & Meaning**
- [ ] States why the place exists
- [ ] States what it implies about the world
