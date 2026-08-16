---
type: reference
title: Ryis — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/ryis.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:14Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/ryis.toml
---

# Ryis — NPC Data Profile

Source: `source/fiddle/npcs/ryis.toml`

## Identity

- **Name:** Ryis
- **Aldarian name:** RS
- **Bio:** "Quiet, chill carpenter who works at the woodshop, moved here from the Capital. Nephew of Landen."
- **Job:** Carpenter
- **Birthday:** Spring 4
- **Tags:** townsfolk, carpenter_family, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Ryis
- **Proposal cutscene:** ryis_ten_hearts
- **Children (if married):** Kam
- **Can carry child:** false
- **Roommate routine:** ryis_roommate
- **Journal background color:** [255, 173, 183] (pink)
- **Date photo offset:** [0, 0]

## Gift Preferences

**Loved gifts:** golden_bristle, golden_bull_horn, golden_cheesecake, golden_cookies, golden_duck_feather, golden_feather, golden_horse_hair, hard_wood, lobster_roll, veggie_sub_sandwich

**Liked gifts:** basic_wood, beer, bread, bristle, bull_horn, clay, cranberry_orange_scone, crystal, duck_feather, feather, garlic_bread, glass, glowberry_cookies, horse_hair, iced_coffee, lilac, obsidian, paper, ore_stone, strawberry_shortcake

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** pond_skater

**Drink preferences by friendship level:**
- 6: coffee
- 16: black_tea

## Outfits

spring, summer, autumn, winter, beach, wedding

No seasonal work-variant outfits.

## Portrait Expressions

20 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh, blush_special, sincere_special, bath_neutral, happy_blush, starry_eyed, surprised, thoughtful, thoughtful_blush, shocked, closed_eyes, closed_eyes_blush, closed_eyes_smile, closed_eyes_smile_blush

**Bath variant:** bath_neutral (beach outfit only)

**Wedding-available expressions:** neutral, think, embarrassed, blush_special, happy_blush, starry_eyed, thoughtful_blush, closed_eyes_smile_blush

**Gossip:** line = ryis_gossip, portrait = happy, effect = hearts

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **siteyesclosed** — south and east, seated, all seasonal outfits
- **saw** — east only, all seasonal outfits, pauses to idle when speaking
- **hammer** — east only, all seasonal outfits, sound effect: SoundEffects/Tools/RyisHammerSwingAndHitWood, pauses to idle when speaking
- **wipebrow** — south only, all seasonal outfits, pauses to idle when speaking/background
- **write** — south only, all seasonal outfits, complex type
- **read_sit** — south only, seated, all seasonal outfits, complex type

## Source Absences

- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
- Drink preferences have only 2 tiers (6 and 16) compared to Celine's 4 tiers; no entries at levels 12 or 20
