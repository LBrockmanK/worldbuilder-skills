---
type: reference
title: Natural World — Creatures, Flora, Museum, and Visitors
description: 'Broad-strokes extraction of monsters/, forageables.toml, museum_wings/,
  and cameos/: mine creatures, wild flora, museum collections, and visiting characters.
  No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T23:16Z
resources:
- projects/fields-of-mistria/source/fiddle/monsters/bat.toml
- projects/fields-of-mistria/source/fiddle/monsters/cat.toml
- projects/fields-of-mistria/source/fiddle/monsters/clod.toml
- projects/fields-of-mistria/source/fiddle/monsters/enchantern.toml
- projects/fields-of-mistria/source/fiddle/monsters/mimic.toml
- projects/fields-of-mistria/source/fiddle/monsters/mite.toml
- projects/fields-of-mistria/source/fiddle/monsters/rock_stack.toml
- projects/fields-of-mistria/source/fiddle/monsters/sap.toml
- projects/fields-of-mistria/source/fiddle/monsters/shroom.toml
- projects/fields-of-mistria/source/fiddle/monsters/spirit.toml
- projects/fields-of-mistria/source/fiddle/monsters/statue.toml
- projects/fields-of-mistria/source/fiddle/monsters/tome.toml
- projects/fields-of-mistria/source/fiddle/forageables.toml
- projects/fields-of-mistria/source/fiddle/museum_wings/archaeology.toml
- projects/fields-of-mistria/source/fiddle/museum_wings/fish.toml
- projects/fields-of-mistria/source/fiddle/museum_wings/flora.toml
- projects/fields-of-mistria/source/fiddle/museum_wings/insect.toml
- projects/fields-of-mistria/source/fiddle/cameos/darren.toml
- projects/fields-of-mistria/source/fiddle/cameos/great_bird.toml
- projects/fields-of-mistria/source/fiddle/cameos/linnet.toml
- projects/fields-of-mistria/source/fiddle/cameos/wiscar.toml
- projects/fields-of-mistria/source/fiddle/cameos/wynne.toml
---

# Natural World -- Creatures, Flora, Museum, and Visitors

No-inference extraction from game data files. Mechanical stats (exact HP, damage frame timings, sprite paths, physics values) are abbreviated. Names, drops, habitats, descriptions, and any lore-bearing content are reproduced in full.

## Monsters

All monsters are mine creatures. Each file defines a `[default]` block (shared base stats for that monster family) and one or more named variants.

### Essence Bat (bat.toml)

Flying creature. Object: `obj_monster_bat`. Death sound category: flesh.

**Bat** (base variant): HP 32, damage 18, essence 15. No variant attack. Drops: essence_drop (70%), monster_wing (30%), head_essence_bat_hat cosmetic (5%), pet_skin_essence_bat (5%).

**Bat Blue** (stronger variant): HP 48, damage 32, essence 15. Has variant attack. Higher knockback (4 vs 2). Same drop table as base bat.

Behavior: flies, spits projectile breath attacks. Flees when threatened (flee timer 120-180 frames).

### Lava Cat (cat.toml)

Ground creature. Object: `obj_monster_cat`. Has petrification mechanic (petrified duration 300 frames, shakes at 60 frames). Death sound category: flesh/rock hybrid.

**Cat** (Lava Cat): HP 120, damage 35, essence 15. Water hater (true), not light hater. Charge attack with movement speed 6. Drops: glass (70%, 3-5), ore_stone (70%, 3-5), obsidian (30%), monster_whisker (30%), head_lava_cat_hat cosmetic (5%), pet_skin_lava_cat (10%).

**Cat Void** (Void Cat): HP 220, damage 45, essence 20. Has light_hater mechanic (light_health 300; player light value 1.0, neutral light 0.5; petrifies when exposed to enough light). Drops: monster_whisker (30%), head_void_cat_hat cosmetic (5%), pet_skin_void_cat (10%).

Both variants can be petrified and have petrified walk/hurt sprites.

### Clod (clod.toml)

