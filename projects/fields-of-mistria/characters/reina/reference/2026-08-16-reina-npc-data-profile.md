---
type: reference
title: Reina — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/reina.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T12:15Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/reina.toml
---

# Reina — NPC Data Profile

Source: `source/fiddle/npcs/reina.toml`

## Identity

- **Name:** Reina
- **Aldarian name:** RN
- **Bio:** [field absent from source file]
- **Job:** Head Cook at the Inn
- **Birthday:** Fall 12
- **Tags:** townsfolk, inn_family, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Reina
- **Proposal cutscene:** reina_ten_hearts
- **Children (if married):** Cedar
- **Can carry child:** true
- **Roommate routine:** reina_roommate
- **Journal background color:** [255, 240, 208] (warm peach/cream)

## Gift Preferences

**Loved gifts:** apple_honey_curry, breaded_catfish, cabbage_slaw, ice_cream_sundae, incredibly_hot_pot, rosemary_garlic_noodles, seafood_boil, seafood_snow_pea_noodles, spell_fruit_parfait, sushi_platter

**Liked gifts:** cauliflower_curry, cheese, cod_with_thyme, coffee, crystal_berry_pie, daffodil, deep_sea_soup, flour, garlic, garlic_bread, grilled_cheese, iced_coffee, miners_mushroom_stew, pizza, rice, spicy_cheddar_biscuit, sugar, turnip_and_potato_gratin, upper_mines_mushroom, wildberry_pie

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** tunnel_millipede

**Drink preferences by friendship level:**
- 6: latte
- 12: water
- 16: wine, white_wine, rose_wine
- 20: wine, cocktail

## Outfits

spring, summer, autumn, winter, beach, wedding

Standard outfit set with beach and wedding variants. No garden-variant outfits.

## Portrait Expressions

15 expressions available:

neutral, think, happy, wink, blush, mad, embarrassed, sad, ugh, blush_special, gloomy_special, blush_open_eyes, blush_think, shocked, serious, closed_eyes, closed_eyes_blush, closed_eyes_smile, closed_eyes_smile_blush

**Bath variant:** bath_neutral (beach outfit only)

**Gossip:** line = reina_gossip, portrait = happy, effect = hearts

Notable: Reina has a `serious` expression and several `closed_eyes` variants (closed_eyes, closed_eyes_blush, closed_eyes_smile, closed_eyes_smile_blush) not present in Celine's or Nora's expression sets.

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **chop** — north only, all seasonal outfits, with sound effect (SoundEffects/SpecialEvents/ReinaChop)
- **polish** — east only, all seasonal outfits, complex type
- **write** — south only, all seasonal outfits, complex type
- **write_sit** — south only, seated, all seasonal outfits, complex type
- **read_sit** — south only, seated, all seasonal outfits, complex type

## Source Absences

- No `bio` field present in source file (Celine and Nora both have bio fields)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
