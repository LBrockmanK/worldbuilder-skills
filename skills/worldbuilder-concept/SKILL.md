---
name: worldbuilder-concept
description: Use when writing concept notes for an AI-powered narrative game — establishing surface facts, mid-layer history, deep secrets, recurring world events, or background NPC guidelines. Also use when a concept note feels too broad or too narrow, or when deciding what layer a piece of world knowledge belongs on.
---

# Lorebook

## Overview

World knowledge is organized in `notes/` notes — one note per discrete topic. Export skills read these notes and package them as lorebook entries. This skill covers writing the concept notes well; the export skill handles the packaging.

Good concept notes give the engine exactly what it needs at the moment a topic arises. The goal is precision: the right information for the right moment. Write notes that are dense and specific rather than broad and atmospheric — 50 tokens of exact context beats 300 tokens of unfocused description.

## Concept Note Frontmatter

Every concept note opens with:

```yaml
type: concept
status: draft | complete
aliases: []           # key terms and synonyms — become keyword candidates at export
last_updated: YYYY-MM-DD HH:mm
layer: "[[surface]]" | "[[mid]]" | "[[deep]]"
trigger-context: brief plain-text note on when this should activate
```

`aliases` is the most important field for a concept note. Include every realistic way the topic might be mentioned in dialogue: local names, common phrasings, player-accessible synonyms. The export skill derives keywords from these.

`trigger-context` is a brief note for future reference: what situation causes this lore to be relevant? One phrase is enough. "When player is at or near the old mill" or "When someone mentions the founding family." This guides both alias selection and content focus.

---

## Narrative Purpose

Before writing a concept note's content, answer one question:

> *What does the existence of this thing make impossible, costly, or inevitable in a scene that touches it?*

A concept note that cannot answer this question is description, not a constraint. Writing the answer first shapes what to include and what to cut.

---

## Alias Writing Guidance

The export skill derives keyword triggers from the `aliases` field. Writing good aliases requires thinking about how topics actually come up in dialogue.

**Coverage:** Include every realistic phrasing. If the note is about a specific location, include multiple forms: "the mill," "old mill," "Harrow's mill," "the water wheel." A single overly-precise phrase that never appears verbatim will never trigger.

**Plural and possessive forms:** Matching is typically exact-string. "mill" won't match "mill's" or "mills." Include the forms that will actually appear in dialogue.

**Specificity:** Short generic terms match too broadly. "inn" might fire on "innocent." "well" fires on "well-lit." Prefer multi-word aliases where ambiguity exists: "the inn," "the old well."

**Local names:** Players and characters use the names they know, not the canonical names you used in the note title. Include both.

**Common mistakes:** Single generic word that fires constantly; forgetting local names or synonyms; so many required terms that the combination almost never matches in practice.

---

## Limitations and Costs

For any concept note covering a rule-bearing concept — magic systems, institutions, cultural practices, social structures, belief systems, anything with internal logic that scenes must respect — include a limitations and costs block.

The block specifies:
- What the concept **cannot** do
- What it **costs or demands** from those who use it or participate in it
- What makes it **fail, break, or produce unexpected results**

A concept documented only by what it can do cannot constrain a scene. One documented by its limits and costs can.

**Example:** A healing magic concept note that says "healers can mend wounds and cure illness" does not constrain anything. One that adds "healing draws from the healer's own vitality — serious wounds leave the healer bedridden for an equal period, and healing the dying risks the healer's own death" constrains every scene that touches it.

Concept notes for rule-bearing concepts without a limitations block are incomplete — see the self-check at the end of this skill.

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

## The Iceberg Split

Distinct from the surface/mid/deep layer classification. The iceberg split operates *within a single note*, for cases where what people in the world believe and what is actually true diverge.

Where the gap between belief and truth is narratively significant, document both explicitly in the same note:

**Believed:** what characters in the world commonly say, assume, or act on — the public version, the legend, the received wisdom.

**True:** what actually happened, or how the thing actually works underneath the common understanding.

This lets the engine have characters speak and act from belief while the true version constrains what can actually happen and what specific informed characters know.

