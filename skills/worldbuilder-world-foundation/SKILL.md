---
name: worldbuilder-world-foundation
description: Use at the start of a new worldbuilding project to establish setting structure and produce the seed document. Also use when auditing an existing world for structural gaps in household design, cast architecture, or thematic grounding.
---

# World Foundation

## Overview

This skill covers two things: the structural decisions that shape the world, and the seed document that captures them. Work through the decisions first; the seed document is the output, not the starting point.

The seed document is a starting point, not a finished world — it will grow in directions it does not anticipate.

---

## Opening Act: Ingestion

Before asking any questions, check whether the user has reference material to provide.

Ask: "Do you have any existing material for this world — notes, documents, previous writing, URLs, or reference media you want to draw from?"

If yes:
- Accept files, pasted text, or URLs
- Read everything before proceeding
- Extract any decisions already made (setting name, tone, existing characters, world details)
- Note contradictions or gaps to resolve during the questions phase
- Do not discard or override anything the user has already decided

If no: proceed directly to the six foundational questions.

---

## The Six Foundational Questions

Work through these before writing any part of the seed document. They are not a form to fill in — they are decisions to make. Stop and ask the user at each one. Do not assume or fill in gaps.

### 1. What is the setting's wound?

Every good setting has something wrong with it — something it lost, something that divided it, something it has been unable to face. This determines what the player's presence means, what the opening arc is, and what long-term healing looks like.

Examples:
- An institution in decline while a hostile outside force moves in
- A guardian or protector who can no longer perform that function
- A founding betrayal the community has never fully reckoned with
- A loss so old it has become local myth

### 2. What is the community's character?

Not just a name — its personality. Is it proud of its history or embarrassed by it? Tightly knit or full of old grudges? Welcoming to outsiders or suspicious? The community's personality is the default filter every character's behavior runs through.

### 3. What is the player's connection to this place?

Inherited property? Drawn here by something? Washed up by accident? The connection determines who knew the predecessor, what the player's presence means to different characters, and what stakes the player has from day one.

### 4. What is the setting's hidden layer?

If the setting includes supernatural elements, the origin shapes tone:
- A catastrophe long ago (the world is in recovery; magic is a relic)
- A choice made by the founders (something was suppressed or traded away)
- A natural cycle (the world breathes in and out; this is an exhale)
- Something ongoing (the change is still happening; something is causing it)

If the setting has no magic, this becomes: what is the setting's concealed depth? Every good setting has something beneath the surface — a secret, a history, a truth the surface doesn't advertise.

### 5. What is the era?

Approximate technology and cultural reference point. Affects every character's daily life and what kinds of problems are plausible:
- Contemporary with poor infrastructure
- Early modern (electricity and transport, no internet)
- Pastoral (no technology, not medieval)
- Fantasy-modern (technology alongside magic)

### 6. How many household clusters, and what are they?

Design the setting as 6–8 household clusters before naming any individuals. Characters gain meaning from their relationships with each other, not just with the player.

---

## Household Design

For each household before assigning any characters:

```
HOUSEHOLD NAME / LOCATION
Function: role in the community economy or social structure
Internal tension: what is unresolved or complicated between the members
Inter-household connections: which other households are tied to this one, and how
Narrative hook: what is interesting about this household as a unit
Trajectory: where are they headed if nothing changes — the slow drift of their situation
```

**Every household needs:**
- A physical location
- A primary function in the setting's economy or community
- An internal tension
- At least one connection to another household
- A trajectory — this is what makes household dynamics feel like they exist in time

Characters who exist in isolation from every other household are underwritten. The household structure is what gives the cast its web of meaning.

---

## Cast Architecture

Design the cast structure before naming individuals.

### Romance candidate archetypes

Romance-eligible characters should collectively cover these six slots across gender presentations.

1. **Initially hostile / cold** — earns warmth through player investment; strongest attachment when won
2. **Warm / immediately approachable** — accessible early-game anchor
3. **Quirky / alternative** — operates outside social norms
4. **Ambitious / driven** — has independent goals that don't revolve around the player
5. **Creative / dreamy** — artistic or philosophical orientation
6. **Wild card** — resists easy categorization

