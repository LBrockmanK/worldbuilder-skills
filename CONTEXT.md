# RPG World Builder Skills

Workflow skills for building and realizing a player's world vision for the ainime-games.com world builder platform. Phases 1 and 2 are platform-agnostic. Only Phase 3 (Export) produces ainime-specific output.

## Language

### Phases

**Seed phase (Phase 1)**:
The clarification-heavy opening phase. Produces `seed.md` — a platform-agnostic project proposal capturing foundational decisions. Ends when the user confirms the seed is ready.
_Avoid_: Foundation phase, setup phase

**Wide phase (Phase 2)**:
The expansive generative phase. Produces platform-agnostic notes: character notes, concept notes, event notes, story notes. All creative decisions live here.
_Avoid_: Development phase, building phase

**Export phase (Phase 3)**:
The conversion phase. Wide-phase notes are read by the export skill and packaged into the target system's format. The only phase that writes ainime field names.
_Avoid_: Deliverables phase, finalization phase, output phase

### Documents

**`seed.md`**:
The world foundation document. Plain prose with natural section headers — not written in any export format. Captures: setting summary, genre and tone, inspirations, community description, world introduction, opening situation, story direction stub, locations list, art style reference, musical theme, household designs.
_Avoid_: world-seed.md, seed document (if referring to a file — use `seed.md`)

**Character note**:
The comprehensive Wide-phase document for a single character. Single source of truth — richer than any export format can hold. Sections: frontmatter, preamble, concept, inspirations, design notes, foundation, behavioral descriptions, relationships, relationship behavior, storylines. The ainime character card (`baseProfile`) is derived from this note by the export skill.
_Avoid_: Blueprint, draft card

**Concept note**:
A discrete piece of world knowledge in `notes/`. Layer-tagged (surface, mid, deep). Aliases in frontmatter become keyword candidates at export. The export skill packages concept notes as lorebook entries.
_Avoid_: Lorebook entry (when referring to the Wide-phase artifact), Lorebook Candidates

**Event note**:
A calendar or historical event in `notes/`. Frontmatter includes `date` (calendar day), `recurring`, `characters`, `location`. The export skill packages event notes as `storyTriggers` and `calendarConfig` entries.
_Avoid_: Calendar entry (when referring to the note itself)

**Story note**:
A narrative direction document in `notes/`. Three scopes connected by `up:` hierarchy: direction (top-level creative brief), arc (major story section), intention (specific story possibility). The export skill maps direction notes to `arcManagerGuidance` and intention notes to `storyTriggers` where conditions allow.
_Avoid_: story.md (as a single document)

**Introduction note**:
A story note with `scope: "[[introduction]]"` describing first contact between the player and a character. Belongs in `notes/`, not in the character note. One introduction note can cover multiple characters.

### Process

**Cast planning**:
The Phase 2 process of planning the full cast before writing individual character notes. Produces a cast plan in `worldbuilding-plan.md`. Coverage check happens here.

**Coverage check**:
A pre-completion review of the cast plan verifying: main/side ratio against the 8/16 default target, household balance, archetype slot coverage (6 romance archetypes, all non-romance archetypes placed), negative-track characters present.

**Post-group sync pass**:
A review run after completing a household group of character notes. Checks that named relationships are consistent across the group before moving on.

**Target system**:
The ainime-games.com world builder — the platform that consumes all export deliverables. Its field structure is documented in `docs/target-system.md`. Only the Export phase writes to this structure.

---

## Project File Structure

A complete project uses a shallow hybrid vault organized by note type.

```
worldbuilding-plan.md   ← project plan, cast plan, phase status (type: project)
seed.md                 ← world foundation (Seed phase output) (type: project)
log.md                  ← retcon and change log (type: project)
agent-context.md        ← agent operational reference (type: reference)
notes/                  ← all Wide-phase content notes (character, location, faction, event, concept, story)
_templates/             ← note templates for human users
```

### Note types and frontmatter

All notes carry universal frontmatter plus type-specific fields:

**Universal:**
```yaml
type: character | location | faction | event | concept | story | project | reference
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
```

**Character:**
```yaml
factions: ["[[Household Name]]"]   # links
role: plain text
archetype: "[[Initially Hostile]]" # link
```

**Location:**
```yaml
region: "[[The Valley]]"           # link
function: one phrase
primary-characters: ["[[Name]]"]   # links
```

**Faction/Household:**
```yaml
members: ["[[Name]]"]              # links
function: one phrase
```

**Event:**
```yaml
date: "[[Spring-08]]"              # link; clusters events by day
recurring: false
characters: ["[[Name]]"]           # links
location: "[[Location Name]]"      # link
```

**Concept (lore):**
```yaml
layer: "[[surface]]"               # link; clusters by depth
trigger-context: brief plain text
```

**Story:**
```yaml
up: "[[parent-story-note]]"        # absent on top-level direction note
scope: "[[direction]]" | "[[arc]]" | "[[intention]]" | "[[introduction]]"
```

**Link convention:** Anything that represents a category, entity, or concept worth filtering by uses a `[[wikilink]]`. Plain values for operational fields (`status`, `last_updated`, `recurring`, booleans).

### What goes where

| Note | ainime JSON field(s) |
|---|---|
| `seed.md` — Setting Summary | `settingSummary` |
| `seed.md` — Genre and Tone | `genre` |
| `seed.md` — Inspirations / Tonal Inspirations | `inspirations[]`, `tonalInspirations[]` |
| `seed.md` — Key Tropes and Themes | `keyTropesAndThemes[]` |
| `seed.md` — Community | `communityDescription` |
| `seed.md` — World Introduction | `introText` |
| `seed.md` — Opening Situation | `initialStoryArc` |
| `seed.md` — era | `calendarConfig.eraReminder` |
| `notes/` notes with `type: concept` | `loreEntries[]` |
| `notes/` notes with `type: event` | `storyTriggers[]`, `calendarConfig.weatherPools`, `eventCalendarSummary` |
| `notes/direction.md` | `arcManagerGuidance` |
| `notes/intention-*.md` | `storyTriggers[]` (where day trigger exists) |
| `notes/` notes with `type: character` | `characters[]` (baseProfile, appearance, spriteSets, metadata) |

Full ainime field reference: `docs/target-system.md`.

---

## Example Dialogue

> "Should I add the smithy description to Bram's character note?"
>
> "No — that goes in a concept note for the smithy. The smithy only matters when someone is at or near it; it's not core to who Bram is. Create `notes/harrows-smithy.md` with `layer: surface` and add 'the smithy', 'Harrow's smithy', 'the forge' to its aliases."

> "We're done with all the character notes. What's next?"
>
> "Start the Export phase. For each character, run `worldbuilder-ainime-export` and build the card from the character note. Character notes are independent once complete — parallelize freely."

> "Should I start writing event notes before the cast is finished?"
>
> "Skeleton structure is fine, but hold the detailed event descriptions until the cast exists. Festival scenes are richer once you know who's in them. You can write `events/spring-festival.md` with frontmatter and a placeholder body, then flesh it out after the cast notes are done."
