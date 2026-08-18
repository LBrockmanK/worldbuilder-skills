---
type: reference
title: "Luc — NPC Data"
description: "Extracted game data from source/fiddle/npcs/luc.toml: identity, tags, gift preferences, outfit variants, portrait expressions, animation cycles."
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T18:00Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/luc.toml
---

# Luc — NPC Data

Source: `source/fiddle/npcs/luc.toml`

## Identity

- **Name:** Luc
- **Aldarian name:** LK
- **Bio:** "Budding entomologist with big dreams and bigger bugs. Brother to Reina and Maple, son of Hemlock and Josephine."
- **Job:** Future Entomologist
- **Birthday:** Spring 21
- **Tags:** townsfolk, inn_family, child
- **Dateable:** false
- **Journal background color:** [255, 210, 227] (pink)
- **Journal portrait offset:** [-116, -70]
- **Date photo offset:** [0, 0]

## Sprites

- **Icon sprite:** spr_ui_generic_icon_npc_luc
- **Small icon sprite:** spr_ui_generic_icon_npc_small_luc
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_luc

## Gossip

- **Line:** luc_gossip
- **Portrait:** happy
- **Effect:** hearts

## Gift Preferences

**Loved gifts:** amber_trapped_insect, bumblebee, copper_beetle, fairy_bee, grilled_cheese, jewel_beetle, rhinoceros_beetle, roly_poly, sea_scarab, strobe_firefly

**Liked gifts:** ant, butterfly, cave_shrimp, cheese, chocolate, cricket, fuzzy_moth, hot_cocoa, hummingbird_hawk_moth, inchworm, jam_sandwich, mistmoth, monarch_butterfly, orchid_mantis, pond_skater, praying_mantis, puddle_spider, river_snail, snowball_beetle, worm

**Disliked gift tags:** junk, weird_gift, caffeine, alcohol

**Hated gift:** frog

**Banned gift tags:** alcohol, caffeine, bomb

**Drink preferences by friendship level:**
- 6: hot_chocolate
- 12: water, juice
- 17: juice
- 19: milk, hot_chocolate

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

**Portrait offset:** [-128, -65]

## Effect Offsets

| Effect | Offset |
|---|---|
| sweat | [-5, 37] |
| hearts | [-5, 37] |
| angry | [-5, 41] |
| sparkles | [0, 40] |
| sparkles_dark | [0, 40] |
| sick | [-1, 41] |
| music_notes | [0, 40] |
| intensity | [2, 28] |
| surprise | [0, 38] |
| shock | [-5, 30] |
| sigh | [5, 29] |
| loud | [-2, 32] |
| cheery | [0, 34] |
| drop | [-2, 37] |

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
- **Default direction:** south
- **Directions:** south, east, north
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **last_frame_hold:** [240, 360]
- **on_pause_speaking:** idle

### net
- **Default direction:** east
- **Directions:** east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **on_pause_speaking:** idle

### scratch_head
- **Default direction:** south
- **Directions:** south
- **Outfits:** spring, summer, autumn, winter
- **Type:** complex
- **on_pause_speaking:** idle
- **on_pause_background:** idle

## Source Absences

- No music track defined (present in dateable NPCs like Celine but absent here — consistent with `dateable = false`)
- No proposal cutscene, children, roommate routine, or partner-related fields (consistent with child NPC)
- The `shocked` cycle only has spring outfit, unlike other cycles which have all four seasons
- The `blink` cycle only supports south and east directions, fewer than most other cycles
