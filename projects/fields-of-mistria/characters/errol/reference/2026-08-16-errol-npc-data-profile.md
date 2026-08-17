---
type: reference
title: Errol — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/errol.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/errol.toml
---

# Errol — NPC Data Profile

Source: `source/fiddle/npcs/errol.toml`

## Identity

- **Name:** Errol
- **Aldarian name:** ERL
- **Job:** Museum Curator
- **Birthday:** Winter 11
- **Tags:** townsfolk
- **Dateable:** false
- **Journal background color:** [255, 242, 205] (warm yellow)

## Icon Sprites

- **Icon:** spr_ui_generic_icon_npc_errol
- **Small icon:** spr_ui_generic_icon_npc_small_errol
- **Small outlined icon:** spr_ui_generic_icon_npc_small_outline_errol

## Gift Preferences

**Loved gifts:** baked_sweetroot, braised_burdock, clam_chowder, fish_skewer, miners_helmet, miners_mushroom_stew, pan_fried_bream, perch_risotto, shard_mass, white_wine

**Liked gifts:** apple, beer, breaded_catfish, canned_sardines, ore_copper, fish_stew, ore_gold, hot_toddy, ore_iron, ore_mistril, latte, mocha, pear, peat, pomegranate, red_wine, ore_silver, sweetroot, upper_mines_mushroom, wintergreen_ice_cream

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** hard_boiled_egg

**Drink preferences by friendship level:**
- 6: coffee, latte, water
- 12: latte, water
- 16: beer
- 20: whiskey, green_bottle

**Drink offset:** -2

## Gossip

- **Line:** errol_gossip
- **Portrait:** happy
- **Effect:** hearts

## Outfits

spring, summer, autumn, winter

No beach, wedding, or activity-variant outfits.

## Portrait Expressions

9 expressions available:

neutral, neutral_closed, think, happy, wink, mad, embarrassed, sad, ugh

All expressions available in all 4 seasonal outfits (spring, summer, autumn, winter).

No bath variant. No child portrait fallbacks listed.

## Animation Offsets

- **Portrait:** [-127, -65]
- **Journal portrait:** [-114, -32]
- **Date photo:** [0, 0]
- **Sweat:** [0, -2]
- **Hearts:** [0, -2]
- **Angry:** [-5, -5]
- **Sparkles:** [0, -5]
- **Sparkles dark:** [0, -5]
- **Sick:** [2, -4]
- **Music notes:** [0, -5]
- **Intensity:** [0, -13]
- **Surprise:** [-1, -1]
- **Shock:** [0, -7]
- **Sigh:** [4, -8]
- **Loud:** [2, -6]
- **Cheery:** [0, 0]
- **Drop:** [0, -9]

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **magnify** — south only, all seasonal outfits, complex type, on_pause_speaking = idle
- **brush** — east only, all seasonal outfits, linear type
- **pickaxe** — east only, all seasonal outfits, linear type, on_pause_speaking = idle
- **trowel** — east only, all seasonal outfits, linear type

## Source Absences

- No `bio` field (field absent from this file; present for dateable NPCs like Celine)
- No `music` field (no character theme track)
- No `proposal_cutscene`, `children`, `can_carry_child`, or `roommate_routine` fields (non-dateable)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