**Anti-redundancy check:** If two characters occupy the same slot, verify they differ substantially in execution — different emotional register, different obstacle, different function in the setting. The same archetype expressed the same way produces redundancy that players notice.

### Non-romance archetypes to place somewhere in the cast

- Authority figure — has own agenda beyond the player; satirizes small-community governance
- Mentor / elder — carries the setting's memory, connects player to local history
- Elderly couple or widow/widower — anchors mortality and long-term commitment
- Child or young teenager — creates stakes for adult characters, multiplies adult complexity
- Outcast / philosopher — lives outside the norm by choice, challenges assumptions about good lives
- Magical practitioner or equivalent — knows more than they say; bridge between surface and hidden layers
- The one who left and came back (or should have left and didn't)
- Someone carrying a secret the surface doesn't reveal

### Negative-track characters

At least 2–3 characters should have meaningful content at low or negative influence — not just distance, but legitimate grievance or opposition. The player should be able to genuinely wrong someone, or encounter someone whose hostility has nothing to do with player behavior.

### Cast size targets

- Default: 8 main / 16 side characters
- Range: 6–10 main, 6–20 side
- The coverage check in `worldbuilder-world-planning` verifies ratio, archetype coverage, and household balance before the roster is confirmed complete

---

## Seed Document

Once the foundational questions and household structure are settled, produce `seed.md` at the project root.

`seed.md` is a platform-agnostic project proposal. Write each section as plain prose under natural headers — this is not an export format, it is the creative document that export skills derive from. The ainime export skill handles field mapping.

### Sections

**Setting Summary**
Time, place, society, and general feel. The always-active context — concrete and specific.

**Genre and Tone**
Primary genre, tonal range (how dark, how light), and any content notes.

**Inspirations**
Source games and media, one per line. Include what specifically is drawn from each rather than just the title ("Stardew Valley — farming life rhythm and community bonds" not just "Stardew Valley").

**Tonal Inspirations**
Other media capturing the right feel — films, books, music, anime. One per line with what's being borrowed tonally.

**Key Tropes and Themes**
8–12 recurring concerns of this world. Both setting tropes and emotional themes.

**Community**
The community's social and emotional identity — not its physical description, not a repeat of the Setting Summary. How the community behaves and feels as a social entity.

**World Introduction**
Pre-game text the player reads before starting. Sets expectations for tone and situation.

**Opening Situation**
The situation the player arrives into. Evocative, not scripted — establishes the stage rather than dictating what happens. Cover: the setting's visible state on arrival, the immediate invitation for engagement, what the player's arrival means to the community.

**Story Direction note**
Do not write story direction content into seed.md. direction.md is a separate project document produced in Phase 1b by world-planning, after seed.md is confirmed. See `worldbuilder-story` for section templates and content guidance.

### Additional seed outputs

**Locations list**
Named locations with one sentence each on function and character. 10–14 locations. Not full location notes — a spatial anchor for the Wide phase. Full location notes come later.

**Art style**
Desired visual aesthetic: overall style (anime, painterly, pixel, etc.), color palette tendencies, reference works if any.

**Musical theme**
Desired audio atmosphere: genre, tempo, instrumentation reference, how mood shifts across emotional registers. Reference tracks or artists if helpful.

---

## Working Principles

**Households before individuals.** Characters gain meaning from their relationships with each other. A character whose card doesn't reference anyone else in the setting is underwritten.

**The setting's wound is structural.** It should be visible in at least two or three unrelated characters' motivations. If the wound only affects one character, it's a personal subplot, not the town's wound.

**The hidden layer is structural, not explained.** The world doesn't owe an explanation. Early encounters hint; later encounters acknowledge; deep lore confirms. Front-loading reveals kills the effect.

**All characters get equal depth.** The main/side toggle is a player-facing engagement setting, not a signal to write a thinner character card.

**Ask at every decision point.** The cost of fixing errors in generated documents is higher than the cost of answering an upfront question. When anything is ambiguous, surface it.
