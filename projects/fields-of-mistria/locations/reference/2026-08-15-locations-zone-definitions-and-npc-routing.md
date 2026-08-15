---
type: reference
title: Locations — Zone Definitions and NPC Routing
description: 'Extracted zone and routing data from fiddle/t2_location_descriptions.toml:
  NPC routing overlap allowances and per-location zone definitions with named trellis
  points (seating, work stations, activity areas). No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T22:14Z
resources:
- projects/fields-of-mistria/source/fiddle/t2_location_descriptions.toml
---

# Locations — Zone Definitions and NPC Routing

Source: `source/fiddle/t2_location_descriptions.toml`

Source comment on zones: "Each zone needs to be `x.y`, where `x` is the name of a location and `y` is the name of the zone. It needs to be an array of points, and each point is just the name of the trellis point within the room `x`. Additionally, there are auto-inserted `personal.<npc>` zones, which are composed of no points themselves."

## Allowed Overlaps

NPC routing paths that are permitted to overlap:

- general_store_store/south_entrance_to_shift
- eilands_office/routine_entrance
- town/blacksmith_routine_entrance
- general_store_store/shopping_entrance
- inn/food_service_entrance
- inn/bartender_entrance
- eastern_road/north_west_routine_entrance
- town/garden_wander_entrance
- general_store_home/south_routine_entrance
- town/general_store_entrance_routine
- inn/chores_to_food_service
- town/inn_exit_routine
- town/north_west_routine_entrance
- museum_entry/south_routine_entrance
- town/hf_kitchen_entrance

## Zone Definitions

### adelines_bedroom

- **seats**: Loveseat Left Seat, Loveseat Right Seat, Armchair Seat

### adelines_office

- **room**: Left Bookshelf, Right Bookshelf, Desk Chair Seat, Pacing Left, Pacing Right, Ad Couch Top Seat, Ad Couch Middle Seat, Ad Couch Bottom Seat, chat_1, chat_2, chat_3

### bathhouse

- **cauldron**: Cauldron 1, Cauldron 2, Cauldron 3, Cauldron 4, supervisor_1, supervisor_2
- **cauldron_convo**: cauldron_convo_1, cauldron_convo_2
- **desk**: Dozy, Front Desk, customer, dozy_bed_chat_1, dozy_bed_chat_2

### bathhouse_change_room

- **seats**: Left Stool Seat, Right Stool Seat, Left Bench Left Seat, Left Bench Right Seat, Middle Bench Left Seat, Middle Bench Right Seat, Right Bench Left Seat, Right Bench Right Seat

### beach

- **campfire_benches**: Left Bench Seat, Top Bench Seat, Right Bench Seat
- **dock**: Dock Chatting 1, Dock Chatting 2
- **picnic_bench**: Picnic Bench Top Left, Picnic Bench Top Right, Picnic Bench Bottom Left, Picnic Bench Bottom Right
- **sand_castle**: sand_castle_1, sand_castle_2, sand_castle_3
- **towels**: Chat Below Towels 1, Chat Below Towels 2, Chat Below Towels 3

### blacksmith_store

- **fireplace**: Fireplace Seat Left, Fireplace Seat Right, Fireplace Stool Left
- **till**: Blacksmith Till, North Hangout
- **workbench**: Workbench Stool, Store Chatting Left, Store Chatting Right, Store Chatting Bottom

### caldarus_house

- **firepit**: Caldarus Pouf Left, Caldarus Pouf Right, tea_1, tea_2, tea_3, tea_4
- **shelf_left**: scroll_1, scroll_2, reading_1
- **shelf_right**: scroll_3, scroll_4, reading_2
- **statue**: dragon_cleaning_1, dragon_cleaning_2
- **tree_left**: tree_1, tree_2
- **tree_right**: tree_3, tree_4

### celines_room

- **living_room**: ArmChair Seat, Couch Seat Upper, Couch Seat Middle, Couch Seat Bottom

### clinic_f1

- **babysitting**: Valen Babysitting, Kids 1, Kids 2, Kids 3
- **desk**: Doctor's Desk, Valen Chatting, Bothering Valen, Check In, Prescription
- **top_bed**: Top Bed, North Bed Side

