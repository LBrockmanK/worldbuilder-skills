---
name: worldbuilder-lorebook
description: Use when writing world lore entries for an AI-powered narrative game — establishing surface facts, mid-layer history, deep secrets, location descriptions, or background NPC guidelines. Also use when designing keyword triggers and date gates for those entries, or when lorebook entries are injecting too much irrelevant context or too little relevant context.
---

# RPG Lorebook

## Overview

Lorebook entries are keyword-triggered context injected into the LLM's prompt when relevant terms appear in recent scene dialogue. They are precision tools, not flavor text. When keywords match, the matching lore is automatically injected into that specific prompt — giving the engine the right information exactly when it needs it, without bloating every prompt with lore that isn't relevant.

Good entries give the engine exactly what it needs at the moment a topic arises. Poor entries are either never triggered (bad keywords) or always triggered (too broad), polluting context with irrelevant material.

---

## How Matching Works

Before each scene, the engine scans recent dialogue and scene context for keywords. Matching entries are injected into that prompt only.

**AND groups:** Use `+` between words to require all of them. `ruins+old` triggers only when both appear in context.

**OR groups:** Comma-separated keywords trigger if any match. `old mill, abandoned mill, the mill` triggers on any of these.

**Date gates:** Set an earliest activation day. Entries with a future gate date are invisible until that day passes. Use this to prevent deep lore from surfacing before the player has spent enough time in the setting.

**Keyword coverage:** Include the variations people would actually use in conversation. If the entry is about a specific location, include multiple phrasings: "the mill," "old mill," "Harrow's mill," "the water wheel." Don't require exact matches on a single obscure trigger.

**Plural and possessive forms:** Exact-string matching doesn't account for "mill's" or "mills" if your keyword is "mill." Include the forms that will actually appear in dialogue.

**Partial-match traps:** Short keywords can match inside longer words depending on platform. "Inn" might fire on "innocent." "Well" fires on "well-lit." Prefer multi-word triggers where ambiguity exists: "the inn," "the old well" rather than bare short words.

**Common keyword mistakes:** Single overly-precise phrase that never appears verbatim; single generic word that fires constantly; forgetting local names or player-accessible synonyms for the same thing; requiring AND combinations so restrictive they almost never match.

---

## The Three-Layer Structure

The setting deepens as the player invests. Do not front-load. Surface entries establish a mundane world with texture; mid-layer entries acknowledge the old stories; deep entries confirm what the hints implied. Jumping straight to deep lore in early entries kills the effect.

### Surface layer (always active — no date gate)

What everyone knows. The baseline reality of the setting.

- Geography and physical character of the setting
- Economy — what does this place do, how do people make a living
- Social texture — is the community close-knit, fractured, proud, struggling
- Common local history — the stories everyone tells
- Practical knowledge relevant to the player's daily activities

**Tone:** Matter-of-fact. No mysticism. These entries establish normalcy so that later disruptions of normalcy carry weight. If a surface entry contains a hint like "but some say this is connected to the old stories," you've broken the layer structure.

### Mid-layer (date-gate: roughly the end of the first season)

Things people half-remember. Old stories told as legend but believed a little.

- The old stories — things the community tells as history but with mythic edges
- Wilderness, ruins, old buildings and what people say about them
- Historical events that left marks: a fire, a founding family's story, something that divided the community
- Hints at what lies beneath the surface

**Tone:** Uncertain. Hedged. People who know these stories are not sure they believe them. "They say..." "It's probably nothing, but..." Characters rationalize and deflect.

### Deep layer (date-gate: second season or later)

The actual hidden layer — what the hints were pointing toward.

- The supernatural specifics (if the setting has them)
- The setting's true history
- The real origin of the wound
- Any non-human or supernatural entities in detail

**Tone:** Confirmed and weighted. These entries feel like the answer to questions the surface layer raised. Don't explain everything — some things can remain permanent mystery.

---

## Location Entries

Short. Physical character first, then narrative associations.

Cover:
- What the place looks like
- Who comes here, why, what they do
- What it means — the emotional or narrative weight of this location
- One vivid specific detail

One vivid detail beats three paragraphs of layout. "The old mill hasn't operated in fifteen years. The water wheel still turns sometimes when there's no wind." tells the engine more useful things than a floor plan.

Location entries are not image generation descriptions. They tell the engine what a place means and who uses it — not a visual reference. Image generation descriptions are a separate document.

---

## Background NPC Guidelines

Rather than individual unnamed characters, write guidelines for how the engine should construct background figures. Include in a lorebook entry active from day 1.

Cover:
- What kinds of people live here — occupations, ages, social roles
- What personality tendencies fit the setting's character
- How they should be incorporated when the player engages with them
- What topics they discuss, what they know, what they don't

This gives the engine a construction kit rather than a cast list, producing more varied and naturalistic background interactions than a list of named extras.

---

## Lorebook Lifecycle

The lorebook is a living document, not a phase that opens and closes. Any stage of the project can produce facts worth capturing: a household design decision, a character backstory detail, a calendar event's implied history, a conversation that clarifies the magic system. Do not wait until "the lorebook phase" to write entries — you will forget what you meant to capture.

**During active development:** Maintain a `lorebook-notes.md` scratch file. When any working session produces a fact, name, or implication that belongs in the lorebook, drop it there immediately — a single sentence is enough to anchor the thought. It does not need to be written as a full entry yet.

**At project completion:** Run a focused validation pass across the full lorebook:
- Write any entries that are still only notes
- Test every keyword set: does it cover the realistic phrasings? Does it trigger on things it shouldn't?
- Check for contradictions across layers — surface entries should not imply what deep entries are supposed to reveal
- Verify date gates: are entries gated appropriately for what they reveal?
- Cross-reference with completed character cards: any implied lore in the cards that has no lorebook entry?

**Don't front-load.** Writing the complete lorebook before characters are drafted means writing it before you know what the characters will imply about the world. Let the lorebook reflect the full project, not just what you knew at the start.

---

## Writing Principles

**Short is usually better.** An entry that injects 50 tokens of precise context beats one that injects 300 tokens of unfocused description. The goal is the right thing at the right moment.

**Don't activate on overly common words.** A keyword of "house" or "old" will trigger on nearly every scene. Keywords should be specific enough that they only fire when the topic is actually relevant.

**Separate entries for separate topics.** Don't pack "the old mill AND the mill family AND the flood of thirty years ago" into a single entry. Split them so each triggers independently and doesn't bloat context when only one is relevant.

**Test the trigger mentally.** Read a sample scene where the topic comes up naturally. Does your keyword set cover the realistic phrasings? Does it avoid triggering on unrelated uses of the same word?
