---
name: worldbuilder-character
description: Use when building or developing a character for an AI-powered RPG or collaborative fiction — creating from scratch, deepening an existing character note, or fixing a character who feels flat, inconsistent, or generating repetitive LLM output.
---

# Character Blueprint

## Overview

A character for an LLM-powered game is not a description — it is a behavioral specification. The engine handles generic social warmth and distance; the character note supplies the specific: what this character carries privately, what they do when trust is low or high, what their contradiction is. Three dimensions build this: body (the physical), environment (the formative), soul (the psychological). Each feeds the next.

The character note is the comprehensive single source of truth for a character in the Wide phase. It is richer than any export format can hold — it contains everything true about the character, including material that won't appear in any platform output. Export skills derive their output from this note.

---

## Character Note Structure

Work through sections in order. Do not skip sections because the character seems simple — every section exists to catch what the others miss.

| Section | Sub-file | Notes |
|---|---|---|
| Frontmatter | — | YAML; see below |
| Preamble | — | 2–3 sentences; see below |
| Design Notes | — | Builder context; excluded from exports |
| Foundation | `framework.md` | Body, Environment, Soul |
| Behavioral Descriptions | `framework.md` | When/Behavior/Because formula; contradictions |
| Relationships | `relationships.md` | Social web; 12 archetypes; coverage check |
| Relationship Behavior | — | Trust/distance axis; see below |
| Intimate Dynamics (if flagged) | `intimate.md` | Only if flagged in project plan |

---

## Frontmatter

Every character note opens with YAML frontmatter. Required fields:

```yaml
type: character
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
factions: ["[[Household Name]]", "[[Guild Name]]"]   # list; links to faction notes
role: plain text
archetype: "[[Initially Hostile]]"                    # link; makes archetype groups queryable
```

`factions` and `archetype` use `[[wikilinks]]`. The export skill and Obsidian graph both query these fields. `role` stays plain text — it is too specific per character to warrant a navigable link.

---

## Preamble

2–3 sentences at the top of the note body (after frontmatter). Answers: what is this character, and when should this note be used?

> *Aldric is the village blacksmith and the player's primary source of crafting and tool repair. Use this note when the player interacts with him, mentions the smithy, or asks about anything to do with metalwork or local crafts. He is the most physically imposing cast member and the one most likely to underestimate the player initially.*

This is the fast-path layer — the summary that makes the note immediately useful without reading it in full. Write it as if briefing a new reader who needs to use the character correctly right now.

---

## Design Notes

Design Notes is a bullet-point section containing anything that drives the design of this character but does not appear directly in the behavioral content. Excluded from all exports — write freely here.

Typical bullets to include:
- Narrative function: what this character uniquely contributes to the setting; what kinds of scenes they anchor; what tension or theme they embody
- External references: named real people, fictional characters, or combinations that shaped the design; what specifically was drawn from each
- Design decisions and constraints: choices made that would be confusing without context
- Open questions: unresolved decisions to revisit in future sessions

Leave blank if there is nothing worth capturing here. Do not pad it with character summary.

---

## Foundation, Behavioral Descriptions, Relationships

See `framework.md` for Foundation (Body, Environment, Soul) and Behavioral Descriptions (When/Behavior/Because formula, contradictions). See `relationships.md` for the Relationships section.

> **Note on Appearance:** Physical description belongs in Body (Foundation) — it is part of who the character is, not a separate section. Export skills derive appearance from Body. Existing character notes that have a standalone `## Appearance` section can keep it; export skills will read it if found. New notes should put this information in Body only.

Key rules that apply throughout all three:

**Make decisions, don't hedge.** Every fact in the note is a decision. Never write "X or Y" or "grew up somewhere, perhaps Y" unless the ambiguity is a deliberate mystery being preserved intentionally. If you don't know, ask the user. A character who "grew up in the city or possibly a small town" is an incomplete note, not a subtle one.

**Note register is functional, not literary.** Plain, direct language throughout. Prefer short concrete words over Latinate vocabulary: "she knows," "he keeps it to himself" rather than "she maintains an internal rationalization," "he sustains that framing." If a sentence sounds like it belongs in a novel, rewrite it as a direct statement. Only Example Dialogue earns stylistic voice.

**Write what characters ARE, not what they aren't.** Positive statements give the LLM something to act on. Negative constructions ("not the quiet one," "doesn't believe in magic") define by absence — the LLM has to invent the positive case itself. State the fact directly. Factual negatives are fine when the un-done thing is the meaningful information: "she has not sent the letter," "he hasn't asked."

