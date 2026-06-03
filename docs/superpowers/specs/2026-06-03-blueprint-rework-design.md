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

## Session Flow

Before writing any note section, the agent conducts a structured Q&A with the user. This is conversational — the agent asks, the user answers, the agent captures.

**Questions to ask (in any order that fits the conversation):**

*Background:* Where did they grow up? What class, culture, community? What was valued or looked down on? What were the key formative experiences? Where are they now and how do they feel about it?

*Body:* What do they look like — age, build, distinguishing features? Has their appearance attracted attention they wanted or didn't? What do their clothing and grooming choices reveal? Any physical habits, self-consciousness, or pride?

*Soul:* What do they want most — not the surface want, the deeper one? What are they afraid of? Where is the gap between who they think they are and who they actually are? What irrational thing do they do, and where does it come from?

**What happens to the answers:** Captured in Design Notes under a "Session Notes" block — raw user intent, plain language. This is the builder record. Future agents revisiting the character read Design Notes to understand what was originally intended before checking the behavioral sections.

The agent then writes each section using the Q&A answers as source material. The answers do not appear in the behavioral sections — they inform the behavioral descriptions through the Because clause.

---

## Construction Formats

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

Behavioral dynamic entries written to the same construction discipline as Soul and Body. Each entry describes what this character does in this relationship — not how they feel about the person, not the other person's internal state.

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

Design Notes now has two categories of content:

**Session Notes (new):** A capture of the Q&A conversation — what the user said they wanted this character to be. Raw intent, not polished prose. Bullet points. This is the builder record: if the character needs to be revised, the agent reads this first to understand original intent before examining the behavioral sections.

**Builder context (existing, unchanged):** Narrative function, external references, design decisions, open questions.

Both categories are excluded from exports.

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
