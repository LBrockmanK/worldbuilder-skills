---
type: reference
title: Hemlock — NPC Data
description: 'Extracted game data from source/fiddle/npcs/hemlock.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T18:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/hemlock.toml
---

# Hemlock — NPC Data

Source: `source/fiddle/npcs/hemlock.toml`

## Identity

- **Name:** Hemlock
- **Aldarian name:** HMLK
- **Bio:** Laid-back innkeeper, former touring musician. Married to Josephine, father to Reina, Luc and Maple.
- **Job:** Inn Co-Owner, Bartender
- **Birthday:** Winter 23
- **Tags:** townsfolk, inn_family
- **Dateable:** false
- **Icon sprite:** spr_ui_generic_icon_npc_hemlock
- **Small icon sprite:** spr_ui_generic_icon_npc_small_hemlock
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_hemlock
- **Journal portrait offset:** [-129, -28]
- **Journal background color:** [255, 199, 220] (pink)
- **Date photo offset:** [0, 0]

## Gossip

- **Line:** hemlock_gossip
- **Portrait:** happy
- **Effect:** hearts

## Gift Preferences

**Loved gifts:** beer, chili_coconut_curry, crayfish_etouffee, crispy_fried_earthshroom, caldosian_drinking_horn, hot_toddy, incredibly_hot_pot, white_wine, wild_grapes, spicy_corn

**Liked gifts:** basil, chili_pepper, coffee, crunchy_chickpeas, dried_squid, honey, lemon, roasted_chestnuts, rock_salt, sesame_broccoli, spicy_cheddar_biscuit, grape_juice, spicy_crab_sushi, spicy_water_chestnuts, summer_salad, tea, thyme, toasted_sunflower_seeds, trail_mix, water_chestnut_fritters

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** newt

**Drink preferences by friendship level:**
- 6: water, juice
- 16: beer
- 22: beer, coffee

## Outfits

spring, summer, autumn, winter

## Portraits

| Expression | Seasons |
|---|---|
| neutral | spring, summer, autumn, winter |
| think | spring, summer, autumn, winter |
| happy | spring, summer, autumn, winter |
| wink | spring, summer, autumn, winter |
| mad | spring, summer, autumn, winter |
| embarrassed | spring, summer, autumn, winter |
| sad | spring, summer, autumn, winter |
| ugh | spring, summer, autumn, winter |

## Portrait & Effect Offsets

- **portrait:** [-132, -65]
- **sweat:** [23, -9]
- **hearts:** [23, -9]
- **angry:** [18, -5]
- **sparkles:** [20, -1]
- **sparkles_dark:** [20, -1]
- **sick:** [24, -3]
- **music_notes:** [16, -1]
- **intensity:** [17, -12]
- **surprise:** [22, -4]
- **shock:** [23, -10]
- **sigh:** [13, -1]
- **loud:** [26, -7]
- **cheery:** [20, -2]
- **drop:** [22, -8]

## Animation Cycles

### idle
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **on_pause_speaking_turn:** true

### walk
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **on_pause_speaking_turn:** true
- **on_pause_speaking:** idle
- **on_pause_background:** idle

### blink
- **Default direction:** south
- **Directions:** south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear

### shocked
- **Default direction:** south
- **Directions:** south
- **Outfits:** spring
- **Type:** complex

### sit
- **Default direction:** south
- **Directions:** north, south, east
- **is_seated:** true
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear

### drink
- **Default direction:** south
- **Directions:** south, east, north
- **is_seated:** true
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **last_frame_hold:** [240, 360]

### eat
- **Default direction:** south
- **Directions:** south, east, north
- **is_seated:** true
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **last_frame_hold:** [240, 360]

### action
- **Default direction:** north
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **last_frame_hold:** [240, 360]
- **on_pause_speaking:** idle

### write
- **Default direction:** south
- **Directions:** south
- **Outfits:** spring, summer, autumn, winter
- **Type:** complex

### polish
- **Default direction:** east
- **Directions:** east
- **Outfits:** spring, summer, autumn, winter
- **Type:** complex

### chop
- **Default direction:** north
- **Directions:** north
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **Sound:** SoundEffects/SpecialEvents/ReinaChop
- **on_pause_speaking:** idle

### lute_play
- **Default direction:** south
- **Directions:** south
- **Outfits:** spring, summer, autumn
- **Type:** complex
- **on_pause_speaking:** idle

## Source Absences

- No `music` field (present in dateable NPC profiles like Reina)
- No `proposal_cutscene`, `children`, `can_carry_child`, or `roommate_routine` fields (consistent with dateable = false)
- The `shocked` animation cycle only has a spring outfit variant, unlike most other cycles which cover all four seasons
- The `lute_play` animation cycle covers spring, summer, autumn but not winter
- The `chop` cycle references a sound file named "ReinaChop" rather than a Hemlock-specific sound
