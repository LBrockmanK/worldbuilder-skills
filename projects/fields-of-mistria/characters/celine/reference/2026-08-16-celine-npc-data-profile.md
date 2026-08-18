---
type: reference
title: Celine — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/celine.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T12:15Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/celine.toml
---

# Celine — NPC Data Profile

Source: `source/fiddle/npcs/celine.toml`

## Identity

- **Name:** Celine
- **Aldarian name:** SLN
- **Bio:** "Sweet, bookish gardener who works part-time at her parents' General Store. Daughter of Nora and Holt, sister to Dell."
- **Job:** Gardener, Part-Timer
- **Birthday:** Summer 14
- **Tags:** townsfolk, general_store_family, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Celine
- **Proposal cutscene:** celine_ten_hearts
- **Children (if married):** Rowan
- **Can carry child:** true
- **Roommate routine:** celine_roommate
- **Journal background color:** [215, 249, 246] (light teal)

## Gift Preferences

**Loved gifts:** breath_of_fire, crystal_rose, essence_blossom, frost_lily, hydrangea, middlemist, plum_blossom, rose, snowdrop_anemone, temple_flower

**Liked gifts:** catmint, celosia, chrysanthemum, cosmos, crocus, daffodil, daisy, dandelion, heather, iris, jasmine, lilac, marigold, poinsettia, rose_tea, snapdragon, spring_salad, sunflower, tulip, viola

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** caterpillar

**Drink preferences by friendship level:**
- 6: black_tea, green_tea
- 12: green_tea, lemonade
- 16: wine, white_wine, rose_wine
- 20: wine, cocktail

## Outfits

spring, spring_garden, summer, summer_garden, autumn, autumn_garden, winter, beach, wedding

Garden-variant outfits (spring_garden, summer_garden, autumn_garden) are unique to Celine among Batch 2 characters.

## Portrait Expressions

22 expressions available:

neutral, think, happy, wink, very_happy, blush, embarrassed, blush_closed_eyes, blush_special, annoyed, mad, angry_blush, gloomy, concerned, sad, laugh, sweat, ugh, think_special, teary_special, shy_blush, shocked

**Bath variant:** bath_neutral (beach outfit only)

**Child portrait fallbacks:** very_happy → happy, blush → blush_closed_eyes, mad → annoyed, concerned → gloomy, sad → gloomy, ugh → gloomy

**Gossip:** line = celine_gossip, portrait = happy, effect = hearts

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **herb** — south only, spring outfit
- **book_stand** — south only, all seasonal outfits, complex type
- **book_sit** — south only, seated, all seasonal outfits, complex type
- **sweep** — south only, all seasonal outfits, complex type
- **harvest** — east only, garden outfits + winter
- **water** — east only, all seasonal outfits + garden variants

## Source Absences

- No `bio` field discrepancy (present and populated)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
