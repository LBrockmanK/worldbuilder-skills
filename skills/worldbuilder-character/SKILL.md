---
name: worldbuilder-character
description: Use when building or developing a character for an AI-powered RPG or collaborative fiction — creating from scratch, deepening an existing character note, or fixing a character who feels flat, inconsistent, or generating repetitive LLM output.
---

# Character Blueprint

## Overview

A character for an LLM-powered game is not a description — it is a behavioral specification. The engine handles generic social warmth and distance; the character note supplies the specific: what this character carries privately, what they do when trust is low or high, what their contradiction is.

The character note is the comprehensive single source of truth for a character in the Wide phase. It is richer than any export format can hold — it contains everything true about the character, including material that won't appear in any platform output. Export skills derive their output from this note.

---

## Working with Vault Files

**Renaming a note:** Use Edit or Write to rename the file. Then immediately run `skills/worldbuilder-linking/scripts/rename-note.ps1 -OldName "OldName" -NewName "NewName" -VaultPath <vault-root>` to update all markdown links across the vault. Do not skip this step — Obsidian's auto-rename is bypassed when files are edited directly.

---

## Character Note Structure

Work through sections in order. Do not skip sections because the character seems simple — every section exists to catch what the others miss.

| Section | Sub-file | Notes |
|---|---|---|
| Frontmatter | — | YAML; see below |
| Design Notes | — | Builder record; H3 subheadings; excluded from exports |
| Background | `framework.md` | Declarative context; different in kind from behavioral sections |
| Body | `framework.md` | Physical behavioral descriptions |
| Soul | `framework.md` | Psychological + social behavioral descriptions |
| Relationships | `relationships.md` | Named relationships; bullet format |
| Intimate Dynamics (if flagged) | `intimate.md` | Only if flagged in project plan |

---

## Frontmatter

Every character note opens with YAML frontmatter. Required fields:

```yaml
type: character
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
factions: ["[Household Name](notes/Household Name.md)", "[Guild Name](notes/Guild Name.md)"]   # links to faction notes
brief: |                                              # plain prose; written last — see ## Brief below
  <written after the full blueprint is complete>
```

`factions` uses markdown links to faction notes. The filename matches the display name. `brief` is plain prose — not a link.

---

## Brief

`brief` is the cast navigation field. When an agent is building relationships for another character or planning story arcs, they scan `brief` across the full roster to understand each character without opening their notes.

**Content:** who this character is in the world, their personality and key traits, their place in the social ecosystem, what makes them distinctive. Described, not prescribed — no relationship recommendations, no design rationale (that goes in Design Notes).

**Length:** up to ~150 words / ~200 tokens. As long as needed; not padded.

**Timing:** written last — after the full blueprint is complete. It can only accurately reflect a completed character.

> **Provisional note:** The content guidelines for this field should be reviewed and refined after initial session testing. An example should be added at that point.

---

## Design Notes

Design Notes is the builder record — it captures what drove the design of this character. Excluded from all exports. Two H3 subheadings:

### Session Notes

Q&A capture: what the user said they wanted this character to be. Written during the Q&A phase, before any note sections are drafted. Raw intent, plain language, bullet points. Future agents revisiting this character read Session Notes first to understand original intent before examining the behavioral sections.

### Builder Context

Narrative function, external references, design decisions, open questions. Bullet points. Leave blank if there is nothing worth capturing — do not pad.

Typical bullets for Builder Context:
- Narrative function: what this character uniquely contributes to the setting; what tensions or themes they embody
- External references: named real people, fictional characters, or combinations that shaped the design; what specifically was drawn from each
- Design decisions and constraints: choices made that would be confusing without context
- Open questions: unresolved decisions to revisit in future sessions

---

## Session Flow

Before writing any note section, conduct a Q&A with the user. Ask one question at a time — this is a conversation, not a checklist delivered in bulk.

**Technique:**

- **One question at a time.** Ask one, wait for the answer, ask the next.
- **Offer a hypothesis.** After each answer, surface what it implies: "Based on that, she might be afraid of being truly seen — does that sound right?" Give the user something to confirm, redirect, or build on.
- **Follow threads.** When an answer opens something up, pursue it before moving topics. A Background answer that implies a Soul pattern should be surfaced immediately: "You said she was the reliable one — that might mean her irrational behavior is overcommitting even when she can't afford to. Does that track?"
- **Sharpen vague answers.** "She has trouble trusting people" is not enough. Ask what that looks like: does she test people, avoid closeness, or extend trust and then panic when it's taken seriously?
- **Check Intimate Dynamics flag first.** Before beginning Q&A, check whether the character is flagged for Intimate Dynamics in the project plan. If flagged, include intimate coverage in the Q&A (see coverage list below). If not flagged, do not raise it.

**Coverage before writing begins:**

- Background: origin, class/culture, key formative events, current situation and how they feel about it
- Body: appearance, any notable physical self-consciousness, embodied habits
- Soul (psychological): core want beneath the surface want, core fear, self-image gap, irrational behavior and its root
- Soul (social behavior): how they are with strangers, what warmth looks like, what distance or friction looks like
- Relationships: who the named cast is, which relationships matter most to this character, the behavioral dynamic of each — what it makes them do when that person is present or mentioned
- Intimate Dynamics: if the character is flagged for intimate dynamics (check project plan first), also cover how they express attraction, what makes them hold back, and any specific dynamic that drives their intimate behavior

