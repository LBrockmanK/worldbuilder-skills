# Ainime Frontend Beta — Field Reference

Characterization of the beta build at `ainime-games.com/game/ainime-frontend`,
compared against the current live build at `ainime-games.com/game/sandbox`.
Both versions loaded with the same world ("Express Verdict!") on 2026-08-30.

Once finalized, the changes documented here will be folded into the main
`target-system.md` and `SKILL.md`. Until then, this file is the reference for
beta-targeted work.

---

## Tabs Unchanged

These tabs have identical field structure between current and beta:

- **Setting** — all fields identical
- **Lore** — same per-entry fields (Day, Keywords, Lore Content)
- **Locations** — same AI Location Builder fields and location image structure
- **Moods** — same Music Style, System Moods, and Gameplay Moods structure
- **Theme** — same UI color configuration
- **Characters (detail view)** — same per-character fields (First Name, Last Name, Type, Available From Day, Starting Influence, Role, Character Card / Profile, Appearance, Name Color, Sprite Sets)

---

## Tab Renamed

| Current | Beta |
|---------|------|
| Custom Prompts | **Prompts** |

---

## Characters Tab — List-Level Changes

Field-level character data is unchanged. The list-level UI has these differences:

| Feature | Current | Beta |
|---------|---------|------|
| Character reordering | Up/Down arrow buttons | **Drag to reorder** |
| AI character creation | — | **"Invent a character"** button — generates a character that fits the world and cast from user instructions |
| "Import Cards" button | Separate top-level button | Moved into the Import/Export button group |

---

## Adventure Tab

Three new boolean toggles for story-generation behavior at New Game time:

| Toggle | Description |
|--------|-------------|
| **Randomize the opening arc** | Each New Game rolls a threat and roles, then weaves and adapts them through Opening Story Arc. Adds replayability while preserving the authored arc as a foundation. |
| **Ignore Opening Story Arc — purely random story** | Each New Game ignores Opening Story Arc entirely and builds a new plot from the dice alone. |
| **Random NPC romance pair** | Each New Game picks two people from the character pool and a relationship dynamic. Independent of the opening arc toggles. |

Existing fields unchanged: AI generate side character toggle, Opening Story Arc, Ongoing Story Direction.

### JSON export status

These toggles do NOT appear in the exported `.sbworld` file. They are
app-level gameplay settings stored outside the world config — the export
contains only `generateSideCharacterOnNewGame` as before. The three new
toggles are user preferences set in the UI, not world data the export
skill produces.

---

## Calendar Tab

### New calendarConfig fields (confirmed from export)

| JSON field | UI label | Type | Value in sample |
|------------|----------|------|-----------------|
| `calendarConfig.dailyInfluenceCapGain` | Daily Influence Cap (Gain) | integer | `6` |
| `calendarConfig.dailyInfluenceCapLoss` | Daily Influence Cap (Loss) | integer | `6` |
| `calendarConfig.influenceMagnitudeTiers` | Influence Magnitude Ladder | string (multi-line) | See below |
| `calendarConfig.earliestClosePrompts` | Scene Ending Guidance: Earliest perfect close | integer | `6` |
| `calendarConfig.minPromptsBeforeTransition` | Scene Ending Guidance: Usual minimum | integer | `10` |
| `calendarConfig.usualMaxPrompts` | Scene Ending Guidance: Usual maximum | integer | `16` |

The old `calendarConfig.dailyInfluenceCap` still exists in the export alongside
the new split gain/loss fields. The split fields take precedence in the beta
engine.

**`influenceMagnitudeTiers`** format — one rung per line, value first:

```
- ±1: playful jab, eccentric gesture, small favor, or minor professional friction
- ±2: significant trust, shared evidence, public defense, or serious betrayal
- ±3: save a life or career, reveal a central secret, convict or clear someone close
```

The highest rung is the ceiling the AI cannot pass. Each rung costs that many
points of the daily cap (a ±3 spends 3 of the cap, not 1).

### Renamed calendarConfig field

| Current key | Beta key | Note |
|-------------|----------|------|
| `startingYear` | `baseYear` | Changed from `startingYear` to `baseYear` in calendarConfig |

### UI-renamed field (JSON key unchanged)

| UI label (current) | UI label (beta) | JSON key |
|---------------------|-----------------|----------|
| Daily Planner Directive | **Daily Directive** | `dailyPlannerDirective` (unchanged) |

The UI description changed from "the AI planner sees this every day" to "the
scene AI sees this every opening as standing day-shape," but the JSON key is
the same. No rename needed in the export skill.

### New top-level field: `yearContexts` (Life Stages)

A new **Life stages** section at the bottom of the Calendar tab. Life stages
define year-over-year progression of the world — how the setting evolves across
multiple in-game years.

