---
type: reference
title: Story Structure — Quests and Calendar
description: 'Broad-strokes extraction of quests/ directory and dates.toml: main story
  quests, heart quests, fetch quests, challenge quests, and the game calendar system.
  No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T23:15Z
resources:
- projects/fields-of-mistria/source/fiddle/quests/story_quests.toml
- projects/fields-of-mistria/source/fiddle/quests/heart_quests.toml
- projects/fields-of-mistria/source/fiddle/quests/fetch_quests.toml
- projects/fields-of-mistria/source/fiddle/quests/crown_quests.toml
- projects/fields-of-mistria/source/fiddle/quests/tali_challenges.toml
- projects/fields-of-mistria/source/fiddle/quests/stillwell_challenges.toml
- projects/fields-of-mistria/source/fiddle/quests/request_board.toml
- projects/fields-of-mistria/source/fiddle/quests/crown_registry.toml
- projects/fields-of-mistria/source/fiddle/quests/tali_registry.toml
- projects/fields-of-mistria/source/fiddle/quests/stillwell_registry.toml
- projects/fields-of-mistria/source/fiddle/dates.toml
- projects/fields-of-mistria/source/fiddle/festivals.toml
---

# Story Structure — Quests and Calendar

## quests/story_quests.toml

Story quests define the main narrative progression. Each has a `test_target` field indicating its storyline track: `main_story`, `dragon_story`, or `festivals`.

### Main Story Track

These quests drive the town restoration arc. The player arrives in Mistria after an earthquake and progressively rebuilds the town, raising its rank.

**Greet the Townsfolk** — Meet all townsfolk (22 named NPCs) and report to Adeline. Rewards: 3 potato seeds, 100 gold, 20 renown.

**Do a Bro a Favor** — Talk to Olric. Rewards: worn pickaxe, 20 renown.

**Stinky Stamina Potion** — Bring a lilac to Juniper. Rewards: 20 renown.

**Friday at the Sleeping Dragon Inn** — Meet Reina at the Inn after 6pm on a Friday. Rewards: mixed fruit juice, 20 renown.

**Museum Donations Wanted** — Meet Errol at the Museum in the Narrows. Rewards: 100 gold, 20 renown.

**Cop Some Ore** — Bring March 3 copper ore. Rewards: 100 gold, 20 renown.

**Greet the Vendors** — Meet all four Saturday Market vendors (Merri, Darcy, Vera, Louis), then report to Nora. Rewards: 200 gold, 20 renown.

**Something's Bugging Me** — Meet Luc at the Inn. Rewards: worn net, 20 renown.

**The Mill Restoration Project** — Two-stage quest. Meet Adeline at the Manor House, then deposit 200 stone, 150 wood, 2 copper ingots and bring 1000 tesserae to Adeline. Rewards: 20 renown.

**Jo's Cooking Class** — Meet Josephine at the Inn. Rewards: vegetable soup recipe, 20 renown.

**Tea with Hayden** — Meet Hayden at his house. Rewards: 10 hay, 10 grass seed, cup of tea, 20 renown.

**Crafting Tutorial** — Bring Ryis 10 wood. Rewards: 20 renown, 5 starter wood fences.

**Restocking Mistria's Food Reserves** — Meet Adeline at Manor House, then ship 10 crops. Rewards: 20 renown.

**Repair the General Store** — Two-stage. Deposit 500 stone, 300 wood, 5 copper ingots, 5 iron ingots and bring 3000 tesserae. Rewards: 50 renown.

**Beautification Project** — Meet Adeline in front of the Manor House. Rewards: 20 renown.

**Upgrade Hayden's Barn** — Two-stage. Deposit 500 stone, 400 wood, 8 iron ingots and bring 4000 tesserae. Rewards: 50 renown.

**Restocking Mistria's Food Reserves 2** — Two-stage. Deposit 10 cheese, 12 eggs. Rewards: 30 renown, a cow with cheese hat, a chicken with egg hat.

**Repair the Beach Bridge** — Two-stage. Deposit 150 stone, 300 wood, 50 fiber and bring 1000 tesserae. Rewards: 20 renown.

