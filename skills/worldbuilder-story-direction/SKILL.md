---
name: worldbuilder-story-direction
description: Use when writing the opening arc or standing creative brief for an AI-powered narrative game. Also use when LLM output escalates too fast, when romantic or dramatic intensity feels unearned, when dark content is handled carelessly, or when scenes lack pacing variation.
---

# Story Direction

## Overview

The story direction is the LLM's standing creative brief. It doesn't describe events — it shapes the engine's approach to generating them. Two documents serve this function:

**Opening Story Arc:** The initial situation that draws the player in. The only thing approaching a scripted beginning. Sets the stage without constraining it.

**Ongoing Story Direction:** Persistent creative instructions the engine follows throughout the game. The primary guard rail against the LLM's default tendencies — escalation, flattening, repetition, and inappropriate intimacy pacing.

---

## Opening Story Arc

### What it is

A brief description of the initial situation: what is happening in the setting when the player arrives, what tension or possibility is visible, who the player might immediately encounter. Evocative, not prescribed.

### What it is not

A plot outline. A sequence of events. A list of story beats. The opening arc establishes a stage; player choices and LLM variance will push everything off any scripted path immediately. Design for evocation, not control.

### What to cover

- The setting's visible state when the player arrives
- The immediate invitation for engagement — a job, a problem, a mystery, an encounter
- The tone of the first few scenes
- What the player's arrival means to the community

---

## Ongoing Story Direction

### Author framing

Position the LLM as a skilled author giving voice to characters, not an entity that becomes them. Author-capture — losing narrative perspective, mirroring the player's mood regardless of whether that serves the story, abandoning a character's established behavioral register — is the root failure mode for most output quality problems.

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

Brief guidance on each time period's emotional register. The same event at different points in the year should feel different.

Example for a four-season setting:
> Spring: possibility, new starts, something stirring. Summer: abundance, heat, restlessness, the world at full volume. Autumn: harvest and melancholy together; things ending, things becoming clear. Winter: stillness, interiority, honesty that comes with the dark.

Adapt to the setting's actual time structure. If the setting uses a different rhythm — tides, academic terms, festival calendar — substitute that.

### Pacing and scene structure

Guard against escalation addiction and unnatural day rhythm. Before writing this section, check `calendar.md` for a **Scene Structure Notes** section — any setting-specific day-structure needs noted there should be incorporated here.

> Not every scene needs to advance a plot or deepen a relationship. Quiet moments — ordinary routines, passing conversation, small domestic beats — are the foundation that makes eventful scenes meaningful. A given day should have at most one emotionally significant beat under normal circumstances. Multiple significant beats in a single day should feel exceptional. Follow the player's lead when they push toward depth, but let the following scene settle before introducing new material.

**Time-of-day rhythms:** Specify who is naturally awake, active, and social at what point in the day, and include brief guidance on transitions between day segments (Morning / Afternoon / Evening / Night). A brief transition acknowledgment grounds the scene change without consuming the scene itself.

### NPC relationships (year 2+ guidance)

After the first full year, if characters with strong chemistry have not moved toward formal romantic or close-friendship commitment, the engine should let that natural pull become more visible. Do not force outcomes — let the existing dynamic mature without manufactured escalation.

---

## Common Failure Modes

**The engine escalates too fast.** Romance pacing and dark themes guidance are the primary fixes. If the problem persists after first drafting, strengthen the explicit language in those sections.

**Scenes feel samey.** The pacing section must explicitly say quiet scenes are valid and desirable — not every scene needs to be emotionally meaningful. If this isn't said, the engine treats every scene as an opportunity for significance.

**Dark content feels gratuitous.** "Handle with care and weight, not for shock value" combined with "the player is a witness, not a savior" addresses the most common failures.

**Characters collapse into positivity.** This is a character card problem, not a story direction problem — see `worldbuilder-character-blueprint`, particularly the influence thresholds section and the negative-track character guidance in `worldbuilder-world-planning`.

---

## Lorebook Candidates

End `story.md` with a `## Lorebook Candidates` section. Collect here any world-building material that came up during story direction work but belongs in the lorebook rather than the story brief — historical context implied by the opening arc, background on the hidden layer that shouldn't be in the standing brief itself, lore that shapes pacing guidance but reads as exposition if left in this document.

Format: one entry per candidate, with the lore layer it belongs to (surface, mid, or deep) and a one-sentence note on what it is and why it was cut.

This section may be empty. An empty section is a valid outcome. The `worldbuilder-lorebook` review pass collects from this section along with candidates from blueprints and calendar.
