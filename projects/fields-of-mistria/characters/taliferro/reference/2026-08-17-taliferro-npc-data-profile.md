---
type: reference
title: Taliferro — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/taliferro.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/taliferro.toml
- projects/fields-of-mistria/source/fiddle/barks.toml
---

# Taliferro — NPC Data Profile

Source: `source/fiddle/npcs/taliferro.toml`

## Identity

- **Name:** Taliferro
- **Aldarian name:** TLFR
- **Job:** Chef
- **Bio:** "Celebrated chef of noble birth, hailing from the Capital and seeking to bring his exquisite cooking to the simple peasants at the Saturday Market."
- **Birthday:** Spring 13
- **Tags:** vendor
- **Dateable:** false
- **Journal background color:** [255, 227, 175] (warm peach/gold)

## Icon Sprites

- **Icon:** spr_ui_generic_icon_npc_taliferro
- **Small icon:** spr_ui_generic_icon_npc_small_taliferro
- **Small outlined icon:** spr_ui_generic_icon_npc_small_outline_taliferro

## Gift Preferences

**Loved gifts:** apple_honey_curry, beet_soup, fried_rice, harvest_plate, mont_blanc, seafood_boil, seafood_snow_pea_noodles, spell_fruit_parfait, spring_galette, sushi_platter

**Liked gifts:** chili_coconut_curry, coconut_cream_pie, crab_cakes, fish_tacos, glowberry_cookies, golden_cheesecake, golden_cookies, herb_salad, ice_cream_sundae, incredibly_hot_pot, lobster_roll, mushroom_steak_dinner, perch_risotto, pumpkin_pie, red_wine, sea_bream_rice, vegetable_pot_pie, vegetable_quiche, veggie_sub_sandwich, white_wine

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** monster_mash

**Drink preferences by friendship level:**
- 6: coffee
- 17: wine

## Gossip

- **Line:** taliferro_gossip
- **Portrait:** happy
- **Effect:** hearts

## Outfits

spring, summer, autumn, winter

No beach, wedding, or activity-variant outfits.

## Portrait Expressions

9 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh, sly

All expressions available in all 4 seasonal outfits (spring, summer, autumn, winter).

No bath variant. No child portrait fallbacks listed.

## Animation Offsets

- **Portrait:** [-125, -65]
- **Journal portrait:** [-116, -28]
- **Date photo:** [0, 0]
- **Sweat:** [-1, -3]
- **Hearts:** [-1, -3]
- **Angry:** [0, -3]
- **Sparkles:** [2, -5]
- **Sparkles dark:** [2, -5]
- **Sick:** [8, -6]
- **Music notes:** [0, -5]
- **Intensity:** [0, -13]
- **Surprise:** [2, -4]
- **Shock:** [0, -15]
- **Sigh:** [-2, -7]
- **Loud:** [4, -11]
- **Cheery:** [1, -4]
- **Drop:** [4, -13]

## Animation Cycles

**idle** — default south, directions: north/south/east, all seasonal outfits, linear type, on_pause_speaking_turn = true

**walk** — default south, directions: north/south/east, all seasonal outfits, linear type, on_pause_speaking_turn = true, on_pause_speaking = idle, on_pause_background = idle

**blink** — default south, directions: south/east, all seasonal outfits, linear type

**action** — default south, directions: north/south/east, all seasonal outfits, linear type, last_frame_hold = [240, 360], on_pause_speaking = idle

**sit** — default south, directions: north/south/east, is_seated = true, all seasonal outfits, linear type

**eat** — default south, directions: south only, is_seated = true, all seasonal outfits, linear type, last_frame_hold = [240, 360]

## Vendor Data

Taliferro appears in `barks.toml` with an icon entry: `spr_ui_generic_icon_npc_small_taliferro`.

No entry found in `stores.toml` — Taliferro does not sell items directly. His booth runs the Cooking Challenge system rather than a shop inventory.

## Source Absences

- No `music` field (no character theme track)
- No `proposal_cutscene`, `children`, `can_carry_child`, or `roommate_routine` fields (non-dateable)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
- No store inventory (runs Cooking Challenge, not a shop)
