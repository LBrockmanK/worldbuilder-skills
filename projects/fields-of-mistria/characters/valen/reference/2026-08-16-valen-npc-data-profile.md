---
type: reference
title: Valen — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/valen.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:22Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/valen.toml
---

# Valen — NPC Data Profile

Source: `source/fiddle/npcs/valen.toml`

## Identity

- **Name:** Valen
- **Aldarian name:** VLN
- **Job:** Town Doctor
- **Birthday:** Fall 1
- **Tags:** townsfolk, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Valen
- **Proposal cutscene:** valen_ten_hearts
- **Children (if married):** Torin
- **Can carry child:** true
- **Roommate routine:** valen_roommate
- **Journal background color:** [220, 219, 237] (light purple)
- **Journal portrait offset:** [-112, -31]
- **Date photo offset:** [-1, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_valen
- **Small icon sprite:** spr_ui_generic_icon_npc_small_valen
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_valen

## Gift Preferences

**Loved gifts:** beet, beet_salad, beet_soup, deep_sea_soup, dragon_scale, harvest_plate, rosemary_garlic_noodles, summer_salad, sushi_platter, vegetable_soup

**Liked gifts:** coffee, cucumber, cucumber_salad, dandelion, garlic, green_tea, herb_salad, honey, nettle, pan_fried_salmon, red_wine, rose_hip, rosehip_jam, rosemary, seaweed, seaweed_salad, spring_salad, sweetroot, underseaweed, white_wine

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** red_toadstool

**Drink preferences by friendship level:**
- 6: coffee, water
- 12: water
- 14: water, green_tea
- 18: wine

## Outfits

spring, summer, autumn, winter, beach, wedding

## Portrait Expressions

18 expressions available:

neutral, raised_eyebrow, think, happy, wink, mad, embarrassed, sad, ugh, caring_special, sincere_special, neutral_blush, teary, panic, think_blush, think_smile, happy_blush

**Bath variant:** bath_neutral (beach outfit only)

**Outfit availability per expression:**
- All seasonal + beach + wedding: neutral, think, embarrassed, caring_special, teary, think_blush, happy_blush
- All seasonal + beach: raised_eyebrow, happy, wink, mad, sad, ugh, sincere_special, neutral_blush, think_smile
- All seasonal only: panic

**Gossip:** line = valen_gossip, portrait = happy, effect = hearts

## Effect Offsets

portrait [-123, -65], sweat [-6, 3], hearts [-6, 3], angry [-8, 9], sparkles [-3, 3], sparkles_dark [-3, 3], sick [-6, 6], music_notes [-3, 3], intensity [-2, -4], surprise [-7, -3], shock [-5, -6], sigh [-4, 1], loud [0, -2], cheery [-2, 1], drop [-3, 0]

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **write** -- south only, all seasonal outfits, complex type
- **write_sit** -- south only, seated, spring and summer outfits, complex type
- **charm** -- south only, spring outfit, complex type
- **heal** -- east only, all seasonal outfits, complex type, on_pause_speaking = idle
- **read_sit** -- south only, seated, all seasonal outfits, complex type

## Source Absences

- No `bio` field (present in some other NPC files, absent here)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
- No child portrait fallbacks defined (present in some other NPC files)
