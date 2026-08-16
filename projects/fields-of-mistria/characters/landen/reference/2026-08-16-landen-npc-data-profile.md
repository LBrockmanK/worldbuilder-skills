---
type: reference
title: Landen — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/landen.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:14Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/landen.toml
---

# Landen — NPC Data Profile

Source: `source/fiddle/npcs/landen.toml`

## Identity

- **Name:** Landen
- **Aldarian name:** LNDN
- **Bio:** "Suave, 'retired' carpenter who, ah, you're doing it wrong, let me show you how a pro does it! Uncle to Ryis."
- **Job:** Semi-Retired Carpenter
- **Birthday:** Fall 4
- **Tags:** townsfolk, carpenter_family
- **Dateable:** false
- **Journal background color:** [250, 223, 255] (light purple)

## Gift Preferences

**Loved gifts:** coconut_cream_pie, golden_bristle, golden_bull_horn, golden_cheesecake, golden_cookies, golden_duck_feather, golden_horse_hair, golden_feather, hard_wood, shard_mass

**Liked gifts:** basic_wood, bristle, bull_horn, canned_sardines, clay, coconut, coconut_milk, crystal, deep_sea_soup, duck_feather, glass, horse_hair, obsidian, paper, feather, ore_stone, shards, tomato_soup, vegetable_pot_pie, vegetable_soup

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** roly_poly

**Drink preferences by friendship level:**
- 6: coffee
- 12: coffee, water
- 15: wine, beer, green_bottle
- 21: whiskey, wine

## Outfits

spring, summer, autumn, winter

No special outfit variants (beach, wedding, etc.).

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

All expressions available in all 4 seasonal outfits.

No bath variant. No child portrait fallbacks.

**Gossip:** line = landen_gossip, portrait = happy, effect = hearts

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **hammer** — east only, all seasonal outfits, linear type

No bath_swim, kiss, or sleep cycles present.

## Source Absences

- No music field (no personal NPC track)
- No proposal cutscene, children, roommate routine, or carry child fields (not dateable)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
