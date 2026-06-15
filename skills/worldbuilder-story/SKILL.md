---
name: worldbuilder-story
description: Use when writing arc notes and intention notes for an AI-powered narrative game, or when producing direction.md in Phase 1. Also use when LLM output escalates too fast, when romantic or dramatic intensity feels unearned, when dark content is handled carelessly, or when scenes lack pacing variation.
---

# Story

## Overview

This skill serves two related purposes:

**Phase 1b — direction.md:** `direction.md` is the world's standing creative brief and the story engine's primary guard rail. It is a project document (`type: project`), produced in Phase 1 by world-planning using this skill's section templates as guidance. See the Ongoing Story Direction section below for its complete structure.

**Phase 2b — Arc, intention, and introduction notes:** Once direction.md exists, this skill creates the story notes that extend it. Story notes live in `notes/` and link up to `direction.md` via `up:` frontmatter.

Story note types:

**Arc** (`scope: "[arc](notes/arc.md)"`) — A major story section. `up: "[Direction](notes/Direction.md)"`. Covers a season, a storyline, or a thematic phase.

**Intention** (`scope: "[intention](notes/intention.md)"`) — A specific story possibility within an arc. `up: "[Arc Name](notes/Arc Name.md)"`. Not scripted outcomes — soft targets the world is set up to enable.

**Introduction** (`scope: "[introduction](notes/introduction.md)"`) — First-contact scene for a specific character. Created during or after character note work, not during the story notes phase.

