---
type: reference
title: World Lore — Magic, Artifacts, and Music
description: 'Broad-strokes extraction of spells.toml, artifacts.toml, and songs.toml:
  magic system, collectible lore objects, and in-world music/songs. No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T23:15Z
resources:
- projects/fields-of-mistria/source/fiddle/spells.toml
- projects/fields-of-mistria/source/fiddle/artifacts.toml
- projects/fields-of-mistria/source/fiddle/songs.toml
---

# World Lore — Magic, Artifacts, and Music

## Source: `source/fiddle/spells.toml`

### Full Restore

- **Type:** Healing
- **Cost:** 4
- **Description:** Restores all of your Stamina and HP when cast.

### Summon Rain

- **Type:** Farming
- **Cost:** 4
- **Description:** Summons a brief rain storm that waters all of your crops when cast.
- **Indoor duration:** 300
- **Indoor fade length:** 120

### Growth

- **Type:** Farming
- **Cost:** 8
- **Description:** Fully grows crops in a 3x3 area when cast. It can also progress tree growth by 1 stage.

### Dragon's Breath

- **Key:** `fire_breath`
- **Type:** Offense
- **Cost:** 8
- **Description:** Projects a stream of fire that can be used to destroy objects and monsters for a short time.

### Sacred Light

- **Type:** Utility
- **Cost:** 4
- **Description:** Illuminates dark floors in the Ruins deep underground.

### Default (placeholder)

- **Name:** `<n/a>`
- **Description:** `<n/a>`
- **Cost:** 4
- **Mana modifier:** 4
- All icon keys set to `spr_illegal_16` (placeholder sprite).

## Source: `source/fiddle/artifacts.toml`

### Rarity Vote Weights

| Rarity | Votes |
|---|---|
| Legendary | 3 |
| Rare | 6 |
| Uncommon | 9 |
| Common | 12 |

### Dig-Site Locations

Each location maps to a thematic artifact pool:

| Location key | Pool name |
|---|---|
| narrows | aldarian |
| eastern_road | caldosian |
| haydens_farm | alda |
| western_ruins | ancient |
| beach | prehistoric |
| deep_woods | deep_woods |
| dungeon | mine |
| farm | vintage_farm_tools |

### Artifact Loot Table

#### Common

- peat
- sod
- shards
- shard_mass
- clay
- rusted_shield (noted as "sunken" — 5% appearance rate)
- rock_with_a_hole (noted as "sunken" — 5% appearance rate)

#### Uncommon

- aldarian_sword
- family_crest_pendant
- caldosian_sword
- caldosian_emperor_bust
- alda_clay_pot
- alda_feather_pendant
- ancient_stone_lantern
- ancient_gold_coin
- dragon_scale
- dragon_claw
- trilobite_fossil
- amber_trapped_insect
- coin_lump
- water_sphere
- rainbow_seaweed
- criminal_confession
- petrified_wood
- gathering_basket
- rubber_fish
- giant_fish_scale

#### Rare

- aldarian_war_banner
- aldarian_gauntlet
- caldosian_breastplate
- caldosian_drinking_horn
- alda_mural_tablet
- alda_bronze_sword
- ancient_crystal_goblet
- ancient_horn_circlet
- hardened_essence
- dragon_forged_bracelet
- tiny_dinosaur_skeleton
- fossilized_egg
- rusted_treasure_chest
- mermaids_comb

#### Legendary

- lost_crown_of_aldaria
- statuette_of_caldarus
- alda_gem_bracelet
- ancient_royal_scepter
- dragon_pact_tablet
- meteorite
- fossilized_mandrake_root
- crystal_apple
- metal_leaf

#### Legendary — OOPArts

- weightless_stone
- muttering_cube
- completely_wrong_map
- black_tablet
- unknown_dragon_statuette

### Dungeon Sub-area Artifacts

#### Upper Mines

| Artifact | Rarity |
|---|---|
| miners_pickaxe | common |
| tin_lunchbox | common |
| miners_slab | uncommon |
| miners_rucksack | uncommon |
| miners_helmet | rare |

#### Tide Caverns

| Artifact | Rarity |
|---|---|
| stone_shell | common |
| starlight_coral | common |
| tidestone | uncommon |
| dense_water | uncommon |
| crab_statue | rare |

#### Deep Earth

| Artifact | Rarity |
|---|---|
| really_round_rock | common |
| seriously_square_stone | common |
| earth_infused_stone | uncommon |
| faceted_rock_gem | uncommon |
| rock_statue | rare |

#### Lava Caves

