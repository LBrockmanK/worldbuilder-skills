---
type: reference
title: "Josephine — NPC Data"
description: 'Extracted game data from source/fiddle/npcs/josephine.toml: identity, tags,
  gift preferences, drink preferences, outfit variants, portrait expressions, animation
  cycles, gossip, and sprite offsets.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T20:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/josephine.toml
---

# Josephine — NPC Data

Source: `source/fiddle/npcs/josephine.toml`

## Identity

- **Name:** Josephine
- **Aldarian name:** JSFN
- **Bio:** [field absent from source file]
- **Job:** Inn Co-Owner
- **Birthday:** Summer 16
- **Tags:** townsfolk, inn_family
- **Dateable:** false
- **Icon sprite:** spr_ui_generic_icon_npc_josephine
- **Small icon sprite:** spr_ui_generic_icon_npc_small_josephine
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_josephine
- **Journal portrait offset:** [-114, -31]
- **Journal background color:** [255, 227, 200]
- **Date photo offset:** [0, 0]

## Gift Preferences

**Loved gifts:** jasmine_tea, green_tea, lavender_tea, quiche, roasted_rice_tea, rose_tea, cup_of_tea, incredibly_hot_pot, chili_coconut_curry, crayfish_etouffee

**Liked gifts:** breath_of_fire, chili_pepper, curry_powder, essence_blossom, flour, honey, jam_sandwich, jasmine, oil, rice, rose, soy_sauce, spicy_cheddar_biscuit, spicy_corn, spicy_crab_sushi, spicy_water_chestnuts, sugar, sunflower, tea, wild_berry_jam

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** worm

## Gossip

- **Line:** josephine_gossip
- **Portrait:** happy
- **Effect:** hearts

## Drink Preferences

| Time | Drinks |
|------|--------|
| 6 | black_tea, green_tea |
| 12 | lemonade, green_tea |
| 16 | wine |
| 20 | wine, cocktail |

## Outfits

spring, summer, autumn, winter

## Portraits

| Expression | Seasons |
|------------|---------|
| neutral | spring, summer, autumn, winter |
| think | spring, summer, autumn, winter |
| happy | spring, summer, autumn, winter |
| wink | spring, summer, autumn, winter |
| mad | spring, summer, autumn, winter |
| embarrassed | spring, summer, autumn, winter |
| sad | spring, summer, autumn, winter |
| ugh | spring, summer, autumn, winter |

## Sprite Offsets

- **Portrait:** [-129, -65]
- **Sweat:** [-2, 7]
- **Hearts:** [-2, 7]
- **Angry:** [-3, 11]
- **Sparkles:** [2, 4]
- **Sparkles dark:** [2, 4]
- **Sick:** [-2, 8]
- **Music notes:** [0, 4]
- **Intensity:** [2, 0]
- **Surprise:** [0, -4]
- **Shock:** [0, -6]
- **Sigh:** [4, 4]
- **Loud:** [8, 2]
- **Cheery:** [0, 11]
- **Drop:** [0, 6]

## Animation Cycles

### idle
- Default direction: south
- Directions: north, south, east
- Outfits: spring, summer, autumn, winter
- Type: linear
- on_pause_speaking_turn: true

### walk
- Default direction: south
- Directions: north, south, east
- Outfits: spring, summer, autumn, winter
- Type: linear
- on_pause_speaking_turn: true
- on_pause_speaking: idle
- on_pause_background: idle

### blink
- Default direction: south
- Directions: south, east
- Outfits: spring, summer, autumn, winter
- Type: linear

### shocked
- Default direction: south
- Directions: south
- Outfits: spring
- Type: complex

### sit
- Default direction: south
- Directions: north, south, east
- is_seated: true
- Outfits: spring, summer, autumn, winter
- Type: linear

### drink
- Default direction: south
- Directions: south, east, north
- is_seated: true
- Outfits: spring, summer, autumn, winter
- Type: linear
- last_frame_hold: [240, 360]

### eat
- Default direction: south
- Directions: south, east, north
- is_seated: true
- Outfits: spring, summer, autumn, winter
- Type: linear
- last_frame_hold: [240, 360]

### action
- Default direction: north
- Directions: north, south, east
- Outfits: spring, summer, autumn, winter
- Type: linear
- last_frame_hold: [240, 360]
- on_pause_speaking: idle

### write
- Default direction: south
- Directions: south
- Outfits: spring, summer, autumn, winter
- Type: complex

### sweep
- Default direction: south
- Directions: south
- Outfits: spring, summer, autumn, winter
- Type: complex
- on_pause_speaking: idle

### sing
- Default direction: south
- Directions: south
- Outfits: spring, summer, autumn, winter
- Type: complex
- on_pause_speaking: idle

### chop
- Default direction: north
- Directions: north
- Outfits: spring, summer, autumn, winter
- Type: linear
- Sound: SoundEffects/SpecialEvents/ReinaChop
- on_pause_speaking: idle

### polish
- Default direction: east
- Directions: east
- Outfits: spring, summer, autumn, winter
- Type: complex

## Source Absences

- **bio** field is absent (present in some other NPC TOML files)
- **music** field is absent
- **proposal_cutscene** field is absent (consistent with dateable = false)
- **child**, **can_carry_child**, **roommate_routine** fields are absent (consistent with dateable = false)
- **chop** cycle references sound path "SoundEffects/SpecialEvents/ReinaChop" — uses Reina's sound asset name, which may be a shared asset or a copy-paste artifact from the source
