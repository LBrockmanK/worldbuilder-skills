---
type: reference
title: Stillwell — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/stillwell.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles, vendor service.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/stillwell.toml
- projects/fields-of-mistria/source/fiddle/barks.toml
---

# Stillwell — NPC Data Profile

Source: `source/fiddle/npcs/stillwell.toml`

## Identity

- **Name:** Stillwell
- **Aldarian name:** STLWL
- **Job:** Fortune Telling Vendor
- **Birthday:** Winter 27
- **Tags:** vendor
- **Dateable:** false
- **Journal portrait offset:** [-134, -38]
- **Journal background color:** [202, 179, 255] (light purple)
- **Date photo offset:** [0, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_stillwell
- **Small icon sprite:** spr_ui_generic_icon_npc_small_stillwell
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_stillwell

## Gift Preferences

**Loved gifts:** ancient_crystal_goblet, black_tablet, crystal_apple, crystal_berry_pie, fog_orchid, red_wine, spell_fruit_parfait, weightless_stone, fire_crystal, completely_wrong_map

**Liked gifts:** caramelized_moon_fruit, coffee, crystal, crystal_berries, crystal_rose, crystal_wing_moth, crystal_caterpillar, crystalline_cricket, monster_cookie, obsidian, voidite, monster_mash, moon_fruit, moon_fruit_cake, muttering_cube, night_queen, poached_pear, rose, shadow_flower, spell_fruit

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** sunflower

## Drink Preferences

- **6 AM:** coffee
- **17 (5 PM):** wine

## Gossip

- **Line key:** stillwell_gossip
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
- closed_eyes

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

- portrait: [-132, -65]
- sweat: [19, 9]
- hearts: [19, 9]
- angry: [23, 13]
- sparkles: [22, 5]
- sparkles_dark: [22, 5]
- sick: [27, 6]
- music_notes: [19, 5]
- intensity: [21, 0]
- surprise: [23, 4]
- shock: [27, 5]
- sigh: [13, 6]
- loud: [30, 8]
- cheery: [22, 9]
- drop: [27, -1]

## Vendor Service

Stillwell does not appear in `stores.toml` — he has no traditional shop inventory. His vendor service is fortune-telling, delivered through the conversation system:

- **Cost:** 100 tesserae per fortune
- **Location:** Saturday Market, at booth "town/Stillwell"
- **Availability:** Saturdays only (pleasant weather), after the market plaza upgrade quest
- **Service:** Player chooses from three fortune categories: Money, Friendship, or Love
- **Fortune pool:** 8 unique fortune sets, each refreshing after 1 year
- **Denial condition:** If player has fewer than 100 tesserae, fortune is refused

## Barks

Stillwell appears in `barks.toml` with icon `spr_ui_generic_icon_npc_small_stillwell`. No bark text lines were found in the barks data beyond the icon registration.
