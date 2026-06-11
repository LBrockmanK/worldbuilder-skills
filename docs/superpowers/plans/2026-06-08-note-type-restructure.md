# Note Type Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite all five non-character note type skills under the Design Notes / Facts / Function framework, adding `brief` to frontmatter universally.

**Architecture:** Each note type gets the same three-body-section structure: Design Notes (builder context, excluded from exports), a Facts section (declarative information about the thing in the world), and a Function section (what the thing does to scenes and characters). A `brief` frontmatter field replaces in-body preambles and the trigger-context field. Section names vary per type. Tasks are fully independent — execute in parallel.

**Design spec:** The design was worked out in session. The shared framework is:

| Type | Facts section name | Function section name |
|---|---|---|
| Location | Form & History | Presence |
| Faction | Origin & Structure | Collective Behavior |
| Concept | Lore | Implications |
| Event | What Happens | Scene Effects |
| Story (arc/intention/intro) | Situation | Story Possibilities |

**`brief` field (all types):**
- Plain prose, ~1-2 sentences, written last after the full note is complete
- Purpose: cast/world navigation — other agents scan `brief` fields to understand a note without opening it
- Same frontmatter position as in character notes
- No recommendations, no design rationale (that goes in Design Notes)

**Design Notes section (all types):**
- Builder record — excluded from all exports
- Contains: narrative purpose/function, inspirations (real or fictional references), design decisions, open questions
- Written at creation time, updated during the session
- An agent working on the world at runtime should not act on Design Notes content

---

## Task 1: Rewrite worldbuilder-location/SKILL.md

**Files:**
- Read: `skills/worldbuilder-location/SKILL.md` (current)
- Modify: `skills/worldbuilder-location/SKILL.md`

- [ ] **Step 1: Read the current file**

Read `skills/worldbuilder-location/SKILL.md` in full before writing anything.

- [ ] **Step 2: Update frontmatter spec**

Add `brief` to the frontmatter block. The field goes after `primary-characters`. Mark it as plain prose, written last.

Remove the Preamble section from the note body structure — its purpose moves to `brief`.

Updated frontmatter block:
```yaml
type: location
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
region: "[[The Valley]]"           # link to region note
function: one phrase (plain text)
primary-characters: ["[[Name]]"]   # links to character notes
brief: |                           # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

- [ ] **Step 3: Write the Brief section**

Add a `## Brief` section after frontmatter. Content:

Brief is the world navigation field. When an agent is writing character relationships, planning story arcs, or building export content, they scan `brief` across location notes to understand each place without opening the note.

Content: what this place is, what makes it distinctive, what role it plays in the setting's social and narrative life. One or two sentences. Not a physical description — that goes in Form & History.

Written last — after the full note is complete. Example: "The old mill: closed for fifteen years, still visited by people who need to be alone with guilt. The town's primary location of unresolved history."

Length: 1–2 sentences. No design rationale, no recommendations.

- [ ] **Step 4: Write the Design Notes section**

Add a `## Design Notes` section. Mark it as excluded from exports. Content requirements:

**What to include:**
- Narrative function: what does this location uniquely contribute that no other location does?
- Intended scene types: what kinds of scenes can only happen here? What does a player gain access to by coming here?
- Inspirations: real or fictional places, what specifically was drawn from each
- Design decisions: choices made that would be confusing without context
- Open questions: unresolved decisions to revisit

**Format:** Bullet points under plain sub-headers. Leave blank if nothing warrants capturing — do not pad.

**Excluded from exports:** Agent-context only. The export skill and runtime story engine do not read this section.

- [ ] **Step 5: Write the Form & History section (Facts)**

This combines the current Physical Form and History & Meaning sections into one section. Rename to `## Form & History`.

Content from Physical Form:
- 1–3 sentences: scale, age, condition, environment, one vivid specific detail
- Not a floor plan — the engine needs to know what kind of place this is, not where the furniture is

Content from History & Meaning:
- Why this place exists
- What it carries from the past
- What it implies about the world
- Secrets if it has them

Keep the existing push-back test note: a location with no reason to exist generates no scenes worth setting there.

