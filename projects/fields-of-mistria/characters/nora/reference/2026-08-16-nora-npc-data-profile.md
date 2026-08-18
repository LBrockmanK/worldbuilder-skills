---
type: reference
title: Nora — NPC Data Profile
description: 'Extracted game data from source/fiddle/npcs/nora.toml: identity, tags,
  gift preferences, outfit variants, portrait expressions, animation cycles.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T12:15Z
resources:
- projects/fields-of-mistria/source/fiddle/npcs/nora.toml
---

# Nora — NPC Data Profile

Source: `source/fiddle/npcs/nora.toml`

## Identity

- **Name:** Nora
- **Aldarian name:** NR
- **Bio:** "Stern, business-minded shopkeep who runs the General Store. Mother to Celine and Dell, married to Holt."
- **Job:** General Store Co-Owner
- **Birthday:** Summer 24
- **Tags:** townsfolk, general_store_family
- **Dateable:** false
- **Music:** [field absent — no character music track]
- **Journal background color:** [204, 225, 255] (light blue)

## Gift Preferences

**Loved gifts:** ancient_gold_coin, cherry_cobbler, fried_rice, onion_soup, peaches_and_cream, pumpkin_stew, roasted_cauliflower, roasted_sweet_potato, sauteed_snow_peas, toasted_sunflower_seeds

**Liked gifts:** baked_potato, beet_salad, braised_burdock, braised_carrots, butter, cabbage_slaw, candied_lemon_peel, coconut_milk, coffee, cucumber_salad, grilled_corn, latte, poached_pear, salted_watermelon, sesame_broccoli, simmered_daikon, sliced_turnip, spicy_water_chestnuts, strawberries_and_cream, tomato_soup

**Disliked gift tags:** junk, bugs, weird_gift

**Hated gift:** narrows_moss

**Drink preferences by friendship level:**
- 6: latte
- 12: water
- 16: white_wine, rose_wine
- 20: white_wine, cocktail

## Outfits

spring, summer, autumn, winter

Four seasonal outfits only. No beach, wedding, or garden variants.

## Portrait Expressions

8 expressions available:

neutral, think, happy, wink, mad, embarrassed, sad, ugh

**Gossip:** line = nora_gossip, portrait = happy, effect = hearts

Smallest expression set of the three characters. No blush, gloomy, concerned, shocked, or specialty expressions.

## Animation Cycles

**Standard:** idle, walk, blink, shocked, sit, drink, eat, action

**Character-specific:**
- **sweep** — south only, all seasonal outfits, complex type
- **write_sit** — east only, seated, all seasonal outfits, complex type
- **tap** — south only, all seasonal outfits, complex type

**Absent from standard set:** kiss, sleep, bath_swim (consistent with non-dateable status)

## Source Absences

- No `music` field (Celine and Reina both have music tracks)
- No `proposal_cutscene` field (not dateable)
- No `children` field (not dateable)
- No `can_carry_child` field (not dateable)
- No `roommate_routine` field (not dateable)
- No `date_photo_offset` has value [0, 0] (placeholder — no dating functionality)
- No schedule data in this file (schedules stored separately in t2/Schedules/)
- No dialogue content (stored in t2/Conversations/)
- No physical description (appearance derived from portraits and wiki)
</content>
</invoke>
