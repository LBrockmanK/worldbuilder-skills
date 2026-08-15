---
type: reference
title: Locations — Game Location Definitions
description: 'Extracted location definitions from fiddle/locations.toml: all game
  locations with their properties (names, indoor/outdoor, map relationships, music,
  building assignments, gameplay parameters). No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T22:12Z
resources:
- projects/fields-of-mistria/source/fiddle/locations.toml
---

# Locations — Game Location Definitions

Source: `source/fiddle/locations.toml`

## Default Properties

Properties applied to any location that omits them.

- name: "MISSING NAME"
- forageables: 2
- bugs: 2
- gm_room: "&lt;..&gt;" (auto-detect from location name)
- outdoor: false
- bug_tag: false
- farm: false
- map_location: "&lt;..&gt;" (uses the location itself)
- music: "&lt;n/a&gt;"
- ambience: "&lt;n/a&gt;"
- npc_farm: false
- dig_sites: 0
- special_dig_sites: 0
- serializable: false
- reset_every_night: false
- inhibit_music: false
- bird_count: false
- npa_spawn_points: []
- replace_tilemaps: true
- ignore_seasons: false
- lost_and_found: true
- mist_sights: false

Source comments on defaults:
- forageables: "only applies to outdoor rooms"
- bugs: "only applies to outdoor rooms"
- npc_farm: "this means Npcs farm here (Celine, Hayden)"
- dig_sites: "only outdoor, non-farm rooms should have a non-zero value"
- special_dig_sites: "this should be 0 for everyone but the WesternRuins"
- bird_count: "set this to a non-false array ([3, 4] for example) to start getting birbs"
- ignore_seasons: "whether or not we care about seasonality for crops, commonly used in greenhouses"

## aldaria

No properties set — uses all defaults.

## farm

- outdoor: true
- bug_tag: ["standard", "water_bug"]
- bug_water_boxes: [[[118, 120], [256, 130]], [[116, 24], [178, 120]]]
- serializable: true
- farm: true
- forageables: 0
- bird_count: [0, 2]
- bugs: 3
- safe_position: [1032, 124]

## town

- name: "Mistria"
- serializable: true
- outdoor: true
- bug_tag: ["standard", "water_bug"]
- bug_water_boxes: [[[208, 18], [218, 306]], [[72, 312], [240, 348]]]
- dig_sites: 1
- forageables: 1
- npc_farm: true
- reset_every_night: true
- bird_count: [0, 2]
- bugs: 5
- mist_sights: [[1928.0, 1128.0], [1864.0, 2200.0], [1000.0, 2352.0], [344.0, 1128.0], [424.0, 2152.0], [1288.0, 2696.0]]
- safe_position: [1096, 1080]

## bathhouse

- name: "Bathhouse"
- map_location: "town"
- music: "Music/Location Tracks/Bathhouse"
- building: "bathhouse"

## bathhouse_bedroom

- map_location: "town"
- music: "Music/Location Tracks/Bathhouse"
- building: "bathhouse"

## bathhouse_change_room

- map_location: "town"
- music: "Music/Location Tracks/Bathhouse"
- building: "bathhouse"

## bathhouse_bath

- map_location: "town"
- music: "Music/Location Tracks/Bathhouse"
- building: "bathhouse"

## bell_tower_f1

- name: "Bell Tower"
- map_location: "town"
- building: "bell_tower"

## bell_tower_f2

- map_location: "town"
- building: "bell_tower"

## caldarus_house

- name: "Caldarus' House"
- music: "Music/Location Tracks/Deep Woods"
- map_location: "deep_woods"
- building: "caldarus_house"

## eastern_road

- name: "The Eastern Road"
- serializable: true
- outdoor: true
- bug_tag: ["standard", "water_bug"]
- bug_water_boxes: [[[32, 200], [68, 236]], [[50, 260], [78, 274]], [[110, 258], [120, 270]], [[152, 28], [166, 128]], [[150, 130], [198, 142]]]
- dig_sites: 1
- forageables: 2
- reset_every_night: true
- bugs: 4
- bird_count: [0, 2]
- mist_sights: [[728.0, 1544.0], [1080.0, 1320.0], [280.0, 808.0], [184.0, 2072.0], [952.0, 536.0], [872.0, 776.0], [432.0, 1552.0]]
- safe_position: [800, 1472]

## deep_woods

- name: "The Deep Woods"
- serializable: true
- forageables: 2
- bugs: 3
- outdoor: true
- bug_tag: ["deep_woods"]
- dig_sites: 1
- music: "Music/Location Tracks/Deep Woods"
- reset_every_night: true
- bird_count: [2, 5]
- mist_sights: [[1272.0, 1368.0], [2200.0, 1320.0]]
- safe_position: [1344, 1328]

