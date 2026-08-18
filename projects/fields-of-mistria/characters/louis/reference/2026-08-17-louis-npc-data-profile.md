---
type: reference
title: Louis — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/louis.toml and stores.toml:
  identity, tags, gift preferences, outfit variants, portrait expressions, animation
  cycles, vendor inventory.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/louis.toml
- projects/fields-of-mistria/source/fiddle/stores.toml
- projects/fields-of-mistria/source/fiddle/barks.toml
---

# Louis — NPC Data Profile

Source: `source/fiddle/npcs/louis.toml`, `source/fiddle/stores.toml`

## Identity

- **Name:** Louis
- **Aldarian name:** LW
- **Bio:** "Legendary tailor banished from the Capital, now a fixture of Mistria's Saturday Market."
- **Job:** Clothing Vendor
- **Birthday:** Fall 20
- **Tags:** vendor
- **Dateable:** false
- **Journal background color:** [255, 216, 254] (light pink/lavender)

## Gift Preferences

**Loved gifts:** golden_alpaca_wool, golden_bristle, golden_duck_feather, golden_feather, golden_horse_hair, golden_rabbit_wool, golden_sheep_wool, middlemist, red_wine, white_wine

**Liked gifts:** alpaca_wool, breath_of_fire, bristle, cattail, celosia, crystal, crystal_rose, duck_feather, essence_blossom, feather, cup_of_tea, frost_lily, horse_hair, lilac, marigold, rabbit_wool, shadow_flower, snapdragon, viola, sheep_wool

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** fuzzy_moth

**Drink preferences by friendship level:**
- 6: coffee
- 17: wine

## Outfits

spring, summer, autumn, winter

Four seasonal outfits only. No beach, wedding, or special variants.

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

All expressions have seasonal variants (spring, summer, autumn, winter).

**Gossip:** line = louis_gossip, portrait = happy, effect = hearts

## Animation Cycles

**idle:**
- Directions: north, south, east (default: south)
- Outfits: spring, summer, autumn, winter
- Type: linear
- on_pause_speaking_turn: true

**walk:**
- Directions: north, south, east (default: south)
- Outfits: spring, summer, autumn, winter
- Type: linear
- on_pause_speaking_turn: true
- on_pause_speaking: idle
- on_pause_background: idle

**blink:**
- Directions: south, east (default: south)
- Outfits: spring, summer, autumn, winter
- Type: linear

**action:**
- Directions: north, south, east (default: south)
- Outfits: spring, summer, autumn, winter
- Type: linear
- last_frame_hold: [240, 360]
- on_pause_speaking: idle

No west-facing direction in any cycle.

## Sprite References

- **Icon:** spr_ui_generic_icon_npc_louis
- **Small icon:** spr_ui_generic_icon_npc_small_louis
- **Small outlined icon:** spr_ui_generic_icon_npc_small_outline_louis
- **Journal portrait offset:** [-118, -36]
- **Portrait offset:** [-126, -65]
- **Date photo offset:** [0, 0]

## Effect Offsets

| Effect | Offset |
|---|---|
| sweat | [0, 9] |
| hearts | [0, 4] |
| angry | [-5, 6] |
| sparkles | [1, 9] |
| sparkles_dark | [1, 9] |
| sick | [0, 8] |
| music_notes | [-2, 5] |
| intensity | [-2, -4] |
| surprise | [-1, 6] |
| shock | [5, -8] |
| sigh | [1, -1] |
| loud | [7, -4] |
| cheery | [0, -2] |
| drop | [-3, -2] |

## Barks

Louis has an entry in barks.toml with icon `spr_ui_generic_icon_npc_small_louis`. No specific bark text lines found in the barks file beyond the icon reference.

## Vendor Inventory — Louis' Stall

Source: `source/fiddle/stores.toml` [louis]

Store name: "Louis' Stall"

### Category 1: General Clothing

Icon: `spr_ui_customization_icon_short_sleeved_tops`
Target selections: 10 (randomly selected from pool each week)

**Random stock pool:**
- dress_maid
- shoes_sneakers_basic
- face_gear_hoop_earrings
- head_lily_pad
- head_cat_ears
- skirt_pleated_short
- top_long_sleeve_striped
- head_tangerine
- skirt_long_scalloped
- head_cap_basic
- shoes_dressy_stockings
- head_devil_horns
- top_tee_oversized
- top_tanktop_buttons
- head_striped_bow
- head_striped_bucket_hat
- head_paisley_bandana
- head_sprout_hat

### Category 2: Seasonal Clothing

Icon: `spr_ui_store_category_icon_seasonal`
Target selections: 10 (randomly selected from seasonally available pool)

**Spring items:**
- head_bunny_ears
- head_strawberry_beret
- head_lemon_beret
- head_cherry_beret

**Summer items:**
- suit_halter_bikini_set
- top_halter_bikini
- shorts_swimtrunks

**Fall items:**
- head_pumpkin_beanie
- face_gear_pumpkin_earrings
- shoes_boots_pumpkin
- top_wool_lined_jacket

**Winter items:**
- head_winter_beanie
- head_ear_muffs
- top_cropped_puff_jacket
- top_puff_jacket
