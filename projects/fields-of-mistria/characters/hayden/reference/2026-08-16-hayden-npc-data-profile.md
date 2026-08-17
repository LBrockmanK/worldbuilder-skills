---
type: reference
title: Hayden — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/hayden.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:22Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/hayden.toml
---

# Hayden — NPC Data Profile

Source: `source/fiddle/npcs/hayden.toml`

## Identity

- **Name:** Hayden
- **Aldarian name:** HDN
- **Job:** Runs Sweetwater Farm
- **Birthday:** Winter 8
- **Tags:** townsfolk, dateable
- **Dateable:** true
- **Music:** Music/Npc Tracks/Hayden
- **Proposal cutscene:** hayden_ten_hearts
- **Children (if married):** Wilder
- **Can carry child:** false
- **Roommate routine:** hayden_roommate
- **Journal background color:** [255, 219, 169] (warm peach/tan)
- **Journal portrait offset:** [-112, -15]
- **Date photo offset:** [2, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_hayden
- **Small icon sprite:** spr_ui_generic_icon_npc_small_hayden
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_hayden

No `bio` field present in source file.

## Gift Preferences

**Loved gifts:** golden_butter, golden_cheese, golden_duck_egg, golden_duck_mayonnaise, golden_egg, golden_mayonnaise, golden_cow_milk, pumpkin_pie, stone_horse, vegetable_quiche

**Liked gifts:** apple_pie, butter, cheese, coconut_cream_pie, coffee, crystal_berry_pie, duck_egg, duck_mayonnaise, egg, lemon_pie, loaded_baked_potato, mayonnaise, cow_milk, mushroom_steak_dinner, pumpkin_stew, quiche, sweet_potato_pie, cup_of_tea, vegetable_pot_pie, wildberry_pie

**Disliked gift tags:** junk, bugs, fishy, weird_gift

**Hated gift:** sushi_platter

**Drink preferences by friendship level:**
- 6: coffee, water, juice
- 16: beer
- 22: green_tea

**Drink offset:** -2

## Gossip

- **Line:** hayden_gossip
- **Portrait:** happy
- **Effect:** hearts

## Outfits

spring, summer, autumn, winter, beach, wedding

No garden-variant outfits.

## Portrait Expressions

26 expressions available:

neutral, neutral_arm_down, neutral_fist, think, happy, happy_arm_down, happy_fist, wink, wink_arm_down, wink_fist, laugh, blush, embarrassed, annoyed, mad, gloomy, sad, sweat, ugh, think_special, shy_special, confident_blush, happy_arm_down_blush, shocked, laugh_blush, bath_neutral

**Bath variant:** bath_neutral (beach outfit only)

**Child portrait fallbacks:** laugh → happy_arm_down, embarrassed → happy_arm_down_blush, sweat → happy_arm_down, laugh_blush → happy_arm_down_blush

**Portrait offset:** [-121, -65]

**Effect offsets:**
- sweat: [-8, -18]
- hearts: [-8, -18]
- angry: [-7, -17]
- sparkles: [0, -13]
- sparkles_dark: [0, -13]
- sick: [-1, -15]
- music_notes: [-2, -13]
- intensity: [0, -22]
- surprise: [27, -4]
- shock: [0, -24]
- sigh: [0, -17]
- loud: [5, -15]
- cheery: [0, -14]
- drop: [-1, -25]

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, kiss, action, sleep, bath_swim

**Character-specific:**
- **sigh** — south only, spring outfit
- **wipebrow** — south only, all seasonal outfits
- **pet** — east only, spring outfit
- **till** — east only, all seasonal outfits
- **hammer** — east only, all seasonal outfits, sound: SoundEffects/Tools/RyisHammerSwingAndHitWood
- **water** — east only, all seasonal outfits
- **harvest** — east only, all seasonal outfits
- **read_sit** — south only, all seasonal outfits, complex type, seated

**Riding cycles (spring outfit only):**
- **ride_idle_1** — north/south/east
- **ride_idle_2** — north/south/east
- **ride_idle_3** — east only
- **ride_blink** — south/east
- **ride_walk** — north/south/east, sound: SoundEffects/Animals/HorseFootsteps/HorseFootstepWalkGrass
- **ride_run** — north/south/east, sound: SoundEffects/Animals/HorseFootsteps/HorseFootstepGallopGrass
- **ride_jump** — north/south/east

## Source Absences

- No `bio` field (present for some other NPCs such as Celine)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
