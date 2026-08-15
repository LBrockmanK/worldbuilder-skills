---
type: spec
title: Card Format Amendments — Body Appearance Preamble and Story Beats Addon
description: 'Two amendments to card-format.md: (1) a prose preamble in Body for static
  appearance, exempt from the staging test; (2) a Story Beats addon block for triggerable
  narrative scenarios with labeled prose entries.'
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T17:11Z
resources: []
---

# Card Format Amendments — Body Appearance Preamble and Story Beats Addon

## Context

The [character card architecture spec](2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md)
defines the block model for character cards: Core block (Background,
Body, Soul) plus addon blocks (Relationships, Intimate Dynamics,
Voice/Dialogue). During a source-ingestion test case using Fields of
Mistria game assets, two layout gaps surfaced.

**Body has no home for static appearance.** Body's entry format
requires "one stageable sentence per entry" describing "physical
behavior that can be observed." Physical appearance — hair color, eye
color, skin tone, build, clothing — is observable but not behavioral.
Background is factual but covers history and circumstances, not
physical properties. The result: appearance entries land in Body
violating the staging test, or in Background blurring the
information-type boundary.

**No section for triggerable narrative scenarios.** Heart events,
story events, and progression-gated encounters are valuable
character material that maps to platform features (ainime future
storylines, SillyTavern alternate greetings) but has no place in the
card format. Voice/Dialogue covers speech patterns across situations;
calendar events cover recurring schedule items. Story Beats — one-time
or progression-gated narrative moments — fall between the two.

## Decisions

### D1. Body Appearance Preamble

Add an appearance preamble to the Body section. Body opens with
short descriptive prose covering the character's static physical
appearance, followed by the existing behavioral entries as bullet
points.

**Preamble rules:**
- Short descriptive prose (sentences or descriptive clauses),
  not bulleted entries
- Exempt from the staging test (appearance is observable but not
  stageable as an action)
- Orwell co-anchor applies (shortest word, active voice, cut waste)
- Trait-word ban applies (no "beautiful," "imposing" — describe what
  is seen)
- No meta-vocabulary from the builder abstraction layer

**What goes in the preamble:** hair, eyes, skin, build, distinguishing
physical features, default or seasonal clothing, and hidden static
features (scars, marks, tattoos) when relevant. Everything about
what this person looks like — regardless of depth-of-access. A scar
hidden under clothing is still static appearance and belongs in the
preamble, not as a behavioral entry.

**What stays as entries:** physical mannerisms, posture habits, how
they move or carry themselves — anything that passes the staging test.

**Example:**

> Pink wavy hair past her shoulders, a bow on top that stays across
> every outfit. Purple eyes, brown skin. In spring she wears a
> magenta bodice over white puffed sleeves with a dark navy skirt
> embroidered in flowers — the outfit changes with the season.
>
> - When she is caught off guard emotionally, a blush rises before
>   she can redirect the conversation.

**Q&A workflow change:** during the Body section, ask about appearance
first (preamble), then physical mannerisms (entries). The preamble
covers static appearance at all depths (surface and hidden); the
depth-of-access grid's Body row guides behavioral entries only.

**Working-document convention:** the preamble is prose before the
first bullet point — a recognized exception to the all-bullets
convention. Export strips any working annotations but preserves the
preamble as section-opening prose.

### D2. Story Beats Addon Block

Add Story Beats as an addon block. It is included when the character
has triggerable narrative scenarios worth specifying — not required
for every character.

**Session opening:** recommend Story Beats when the character has
progression-gated events (relationship milestones, story
involvement), when the target platform supports future storylines or
alternate greetings, or when the source material provides rich
scenario data. The user decides.

**Boundary with story notes:** the existing SKILL.md says story
possibilities live in separate story notes with intention scope. Story
Beats do not replace story notes. A Story Beat is a character-local
scenario sketch — a hook, short enough to live inside the character
card. A story note is a full narrative document with arc structure,
scope, and its own lifecycle. Story Beats may reference story notes
for arcs they participate in. The boundary: if the scenario needs
more than 2-4 sentences of prose to describe, it belongs in a story
note, not a Story Beat.

**Entry format: labeled prose blocks.** Each entry has:
- A short title (descriptive label for working reference)
- A trigger/condition note (what relationship state, story progress,
  or situation makes this scenario available)