The Q&A ends when the agent has confident, specific answers across all coverage areas. Capture answers in Design Notes → Session Notes before moving to note writing.

---

## Writing Rules

These rules apply to all behavioral sections (Body, Soul, Relationships, Intimate Dynamics):

**Make decisions, don't hedge.** Every fact in the note is a decision. Never write "X or Y" or "grew up somewhere, perhaps Y" unless the ambiguity is a deliberate mystery being preserved. If you don't know, ask the user.

**Write plainly. No flair.** Write each behavioral description the way a screenplay writes action lines: present tense, only what can be seen or heard, no internal states, short plain sentences. If a director cannot stage the sentence, rewrite it. For vocabulary: shortest Anglo-Saxon word that works, active voice, cut every word that can go. See `writing-style.md` for the full style model.

**Write what characters ARE, not what they aren't.** Positive statements give the LLM something to act on. Negative constructions define by absence — the LLM has to invent the positive case itself. State the fact directly. Factual negatives are fine when the un-done thing is the meaningful information: "she has not sent the letter," "he hasn't asked."

**The note describes the character's starting state.** Nothing in the note may reference events that haven't happened yet. Check: has this already happened before the player meets this character? If not, create a story note or cut it.

**Section discipline.** Each section carries information the others don't:
- Background: where they came from (facts, not behavior)
- Body: behaviors grounded in physical experience
- Soul: general psychological and social patterns
- Relationships: behaviors specific to named individuals

Physical description (appearance, carriage, notable physical traits) belongs in Body — it is the physical reality that produces behavior, not a separate Appearance section.

If a behavior is primarily about one specific relationship, it belongs in Relationships. If a behavioral pattern is general (appears with many people), it belongs in Soul. Redundancy between sections means content is in the wrong place.

**Asymmetry in relationships is normal.** A named relationship does not require the other character to name it back. Write only what this character actually experiences.

---

## Background, Body & Soul

See `framework.md` for construction format, coverage requirements, the When/Behavior/Because formula, and examples for all three sections.

---

## Relationships

See `relationships.md` for the full relationship archetypes, coverage requirements, generativity hierarchy, perspective-focus rules, and entry format.

---

## Story Notes

**Story notes instead of inline storylines.** Story possibilities for this character live in separate story notes, not in the character note. When you have enough clarity on a character's arc, create a story note with `type: story`, `scope: "[intention](notes/intention.md)"`, and `characters: ["[Character Name](notes/Character Name.md)"]`. Link back to the character note via the `characters:` field. See `worldbuilder-story` for story note structure.

The introduction note is also a story note (`scope: "[introduction](notes/introduction.md)"`). When you have enough character clarity to know where and how the player would first meet this character, create it then.

---

## Intimate Dynamics

Check the project plan before starting any blueprint. If the character is flagged for intimate dynamics, read `intimate.md` before beginning the Soul section. If the flag is absent, skip `intimate.md` entirely — do not prompt for it or ask about it.

---

## Post-Group Sync Pass

After completing a household group or batch of characters, run a relationship sync pass before moving on. Characters develop during the blueprinting sequence — a character written later may shift in ways that make an earlier character's relationship entry inaccurate. Check the group's notes against each other: are named relationships still consistent? Update when the sequence reveals something that changes the picture.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] All required fields present
- [ ] `factions` uses markdown links: `[Name](notes/name.md)`
- [ ] `status` is `draft` or `complete`

**Design Notes**
- [ ] `### Session Notes` present with Q&A capture
- [ ] `### Builder Context` present as applicable; not padded

**Background**
- [ ] Declarative fact pairs only — no behavioral content, no prose elaboration

**Body**
- [ ] Entries grounded in physical experience
- [ ] No forced entries — thin is acceptable if nothing is distinctive

**Soul**
- [ ] 3–5 psychological behavioral entries minimum
- [ ] 2–3 general social behavior entries minimum
- [ ] One contradiction stated as a behavioral description
- [ ] Irrational behavior with emotional root present
- [ ] Self-image gap expressed as behavioral description
- [ ] Speech patterns described concretely if distinctive
- [ ] Because clauses trace to the user's stated wants, fears, or experiences from Session Notes — if a Because clause didn't emerge from the Q&A, ask the user before writing
- [ ] Plain language throughout — no literary flair, no Latinate vocabulary
- [ ] No negative-led characterization (state what they ARE)
- [ ] No forward references (starting state only)

**Relationships**
- [ ] Coverage requirements met: 8 named relationships for major characters, 5 for supporting; required anchor types present (family or Ghost, Authority, friction or rivalry, Confidant — see `relationships.md` for full requirements)
- [ ] Each entry in bullet format with `**Name — Archetype(s):**` prefix
- [ ] Each entry describes behavioral dynamic, not history or emotional label
- [ ] Each entry describes this character's experience only, not the other person's traits

**Intimate Dynamics (if flagged)**
- [ ] Behavioral entries covering attraction expression, hesitation/limits, specific dynamic if present
- [ ] One friction point present

**Story Notes**
- [ ] Story notes created or flagged as pending for any known character arcs
- [ ] Introduction note created or flagged as pending

**Pre-Handoff Scan**
- [ ] Before moving to the next character, scan the session for any decisions made about characters who do not yet have a complete note
- [ ] Record any such decisions as a Blueprint note in that character's cast plan entry in `worldbuilding-plan.md`

**Brief**
- [ ] `brief:` written and reflects the completed character; no recommendations, no design rationale