## dragonsworn_glade

- name: "The Dragonsworn Glade"
- serializable: true
- forageables: 0
- bugs: 1
- outdoor: true
- bug_tag: ["deep_woods"]
- dig_sites: 0
- music: "Music/Location Tracks/Deep Woods"
- reset_every_night: true
- bird_count: [0, 1]
- safe_position: [1208, 1200]

## narrows

- name: "The Narrows"
- serializable: true
- bugs: 2
- outdoor: true
- bug_tag: ["standard", "water_bug"]
- bug_water_boxes: [[[56, 16], [64, 120]], [[104, 158], [182, 172]]]
- dig_sites: 1
- forageables: 2
- reset_every_night: true
- npc_farm: true
- bird_count: [0, 2]
- mist_sights: [[216.0, 616.0], [952.0, 440.0], [1272.0, 744.0], [1400.0, 1560.0], [1192.0, 1112.0], [1016.0, 584.0]]
- safe_position: [1350, 880]

## player_home

- name: "Home"
- serializable: true
- gm_room: "rm_farmhouse"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104
- music.day: "Music/Location Tracks/Player Home Day"
- music.night: "Music/Location Tracks/Player Home Night"

## player_home_west

- name: "Western Wing"
- serializable: true
- gm_room: "rm_farmhouse_west"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104
- music.day: "Music/Location Tracks/Player Home Day"
- music.night: "Music/Location Tracks/Player Home Night"

## player_home_east

- name: "Eastern Wing"
- serializable: true
- gm_room: "rm_farmhouse_east"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104
- music.day: "Music/Location Tracks/Player Home Day"
- music.night: "Music/Location Tracks/Player Home Night"

## player_home_north

- name: "Northern Wing"
- serializable: true
- gm_room: "rm_farmhouse_north"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104

## player_home_upper_central

- name: "Home, Upper Floor"
- serializable: true
- gm_room: "rm_farmhouse_upper"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104
- music.day: "Music/Location Tracks/Player Home Day"
- music.night: "Music/Location Tracks/Player Home Night"

## player_home_upper_west

- name: "Western Wing, Upper Floor"
- serializable: true
- gm_room: "rm_farmhouse_west_upper"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104
- music.day: "Music/Location Tracks/Player Home Day"
- music.night: "Music/Location Tracks/Player Home Night"

## player_home_upper_east

- name: "Eastern Wing, Upper Floor"
- serializable: true
- gm_room: "rm_farmhouse_east_upper"
- map_location: "farm"
- building: "player_home"
- lost_and_found: false
- wall_shadows: 104
- music.day: "Music/Location Tracks/Player Home Day"
- music.night: "Music/Location Tracks/Player Home Night"

## summit

- name: "The Summit"
- serializable: true
- outdoor: true
- bug_tag: ["standard"]
- bug_boxes: [[[116, 76], [138, 88]]]
- dig_sites: 1
- reset_every_night: true
- safe_position: [1016, 760]

## western_ruins

- name: "The Western Ruins"
- serializable: true
- forageables: 1
- outdoor: true
- bug_tag: ["standard"]
- bug_boxes: [[[148, 54], [208, 174]]]
- dig_sites: 1
- special_dig_sites: 2
- bugs: 2
- reset_every_night: true
- bird_count: [0, 2]
- mist_sights: [[1544.0, 936.0], [1320.0, 1004.0]]
- safe_position: [1664, 1008]

## seridias_house

- name: "Seridia's House"
- music: "Music/Npc Tracks/Seridia"
- map_location: "western_ruins"
- building: "seridias_house"

## seridias_house_back

- music: "Music/Location Tracks/SeridiaVoidRoom"
- map_location: "western_ruins"
- building: "seridias_house"

## beach

- name: "The Beach"
- serializable: true
- outdoor: true
- bug_tag: ["beach"]
- bug_boxes: [[[54, 18], [132, 52]], [[154, 20], [314, 86]], [[148, 54], [208, 174]]]
- dig_sites: 1
- special_dig_sites: 1
- bugs: 3
- forageables: 3
- ambience.day: "Ambience/Beach"
- ambience.night: "Ambience/Beach"
- reset_every_night: true
- bird_count: [0, 2]
- mist_sights: [[1992.0, 268.0], [1496.0, 332.0]]
- safe_position: [1736, 136]

## terithias_house

- name: "Tackle Shop"
- map_location: "beach"
- building: "terithias_house"

