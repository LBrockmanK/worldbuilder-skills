---
type: spec
title: "Design: World Entity Note Skills — Location, Faction, Concept Depth"
description: Design applying the character blueprint's behavioral-specification reframing to location, faction, and concept notes.
tags: [complete]
date: 2026-05-28
timestamp: 2026-05-28T17:10
resources: []
---
# Design: World Entity Note Skills — Location, Faction, Concept Depth

**Date:** 2026-05-28
**Status:** Approved

---

## Overview

The character blueprint is the most developed skill in the worldbuilder skill set. Its power comes from a single reframing: a character note is not a description — it is a behavioral specification that tells the engine what this person does in any situation, why, and what their contradictions are.

Location notes, faction notes, and concept notes lack equivalent depth. This design applies the same reframing to each and specifies three deliverables:

1. **New skill: `worldbuilder-location-blueprint`**
2. **New skill: `worldbuilder-faction-blueprint`**
3. **Targeted improvements to `worldbuilder-lorebook`**

All three skills are Wide-phase and platform-agnostic. Nothing in these skills references export format or target platform. The export skill reads the notes these skills produce; it is the only skill that knows what to do with them.

---

## The Reframings

Each note type gets one central reframing that drives all section decisions:

**Location:** A location note is not a description. The question is not "what does this place look like?" It is: *what happens here, who comes and why, and how does this place push back on a scene set in it?* A note that answers only the first question is a backdrop. One that answers all three is an actor.

**Faction:** A faction note is not a roster. The question is not "who are the members and what is their history?" It is: *how does this group act, such that any member reads as a member?* When a faction is underspecified, the LLM defaults to making every member a generic instance of their surface role. The faction becomes invisible.

**Concept:** A concept note is not a fact. The question is not "what is this thing?" It is: *what does the existence of this thing make impossible, costly, or inevitable?* A concept note that can only describe is not a constraint; it cannot shape what happens in a scene.

---

## Architecture

The three deliverables are peers to the existing character blueprint — each produces a Wide-phase note that export skills can read. They do not change the world-planning, world-foundation, story-direction, or export skills.

The location entries section currently inside `worldbuilder-lorebook` is superseded by the location blueprint skill and will be retired with a pointer.

---

## Deliverable 1: `worldbuilder-location-blueprint`

### Skill trigger

Use when creating or deepening a named location note: a place that characters inhabit and scenes take place in — a settlement, a building, a ruin, a road, a wilderness area.

### Note structure

Work through sections in order. Do not skip sections because the location seems simple.

| Section | Notes |
|---|---|
| Frontmatter | YAML; standard + location-specific fields |
| Preamble | 2–3 sentences; what this place is and when to use this note |
| Concept | Narrative purpose — what can only happen here? |
| Physical Form | Scale, condition, one vivid specific detail — not a floor plan |
| Social Life | Who comes here, why, what they want, what tensions exist |
| Behavioral Register | How this place reads differently across time / observer / circumstances |
| History & Meaning | Why it exists, what it implies, secrets if any |

### Frontmatter

```yaml
type: location
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
region: "[[The Valley]]"
function: one phrase (plain text)
primary-characters: ["[[Name]]"]
```

`region` and `primary-characters` use `[[wikilinks]]`. `function` stays plain — it is usually too specific per location to be worth linking.

### Preamble

2–3 sentences. What is this place and when should this note be used? Written as a fast-path briefing — usable without reading the full note.

### Concept

The narrative purpose of the location. Not a description of what it looks like or what happened there.

Covers: what does this location bring to the setting that no other location does? What kinds of scenes can only happen here? What tension or theme does it anchor?

The concept drives all other section decisions. If two sections pull in different directions, the concept is the tiebreaker.

### Physical Form

1–3 sentences. Scale, age, condition, environment, one vivid specific detail.

Not a floor plan. The engine needs to know what kind of place this is, not where the furniture is. One concrete detail beats three paragraphs of layout.

### Social Life

The ecosystem layer. Who comes here and why. What they do when they arrive. What they want that they might not get. What tensions exist between different regular visitors, or between visitors and whoever maintains the place.

Written as who-does-what, not who-is-there. "Farmers come to argue prices with the grain merchant, who holds the only scales in the valley" is a social life entry. "Farmers and merchants frequent this location" is not.

### Behavioral Register

The section with no equivalent in the current skill set — and the one that turns a backdrop into an actor.

How this place reads across variations:

- **Time:** day vs. night, busy periods vs. quiet, seasonal rhythm if it matters
- **Observer:** insider/regular vs. stranger/first-timer, if that distinction produces meaningfully different scenes
- **Circumstances:** normal operation vs. disrupted or crisis state

Not all axes apply to every location. Cover the variations that would produce different scenes; skip those that wouldn't. A remote ruin does not need an insider/stranger distinction. A village market square probably needs all three.

The self-check test for this section: *can this place push back against the characters in it?* A place that reads identically regardless of who is present or what is happening is a backdrop. One that changes tone, creates friction, or imposes its own logic on a scene is a behavioral spec.