### deep_woods

- **bench**: Caldarus Bench Left, Caldarus Bench Right, lute_1
- **garden**: gardening_1 through gardening_8
- **lake**: foraging_chat_1, foraging_chat_2
- **pond_left**: pond_1 through pond_6, west_pond_convo_1, west_pond_convo_2
- **pond_right**: pond_7 through pond_12

### dells_bedroom

- **bed**: Dell Wake Point, Dell Bed
- **hanging_out**: Hanging Out 1, Hanging Out 2, Hanging Out 3

### eastern_road

- **business_check_in**: adeline_business_carpenter, business_carpenter, business_carpenter_shadow_1, business_carpenter_shadow_2, business_carpenter_shadow_3
- **foraging_chat**: foraging_chat_1, foraging_chat_2
- **pond_bench**: Bench Left, Bench Right
- **pond_north**: North Side of Pond, fishing_3
- **porch_conversation**: Porch Conversation Left, Porch Conversation Right
- **supervising**: supervising_1, supervising_extra, kids_1, kids_2, kids_3
- **tree_chat**: tree_chat_1, tree_chat_2
- **work_station**: Carpenter's Workshop Stool, Lumber 1, Porch Near Lumber, Workbench 1, Workbench 2
- **work_station_teaching**: observation_1, observation_2, observation_3, explanation

### eilands_bedroom

- **loveseat**: Loveseat Left Seat, Loveseat Right Seat

### eilands_office

- **office_chat**: office_chat_1, office_chat_2, office_chat_3, office_chat_4
- **room**: Left Cabinet, Right Cabinet, Desk Chair Seat, Pacing Left, Pacing Right, South Table, Front of Desk
- **viewing_0**: viewing_0_a, viewing_0_b
- **viewing_1**: viewing_1_a, viewing_1_b
- **viewing_2**: viewing_2_a, viewing_2_b
- **viewing_3**: viewing_3_a, viewing_3_b

### elsies_bedroom

- **seats**: Chaise Left Seat, Chaise Right Seat, Desk Chair Seat

### general_store_home

- **kids_play**: kids_play_1, kids_play_2, kids_play_3
- **living_room**: Upper Couch Left Seat, Upper Couch Middle Seat, Upper Couch Right Seat, Lower Couch Left Seat, Lower Couch Middle Seat, Lower Couch Right Seat, Armchair
- **kitchen**: Kitchen Stool Left, Kitchen Stool Right, Kitchen Counter, General Store Kitchen Mat, chores_cleaning_1, Stove
- **kitchen_table**: Kitchen Table Top Left, Kitchen Table Top Right, Kitchen Table Bottom Left, Kitchen Table Bottom Right

### general_store_store

- **north_east_shelves**: Stocking 1, Stocking 2
- **north_west_shelves**: Shopping 4, Group Chatting 1, Group Chatting 2, Group Chatting 3
- **register**: Checking Out, Dell Helping At Register, General Store Register, General Store Work Lunch, north_entrance_to_shift
- **south_east_shelves**: Shopping 1, Shopping 2

### haydens_farm

- **barn**: Hayden Chores Cows Horses, Farm Visitor 1, Farm Visitor 2
- **farm_chat**: farm_chat_1, farm_chat_2, farm_chat_3, farm_chat_4
- **foraging_chat**: foraging_chat_1, foraging_chat_2
- **statue**: statue_1, statue_2

### haydens_house

- **bench**: Bench Seat 1, Bench Seat 2, Bench Seat 3
- **living_room**: Haybale Seat 1, Haybale Seat 2, Couch Seat Left, Couch Seat Middle, Couch Seat Right
- **table**: Table Seat 1, Table Seat 2, Table Seat 3

### inn

