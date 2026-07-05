---
type: reflection
title: "Research Brief: Location, Faction, and Concept Note Depth"
description: Research brief requesting guidance on bringing location, faction, and concept notes to the same behavioral-specification depth as character notes.
tags: [complete]
date: 2026-06-15
timestamp: 2026-06-15T17:10
resources: []
---
# Research Brief: Location, Faction, and Concept Note Depth

## Purpose

We are building a worldbuilding workflow skill set for AI-assisted interactive fiction. The workflow is platform-agnostic in phases 1 and 2, with export to specific platforms (currently ainime-games.com) handled in phase 3.

The skill set already has a well-developed character note skill (`worldbuilder-character-blueprint`). Its central reframing is: **a character note is not a description — it is a behavioral specification.** The note tells an LLM what the character does in any situation, why they do it, and what their contradictions are. This is distinct from a character description, which tells you what they look like and what happened to them.

We need equivalent depth for three other note types: **location notes**, **faction notes**, and **concept notes**. Currently:

- **Concept notes** — covered by `worldbuilder-lorebook`, but from the export-mechanics side: layer classification (surface/mid/deep), alias guidance for keyword triggering, entry length discipline. The creative depth is thin: no guidance on narrative purpose, no framework for deciding what a concept note needs to accomplish, no completion criteria.
- **Location notes** — one page of guidance inside `worldbuilder-lorebook`. Physical description first, then narrative associations, one vivid specific detail. No structured process, no note sections, no equivalent of the character's Foundation → Behavioral Descriptions → Relationships progression.
- **Faction notes** — nothing beyond frontmatter fields (members, function). No skill exists.

The gap in one sentence: we know what to put in these notes mechanically, but we have no framework for what they need to **accomplish** — no equivalent of the character blueprint's behavioral-specification framing.

---

## What We Have Already

From the first research pass (`Worldbuilding Structure Research Results.md`), we already know:

- Vault structure: shallow hybrid, 6–8 folders by note type, flat within each.
- Universal frontmatter: type, status, aliases, last_updated.
- Type-specific frontmatter for all note types (location: region, function, primary-characters; faction: members, function; concept: layer, trigger-context).
- "For future Claude" preamble on every note — 2–3 sentences on what the note is and when to use it.
- LLM-readability principles: flat YAML, consistent H2 section headers, mandatory wikilinks, 200–800 word notes, aliases for every entity.
- The three-layer concept structure (surface/mid/deep) and alias/keyword guidance for concept notes.

Do not re-research these. They are settled.

---

## Section 1: Location Notes

A location note in our system covers named places that characters inhabit and scenes take place in — a village, a smithy, a ruin, a forest road. We currently treat these as "physical description + what it means." We want to understand what a richer framework looks like.

### 1a. Location documentation in professional worldbuilding

- How do TTRPG sourcebooks (Forgotten Realms, Eberron, Pathfinder, Blades in the Dark, etc.) structure individual location entries? What sections are standard? What order do they appear in?
- How do published campaign settings distinguish between different scales of location — region, settlement, specific building? Do they use the same structure or differentiate?
- In game design documents for narrative RPGs (Dragon Age, The Witcher, Mass Effect), how are locations documented for writers? Not for level design — for the writers who must write dialogue and scenes set there. What does that documentation contain?
- How do professional novelists and screenwriters document locations in their world bibles? Are there published examples or described practices?

### 1b. What a location note needs to accomplish for an LLM

- In AI roleplay and interactive fiction contexts, what are the documented failure modes of location entries? When does a scene set in a location feel flat, directionless, or repetitive?
- Are there community-established patterns in SillyTavern or other platforms for writing location lorebook entries that produce richer scenes? What distinguishes an entry that "works" from one that doesn't?
- The character blueprint asks: what does this character *do* in any situation? What is the equivalent question for a location? What does a location entry need to tell the LLM that makes the difference between a vivid, consistent scene and a generic one?
- What information about a location tends to be missing from simple physical-description entries, and what does the LLM hallucinate or invent poorly in its absence?

