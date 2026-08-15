---
type: reference
title: Festivals — Game Festival Definitions
description: 'Extracted festival definitions from fiddle/festivals.toml: four seasonal
  festivals with dates, locations, challenges, vendor stocks, NPC date mechanics,
  and decoration data. No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T22:16Z
resources:
- projects/fields-of-mistria/source/fiddle/festivals.toml
---

# Festivals — Game Festival Definitions

Source: `source/fiddle/festivals.toml`

## Default Properties

- date: "&lt;n/a&gt;"
- icon: "spr_illegal_16"
- name: "MISSING NAME"
- challenges: []
- decor: {}
- stocks: {}
- associated_quest: "&lt;n/a&gt;"
- npc_date: "&lt;n/a&gt;"
- forced_weather: "calm"
- location_music: {}
- daytime_music: "&lt;n/a&gt;"
- location: "&lt;n/a&gt;"
- implemented: false
- festival_post_line: "&lt;n/a&gt;"
- festival_post_sprite: "&lt;n/a&gt;"
- interact_local: "misc_local/interact_invite"
- writes: []

Source comments:
- implemented: "Whether or not we're done implementing this festival. This is so users can see them on the calendar as upcoming content, and we can keep them here, but they won't have consequences"
- festival_post_line: "this is the stringified *gameplay_triggered_conversation* name. confusing, yah?"
- writes: "if there are any writes for t2 facts, they should go here. these will be written on the day of the festival at 6am"

## Animal Festival

- date: winter, day 10
- name: "Animal Festival"
- location: "town"
- icon: "spr_ui_calendar_icon_event_animal_festival"
- forced_weather: "calm"
- implemented: true
- associated_quest: "the_animal_festival"
- festival_post_line: "animal_festival_post"
- festival_post_sprite: "spr_town_flag_post_animal_festival_winter"
- writes: [["small_animal_place", "&lt;n/a&gt;"], ["large_animal_place", "&lt;n/a&gt;"]]

### Location Music

- town: day = "Music/Location Tracks/AnimalFestival", night = "&lt;n/a&gt;"

### Decor — town

- asset_layers: ["Level_0_Assets_Animal_Festival", "Level_0_FloorSprites_Animal_Festival"]
- collision_layers: ["Animal_Festival"]
- grid_flag_edits: []

### Stocks — nora_souvenir_stall

- recipe_scroll: golden_cookies (tier 0)
- recipe_scroll: golden_cheesecake (tier 0)
- item: chicky_hot_chocolate (tier 0)
- item: cow_donut (tier 0)
- animal: chicken, cosmetic: apple (tier 0)
- animal: chicken, cosmetic: baseball_cap (tier 0)
- animal: cow, cosmetic: bell_collar (tier 0)
- animal: cow, cosmetic: laurels (tier 0)
- animal: horse, cosmetic: monocle (tier 0, requires has_unlocked_animal: horse)
- animal: horse, cosmetic: bandana (tier 0, requires has_unlocked_animal: horse)
- animal: duck, cosmetic: backwards_cap (tier 0, requires has_unlocked_animal: duck)
- animal: duck, cosmetic: strawberry_hat (tier 0, requires has_unlocked_animal: duck)
- animal: sheep, cosmetic: hot_water_bottle (tier 0, requires has_unlocked_animal: sheep)
- animal: sheep, cosmetic: green_visor (tier 0, requires has_unlocked_animal: sheep)
- animal: rabbit, cosmetic: cowboy_hat (tier 0, requires has_unlocked_animal: rabbit)
- animal: rabbit, cosmetic: chef_hat (tier 0, requires has_unlocked_animal: rabbit)
- animal: alpaca, cosmetic: beret (tier 0, requires has_unlocked_animal: alpaca)
- animal: alpaca, cosmetic: lacy_collar (tier 0, requires has_unlocked_animal: alpaca)
- animal: capybara, cosmetic: angel_wings (tier 0, requires has_unlocked_animal: capybara)
- animal: capybara, cosmetic: bat_wings (tier 0, requires has_unlocked_animal: capybara)

---

## Harvest Festival

- date: fall, day 10
- name: "Harvest Festival"
- location: "town"
- icon: "spr_ui_calendar_icon_event_harvest_festival"
- forced_weather: "special"
- implemented: true
- associated_quest: "the_harvest_festival"
- festival_post_line: "harvest_festival_post"
- festival_post_sprite: "spr_town_flag_post_harvest_festival_spring"
- interact_local: "misc_local/interact_dance"

### Location Music

- town: day = "Music/Location Tracks/HarvestFestivalTheme", night = "&lt;n/a&gt;"

### Decor — town

