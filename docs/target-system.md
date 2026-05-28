# Target System — Field Reference

The ainime-games.com world builder stores all world configuration in a `.sbworld` archive (a ZIP containing `world.json` + image assets). This document is the authoritative map of the `world.json` schema: every field we write, what goes in it, and which skill produces it.

All field names below are the exact JSON keys. These fields are produced by `worldbuilder-ainime-export`, which reads from platform-agnostic Wide-phase notes. The Skill column shows the Wide-phase skill that authors the source content.

**Format version:** 2 (`.sbworld` — current). Earlier `.json` exports may have different or missing fields.

---

## Setting Tab

| JSON field | UI label | Type | Source content skill |
|---|---|---|---|
| `settingSummary` | Setting Summary | string | `worldbuilder-world-foundation` → `seed.md` |
| `genre` | Genre & Tone | string | `worldbuilder-world-foundation` → `seed.md` |
| `inspirations` | Inspirations | string[ ] | `worldbuilder-world-foundation` → `seed.md` |
| `tonalInspirations` | Tonal Inspirations | string[ ] | `worldbuilder-world-foundation` → `seed.md` |
| `keyTropesAndThemes` | Key Tropes & Themes | string[ ] | `worldbuilder-world-foundation` → `seed.md` |
| `communityDescription` | Community Description | string | `worldbuilder-world-foundation` → `seed.md` |
| `introText` | World Introduction | string | `worldbuilder-world-foundation` → `seed.md` |

### Field notes

**`settingSummary`** — The primary always-active context the engine reads for every scene. Should establish where, when, what the community is like, what the player's situation is, and what the overall tone is. Write it as concrete and specific as possible — this is the context the AI reads constantly.

**`genre`** — Full field label is "Genre & Tone". Not just a genre tag; it is an explicit description for the AI covering primary genre, tonal range (how dark can it go, how light), and content notes.

**`inspirations`** — One string per item. Include what is specifically drawn from each reference, not just the title. `"Stardew Valley — farming life rhythm and community bonds"` not `"Stardew Valley"`.

**`tonalInspirations`** — Same format as `inspirations`. Films, books, music, anime — media that captures the right feel even if it doesn't share the genre.

**`keyTropesAndThemes`** — One string per item. 8–12 entries covering both setting tropes and emotional themes. These shape what the AI treats as thematically available throughout the game.

**`communityDescription`** — The community's social and emotional identity. Not a physical description and not a repeat of `settingSummary` — this is specifically how the community behaves and feels as a social entity. Used as context for how background characters and social dynamics should read.

**`introText`** — Pre-game text the player reads before creating their character. Sets expectations for tone and situation. The player creates only name and appearance — the intro should reflect that. Typically 2–4 short paragraphs.

---

## Adventure Tab

| JSON field | UI label | Type | Source content skill |
|---|---|---|---|
| `initialStoryArc` | Opening Story Arc | string | `worldbuilder-world-foundation` → `seed.md` |
| `arcManagerGuidance` | Ongoing Story Direction | string | `worldbuilder-story-direction` → `story/` |
| `storyTriggers` | Story Triggers (Events) | StoryTrigger[ ] | `worldbuilder-story-direction` + `worldbuilder-calendar` → `story/` + `events/` |

### Field notes

**`initialStoryArc`** — A brief, evocative description of the situation when the player arrives. Not a scripted sequence — it sets the stage. Drafted in the Seed phase and refined after the cast exists. See `worldbuilder-story-direction` for content guidance.

**`arcManagerGuidance`** — The engine's standing creative brief throughout the game. The primary guard against escalation, flattening, and inappropriate pacing. Covers: author framing, romance pacing, dark themes, hidden layer handling, seasonal tone, pacing. This is one of the most important fields; a weak brief here degrades every scene the engine generates. See `worldbuilder-story-direction` for the full template.