## landens_house_f1

- name: "Carpenter's Shop"
- map_location: "eastern_road"
- building: "landens_house"
- music: "Music/Location Tracks/Carpenter"

## landens_house_f2

- map_location: "eastern_road"
- building: "landens_house"
- music: "Music/Location Tracks/Carpenter"

## haydens_farm

- name: "Sweetwater Farm"
- serializable: true
- outdoor: true
- bug_tag: ["standard"]
- bug_boxes: [[[40, 0], [210, 120]]]
- dig_sites: 1
- bugs: 2
- forageables: 1
- npc_farm: true
- reset_every_night: true
- bird_count: [0, 2]
- npa_spawn_points: ["npa_0", "npa_1", "npa_2", "npa_3", "npa_4", "npa_5", "npa_6", "npa_7", "npa_8"]
- mist_sights: [[1656.0, 780.0], [600.0, 396.0], [1000.0, 780.0]]
- safe_position: [1184, 680]

## haydens_house

- name: "Hayden's Shop"
- map_location: "haydens_farm"
- building: "haydens_house"

## mines_entry

- name: "Mines Entrance"
- map_location: "narrows"
- ambience: "Ambience/Cave"
- serializable: true
- safe_position: [216, 240]
- music.day: "Music/Location Tracks/MinesEntry"
- music.night: "Music/Location Tracks/MinesEntry"

## abandoned_mines

- map_location: "mines_entry"
- ambience: "Ambience/Cave"

## abandoned_pit

- map_location: "abandoned_mines"
- ambience: "Ambience/Cave"

## blacksmith_store

- name: "Blacksmith's Shop"
- map_location: "town"
- music: "Music/Location Tracks/Blacksmith"
- building: "blacksmith"

## blacksmith_room_left

- map_location: "town"
- music: "Music/Location Tracks/Blacksmith"
- building: "blacksmith"

## blacksmith_room_right

- map_location: "town"
- music: "Music/Location Tracks/Blacksmith"
- building: "blacksmith"

## general_store_store

- name: "General Store"
- map_location: "town"
- building: "general_store"
- music: "Music/Location Tracks/General Store"
- safe_position: [168, 256]

## general_store_home

- map_location: "town"
- building: "general_store"
- music: "Music/Location Tracks/General Store"
- safe_position: [224, 248]

## inn

- name: "The Inn"
- map_location: "town"
- building: "inn"
- music: "Music/Location Tracks/InnLessBusy"
- safe_position: [256, 432]

## inn_east_room

- map_location: "town"
- building: "inn"

## jo_and_hemlocks_room

- gm_room: "rm_jo_hemlocks_room"
- map_location: "town"
- building: "inn"

## lucs_room

- map_location: "town"
- building: "inn"

## maples_room

- map_location: "town"
- building: "inn"

## reinas_room

- map_location: "town"
- building: "inn"

## balors_room

- map_location: "town"
- building: "inn"

## celines_room

- name: "Celine's Cottage"
- map_location: "town"
- building: "celines_room"

## clinic_f1

- name: "Clinic"
- map_location: "town"
- building: "clinic"
- music: "Music/Location Tracks/Clinic"

## clinic_f2

- map_location: "town"
- building: "clinic"
- music: "Music/Location Tracks/Clinic"

## clinic_b1

- map_location: "town"
- ambience: "SoundEffects/Environment/ValenBasementLoop"
- building: "clinic"

## small_coop

- wall_shadows: 88
- map_location: "farm"

## medium_coop

- wall_shadows: 88
- map_location: "farm"

## large_coop

- wall_shadows: 88
- map_location: "farm"

## small_barn

- wall_shadows: 88
- map_location: "farm"

## medium_barn

- wall_shadows: 88
- map_location: "farm"

## large_barn

- wall_shadows: 88
- map_location: "farm"

## small_greenhouse

- ignore_seasons: true
- map_location: "farm"
- farm: true

## large_greenhouse

- ignore_seasons: true
- map_location: "farm"
- farm: true

## mini_museum

- wall_shadows: 98
- map_location: "farm"

## dungeon

- gm_room: "rm_mines_upper_canada"
- map_location: "narrows"
- music: "Music/Location Tracks/MinesEntry"
- ambience: "Ambience/Cave"
- bug_tag: ["mines"]

## manor_house_entry

- name: "Manor House"
- map_location: "town"
- building: "manor_house"
- safe_position: [264, 480]

## adelines_office

- map_location: "town"
- building: "manor_house"

## eilands_office

- map_location: "town"
- building: "manor_house"

## manor_house_dining_room