- asset_layers: ["Level_0_Assets_Harvest_Festival", "Level_0_FloorSprites_Harvest_Festival"]
- collision_layers: ["Harvest_Festival"]
- grid_flag_edits: []

### Challenge

- artifact_key: "harvest_festival"
- Tier results (in order):
  1. cutscene: "harvest_festival_no_place"
  2. cutscene: "harvest_festival_third_place"
  3. cutscene: "harvest_festival_second_place"
  4. cutscene: "harvest_festival_first_place"

### NPC Date — Dance

- manual: true

| NPC | Accept Line | Heart Requirement | Super Accept | Decline Line | Cutscene |
|-----|------------|-------------------|--------------|--------------|----------|
| Adeline | harvest_adeline_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Balor | harvest_balor_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Caldarus | harvest_caldarus_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Celine | harvest_celine_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Eiland | harvest_eiland_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Hayden | harvest_hayden_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Juniper | harvest_juniper_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| March | harvest_march_basic_accept | 4 | harvest_march_super_accept (heart 8 + is_partner) | harvest_festival_rejection | harvest_festival_dance |
| Reina | harvest_reina_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Ryis | harvest_ryis_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |
| Seridia | harvest_seridia_basic_accept | 6 | — | harvest_festival_rejection | harvest_festival_dance |
| Valen | harvest_valen_basic_accept | 4 | — | harvest_festival_rejection | harvest_festival_dance |

Source comment on Caldarus: "switch to new line post dt4 is handled manually, line is harvest_caldarus_basic_accept_eog"

All NPCs share the same decline_line ("harvest_festival_rejection") and friend_decline_line ("harvest_festival_friend_rejection"). All use the same cutscene ("harvest_festival_dance"). Seridia requires heart level 6 instead of 4. March is the only NPC with a super_accept (requires heart 8 and is_partner).

### Stocks — nora_souvenir_stall

- item: candied_queen_berries (tier 0)
- item: queen_berry_pie (tier 0)
- recipe_scroll: pumpkin_pie (tier 0)
- recipe_scroll: apple_honey_curry (tier 0)
- recipe_scroll: harvest_plate (tier 0)
- item: autumn_scarecrow (tier 0)
- item: cornucopia (tier 0)
- cosmetic: head_berry_crown (tier 0)
- cosmetic: head_berry_hat (tier 0)
- cosmetic: dress_berry (tier 0)
- cosmetic: suit_berry (tier 0)

---

## Shooting Star Festival

- date: summer, day 28
- name: "Shooting Star Festival"
- location: "summit"
- icon: "spr_ui_calendar_icon_event_shooting_star_festival"
- forced_weather: "calm"
- implemented: true
- associated_quest: "the_shooting_star_festival"
- festival_post_line: "shooting_star_post"
- festival_post_sprite: "spr_town_flag_post_shooting_star_festival_spring"

### Location Music

Night music "Music/Events/ShootingStarNight" applied to: town, deep_woods, farm, eastern_road, dragonsworn_glade, narrows, summit, western_ruins, beach, haydens_farm. Day music "&lt;n/a&gt;" for all.

### NPC Date — Star Watching

- item: "star_brooch"
- solo_cutscene: "shooting_star_solo"
- manual: false

| NPC | Accept Line | Heart Req | Super Accept | Super Req | Decline Line | Cutscene |
|-----|------------|-----------|--------------|-----------|--------------|----------|
| Adeline | shooting_star_adeline_basic_accept | 4 | shooting_star_adeline_super_accept | is_partner: adeline | shooting_star_adeline_decline | shooting_star_adeline |
| Balor | shooting_star_balor_basic_accept | 4 | shooting_star_balor_super_accept | is_partner: balor | shooting_star_balor_decline | shooting_star_balor |
| Caldarus | shooting_star_caldarus_basic_accept | 4 | shooting_star_caldarus_super_accept | is_partner: caldarus | shooting_star_caldarus_basic_accept | shooting_star_caldarus |
| Celine | shooting_star_celine_basic_accept | 4 | shooting_star_celine_super_accept | is_partner: celine | shooting_star_celine_decline | shooting_star_celine |
| Eiland | shooting_star_eiland_basic_accept | 4 | shooting_star_eiland_super_accept | is_partner: eiland | shooting_star_eiland_decline | shooting_star_eiland |
| Hayden | shooting_star_hayden_basic_accept | 4 | shooting_star_hayden_super_accept | is_partner: hayden | shooting_star_hayden_decline | shooting_star_hayden |
| Juniper | shooting_star_juniper_basic_accept | 4 | shooting_star_juniper_super_accept | is_partner: juniper | shooting_star_juniper_decline | shooting_star_juniper |
| March | shooting_star_march_basic_accept | 4 | shooting_star_march_super_accept | is_partner: march | shooting_star_march_decline | shooting_star_march |
| Reina | shooting_star_reina_basic_accept | 4 | shooting_star_reina_super_accept | is_partner: reina | shooting_star_reina_decline | shooting_star_reina |
| Ryis | shooting_star_ryis_basic_accept | 4 | shooting_star_ryis_super_accept | is_partner: ryis | shooting_star_ryis_decline | shooting_star_ryis |
| Seridia | shooting_star_seridia_basic_accept | 6 | shooting_star_seridia_super_accept | is_partner: seridia | shooting_star_seridia_basic_accept | shooting_star_seridia |
| Valen | shooting_star_valen_basic_accept | 4 | shooting_star_valen_super_accept | is_partner: valen | shooting_star_valen_decline | shooting_star_valen |