### History & Meaning

Why this place exists, what it carries from the past, what it implies about the world. Where secrets live if the location has them.

Not required to be long — a sentence or two is often enough — but the "what it implies" question must be answered. A place that exists for no reason is a prop.

### Key principles

**Make decisions, don't hedge.** Every fact in the note is a decision. "The mill burned under disputed circumstances" is a decision. "Something may have happened to the mill at some point" is an incomplete note.

**Note register is functional, not literary.** Plain, direct language throughout. "Locals avoid the east wing after dark" is correct. "Shadows cling to its ancient stones like a shroud of forgotten memory" belongs in a novel, not a note.

**Physical Form is not the point.** A location note that is mostly Physical Form and thin on everything else is description masquerading as specification. Social Life and Behavioral Register carry the most behavioral weight.

### Self-check before marking complete

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
- [ ] At least one tension or conflict in the ecosystem
- [ ] Written as who-does-what, not who-is-there

**Behavioral Register**
- [ ] At least one meaningful variation specified
- [ ] Passes the push-back test: the place can act on the scene, not just contain it

**History & Meaning**
- [ ] States why the place exists
- [ ] States what it implies about the world

---

## Deliverable 2: `worldbuilder-faction-blueprint`

### Skill trigger

Use when creating or deepening a faction, household, organization, or any named group — a noble family, a merchant guild, a religious order, a criminal network, an informal community with shared identity.

### Note structure

| Section | Character blueprint analog | Notes |
|---|---|---|
| Frontmatter | — | YAML; standard + faction-specific fields |
| Preamble | Preamble | 2–3 sentences; what this faction is and when to use this note |
| Concept | Concept | What narrative engine does this faction run? |
| Origin & Purpose | Foundation | Founding, what it controls, its current goal(s) |
| Collective Behavior | Behavioral Descriptions | When/Behavior/Because for the group; Demeanor/Nature split |
| Membership | — | Ranks, acquisition/loss, ambiguity cases |
| Inter-Faction Web | Relationships | Direct allies/rivals only — lightweight by design |
| Storylines | Storylines | Story possibilities anchored by this faction |

### Frontmatter

```yaml
type: faction
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
members: ["[[Name]]"]
function: one phrase (plain text)
```

`members` uses `[[wikilinks]]`. `function` stays plain.

### Preamble

2–3 sentences. What is this faction and when should this note be used?

### Concept

The narrative engine this faction runs. Not a description of its membership or history — what does it *do* to the story? What conflicts does it generate or embody? What role does it fill that no other faction could?

A merchant guild and a thieves' guild that produce the same kinds of scenes have the same concept. That is a problem, not an accident.

### Origin & Purpose

Three things, in order:

1. **Founding** — how the faction came to exist, its original purpose
2. **Current holdings** — what it controls now: resources, territory, monopoly, information, relationships, obligations owed to it
3. **Active goal(s)** — what it is trying to achieve right now

Goals must be specific. "Seeks power" is not a goal. "Controls the grain trade and intends to extend that monopoly to the river docks before the spring thaw" is a goal. Specific goals connect the faction to the events layer and make it a story engine.

### Collective Behavior

The key section. Written entirely as instructional directives — not description of what members are, but specification of what they do.

**Phrasing rule:** instructional, not descriptive throughout. *"Members address outsiders with measured formality and rarely volunteer information unprompted — show this"* not *"Members are formal and guarded."* Descriptive phrasing tells the engine what to know. Instructional phrasing tells it what to do.

Three components:

**Shared behavioral tendencies** — 3–5 entries in When/Behavior/Because form, applied to the group as a whole. Cover recognizable situations: encountering outsiders, handling internal conflict, interacting with rivals, operating under pressure or scrutiny.

*Format:* same as the character blueprint's behavioral descriptions, but the subject is "members of this faction" or the faction name:

> When [situation], [members do X] because [faction value/principle].

**The collective mask (Demeanor)** — how members present as a group to people who don't know them. What a stranger interacting with any member of this faction expects to encounter. This is the shared surface — what makes members recognizable as members before their individual character comes through.

**The variation layer (Nature)** — the individual underneath the collective mask. Members share the Demeanor without sharing the same personality. This section acknowledges natural variation axes: loyalists vs. cynics, true believers vs. pragmatists, long-timers vs. new recruits. It does not write out every variation — it names the axes so that individual character notes can position characters against them.

This split is what prevents faction members from being interchangeable. They wear the same mask; who they are underneath differs.

### Membership

Deliberately thin on named-member content — those belong in character notes. Covers:

- Ranks or tiers, if they exist (brief — hierarchy only, not personalities)
- How membership is acquired and how it is lost
- Ambiguity cases: former members, dual loyalties, contested membership, outsiders who function as members without formal standing

Ambiguity cases earn their place because characters who straddle faction lines are often the most narratively generative.

### Inter-Faction Web

Lightweight by design. Direct relationships only — alliances, rivalries, contested territory, historical grievances with active weight. No comprehensive opinion-of-everyone map.

