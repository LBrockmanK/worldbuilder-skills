---
type: reference
title: Holt — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/holt.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:14Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/holt.toml
---

# Holt — NPC Data Profile

Source: `source/fiddle/npcs/holt.toml`

## Identity

- **Name:** Holt
- **Aldarian name:** HLT
- **Job:** General Store Co-Owner
- **Birthday:** Fall 14
- **Tags:** townsfolk, general_store_family
- **Dateable:** false
- **Journal background color:** [255, 189, 145] (warm orange)

## Gift Preferences

**Loved gifts:** flour, gazpacho, hard_wood, loaded_baked_potato, baked_potato, stone_horse, narrows_moss, coffee, watermelon, wheat

**Liked gifts:** potato, beet, broccoli, cabbage, carrot, cauliflower, chili_pepper, corn, cranberry, cucumber, daikon_radish, onion, peas, pumpkin, rice_stalk, snow_peas, strawberry, sugar_cane, sweet_potato, turnip

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** puddle_spider

**Drink preferences by friendship level:**
- 6: latte, juice
- 12: lemonade
- 16: beer, green_bottle
- 20: beer, whiskey, cocktail

## Outfits

spring, summer, autumn, winter

No seasonal variants, no beach outfit, no wedding outfit.

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

No bath variant. No child portrait fallbacks.

**Gossip:** line = holt_gossip, portrait = happy, effect = hearts

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **sweep** — south only, all seasonal outfits, complex type
- **whittle** — east only, all seasonal outfits, linear type
- **write** — south only, all seasonal outfits, complex type

No sleep, kiss, or bath_swim cycles.

## Source Absences

- No `bio` field in the toml file
- No music track assignment
- No proposal cutscene, children, roommate routine, or carry-child fields (not dateable)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