Frontmatter for story notes (arc, intention, introduction):
```yaml
type: story
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
up: "[Parent Note](notes/Parent Note.md)"               # link to parent story note
scope: "[arc](notes/arc.md)"                            # link; arc | intention | introduction
characters: ["[Name](notes/Name.md)"]                   # optional; links to character notes
brief: |    # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

Note: direction notes also use `type: story` but have no `up:` field. `brief` applies to all story notes including direction.

Structure for arc, intention, and introduction notes:

| Section | Notes |
|---|---|
| Frontmatter | YAML; see above |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| Situation | State of affairs before player involvement |
| Story Possibilities | What could happen; phrased as possibility not script |

Read `direction.md` before creating arc notes. Arc notes develop what the brief establishes — they do not contradict it.

---

## Working with Vault Files

**Renaming a note:** Use Edit or Write to rename the file. Then immediately run `agents/linker/scripts/rename-note.ps1 -OldName "OldName" -NewName "NewName" -VaultPath <vault-root>` to update all markdown links across the vault. Do not skip this step — Obsidian's auto-rename is bypassed when files are edited directly.

---

## Arc, Intention, and Introduction Notes

### Brief

`brief` is a frontmatter field, not a heading inside the note body. Write it last, after the full note is complete.

**For arc notes:** What this story arc is and what emotional territory it covers.
Example: "The mill arc: the founding family's buried guilt surfaces; the town must decide whether to protect the story they've told themselves or face what actually happened."

**For intention notes:** What this story possibility is in one sentence.
Example: "The confession scene: if trust reaches a high point during the autumn festival, Mira may tell the player what she actually saw the night of the flood."

**For introduction notes:** Who this introduces and the first impression.
Example: "Introduces Bram: the player's first encounter is him repairing something that isn't broken, because staying busy is easier than acknowledging they've arrived."

1–2 sentences. Other agents scan this field when planning arcs or building character notes.

### Design Notes

> **Excluded from exports.** The story engine acts on Situation and Story Possibilities. Design Notes are for the builder.

This section captures creative intent — the thinking behind the arc or moment before it becomes structure.

Cover:

- **Creative intent:** What kind of story is this emotionally? What should it feel like when it plays out? What experience is the builder trying to create for the player?
- **Inspirations:** Specific scenes, arcs, or moments from other media being evoked. Name what is being drawn from each — not just "like the opening of Episode 4" but what specifically about that opening: the scale, the stillness before action, the sense of something already in motion.
- **Why this is worth building toward:** What makes this arc or moment interesting? Why does it earn space in the world?
- **Open questions:** What is not yet resolved about this arc — thematic, structural, or about a specific character's behavior in it?

### Situation

This section establishes the state of things before any player involvement. Write in present tense.

**For arc and intention notes:**

- The current state of affairs in the world that makes this arc or intention possible
- Who is involved and what each party wants or fears going in
- Timing constraints or seasonal considerations if relevant
- Preconditions: what needs to be true — player trust level, prior events, season — for this arc or intention to be accessible

**For introduction notes:**

- Where and when the introduction could happen
- Who else is present
- What the circumstances are that make this a natural first meeting

### Story Possibilities

This section covers what could happen and how it could develop. Phrased as possibility, not script: use "may," "could," "there is a possibility that."

Do not script outcomes. Write for robustness — arcs that remain interesting whether or not a specific beat fires.

**For arc notes:**

- What could happen and how it could develop
- Key moments: the set pieces that make the arc feel real if they fire
- Resolution directions: natural ways things could go, not scripted outcomes
- Connection to other arcs or characters

**For intention notes:**

Typically shorter — one key possibility with the moment that would trigger it and the direction it could go.

**For introduction notes:**

How the scene plays, what the character does, what invitation it extends to the player.

---

## Self-Check Before Marking Complete (arc, intention, introduction notes)

**Brief**
- [ ] Written last
- [ ] 1–2 sentences; navigable summary of what this arc or intention is

**Design Notes**
- [ ] Creative intent stated
- [ ] Inspirations named with what specifically is being drawn
- [ ] Not padded

**Situation**
- [ ] State of affairs before player involvement stated
- [ ] Preconditions named

**Story Possibilities**
- [ ] All entries phrased as possibility, not script
- [ ] At least one key moment or set piece named
- [ ] Connection to other arcs or characters noted

---

## Ongoing Story Direction

> Direction notes are operational instructions for the story engine. They do not use the Design Notes / Situation / Story Possibilities structure — that structure applies to arc, intention, and introduction notes only.

### Author framing

Position the LLM as a skilled author giving voice to characters, not an entity that becomes them. Author-capture — losing narrative perspective, mirroring the player's mood regardless of whether that serves the story, abandoning a character's established behavioral patterns — is the root failure mode for most output quality problems.

Adapt this language:

> You are a skilled author giving voice to the characters of [setting name]. Each character has their own perspective, history, and behavioral tendencies that you maintain consistently. You do not become the characters — you portray them with authorial judgment, the same way a novelist writes compelling antagonists or morally complex figures without endorsing their views or losing narrative perspective.

**Positive framing only:** Write what characters are — their actual qualities, behaviors, and motivations — not what they aren't. "She is guarded" produces behavioral texture; "she is not warm or friendly" produces only absence. Negative constructions give the engine one mode (avoidance) instead of something to generate from. This applies to all character portrayal in the story direction and character descriptions.

### Romance pacing

The engine by default moves too fast. This section is the primary guard rail.

Adapt this language:

> Romantic relationships develop through accumulated familiarity, genuine emotional connection, and earned trust. Physical and sexual intimacy should not occur until a deep relationship is established — characters are not available simply because the player has been friendly. Romantic interest emerges gradually and should include moments of resistance, uncertainty, or vulnerability before commitment. Early flirtation is fine; it should not rapidly escalate. A relationship that has only had pleasant surface conversation is not ready for intimacy. Let each stage breathe.

Key elements to specify: slow and earned escalation; visible resistance and uncertainty before commitment; escalation that can only follow genuine emotional depth.

### Dark themes

Permission to go there, with guidance on how:

> Difficult material — depression, grief, addiction, family trauma, loss — exists in this world and can surface when context warrants it. Handle it with care and weight, not for shock value. Dark arcs tend toward hope but do not require resolution. A character in recovery is still in recovery; a character who is grieving may always carry some of that grief. The player is a witness and companion, not a therapist or savior. Do not rush toward catharsis.

Key framing: dark material is handled with weight, not shock value; resolution is not required; the player is witness, not savior.

### The hidden layer (if applicable)

For settings with supernatural or concealed depth:

> [The hidden layer] is real in this world but not advertised. Most characters who encounter something genuinely strange will rationalize it, stay quiet about it, or feel unsettled without knowing why. Direct [supernatural] events are rare and carry weight — they should feel significant, not casual. The boundary between mundane and hidden is more permeable near old places, during certain times, and for people who know how to look. The world does not explain itself.

Adapt the bracketed terms to the setting. If the setting has no supernatural element, replace with equivalent guidance on whatever its concealed layer is — mystery, historical truth, institutional corruption, etc.

### Seasonal tone (if applicable)

Brief guidance on each time period's emotional tone. The same event at different points in the year should feel different.

Example for a four-season setting:
> Spring: possibility, new starts, something stirring. Summer: abundance, heat, restlessness, the world at full volume. Autumn: harvest and melancholy together; things ending, things becoming clear. Winter: stillness, withdrawal, honesty that comes with the dark.

Adapt to the setting's actual time structure. If the setting uses a different rhythm — tides, academic terms, festival calendar — substitute that.

### Pacing and scene structure

Guard against escalation addiction and unnatural day rhythm. Before writing this section, check the calendar events for a **Scene Structure Notes** section — any setting-specific day-structure needs noted there should be incorporated here.

> Not every scene needs to advance a plot or deepen a relationship. Quiet moments — ordinary routines, passing conversation, small domestic beats — are the foundation that makes eventful scenes meaningful. A given day should have at most one emotionally significant beat under normal circumstances. Multiple significant beats in a single day should feel exceptional. Follow the player's lead when they push toward depth, but let the following scene settle before introducing new material.

**Time-of-day rhythms:** Specify who is naturally awake, active, and social at what point in the day, and include brief guidance on transitions between day segments (Morning / Afternoon / Evening / Night). A brief transition acknowledgment grounds the scene change without consuming the scene itself.

### NPC relationships (year 2+ guidance)

After the first full year, if characters with strong chemistry have not moved toward formal romantic or close-friendship commitment, the engine should let that natural pull become more visible. Do not force outcomes — let the existing dynamic mature without manufactured escalation.

---

## Common Failure Modes

**The engine escalates too fast.** Romance pacing and dark themes guidance are the primary fixes. If the problem persists after first drafting, strengthen the explicit language in those sections.

**Scenes feel samey.** The pacing section must explicitly say quiet scenes are valid and desirable — not every scene needs to be emotionally meaningful. If this isn't said, the engine treats every scene as an opportunity for significance.

**Dark content feels gratuitous.** "Handle with care and weight, not for shock value" combined with "the player is a witness, not a savior" addresses the most common failures.

**Characters collapse into positivity.** This is a character note problem, not a story direction problem — see `worldbuilder-character`, particularly the Relationship Behavior section and the negative-track character guidance in `worldbuilder-world-planning`.

---

## World Knowledge from Story Direction Work

Story direction work regularly surfaces world knowledge that belongs in `notes/` notes rather than the direction brief — historical context implied by the opening arc, background on the hidden layer that shouldn't be in the standing brief, lore that shapes pacing guidance but reads as exposition if left in this document.

When this happens, create a concept note immediately. Use `worldbuilder-concept` for layer classification and writing guidance. Do not leave world knowledge embedded in the story notes — it will either bloat the brief or be invisible to the export layer's lorebook packaging.