### 1c. Location-as-system

- Some worldbuilding frameworks treat locations as social ecosystems: who comes here, what do they want, what conflicts exist, what changes over time. Are there documented frameworks for this approach?
- How do published settings handle the "living location" — places that change with player/protagonist actions, places that have their own moods, places that behave differently at different times of day or under different circumstances?
- What is the equivalent of a character's "behavioral register" for a place? How do worldbuilders capture the difference between how a tavern feels at noon vs. midnight, or how a noble's court feels to an insider vs. a stranger?

---

## Section 2: Faction Notes

A faction note covers any organized group — a noble household, a merchant guild, a religious order, a criminal network, an informal community. We currently have no skill for this. The frontmatter exists (members, function); the content guidance does not.

### 2a. Faction documentation in professional worldbuilding

- How do TTRPG sourcebooks document factions and organizations? What sections are standard — history, goals, structure, membership, relationships with other factions?
- How do narrative game design documents handle factions? Are factions documented as entities with goals and behaviors, or as context for character and location documents?
- In TV series bibles and novel world bibles, how are political entities, families, and organizations documented? Are there published examples?
- How does published worldbuilding documentation handle faction *internal* dynamics — power structures, internal conflicts, factionalism within factions?

### 2b. Faction as behavioral entity

- A character note is a behavioral specification. Can a faction note be the same — a specification of how the group *acts*, not just who its members are? Are there frameworks that approach factions this way?
- What does the LLM need from a faction note to portray faction members consistently? A member of a tight-knit fishing community should feel different from a member of a criminal guild — what note content drives that difference?
- In AI RP contexts, what are the documented failure modes when factions are underspecified? What does the LLM default to when faction identity is absent?
- How do worldbuilders handle faction membership ambiguity — characters who are in multiple factions, characters whose loyalty is contested, former members?

### 2c. Faction relationships and faction change