**`storyTriggers`** — Named events with a day trigger and a narrative injection prompt. When the trigger day is reached (or when a recurring event's anniversary arrives), the `promptInjection` text is injected into the engine's context.

StoryTrigger schema:
```json
{
  "id": "uuid",
  "name": "Event name",
  "triggerOnDay": 8,
  "promptInjection": "Narrative direction text injected on this day.",
  "recurring": false
}
```

Set `recurring: true` for annual events (festivals, observances). One-time events use `recurring: false`.

---

## Calendar Tab

| JSON field / path | UI label | Type | Source content skill |
|---|---|---|---|
| `calendarConfig.seasons` | Seasons | string[ ] | `worldbuilder-calendar` → `events/` |
| `calendarConfig.daysPerSeason` | Days per Season | number | `worldbuilder-calendar` → `events/` |
| `calendarConfig.daysOfWeek` | Days of Week | string[ ] | `worldbuilder-calendar` → `events/` |
| `calendarConfig.daySegments` | Day Segments | string[ ] | `worldbuilder-calendar` → `events/` |
| `calendarConfig.eraReminder` | Era | string | `worldbuilder-world-foundation` → `seed.md` |
| `calendarConfig.weatherPools` | Weather Pools | object | `worldbuilder-calendar` → `events/` |
| `storyTriggers` | Events / Recurring Events | StoryTrigger[ ] | `worldbuilder-calendar` → `events/` |
| `eventCalendarSummary` | Event Calendar Summary | string | `worldbuilder-calendar` → `events/` |

> **Note on `dailyPlannerDirective`:** This field appeared in some earlier `.json` world exports but is absent from the current `.sbworld` format. It may have been folded into `arcManagerGuidance`, removed from the schema, or be UI-only content that does not export. Treat daily planner guidance as part of `arcManagerGuidance` until the field status is confirmed.

### Field notes

**`calendarConfig.eraReminder`** — One phrase describing the technology and cultural reference point. The engine uses this to calibrate anachronism. Decided in the Seed phase. Example: `"Contemporary rural — smartphones exist but signal is bad."` or `"Pre-industrial fantasy, no electricity."`

**`calendarConfig.weatherPools`** — Nested object: season → day segment → string array. Each string is a one-line weather description. The AI picks from the pool when generating scenes. Aim for 10–16 entries per season/segment combination.

```json
{
  "Spring": {
    "Morning": ["Light fog lifting...", "Crisp clean air..."],
    "Afternoon": ["..."],
    "Evening": ["..."],
    "Night": ["..."]
  }
}
```

**`storyTriggers`** — The calendar events field. Both recurring annual events (`recurring: true`) and one-time events (`recurring: false`) are stored here. See the Adventure tab section above for the schema.

**`eventCalendarSummary`** — Narrative overview of the full event calendar for LLM reference. A prose summary of the festival calendar and its emotional rhythms — written for the AI, not the player. Produced after all events are written.

**`calendarConfig.seasons`, `daysPerSeason`, `daysOfWeek`, `daySegments`** — Structural configuration. Defaults: 4 seasons, 28 days per season, standard day names, Morning/Afternoon/Evening/Night. Change only if the world needs a different time structure.

---

## Lore Tab

| JSON field path | Type | Skill |
|---|---|---|
| `loreEntries` | LoreEntry[ ] | `worldbuilder-lorebook` |

### LoreEntry schema

```json
{
  "id": "lore_{timestamp}_{random}",
  "keywords": ["keyword1", "keyword2+keyword3"],
  "content": "Lore text injected when keywords match.",
  "enabled": true
}
```

**`keywords`** — Array of trigger strings. Comma-separated entries are OR (any one triggers). Use `+` between words for AND (both must appear). Keep keywords specific enough that they only fire when the topic is actually relevant.

**`content`** — The lore text injected into context when keywords match. Aim for precision over length — 50 tokens of exact context beats 300 tokens of unfocused description.

**`enabled`** — Boolean. Disabled entries exist but never trigger.

**Date gates** — The UI shows an "Available Day" field for lore entries. This controls when an entry becomes active. Set it to prevent deep lore from surfacing before the player has invested enough time. In the JSON, this field may appear as `availableFromDay` on individual entries. If not present, the entry is active from day 1.

---

## Characters Tab

One object per character in the `characters` array.

| JSON field | UI label | Notes |
|---|---|---|
| `name` | First Name | — |
| `lastName` | Last Name | — |
| `role` | Role | One or two phrases |
| `baseProfile` | Character Card | Main character description — see below |
| `appearance` | Appearance | Physical description for image generation and LLM reference |
| `type` | Type | `"main"` or `"side"` |
| `availableFromDay` | Available Day | Earliest possible introduction day |
| `spriteSets` | Sprite Sets | Visual states for artwork |
| `color` | Color | UI display color (CSS class string) |

### `baseProfile` — structure

The `baseProfile` field is a single text block: unstructured flowing prose. No JSON sub-fields, no rigid internal format. The card body (personality, background, behavior, relationships, influence thresholds) is written as connected prose followed by a **Future Storylines** section. No internal headers in the card body.

See `worldbuilder-ainime-export/card-assembly.md` for the full assembly guide, register rules, and token targets.

### `appearance` — structure

Physical description for image generation and LLM reference. Cover: species/type and sex (if relevant), age presentation and body type, notable features, clothing style. Should be consistent with `baseProfile`.

### `spriteSets` schema

```json
[
  {
    "name": "default",
    "description": "Casual, at rest — the character's natural state",
    "expressions": {
      "neutral": "image generation prompt for this state"
    }
  }
]
```

Each sprite set is a named visual state (Casual, Working, Formal, etc.). Not emotional expressions — those are handled separately. The `description` guides art generation; the `expressions` object contains per-expression image prompts.

---

## Locations Tab

The Locations tab manages image pools — sets of location images by time of day. It is NOT the source of narrative location descriptions.

| JSON path | Structure |
|---|---|
| `locations` | `{[timeSegment]: LocationImage[]}` |

```json
{
  "Morning": [{"name": "slug_name", "url": "base64...", "prompt": "image gen prompt"}],
  "Afternoon": [...],
  "Evening": [...],
  "Night": [...]
}
```

**Narrative location descriptions** belong in `loreEntries`, not the `locations` object. Write a lorebook entry for each major location covering what the place looks like, who uses it, what it means, and one vivid specific detail. The `locations` object is for art assets.

---

## Art Style Tab

The Art Style tab configures image generation prompts for backgrounds and character sprites.

| JSON path | What it contains |
|---|---|
| `artStyle.background.style_prefix` | Prefix prepended to all background generation prompts |
| `artStyle.background.style_suffix` | Suffix appended to all background prompts |
| `artStyle.background.time_contexts` | Per-segment lighting descriptions added to prompts |
| `artStyle.background.negative_prompt` | Negative prompt for backgrounds |
| `artStyle.sprite.style_prefix` | Prefix for all sprite generation prompts |
| `artStyle.sprite.style_suffix` | Suffix for all sprite prompts |
| `artStyle.sprite.negative_prompt` | Negative prompt for sprites |

The Seed phase produces a **plain-language art style reference** describing the desired visual style, color palette, and reference works. This is translated into prompt-engineering format during export.

Do not attempt to write `style_prefix` / `style_suffix` content during the Seed or Wide phases — these are prompt-engineering outputs produced by `worldbuilder-ainime-export`.

---

## Moods Tab

The Moods tab drives AI-generated music. It has no text fields that the worldbuilding workflow writes — the AI generates music based on your world configuration.

The Seed phase produces a **plain-language musical theme reference** describing genre, tempo, instrumentation, and mood register. This informs the music generation configuration but does not map to a specific JSON text field.

---

## Theme Tab

UI color theme. Not part of the worldbuilding workflow. Configure after content is complete.

| JSON field | Content |
|---|---|
| `uiTheme.primaryColor` | Primary accent color |
| `uiTheme.secondaryColor` | Secondary color |
| `uiTheme.textboxGradient1/2/3` | Dialog box gradient colors |

---

## Custom Prompts Tab

Advanced overrides for specific engine prompts. Not part of the standard worldbuilding workflow.

| JSON field | Content |
|---|---|
| `customPrompts` | Object with keys: `dm` (director), `am` (arc manager), `na` (narrator), `td` (translator), and others |

---

## Phase → Field Mapping

All JSON fields are produced by `worldbuilder-ainime-export` reading from Wide-phase notes. This table shows which notes are the source for each field group.

### Wide-phase sources → ainime export input

```
seed.md                → settingSummary, genre, inspirations, tonalInspirations,
                         keyTropesAndThemes, communityDescription, introText,
                         initialStoryArc, calendarConfig.eraReminder,
                         calendarConfig.seasons/daysPerSeason/daysOfWeek/daySegments
                         [art style reference → artStyle.* prompts]

concepts/              → loreEntries[]

events/                → calendarConfig.weatherPools, storyTriggers[] (events),
                         eventCalendarSummary

story/direction.md     → arcManagerGuidance
story/intention-*.md   → storyTriggers[] (story events, where trigger day exists)

characters/*.md        → characters[].name, lastName, type, role, availableFromDay,
                         baseProfile, appearance, spriteSets[]
```

### Export skill deliverables

The `worldbuilder-ainime-export` skill produces formatted output ready for entry into the ainime platform. Character cards are the most complex output; see `card-assembly.md` in that skill's directory.

---

## Fields We Do Not Write

These fields are auto-generated or configured by the platform — do not produce content for them:

- `worldId` — UUID assigned by the platform
- `availableExpressions` — system-provided expression list
- `generateSideCharacterOnNewGame` — platform toggle
- `characters[].color` — UI display color, set in platform
- `characters[].image` — generated artwork
- `characters[].expressionPrompts` — generated expression prompts
- `locations[].url` — generated background images
- `artStyle.sprite.same_character_consistency` — platform setting
- `artStyle.sprite.use_tag_style_prompts` — platform setting
- `uiTheme.*` — UI configuration, set after content
- `customPrompts.*` — advanced overrides, not standard workflow
- `mainMenuBackground` / `mainMenuBackgroundThumbnail` — generated images
- `author`, `tags` — publishing metadata