Each entry: faction name + status (allied / neutral / rival / enemy) + one sentence on what drives it.

Relationships that don't bear on the current project do not go here.

### Storylines

Story possibilities anchored by this faction's existence. Not scripts — possibilities. Phrased as "could," "may," "there is a possibility that." What could this faction do or reveal that no other faction could?

### Key principles

**The member test.** After completing the Collective Behavior section, read it and ask: if you wrote a new unnamed member of this faction into a scene with no other characterization, would they read as a member? If not, the section is incomplete.

**Make decisions, don't hedge.** Same rule as for characters and locations. An active goal that is vague is not a goal. A Demeanor that could belong to any group is not a Demeanor.

**Collective Behavior is the priority section.** A faction note that is mostly Origin & Purpose and thin on Collective Behavior documents history without specifying behavior. The history is less important than what the faction does.

### Self-check before marking complete

**Frontmatter**
- [ ] All required fields present
- [ ] `members` uses `[[wikilinks]]`
- [ ] `status` is `draft` or `complete`

**Preamble**
- [ ] 2–3 sentences; usable without reading the full note

**Concept**
- [ ] States what narrative engine this faction runs
- [ ] Names what conflicts it generates that no other faction could

**Origin & Purpose**
- [ ] Has a specific active goal (not "seeks power" or similar)
- [ ] Names what the faction currently controls

**Collective Behavior**
- [ ] 3–5 When/Behavior/Because entries for the group
- [ ] Demeanor (collective mask) described
- [ ] Variation layer (Nature axes) acknowledged
- [ ] All phrased as instructional directives, not description
- [ ] Member test passes: an unnamed member would read as a member

**Membership**
- [ ] Acquisition and loss of membership stated
- [ ] Ambiguity cases addressed

**Inter-Faction Web**
- [ ] Direct relationships only
- [ ] Each entry has status + one sentence on the driver

**Storylines**
- [ ] All entries phrased as possibility, not script

---

## Deliverable 3: `worldbuilder-lorebook` Improvements

### What stays unchanged

The existing alias writing guidance, three-layer structure, entry length discipline, and writing principles are solid. No structural overhaul.

### Addition 1: Narrative purpose prompt

Inserted before the alias writing guidance. Before writing a concept note's content, answer one question:

> *What does the existence of this thing make impossible, costly, or inevitable in a scene that touches it?*

A concept note that cannot answer this is description, not a constraint. Writing the answer first shapes the note.

### Addition 2: Limitations and costs block

A required block for any concept note covering a rule-bearing concept — magic systems, institutions, cultural practices, social structures, belief systems, anything with internal logic that scenes must respect.

The block specifies: what the concept cannot do; what it costs or demands from those who use or participate in it; what makes it fail, break, or produce unexpected results.

A concept documented only by what it can do cannot constrain a scene. One documented by what it cannot do, what it costs, and where it breaks can.

Notes for rule-bearing concepts that lack this block are flagged incomplete by the self-check.

### Addition 3: Two-layer iceberg split

Added to the three-layer structure section as a distinct mechanism.

The surface/mid/deep classification governs editorial intent about pacing — when a piece of knowledge should feel available to the player, and at what register to write it. That classification is not a reliable runtime gate; engines vary in whether and how they can suppress information conditionally. Its value is in shaping how the content is written (surface: matter-of-fact; mid: hedged and uncertain; deep: confirmed and weighted) and in recording authorial intent for export tools that can use it.

The iceberg split is a separate concept that operates *within a single note*. Where what people in the world believe and what is actually true diverge, document both explicitly in the same note:

- **Believed:** what characters in the world commonly say, assume, or act on
- **True:** what actually happened or how the thing actually works

This allows the engine to have characters speak and act from belief while the true version constrains what can actually happen and what specific characters know. Not every concept note needs this — only ones where the gap between belief and truth is narratively significant.

### Addition 4: Completion self-check

Three tests added at the end of the skill:

**Complete when:** the note can constrain or shape any scene that touches this concept.

**Limitations block check:** if this is a rule-bearing concept (magic system, institution, cultural practice, social structure, belief system), does the note include a limitations and costs block? If not, it is incomplete regardless of how much descriptive content it contains.

**Over-documented when:** any section adds detail no scene will touch, or duplicates content already in a character, location, or faction note. Concept notes are meant to be short and dense — duplication bloats context for no gain.

### Addition 5: Location entries section

The "Location Entries" section is removed and replaced with a one-line pointer to `worldbuilder-location-blueprint`. That skill now owns all guidance on writing location notes.

---

## What This Does Not Change

- `worldbuilder-world-planning` — orchestration skill; phase table and checklists unchanged
- `worldbuilder-world-foundation` — seed.md production; unchanged
- `worldbuilder-story-direction` — story/ note hierarchy; unchanged
- `worldbuilder-ainime-export` — export skill; reads the new note types the same way it reads character notes; no changes needed
- `worldbuilder-character-blueprint` — unchanged
- Vault structure, frontmatter schema, wikilink conventions — all settled; unchanged