If the location is the subject of concept notes at different layers, link to them rather than duplicating their content.

- [ ] **Step 6: Write the Presence section (Function)**

This combines the current Social Life and Behavioral Register sections into one section. Rename to `## Presence`.

Preserve all content from both sections:

From Social Life:
- Who comes here, why, what they want, what tensions exist between different visitor types
- Written as who-does-what, not who-is-there
- Example showing three visitor types with tensions

From Behavioral Register:
- How the place reads across time (day/night, busy/quiet, seasonal rhythm), observer (insider vs stranger), circumstances (normal vs disrupted)
- Not all axes apply — cover only those that produce different scene logic
- The push-back test: does this place DO something to characters, or only describe what's there?
- Failing example vs passing example

- [ ] **Step 7: Update the note structure table**

Update the section table at the top of the file to reflect the new sections:

```
| Section | Notes |
|---|---|
| Frontmatter | YAML; see below |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| Form & History | Physical reality and what the place carries |
| Presence | Who comes here and how the place behaves |
```

Remove the Preamble row.

- [ ] **Step 8: Update Key Principles**

The "Write plainly. No flair." principle is already present. Keep it.

Remove the Preamble-related principle if any exists.

Add: "Design Notes are builder context. Do not include narrative purpose or creative intent in the note body sections — that goes in Design Notes."

- [ ] **Step 9: Update the self-check**

Remove the Preamble checklist block entirely.

Add a Brief checklist block:
```
**Brief**
- [ ] Written last — after the full note is complete
- [ ] 1–2 sentences; describes what makes this location distinctive, not its physical form
- [ ] No design rationale, no export recommendations
```

Add a Design Notes checklist block:
```
**Design Notes**
- [ ] Narrative function stated
- [ ] Intended scene types named
- [ ] Not padded — blank is acceptable if nothing warrants capturing
```

Rename existing checklist sections to match new section names:
- Physical Form → Form & History
- Social Life → (keep in Presence block)
- Behavioral Register → (keep in Presence block)
- History & Meaning → (absorbed into Form & History block)

- [ ] **Step 10: Verify against spec**

- [ ] `brief` field in frontmatter with description and "written last" instruction
- [ ] Preamble removed from body and from self-check
- [ ] Design Notes section present, marked excluded from exports, has correct content requirements
- [ ] Form & History covers all Physical Form + History & Meaning content
- [ ] Presence covers all Social Life + Behavioral Register content including both examples and the push-back test
- [ ] Section table updated
- [ ] Self-check updated for all new section names
- [ ] No uses of "register" in the communication sense
- [ ] Writing style: plain, no flair

- [ ] **Step 11: Commit**

```
git add skills/worldbuilder-location/SKILL.md
git commit -m "feat: restructure location note under Design Notes / Form & History / Presence framework"
```

---

## Task 2: Rewrite worldbuilder-faction/SKILL.md

**Files:**
- Read: `skills/worldbuilder-faction/SKILL.md` (current)
- Modify: `skills/worldbuilder-faction/SKILL.md`

- [ ] **Step 1: Read the current file**

Read `skills/worldbuilder-faction/SKILL.md` in full before writing anything.

- [ ] **Step 2: Update frontmatter spec**

Add `brief` after `function`. Remove Preamble from body structure.

```yaml
type: faction
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
members: ["[[Name]]"]   # links to character notes
function: one phrase (plain text)
brief: |                # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

- [ ] **Step 3: Write the Brief section**

Brief is the world navigation field for factions. Content: what this group is, what it does to scenes, what a player can expect from any member they encounter.

Example: "The Silt Brotherhood: controls river trade and treats pricing information as proprietary — any member in a scene will deflect direct questions about costs and find a reason to leave before being pressed further."

Written last. 1–2 sentences. Behavioral, not descriptive.

- [ ] **Step 4: Write the Design Notes section**

Rename the current `## Concept` section to `## Design Notes`. Mark as excluded from exports.

Content requirements:
- Narrative engine: what conflicts does this faction generate that no other faction could? What role does it fill uniquely?
- Inspirations: real organizations or fictional factions, what was drawn from each
- Design decisions and constraints
- Open questions

