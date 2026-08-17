---
type: reference
title: Juniper — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/juniper.toml: identity,
  tags, gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/juniper.toml
---

# Juniper — NPC Data Profile

Source: `source/fiddle/npcs/juniper.toml`

## Identity

- **Name:** Juniper
- **Aldarian name:** JNPR
- **Job:** Runs the Bathhouse
- **Birthday:** Fall 26
- **Tags:** townsfolk, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Juniper
- **Proposal cutscene:** juniper_ten_hearts
- **Children (if married):** Rune
- **Can carry child:** true
- **Roommate routine:** juniper_roommate
- **Journal background color:** [243, 219, 255] (light purple)
- **Journal portrait offset:** [-116, -35]
- **Date photo offset:** [-4, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_juniper
- **Small icon sprite:** spr_ui_generic_icon_npc_small_juniper
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_juniper

## Gift Preferences

**Loved gifts:** ancient_royal_scepter, black_tablet, crystal_rose, fish_tacos, golden_cookies, hardened_essence, moon_fruit_cake, mushroom_brew, pizza, spell_fruit_parfait

**Liked gifts:** crunchy_chickpeas, crystal, fog_orchid, frog, latte, middlemist, morel_mushroom, nettle, newt, night_queen, essence_blossom, poinsettia, red_toadstool, red_wine, monster_powder, shadow_flower, spell_fruit, toasted_sunflower_seeds, water_chestnut_fritters, white_wine

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** sod

**Drink preferences by friendship level:**
- 6: coffee, espresso, latte
- 12: latte
- 15: wine
- 22: absinthe, wine

## Outfits

spring, summer, autumn, winter, beach, wedding, beach_accident

The beach_accident outfit is unique to Juniper among the dateable characters.

## Portrait Expressions

27 expressions available:

neutral, think, happy, wink, laugh, wild_laugh, blush, angry_brows, embarrassed, annoyed, mad, angry_blush, unimpressed, sad, ugh, sly, sad_special, sincere_special, think_special, closed_eyes, smile, shocked, bath_neutral, happy_blush, neutral_blush, teary_blush, wild_laugh_blush

**Bath variant:** bath_neutral (beach outfit only)

**Beach accident variants:** neutral, think, closed_eyes, smile (beach_accident outfit only; smile is exclusive to beach_accident)

**Child portrait fallbacks:** laugh -> happy, wild_laugh -> happy, wild_laugh_blush -> happy

**Portrait sound overrides:** laugh = "SoundEffects/NPCs/Vocal/JuniperLaugh"

**Gossip:** line = juniper_gossip, portrait = happy, effect = hearts

## Effect Offsets

sweat = [1, 2], hearts = [1, 2], angry = [1, 6], sparkles = [4, 0], sparkles_dark = [4, 0], sick = [2, 4], music_notes = [2, 0], intensity = [3, 0], surprise = [0, 0], shock = [5, 0], sigh = [-1, 2], loud = [9, 2], cheery = [3, 9], drop = [6, -2]

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **gremlin** — east only, spring outfit
- **hair_flip** — south only, all seasonal outfits
- **spell_cast** — south only, all seasonal outfits, complex type, sound = "SoundEffects/NPCs/JuniperMagic" (detached)
- **snooze** — south only, all seasonal outfits, on_pause_speaking = sit
- **charm** — south only, spring outfit, complex type
- **laugh** — south only, all seasonal outfits, complex type
- **pose** — south only, spring outfit
- **swim_idle** — north/south/east, beach outfit
- **swim_spell_cast** — south only, beach outfit
- **transform** — south only, beach_accident outfit
- **read_sit** — south only, all seasonal outfits, complex type, seated

## Source Absences

- No bio field (present in other NPC files like Celine's)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
