# Character Blueprint Rework — Design Spec

**Date:** 2026-06-03  
**Issue:** [#13](https://github.com/LBrockmanK/worldbuilder-skills/issues/13)  
**Status:** Approved for implementation

---

## Problem

The character blueprint produces redundant content across sections. Soul, Behavioral Descriptions, and Relationship Behavior all describe the same psychology from different angles — Soul as inventory, Behavioral Descriptions as conversion output, Relationship Behavior as social-register output. The result is the same characterization appearing in multiple sections with Behavioral Descriptions consistently producing the best writing, because it has the clearest construction discipline.

Root cause: the Soul/Behavioral Descriptions separation was inherited from The Character Foundry, which was designed as a human worksheet. The exploration phase (Soul questions help the human think) and the conversion phase (When/Behavior/Because turns that thinking into behavioral output) were designed to be separate for human use. An AI agent doesn't need the exploration phase as a note-layer — it produces redundancy.

---

## Solution Overview

Every section of the character note becomes behavioral descriptions in a specific context. Sections carry non-overlapping content types enforced by construction format, not by audit. The exploration/Q&A phase moves to the conversation between agent and user, with answers captured in Design Notes as a builder record. The note itself contains only behavioral output.

Two sections dissolved: **Behavioral Descriptions** (absorbed into Soul) and **Relationship Behavior** (absorbed into Soul as general social register entries).

---

## Note Structure

Sections in order:

| Section | Type | Role |
|---|---|---|
| Frontmatter | YAML | Unchanged |
| Design Notes | Builder record | Expanded: now includes Q&A session capture |
| Background | Declarative context | Where this character comes from; different in kind from behavioral sections |
| Body | Physical behavioral descriptions | How physicality shapes behavior |
| Soul | Psychological + social behavioral descriptions | Internal patterns, drives, general social register |
| Relationships | Named relationship dynamics | Specific named relationships, behavioral construction |
| Intimate Dynamics (if flagged) | Intimate behavioral descriptions | Same trigger and coverage; construction format updated to match |

**Background** is placed before Body and Soul to signal its different nature — it is causal context, not behavioral output.

---

## Formatting

### Section headings

Each main section is H2 (`##`): Design Notes, Background, Body, Soul, Relationships, Intimate Dynamics (if present). No H3 subheadings within behavioral sections — Soul's psychological and social-register entries run together in a single bullet list with no dividers.

### Design Notes

H2 section. Two H3 subheadings inside it: `### Session Notes` and `### Builder Context`. Each subheading is followed by a bullet list.

```
## Design Notes

### Session Notes

- [Q&A capture — raw user intent, plain language]

### Builder Context

- [Narrative function, external references, design decisions, open questions]
```

### Background

Bullet list. One entry per fact pair:

```
- [Formative fact] → [what it made true]
```

No prose, no elaboration beyond the pair.

### Body, Soul, Intimate Dynamics

Bullet list. One behavioral description per bullet, written as a prose sentence. The When/Behavior/Because structure is a writing guide — it does not appear as visible labels in the output. The sentence embeds all three elements naturally.

*Example bullet:*
```
- When she enters a room she doesn't know, she finds a wall or corner first — she grew up visible in ways she didn't choose, and learned to make herself an observer before becoming a subject.
```

### Relationships

Bullet list. One entry per relationship. Bold `**Name — Archetype(s):**` prefix inline on the bullet, followed by the behavioral description as prose sentence(s).

*Example bullet:*
```
- **Mira — Kin:** When Mira dismisses her ideas in front of others, she doesn't argue — she brings the idea back later, one-on-one, where Mira has room to change her mind without losing face.
```

---

## Session Flow

Before writing any note section, the agent conducts a Q&A with the user. The Q&A is conversational — the agent asks one question at a time, waits for an answer, then continues. It is not a checklist delivered in bulk.

**Technique (drawn from grill-me approach):**

- **One question at a time.** Never present the full question list. Ask one, get an answer, ask the next.
- **Offer a hypothesis.** After each answer, surface what it implies before moving on: "Based on that, she might be afraid of being truly seen — does that sound right?" This gives the user something to confirm, redirect, or build on rather than starting cold each time.
- **Follow threads.** When an answer opens something up, pursue it before changing topics. A Background answer that implies a Soul pattern should be surfaced immediately: "You said she was the reliable one — that might mean her irrational behavior is overcommitting even when she can't afford to. Does that track?"
- **Sharpen vague answers.** "She has trouble trusting people" is not enough. Ask what that looks like: does she test people, avoid closeness, or extend trust and then panic when it's taken seriously?

**Coverage the Q&A must reach before writing begins:**

- Background: origin, class/culture, key formative events, current situation and how they feel about it
- Body: appearance, any notable physical self-consciousness, embodied habits
- Soul (psychological): core want beneath the surface want, core fear, self-image gap, irrational behavior and its root
- Soul (social register): how they are with strangers, what warmth looks like, what distance or conflict looks like

The Q&A ends when the agent has confident, specific answers across all four areas — not when the list is mechanically exhausted.

**What happens to the answers:** Captured in Design Notes under `### Session Notes` — raw user intent, plain language, bullet points. This is the builder record. Future agents revisiting the character read Session Notes first to understand original intent before examining the behavioral sections.

The agent then writes each section from the Q&A answers. Answers do not appear in the behavioral sections — they inform the behavioral descriptions through the Because clause.

---

## Construction Formats

### Design Notes

Two subheadings, each followed by a bullet list.

**Session Notes:** Raw Q&A capture — what the user said they wanted this character to be. Plain language, one bullet per answer or insight. Written during the Q&A phase before note sections are drafted.

**Builder Context:** Narrative function, external references, design decisions, open questions. One bullet per item. Leave blank if there is nothing worth capturing — do not pad.

### Background

Declarative fact pairs: `[Formative fact] → [what it made true]`

No behavioral framing. No prose elaboration. These are inputs to the behavioral sections, not behavioral descriptions themselves.

*Example: "Grew up working-class in a trade city → learned early that competence is the only currency nobody can take from you."*

### Body

When/Behavior/Because entries grounded in physical experience.

Coverage prompts (not all require an entry — only those that produce distinctive behavior):
- Appearance and how it gets noticed or avoided
- Physical self-consciousness or pride and what it produces
- Embodied habits: how they carry themselves, what they do with their hands, how they move in spaces

Thin body sections are acceptable when nothing about a character's physicality is distinctive. Forced entries are not.

### Soul

When/Behavior/Because entries. Two coverage areas with no subheadings — they run together as a single section.

**Psychological patterns (3–5 entries minimum):**
- Emotional triggers and responses
- Core drives in action (what does wanting to be respected actually look like when they're in a room?)
- Irrational behavior with its emotional root
- Self-image gap expressed as behavioral contradiction
- Contradiction between presented self and actual self (required — one entry must name this)

**General social register (2–3 entries minimum):**
- Default mode with strangers — what a first encounter feels like
- What warmth looks like when it appears — specific behavior, not "they become warm"
- What distance or friction looks like — specific behavior, not "they become cold"
- Relationship-type variation if it exists (with authority vs. peers vs. someone they're protecting)

The Because clause carries the psychological root drawn from the Q&A session. The agent does not invent psychology — it derives the Because from what the user said their character is driven by.

### Relationships

Bullet list. One bullet per relationship. Each entry opens with `**Name — Archetype(s):**` as an inline bold prefix, followed by a prose behavioral description — what this character does in this relationship, not how they feel about the person, not the other person's internal state.

Archetype framework, coverage requirements (8 named for major characters, 5 for supporting), generativity hierarchy, perspective-focus rules, and cross-character capture guidance are unchanged.

### Intimate Dynamics (if flagged)

When/Behavior/Because entries only.

Coverage check:
- How they express attraction or interest
- What makes them hesitate, pull back, or hold a limit
- Specific dynamic (if the character is built around one): what it gives them emotionally, what its behavioral signature is

One required friction point: a contradiction in their intimate behavior.

Exploration questions (what does the dynamic give them, how does it connect to their history, what would go wrong) move to Q&A / Design Notes — not written into the section.

---

## Design Notes Changes

Design Notes now has two H3 subheadings:

```
## Design Notes

### Session Notes
- [Q&A capture — raw user intent, plain language, bullet points]

### Builder Context
- [Narrative function, external references, design decisions, open questions]
```

**Session Notes** is new. It captures the Q&A conversation: what the user said they wanted this character to be. Raw intent, not polished prose. Written during the Q&A phase before note sections are drafted. This is the builder record — future agents read it first when revisiting the character.

**Builder Context** is unchanged in content. The name is now explicit where before the section had no internal structure.

Both subheadings are excluded from exports.

---

## Self-Check Changes

**Background**
- [ ] Declarative fact pairs only — no behavioral content, no prose elaboration

**Body**
- [ ] Entries grounded in physical experience
- [ ] No forced entries — thin is acceptable if nothing is distinctive

**Soul**
- [ ] 3–5 psychological behavioral entries minimum
- [ ] 2–3 general social register entries minimum
- [ ] One contradiction stated as a behavioral description
- [ ] Because clauses derive psychology from Design Notes session capture, not invented
- [ ] No literary flair, no hedging, no negative-led characterization

**Relationships**
- [ ] Coverage requirements met
- [ ] Each entry written in behavioral construction discipline
- [ ] Perspective-focus maintained (this character's experience only)

**Intimate Dynamics (if flagged)**
- [ ] Behavioral entries covering attraction expression, hesitation/limits, specific dynamic if present
- [ ] One friction point present

**Design Notes**
- [ ] Session Notes block present with Q&A capture
- [ ] Builder context present as applicable

---

## Note Template Skeleton

The character note template (`_templates/character.md`) updates to:

```markdown
---
type: character
status: draft
aliases: []
last_updated: YYYY-MM-DD HH:mm
factions: []
brief: ""
---

> For future agents: this is a character note. The filename is the character's name. Use `worldbuilder-character` to build it out.

## Design Notes

### Session Notes

_Q&A capture: what the user said they wanted this character to be. Raw intent, bullet points._

-

### Builder Context

_Narrative function, external references, design decisions, open questions. Bullet points._

-

## Background

_Where this character comes from. Declarative fact pairs: [Fact] → [what it made true]. No behavioral content._

-

## Body

_Physical behavioral descriptions. One entry per bullet._

-

## Soul

_Psychological and social behavioral descriptions. One entry per bullet._

-

## Relationships

_Named relationship dynamics._

## Intimate Dynamics

_Only present if flagged in project plan. Remove this section if not flagged._

-
```

---

## Dissolved Sections

- **Behavioral Descriptions** — content absorbed into Soul
- **Relationship Behavior** — content absorbed into Soul as general social register entries

These section names should not appear in character notes going forward. The self-check items for both are replaced by the Soul coverage check above.

---

## Out of Scope

- Frontmatter fields
- Export behavior
- Other note types (location, faction, concept, story) — addressed separately after character validation
- Relationships archetype system, coverage requirements, generativity guidance

---

## Acceptance Criteria

- [ ] At least one full character session tested under this approach before direction is committed
- [ ] Tested against an existing Viralys character — quality equal or better
- [ ] No characterization content appears in more than one section in the resulting note
- [ ] Section guidance updated to reflect new construction approach
- [ ] Character note template updated to match
- [ ] Export skill functions correctly with restructured notes
