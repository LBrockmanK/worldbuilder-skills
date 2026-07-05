---
name: worldbuilder-ainime-export
description: Use when exporting a completed Wide-phase worldbuilding project to ainime-games.com format. Requires complete character notes, a complete project/seed.md, and Wide-phase concept and story notes.
---

# Ainime Export

## Overview

This skill is the only one in the worldbuilder workflow that knows ainime-games field names. Every skill before this phase writes platform-agnostic notes. This skill reads those notes and packages them into the ainime `world.json` format.

Full JSON schema reference: `../../docs/target-system.md`.

---

## Prerequisites

Before running export, verify:
- [ ] `project/seed.md` tagged `complete` (all sections present)
- [ ] Every character note in `notes/` carries a closed status tag
- [ ] Concept notes in `notes/` written with `layer` set
- [ ] `project/direction.md` and the story notes (arcs, key intentions) in `notes/` tagged `complete`
- [ ] Introduction notes created for all characters

If any prerequisite is incomplete, return to the relevant Wide-phase skill rather than exporting a partial world.

---

## Field Map

| Source | ainime JSON field(s) |
|---|---|
| `project/seed.md` — Setting Summary | `settingSummary` |
| `project/seed.md` — Genre and Tone | `genre` |
| `project/seed.md` — Inspirations | `inspirations[]` |
| `project/seed.md` — Tonal Inspirations | `tonalInspirations[]` |
| `project/seed.md` — Key Tropes and Themes | `keyTropesAndThemes[]` |
| `project/seed.md` — Community | `communityDescription` |
| `project/seed.md` — World Introduction | `introText` |
| `project/seed.md` — Opening Situation | `initialStoryArc` |
| `project/seed.md` — era (from story direction or seed) | `calendarConfig.eraReminder` |
| `project/direction.md` | `arcManagerGuidance` |
| intention story notes + event notes in `notes/` | `storyTriggers[]` |
| event notes in `notes/` | `calendarConfig.weatherPools`, `eventCalendarSummary` |
| concept notes in `notes/` | `loreEntries[]` |
| character notes in `notes/` | `characters[]` |
| `project/seed.md` — Art style | `artStyle.background.*`, `artStyle.sprite.*` |

---

## Setting and Adventure Fields

Read `project/seed.md` and extract the following. The section names in the seed map directly.

**`settingSummary`** — Setting Summary section verbatim. Concrete and specific; this is the always-active context.

**`genre`** — Genre and Tone section verbatim.

**`inspirations`** — Inspirations section as a string array. One entry per line item.

**`tonalInspirations`** — Tonal Inspirations section as a string array. One entry per line item.

**`keyTropesAndThemes`** — Key Tropes and Themes section as a string array. One entry per line item.

**`communityDescription`** — Community section verbatim.

**`introText`** — World Introduction section verbatim.

**`initialStoryArc`** — Opening Situation section verbatim.

**`calendarConfig.eraReminder`** — One-phrase era descriptor. Extract from the seed's era description or story direction note.

**`calendarConfig.seasons`, `daysPerSeason`, `daysOfWeek`, `daySegments`** — Structural calendar configuration. Defaults: 4 seasons, 28 days/season, standard day names, Morning/Afternoon/Evening/Night. Change only if the world requires a different structure.

---

## Calendar Configuration

