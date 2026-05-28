---
name: worldbuilder-lorebook
description: Use when writing world knowledge concept notes for an AI-powered narrative game — establishing surface facts, mid-layer history, deep secrets, location descriptions, or background NPC guidelines. Also use when a concept note feels too broad or too narrow, or when deciding what layer a piece of world knowledge belongs on.
---

# Lorebook

## Overview

World knowledge is organized in `concepts/` notes — one note per discrete topic. The ainime export skill reads these notes and packages them as keyword-triggered lorebook entries. This skill covers writing the concept notes well; the export skill handles the packaging.

Good concept notes give the engine exactly what it needs at the moment a topic arises. The goal is precision: the right information for the right moment. Write notes that are dense and specific rather than broad and atmospheric — 50 tokens of exact context beats 300 tokens of unfocused description.

## Concept Note Frontmatter

Every concept note opens with:

```yaml
type: concept
status: draft | complete
aliases: []           # key terms and synonyms — become keyword candidates at export
last_updated: YYYY-MM-DD
layer: "[[surface]]" | "[[mid]]" | "[[deep]]"
trigger-context: brief plain-text note on when this should activate
```

`aliases` is the most important field for a concept note. Include every realistic way the topic might be mentioned in dialogue: local names, common phrasings, player-accessible synonyms. The export skill derives keywords from these.

`trigger-context` is a brief note for future reference: what situation causes this lore to be relevant? One phrase is enough. "When player is at or near the old mill" or "When someone mentions the founding family." This guides both alias selection and content focus.

---

## Alias Writing Guidance

The export skill derives keyword triggers from the `aliases` field. Writing good aliases requires thinking about how topics actually come up in dialogue.

**Coverage:** Include every realistic phrasing. If the note is about a specific location, include multiple forms: "the mill," "old mill," "Harrow's mill," "the water wheel." A single overly-precise phrase that never appears verbatim will never trigger.

**Plural and possessive forms:** Matching is typically exact-string. "mill" won't match "mill's" or "mills." Include the forms that will actually appear in dialogue.

**Specificity:** Short generic terms match too broadly. "inn" might fire on "innocent." "well" fires on "well-lit." Prefer multi-word aliases where ambiguity exists: "the inn," "the old well."

**Local names:** Players and characters use the names they know, not the canonical names you used in the note title. Include both.

**Common mistakes:** Single generic word that fires constantly; forgetting local names or synonyms; so many required terms that the combination almost never matches in practice.

---

## The Three-Layer Structure

The setting deepens as the player invests. Do not front-load. Surface entries establish a mundane world with texture; mid-layer entries acknowledge the old stories; deep entries confirm what the hints implied. Jumping straight to deep lore in early entries kills the effect.

### Surface layer (active from the start)

What everyone knows. The baseline reality of the setting.

- Geography and physical character of the setting
- Economy — what does this place do, how do people make a living
- Social texture — is the community close-knit, fractured, proud, struggling
- Common local history — the stories everyone tells
- Practical knowledge relevant to the player's daily activities

**Tone:** Matter-of-fact. No mysticism. These entries establish normalcy so that later disruptions of normalcy carry weight. If a surface entry contains a hint like "but some say this is connected to the old stories," you've broken the layer structure.

### Mid-layer (available after early investment)

Things people half-remember. Old stories told as legend but believed a little.

- The old stories — things the community tells as history but with mythic edges
- Wilderness, ruins, old buildings and what people say about them
- Historical events that left marks: a fire, a founding family's story, something that divided the community
- Hints at what lies beneath the surface

**Tone:** Uncertain. Hedged. People who know these stories are not sure they believe them. "They say..." "It's probably nothing, but..." Characters rationalize and deflect.

### Deep layer (available after significant investment)

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

## Concept Note Lifecycle

World knowledge is a living collection, not a phase that opens and closes. Any stage of the project can produce facts worth capturing: a household design decision, a character backstory detail, an event's implied history, a conversation that clarifies the magic system. Create a concept note whenever a discrete piece of world knowledge solidifies — do not wait.

**During active development:** When any working session produces a fact or implication that belongs in the lorebook, create a concept note stub immediately — frontmatter + preamble is enough to anchor the thought. Flesh it out when you have more context.

**At project completion:** Run a validation pass across all `concepts/` notes:
- Verify every note has complete frontmatter including `layer` and `aliases`
- Check for contradictions across layers — surface notes should not imply what deep notes are supposed to reveal
- Cross-reference with completed character notes: any implied lore in those notes that has no concept note?
- Check that each note's `trigger-context` is specific enough to inform good keyword derivation at export

**Don't front-load.** Writing all concept notes before characters are drafted means writing them before you know what the characters will imply about the world. Let the `concepts/` collection grow with the project.

---

## Writing Principles

**Short is usually better.** An entry that injects 50 tokens of precise context beats one that injects 300 tokens of unfocused description. The goal is the right thing at the right moment.

**Don't activate on overly common words.** A keyword of "house" or "old" will trigger on nearly every scene. Keywords should be specific enough that they only fire when the topic is actually relevant.

**Separate entries for separate topics.** Don't pack "the old mill AND the mill family AND the flood of thirty years ago" into a single entry. Split them so each triggers independently and doesn't bloat context when only one is relevant.

**Test the trigger mentally.** Read a sample scene where the topic comes up naturally. Does your keyword set cover the realistic phrasings? Does it avoid triggering on unrelated uses of the same word?
