---
type: reference
title: Zorel — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/zorel.toml and stores.toml:
  identity, tags, gift preferences, outfit variants, portrait expressions, animation
  cycles, vendor inventory.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/zorel.toml
- projects/fields-of-mistria/source/fiddle/stores.toml
---

# Zorel — NPC Data Profile

Source: `source/fiddle/npcs/zorel.toml`, `source/fiddle/stores.toml`

## Identity

- **Name:** Zorel
- **Aldarian name:** ZRL
- **Job:** Music Vendor
- **Birthday:** Spring 6
- **Tags:** vendor
- **Dateable:** false
- **Journal background color:** [221, 255, 238] (light green)
- **Icon sprite:** spr_ui_generic_icon_npc_zorel
- **Small icon sprite:** spr_ui_generic_icon_npc_small_zorel
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_zorel

## Gift Preferences

**Loved gifts:** middlemist, sunflower, heather, morel_mushroom

**Liked gifts:** mushroom_rice, red_toadstool, upper_mines_mushroom, glowing_mushroom, miners_mushroom_stew, wild_mushroom, dandelion, fiddlehead, nettle, wild_leek, fennel, sage

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** cicada

**Drink preferences by friendship level:**
- 6: coffee
- 17: wine

**Gossip:** line = zorel_gossip, portrait = happy, effect = hearts

## Outfits

spring, summer, autumn, winter

Four seasonal outfits only. No beach, wedding, or special variants.

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

All expressions have seasonal variants (spring, summer, autumn, winter).

## Animation Cycles

**idle:** directions north/south/east, default south, linear, pauses on speaking turn
**walk:** directions north/south/east, default south, linear, pauses on speaking turn, switches to idle on pause
**blink:** directions south/east, default south, linear
**action:** directions north/south/east, default south, linear, last frame hold 240-360, switches to idle on speaking pause
**sit:** directions north/south/east, default south, linear, seated

## Portrait and Effect Offsets

- **Portrait offset:** [-121, -65]
- **Journal portrait offset:** [-111, -32]
- **Date photo offset:** [0, 0]
- **Emote offsets:** sweat [-10, 8], hearts [-10, 8], angry [-8, 11], sparkles [-4, 3], sparkles_dark [-4, 3], sick [-6, 9], music_notes [-4, 3], intensity [-3, 0], surprise [-2, 0], shock [0, 0], sigh [-5, 5], loud [2, -2], cheery [-3, 15], drop [-6, 5]

## Vendor Inventory — Zorel's Stall

Source: `source/fiddle/stores.toml` section `[zorel]`

**Store name:** Zorel's Stall

### Constant Stock (Crystal Resonators)

Always available:
- crystal_resonator_red
- crystal_resonator_orange
- crystal_resonator_gold
- crystal_resonator_green
- crystal_resonator_blue
- crystal_resonator_purple
- crystal_resonator_silver
- crystal_resonator_black
- crystal_resonator_void
- crystal_resonator_pink

### Random Stock (Song Crystals)

5 selected per rotation (`target_selections = 5`) from the following pool:

- song_crystal_farm_boy
- song_crystal_pink_twintails
- song_crystal_crystal_caves
- song_crystal_misty_pasture
- song_crystal_purple_potions
- song_crystal_heros_journey
- song_crystal_five_more_minutes
- song_crystal_dream_lobby
- song_crystal_rainy_window
- song_crystal_adelines_theme
- song_crystal_balors_theme
- song_crystal_caldarus_theme (requires: broke_fire_seal = true)
- song_crystal_celines_theme
- song_crystal_eilands_theme
- song_crystal_haydens_theme
- song_crystal_junipers_theme
- song_crystal_marchs_theme
- song_crystal_reinas_theme
- song_crystal_ryis_theme
- song_crystal_seridias_theme (requires: seridia_transformed = true)
- song_crystal_valens_theme

### Barks

Source: `source/fiddle/barks.toml`

Zorel has a bark entry with icon `spr_ui_generic_icon_npc_small_zorel`. No bark dialogue text found in the data.