- **balcony_dragonguard**: dragonguard_1 through dragonguard_5
- **balcony_hang**: Balcony Hang 1, Balcony Hang 2, Balcony Hang 3
- **bar**: Bottom-Middle Bar Seat, Bottom Bar Seat, Top Bar Seat, Top-Middle Bar Seat, Top Bar Hang, Bar Stand North, Bar Stand Middle, Bar Stand South, Bartender 1, Bartender 2, Bartender 3, Bartender 4
- **capital_club**: capital_club_1, capital_club_2, capital_club_3
- **kitchen**: Cutting Board, Stove-Top Kitchen, Hot Pass
- **kitchen_tutorial**: cooking_tutorial_1, cooking_tutorial_2, cooking_tutorial_3, cooking_tutorial_4
- **performance**: Jo Singing, Hemlock Playing, Second Singer
- **north_table**: North Table Bottom 1–3, North Table Left End, North Table Right End, North Table Top 1–3, fnati_art_model
- **song_listening**: Song Listening 1, Song Listening 2
- **south_table**: South Table Bottom 1–3, South Table Left End, South Table Top 1–3
- **story**: Story Listener 1–3, Storyteller, Storyteller Duo 1, Storyteller Duo 2
- **work**: work_chat_1, work_chat_2

### landens_house_f1

- **kitchen_table**: Kitchen Chair Left, Kitchen Chair Right
- **register**: Register, Register Chatting
- **shop_south**: shop_south_1, shop_south_2, shop_south_3, shop_south_4
- **tools_group**: Chatting 1, Chatting 2, Chatting 3
- **worktable**: Carpentry Point Left, Carpentry Point Right, Extra Hang

### lucs_room

- **hanging_out**: Luc Wake Point, Maple Hanging Out, Luc Bed

### manor_house_dining_room

- **table**: Table Left Seat 1–4, Table Right Seat 1–4, Standing

### manor_house_entry

- **east_chat**: east_chat_1, east_chat_2, east_chat_3, east_chat_4
- **west_chat**: west_chat_1, west_chat_2
- **couch**: Couch Left Seat, Couch Middle Seat, Couch Right Seat

### maples_room

- **hanging_out**: Luc Hanging Out, Reina_Reading, Maple Wake Point

### museum_entry

- **chat**: Museum Admiring Painting Left, Museum Admiring Painting Right, museum_conversation_shadow
- **chat_2**: chat_1, chat_2, chat_3
- **desk**: Museum Desk, museum_desk_shadow

### narrows

- **fishing**: Gathering Bait Near River, fishing_1
- **hang**: kid_group_hang_1, kid_group_hang_2, kid_group_hang_3
- **mines_chat**: mines_chat_1, mines_chat_2
- **museum_chat**: museum_chat_1, museum_chat_2
- **ruins**: archaeology_1, archaeology_2, archaeology_3, archaeology_7, North West Ruins Corner, South East Ruins Corner
- **ruins_routine**: narrows_ruins_routine_entrance, workout_0, workout_1, workout_2, workout_3
- **supervisors**: supervisor_1, supervisor_2

### terithias_house

- **couch**: Couch Seat Top, Couch Seat Middle, Couch Seat Bottom

### town

