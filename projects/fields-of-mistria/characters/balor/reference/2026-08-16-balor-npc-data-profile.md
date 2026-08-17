---
type: reference
title: Balor — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/balor.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/balor.toml
---

# Balor — NPC Data Profile

Source: `source/fiddle/npcs/balor.toml`

## Identity

- **Name:** Balor
- **Aldarian name:** BLR
- **Job:** Traveling Merchant
- **Birthday:** Summer 10
- **Tags:** townsfolk, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Balor
- **Proposal cutscene:** balor_ten_hearts
- **Children (if married):** Sterling
- **Can carry child:** false
- **Roommate routine:** balor_roommate
- **Journal background color:** [207, 211, 250] (light blue-purple)
- **Journal portrait offset:** [-115, -27]
- **Date photo offset:** [-2, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_balor
- **Small icon sprite:** spr_ui_generic_icon_npc_small_balor
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_balor

## Gift Preferences

**Loved gifts:** alda_gem_bracelet, apple_honey_curry, chili_coconut_curry, deluxe_curry, family_crest_pendant, perfect_diamond, perfect_emerald, perfect_pink_diamond, perfect_ruby, perfect_sapphire

**Liked gifts:** cauliflower_curry, chickpea_curry, crystal_rose, ore_diamond, ore_emerald, fog_orchid, frost_lily, gold_ingot, ore_gold, golden_cookies, golden_cheesecake, jasmine, perfect_gold_ore, ore_pink_diamond, rose, ore_ruby, rusted_treasure_chest, ore_sapphire, sapphire_betta, snowdrop_anemone

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** ant

**Drink preferences by friendship level:**
- 6: black_tea
- 16: beer
- 18: beer, whiskey
- 22: whiskey, wine

## Outfits

spring, summer, autumn, winter, beach, wedding

No character-specific outfit variants (unlike Celine's garden variants).

## Portrait Expressions

18 expressions available:

neutral, think, concerned, happy, wink, blush, mad, angry_blush, embarrassed, sad, ugh, sigh, sly, blush_special, hope_special, sincere_special, hurt, sad_special, bath_neutral, happy_blush, shocked, shocked_special

**Bath variant:** bath_neutral (beach outfit only)

**Outfit-restricted expressions:** hurt and sad_special are available in spring/summer/autumn/winter only (not beach). sincere_special and blush_special include wedding outfit. happy_blush includes wedding outfit.

**Gossip:** line = balor_gossip, portrait = happy, effect = hearts

## Effect Offsets

portrait = [-121, -65], sweat = [0, -9], hearts = [0, -9], angry = [0, -6], sparkles = [1, -4], sparkles_dark = [1, -4], sick = [0, -9], music_notes = [0, -4], intensity = [2, -13], surprise = [0, -4], shock = [0, -11], sigh = [-1, -6], loud = [5, -7], cheery = [-1, -4], drop = [-1, -12]

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **hair_flip** — south only, spring + beach outfits, linear
- **coin_flip** — south only, spring + summer outfits, linear
- **inspect_gem** — south only, all seasonal outfits, complex type
- **read_sit** — south only, seated, all seasonal outfits, complex type
- **jump** — east only, spring outfit, linear

## Source Absences

- No bio field present in the TOML (unlike Celine who has a bio)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