The current Concept section asks "what does it DO to the story?" — that question moves here. Keep that framing.

- [ ] **Step 5: Write the Origin & Structure section (Facts)**

Combine the current Origin & Purpose and Membership sections into `## Origin & Structure`.

From Origin & Purpose:
- Founding: how the faction came to exist and its original purpose
- Current holdings: specific resources, territory, monopoly, information, obligations — "has influence" is not a holding
- Active goals: what the faction is trying to achieve right now — specific and active, not "seeks power"

From Membership:
- Ranks or tiers if they exist
- How membership is acquired and lost
- Ambiguity cases: former members, dual loyalties, contested membership, outsiders who function as members

Keep the existing note: "Seeks to grow its power and influence" is not a goal.

- [ ] **Step 6: Write the Collective Behavior section (Function)**

This section stays largely as-is but is now explicitly labeled as the Function section. Rename from `## Collective Behavior` — or keep the name since it's meaningful and the function label is structural not visible.

Preserve all current content:
- Phrasing rule: instructional, not descriptive
- Failing/passing examples
- Shared behavioral tendencies (When/Behavior/Because, 3–5 entries)
- The collective mask (Demeanor)
- The variation layer (Nature)
- Inter-faction web (direct relationships only)

Remove the `## Storylines` section entirely. Story possibilities for factions become story notes with `characters:` or faction references — same as characters.

- [ ] **Step 7: Update the note structure table**

```
| Section | Notes |
|---|---|
| Frontmatter | YAML; see below |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| Origin & Structure | Founding, holdings, membership |
| Collective Behavior | Active goals, behavioral entries, mask, variation, inter-faction |
```

- [ ] **Step 8: Update Key Principles**

Keep "Write plainly. No flair." and "Make decisions, don't hedge." and "Instructional phrasing is not optional."

Add: "Storylines belong in story notes, not faction notes. If a story possibility is anchored by this faction's existence, create a story note."

Remove any Preamble-related principles.

- [ ] **Step 9: Update the self-check**

Remove Preamble and Concept checklist blocks.

Add:
```
**Brief**
- [ ] Written last
- [ ] 1–2 sentences; behavioral — describes what a player encounters with any member, not what the faction is in the abstract

**Design Notes**
- [ ] Narrative engine stated
- [ ] Not padded
```

Rename Origin & Purpose → Origin & Structure in the checklist. Add membership items to that block if they were in a separate Membership block.

Remove Storylines checklist block.

- [ ] **Step 10: Verify against spec**

- [ ] `brief` in frontmatter, written last
- [ ] Preamble removed from body
- [ ] Design Notes replaces Concept, marked excluded from exports
- [ ] Origin & Structure covers founding, holdings, membership, active goals
- [ ] Collective Behavior covers all existing content plus inter-faction web
- [ ] Storylines removed
- [ ] Self-check updated
- [ ] Writing style clean

- [ ] **Step 11: Commit**

```
git add skills/worldbuilder-faction/SKILL.md
git commit -m "feat: restructure faction note under Design Notes / Origin & Structure / Collective Behavior framework"
```

---

## Task 3: Rewrite worldbuilder-concept/SKILL.md

**Files:**
- Read: `skills/worldbuilder-concept/SKILL.md` (current)
- Modify: `skills/worldbuilder-concept/SKILL.md`

- [ ] **Step 1: Read the current file**

Read `skills/worldbuilder-concept/SKILL.md` in full before writing anything.

- [ ] **Step 2: Update frontmatter spec**

Remove `trigger-context` from frontmatter. Add `brief`. The `trigger-context` content moves into the Implications section body.