Source comments: Caldarus decline_line is set to basic_accept with comment "# this isn't possible". Seridia decline_line also set to basic_accept with same comment. Seridia requires heart level 6 instead of 4. Each NPC gets a unique cutscene (unlike Harvest Festival where all share one).

### Decor — town

- asset_layers: ["Level_0_Assets_Shooting_Star_Festival", "Level_0_FloorSprites_Shooting_Star_Festival"]
- collision_layers: ["Shooting_Star_Festival"]
- grid_flag_edits: 38 position entries (tile coordinate overrides, value 3)

### Decor — summit

- asset_layers: ["Level_0_Assets_Shooting_Star_Festival", "Level_0_FloorSprites_Shooting_Star_Festival"]
- collision_layers: []
- grid_flag_edits: []

---

## Spring Festival

- date: spring, day 17
- name: "Spring Festival"
- location: "town"
- icon: "spr_ui_calendar_icon_event_spring_festival"
- forced_weather: "special"
- implemented: true
- associated_quest: "the_spring_festival"
- festival_post_line: "spring_festival_post"
- festival_post_sprite: "spr_town_flag_post_spring_festival_spring"

### Location Music

- town: day = "Music/Location Tracks/SpringFestival", night = "&lt;n/a&gt;"

### Challenge

- artifact_key: "spring_festival"
- Tier results (in order):
  1. asset_layer: "Level_0_Assets_Spring_Festival_Tier_1", collision_layer: "Spring_Festival_Tier_1", cutscene: "spring_festival_no_place"
  2. cutscene: "spring_festival_third_place"
  3. asset_layer: "Level_0_Assets_Spring_Festival_Tier_2", collision_layer: "Spring_Festival_Tier_2", sprite_swaps: {spr_town_planter_barrel_spring → spr_decor_spring_festival_basket_spring}, cutscene: "spring_festival_second_place"
  4. asset_layer: "Level_0_Assets_Spring_Festival_Tier_3", collision_layer: "Spring_Festival_Tier_3", sprite_swaps: {spr_town_planter_rustic_medium_spring → spr_decor_spring_festival_large_planter_spring}, cutscene: "spring_festival_first_place"
  5. sprite_swaps: {spr_town_fountain_spring → spr_town_spring_festival_fountain_spring}, cutscene: "spring_festival_first_place_plus"

### Stocks

**maple_spring_festival:**
- item: floral_tea (tier 0)
- item: coffee (tier 0)
- item: tulip_cake (tier 2)
- item: mocha (tier 3)
- item: rose_tea (tier 3)
- item: lavender_tea (tier 4)

**nora_souvenir_stall:**
- item: scent_of_spring (tier 0)
- item: spring_festival_planter (tier 0)
- item: spring_festival_basket (tier 0)
- item: spring_festival_wreath (tier 2)
- item: spring_festival_large_planter (tier 3)
- item: spring_festival_flower_chest (tier 4)

**elsie_spring_festival:**
- cosmetic: head_flower_crown (tier 0)
- cosmetic: face_gear_flower_earrings (tier 2)
- cosmetic: dress_spring_festival (tier 3)
- cosmetic: suit_spring_festival (tier 3)
- cosmetic: head_flower_top_hat (tier 4)

### Decor — town

- asset_layers: ["Level_0_FloorSprites_Spring_Festival"]
- collision_layers: []
- grid_flag_edits: []

---

## Source Absences

- Only 4 festivals defined. No summer festival other than Shooting Star (which takes place on the last day of summer). No winter festival besides Animal Festival.
- Animal Festival has no challenges defined (only stocks). It is the only festival with no challenge/competition mechanic.
- Spring Festival has no npc_date data — it is the only implemented festival with no date mechanic.
- No festival targets locations other than "town" and "summit" (Shooting Star only).
- The `cutscenes` default property is listed in the source comment but no value is shown — field purpose unclear from this file alone.
