---
type: reference
title: Maple — NPC Data
description: 'Extracted game data from source/fiddle/npcs/maple.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/maple.toml
---

# Maple — NPC Data

Source: `source/fiddle/npcs/maple.toml`

## Identity

- **Name:** Maple
- **Aldarian name:** MPL
- **Job:** Royalty Expert
- **Birthday:** Summer 26
- **Tags:** townsfolk, inn_family, child
- **Dateable:** false

## Sprites and UI

- **Icon sprite:** spr_ui_generic_icon_npc_maple
- **Small icon sprite:** spr_ui_generic_icon_npc_small_maple
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_maple
- **Journal portrait offset:** [-117, -61]
- **Journal background color:** [239, 196, 255] (light purple)
- **Date photo offset:** [0, 0]

## Gift Preferences

**Loved gifts:** ancient_horn_circlet, berries_and_cream, chocolate, hot_cocoa, lemon_pie, lost_crown_of_aldaria, middlemist, monarch_butterfly, mont_blanc, stone_shell

**Liked gifts:** blackberry, blue_conch_shell, cheese, daisy, glowberry_cookies, golden_cookies, grilled_cheese, ice_cream_sundae, jam_sandwich, pink_scallop_shell, pomegranate_sorbet, pudding, sand_dollar, spirula_shell, strawberry_shortcake, sunflower, trail_mix, tulip, wildberry_pie, wintergreen_ice_cream

**Disliked gift tags:** junk, bugs, weird_gift, caffeine, alcohol

**Hated gift:** peat

**Banned gift tags:** alcohol, caffeine, bomb

## Gossip

- **Line:** maple_gossip
- **Portrait:** happy
- **Effect:** hearts

## Drink Preferences

- **Hour 6:** lemonade
- **Hour 12:** water, juice
- **Hour 17:** hot_chocolate
- **Hour 19:** milk, hot_chocolate

## Outfits

spring, summer, autumn, winter

## Portraits

| Expression   | Seasonal variants                  |
|-------------|------------------------------------|
| neutral      | spring, summer, autumn, winter     |
| think        | spring, summer, autumn, winter     |
| happy        | spring, summer, autumn, winter     |
| wink         | spring, summer, autumn, winter     |
| mad          | spring, summer, autumn, winter     |
| embarrassed  | spring, summer, autumn, winter     |
| sad          | spring, summer, autumn, winter     |
| ugh          | spring, summer, autumn, winter     |

## Portrait Offsets

- **portrait:** [-130, -65]
- **sweat:** [-3, 30]
- **hearts:** [-3, 30]
- **angry:** [-1, 31]
- **sparkles:** [-1, 28]
- **sparkles_dark:** [-1, 28]
- **sick:** [-2, 32]
- **music_notes:** [-1, 28]
- **intensity:** [1, 20]
- **surprise:** [0, 29]
- **shock:** [-3, 20]
- **sigh:** [1, 25]
- **loud:** [3, 26]
- **cheery:** [0, 27]
- **drop:** [0, 32]

## Animation Cycles

**idle:** directions north/south/east, default south, type linear, all seasons. Pauses on speaking turn.

**walk:** directions north/south/east, default south, type linear, all seasons. On pause: speaking turn, speaking falls back to idle, background falls back to idle.

**blink:** directions south/east, default south, type linear, all seasons.

**shocked:** direction south only, default south, type complex, spring only.

**sit:** directions north/south/east, default south, type linear, all seasons. Seated.

**drink:** directions south/east/north, default south, type linear, all seasons. Seated. Last frame hold: [240, 360].

**eat:** directions south/east/north, default south, type linear, all seasons. Seated. Last frame hold: [240, 360].

**action:** directions south/east/north, default south, type linear, all seasons. Last frame hold: [240, 360]. On pause speaking: idle.

**play_doll:** direction south only, default south, type complex, spring/summer. On pause speaking: idle.

**scratch_head:** direction south only, default south, type complex, all seasons. On pause: speaking falls back to idle, background falls back to idle.

## Source Absences

- **No `bio` field.** Other NPC profiles (e.g., Celine) include a `bio` string; Maple's TOML has none.
- **No `music` field.** No NPC track referenced.
- **No marriage-related fields** (proposal_cutscene, children, can_carry_child, roommate_routine) — consistent with `dateable = false` and `child` tag.