Rock creature family. Object: `obj_monster_clod`. Hops to move. Spits rock projectiles that can be reflected by sword. Death sound category: rock.

**Rockclod** (base): HP 8, damage 10, essence 5. Drops: ore_stone (70%, 1-2), monster_shell (30%), head_rockclod_hat cosmetic (5%), pet_skin_rockclod (5%).

**Copperclod**: HP 16, damage 12, essence 5. Fires 2-projectile legion. Drops: ore_copper (70%, 1-3), monster_shell (25%), ore_ruby (5%), head_oreclod_hat cosmetic (5%), pet_skin_oreclod (5%).

**Rockclod Blue**: HP 16, damage 12, essence 10. Fires 2-shot sequence. Drops: ore_stone (70%, 2-4), monster_shell (30%, 1-2), head_rockclod_hat cosmetic (5%), pet_skin_rockclod (5%).

**Ironclod**: HP 32, damage 17, essence 15. Fires at 45-degree radial spread. Drops: ore_iron (70%, 1-3), monster_shell (25%, 1-2), ore_sapphire (5%), head_oreclod_hat cosmetic (5%), pet_skin_oreclod (5%).

**Rockclod Green**: HP 32, damage 24, essence 15. Launcher variant (launches itself into air, can fly). Drops: ore_stone (70%, 4-6), monster_shell (30%, 1-3), head_rockclod_hat cosmetic (5%), pet_skin_rockclod (5%).

**Silverclod**: HP 48, damage 22, essence 15. Bomber variant (bomb_ammo 2, bomb_chance 40%, bomb_radius 64). Drops: ore_silver (70%, 1-3), monster_shell (25%, 1-3), ore_emerald (5%), head_oreclod_hat cosmetic (5%), pet_skin_oreclod (5%).

**Rockclod Red**: HP 48, damage 36, essence 20. Fires 9-projectile sequence at 45-degree turns. Explodes on death (9 projectiles). Drops: ore_stone (70%, 6-12), monster_shell (30%, 1-4), head_rockclod_hat cosmetic (5%), pet_skin_rockclod (5%).

**Goldclod**: HP 48, damage 28, essence 20. Projectiles split (depth 2, 40-degree angle). Drops: ore_gold (1-3, exclusive=false), monster_shell (25%, 1-4), ore_diamond (5%), head_oreclod_hat cosmetic (5%), pet_skin_oreclod (5%).

**Rockclod Purple**: HP 1000, damage 50, essence 25. Drops: ore_stone (1, exclusive=false), ore_pink_diamond (5%), perfect_pink_diamond (1%).

**Mistrilclod**: HP 1000, damage 20, essence 15. Fires 5-projectile sequence in 5-projectile legion. Drops: ore_mistril (1, exclusive=false), ore_pink_diamond (5%), perfect_pink_diamond (1%).

Lore note: the clod family forms a mineral progression (stone, copper, iron, silver, gold, mistril) with matching ore drops and increasing power. Purple and mistril variants have 1000 HP, making them endurance encounters.

### Enchantern (enchantern.toml)

Lantern creature. Object: `obj_monster_enchantern`. Has on/off state (flickers on to attack, charges, then winds down). Death sound category: rock.

**Enchantern** (base): HP 24, damage 12, essence 5. Yellow electrocute. Does not drop floor balls. Drops: glass (70%), monster_core (30%), head_enchantern_hat cosmetic (5%), pet_skin_enchantern (5%).

**Enchantern Blue**: HP 48, damage 20, essence 10. Blue electrocute. Drops floor balls (energy orbs on the ground). Drops: glass (70%, 1-2), monster_core (30%, 1-2), head_enchantern_hat cosmetic (5%), pet_skin_enchantern (5%).

Behavior: starts inactive, flickers on when aggro'd, charges at player, then deactivates and flees.

### Mimic (mimic.toml)

Chest mimic. Object: `obj_monster_mimic`. Stationary ambush creature, always faces south (starting_dir [181, 181]).