**The note describes the character's starting state.** Nothing in the character note may reference events that haven't happened yet or developments that require time to unfold. Check: has this already happened before the player meets this character? If not, create a story note for it or cut it.

**Section discipline.** Each section carries information the others don't. Soul and behavioral descriptions describe general patterns — if a behavior is primarily about one specific relationship, it belongs in Relationships. History and formative events involving named people belong in Environment. Redundancy between sections usually means content is in the wrong place.

**Asymmetry in relationships is normal.** A named relationship does not require the other character to name it back. Write only what this character actually experiences.

---

## Relationship Behavior

How this character acts and speaks across the like/dislike axis. Written as behavioral description — not a numbered band format.

Cover these dimensions without subheadings (prose):

- **Default register:** How they present to people they don't know yet. What a stranger experiences.
- **Warmth:** What it looks like when it's present. Does it show? How? What specifically changes in tone, words, or behavior when this character warms to someone?
- **Distance/conflict:** What distance, coldness, or active friction looks like for this character specifically. Not generic "they become cold" — describe the actual behavior.
- **Relationship-type variation:** If this character behaves notably differently with authority figures vs. peers vs. someone they're protecting, note it. Skip this if there is no meaningful variation.

The intimate register is handled separately in the Intimate Dynamics section if flagged.

Export skills map this section to platform mechanics (influence bands, trust tiers, etc.) as needed. Write it as behavioral truth; the platform mapping is not your concern here.

---

## Story Notes

**Story notes instead of inline storylines.** Story possibilities for this character live in separate story notes, not in the character note. When you have enough clarity on a character's arc, create a story note with `type: story`, `scope: "[[intention]]"`, and `characters: ["[[Character Name]]"]`. Link back to the character note via the `characters:` field. See `worldbuilder-story` for story note structure.

The introduction note is also a story note (`scope: "[[introduction]]"`). When you have enough character clarity to know where and how the player would first meet this character, create it then.

---

## Intimate Dynamics

Check the project plan before starting any blueprint. If the character is flagged for intimate dynamics, read `intimate.md` before beginning the Relationship Behavior section. If the flag is absent, skip `intimate.md` entirely — do not prompt for it or ask about it.

---

## Post-Group Sync Pass

After completing a household group or batch of characters, run a relationship sync pass before moving on. Characters develop during the blueprinting sequence — a character written later may shift in ways that make an earlier character's relationship entry inaccurate. Check the group's notes against each other: are named relationships still consistent? Update when the sequence reveals something that changes the picture.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] All required fields present
- [ ] `factions` and `archetype` use `[[wikilinks]]`
- [ ] `status` is `draft` or `complete`

**Preamble**
- [ ] 2–3 sentences; answers what this character is and when to use this note
- [ ] Usable without reading the full note

**Design Notes**
- [ ] Bullet-point format; covers narrative function, external references, design decisions, and/or open questions as applicable; not padded with character summary

**Foundation + Behavioral Descriptions**
- [ ] 3–5 behavioral descriptions in When/Behavior/Because form
- [ ] One clear contradiction or friction point
- [ ] Irrational behavior with emotional root
- [ ] Self-image gap stated directly
- [ ] Speech patterns described concretely if distinctive
- [ ] Plain language throughout — no literary flair
- [ ] No negative-led trait characterization (state what they ARE)
- [ ] No forward references to events that haven't happened yet (the note describes starting state only; future arc possibilities go in story notes)

**Relationships**
- [ ] Coverage requirements met (see `relationships.md`)
- [ ] Each entry specifies current behavioral dynamic, not just history or emotional label
- [ ] Each entry describes this character's experience of the other person, not the other person's traits

**Relationship Behavior**
- [ ] Default register described
- [ ] Warmth described specifically (not "they become warm")
- [ ] Distance/conflict described specifically (not "they become cold")
- [ ] Relationship-type variation noted if it exists

**Story Notes**
- [ ] Story notes created or flagged as pending for any known character arcs
- [ ] Introduction note created or flagged as pending

**Pre-Handoff Scan**
- [ ] Before moving to the next character, scan the session for any decisions made about characters who do not yet have a complete note
- [ ] Record any such decisions as a Blueprint note in that character's cast plan entry in `worldbuilding-plan.md`