Read `calendar.md` (this skill's reference file) for design guidance on weather pools, festival layout, and day-segment defaults before building this section.

**`calendarConfig.weatherPools`** — Nested object: season → day segment → string array. Each string is a one-line weather description. 10–16 entries per season/segment. Derive from the world's seasonal tone and `project/seed.md`; see `calendar.md` for writing guidance.

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

**`eventCalendarSummary`** — Prose overview of the event calendar for LLM reference. Summarize the festival calendar and its emotional rhythms after all events are written.

**`storyTriggers[]` (calendar events)** — One entry per event note. Recurring annual events use `recurring: true` in the output. See `calendar.md` for how to derive `triggerOnDay` from the timing language that opens each event note's What Happens section, and how to write effective `promptInjection` content.

```json
{
  "id": "uuid",
  "name": "Event name",
  "triggerOnDay": 8,
  "promptInjection": "Active creative direction injected on this day.",
  "recurring": true
}
```

`triggerOnDay` is the absolute calendar day (1–112 for the 4×28 default). `promptInjection` is active direction to the story engine, not a neutral description of the event.

---

## Story Direction and Triggers

**`arcManagerGuidance`** — Read `project/direction.md`. This is the standing creative direction for the engine — the primary guard against escalation, flattening, and inappropriate pacing. Export verbatim; do not summarize.

**`storyTriggers[]` (story events)** — One entry per intention story note where a trigger condition can be expressed as a calendar day or a story moment. Intentions without a concrete trigger day do not produce `storyTriggers` entries; they remain in the `arcManagerGuidance` as ongoing direction instead.

---

## Lorebook Entries

Read all concept notes in `notes/`. Each note produces one `loreEntry`.

```json
{
  "id": "lore_{timestamp}_{random}",
  "keywords": ["keyword1", "keyword2+keyword3"],
  "content": "Lore text injected when keywords match.",
  "enabled": true
}
```

**Keywords** — Derive from the note's `aliases` frontmatter and any key terms in the note body. Use `+` between words for AND (both must appear together). Single terms are OR with other array entries. Keep keywords specific enough that they only fire when the topic is actually relevant.

**Content** — Summarize the concept note into a precise, dense lore injection. 50 tokens of exact context beats 300 tokens of vague description. Aim for what the AI most needs to know at the moment the topic arises.

**`availableFromDay`** — Set based on the note's `layer` frontmatter:
- `surface` — active from day 1
- `mid` — active from day 14 (one half-season in)
- `deep` — active from day 56 (two seasons in)
Adjust thresholds based on world pacing if these defaults don't fit.

**Enabled** — All entries default to `true`. Set `false` only for entries that should exist in the export but never activate.

---

## Character Export

For each character note in `notes/`, produce a character record. Process one character at a time; read `card-assembly.md` before writing the card.

| Character note field | ainime JSON field |
|---|---|
| Major/Supporting (cast plan entry in `project/plan.md`) | `type`: `"main"` or `"side"` |
| Character name | `name`, `lastName` |
| Derived by export skill | `role` |
| Assembled card prose | `baseProfile` |
| Appearance section | `appearance` |
| Sprite sets (see below) | `spriteSets[]` |
| Available Day (see below) | `availableFromDay` |

**`name` / `lastName`** — Extract from the character note filename.

**`type`** — `"main"` for major characters, `"side"` for supporting. Maps from the character's Major/Supporting designation in the cast plan (`project/plan.md`).

**`role`** — Not stored in the character note. Derive from the character's function as established by the character note content (their position in the world, their relationship to the player, their narrative role). Write as plain text.

**`baseProfile`** — The card prose. See `card-assembly.md` for full assembly guidance. This is the most complex field; do not attempt it without reading that file.

**`appearance`** — Use the Appearance section of the character note verbatim or lightly condensed. Cover species/type and sex if relevant, age presentation and body type, notable features, clothing style.

---

## Available Day Assignment

`availableFromDay` controls the earliest day the player can encounter this character. Assign based on narrative logic, not the export skill's defaults — the right day varies by world.

Guidelines:
- Day 1–3: characters the player would plausibly meet on arrival
- Day 7–14: characters tied to weekly routines or early story beats
- Day 15–28: characters the player needs to seek out or earn access to
- Day 29+: characters behind story gates or late-world reveals

Check all introduction notes to ensure each character's introduction scene can actually occur before their `availableFromDay`.

---

## Sprite Sets

`spriteSets` are named visual states for artwork — not emotional expressions. Expressions exist within states; states are the costume/context categories.

```json
[
  {
    "name": "default",
    "description": "Casual, at rest — the character's natural default state",
    "expressions": {
      "neutral": "image generation prompt for this state and expression"
    }
  }
]
```

Every character needs at minimum:
- **Casual** (`name: "default"`) — at rest, natural state
- **Working/Active** — doing their primary activity

Add additional states only where they're meaningfully distinct from the above (Formal for a character who attends ceremonial occasions; Combat for a fighter, etc.). Do not create states for transient emotional conditions.

The `description` drives art generation context; keep it concrete and consistent with the character's Appearance section. The `expressions.neutral` prompt is the base image generation prompt for that state.

---

## Art Style Prompts

Read the Art style section of `seed.md`. Translate the plain-language reference into prompt-engineering format.

**`artStyle.background.style_prefix`** — Prepended to all background prompts. Should establish the visual style consistently: rendering style, color palette tendencies, era cues.

**`artStyle.background.style_suffix`** — Appended to background prompts. Typically quality modifiers and technical parameters.

**`artStyle.background.negative_prompt`** — Elements to suppress across all backgrounds.

**`artStyle.sprite.style_prefix`** / **`style_suffix`** / **`negative_prompt`** — Same structure for character sprites. Sprite style should be consistent with background style but may have different technical requirements (transparent background, consistent character proportions).

Do not attempt to write `artStyle` content during Wide-phase work — this is a prompt-engineering output that belongs here.

---

## Self-Check Before Export Complete

**Setting fields**
- [ ] All seven Setting Tab fields present and non-empty
- [ ] `inspirations` and `tonalInspirations` are arrays, one item per source
- [ ] `keyTropesAndThemes` has 8–12 entries

**Calendar**
- [ ] `weatherPools` covers all seasons and all day segments
- [ ] All festival and observance events have `storyTriggers` entries
- [ ] Recurring events have `recurring: true`
- [ ] `eventCalendarSummary` written

**Lorebook**
- [ ] Every major location has a concept note → lore entry
- [ ] Background NPC guidelines entry present
- [ ] `availableFromDay` set on all entries per layer
- [ ] Keywords are specific; no partial-match traps

**Story direction**
- [ ] `arcManagerGuidance` is the full direction note, not a stub
- [ ] Story intention notes with concrete triggers have `storyTriggers` entries

**Characters (per character)**
- [ ] All required fields present: name, lastName, type, role, baseProfile, appearance, availableFromDay
- [ ] `baseProfile` prose is complete and in target range (~900 supporting, ~1500 major tokens)
- [ ] All six influence bands present in the card
- [ ] Sprite sets include at minimum Casual and Working/Active
- [ ] Introduction note created and introduction scene day ≤ `availableFromDay`