**Mimic**: HP 1000 (from default), damage 20, essence 0. No drops defined. Has idle shake, attack (opens), gobble (eats), hurt, and fade (disappear) states. No coins (coin_count [1, 3] from default).

Behavior: disguises as chest, attacks when approached, can gobble items.

### Stalagmite / Mite (mite.toml)

Burrowing spike creature. Object: `obj_monster_mite`. Moves underground, erupts from floor to attack. Death sound category: rock.

**Stalagmite** (Blue): HP 24, damage 25, essence 5. No secondary spikes. Drops: ore_copper (70%), monster_horn (30%), head_stalagmite_hat cosmetic (5%), pet_skin_stalagmite (5%).

**Stalagmite Green**: HP 36, damage 30, essence 10. Has secondary spikes (6 surrounding spike positions). Drops: ore_iron (70%), monster_horn (30%, 1-2), head_stalagmite_hat cosmetic (5%), pet_skin_stalagmite (5%).

**Stalagmite Purple**: HP 65, damage 35, essence 15. Has secondary spikes (8 surrounding positions, wider pattern). Drops: ore_gold (70%), monster_horn (30%, 1-3), head_stalagmite_hat cosmetic (5%), pet_skin_stalagmite (5%).

### Rock Stack (rock_stack.toml)

Stacking rock creature. Object: `obj_monster_rock_stack`. Two rocks that launch one atop the other; the top rock tracks the player while airborne and slams down.

**Rock Stack**: HP 150, damage 50, essence 15. Drops: ore_stone (70%, 1-2), monster_block (30%), head_rock_stack_hat cosmetic (5%), pet_skin_rock_stack (10%). Super drops: ore_diamond (100%, 3-5).

Behavior: launches top half into air, top half tracks player (air_speed_max 1.5), slams down. Can hop onto another rock_stack (hop_threshold 48).

### Sapling (sap.toml)

Plant creature. Object: `obj_monster_sap`. Jumps to attack. Death sound category: flesh.

**Sapling** (base): HP 24, damage 10, essence 5. Drops: sap (70%), monster_fang (30%), head_sapling_hat cosmetic (5%), pet_skin_sapling (5%).

**Sapling Cool**: HP 36, damage 17, essence 10. Wears sunglasses (face_gear_sunglasses cosmetic drop at 5%). Same core drops as base sapling.

**Sapling Blue**: HP 36, damage 24, essence 10. Sticky (slows player on hit). Drops: sap (70%, 1-2), monster_fang (30%, 1-2), head_sapling_hat cosmetic (5%), pet_skin_sapling (5%).

**Sapling Purple**: HP 48, damage 24, essence 15. Free-flying variant (can fly through air). Massive aggro/attack radius (624). Drops: sap (70%, 1-2), monster_fang (30%, 1-2), head_sapling_hat cosmetic (5%), pet_skin_sapling (5%).

**Sapling Orange**: HP 72, damage 44, essence 20. Spawns 2 mini saplings (sapling_orange_mini) on hit. Drops: sap (70%, 1-3), monster_fang (30%, 1-3), head_sapling_hat cosmetic (5%), pet_skin_sapling (5%).

**Sapling Orange Mini**: HP 24, damage 10, essence 5. Spawned by orange sapling. Drops: sap (35%), monster_fang (15%).

**Sapling Pink**: HP 150, damage 50, essence 25. Has hyper armor (2 hits absorbed before stagger). Drops skull mask cosmetics. Drops: sap (70%, 1-3), monster_fang (30%, 1-3), head_sapling_hat cosmetic (5%), head_skull_mask cosmetic (5%), pet_skin_sapling (5%), skull_mask pet cosmetic (10%).

### Mushroom / Shroom (shroom.toml)

Mushroom creature. Object: `obj_monster_shroom`. Can retract into its cap (shell state) for defense, then wiggle to flip over. Death sound category: flesh.

**Mushroom** (Red, base): HP 24, damage 15, essence 5. Drops: red_toadstool (70%), monster_powder (30%), head_mushroom_hat cosmetic (5%), pet_skin_mushroom (5%).

