# RPG World Builder Skills

Workflow skills for building and realizing a player's world vision for the ainime-games.com world builder platform. All outputs are functional documents for an AI GM — clarity and precision outrank stylistic quality in every phase.

## Language

### Phases

**Seed phase (Phase 1)**:
The clarification-heavy opening phase. Produces the seed document. Ends when the user confirms the seed is ready.
_Avoid_: Foundation phase, setup phase

**Wide phase (Phase 2)**:
The expansive generative phase. Covers the character roster, blueprints, locations, and broad setting detail. Lorebook Candidates accumulate here.
_Avoid_: Development phase, building phase

**Deliverables phase (Phase 3)**:
The conversion phase. Broad Phase 2 documents are trimmed and distilled into final target-format outputs. Trimming at two points — Phase 2→3 transition and within Phase 3 — both generate Lorebook Candidates.
_Avoid_: Finalization phase, output phase

### Documents

**Seed document**:
The world foundation document. A direct draft of the target system's Setting fields, written in final format from the start. A starting point, not gospel — the world will grow in directions it does not anticipate.
_Avoid_: World summary, world overview, foundation document

**Blueprint**:
A broad, exploratory Phase 2 document for a single character. Covers all dimensions of the character without constraint on length or scope. Distilled into the card.
_Avoid_: Draft card, character sheet

**Card**:
The final character deliverable. Distilled from the blueprint into compact flowing prose. A functional specification for the AI GM, not a creative writing exercise.
_Avoid_: Character sheet, character document

**Lorebook Candidates**:
A dedicated section present in every Phase 2 document. Collects facts that are true and interesting but too narrow in scope for core documents — things best triggered by keyword in-scene rather than always active. Accumulates across both trim passes without being emptied between them.
_Avoid_: Overflow, world info, extras

### Process

**Trim pass**:
A review that cuts content from a document to sharpen focus. Two occur per character: once at the Phase 2→3 transition, once within Phase 3 as the card is tightened. Cut content with ongoing value goes to Lorebook Candidates.

**Coverage check**:
A pre-completion review of the character roster showing main/side ratio against the 8/16 default target, household balance, and archetype slot coverage. Surfaced by the skill before asking the user to confirm the roster is complete.

**Target system**:
The ainime-games.com world builder — the platform that will consume all final deliverables. Its field structure defines what the seed document and all final outputs must map to.

## Expected Project File Structure

At each phase boundary, a complete project should contain the following files. Paths are relative to the project root.

### After Seed phase

```
worldbuilding-plan.md
world-seed.md
```

`world-seed.md` contains all Setting tab fields and stubs for the Adventure tab fields. The locations list (10–14 entries), art style reference, and musical theme reference are also in `world-seed.md` — they are plain-language descriptions that will be translated to prompt format during the Deliverables phase.

### After Wide phase

```
worldbuilding-plan.md
world-seed.md
lorebook.md               ← draft; final pass happens after blueprints
calendar.md
story.md
characters/
  roster.md
  blueprints/
    firstname-lastname.md  (one per character)
```

Every blueprint ends with a `## Lorebook Candidates` section. `calendar.md` and `story.md` also end with `## Lorebook Candidates` sections.

### After Deliverables phase (project complete)

```
worldbuilding-plan.md
world-seed.md             ← not modified; source of truth for Setting fields
lorebook.md               ← finalized after lorebook review pass
calendar.md
story.md
characters/
  roster.md
  blueprints/             ← retained as reference
    firstname-lastname.md
  cards/
    firstname-lastname.md  (one per character — final card format)
```

### What goes where

| Document | JSON field(s) it maps to |
|---|---|
| `world-seed.md` | `settingSummary`, `genre`, `inspirations`, `tonalInspirations`, `keyTropesAndThemes`, `communityDescription`, `introText`, `initialStoryArc` (stub), `arcManagerGuidance` (stub), `calendarConfig.eraReminder` |
| `lorebook.md` | `loreEntries[]` |
| `calendar.md` | `calendarConfig.weatherPools`, `storyTriggers[]` (events), `dailyPlannerDirective`, `eventCalendarSummary` |
| `story.md` | `arcManagerGuidance` (full), `storyTriggers[]` (story events), `initialStoryArc` (refined) |
| `characters/roster.md` | Precursor to all `characters[]` entries; not directly imported |
| `characters/blueprints/` | Precursor to `characters[].baseProfile`; not directly imported |
| `characters/cards/` | `characters[].baseProfile`, `characters[].appearance`, `characters[].spriteSets[].description` |

Full JSON field reference: `docs/target-system.md`.

---

## Example Dialogue

> "Should I write the smithy description in Bram's card?"
>
> "No — that goes in Lorebook Candidates on his blueprint. The smithy only matters when someone is at the smithy; it's not core to who Bram is. Strip it from the card and flag it as a lorebook entry."

> "We're done with the blueprints. What's next?"
>
> "Start the deliverables phase. For each character, distill the blueprint into the card. Anything cut goes to Lorebook Candidates if it's still true and useful. After all cards are done, run the lorebook review pass across every Lorebook Candidates section."

> "Should I start the calendar before the roster is finished?"
>
> "No. Skeleton structure is fine, but hold the events until the cast exists. Festival scenes are richer once you know who's in them."