- **animal_festival_east_chat**: af_east_chat_1, af_east_chat_2
- **animal_festival_large_animal_booth**: af_large_booth_1 through af_large_booth_4
- **animal_festival_north_chat**: af_north_chat_1, af_north_chat_2, af_north_chat_3
- **animal_festival_podium**: af_podium, af_podium_chat
- **animal_festival_small_animal_booth**: af_small_booth_1 through af_small_booth_4
- **animal_festival_south_chat**: af_south_chat_1, af_south_chat_2, af_south_chat_3
- **animal_festival_souvenir_booth**: af_souvenir_booth_1 through af_souvenir_booth_4
- **animal_festival_zoo_south**: af_zoo_3, af_zoo_4, af_zoo_5
- **animal_festival_zoo_west**: af_zoo_1, af_zoo_2, af_zoo_6
- **bathhouse_exterior**: bathhouse_chat_1, bathhouse_chat_2
- **blacksmith_business**: adeline_business_blacksmith, business_blacksmith, business_blacksmith_2, business_blacksmith_shadow_1, business_blacksmith_shadow_2, business_blacksmith_shadow_3
- **blacksmith_forge**: Anvil, Forge, Anvil Olric Helping, Blacksmith Customer, Anvil Chatting 1, Anvil Chatting 2
- **bridge**: Bridge Hang Left Up, Bridge Standing Left
- **celine_bench**: Celine Cottage Bench Left, Celine Cottage Bench Right
- **celine_garden**: Celine Garden 1–4, Celine Garden Talking To, celine_garden_start
- **celine_garden_chat**: gardening_talk_1 through gardening_talk_5
- **center_square**: Maple DG Town Meet, Dell DG Town Meet, Luc DG Town Meet
- **clinic**: Conversation Outside Clinic Left, Conversation Outside Clinic Right
- **darcy_stall_chat**: market_darcy_0, market_darcy_1, market_darcy_2
- **darcy_stall_booth**: market_darcy_4, market_darcy_5
- **fishing**: River Fishing Near Celine's House, Town Fishing Friend
- **fountain_north_east**: Fountain Square Right 1–3
- **fountain_north_west**: Fountain Square Left 1–3
- **fountain_south**: Fountain Hang 1–3, Fountain Meetcute 1–2, south_fountain_1 through south_fountain_4
- **forge_lesson**: forge_observation_1, forge_observation_2, forge_observation_3, forge_explanation
- **front_of_manor**: Adeline Wake Point, Eiland Wake Point
- **gazebo**: Gazebo Hang Left, Gazebo Hang Right, Manor Gazebo
- **general_store_business**: adeline_business_general_store, business_general_store, general_store_sweep_2, business_general_store_shadow_1 through shadow_3
- **harvest_festival_chat**: hf_chat_0, hf_chat_1, hf_chat_2
- **harvest_festival_kitchen**: hf_kitchen_0, hf_kitchen_1, hf_kitchen_2, hf_kitchen_4, hf_kitchen_5, hf_kitchen_entrance
- **harvest_festival_kitchen_bar**: hf_bar_0, hf_bar_1
- **harvest_festival_kitchen_customer**: hf_kitchen_3
- **harvest_festival_kitchen_hang**: hf_kitchen_hang_0, hf_kitchen_hang_1, hf_kitchen_hang_2
- **harvest_festival_patch**: hf_patch_0, hf_patch_1, hf_patch_2, hf_patch_3
- **harvest_festival_side_chat**: hf_side_chat_0, hf_side_chat_1, hf_side_chat_2
- **harvest_festival_shopping**: hf_shopping_0, hf_shopping_1, hf_shopping_2, hf_shopping_3
- **harvest_festival_table_north_east**: hf_table_north_4, hf_table_north_5
- **harvest_festival_table_north_west**: hf_table_north_1, hf_table_north_2
- **harvest_festival_table_south_east**: hf_table_south_4, hf_table_south_5
- **harvest_festival_table_south_west**: hf_table_south_1, hf_table_south_2
- **inn_business**: adeline_business_inn, business_inn, business_inn_shadow_1, business_inn_shadow_2, business_inn_shadow_3
- **inn_yard_chat**: Inn Yard, Inn Yard Talking To
- **inn_yard_chores**: inn_yard_chores_1 through inn_yard_chores_5
- **louis_stall_chat**: market_louis_3, market_louis_4
- **louis_stall_trio**: market_louis_0, market_louis_1, market_louis_2
- **manor_flowers_north_east**: manor_gardening_3, manor_gardening_4, manor_garden_north_east, manor_garden_north_east_2
- **manor_flowers_north_west**: manor_gardening_1, manor_gardening_2, manor_garden_north_west, manor_garden_north_west_2
- **manor_flowers_south_east**: manor_gardening_7, manor_gardening_8, manor_garden_south_east, manor_garden_south_east_2
- **manor_flowers_south_west**: manor_gardening_5, manor_gardening_6, manor_garden_south_west, manor_garden_south_west_2
- **merri_stall_chat**: market_merri_3, market_merri_4, merri_packing_2
- **merri_stall_hang**: market_merri_0, market_merri_1, market_merri_2
- **mill**: Mill Inspection 1, Mill Inspection 2
- **playground**: Big Tree Left, Big Tree Right
- **playground_parent**: Playground Parent 1–4
- **playground_playdate**: Big Tree Playdate 1–4
- **quest_board**: Quest Board, Quest Board Friend
- **quest_board_looking**: Quest Board Looking 1–3
- **repair_observation**: repair_observation_1, repair_observation_2
- **repair_yard**: repair_work_1 through repair_work_5
- **shooting_star_blacksmith**: star_festival_march, star_festival_olric
- **shooting_star_carpenters_plus**: star_festival_errol, star_festival_landen, star_festival_ryis, star_festival_terithia
- **shooting_star_general_store**: star_festival_celine, star_festival_dell, star_festival_holt, star_festival_nora
- **shooting_star_inn**: star_festival_hemlock, star_festival_josephine, star_festival_luc, star_festival_maple, star_festival_reina
- **shooting_star_manor**: star_festival_adeline, star_festival_eiland, star_festival_elsie
- **shooting_star_misc_dateables**: star_festival_balor, star_festival_dozy, star_festival_hayden, star_festival_henrietta, star_festival_juniper, star_festival_valen
- **south_street_central**: Town South Meetup 1–4
- **south_street_east**: Windmill Watch 1–3
- **spring_festival_elsie_booth_shoppers**: sf_errol_booth, sf_landen_booth, sf_terithia_booth
- **spring_festival_fountain**: sf_terithia_chat, sf_valen_chat
- **spring_festival_maple_booth_shoppers**: sf_dell_booth, sf_hayden_booth, sf_henrietta_booth, sf_luc_booth
- **spring_festival_nora_booth_shoppers**: sf_balor_booth, sf_dell_booth_2, sf_march_booth
- **spring_festival_nora_booth_side**: sf_celine_booth, sf_holt_booth
- **spring_festival_podium**: sf_adeline_booth, sf_josephine_booth
- **spring_festival_stage_performers**: sf_elsie_duet, sf_hemlock_duet, sf_hemlock_play
- **spring_festival_trio**: sf_errol_chat, sf_march_chat, sf_olric_chat
- **stillwell_board_chat**: market_stillwell_1, market_stillwell_2
- **stillwell_stall_booth**: market_stillwell_0, market_stillwell_4
- **stillwell_stall_chat**: market_stillwell_3, market_stillwell_5
- **vera_stall_chat**: market_vera_0, market_vera_1
- **vera_stall_trio**: market_vera_2, market_vera_3, market_vera_4
- **taliferro_stall_chat**: market_taliferro_0, market_taliferro_1
- **taliferro_stall_trio**: market_taliferro_2, market_taliferro_3, market_taliferro_4
- **zorel_stall_trio**: market_zorel_1, market_zorel_2, market_zorel_3
- **wagon**: Bothering Balor, Wagon Meet Up 1–3
- **wheedle_stall_booth**: market_wheedle_0, market_wheedle_1, wheedle_packing_5
- **wheedle_stall_chat**: market_wheedle_2, market_wheedle_3
- **wheedle_stall_shop**: market_wheedle_4

### western_ruins

- **pit**: pit_1 through pit_4, pit_edges_1, pit_edges_2, Grid Supervisor
- **ruins_chat**: ruins_chat_1, ruins_chat_2
- **tarp**: artifacts_1, artifacts_2
- **tour**: Dig Site Tour 1–3, Dig Site Tour Guide

## Source Absences

- Despite the filename `t2_location_descriptions`, this file contains no location prose descriptions — only zone point definitions and routing overlap rules.
- Locations present in `locations.toml` that have no zone definitions in this file: aldaria, farm, summit, dragonsworn_glade, all player_home variants, all coop/barn/greenhouse variants, mini_museum, dungeon, all seal locations, priestess_quarters, narrows_secret, beach_secret, all clinic floors except clinic_f1, seridias_house, seridias_house_back, seridias_chamber, errols_bedroom, haydens_bedroom, holt_and_noras_bedroom, balors_room, reinas_room, inn_east_room, jo_and_hemlocks_room.
- No zone definitions for any mines/dungeon rooms.
- The source comments mention "auto-inserted `personal.<npc>` zones" but no explicit personal zones appear in the file — they are generated by the engine.
