---
type: reference
title: Vera — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/vera.toml and stores.toml:
  identity, tags, gift preferences, outfit variants, portrait expressions, animation
  cycles, vendor inventory.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/vera.toml
- projects/fields-of-mistria/source/fiddle/stores.toml
---

# Vera — NPC Data Profile

Source: `source/fiddle/npcs/vera.toml`, `source/fiddle/stores.toml`

## Identity

- **Name:** Vera
- **Aldarian name:** VR
- **Job:** Hairstyle & Accessory Vendor
- **Birthday:** Summer 6
- **Tags:** vendor
- **Dateable:** false
- **Journal portrait offset:** [-118, -39]
- **Journal background color:** [255, 235, 245] (light pink)
- **Date photo offset:** [0, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_vera
- **Small icon sprite:** spr_ui_generic_icon_npc_small_vera
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_vera

## Gift Preferences

**Loved gifts:** beet_soup, chili_coconut_curry, gazpacho, harvest_plate, mushroom_steak_dinner, pomegranate_sorbet, summer_salad, sweet_potato_pie, vegetable_pot_pie, winter_stew

**Liked gifts:** beet_salad, braised_burdock, cauliflower_curry, chickpea_curry, coconut_milk, cranberry_juice, crispy_fried_earthshroom, cucumber_salad, orange_juice, pomegranate, pomegranate_juice, roasted_cauliflower, salted_watermelon, sauteed_snow_peas, seaweed_salad, sesame_broccoli, simmered_daikon, steamed_broccoli, tide_salad, turnip_and_cabbage_salad

**Disliked gift tags:** junk, bugs, fishable, animal_product, weird_gift

**Hated gift:** clam

## Drink Preferences

- **6 AM:** coffee
- **17 (5 PM):** wine

## Gossip

- **Line key:** vera_gossip
- **Portrait:** happy
- **Effect:** hearts

## Outfits

- spring
- summer
- autumn
- winter

(No special outfits listed.)

## Portrait Expressions

All expressions have seasonal variants (spring, summer, autumn, winter):

- neutral
- think
- happy
- wink
- mad
- embarrassed
- sad
- ugh

## Animation Cycles

### idle
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **On pause speaking turn:** true

### walk
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **On pause speaking turn:** true
- **On pause speaking:** idle
- **On pause background:** idle

### blink
- **Default direction:** south
- **Directions:** south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear

### action
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **Last frame hold:** [240, 360]
- **On pause speaking:** idle

### sit
- **Default direction:** south
- **Directions:** north, south, east
- **Is seated:** true
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear

### eat
- **Default direction:** south
- **Directions:** south
- **Is seated:** true
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **Last frame hold:** [240, 360]

## Portrait Offsets

- portrait: [-121, -65]
- sweat: [-4, 14]
- hearts: [-4, 14]
- angry: [-6, 14]
- sparkles: [1, 6]
- sparkles_dark: [1, 6]
- sick: [-5, 16]
- music_notes: [-5, 8]
- intensity: [-2, 6]
- surprise: [-2, 6]
- shock: [7, 1]
- sigh: [-5, 10]
- loud: [11, 6]
- cheery: [3, 23]
- drop: [-3, 11]

## Vendor Inventory (Vera's Stall)

Source: `source/fiddle/stores.toml`, section `[vera]`

- **Shop name:** Vera's Stall
- **Category icon:** spr_ui_customization_icon_medium_hair
- **Stock type:** Random selection (10 items shown per visit)

**Full inventory pool:**

Hairstyles:
- hair_afro_puffs
- hair_curly_pompadour
- hair_dreadlock_twin_buns
- hair_medium_half_bun
- hair_medium_half_bun_fringe
- hair_medium_pigtails
- hair_rounded_afro
- hair_shaggy_bob
- hair_short_parted_curls
- hair_short_parted_straight
- hair_spiky
- hair_straight_buns_fringed
- hair_straight_long_twin_buns
- hair_straight_long_bun
- hair_straight_pompadour
- hair_surfer
- hair_wavy_rugged
- hair_wavy_medium_twin_buns
- hair_wavy_long_twin_buns
- hair_wavy_long_ponytail

Accessories (hair clips):
- head_clips_angel_wing
- head_clips_bat_wing
- head_clips_heart
- head_clips_moon
- head_clips_star
- head_clips_strawberry