```yaml
type: concept
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
layer: "[[surface]]" | "[[mid]]" | "[[deep]]"
brief: |    # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

- [ ] **Step 3: Write the Brief section**

Brief is the world navigation field for concept notes. Content: what this piece of world knowledge is and when it matters.

Example: "The founding flood: the real cause of the Harrow family's departure — the surface story omits that the flood was foreseeable and the warning was ignored. Relevant whenever the Harrow family, the mill, or the town's founding comes up."

Written last. 1–2 sentences. Richer than the old `trigger-context` one-phrase.

- [ ] **Step 4: Write the Design Notes section**

This is a new section. Content requirements:

- Narrative purpose: what does the existence of this thing make impossible, costly, or inevitable in any scene that touches it? (This question previously appeared as a standalone block — move it here.)
- Why this is its own note rather than embedded in a character or location note
- Layer classification rationale: why surface vs. mid vs. deep
- Open questions

Mark as excluded from exports.

- [ ] **Step 5: Write the Lore section (Facts)**

This is the main content section. Rename from whatever the current body content is called (currently it flows unlabelled under the three-layer structure guidance).

Content: what is true about this thing in the world. Written at the appropriate layer register:
- Surface: matter-of-fact, no mysticism
- Mid: uncertain, hedged — "they say..." — people half-believe
- Deep: confirmed and weighted

For notes with an iceberg split, include Believed / True sub-sections within Lore. Keep the existing iceberg split guidance (when to use it, format).

Preserve the three-layer structure section as guidance for how to write Lore content at each layer. Keep the tone guidance per layer.

- [ ] **Step 6: Write the Implications section (Function)**

This replaces the Limitations and Costs block and absorbs the trigger-context purpose.

Content requirements:

**What this section covers:**
- What follows from this thing being true: behavioral norms, social structures, economic consequences, tensions
- What people do differently because this thing exists
- Costs and limitations: what the thing cannot do, what it demands, what makes it fail
- Activation context: when this lore becomes relevant — the situations and phrasings that trigger it (replaces trigger-context)

**The key question:** What would a scene look like differently because this thing exists? If the answer is "nothing specific," the Implications section is too thin.

**Required for rule-bearing concepts:** Notes covering magic systems, institutions, cultural practices, belief systems, or anything with internal logic must include explicit costs and limits. A concept documented only by what it can do cannot constrain a scene. Keep this requirement and the healing magic example from the current file.

Keep the alias writing guidance section — it's still needed and belongs after Implications.

- [ ] **Step 7: Remove the Recurring World Events section**

This section moves to the new worldbuilder-event skill. Replace with a one-line pointer:

> "Event notes — festivals, seasonal observances, recurring world events — have their own skill: `worldbuilder-event`. Use that skill for any recurring or calendar event."

- [ ] **Step 8: Update the note structure table or add one**

Add a structure table near the top:
```
| Section | Notes |
|---|---|
| Frontmatter | YAML; see below |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| Lore | What is true about this thing in the world |
| Implications | What follows from this being true; activation context |
```

- [ ] **Step 9: Update the self-check**

Remove trigger-context from frontmatter check. Add `brief` and `layer` as required frontmatter fields.

Add:
```
**Brief**
- [ ] Written last
- [ ] 1–2 sentences; covers what this knowledge is and when it matters

**Design Notes**
- [ ] Narrative purpose stated (what does this make impossible, costly, or inevitable?)
- [ ] Layer rationale present
```

Update Lore/Implications checks:
```
**Lore**
- [ ] Content written at the correct layer register
- [ ] Iceberg split present if belief/truth gap is narratively live