**Upgrade the Inn** — Deposit 500 stone, 600 wood, 10 silver ingots, 25 glass, 10 peat and bring 6000 tesserae. Rewards: 50 renown.

**Find the Weathervane** — Find Hayden's weathervane in the Narrows and return it.

**Stone Refinery** — Meet Adeline at the Mines entrance, deposit 400 stone, 200 wood, 20 sap and bring 5000 tesserae. Rewards: 30 renown.

**Seeking Gossip** — Collect gossip from Balor, Juniper, and Dell, then tell Elsie. Rewards: 20 renown.

**Repair the General Store** (already listed above)

**Apiaries and Terrariums** — Meet Luc at the Inn, then ship 20 bugs. Rewards: 20 renown, apiary, terrarium, crafting scrolls for both.

**Upgrade the Saturday Market** — Deposit 8 gold ingots, 20 obsidian, 20 crystal, 100 hardwood, 50 refined stone. Rewards: 50 renown.

**Upgrade the Carpenter's Shop** — Deposit 100 glass, 100 refined stone, 30 crystal, 30 obsidian. Rewards: 50 renown, small greenhouse blueprint.

**Lost & Found** — Meet Adeline at the Manor House Dining Room. Rewards: 20 renown.

**Expanding the Saturday Market** — Deposit 50 voidite, 20 refined stone, 5 mistril ingots, 10 monster cores, 5 monster blocks. Rewards: 50 renown.

**Meet the New Vendors** — Meet Stillwell and Zorel at the Saturday Market, talk to Nora. Rewards: 1000 gold, 20 renown.

**Repair the Bell Tower** — Deposit 20 refined stone, 30 hardwood, 1 dragon-forged fang, 1 dragon-forged core. Rewards: 50 renown.

**Complete the Museum** — Complete the Museum's collection. Rewards: 20 renown, 10000 gold, mini museum blueprint.

### Town Rank Milestones

A series of quests requiring the player to reach specific renown levels:
- Copper Star (lvl 20)
- Ruby Star (lvl 30)
- Iron Star (lvl 40)
- Sapphire Star (lvl 50)
- Silver Star (lvl 60)
- Emerald Star (lvl 70)
- Gold Star (lvl 80)
- Diamond Star (lvl 90)
- Mistril Star (lvl 100)

All use `test_target = "main_story"` and track via `reached_renown_level`.

### Dragon Story Track

These quests form a separate dungeon/lore storyline (`test_target = "dragon_story"`).

**The State of the Mines** — Meet Eiland at the Museum to discuss reopening the Mines. Rewards: 20 renown.

**Unlocking the Mines** — Meet Errol and Eiland at the Mines entrance. Rewards: 20 renown.

**Repair the Bridge** — Meet Adeline near the bridge on the Eastern Road, then deposit 60 stone, 60 wood. Rewards: 30 renown.

**The Water Tablet** — Speak to Eiland about the tablet, then offer lantern moth, ruby, stone loach, and upper mines mushroom to the water seal. Rewards: 20 renown.

**The Earth Tablet** — Speak to Juniper, then offer coral mantis, sapphire, archerfish, cave kelp to the earth seal. Rewards: 20 renown.

**The Fire Tablet** — Speak to Juniper about the fire tablet. Rewards: 20 renown.

**Procuring the Sealing Scroll** — Wait for Balor, meet him in his room, then deposit 10 silver ingots, 10 rubies, 10 sapphires, 10 emeralds. Rewards: 20 renown, unlocks "Delivering the Sealing Scroll."

**Delivering the Sealing Scroll** — Wait for Balor to deliver the scroll.

**Breaking The Fire Seal** — Offer faceted rock gem, rockroot, emerald, sealing scroll to the fire seal.

**Find the Magic Key** — Six-stage puzzle quest in the Priestess Quarters. Explore rooms, light the Dragon Forge, inspect the Library, offer temple flower and marigold, grow Seed of Balance, use the Magic Key.

**Creating the Void Mass** — Offer 5 void stones, 5 void powder, 5 void herbs, 5 void pearls to the Cauldron.

**Breaking the Ruins Seal** — Offer breath of fire, smoke moth, firesail fish, obsidian to the ruins seal.

