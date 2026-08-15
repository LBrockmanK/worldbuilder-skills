---
type: reference
title: Weather — Seasonal Weather System
description: 'Extracted weather definitions from fiddle/weather.toml: seasonal weather
  counts, weather types (calm, inclement, heavy inclement, special) with music and
  gameplay effects. No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T22:53Z
resources:
- projects/fields-of-mistria/source/fiddle/weather.toml
---

# Weather — Seasonal Weather System

Source: `source/fiddle/weather.toml`

## Seasonal Weather Counts

Number of days per season with each weather type (range: min–max).

| Season | Inclement Days | Special Days |
|--------|---------------|--------------|
| Spring | 4–6 | 4–6 |
| Summer | 4–6 | 0 |
| Fall | 4–6 | 4–6 |
| Winter | 4–6 | 0 |

## High Cloud Rendering

- fade_in: 7:30–8:30
- fade_out: 18:30–19:30
- range: [550, 700]
- speed: [0.07, 0.1]
- angle: [35, 55]
- opacity: 0.14

## Default Weather Properties

- bug_spawn_multiplier: 1
- music: "&lt;n/a&gt;"

Source comment: "A multiplier on the number of bugs that will spawn during this weather event. For example, if 10 bugs are supposed to spawn, and our multiplier is 0.5, 5 bugs will spawn."

## Weather Types

### calm

Default / empty weather. Source comment: "Calm weather behaves differently than everything else since it is our default / empty weather. Basically, leave it alone!"

No properties set — uses all defaults.

### inclement

- bug_spawn_multiplier: 0.8
- Music by season:
  - Spring: "Music/Playlists/Spring Rain"
  - Summer: "Music/Playlists/Spring Rain"
  - Fall: "Music/Playlists/Spring Rain"
  - Winter: "Music/Playlists/Winter Snow"

### heavy_inclement

- bug_spawn_multiplier: 0.3
- Music by season:
  - Spring: "Music/Playlists/Spring Rain"
  - Summer: "Music/Playlists/Spring Rain"
  - Fall: "Music/Playlists/Spring Rain"
  - Winter: "Music/Playlists/Winter Snow"

### special

No properties set — uses all defaults.

## Source Absences

- No weather descriptions or visual effects defined — only gameplay multipliers and music.
- Summer and winter have 0 special weather days despite the weather type existing.
- Inclement and heavy_inclement share the same music tracks; only the bug spawn multiplier differs (0.8 vs 0.3).
- No "heavy_special" or other weather variants exist.
- No per-location weather overrides — festivals use `forced_weather` in `festivals.toml` instead.