**Implications**
- [ ] Covers behavioral and social consequences, not just restrictions
- [ ] Costs and limits present for rule-bearing concepts
- [ ] Activation context stated
```

- [ ] **Step 10: Verify against spec**

- [ ] `trigger-context` removed from frontmatter; `brief` added
- [ ] Brief section present, written last instruction included
- [ ] Design Notes present, marked excluded from exports, contains narrative purpose block
- [ ] Lore section covers factual content with layer-register guidance
- [ ] Implications covers behavioral consequences + costs + activation context
- [ ] Recurring World Events section removed; pointer to worldbuilder-event added
- [ ] Alias writing guidance preserved
- [ ] Self-check updated

- [ ] **Step 11: Commit**

```
git add skills/worldbuilder-concept/SKILL.md
git commit -m "feat: restructure concept note under Design Notes / Lore / Implications framework; remove event guidance to worldbuilder-event"
```

---

## Task 4: Create worldbuilder-event/SKILL.md

**Files:**
- Create: `skills/worldbuilder-event/SKILL.md`
- Modify: `skills/worldbuilder-world-planning/SKILL.md` (add worldbuilder-event reference)

This is a new skill file. Event notes currently have almost no body guidance — they're described in worldbuilder-concept's "Recurring World Events" section. This task gives them a full skill with the Design Notes / What Happens / Scene Effects structure.

- [ ] **Step 1: Read reference material**

Read the following before writing:
- `skills/worldbuilder-concept/SKILL.md` — find the "Recurring World Events" section for content to preserve
- `skills/worldbuilder-ainime-export/SKILL.md` — find how event notes are exported (`storyTriggers`, `calendarConfig`)
- `skills/worldbuilder-ainime-export/calendar.md` — understand the calendar/festival structure
- `skills/worldbuilder-world-planning/SKILL.md` — understand where events fit in the phase structure

- [ ] **Step 2: Write the skill file**

Create `skills/worldbuilder-event/SKILL.md` with the following structure:

**Frontmatter block:**
```yaml
---
name: worldbuilder-event
description: Use when creating or deepening an event note for an AI-powered narrative game — festivals, seasonal observances, calendar events, cultural rituals, historical commemorations, or any recurring world event. Also use when an event note feels thin, generic, or is failing to generate distinctive scene behavior.
---
```

**Overview section:**
An event note is not a schedule entry — it is a behavioral specification for a day. The export skill handles calendar mapping and storyTrigger packaging; this skill covers writing event notes that do real work: making any scene set on this day feel different from any other day.

**Working with Vault Files:** (standard renaming note — same as other skills)

**Frontmatter spec:**
```yaml
type: event
status: draft | complete
aliases: []           # every realistic way this event is mentioned in dialogue
last_updated: YYYY-MM-DD HH:mm
date: "[[Spring-08]]"    # link; clusters events by day
recurring: true | false
characters: ["[[Name]]"]   # characters central to this event
location: "[[Location Name]]"   # primary location if fixed
brief: |              # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

`aliases` functions the same as in concept notes — the export skill derives keyword triggers from it. Include every realistic phrasing: "the festival," "harvest time," "the long night."

**Brief section:**
Brief is the world navigation field. Content: what this event is and what it does to the community. Written last.

Example: "The Spring Harvest Festival: the one day the town's usual distances relax — introductions that normally take weeks happen naturally, and the player meets the community as a whole for the first time."

1–2 sentences. Behavioral — what the event does, not what it is.

**Note structure table:**
```
| Section | Notes |
|---|---|
| Frontmatter | YAML; see above |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| What Happens | Factual description of the event |
| Scene Effects | What the event does to scenes and social dynamics |
```

**Design Notes section:**
Builder record. Excluded from exports.

Content:
- What this event contributes that no other event does — what makes it distinctive?
- Inspirations: real festivals, cultural observances, fictional events, what was drawn
- Narrative intent: what kinds of scenes does this enable?
- Open questions

**What Happens section (Facts):**
Factual description of the event.

Cover:
- Timing: season, rough calendar position (exact day is an export decision — write "early spring," not "day 8")
- Who participates: universal, optional, by community role or invitation
- What physically occurs: activities, rituals, traditions
- Origin: what the event commemorates or why it exists

Vague timing is fine — write for content, not calendar precision. The export skill assigns the specific day.

**Scene Effects section (Function):**
What the event does to scenes and social dynamics. This is the section that makes event notes worth having.

Cover:
- Social dynamics: what distances relax, what tensions tighten, who talks to whom that normally wouldn't
- Obligations and costs: who is expected to attend, what happens socially if someone doesn't
- Scene logic: what becomes natural on this day, what becomes unusual or impossible
- Hidden layer: how the event touches deeper world elements if relevant

**The scene test:** After writing Scene Effects, ask: if the engine generates a scene set on this day with no other context, does it feel different from any other day? If not, Scene Effects is too thin.

Failing example: "It is a day of celebration. People are happy and gather in the town square." — This could be any day. The event is invisible.

Passing example: "The usual rules about who approaches whom are suspended today. Characters who normally hold themselves apart from the player will initiate conversation. The player meets the full community for the first time, and relationships that normally require weeks of individual cultivation can begin here." — The engine has specific behavioral direction.

