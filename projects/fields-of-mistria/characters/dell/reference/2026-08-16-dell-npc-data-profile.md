---
type: reference
title: Dell — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/dell.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:15Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/dell.toml
---

# Dell — NPC Data Profile

Source: `source/fiddle/npcs/dell.toml`

## Identity

- **Name:** Dell
- **Aldarian name:** DL
- **Bio:** "Excitable, wildchild leader of the Dragonguard. Sister to Celine, daughter of Nora and Holt."
- **Job:** Leader of the Dragonguard
- **Birthday:** Winter 3
- **Tags:** townsfolk, general_store_family, child
- **Dateable:** false
- **Icon sprites:** spr_ui_generic_icon_npc_dell, spr_ui_generic_icon_npc_small_dell, spr_ui_generic_icon_npc_small_outline_dell
- **Journal portrait offset:** [-113, -59]
- **Journal background color:** [211, 222, 225] (light gray-blue)
- **Date photo offset:** [0, 0]

## Gift Preferences

**Loved gifts:** alda_bronze_sword, aldarian_sword, apple_juice, bullfrog, caldosian_sword, chocolate, golden_cookies, hermit_crab, ice_cream_sundae, jam_sandwich

**Liked gifts:** apple, basic_wood, blackberry, caramel_candy, cattail, clay, frog, glowberry_cookies, grape_juice, grilled_cheese, hot_cocoa, sour_lemon_cake, lemonade, lightning_dragonfly, monster_cookie, pudding, snail, ore_stone, trail_mix, turtle

**Disliked gift tags:** junk, weird_gift, caffeine, alcohol

**Hated gift:** broccoli

**Banned gift tags:** alcohol, caffeine, bomb

**Drink preferences by friendship level:**
- 6: juice
- 12: juice, lemonade
- 17: milk
- 19: milk, hot_chocolate

## Outfits

spring, summer, autumn, winter

No seasonal variants, beach, or wedding outfits.

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

No bath variant. No child portrait fallbacks listed (Dell is a child NPC).

**Gossip:** line = dell_gossip, portrait = happy, effect = hearts

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **yawn** - south only, spring outfit, complex type
- **stretch** - south only, spring outfit, complex type
- **scratch_head** - south only, spring/summer outfits, complex type
- **swing_stick** - east only, all seasonal outfits, linear type

No kiss, sleep, or bath_swim cycles (child NPC).

## Effect Offsets

portrait: [-123, -65], sweat: [-3, 28], hearts: [-3, 28], angry: [-2, 31], sparkles: [-1, 24], sparkles_dark: [-1, 24], sick: [-1, 30], music_notes: [-2, 24], intensity: [0, 23], surprise: [0, 28], shock: [0, 24], sigh: [-3, 26], loud: [4, 25], cheery: [0, 39], drop: [0, 28]

## Source Absences

- No music field (present on dateable NPCs)
- No proposal cutscene, children, roommate routine fields (child NPC)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