**Mushroom Green**: HP 48, damage 25, essence 10. Explodes on death. Drops: wild_mushroom (70%), monster_powder (30%, 1-2), head_mushroom_hat cosmetic (5%), pet_skin_mushroom (5%).

**Mushroom Blue**: HP 72, damage 35, essence 15. Fades in/out (invisibility mechanic, fade rates 0.05, shadow threshold 0.5). Short windup (15-25 frames). Drops: glowing_mushroom (70%), monster_powder (30%, 1-2), head_mushroom_hat cosmetic (5%), pet_skin_mushroom (5%).

**Mushroom Purple**: HP 96, damage 50, essence 20. Spews lava (lava_damage 1, lava_angle 90, lava_timer 300). Drops: purple_mushroom (70%), monster_powder (30%, 1-3), head_mushroom_hat cosmetic (5%), pet_skin_mushroom (5%).

### Flame Spirit (spirit.toml)

Floating fire spirit. Object: `obj_monster_spirit`. Teleports and fires homing projectiles. Death sound category: flesh.

**Spirit** (Flame Spirit): HP 80, damage 28, essence 15. Teleports near player (distance 30-96). Fires homing projectiles (turn rate 0.35, speed 1.5, damage 30, lifetime 240-400 frames). Drops: basic_wood (70%, 3-5), peat (70%), monster_core (30%), head_flame_spirit_hat cosmetic (5%), pet_skin_flame_spirit (5%).

**Spirit Purple**: HP 150, damage 38, essence 15. Fires orbiting belt of 3 projectiles (shot_rate 90, rotation_speed 4.75). Projectiles have near-infinite lifetime (99999 frames). Fades in (rate 0.1). Drops: same as base spirit.

### Griffin Statue (statue.toml)

Animated stone statue. Object: `obj_monster_statue`. Chases and tumbles into player. Death sound category: rock.

**Griffin Statue**: HP 200, damage 60 (+ bonus_damage 5), essence 0 (not set, inherits default 0). Tumbles when hit (tumble mechanics). Drops: monster_block (70%, 1-3), monster_fang (30%, 1-3), head_griffin_statue_hat cosmetic (10%), pet_skin_gryphon_statue (10%).

Lore note: called "living griffin statue" in sprites. A gryphon-shaped stone construct.

### Flying Tome (tome.toml)

Animated book creature. Object: `obj_monster_tome`. Flies and chomps; when stunned, falls to ground and performs wind tornado attack.

**Tome**: HP 150, damage 50, essence 5. Steering 0.5, flying speed 2.4, timeout 220 frames. When stunned (stun_star_duration 60, stun_blink_duration 180), performs wind attack (duration 135 frames). Drops: sap (70%), monster_fang (30%), head_flying_tome_hat cosmetic (5%), pet_skin_flying_tome (10%).

### Monster Drop Summary

Recurring drop items with lore implications:
- **Essence drops**: essence_drop (bat family)
- **Body parts**: monster_wing (bats), monster_whisker (cats), monster_shell (clods), monster_core (enchanterns, spirits), monster_horn (stalagmites), monster_fang (saplings, tomes, griffin statues), monster_powder (mushrooms), monster_block (rock stacks, griffin statues)
- **Ores**: stone, copper, iron, silver, gold, mistril, ruby, sapphire, emerald, diamond, pink_diamond, obsidian, perfect_pink_diamond
- **Organic**: sap (saplings, tomes), red_toadstool, wild_mushroom, glowing_mushroom, purple_mushroom, glass (enchanterns, cats), peat, basic_wood (spirits)
- **Cosmetics**: every monster family has a hat cosmetic and a pet skin

## Forageables

Source: `forageables.toml`. Seasonal wild items found by foraging. Rarity tiers with weighted votes: legendary (3 votes), rare (6), uncommon (9), common (12).

### Beach Forageables (Sand)

Found on sand, placed in the common category: blue_conch_shell, sand_dollar, spirula_shell, pink_scallop_shell.

### Spring