- How do worldbuilding frameworks document relationships *between* factions — alliances, rivalries, histories of conflict?
- Published settings like Game of Thrones or Dune have factions that change significantly over the story. How do their documentation approaches handle faction state over time?
- In interactive fiction with meaningful faction dynamics (Baldur's Gate, Dragon Age, Disco Elysium), how do the underlying faction systems map to documentation? What does the design document layer look like?

---

## Section 3: Concept Notes

A concept note covers world knowledge — how the magic system works, what a cultural practice means, the history of an event, what a place or object is famous for. We have the mechanical side (layer classification, alias writing, entry length). We want to understand the creative/design side.

### 3a. What makes a concept entry work

- In SillyTavern and similar platforms, what distinguishes a concept/lore lorebook entry that produces rich, consistent output from one that is ignored or produces generic results? Are there community guides on this specifically?
- Beyond the keyword-trigger mechanics, what is the *content* of a good lore entry? How much context does it need? What framing? What should it not include?
- For "behavioral rules" entries (the SillyTavern community calls these the highest-impact entry type) — how are these written? What do they look like for world rules vs. cultural practices vs. event history?

### 3b. Concept note depth in worldbuilding frameworks

- How do professional worldbuilders decide what deserves its own concept note vs. what goes inline in a character or location note? Are there documented decision rules?
- For magic systems, religions, cultural practices, and other "systems" — how do worldbuilding frameworks distinguish between surface documentation (what it looks like) and deep documentation (how it works, why it exists, what it implies about the world)?
- The three-layer structure (surface/mid/deep) we use maps well to how the *player* encounters lore. How do other worldbuilding frameworks handle the distinction between "what everyone knows" and "what is actually true"? Are there published frameworks or tools that handle this?

### 3c. Concept notes as world constraints

- A concept note is not just storage — it constrains what can happen in scenes that touch the concept. How do worldbuilders think about concept documentation as a constraint system vs. a description system?
- In game design documentation, "world rules" are documented as hard constraints (magic rules, tech limits, social orders "what the story never contradicts"). How is this distinguished from softer world flavor? What makes a rule worth documenting explicitly?
- What is the relationship between a good concept note and the scenes that invoke it? How do you know when a concept note has enough in it?

---

## Section 4: Cross-Cutting Questions

### 4a. Analogs to the character blueprint's structure

The character blueprint builds richness through three layers:
1. **Foundation** (Body / Environment / Soul) — what shaped this person
2. **Behavioral Descriptions** (When / Behavior / Because) — what they do and why
3. **Relationships** — their social web and its dynamics

- Are there analogous three-part structures for locations and factions in any professional worldbuilding framework?
- What worldbuilding frameworks or templates produce the deepest, most narratively generative documentation for non-character entities?
- For locations: is there an equivalent of "body, environment, soul"? (Physical form / social/economic life / history and meaning?)
- For factions: is there an equivalent of "foundation, behavioral descriptions, relationships"? (Origin and purpose / collective behavior / inter-faction web?)

### 4b. Completion criteria and self-checks

- The character blueprint has a self-check list that tells you when a character note is done. For location and faction notes, what would the equivalent criteria be? What is the minimum a location note must contain to be "complete"?
- How do professional worldbuilders know when a world entity is documented enough vs. over-documented? Are there rules of thumb?
- In published worldbuilding guides or game design resources, are there explicitly stated criteria for "done" on entity documentation?

### 4c. Common underspecification failure modes

- When location notes are underspecified, what specifically goes wrong in the generated output? What does an LLM do when it doesn't have enough to work with?
- When faction documentation is absent, what do LLM-powered systems do? Do members of different factions sound the same? Does faction membership become invisible in scenes?
- For concept notes, what's the difference between too sparse (LLM ignores or fills in randomly) and too dense (bloats context, overwhelms the scene)?

---

## Key Questions

Regardless of source, these are the specific questions we most need answered:

1. **The behavioral specification for a location.** A character note specifies behavior: what this person does, why, what their contradiction is. What is the equivalent for a location? What does a location note need to contain to tell an LLM what *happens* in this place, who comes here and why, what the emotional register is, and how the place itself constrains and shapes scenes?

2. **The behavioral specification for a faction.** Same question: what does a faction note need to contain so that every character who is a member of the faction reads as a member? What creates collective behavioral identity without making faction members interchangeable?

3. **Section structure for each.** What sections, in what order, produce a complete location note? A complete faction note? Are there standard structures from professional worldbuilding practice that could serve as models?

4. **The concept note creative layer.** Beyond alias/keyword mechanics, what is the narrative purpose of a concept note? What question does a well-written concept note answer that a poorly written one doesn't?

5. **Completion criteria.** What is the minimum viable location note? The minimum viable faction note? Not minimum frontmatter — minimum content that makes the note actually useful to an LLM trying to render scenes set there or involving that group.

6. **Common failure modes.** What specifically goes wrong in scenes when these note types are underspecified? Concrete, observable failure patterns preferred.

---

## Output Format

Findings organized by section. For each finding, note:
- The source or context (e.g., "SillyTavern World Info Encyclopedia," "Dragon Age GDD postmortem," "World Anvil faction template")
- The core insight in plain language
- Any caveats or contexts where it doesn't apply

Prioritize findings that answer the Key Questions directly. We are not looking for general worldbuilding advice or Obsidian plugin recommendations — we have those. We are looking for:

- Frameworks for thinking about *what locations and factions need to accomplish*
- Concrete section structures used by professionals
- Documented failure modes and what fixes them
- Anything that reframes location/faction documentation the way "behavioral specification" reframed character documentation

Where professional practices conflict, document both sides. Where there are no documented practices, say so — that is also useful.