**Layer classification (if applicable):**
Some events carry layer classification like concept notes — a surface festival is well-known and openly celebrated; a mid-layer observance has old stories behind it; a deep-layer ritual touches the hidden layer. Apply `layer:` frontmatter if relevant. Event notes without a hidden dimension do not need layer classification.

**Lifecycle:**
Event notes can be created at any phase. Create a stub (frontmatter + brief body) as soon as an event is named. Flesh out What Happens and Scene Effects once the cast is established — seasonal scenes are richer when you know who is in them.

**Self-check:**
```
**Frontmatter**
- [ ] `aliases` covers every realistic phrasing
- [ ] `date` set as a wikilink
- [ ] `recurring` set

**Brief**
- [ ] Written last
- [ ] Behavioral — describes what the event does to the community

**Design Notes**
- [ ] Distinctive contribution stated
- [ ] Not padded

**What Happens**
- [ ] Timing stated (approximate is fine)
- [ ] Who participates stated
- [ ] Physical activities described

**Scene Effects**
- [ ] Scene test passes: a scene on this day would feel different from any other day
- [ ] At least one social dynamic specified (what relaxes or tightens)
- [ ] Obligations and costs stated if the event carries them
```

- [ ] **Step 3: Update worldbuilder-world-planning to reference the new skill**

In `skills/worldbuilder-world-planning/SKILL.md`, find the phase table row for Phase 2a (Concept notes) and update the skill column to reference both skills:

Change:
```
| 2a. Concept notes | Wide | `worldbuilder-concept` | `notes/` |
```
To:
```
| 2a. Concept & event notes | Wide | `worldbuilder-concept`, `worldbuilder-event` | `notes/` |
```

Also find any mention of event notes in the skill that currently references worldbuilder-concept for event guidance, and update to reference worldbuilder-event.

- [ ] **Step 4: Verify**

- [ ] `skills/worldbuilder-event/SKILL.md` exists and has all sections
- [ ] Frontmatter spec is complete
- [ ] Scene test stated in Scene Effects section
- [ ] Self-check present and complete
- [ ] worldbuilder-world-planning phase table updated
- [ ] Writing style clean: no slop phrases, no "register"

- [ ] **Step 5: Commit**

```
git add skills/worldbuilder-event/SKILL.md skills/worldbuilder-world-planning/SKILL.md
git commit -m "feat: create worldbuilder-event skill with Design Notes / What Happens / Scene Effects structure"
```

---

## Task 5: Rewrite worldbuilder-story/SKILL.md (arc, intention, and introduction notes)

**Files:**
- Read: `skills/worldbuilder-story/SKILL.md` (current)
- Modify: `skills/worldbuilder-story/SKILL.md`

**Scope:** Direction notes (`direction.md`) are operational instructions for the story engine — they stay as-is. The new structure applies to arc notes, intention notes, and introduction notes.

- [ ] **Step 1: Read the current file**

Read `skills/worldbuilder-story/SKILL.md` in full before writing anything.

- [ ] **Step 2: Update the frontmatter spec for arc/intention/introduction notes**

Add `brief` to the frontmatter block. Keep all existing fields.

```yaml
type: story
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
up: "[[parent-note]]"
scope: "[[arc]]" | "[[intention]]" | "[[introduction]]"
characters: ["[[Name]]"]
brief: |    # plain prose; written last — see ## Brief below
  <written after the full note is complete>
```

Note: direction notes also use `type: story` but have no `up:` field. `brief` applies to all story notes including direction.

- [ ] **Step 3: Write the Brief section**

Brief is the navigation field for story notes. Other agents scan it when planning arcs or building character notes.

For arc notes: what this story arc is and what emotional territory it covers.
Example: "The mill arc: the founding family's buried guilt surfaces; the town must decide whether to protect the story they've told themselves or face what actually happened."

For intention notes: what this story possibility is in one sentence.
Example: "The confession scene: if trust reaches a high point during the autumn festival, Mira may tell the player what she actually saw the night of the flood."