- **Common**: daffodil, dandelion, fennel, tulip, chickpea, lilac, wild_leek
- **Uncommon**: (none)
- **Rare**: snowdrop_anemone, fiddlehead, morel_mushroom, nettle
- **Legendary**: middlemist

### Summer

- **Common**: daisy, iris, catmint, cosmos
- **Uncommon**: (none)
- **Rare**: marigold, sage, basil, thyme, oregano, dill, sesame, night_queen
- **Legendary**: (none)

### Fall

- **Common**: heather, horseradish, chestnut
- **Uncommon**: (none)
- **Rare**: moon_fruit, rosemary, garlic, viola, fog_orchid
- **Legendary**: (none)

### Winter

- **Common**: frost_lily, poinsettia, burdock_root, jasmine, crocus, holly, ice_block
- **Uncommon**: (none)
- **Rare**: snapdragon, pineshroom, oyster_mushroom
- **Legendary**: (none)

Note: middlemist is the only legendary forageable (spring only). Summer, fall, and winter have no legendaries. Uncommon tier is empty across all seasons. Several "herbs" (sage, basil, thyme, oregano, dill, sesame) are classified as rare summer forageables rather than crops.

## Museum Wings

The museum has four wings: Archaeology, Fish, Flora, and Insects. Each wing contains named sets of 4-5 items and a tiered reward track.

### Archaeology Wing

21 artifact sets:

- **Aldarian Artifact Set**: "A collection of artifacts from the Aldarian Kingdom's history." Items: aldarian_sword, family_crest_pendant, aldarian_war_banner, aldarian_gauntlet, lost_crown_of_aldaria.
- **Caldosian Artifact Set**: "A collection of artifacts from the Caldosian Empire's history." Items: caldosian_sword, caldosian_emperor_bust, caldosian_breastplate, caldosian_drinking_horn, statuette_of_caldarus.
- **Alda Artifact Set**: "A collection of artifacts from the Dark Ages of Aldaria's history." Items: alda_bronze_sword, alda_clay_pot, alda_feather_pendant, alda_gem_bracelet, alda_mural_tablet.
- **Ancient Artifact Set**: "A collection of artifacts from the age of the Witch Queen's reign." Items: ancient_stone_lantern, ancient_gold_coin, ancient_crystal_goblet, ancient_horn_circlet, ancient_royal_scepter.
- **Dragon Artifact Set**: "A collection of artifacts from the Ruins." Items: dragon_scale, dragon_claw, hardened_essence, dragon_forged_bracelet, dragon_pact_tablet.
- **Prehistoric Artifact Set**: "A collection of artifacts from an unimaginably long time ago." Items: amber_trapped_insect, trilobite_fossil, tiny_dinosaur_skeleton, fossilized_egg, meteorite.
- **Oopart Artifact Set**: "A collection of out of place artifacts with dubious archaeological value." Items: muttering_cube, weightless_stone, completely_wrong_map, black_tablet, unknown_dragon_statuette.
- **Aquatic Artifact Set**: "A collection of artifacts fished from the waters." Items: rubber_fish, giant_fish_scale, coin_lump, water_sphere, rusted_treasure_chest.
- **Sunken Artifact Set**: "A collection of artifacts found by diving below the waters." Items: rusted_shield, rock_with_a_hole, rainbow_seaweed, criminal_confession, mermaids_comb.
- **Deep Woods Artifact Set**: "A collection of artifacts from the depths of the Deep Woods." Items: petrified_wood, gathering_basket, crystal_apple, metal_leaf, fossilized_mandrake_root.
- **Fish Trap Artifact Set**: "A collection of artifacts acquired by using a fish trap." Items: clay_amphora, sea_glass, porcelain_figurine, worn_pendant, message_in_a_bottle.
- **Buried Artifact Set**: "A collection of artifacts from the depths below Mistria." Items: stone_horse, flint_arrowhead, obsidian_blade, diamond_backed_mirror, shortcut_scroll.
- **Upper Mines Artifact Set**: "A collection of artifacts from the Upper Mines." Items: miners_pickaxe, tin_lunchbox, miners_slab, miners_rucksack, miners_helmet.
- **Tide Cavern Artifact Set**: "A collection of artifacts from the Tide Caverns." Items: stone_shell, tidestone, starlight_coral, dense_water, crab_statue.
- **Deep Earth Artifact Set**: "A collection of artifacts from the Deep Earth." Items: really_round_rock, seriously_square_stone, earth_infused_stone, faceted_rock_gem, rock_statue.
- **Lava Caves Artifact Set**: "A collection of artifacts from the Lava Caves." Items: fire_crystal, warm_rock, red_obsidian, rainbow_geode, tiny_volcano.
- **Gems of Mistria Set**: "A collection of perfect gems from across Mistria." Items: perfect_ruby, perfect_sapphire, perfect_emerald, perfect_diamond, perfect_pink_diamond.
- **Metals of Mistria Set**: "A collection of perfect metal ores from across Mistria." Items: perfect_copper_ore, perfect_iron_ore, perfect_silver_ore, perfect_gold_ore, perfect_mistril_ore.
- **Ritual Artifact Set**: "A collection of artifacts found in underground ritual chambers." Items: ritual_incense_burner, ritual_beads, ritual_chalice, ritual_scepter, ritual_tablet.
- **Mist Artifact Set**: "A collection of artifacts found in Mist Spots." Items: misty_black_mirror, misty_feather_quill, mist_crystal, mist_scroll, mist_flute.
- **Vintage Farm Tools Set**: "A collection of vintage farm tools found on your farm." Items: vintage_watering_can, vintage_hammer, vintage_sickle, vintage_brush, vintage_cow_bell.
- **Dig Site Material Set**: "A collection of common materials found while digging." Items: sod, peat, shards, clay, shard_mass.

