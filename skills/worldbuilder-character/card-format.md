# Card Format Definition

*Reference document for `worldbuilder-character`. Defines the block model, entry structure, and section-scoped writing rules for character cards.*

---

## Core block

Three sections organized by information type. Every character card has all three.

### Background

Facts and formative events. What is true about the character. No behavioral framing.

**Entry format:** Fact pairs. A formative fact and what it made true.

**Target range:** 4-8 entries.

**Example entries:**
- Grew up working-class in a trade city, left at 18 → never returned to the neighborhood, never explained why
- Trained as a scribe for 6 years → can read legal documents but has never written one for pay

### Body

Physical presence and habits. What you see and experience physically.

**Entry format:** One stageable sentence per entry. Describes physical behavior that can be observed.

**Target range:** 3-5 entries. Thin Body sections are acceptable when nothing about the character's physicality is distinctive. Do not force entries.

**Example entries:**
- When she enters a room she does not know, she finds a wall or corner first. She grew up visible in ways she did not choose, and learned to make herself an observer before becoming a subject.
- He talks with his hands when he is confident and folds his arms when he is not.

### Soul

Psychological and social behavior. How they think, feel, and act.

**Entry format:** Prose sentences following the When/Behavior/Because structure embedded naturally. The formula is a construction guide, not a labeling scheme.

> When [trigger], they [behavior], because [underlying reason].

**Target range:** 5-8 entries.

**Example entries:**
- When challenged, she responds with certainty, treating doubt as a personal insult rather than a reasonable position, because the last time she showed uncertainty, someone took her job.
- When someone is struggling, he drops everything to help, partly because he cares, partly because being needed is the only time he feels valuable.

---

## Depth-of-access grid

A 3x3 grid crossing the three information-type rows with a depth-of-access progression. This is a Q&A coverage tool, not a document structure. Entries land in flat sections (Background, Body, Soul). The Q&A process uses the grid to guide question order, and a coverage check flags under-represented columns. The grid maps to how roleplay unfolds over time: column 1 early, column 2 as the relationship develops, column 3 in moments of depth.

| | Immediate | Over time | Hidden / foundational |
|---|---|---|---|
| **Background** | Known history, visible circumstances | Things they let slip, stories that emerge | Formative wound, what they never tell |
| **Body** | Surface features, first impression, obvious mannerisms | Subtle habits noticed with familiarity | Hidden under clothes. Scars, marks, physical tells |
| **Soul** | Social persona, default behavior with strangers | True self that emerges with trust | Motivational engine. Core want, fear, false belief, value-conflict stance |

---

## Required doctrine entries

A card is not finalized until all of the following are present or the user explicitly waives specific entries with a recorded reason.

1. **Core want** (behavioral, Soul). How the want shows in action, not a label. Provenance: Character Builder v3's Core slot; community consensus on motivational engine.

2. **Core fear** (behavioral, Soul). What the character does when the feared outcome approaches. Observable action, not internal dread. Provenance: same as core want; fear and desire form the motivational axis.

3. **False belief the character acts on** (Soul). A belief held wrongly and acted on with confidence. The belief and the resulting behavior must both be specific. Provenance: Character Builder v3; described as "a scene generator" in the Hoplight review.

4. **Value-conflict stance** (Soul). Which way they go when values collide with morality, the lever that tips them, how guilt manifests. Provenance: Character Builder v3; graduated in convergence retest (behavioral influence 3/4 scenarios, the only functionally validated doctrine entry).

5. **At least one unresolved tension or competing pull** (Soul). Resolved states become shortcuts models can collapse to. Provenance: community sources in causal character writing research.

6. **Values with costs** (Background or Soul). At least one top value with its stated price. A value without a cost is decoration. Provenance: Character Builder v3 via Hoplight review.

**Finalization gate:** the card is not finalized until every required entry above is present or explicitly waived.

---

## Addon blocks

### Relationships

Named dynamics with specific other characters. One entry per relationship. Relevant for cast-based worldbuilding; not needed for standalone characters. The 12-archetype framework and coverage requirements are defined in `relationships.md`.

### Intimate Dynamics

Optional. The user decides at project planning whether a character includes this block. Entries are behavioral prose in the same format as Soul (When/Behavior/Because embedded naturally). Three coverage areas with 1-2 entries each:

- Attraction expression: how they show interest
- Hesitation and limits: what makes them slow down or hold a boundary
- Specific dynamic (if applicable): behavioral signature and the emotional need it serves

Mandatory friction point: one internal contradiction in intimate behavior. Full reference in `intimate.md`.

### Voice / Dialogue

Recommended when the character will be exported to platforms that support example dialogue or when voice distinctiveness matters for the project. 2-4 composite dialogue snippets, each showing the character pulling from multiple Core areas at the same time.

**Situation categories** (the user picks 2-4 relevant to their character):
- Casual / social
- Conflict / pressure
- Vulnerability / intimacy
- Authority / power dynamic
- Alone / internal

Each snippet includes enough scene context to establish the situation. The working sheet notes which Core areas each example exercises as a coverage sanity check. Include this block when voice distinctiveness matters for the project or when the target platform supports example dialogue.

---

## Section-scoped writing rules

These are overridable defaults. The user can override any rule for their project.

### Background entries

Background is factual, not behavioral. The following rules apply:
- **Orwell co-anchor:** shortest word, active voice, cut waste
- **No meta-vocabulary** from the builder abstraction layer

The staging test, action-line convention, and fact-to-manifestation transformation do not apply to Background. Background states what is true; other sections handle how that truth manifests as behavior.

### Body and Soul entries

Body and Soul are behavioral. The following rules apply:
- **Action-line convention:** present tense, only what can be seen or heard in a scene
- **Staging test:** "Can a director stage this?" The Because clause in Soul entries is exempt. It may name an internal state if the state is specific.
- **Trait-word ban:** no adjective labels. Behavior earns the word. Replace the label with what happens that makes people reach for it.
- **Orwell co-anchor:** shortest word, active voice, cut waste
- **Fact-to-manifestation:** reproduce semantic content from the user's answer, never reproduce the phrasing. The input is the fact; the output is the staged behavior the fact produces.

For the full writing doctrine, see `../writing-style.md`.

---

## Working document conventions

Entries accumulate under section headings as bullet points. The document may carry optional annotations (grid position, coverage area) during creation; export strips these. Annotations are a working aid, not part of the card's final content.