- map_location: "town"
- building: "manor_house"
- safe_position: [136, 304]

## eilands_bedroom

- map_location: "town"
- building: "manor_house"

## adelines_bedroom

- map_location: "town"
- building: "manor_house"

## elsies_bedroom

- map_location: "town"
- building: "manor_house"

## errols_bedroom

- name: "Errol's Cabin"
- map_location: "narrows"
- building: "errols_bedroom"

## museum_entry

- name: "Museum"
- map_location: "narrows"
- building: "museum"

## museum_wing_archaeology

- name: "Archaeology Wing"
- map_location: "narrows"
- building: "museum"

## museum_wing_insect

- name: "Insect Wing"
- map_location: "narrows"
- building: "museum"

## museum_wing_fish

- name: "Fish Wing"
- map_location: "narrows"
- building: "museum"

## museum_wing_flora

- name: "Flora Wing"
- map_location: "narrows"
- building: "museum"

## mill

- name: "The Mill"
- map_location: "town"
- building: "mill"
- ambience: "SoundEffects/Environment/WindmillIndoor2D"

## haydens_bedroom

- map_location: "haydens_farm"
- building: "haydens_house"

## holt_and_noras_bedroom

- map_location: "town"
- building: "general_store"
- music: "Music/Location Tracks/General Store"

## dells_bedroom

- map_location: "town"
- building: "general_store"
- music: "Music/Location Tracks/General Store"

## seridias_chamber

- map_location: "narrows"
- music: {day: "Music/Location Tracks/TheFinalSeal", night: "Music/Location Tracks/TheFinalSeal"}
- ambience: "Ambience/Cave"

## water_seal

- name: "The Water Seal"
- ambience: "Ambience/Cave"
- serializable: true
- music: {day: "Music/Events/TheSeal", night: "Music/Events/TheSeal"}
- map_location: "narrows"

## earth_seal

- name: "The Earth Seal"
- ambience: "Ambience/Cave"
- serializable: true
- music: {day: "Music/Events/TheSeal", night: "Music/Events/TheSeal"}
- map_location: "narrows"

## fire_seal

- name: "The Fire Seal"
- ambience: "Ambience/Cave"
- serializable: true
- music: {day: "Music/Events/TheSeal", night: "Music/Events/TheSeal"}
- map_location: "narrows"

## ruins_seal

- name: "The Ruins Seal"
- ambience: "Ambience/Cave"
- serializable: true
- music: {day: "Music/Events/TheSeal", night: "Music/Events/TheSeal"}
- map_location: "narrows"

## void_seal

- name: "The Void Seal"
- ambience: "Ambience/Void"
- serializable: true
- music: {day: "Music/Location Tracks/VoidSeal", night: "Music/Location Tracks/VoidSeal"}
- map_location: "narrows"

## priestess_quarters

- name: "The Priestess' Quarters"
- ambience: "Ambience/Void"
- inhibit_music: true
- serializable: true
- farm: true
- map_location: "narrows"

## narrows_secret

- name: "Narrows Cave"
- ambience: "Ambience/Cave"
- map_location: "narrows"
- serializable: true
- replace_tilemaps: false

## beach_secret

- name: "Beach Cave"
- ambience: "Ambience/BeachCave"
- map_location: "beach"
- serializable: true
- replace_tilemaps: false

## Source Absences

- No display `name` set for: aldaria, farm, bathhouse_bedroom, bathhouse_change_room, bathhouse_bath, bell_tower_f2, player_home_north (has name but no music unlike other player_home variants), seridias_house_back, landens_house_f2, abandoned_mines, abandoned_pit, blacksmith_room_left, blacksmith_room_right, general_store_home, inn_east_room, jo_and_hemlocks_room, lucs_room, maples_room, reinas_room, balors_room, clinic_f2, clinic_b1, small_coop, medium_coop, large_coop, small_barn, medium_barn, large_barn, small_greenhouse, large_greenhouse, mini_museum, dungeon, adelines_office, eilands_office, manor_house_dining_room, eilands_bedroom, adelines_bedroom, elsies_bedroom, museum_wing_archaeology through museum_wing_flora (have names), haydens_bedroom, holt_and_noras_bedroom, dells_bedroom, seridias_chamber.
- The `aldaria` location has no properties at all — only the section header exists. Purpose unclear from this source alone.
- No location description text in this file — display names only. Prose descriptions may exist in `t2_location_descriptions.toml`.
- No NPC residence mappings in this file — building/room assignments are present but which NPC lives in which room is not declared here (may be in `npcs/` data).
- player_home_north is the only player_home variant that lacks a `music` sub-table.