Historical eras implied by artifact sets: Prehistoric > Alda (Dark Ages, bronze age technology) > Ancient (Witch Queen's reign) > Caldosian Empire > Aldarian Kingdom. Dragon artifacts come from the Ruins. Ritual artifacts from underground chambers. Mist artifacts from "Mist Spots."

Rewards: 21 tiers progressing from wood treasure boxes through copper, silver, to gold, plus explorer outfit cosmetics and explorer-themed furniture/decor crafting scrolls. Notable late rewards include dragon_altar_water, gryphon_statue_replica, dragon_statue_replica, gemstone_bridge, forge_mistril.

### Fish Wing

22 fish sets organized by season and water body:

**Seasonal sets** (5 fish each, by water body):
- Spring: River (bluegill, chub, carp, walleye, paddlefish), Pond (barb, angel_fish, crucian_carp, brown_trout, goldfish), Ocean (anchovy, shrimp, lobster, mackerel, ocean_sunfish)
- Summer: River (minnow, loach, sweetfish, bream, tarpon), Pond (lake_chub, golden_shiner, brown_bullhead, sauger, giant_koi), Ocean (dart, crab, stingray, char, grouper)
- Fall: River (grayling, lamprey, shad, perch, razorback), Pond (killifish, striped_bass, rainbow_trout, bluefish, white_perch), Ocean (saury, butterfish, mullet, halibut, shark)
- Winter: River (dace, herring, freshwater_eel, bowfish, shadow_bass), Pond (tilapia, flathead_catfish, burbot, giant_tilapia, alligator_gar), Ocean (sand_lance, horse_mackerel, sea_bass, king_crab, oarfish)

**Location sets** (mine/dungeon areas):
- Upper Mines: cave_shrimp, rock_guppy, stone_loach, cave_eel, cave_shark
- Tide Caverns: sapphire_betta, archerfish, transparent_jellyfish, water_balloon_fish, mini_whale_shark
- Deep Earth: pebble_minnow, shardfin, earth_eel, rockbiter, emerald_horned_charger
- Lava Caves: lava_piranha, candelabra_seadragon, armored_bass, sulfur_crab, firesail_fish
- Ruins: winged_shrimp, gazer, luminescent_crab, giant_jellyfish, coelacanth
- Deep Woods: sunny, forest_perch, silver_redhorse, lake_trout, muskie

**Special sets**:
- Multi-Season: pollock, koi, pike, smallmouth_bass, trout
- Fish Bait Set: massive_minnow, copper_rockfish, iron_fish, silver_squid, golden_eel
- Fish Trap Set: blue_crab, sea_urchin, bait_thief, hake, amberjack
- Legendary: cherry_fish, lightning_fish, leaf_fish, snow_fish (4 items, one per season implied by names)

Rewards: 22 tiers, fishing outfit cosmetics, fishing-themed furniture, and late rewards including mermaid_bed, animated_waterfall, fish_scale_cape cosmetic, fin hair clips.

### Flora Wing

20 flora sets:

**Seasonal sets** (crops, flowers, forage per season):
- Spring Crops: cabbage, potato, strawberry, turnip, cherry. Spring Flowers: daffodil, tulip, dandelion, lilac, snowdrop_anemone. Spring Forage: fennel, fiddlehead, morel_mushroom, nettle, wild_leek.
- Summer Crops: cucumber, chili_pepper, watermelon, tomato, corn. Summer Flowers: daisy, iris, marigold, catmint, cosmos. Summer Forage: sage, basil, thyme, oregano, dill.
- Fall Crops: broccoli, cranberry, pumpkin, sweet_potato, apple. Fall Flowers: celosia, chrysanthemum, fog_orchid, heather, viola. Fall Forage: rosemary, garlic, horseradish, moon_fruit, chestnut.
- Winter Crops: beet, cauliflower, snow_peas, daikon_radish, pomegranate. Winter Flowers: frost_lily, poinsettia, jasmine, crocus, snapdragon. Winter Forage: burdock_root, holly, pineshroom, oyster_mushroom, rose_hip.

**Location sets**:
- Deep Woods Forage: thorn_vine, spirit_mushroom, temple_flower, walnut, bell_berry
- Upper Mines Forage: upper_mines_mushroom, red_toadstool, sweetroot, shadow_flower, narrows_moss
- Tide Caverns Forage: underseaweed, sea_grapes, cave_kelp, mines_mussels, tide_lettuce
- Deep Earth Forage: crystal_berries, shale_grass, earthshroom, rockroot, crystal_rose
- Lava Caves Forage: flame_pepper, ash_mushroom, lava_chestnuts, hot_potato, breath_of_fire
- Ruins Forage: spell_fruit, written_root, essence_blossom, ethereal_grass, chirping_fern
- Void Forage: void_herb, void_stone, void_powder, void_pearl, voidite

Note: flora wing's winter forage set includes rose_hip, which does not appear in the forageables.toml seasonal lists -- it may come from a different source mechanic. Flora sets include crops (planted/grown) alongside foraged items; the forageables.toml only covers wild forage spawns.

Rewards: 19 tiers, farmer outfit cosmetics, seasonal furniture sets (spring/summer/fall themed), tesserae_tree, void_bonsai.

### Insect Wing

17 insect sets:

**Seasonal**:
- Multi-Season: ant, bumblebee, fuzzy_moth, praying_mantis, hummingbird_hawk_moth
- Spring: luna_moth, butterfly, ladybug, caterpillar, roly_poly
- Summer: cicada, cricket, dragonfly, firefly, sand_bug
- Fall: walking_leaf, cicada_nymph, monarch_butterfly, inchworm, tiger_swallowtail_butterfly
- Winter: crystal_caterpillar, walking_stick, brightbulb_moth, frost_flutter_butterfly, winterpillar

**Location**:
- Upper Mines: lantern_moth, copper_beetle, worm, mine_cricket, tunnel_millipede
- Tide Caverns: sea_scarab, waterfly, hermit_snail, puddle_spider, coral_mantis
- Deep Earth: rock_roach, deep_earthworm, crystalline_cricket, gem_shard_caterpillar, crystal_wing_moth
- Lava Caves: fire_wasp, cooktop_beetle, lava_snail, smoke_moth, diamond_beetle
- Ruins: ancient_firefly, void_snail, giant_worm, parchment_moth, hidden_beetle
- Deep Woods: windleaf_butterfly, mote_firefly, loam_caterpillar, dragon_horn_beetle, singing_katydid
- Beach: hermit_crab, relic_crab, waterbug, surf_beetle, beach_hopper
- Grass: grasshopper, petalhopper, strawhopper, leafhopper, icehopper

**Special**:
- Rare: jewel_beetle, lightning_dragonfly, magma_beetle, mistmoth, orchid_mantis
- Legendary: fairy_bee, flower_crown_beetle, snowball_beetle, speedy_snail, strobe_firefly
- Bee Set: fur_bee, sweet_bee, big_bee, flower_bee, moonlight_bee
- Honey Set: honey, honey_premium, honey_deluxe, honey_legendary, honeycomb
- Bug Pheromone Set: ant_queen, sunset_moth, saint_mantis, queens_birdwing, biggest_beetle
- Terrarium Treasures: bug_pheromone_uncommon, bug_pheromone_rare, bug_pheromone_legendary, fish_bait_uncommon, fish_bait_rare

Rewards: 19 tiers, beekeeper outfit cosmetics, insect-themed furniture, butterfly/dragonfly wing back cosmetics, beetle mandible horn headpiece.

## Cameos (Visiting Characters)

Source: `cameos/`. Each cameo character has a name, outfits, voice clip, portrait expressions, and animation cycles. All five characters have only a "spring" outfit defined.

### Darren

- Voice: TextBlipDarren
- Portraits: neutral, think, happy, wink, mad, embarrassed, sad, ugh (all spring)
- Cycles: idle (N/S/E, pauses on speaking turn), walk (N/S/E), blink (S/E), sit (N/S/E, seated)

### Great Bird

- Voice: TextBlipGeneric
- Portraits: neutral, happy, mad, sad, ugh, neutral_closed (all spring)
- Cycles: none defined (empty [cycles] block)

### Linnet

- Voice: TextBlipLinnet
- Portraits: neutral, think, happy, wink, mad, embarrassed, sad, ugh (all spring)
- Cycles: idle (N/S/E), walk (N/S/E), blink (S/E), sit (N/S/E, seated), action (E only, last_frame_hold 240-360)

### Wiscar

- Voice: TextBlipWiscar
- Portraits: neutral, think, happy, wink, mad, embarrassed, sad, ugh (all spring)
- Cycles: idle (N/S/E), walk (N/S/E), blink (S/E), sit (N/S/E, seated)

### Wynne

- Voice: TextBlipWynne
- Portraits: neutral, think, happy, wink, mad, embarrassed, sad, ugh (all spring)
- Cycles: idle (N/S/E), walk (N/S/E), blink (S/E), sit (N/S/E, seated)

## Source Absences

- **Monster locations**: no data in these files specifies which mine floors or areas each monster spawns on. Spawn locations must come from room/floor definition files not included here.
- **Monster descriptions/flavor text**: these are purely mechanical data files with no narrative descriptions of the creatures.
- **Forageable locations**: forageables.toml defines seasons and rarity but not map spawn points (except the sand_forageables beach note).
- **Crop growth data**: flora museum sets reference crops but crop growth times, watering requirements, etc. are not in these files.
- **Cameo dialogue and schedules**: cameo files define visual/audio assets only -- no dialogue, event triggers, visit schedules, or relationship data.
- **Great Bird**: has no animation cycles defined, suggesting it may be a static/cutscene-only character or incomplete.
- **Museum set completion requirements**: the data shows sets and rewards but no explicit completion thresholds (whether partial completion counts).
- **Uncommon forageables**: all seasons have an empty uncommon tier. Whether this is intentional design or placeholder is not stated.
- **Insect catch mechanics**: insect files define sets but not catch difficulty, spawn conditions, or time-of-day restrictions.
- **Fish difficulty/behavior**: fish sets define names and locations but not catch difficulty, fish size, or behavior patterns.