**The Dragonsworn Tablet** — Investigate the tablet on Floor 100, reach 8 hearts with both Juniper and Eiland and view their 8-heart events, then talk to Juniper. Rewards: full Dragonsworn armor set and cloak.

**Breaking The Final Seal** — Craft and offer dragon-forged fang, horn, core, and powder at the Dragonsworn Tablet.

### Festival Quests

**The Spring Festival** (`test_target = "festivals"`) — Collect Breath of Spring items before the festival. Tiered rewards at 10/30/50/60 score: planter, basket, flower crown cosmetic, wreath.

**The Shooting Star Festival** (`test_target = "none"`) — Visit the Summit after 8pm. Invite someone.

**The Animal Festival** (`test_target = "festivals"`) — Submit animals for judging by Josephine. Separate scoring for small and large animals, tiered plushie rewards at 35/50/65.

**The Harvest Festival** (`test_target = "festivals"`) — Collect Queen Berries. Tiered rewards at 10/30/50 score: centerpiece, arch, trophy.

## quests/heart_quests.toml

Heart quests are relationship milestones triggered at specific heart levels with NPCs. They define the game's relationship narrative arcs.

### Two-Heart Events

Each romanceable NPC has a two-heart quest introducing deeper interaction:

- **Tall, Dark and Mysterious** (Balor) — Help unload supplies. Reward: 200 gold.
- **A Get Together** (Hayden) — Visit Hayden's house.
- **Becoming Juniper's Guinea Pig** (Juniper) — Visit the Bathhouse for a "free health tonic."
- **The Unusual Seed** (Celine) — Help with a mysterious flower at her cottage.
- **The Smell of Drying Ink** (Adeline) — Visit her office. Reward: cherry tart.
- **The Stele** (Eiland) — Meet outside the Manor House.
- **Surprise Me** (March) — Meet at the Blacksmith's store.
- **Pie in the Sky** (Reina) — Taste test at the Inn. Reward: wildberry pie.
- **The Annual Check-up** (Valen) — Visit the Clinic.
- **Bird Song** (Landen/Ryis) — Bring 15 wood. Reward: 150 gold.

### Four-Heart Events

- **A Rewarding Choice** (Adeline) — Help with an "important choice."
- **Water and Soil** (Celine) — The mystery seed hasn't sprouted.
- **Many Hands Make Light Work** (March) — Help at the forge.
- **Shopping Buddy** (Reina) — Join her at the General Store for cooking competition prep.
- **The Ruins** (Eiland) — Meet at the Western Ruins for Dragonsworn Armor clues.
- **Batch 312** (Valen) — Bring 1 peat. Reward: 200 gold.
- **Horsing Around** (Juniper) — Another potion test.
- **An Open Book** (Balor) — Shipping advice at the Inn.
- **A Sapling** (Ryis) — Plant a new tree at the cottage ruins.
- **Extra Feed** (Hayden) — Visit the farm.

### Six-Heart Events

- **An Outside Consultant** (Valen) — Get Juniper's help with panacea research.
- **Real Fine Day** (Hayden) — Socialize Henrietta at the General Store.
- **The Manor** (Eiland) — Dragonsworn Armor search takes a turn.
- **Lemonade From Lemons** (Balor) — Meal at the Inn.
- **A Change of Green-ery** (Celine) — The sprout won't grow further. Reward: cherry cobbler.
- **Farm Fresh Sous Chef** (Reina) — Cooking competition news. Reward: honey curry.
- **Working Like a Dog** (Juniper) — Help with errands.
- **Chief Inspector** (Adeline) — Inspection of Mistria from the Request Board.
- **Shield of the Realm** (March) — Part-time work at the Blacksmith.
- **A Birdhouse** (Ryis) — Build a birdhouse at the Carpenter's Shop.

### Eight-Heart Events

- **Lost Track of Time** (Adeline) — Tea at the Manor House.
- **For Good** (Balor) — Meal in his room.
- **A Lost Flower** (Celine) — Picnic.
- **A Little While Longer** (Hayden) — Time together at his house.
- **Potions and Errands** (Juniper) — Bring a Breath of Flame flower.
- **The Aldarian Cooking Contest** (Reina) — The big moment at the Inn.
- **The Glade** (Eiland) — Walk in the Deep Woods.
- **Life in This Form** (Caldarus) — Meal at his temple.
- **A Duet** (Ryis) — Bird watching at the Hawthorn tree.
- **The Panacea** (Valen) — Search for Cliffblossom at the Western Ruins.
- **Your Heart Desires** (Seridia) — Meet at her temple.