| Artifact | Rarity |
|---|---|
| fire_crystal | common |
| warm_rock | common |
| red_obsidian | uncommon |
| rainbow_geode | uncommon |
| tiny_volcano | rare |

#### Underground

| Artifact | Rarity |
|---|---|
| stone_horse | uncommon |
| flint_arrowhead | uncommon |
| obsidian_blade | rare |
| diamond_backed_mirror | rare |
| shortcut_scroll | legendary |

### Overworld Special Sets

#### Vintage Farm Tools

| Artifact | Rarity |
|---|---|
| vintage_watering_can | uncommon |
| vintage_hammer | uncommon |
| vintage_sickle | uncommon |
| vintage_brush | rare |
| vintage_cow_bell | legendary |

#### Ritual

| Artifact | Rarity |
|---|---|
| ritual_incense_burner | uncommon |
| ritual_beads | uncommon |
| ritual_chalice | uncommon |
| ritual_scepter | rare |
| ritual_tablet | rare |

#### Mist

| Artifact | Rarity |
|---|---|
| misty_black_mirror | uncommon |
| misty_feather_quill | uncommon |
| mist_crystal | uncommon |
| mist_scroll | rare |
| mist_flute | rare |

#### Fish Trap

| Artifact | Rarity |
|---|---|
| clay_amphora | common |
| sea_glass | common |
| porcelain_figurine | uncommon |
| worn_pendant | rare |
| message_in_a_bottle | legendary |

## Source: `source/fiddle/songs.toml`

All songs are collectible as song crystals (icon keys follow `spr_ui_item_song_crystal_*` pattern).

### Ambient / Location Tracks

| Key | Name | Track path |
|---|---|---|
| farm_boy | Farm Boy | Music/Crystal Tracks/FarmBoy |
| pink_twintails | Pink Twintails | Music/Crystal Tracks/PinkTwintails |
| crystal_caves | Crystal Caves | Music/Crystal Tracks/CrystalCaves |
| misty_pasture | Misty Pasture | Music/Crystal Tracks/MistyPasture |
| purple_potions | Purple Potions | Music/Crystal Tracks/PurplePotions |
| heros_journey | Hero's Journey | Music/Crystal Tracks/Hero'sJourney |
| five_more_minutes | Five More Minutes | Music/Crystal Tracks/FiveMoreMinutes |
| dream_lobby | Dream Lobby | Music/Crystal Tracks/DreamLobby |
| rainy_window | Rainy Window | Music/Crystal Tracks/RainyWindow |
| another_tower | Another Tower | Music/Location Tracks/TowerRoom |

### NPC Theme Tracks

| Key | Name (with subtitle) | Track path |
|---|---|---|
| adelines_theme | Adeline's Theme: The Smell of Drying Ink | Music/Npc Tracks/Adeline |
| balors_theme | Balor's Theme: Fair Weather | Music/Npc Tracks/Balor |
| caldarus_theme | Caldarus' Theme: The Sleeping Dragon | Music/Npc Tracks/Caldarus |
| celines_theme | Celine's Theme: Flower in Bloom | Music/Npc Tracks/Celine |
| eilands_theme | Eiland's Theme: Roots, Intertwined | Music/Npc Tracks/Eiland |
| haydens_theme | Hayden's Theme: Roll Up Your Sleeves! | Music/Npc Tracks/Hayden |
| junipers_theme | Juniper's Theme: Something's Brewing | Music/Npc Tracks/Juniper |
| marchs_theme | March's Theme: What Do You Want? | Music/Npc Tracks/March |
| reinas_theme | Reina's Theme: Wildberry Pie | Music/Npc Tracks/Reina |
| ryis_theme | Ryis' Theme: Birdsong | Music/Npc Tracks/Ryis |
| seridias_theme | Seridia's Theme: Rebirth | Music/Npc Tracks/Seridia |
| valens_theme | Valen's Theme: Cactus Blossom | Music/Npc Tracks/Valen |

## Source Absences

- **Spells:** No mana_modifier field on any spell except the placeholder default. No unlock conditions, learning prerequisites, or spell-school hierarchy. No indication of how spells are acquired.
- **Artifacts:** No display names or in-game descriptions — only internal keys. No explicit mapping from artifact keys to dig-site location pools (the location table names pools but artifact entries are not tagged to them). The "sunken" 5% modifier is a source-code comment, not a structured field. OOPArts are distinguished only by a comment, not a field.
- **Songs:** No acquisition method, unlock conditions, or in-game descriptions. No distinction between crystal-track songs and location/NPC tracks beyond the track path prefix.