For introduction notes: who this introduces and the first impression.
Example: "Introduces Bram: the player's first encounter is him repairing something that isn't broken, because staying busy is easier than acknowledging they've arrived."

Written last. 1–2 sentences.

- [ ] **Step 4: Write the Design Notes section for arc/intention/introduction notes**

Add guidance for a Design Notes section in arc, intention, and introduction notes. This section is where the builder captures creative intent — the "Star Wars Episode 4 opening" reference belongs here.

Content requirements:
- Creative intent: what kind of story is this emotionally? What should it feel like when it plays out?
- Inspirations: specific scenes, arcs, or moments from other media being evoked; what specifically is being drawn from each
- Why this arc or moment is worth building toward — what makes it interesting
- Open questions

Mark as excluded from exports. The story engine acts on Situation and Story Possibilities; Design Notes are for the builder.

- [ ] **Step 5: Write the Situation section (Facts)**

This section establishes the state of things before any player involvement. For arc and intention notes.

Content:
- The current state of affairs in the world that makes this arc or intention possible
- Who is involved and what each party wants or fears going in
- Timing constraints or seasonal considerations if relevant
- Preconditions: what needs to be true (player trust level, prior events, season) for this arc or intention to be accessible

For introduction notes: Situation covers where and when the introduction could happen, who else is present, what the circumstances are.

- [ ] **Step 6: Write the Story Possibilities section (Function)**

This section replaces the current opening story arc and story note body content for arc and intention notes.

Content:
- What could happen and how it could develop — phrased as possibility, not script: "may," "could," "there is a possibility that"
- Key moments: the set pieces that make the arc feel real if they fire
- Resolution directions: natural ways things could go, not scripted outcomes
- Connection to other arcs or characters

For intention notes: Story Possibilities is typically shorter — one key possibility with the moment that would trigger it and the direction it could go.

For introduction notes: Story Possibilities covers how the scene plays, what the character does, what invitation it extends to the player.

Keep the existing rule: do not script outcomes. Write for robustness — arcs that remain interesting whether or not a specific beat fires.

- [ ] **Step 7: Keep direction note guidance as-is**

Direction notes are a special case. The Design Notes / Situation / Story Possibilities structure does not apply to them — they are standing operational instructions, not story possibilities. The existing guidance for writing direction.md stays unchanged.

Add a note at the top of the direction note section: "Direction notes are operational instructions for the story engine. They do not use the Design Notes / Situation / Story Possibilities structure — that structure applies to arc, intention, and introduction notes only."

- [ ] **Step 8: Update the note structure section**

Update the overview section to clearly distinguish direction notes (stay as-is) from arc/intention/introduction notes (new structure).

Add a table for arc/intention/introduction notes:
```
| Section | Notes |
|---|---|
| Frontmatter | YAML; see above |
| Brief | Frontmatter field; written last |
| Design Notes | Builder record; excluded from exports |
| Situation | State of affairs before player involvement |
| Story Possibilities | What could happen; phrased as possibility not script |
```

- [ ] **Step 9: Update self-check or add one for arc/intention notes**

Add a self-check for arc and intention notes:
```
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
```

- [ ] **Step 10: Verify**

- [ ] `brief` in frontmatter for all note types including direction
- [ ] Direction note guidance unchanged
- [ ] Design Notes section documented for arc/intention/introduction notes
- [ ] Situation section documented
- [ ] Story Possibilities section documented
- [ ] Self-check present for arc/intention notes
- [ ] Writing style clean

- [ ] **Step 11: Commit**

```
git add skills/worldbuilder-story/SKILL.md
git commit -m "feat: restructure story note (arc/intention/introduction) under Design Notes / Situation / Story Possibilities framework"
```

---

## Post-implementation

After all five tasks complete:

- [ ] Update `memory/MEMORY.md` to record the restructure session
- [ ] Verify worldbuilder-world-planning phase table correctly references worldbuilder-event
- [ ] Check CONTEXT.md for any note type descriptions that need updating (event note entry should reference worldbuilder-event skill)
- [ ] Final commit for any cross-file cleanup

```
git commit -m "docs: update memory and cross-references after note type restructure"
```
