---
name: worldbuilder-faction-blueprint
description: Use when creating or deepening a faction note for an AI-powered narrative game — any named group (noble household, merchant guild, religious order, criminal network, informal community). Also use when faction members feel interchangeable, or when faction identity is invisible in generated scenes.
---

# Faction Blueprint

## Overview

A faction note is not a roster — it is a shared behavioral specification. The engine handles generic social roles; the faction note supplies the specific: how this group acts as a collective, what its members do when they encounter strangers, how they present to outsiders, and how individuals vary beneath that shared surface.

When a faction is underspecified, the engine defaults to making every member a generic instance of their surface role — every guard gruff, every merchant greedy, faction identity invisible across scenes. The faction note exists to prevent this. The section that carries the specification is Collective Behavior. Origin & Purpose and Membership are supporting context.

The faction note is the comprehensive Wide-phase single source of truth for any named group. Export skills derive their output from this note.

---

## Faction Note Structure

Work through sections in order.

| Section | Character blueprint analog | Notes |
|---|---|---|
| Frontmatter | — | YAML; see below |
| Preamble | Preamble | 2–3 sentences; what this faction is and when to use this note |
| Concept | Concept | What narrative engine does this faction run? |
| Origin & Purpose | Foundation | Founding, what it controls, its current goal(s) |
| Collective Behavior | Behavioral Descriptions | When/Behavior/Because for the group; Demeanor/Nature split |
| Membership | — | Ranks, acquisition/loss, ambiguity cases |
| Inter-Faction Web | Relationships | Direct allies/rivals only |
| Storylines | Storylines | Story possibilities anchored by this faction |

Faction notes do not use sub-files — all content lives in one note.

---

## Frontmatter

Every faction note opens with YAML frontmatter. Required fields:

```yaml
type: faction
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
members: ["[[Name]]"]   # links to character notes
function: one phrase (plain text)
```

`members` uses `[[wikilinks]]`. `function` stays plain text.

---

## Preamble

2–3 sentences. What is this faction and when should this note be used?

> *The Silt Brotherhood is a loosely-organized network of river traders who control most commercial traffic between the valley settlements. Use this note when the player deals with any river merchant, asks about trade or supply routes, or encounters anyone working the river. They are the faction most likely to have information the player needs and the least likely to offer it directly.*

Write it as if briefing a reader who needs to use the faction correctly right now, without reading the full note.

---

## Concept

The narrative engine this faction runs. Not a description of its membership or its history — what does it *do* to the story? What conflicts does it generate or embody? What role does it fill that no other faction could?

A merchant guild and a thieves' guild that produce the same kinds of scenes have the same concept. That is a problem.

---

## Origin & Purpose

Three things, in order:

**Founding** — how the faction came to exist and what its original purpose was.

**Current holdings** — what it controls now. Be specific: resources, territory, monopoly, information, relationships, obligations owed to it. "Has influence" is not a holding.

**Active goal(s)** — what the faction is trying to achieve right now. Goals must be specific and active.

> *Controls the grain trade and intends to extend that monopoly to the river docks before the spring thaw.*

"Seeks to grow its power and influence" is not a goal.

Specific goals connect the faction to the events layer and make it a story engine.

---

## Collective Behavior

The key section. This is what makes faction members read as members.

**Phrasing rule throughout this section:** instructional, not descriptive. Write what members DO, not what they ARE.

Failing example:
> "Members are guarded and don't trust outsiders."

Passing example:
> "When approached by an outsider asking about Brotherhood pricing, members deflect with friendly vagueness — they quote ranges rather than figures, suggest the player talk to the factor, and find a reason to be elsewhere if pressed. Show this."

Descriptive phrasing tells the engine what to know. Instructional phrasing tells it what to do. Every entry in this section must be instructional.

### Shared behavioral tendencies

3–5 entries in When/Behavior/Because form, applied to the group as a whole:

> When [situation], [members do X] because [faction value or principle].

Cover recognizable situations: encountering outsiders, handling internal conflict or challenge, interacting with rivals or authority, operating under scrutiny or pressure.

### The collective mask (Demeanor)

How members present as a group to people who don't know them. What a stranger interacting with any member of this faction expects to encounter — before individual personality comes through.

This is the shared surface: the thing that makes members recognizable as members.

### The variation layer (Nature)

The individual underneath the collective mask. Members share the Demeanor without sharing the same personality. Name the natural variation axes — do not write out every possible variation, just the axes that produce meaningfully different characters.

> *Loyalists vs. cynics. True believers vs. pragmatists who joined for the wages. Long-timers who remember the Brotherhood's origins vs. recent recruits who only know its current operation.*

This is what prevents members from being interchangeable. They wear the same mask; who they are underneath differs.

---

## Membership

Deliberately thin on named-member content — named members have their own character notes. Covers:

- **Ranks or tiers** if they exist (hierarchy only — no personalities here)
- **Acquisition** — how one becomes a member
- **Loss** — how membership ends or is revoked
- **Ambiguity cases** — former members, dual loyalties, contested membership, outsiders who function as members without formal standing

Ambiguity cases earn their place because characters who straddle faction lines are often the most narratively generative.

---

## Inter-Faction Web

Lightweight by design. Direct relationships only — alliances, rivalries, contested territory, historical grievances with active weight. No comprehensive opinion-of-everyone map.

Each entry:
```
[[Faction Name]] — allied / neutral / rival / enemy: one sentence on what drives it.
```

Relationships that don't bear on the current project do not go here.

---

## Storylines

Story possibilities anchored by this faction's existence. Not scripts — possibilities. Phrased as "could," "may," "there is a possibility that."

What could this faction do or reveal that no other faction could?

---

## Key Principles

**The member test.** After completing Collective Behavior, ask: if you wrote an unnamed member of this faction into a scene with no other characterization, would they read as a member? If not, the section is incomplete.

**Make decisions, don't hedge.** An active goal that is vague is not a goal. A Demeanor that could belong to any group is not a Demeanor.

**Collective Behavior is the priority section.** A faction note that is mostly Origin & Purpose and thin on Collective Behavior documents history without specifying behavior. History is less important than what the faction does.

**Instructional phrasing is not optional.** Descriptive phrasing in Collective Behavior will not produce behavioral consistency in output. Every entry must specify what members do.

---

## Self-Check Before Marking Complete

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
- [ ] Names what the faction currently controls (specific, not "influence")

**Collective Behavior**
- [ ] 3–5 When/Behavior/Because entries for the group
- [ ] Demeanor (collective mask) described
- [ ] Variation layer (Nature axes) named
- [ ] All entries phrased as instructional directives, not description
- [ ] Member test passes: an unnamed member would read as a member

**Membership**
- [ ] How membership is acquired and lost is stated
- [ ] Ambiguity cases addressed

**Inter-Faction Web**
- [ ] Direct relationships only
- [ ] Each entry has status + one sentence on what drives it

**Storylines**
- [ ] All entries phrased as possibility, not script
