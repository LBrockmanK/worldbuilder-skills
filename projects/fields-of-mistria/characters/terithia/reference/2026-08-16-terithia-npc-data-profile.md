---
type: reference
title: Terithia — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/terithia.toml: identity,
  tags, gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/terithia.toml
---

# Terithia — NPC Data Profile

Source: `source/fiddle/npcs/terithia.toml`

## Identity

- **Name:** Terithia
- **Aldarian name:** TRTY
- **Bio:** "Rough and tough fisherwoman and former soldier with a million stories to tell, living by the ocean."
- **Job:** Fisherwoman
- **Birthday:** Fall 22
- **Tags:** townsfolk
- **Dateable:** false
- **Icon sprite:** spr_ui_generic_icon_npc_terithia
- **Small icon sprite:** spr_ui_generic_icon_npc_small_terithia
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_terithia
- **Journal portrait offset:** [-119, -37]
- **Journal background color:** [185, 247, 255] (light blue)
- **Date photo offset:** [0, 0]

## Gift Preferences

**Loved gifts:** cod_with_thyme, fish_stew, giant_fish_scale, lobster_roll, perch_risotto, rubber_fish, sea_bream_rice, seafood_boil, seafood_snow_pea_noodles, sushi_platter

**Liked gifts:** breaded_catfish, canned_sardines, clam_chowder, crayfish_etouffee, deep_sea_soup, dried_squid, fish_skewer, fish_tacos, grilled_eel_rice_bowl, horseradish_salmon, mackerel_sashimi, pan_fried_bream, pan_fried_salmon, pan_fried_snapper, red_snapper_sushi, salmon_sashimi, sesame_tuna_bowl, smoked_trout_soup, spicy_crab_sushi, tuna_sashimi

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** fiber

**Drink preferences by friendship level:**
- 6: water, coffee
- 12: espresso
- 15: beer

## Outfits

spring, summer, autumn, winter

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

All expressions available in all 4 seasonal outfits (spring, summer, autumn, winter).

**Portrait offset:** [-125, -65]

**Effect offsets:** sweat [5, 10], hearts [5, 10], angry [1, 12], sparkles [7, 7], sparkles_dark [7, 7], sick [-2, 13], music_notes [5, 7], intensity [4, 0], surprise [7, 3], shock [11, 0], sigh [7, 4], loud [7, 5], cheery [4, 11], drop [5, 4]

**Gossip:** line = terithia_gossip, portrait = happy, effect = hearts

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **fish** — south and east, all seasonal outfits, complex type
- **bait** — south and east, all seasonal outfits, complex type

**Cycle details:**
- idle: south (default), north, south, east; linear; on_pause_speaking_turn = true
- walk: south (default), north, south, east; linear; on_pause_speaking_turn = true, on_pause_speaking = idle, on_pause_background = idle
- blink: south (default), south, east; linear
- shocked: south only, spring only; complex
- sit: south (default), north, south, east; seated; linear
- drink: south (default), south, east, north; seated; linear; last_frame_hold [240, 360]
- eat: south (default), south, east, north; seated; linear; last_frame_hold [240, 360]
- action: south (default), north, south, east; linear; last_frame_hold [240, 360]; on_pause_speaking = idle

## Source Absences

- No music field (unlike dateable characters who have NPC tracks)
- No proposal cutscene, children, roommate routine, or carry child fields (consistent with dateable = false)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
- No heart event files exist for Terithia