Not every concept note needs this. Use it only when the gap between belief and truth is a live story element.

**Note on layer classification:** The surface/mid/deep layer on a concept note records authorial intent about pacing and register. It is not a reliable mechanism for suppressing information from the engine at runtime — whether a given engine can actually gate context on conditions varies. Its value is in shaping how the content is written (surface: matter-of-fact; mid: hedged and uncertain; deep: confirmed and weighted) and in what export tools can do with the metadata.

## Location Notes

Location notes have their own dedicated skill: **`worldbuilder-location-blueprint`**. Use that skill when creating or deepening any named location.

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

## Recurring World Events

Festivals, seasonal observances, cultural rituals, and other recurring world events are concept notes like any other world knowledge. Write one note per discrete event.

**Layer classification applies:**
- Surface — well-known community celebrations; everyone participates, no one questions it
- Mid — observances with historical depth or old stories behind them; the community marks them but the origins are half-forgotten
- Deep — rituals with hidden significance, ancestral ceremonies that touch the hidden layer of the setting

**Write the mood, not what happens.** An event note describes the community's collective behavior, the physical and emotional register of the day, what kinds of interactions become natural, and the traditions that anchor it. The engine generates specific scenes from this context — write what makes those scenes possible.

**Aliases** should cover every realistic way the event comes up in dialogue: common name, formal name, what characters actually say ("the festival," "harvest time," "the long night"). The export skill derives keyword triggers from these.

**Limitations and costs apply here too.** If the event carries social obligation, ritual restriction, or community pressure, document it. A harvest festival that everyone is expected to attend and that carries real social consequence for absence generates more behavioral content than one that is merely pleasant.

The export skill packages recurring event notes into platform-specific calendar formats. Write for the AI's context — the platform format is the export skill's concern.

---

## Concept Note Lifecycle

World knowledge is a living collection, not a phase that opens and closes. Any stage of the project can produce facts worth capturing: a household design decision, a character backstory detail, an event's implied history, a conversation that clarifies the magic system. Create a concept note whenever a discrete piece of world knowledge solidifies — do not wait.

**During active development:** When any working session produces a fact or implication that belongs in the lorebook, create a concept note stub immediately — frontmatter + preamble is enough to anchor the thought. Flesh it out when you have more context.

**At project completion:** Run a validation pass across all `notes/` notes:
- Verify every note has complete frontmatter including `layer` and `aliases`
- Check for contradictions across layers — surface notes should not imply what deep notes are supposed to reveal
- Cross-reference with completed character notes: any implied lore in those notes that has no concept note?
- Check that each note's `trigger-context` is specific enough to inform good keyword derivation at export

**Don't front-load.** Writing all concept notes before characters are drafted means writing them before you know what the characters will imply about the world. Let the `notes/` collection grow with the project.

---

## Writing Principles

**Short is usually better.** An entry that injects 50 tokens of precise context beats one that injects 300 tokens of unfocused description. The goal is the right thing at the right moment.

**Don't activate on overly common words.** A keyword of "house" or "old" will trigger on nearly every scene. Keywords should be specific enough that they only fire when the topic is actually relevant.

**Separate entries for separate topics.** Don't pack "the old mill AND the mill family AND the flood of thirty years ago" into a single entry. Split them so each triggers independently and doesn't bloat context when only one is relevant.

**Test the trigger mentally.** Read a sample scene where the topic comes up naturally. Does your keyword set cover the realistic phrasings? Does it avoid triggering on unrelated uses of the same word?

---

## Self-Check Before Marking Complete

**Complete when:** the note can constrain or shape any scene that touches this concept — a scene author reading the note knows what is impossible, what costs something, and what is inevitable because this thing exists.

**Limitations block check:** if this is a rule-bearing concept (magic system, institution, cultural practice, social structure, belief system), does the note include a limitations and costs block? A concept note without one is incomplete regardless of how much descriptive content it contains.

**Over-documented when:** any section adds detail no scene will touch, or duplicates content already in a character, location, or faction note. Concept notes are meant to be short and dense — duplication bloats context for no gain.
