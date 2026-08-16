---
type: reference
title: March — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/march.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:15Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/march.toml
---

# March — NPC Data Profile

Source: `source/fiddle/npcs/march.toml`

## Identity

- **Name:** March
- **Aldarian name:** MRC
- **Job:** Blacksmith
- **Birthday:** Spring 16
- **Tags:** townsfolk, dateable, forge_family
- **Dateable:** true
- **Music:** Music/Npc Tracks/March
- **Proposal cutscene:** march_ten_hearts
- **Children (if married):** Fray
- **Can carry child:** false
- **Roommate routine:** march_roommate
- **Quest turn-in greeting:** "Hey."
- **Journal background color:** [255, 203, 202] (light pink)
- **Journal portrait offset:** [-120, -28]
- **Date photo offset:** [-6, 0]
- **Icon sprites:** spr_ui_generic_icon_npc_march, spr_ui_generic_icon_npc_small_march, spr_ui_generic_icon_npc_small_outline_march

## Gift Preferences

**Loved gifts:** dragon_forged_bracelet, gold_ingot, meteorite, mistril_ingot, perfect_copper_ore, perfect_gold_ore, perfect_iron_ore, perfect_mistril_ore, perfect_silver_ore, sushi_platter

**Liked gifts:** beer, chocolate, caldosian_chocolate_cake, coffee, copper_ingot, ore_copper, ore_gold, grilled_eel_rice_bowl, hot_cocoa, iron_ingot, ore_iron, ore_mistril, mocha, perch_risotto, red_snapper_sushi, sea_bream_rice, sesame_tuna_bowl, silver_ingot, ore_silver, spicy_crab_sushi

**Disliked gift tags:** junk, bugs, archaeology, flower, forageable, weird_gift

**Hated gift:** redhead_worm

**Drink preferences by friendship level:**
- 6: hot_chocolate, water
- 16: beer, juice

## Outfits

spring, summer, autumn, winter, beach, wedding

No season-variant outfits.

## Portrait Expressions

24 standard expressions:

neutral, unimpressed, think, happy, drunk, wink, mad, embarrassed, sad, ugh, sigh, sly, tsundere, mad_special, sad_special, shock_special, sincere_special, hurt_shock, hurt_sad, hurt_sad_special, hurt_mad, hurt_tsundere, hurt_blush, hurt_blush_closed_eyes

7 additional hurt-state expressions:

hurt_closed_eyes, hurt_think, hurt_happy, hurt_happy_blush

4 eight-heart expressions:

eight_heart_happy, eight_heart_think, eight_heart_closed_eyes, eight_heart_blush

4 additional eight-heart expressions:

eight_heart_happy_blush, eight_heart_flustered

2 special expressions:

super_flustered, watery_eyes

1 wedding-only expression:

teary

**Bath variant:** bath_neutral (beach outfit only)

**Gossip:** line = march_gossip, portrait = happy, effect = hearts

**Effect offsets:** sweat [0, 1], hearts [0, 1], angry [1, 4], sparkles [6, -1], sparkles_dark [6, -1], sick [2, 0], music_notes [6, -1], intensity [5, -9], surprise [0, -3], shock [5, -8], sigh [8, -6], loud [9, -4], cheery [3, 0], drop [4, -5]

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **grumpy** -- south only, spring outfit, linear, pauses to idle on speak/background
- **wipebrow** -- south only, all seasonal outfits, linear, pauses to idle on speak/background
- **pose** -- north/south/east, spring + autumn outfits, linear, pauses to idle on speak/background
- **hammer** -- east only, all seasonal outfits, linear, sound: SoundEffects/Tools/MarchBlacksmithingHammerSwingAndHit, pauses to idle on speak
- **sigh** -- south only, spring outfit, linear, pauses to idle on speak/background
- **side_look** -- south only, spring outfit, linear, pauses to idle on speak/background
- **read_sit** -- south only, all seasonal outfits, complex type, seated
- **work_sit** -- north only, all seasonal outfits, complex type, seated

**Hurt-state cycles:**
- **hurt_idle** -- north/south/east, all seasonal outfits, linear
- **hurt_blink** -- south/east, all seasonal outfits, linear
- **hurt_walk** -- north/south/east, all seasonal outfits, linear, pauses to hurt_idle on speak/background
- **hurt_action** -- south only, all seasonal outfits, linear, pauses to hurt_idle on speak
- **hurt_sit** -- north/south/east, all seasonal outfits, seated, linear
- **hurt_sit_blink** -- south/east, all seasonal outfits, seated, linear

## Source Absences

- No bio field in the source file
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
- Drink preferences only at levels 6 and 16 (no entries at 12 or 20, unlike some other characters)