### Pregnancy Cravings

Post-marriage quests where the spouse craves a specific food:
- Adeline: Lemon Pie
- Celine: Spring Salad
- Juniper: Pizza
- Reina: Ice Cream Sundae
- Seridia: Ice Cream Sundae
- Valen: Grilled Cheese

## quests/fetch_quests.toml

Fetch quests are item-delivery requests from NPCs, organized by season and category. There are approximately 100+ fetch quests. Broad structure:

### Seasonal Fetch Quests

**Spring:** Forage requests (berries, fennel, snowdrop anemone, lemon, blueberries, wild leek), material requests (wood, stone, clay, hay), crop requests (strawberry, turnip), mines requests (copper, copper beetle, rock, red toadstool, bait), fish requests (catfish, salmon, trout), cooking requests (baked potato), crafting requests (wood fencing), bug requests (caterpillar).

**Summer:** Farming requests (tomato), forage requests (basil/thyme, coconuts, seashells), and more.

**Fall:** Forage requests (cranberries, garlic, horseradish + salmon, blackberries, chestnuts), and more.

**Winter:** Forage requests (rose hips, pineshrooms, burdock root, ice), fish requests (eel, tilapia), and more.

### Any-Season Categories

- Monster drop requests (monster powder, monster shell, shadow flower)
- Mine progression requests (copper ingot, iron ingot/ore/armor, silver ingot/ore, sapphire, emerald, crystal, tidestone, round rock)
- Animal product requests (eggs, milk, feathers, horns, wool, bristles, duck egg, horse hair)
- Crafted item requests (copper shovel, silver sword, iron watering can)
- Cooking requests (trail mix, tea, noodles, sushi, pudding, etc.)
- Bug requests (pond skater, deep earthworm, dragon horn beetle, fire wasp)
- Saturday Market requests (unlocked after various quest completions, available only on Saturdays)

### Reward Pattern

Nearly all fetch quests reward 20 renown. Additional rewards are either gold (30-960 range), recipe scrolls, or specific items.

## quests/crown_quests.toml

Crown quests are bulk shipping requests from the Crown/kingdom, all given by Adeline. Each rewards 75 renown and a gold treasure box.

20 crown quests covering: crops (30), tables and chairs (6+12), mine forageables (30), fish (40), berries (30), ingots (10 iron + 5 silver), animal materials (10 feathers + 10 wool), soup (15), stone (250), archaeology shards (15 shards + 5 shard masses), copper tools (5), golden ingredients (5 golden cheese + 5 golden mayo), baked dishes (5), stone paths (100), flowers (30), monster materials (30), grass starters (10), refined stone (20), bell berries (20), gold ingots (10).

## quests/tali_challenges.toml

Taliferro's cooking challenges. 12 challenges in fixed order, each requiring the player to turn in a specific dish. All reward 100 renown plus a kitchen crafting scroll and item:

