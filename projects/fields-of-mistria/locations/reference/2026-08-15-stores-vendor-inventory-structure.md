---
type: reference
title: Stores — Vendor Inventory Structure
description: 'Broad-strokes extraction of fiddle/stores.toml: 17 stores with display
  names, category types, and notable stock patterns. Item-level detail omitted per
  user direction. No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T22:40Z
resources:
- projects/fields-of-mistria/source/fiddle/stores.toml
---

# Stores — Vendor Inventory Structure

Source: `source/fiddle/stores.toml` (1,436 lines)

Broad-strokes extraction: store names, category structure, and notable
patterns. Individual item listings omitted — consult the source file
for full inventories.

## Permanent Stores

### General Store

- Key: `general`
- Categories: Seeds (seasonal rotation by spring/summer/fall/winter), Ingredients (constant stock), Tools, Furniture
- Notable: some items gated by `repaired_general_store` requirement

### Carpenter's Shop

- Key: `carpenter`
- Categories: Materials, Furniture (oak and walnut variants), Furniture Recipes, Objects/Buildings
- Notable: some materials gated by `has_perk: steady_supplies`

### Tackle Shop

- Key: `terithia`
- Operator: Terithia
- Categories: Fishing Rods, Fish, Cooking Recipes

### Blacksmith's Shop

- Key: `blacksmith`
- Categories: Axes, Hoes, Pickaxes, Watering Cans, Shovels, Nets, Armor
- Notable: tool upgrades across quality tiers

### Hayden's Shop

- Key: `hayden`
- Operator: Hayden
- Categories: Animal Supplies, Animal Accessories, Animal Toys

### Sleeping Dragon Inn

- Key: `inn`
- Categories: Cooked Dishes, Drinks, Cooking Recipes, Furniture
- Notable: food and drink service plus recipe scrolls and inn-themed furniture

### Valen's Clinic

- Key: `valens_clinic`
- Operator: Valen
- Categories: generic (no category icon specified)
- Notable: smallest store in the file (12 lines)

## Market Stalls (Vendor NPCs)

### Louis' Stall

- Key: `louis`
- Operator: Louis
- Categories: Clothing (seasonal rotation)

### Vera's Stall

- Key: `vera`
- Operator: Vera
- Categories: Cosmetics / Hair Accessories

### Darcy's Stall

- Key: `darcy`
- Operator: Darcy
- Categories: Cooked Dishes, Drinks, Miscellaneous

### Merri's Stall

- Key: `merri`
- Operator: Merri
- Categories: Furniture, Decorative Items, Furniture Recipes
- Notable: large inventory (258 lines) — extensive furniture and decor catalog

### Wheedle's Stall

- Key: `wheedle`
- Operator: Wheedle
- Categories: Consumables

### Zorel's Stall

- Key: `zorel`
- Operator: Zorel
- Categories: Consumables

### Balor's Wagon

- Key: `balor`
- Operator: Balor
- Categories: Materials, Furniture, Furniture Recipes, Player Cosmetics, Cooked Dishes, Ingredients, Seeds
- Notable: largest store in the file (364 lines) — broadest category range of any vendor; functions as a traveling general merchant

## Festival Stalls

These stores are only active during the Spring Festival (defined in `festivals.toml`).

### Food Stall

- Key: `maple_spring_festival`
- Operator: Maple

### Souvenir Stall

- Key: `nora_souvenir_stall`
- Operator: Nora

### Clothing Stall

- Key: `elsie_spring_festival`
- Operator: Elsie

## Source Absences

- No store location mappings in this file — which store is at which game location is not declared here (cross-reference `locations.toml` building assignments and NPC data).
- No pricing data — items are referenced by key only, prices presumably defined elsewhere.
- No store hours or availability schedules.
- Festival vendor stocks for Harvest Festival and Animal Festival are defined in `festivals.toml`, not here — only Spring Festival stalls appear in this file.
- Nora operates both a permanent souvenir stall at festivals (in `festivals.toml`) and a Spring Festival souvenir stall here — stock differs between them.