- 2-4 sentences of scenario prose describing: the setup (where and
  when), the key action or exchange, and what it reveals about the
  character

**Writing rules:**
- Prose follows the action-line convention (present tense, observable)
- Staging test applies to the scenario description
- Orwell co-anchor applies
- Condition notes are factual, not prose-styled
- No meta-vocabulary

**Target range:** 3-8 entries. The range reflects the character's
narrative complexity: a supporting character might have 3 beats, a
romance-track protagonist might have 8.

**Distinction from other sections:**
- Story Beats vs. Voice/Dialogue: Voice/Dialogue shows how the
  character speaks across situations (speech pattern, register).
  Story Beats describe specific events that could unfold (narrative
  content, plot progression).
- Story Beats vs. calendar events: calendar events are recurring
  scheduled occurrences (festivals, weekly gatherings). Story Beats
  are one-time or progression-gated narrative moments. A dated
  one-time event with character-specific narrative content (e.g. a
  festival date at a relationship milestone) is a Story Beat that
  references the calendar context; the calendar entry records the
  date, the Story Beat carries the narrative.
- Story Beats vs. story notes: Story Beats are hooks inside the
  character card; story notes are full arc documents outside it.

**Export mapping:**
- ainime: Story Beat entries are transformed to possibility-style
  framing for the future storylines section. The card stores the
  scenario as a definite description; the export adapts it to the
  engine's possibility voice (e.g. "Adeline might invite the player
  to a working session...").
- SillyTavern: Story Beat scenario prose maps to alternate greetings.
  Trigger conditions that cannot be mechanically enforced are
  degraded to narrative framing within the greeting text (e.g. "After
  months of working together on Mistria's recovery..." establishes
  the relationship context that the platform cannot gate on).

**Working-document convention:** Story Beats are labeled prose blocks,
not bulleted entries — a recognized exception to the all-bullets
convention alongside the Body preamble. Each beat's title is bold,
its condition follows an em-dash, and the prose block follows.

**Example entries:**

> **Paperwork Party** — available at early relationship
>
> Adeline invites the player to a working session at the Manor.
> Elsie writes grant applications, Eiland processes excavation forms,
> Adeline handles tax documents. She calls triple-checking "so
> satisfying" and offers treats from the Inn to whoever finishes
> first.

> **Town Inspection Walk** — available at mid relationship
>
> Adeline takes the player on a walking tour of Mistria to check on
> everyone's needs. Landen tells her to take care of herself; she
> says she is fine and keeps walking. She admits she has been
> enjoying the company but offers the player an exit before the
> next stop.

**Q&A workflow change:** when Story Beats is selected at session
opening, work through the block after Voice/Dialogue (or after the
last selected addon block). Ask about narrative milestones, story
events, or progression-gated encounters. Work through them in
approximate narrative order.

**card-format.md placement:** after Voice/Dialogue in the addon
blocks section.

## Consequences

- Body section in card-format.md gains a preamble definition before
  the entry format specification
- card-format.md working-document conventions section gains a note
  acknowledging the Body preamble and Story Beats labeled prose as
  exceptions to the all-bullets convention
- The addon blocks list grows from three (Relationships, Intimate
  Dynamics, Voice/Dialogue) to four (adding Story Beats)
- The worldbuilder-character SKILL.md session flow gains a Story
  Beats step after Voice/Dialogue
- The SKILL.md session opening gains a Story Beats addon decision
- The SKILL.md completion checklist parenthetical must add Story
  Beats to the enumerated addon blocks
- The SKILL.md Story Notes section must acknowledge the Story Beats
  boundary (hooks in the card vs. full arcs in story notes)
- `defaults/templates/character.md` must add a Body preamble
  placeholder and a Story Beats heading; `defaults/okf.json` must
  be regenerated from the updated template
- Export mapping documentation (extraction-reliability-map.md) needs
  entries for the new block's platform fields
- `skills/worldbuilder-ainime-export/SKILL.md` and
  `skills/worldbuilder-ainime-export/card-assembly.md` must be
  updated to consume the Body preamble and Story Beats block for
  their respective platform fields

## Notes (non-normative)

This spec was surfaced by a source-ingestion test case (Fields of
Mistria, character: Adeline). The test demonstrated that game assets
produce rich appearance data (portraits) and rich scenario data
(heart events, story events) that had no card-format home. Both
amendments address layout gaps revealed by practical use, not
theoretical design.