1. Rice Ball
2. Crispy Fried Earthshroom
3. Crystal Berry Pie
4. Chocolate Cake
5. Tide Salad
6. Omelet
7. Bell Berry Bakewell Tart
8. Herb Salad
9. Incredibly Hot Pot
10. Golden Cookies
11. Veggie Sub Sandwich
12. Beet Soup (final challenge, rewards champion's kitchen)

## quests/stillwell_challenges.toml

Stillwell's monster-slaying challenges. 12 challenges in fixed order, each requiring defeat of specific monster types. All reward 100 renown plus a themed crafting scroll:

1. Green Sapling Surprise — 20 Sapling Monsters
2. Rock Clod Catastrophe — 20 Rock Clods
3. Mushroom Madness — 20 Green Mushrooms (Tide Caverns)
4. Enchantern Explosion — 20 Blue Enchanterns (Tide Caverns)
5. Staggering Stalagmites — 10 Green Stalagmites (Deep Earth)
6. Essence Gone Batty — 20 Blue Essence Bats (Deep Earth)
7. Malicious Mimics — 5 Mimics
8. Flame Spirit Shocker — 20 Flame Spirits (Lava Caves)
9. Lava Cat Conundrum — 20 Lava Cats (Lava Caves)
10. Flying Tome Trouble — 20 Flying Tomes (Ruins)
11. Rock Stack Smackdown — 20 Rock Stacks (Ruins)
12. Gryphon Grapple — 10 Gryphon Statues (Ruins)

## quests/request_board.toml

Governs when quests appear on the town request board. Structure:

- Each quest gets an entry with `requirements` (conditions to appear) and `randomly_selected` (whether it enters a random rotation or appears deterministically).
- Story quests appear deterministically based on date/progress (e.g., `do_a_bro_a_favor` requires Spring day 2; `cop_some_ore` requires mines opened).
- Heart quests appear when heart level requirements are met (e.g., `tall_dark_and_mysterious` requires Balor 2 hearts + completed `repair_the_bridge`).
- Fetch quests are `randomly_selected = true` with seasonal/progression gating (season requirements, skill levels, quest completions like `opened_mines`, `broke_water_seal`, `broke_earth_seal`, `broke_ruins_seal`, `seridia_house_open`, `unlocked_deep_woods`).
- Saturday Market fetch quests require `is_day_type = "saturday"` plus relevant quest completions.

## quests/crown_registry.toml

Defines the crown quest rotation system:
- `order`: fixed sequence of 20 crown quests
- `days_between = 7`: one crown quest available per week
- `tag_registrations`: maps item tags to display text and icons (dining_table, dining_chair, crop, mines_forageable, fishy, berry, feather, wool, soup, copper_tool, golden_mayonnaise, stone_path, flower, monster_part, baked_dish, bugs)

## quests/tali_registry.toml

Defines Taliferro's challenge order: fixed sequence of 12 cooking challenges.

## quests/stillwell_registry.toml

Defines Stillwell's challenge order: fixed sequence of 12 monster-slaying challenges.

## dates.toml

This file defines the romantic date system, not a calendar. Date types available after marriage/partnership:

- **Inn Meal Date** — Weekend meal at the Inn. Random reward from a pool of 30+ cooked dishes.
- **Deep Woods Picnic** — Weekend picnic. Random reward from a pool of 25+ desserts.
- **Beach Date** — Weekend walk. Random reward from shell pool.
- **Park Date** — Weekend visit to Eastern Road Park.
- **Gem Cutting Date** — Weekend gem cutting at the forge. Random reward from gem pool.
- **Bathhouse Date** — Weekend bathhouse visit.

Special unlisted dates: Shooting Star (festival), Wedding, Harvest Dance (festival).

Each date type specifies per-NPC visual data (expression, outfit, frame) for all 12 romanceable characters: Adeline, Balor, Caldarus, Celine, Eiland, Hayden, Juniper, March, Reina, Ryis, Seridia, Valen.

## festivals.toml (supplementary — calendar dates)

The calendar structure is implicit across the data. Seasons referenced: spring, summer, fall, winter. Days are numbered within each season. Day types include "friday" and "saturday." Festival dates from festivals.toml:

- **Spring Festival** — Spring day 17
- **Shooting Star Festival** — Summer day 28
- **Harvest Festival** — Fall day 10
- **Animal Festival** — Winter day 10

Each festival specifies location, weather override, associated quest, music, decorations, and (for some) NPC date participation requiring 4+ hearts (Seridia requires 6).

## Source Absences

- No explicit calendar definition file found (number of days per season, day names, year structure). The calendar structure is inferred from quest conditions: seasons exist, days are numbered, "friday" and "saturday" are day types, years are tracked (some quests require `reached_date` with `year = 2`).
- No quest dependency/ordering graph. Quest sequencing is implicit through `completed_quest` requirements in `request_board.toml` and renown-level gates.
- The `dates.toml` title suggests calendar data but contains romantic date activity definitions instead.
- Fetch quests file was truncated at line 1478 of 2852; approximately half the fetch quests were not individually enumerated but follow the same structural pattern.
