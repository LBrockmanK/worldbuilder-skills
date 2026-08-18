---
type: reference
title: Darcy — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/darcy.toml and stores.toml:
  identity, tags, gift preferences, outfit variants, portrait expressions, animation
  cycles, vendor inventory.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/darcy.toml
- projects/fields-of-mistria/source/fiddle/stores.toml
- projects/fields-of-mistria/source/fiddle/barks.toml
---

# Darcy — NPC Data Profile

Source: `source/fiddle/npcs/darcy.toml`, `source/fiddle/stores.toml`

## Identity

- **Name:** Darcy
- **Aldarian name:** DRS
- **Job:** Cafe Vendor
- **Birthday:** Winter 13
- **Tags:** vendor
- **Dateable:** false
- **Journal background color:** [255, 219, 224] (light pink)
- **Icon sprites:** spr_ui_generic_icon_npc_darcy, spr_ui_generic_icon_npc_small_darcy, spr_ui_generic_icon_npc_small_outline_darcy

## Gift Preferences

**Loved gifts:** chocolate, coconut_milk, crystal_berries, golden_cheesecake, golden_cookies, golden_egg, golden_cow_milk, cow_milk, spell_fruit, sugar

**Liked gifts:** apple, blackberry, blueberry, cherry, coconut, cranberry, moon_fruit, egg, flour, glowberry, lemon, orange, peach, pear, pomegranate, strawberry, tea, wild_berries, wild_grapes, wintergreen_berry

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** ant

**Drink preferences by friendship level:**
- 6: coffee

## Outfits

spring, summer, autumn, winter

Four seasonal outfits only. No beach, wedding, or special variants.

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

All expressions have seasonal variants for spring, summer, autumn, winter.

**Gossip:** line = darcy_gossip, portrait = happy, effect = hearts

## Animation Cycles

**idle:** directions [north, south, east], default south, linear, pauses on speaking turn. All 4 seasonal outfits.

**walk:** directions [north, south, east], default south, linear, pauses on speaking turn/background to idle. All 4 seasonal outfits.

**blink:** directions [south, east], default south, linear. All 4 seasonal outfits.

**action:** directions [north, south, east], default south, linear, last frame hold 240-360, pauses on speaking to idle. All 4 seasonal outfits.

**sit:** directions [north, south, east], default south, is_seated = true, linear. All 4 seasonal outfits.

**eat:** directions [south], default south, is_seated = true, linear, last frame hold 240-360. All 4 seasonal outfits.

## Portrait Offsets

- portrait: [-125, -65]
- journal_portrait_offset: [-112, -43]
- date_photo_offset: [0, 0]

## Effect Offsets

- sweat: [-3, 6]
- hearts: [-3, -6]
- angry: [2, -9]
- sparkles: [0, 6]
- sparkles_dark: [0, 6]
- sick: [1, 14]
- music_notes: [0, 8]
- intensity: [0, 0]
- surprise: [0, 9]
- shock: [2, 5]
- sigh: [-3, 5]
- loud: [5, 8]
- cheery: [2, 10]
- drop: [0, 4]

## Vendor Inventory — Darcy's Stall

Source: `source/fiddle/stores.toml`

Store name: "Darcy's Stall"

### Category 1: Cooked Dishes

Icon: spr_ui_store_category_icon_cooked_dishes
Target selections: 10 (randomly chosen from pool each market day)

Random stock pool:
- berries_and_cream
- candied_lemon_peel
- candied_strawberries
- cherry_tart
- lemon_pie
- pudding
- salted_watermelon
- poached_pear
- peaches_and_cream
- sour_lemon_cake
- strawberries_and_cream
- wildberry_scone
- strawberry_shortcake
- caldosian_chocolate_cake (includes recipe)
- wildberry_pie
- caramelized_moon_fruit
- cranberry_orange_scone
- ice_cream_sundae (includes recipe)
- spicy_cheddar_biscuit (includes recipe)
- pumpkin_pie (includes recipe)
- cherry_cobbler (includes recipe)

### Category 2: Drinks

Icon: spr_ui_store_category_icon_drinks
Target selections: 9 (randomly chosen from pool)

Constant stock (always available):
- coffee

Random stock pool:
- cup_of_tea (includes recipe)
- hot_cocoa (includes recipe)
- lemonade (includes recipe)
- iced_coffee (includes recipe)
- espresso
- latte (includes recipe)
- mocha (includes recipe)
- green_tea (includes recipe)
- roasted_rice_tea (includes recipe)
- jasmine_tea (includes recipe)
- rose_tea
- mushroom_brew
- coconut_milk
- grape_juice (includes recipe)
- cranberry_juice
- orange_juice
- apple_juice
- pomegranate_juice (includes recipe)

### Category 3: Cooking Recipes

Icon: spr_ui_store_category_icon_cooking_recipes
Target selections: 15
Accepts recipes (recipe-only category).

### Category 4: Miscellaneous

Icon: spr_ui_crafting_category_icon_misc
Target selections: 1

Constant stock:
- espresso_machine (includes recipe, requires perk: "espresso_yourself")

## Barks

Source: `source/fiddle/barks.toml`

Darcy has an entry in the barks system with icon: spr_ui_generic_icon_npc_small_darcy. No specific bark text is included in the data file (barks are likely displayed contextually by the engine).

## Notes

- Darcy is a non-dateable vendor NPC. Her role centers on running a cafe stall at the Saturday Market.
- Gift preferences lean heavily toward baking/cooking ingredients (sugar, eggs, flour, fruits, milk, chocolate) and premium items (golden variants, crystal berries, spell fruit).
- The hated gift (ant) aligns with her food vendor role — pests near her stall.
- Coffee is the only drink preference listed, and only at friendship level 6.
- Her shop inventory is heavily dessert-and-beverage focused, fitting her cafe vendor identity.
