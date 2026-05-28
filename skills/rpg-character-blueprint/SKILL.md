---
name: rpg-character-blueprint
description: Use when building or developing an individual character for an AI-powered RPG or collaborative fiction — creating from scratch, expanding a roster entry into a full blueprint, or assembling a final character card. Also use when a character feels flat, inconsistent, or is generating repetitive LLM output.
---

# RPG Character Blueprint

## Overview

A character for an LLM-powered game is not a description — it is a behavioral specification. The engine already handles generic social warmth and distance; what the card must supply is the specific: what this character carries privately, what they do when trust is low or high, what their contradiction is. Three dimensions build this: body (the physical), environment (the formative), soul (the psychological). Each feeds the next.

## Three-Layer Workflow

Characters develop in stages. Do not write a final card before the blueprint is complete.

**Stage 1 — Roster entry:** Short reference per character: role, archetype, key relationships. The cast-wide reference tool.

**Stage 2 — Blueprint:** Full worksheet output. See sub-files below for each section. Iterate until the character is internally consistent and connected to the broader cast.

**Stage 3 — Card:** The blueprint translated into seamless prose. Not an expanded version with more content — the same information woven into a single flowing description without headings or labels. The card contains: the personality/description prose (all foundation dimensions and behavioral descriptions integrated), the influence thresholds (woven with in-character behavioral examples), metadata fields, and future storylines. Example dialogue as a separate section only if it cannot be woven into the prose naturally. Invoke `anthropic-skills:writing` before writing the final card — prose register matters and LLM defaults produce flat output.

**Before starting any blueprint:** Check the character's roster entry for an `Intimate Dynamics: Yes` flag. If present, read `intimate.md` in this skill directory and complete that section as part of the blueprint. If absent, skip it entirely — do not prompt for it or ask about it.

---

## Key Rules

These apply throughout all stages and address the most common blueprint failures.

**Make decisions, don't hedge.** Every fact in the blueprint is a decision. Never write "X or Y," "possibly X," or "grew up somewhere, perhaps Y" unless the ambiguity is a deliberate narrative mystery being preserved intentionally. If you don't know, ask the user. A character who "grew up in the city or possibly a small town" is an incomplete blueprint, not a subtle one.

**Blueprint register is functional, not literary.** Plain, direct language throughout. "He deflects compliments by finding something to fix" is a blueprint sentence. Poetic constructions gesture at something without stating it — state it plainly instead. If a sentence sounds like it belongs in a novel, rewrite it as a direct statement.

**Section discipline.** Each section carries information the others don't. Soul and behavioral descriptions describe general patterns — if a behavior is primarily about one specific relationship, it belongs in Relationships, not here. History and formative events using named people belong in Environment. Redundancy between sections usually means content is in the wrong place.

**Asymmetry in relationships is normal.** A named relationship does not require the other character to name it back. Write only what this character actually experiences — not what would be reciprocally tidy.

---

## Blueprint Sections

Work through these in order. Read the relevant sub-file before writing each section.

| Section | File | Notes |
|---|---|---|
| Part 1: Foundation | `framework.md` | Body, Environment, Soul |
| Part 2: Behavioral Builder | `framework.md` | When/Behavior/Because formula, contradictions |
| Relationships | `relationships.md` | Social web; archetypes; coverage check |
| Part 3: Assembly + Self-Check | `assembly.md` | Card prose structure, register rules, checklist |
| Part 4: Influence Thresholds | `thresholds.md` | Six bands, format, in-character examples |
| Part 5: Future Storylines | Below (inline) | Short enough to keep here |
| Part 6: Metadata | Below (inline) | Short enough to keep here |
| Intimate Dynamics (if flagged) | `intimate.md` | Only if roster entry has `Intimate Dynamics: Yes` |

### Post-group sync pass

After completing a household group or batch of characters, run a brief relationship sync pass before moving on. Characters develop during the blueprinting sequence — a character written later may have shifted in ways that make an earlier character's relationship entry inaccurate or incomplete. Check the group's blueprints against each other: are named relationships still consistent? Did any character develop in a direction that changes how another character should see them? Blueprints are not frozen once written; update them when the sequence reveals something that changes the picture.

---

## Part 5: Future Storylines

Give the LLM material for character development arcs. Write as analytical direction — possibilities, not scripts. The LLM cannot reliably fire conditional events; give it material to work from and let it find the moment.

**The Introduction (required):** Every card must have an Introduction as the first Future Storylines entry: the likely first encounter with the player.

- Where it happens, what the character is doing, how they register the player's presence
- The character should be mid-task, not waiting
- There should be a natural reason for contact
- Behavior immediately consistent with their register at low influence
- Written as direction, not a scene with fixed dialogue

**Additional storylines:** Each entry phrased as possibility ("may surface," "could take," "there is a possibility that"). Identifies what conditions make the arc possible without scripting a trigger. Describes what the character would do or reveal, not what the plot outcome is.

Write for robustness — arcs that remain interesting whether or not a specific beat fires.

---

## Part 6: Metadata

Structured fields at the end of the card.

**Events** — Calendar entries specific to this character: birthdays, recurring personal dates, significant days.

**Core fields:** First Name, Last Name; Type (Major or Supporting); Available Day; Role (one or two phrases).

**Appearance** — Physical description for image generation and LLM reference. Cover: species/type and sex (if relevant), age presentation and body type, notable features, clothing style in 1–2 sentences. Must be consistent with the Personality/Description.

**Sprite Sets** — Named visual states for artwork. These are artwork categories, not emotional expressions. "Concerned" is not a sprite set — it is an expression that exists within any state. Standard states: Casual (default, at rest), Working/Active (doing their primary activity), plus any additional states the character specifically warrants.