The UI includes:
- AI generation with an optional brief
- Review-before-save workflow ("nothing is saved until you review it; tick the
  rows you want")
- Example-based guidance for different world types (high school, idol house,
  fantasy court, neighborhood cafe, historical village)

**JSON structure** — `yearContexts` is a top-level object keyed by
string-numbers ("0", "1", "2", ...). Each entry:

```json
{
  "name": "Year One — The Last Year of Dusk",
  "transition_warning_days": 7,
  "world_context": "The player begins professional life in...",
  "player_context": "The player character is chosen outside this world...",
  "schedule_context": "A case may occupy one, two, or at most three in-world days...",
  "npc_concerns": "Horace must decide whether the player is capable of...",
  "world_pressures": "Every active case has a seventy-two-hour legal deadline...",
  "sprite_set_guidance": "Use professional court or office outfits during work...",
  "transition_context": "Horace's retirement is mandatory on the final day...",
  "arc_resolution_guidance": "End or transform every plot that requires Horace...",
  "next_year_preview": "Next year Horace is retired. The player begins either as..."
}
```

| Field | Purpose |
|-------|---------|
| `name` | Display name for the stage |
| `transition_warning_days` | Days before stage end to warn the player |
| `world_context` | Detailed world state description for this stage |
| `player_context` | Player character context and constraints |
| `schedule_context` | Scheduling rules (workweek structure, case timing) |
| `npc_concerns` | NPC motivations, arcs, and activities during this stage |
| `world_pressures` | External pressures, deadlines, and constraints |
| `sprite_set_guidance` | Which sprite sets to use for characters |
| `transition_context` | What happens at the stage boundary |
| `arc_resolution_guidance` | How story arcs should resolve at stage end |
| `next_year_preview` | Preview of the next stage for continuity |

This is the richest new data structure in the beta — each entry is
essentially a full creative brief for one era of gameplay.

---

## Art Style Tab

### New field

| Field | Section | Description |
|-------|---------|-------------|
| **Clothing rules (one per line)** | Sprite Generation | Per-line clothing directives for sprite generation. Controls what characters wear in generated art. |

Existing fields unchanged: Time-of-Day Lighting, Background Generation
(prefix/suffix/negative), Sprite Generation (prefix/suffix/consistency).

### Confirmed JSON structure

`artStyle.sprite.clothingRules` — **string array**. Each UI line becomes a
separate array entry:

```json
"clothingRules": [
  "Each recurring character must have an instantly recognizable silhouette and color motif.",
  "Provisional licenses carry an amber luminous band somewhere on the outfit.",
  "Clothing can be absurd and theatrical, but must reveal the character's profession, quirk, or philosophy.",
  "Do not copy costumes, hairstyles, accessories, or emblems from existing franchises."
]
```

---

## Prompts Tab (was Custom Prompts)

The most extensively restructured tab. Two major changes:

### 1. Prompt Sets

The beta introduces a **Prompt Sets** system — switchable, named collections of
all prompt overrides. The current version has a single flat configuration.

| Feature | Description |
|---------|-------------|
| **Default** set | Ships read-only with the platform. Cannot be edited directly. |
| **Minimal** set | A second built-in set (presumably stripped-down prompts). |
| **+ New** | Create a custom set. |
| **Start a set from this** | Clone the currently viewed set as a new editable set. |
| **Import set** | Import a prompt set from file. |
| **Browse community presets** | Browse and install prompt sets shared by other users. |

Only one set is **Active** at a time. A set marked "read-only" (like Default)
must be cloned before editing.

### 2. Restructured AI Personas

**Game AI personas** — the AI roles whose system prompts can be overridden:

| Current | Beta | Change |
|---------|------|--------|
| Dungeon Master | Dungeon Master | Unchanged (but now has structured sub-sections — see below) |
| Transition Director | — | **Removed** (functionality may have moved to Volume Synopsis) |
| Arc Manager | Arc Manager | Unchanged |
| Narrative Architect | Narrative Architect | Unchanged |
| Relationship Analyst | Relationship Analyst | Unchanged |
| Cast Analyst | Cast Analyst | Unchanged |
| Novelist | Novelist | Unchanged |
| Psychoanalyst | Psychoanalyst | Unchanged |
| VN Director | VN Director | Unchanged |
| — | **Volume Synopsis** | NEW — likely handles scene/day transition summaries |
| — | **Bio Compressor** | NEW — likely compresses character bios for context efficiency |
| — | **Character Developer** | NEW — likely handles character arc progression |
| — | **Canon Archivist** | NEW — likely maintains world-state consistency |
| — | **Video Director** | NEW — handles video scene generation (separate from VN Director) |

**Structured DM prompt sections** — the Dungeon Master persona (and
presumably others) now exposes structured sub-sections rather than a single
text area:

- **System Prompt** — the base system prompt injection
- **Story Cache** — injected story context
- **User Prompt** — user-turn prompt structure
- **Scene opening + scene plan writing** — scene initialization prompts
- **Every turn** — per-turn prompt injections

### 3. Exposed Generation Templates

The beta exposes the prompts the World Builder itself uses for AI-assisted
content generation. These are customizable per prompt set:

| Template | What it controls |
|----------|-----------------|
| Setting / Lore | AI generation of setting and lore content |
| Arc Builder | AI generation of story arcs |
| Character Fields | AI-assisted character field population |
| Expression Prompts | Expression/emotion prompt generation |
| Time Lighting | Time-of-day lighting description generation |
| Weather | Weather pool generation |
| Events | Calendar event generation |
| Life Stages | Life stage generation |
| Moods / BGM | Mood/music generation |
| Music Style | Music style prompt generation |
| Player Appearance | Player character appearance generation |
| Character Card (In-Game) | In-game character card prompt |
| Character Card (World Builder) | World Builder card writing AI prompt |
| Character Appearance | Character appearance description generation |
| Clothing Rules | Clothing rule generation |

### Export impact (confirmed)

The `customPrompts` object in the exported `.sbworld` is **empty** when
using the built-in Default prompt set. A new top-level field
`activePromptSet` stores only a reference: `{ "kind": "default" }`.

Custom prompt overrides appear to be stored in the `customPrompts` object
only when a user-created prompt set with modifications is active. The
structured sub-sections (System Prompt, Story Cache, User Prompt, etc.)
and the generation templates are UI-level organization — their content
lands in the same `customPrompts` keys when overridden.

The export skill does not need to produce prompt sets. Prompt
customization is a user-facing feature, not world content.

---

## Other UI Changes

| Change | Description |
|--------|-------------|
| **Install App** button | New button in the top menu bar for PWA installation. |
| **Patch notes** | Shared between both versions — same content. |
| **Setting tab intro text** | Beta shows "World Setting" heading with a note about "AI Generate from Imports" filling fields — the current version shows no such intro. |

---

## Confirmed New JSON Fields (from `.sbworld` export)

Export inspected: `Express Verdict!_test.sbworld` from the beta build,
2026-08-30.

### Fields the export skill should produce

| JSON field | Tab | Type | Export priority |
|------------|-----|------|----------------|
| `yearContexts` | Calendar (Life Stages) | object (keyed "0","1",...) | **High** — rich creative content, 10 sub-fields per stage |
| `artStyle.sprite.clothingRules` | Art Style | string[] | **Medium** — one entry per line, derivable from character notes |
| `calendarConfig.influenceMagnitudeTiers` | Calendar | string (multi-line) | **Medium** — world-specific magnitude scale |
| `calendarConfig.earliestClosePrompts` | Calendar | integer | **Low** — pacing config, typically a default |
| `calendarConfig.minPromptsBeforeTransition` | Calendar | integer | **Low** — pacing config |
| `calendarConfig.usualMaxPrompts` | Calendar | integer | **Low** — pacing config |
| `calendarConfig.dailyInfluenceCapGain` | Calendar | integer | **Low** — split from existing `dailyInfluenceCap` |
| `calendarConfig.dailyInfluenceCapLoss` | Calendar | integer | **Low** — split from existing `dailyInfluenceCap` |

### Fields the export skill does NOT produce

| Field | Reason |
|-------|--------|
| Adventure toggles (randomize, ignore, romance pair) | Not in the `.sbworld` export — app-level gameplay settings |
| `activePromptSet` | Reference only (`{ "kind": "default" }`); prompt sets are user customization |
| `customPrompts` structured sub-sections | Empty when Default set is active; user customization, not world content |

### Renamed field

| Old key | New key | Notes |
|---------|---------|-------|
| `startingYear` | `calendarConfig.baseYear` | Renamed in the JSON |

### Unchanged despite UI rename

| JSON key | Old UI label | New UI label |
|----------|-------------|--------------|
| `dailyPlannerDirective` | Daily Planner Directive | Daily Directive |

The key is the same. No export skill change needed.

---

## Remaining Open Questions

- [ ] Test whether a beta `.sbworld` with `yearContexts` and the new
      calendarConfig fields loads correctly on the current live version
      (backward compatibility)
- [ ] Confirm whether `calendarConfig.baseYear` replaces `startingYear`
      entirely or both keys coexist
- [ ] Determine the worldbuilding workflow's source for Life Stages content —
      `yearContexts` is very rich (10 sub-fields per stage) and may need its
      own Wide-phase skill or an extension of `worldbuilder-story`
- [ ] Confirm whether the Sprite Negative Prompt field
      (`artStyle.sprite.negative_prompt`) is new to the beta or was already
      present but undocumented (it does not appear in the export when empty)
