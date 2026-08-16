---
type: reference
title: Olric — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/olric.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:14Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/olric.toml
---

# Olric — NPC Data Profile

Source: `source/fiddle/npcs/olric.toml`

## Identity

- **Name:** Olric
- **Aldarian name:** OLRK
- **Job:** Part-Timer
- **Birthday:** Spring 10
- **Tags:** townsfolk, forge_family
- **Dateable:** false
- **Icon sprites:** spr_ui_generic_icon_npc_olric, spr_ui_generic_icon_npc_small_olric, spr_ui_generic_icon_npc_small_outline_olric
- **Journal portrait offset:** [-115, -23]
- **Journal background color:** [255, 205, 199] (light pink)
- **Date photo offset:** [0, 0]

## Gift Preferences

**Loved gifts:** perfect_copper_ore, perfect_diamond, perfect_emerald, perfect_gold_ore, perfect_iron_ore, perfect_mistril_ore, perfect_pink_diamond, perfect_ruby, perfect_sapphire, perfect_silver_ore

**Liked gifts:** ore_copper, crystal, ore_diamond, ore_emerald, ore_gold, hard_boiled_egg, ore_iron, miners_mushroom_stew, ore_mistril, obsidian, ore_pink_diamond, rock_with_a_hole, rockroot, ore_ruby, ore_sapphire, ore_silver, ore_stone, stone_horse, rock_statue, weightless_stone

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** rockbiter

**Drink preferences by friendship level:**
- 6: coffee
- 12: juice, coffee
- 16: beer
- 22: milk

## Outfits

spring, spring_bunny_ears, summer, summer_bunny_ears, autumn, autumn_bunny_ears, winter, winter_bunny_ears

Bunny-ears variant outfits exist for all 4 seasons.

## Portrait Expressions

7 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

**Neutral** has bunny-ears outfit variants (spring_bunny_ears, summer_bunny_ears, autumn_bunny_ears, winter_bunny_ears). All other expressions use seasonal outfits only (spring, summer, autumn, winter).

**Gossip:** line = olric_gossip, portrait = happy, effect = hearts

**Effect offsets defined:** sweat, hearts, angry, sparkles, sparkles_dark, sick, music_notes, intensity, surprise, shock, sigh, loud, cheery, drop

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **hammer** — east only, all seasonal outfits, sound: SoundEffects/Tools/MarchBlacksmithingHammerSwingAndHit
- **pickaxe** — east only, all seasonal outfits
- **drink_potion** — south only, all seasonal outfits
- **sweep** — south only, all seasonal outfits, complex type
- **squat** — south only, all seasonal outfits
- **lift** — south only, all seasonal outfits, complex type
- **write** — south only, all seasonal outfits, complex type
- **wipebrow** — south only, all seasonal outfits
- **tongs** — east only, all seasonal outfits, complex type
- **polish** — east only, all seasonal outfits, complex type

Idle, walk, and blink cycles include bunny-ears outfit variants. Sit, drink, eat, and action cycles use seasonal outfits only.

## Source Absences

- No bio field in source file
- No music track field
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
