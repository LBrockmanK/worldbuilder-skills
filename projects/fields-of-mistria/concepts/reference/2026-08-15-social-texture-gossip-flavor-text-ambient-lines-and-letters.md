---
type: reference
title: Social Texture — Gossip, Flavor Text, Ambient Lines, and Letters
description: 'Broad-strokes extraction of gossip.toml, flavor_text.toml, barks.toml,
  and letters.toml: NPC social gossip chains, world atmospheric text, ambient NPC
  expressions, and in-world correspondence. No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T23:15Z
resources:
- projects/fields-of-mistria/source/fiddle/gossip.toml
- projects/fields-of-mistria/source/fiddle/flavor_text.toml
- projects/fields-of-mistria/source/fiddle/barks.toml
- projects/fields-of-mistria/source/fiddle/letters.toml
---

# Social Texture — Gossip, Flavor Text, Ambient Lines, and Letters

## Source: `source/fiddle/gossip.toml`

The file contains a single configuration line:

```
loved_chance = 0.2
```

No gossip chains, NPC gossip topics, or dialogue entries are present. The file defines only a probability parameter (`loved_chance = 0.2`) with no associated gossip content.

## Source: `source/fiddle/flavor_text.toml`

This file maps interactive sprite objects to flavor text keys. Each entry ties a sprite name (representing a physical object in a location) to a `flavor_text` string key. The file contains no actual dialogue text — only the key references. Some entries include an `override_mask` or `alternative` variant with requirements.

### Locations and their interactable objects

**Celine's Cottage** (4 objects): desk, fireplace, end table, plant shelf

**General Store Home** (3): bookshelf, dollhouse, workbench

**General Store Shop** (8): produce displays (broken/fixed variants for A and B), product shelves (broken/fixed variants for A and B)

**General Store — Dell's Room** (3): blanket fort, toy box, shelves

**General Store — Holt and Nora's Room** (3): carvings, shelf, journal

**Inn Main** (5): flower pot (broken/fixed variants share key), banner, cabinet (broken/fixed variants share key), locked door

**Inn — Balor's Room** (3): vanity, crate, lockbox

**Inn — Hemlock and Jo's Room** (3): lute, Hemlock's vanity, Jo's vanity

**Inn — Luc's Room** (3): bug net, terrarium, artwork

**Inn — Maple's Room** (3): artwork, plushies, bear

**Inn — Reina's Room** (3): stove, shelf, book

**Valen's Clinic Floor 1** (3): skeleton model, trapdoor, desk

**Valen's Clinic Floor 2** (3): bookshelf, cactus, diary

**Bathhouse Main** (5): shelf A/B/C, locker, cauldron

**Bathhouse — Juniper's Bedroom** (4): potion shelf, cauldron, desk, crystal ball

**Bathhouse — Changing Room** (3): fountain, cubbies, door

**Blacksmiths Main** (2): display, workbench

**Blacksmiths — March's Room** (3): trophy shelf, plant, trunk

**Blacksmiths — Olric's Room** (3): desk, shelf left, shelf right

**Manor House Main** (4): Adeline's bookshelf, pottery, lectern, Eiland's bookshelf

**Manor House — Dining Room** (2): portrait, door

**Manor House — Adeline's Office** (3): left bookshelf, chart, right bookshelf

**Manor House — Eiland's Office** (3): left bookshelf, right bookshelf, pony statue

**Manor House — Adeline's Bedroom** (4): bookshelf, plants, vanity, wardrobe

**Manor House — Eiland's Bedroom** (3): bookshelf, books, candy

**Manor House — Elsie's Bedroom** (3): bookshelf left, bookshelf right, wardrobe

**Carpenter's Shop Floor 1** (3): birdhouses, tools, worktable

**Carpenter's Shop Floor 2** (4): bookshelf, Ryis's desk, Landen's desk, Ryis's trunk

**Errol's Cottage** (3): bookshelf, desk, toolbox

**Museum Entry** (2): velvet rope side, velvet rope front

**Terithia's House** (3): dried fish, wall fish, shelf

**Hayden's House Main** (2): wall art, shelf

**Hayden's Room** (3): statue, nightstand, trunk

**Town Exterior** (7): clinic locked door, clinic shed boarded door, mill boarded door, stele (spring/winter variants), spring flower planter, town fountain

**Narrows Exterior** (6): mines boarded door, gryphon statues A/B/C (each with override mask), broken stairs, cave entrance

**Western Ruins Exterior** (3): broken stairs, ground tools, pit tools

**Eastern Road** (4): broken stairs with seasonal variants (spring, summer, fall, winter)

**Beach** (2): lighthouse locked door, sand castle

**Mines Entry** (2): blocked door, re-sealed door

**Hayden's Farm Exterior** (3): seesaw, small barn, small coop

**Caldarus' House** (4): clothing chest, scroll closet, desk (has alternative with `has_void_sight` requirement), hearth

**Deep Woods Graveyard** (7): cairn, graves B/C/E/F/G, priestess statue

**Dragonsworn's Glade** (8): giant tree (seasonal variants: spring, summer=fall, winter), treasure chests (open/closed, spring/winter variants), flowers

**Priestess' Quarters** (4): beds (3, all highlighted), bedroom shelf left (highlighted), workbenches NW and SE (highlighted)

**Floor 100** (2): barrier door (highlighted), crafting station fire (highlighted)

**Seridia's House** (3): shelves, treasure hoard left, treasure hoard right

### Notable patterns

- Broken/fixed variants exist for General Store shelves and produce, and Inn bar counter/cabinet — reflecting the town repair progression.
- Seasonal variants appear for the Eastern Road stairs, Deep Woods trees, Dragonsworn Glade treasures, and the town stele.
- One conditional alternative: Caldarus' desk shows different text when the player `has_void_sight`.
- Priestess' Quarters and Floor 100 objects have `highlight = true`.

## Source: `source/fiddle/barks.toml`

Barks are floating icon bubbles that appear above NPC heads during gameplay and cutscenes. The file defines bark types with optional icon overrides, sound effects, and opacity.

### Default configuration

```toml
[default]
    icon = "<n/a>"        # auto-resolved to spr_ui_bark_icon_<NAME>
    sound = "<n/a>"       # sound only plays during cutscenes
    opacity = 0.8
```

### Bark categories

**Emotional expressions** (8 types with sounds):
- `angry` — SoundEffects/Barks/BubbleAngry
- `annoyed` — SoundEffects/Barks/BubbleAnnoyed
- `cute_face` — SoundEffects/Barks/BubbleKittyFace
- `exclamation_mark` — SoundEffects/Barks/BubbleSurprised
- `heart` — SoundEffects/Barks/BubbleHeart
- `question_mark` — SoundEffects/Barks/BubbleQuestion
- `sweat_drop` — SoundEffects/Barks/BubbleDrop
- `blush` — SoundEffects/Barks/Bubble_o_o

**Silent emotional expressions** (2): `ellipses`, `sleepy`

**Animal/farming** (8): `breed_male`, `breed_female` (both with AnimalHeartTreat sound), `empty_heart`, `hungry`, `chicken`, `cow`, `horse`, `hay`

**Skill activity icons** (6): `farming`, `fishing`, `mining`, `archaeology`, `crafting`, `woodcrafting`, `cooking`

**Seasons** (4): `spring`, `summer`, `fall` (icon override to `spr_ui_bark_icon_autumn`), `winter`

**Weather** (6): `sunny`, `rainy`, `thunderstorm`, `snow`, `mist`, `heatwave`, `cherry_blossoms`

**Locations** (4): `beach`, `mountain`, `forest`, `lake`

**Items/Resources** (8): `plant_tonic`, `seed`, `coin`, `no_coin`, `book`, `gem`, `fire`, `thread`

**Mine materials** (4): `breath_of_flame`, `smoke_moth`, `firesail`, `obsidian`

**Food/Drink** (3): `yum`, `hot_drink`, `cold_drink`

**Misc** (8): `celebration`, `music`, `moon`, `stars`, `bathhouse`, `crown`, `relationship_status` (icon: `spr_ui_bark_icon_cute_face`, changes if romantic), `fish_bait`

**Numbers** (9): `one` through `nine`

**NPC portrait barks** (30 NPCs): Each NPC has a bark entry with a small portrait icon (`spr_ui_generic_icon_npc_small_<name>`). Full NPC list: Adeline, Balor, Caldarus, Celine, Darcy, Dell, Dozy, Eiland, Elsie, Errol, Hayden, Hemlock, Henrietta, Holt, Josephine, Juniper, Landen, Louis, Luc, Maple, March, Merri, Nora, Olric, Priestess, Reina, Ryis, Seridia, Stillwell, Taliferro, Terithia, Valen, Vera, Wheedle, Zorel

## Source: `source/fiddle/letters.toml`

In-game letters delivered to the player's mailbox. Each letter has: a key, `npc` (sender), `subject_line`, `local` (body text, using `[Ari]` as player name placeholder), `requirements` (conditions to receive), and optionally `quest_to_start`, `quest_to_progress`, `items` (attached items/recipes), and `can_repeat`.

### Letter categories

#### Quest-starting letters (approximately 55 letters)

Letters that trigger quests via `quest_to_start`. Major categories:

**Town infrastructure quests** (from Adeline unless noted):
- `repair_the_bridge` — spring day 3
- `repair_the_mill` — after food reserves quest
- `repair_the_summit_stairs` — after mill repair
- `repair_the_general_store` — after summit stairs
- `repair_the_beach_bridge` — from Terithia, after general store
- `replenishing_mistrias_food_reserves_1` / `_2` — food supply chain
- `repair_haydens_barn` — after food reserves pt 2
- `repair_the_inn` — after barn repair
- `stone_refinery` — renown 50, after inn repair
- `upgrade_the_saturday_market` — renown 60
- `upgrade_the_carpenters_shop` — renown 70
- `upgrade_the_saturday_market_plaza` — from Nora, renown 80
- `repair_the_bell_tower` — from Zorel, renown 90

**Relationship heart-level quests** (triggered at heart levels 2/4/6/8):

| NPC | Heart 2 | Heart 4 | Heart 6 | Heart 8 |
|---|---|---|---|---|
| Adeline | the_smell_of_drying_ink | a_rewarding_choice | chief_inspector | lost_track_of_time |
| Balor | — | an_open_book | lemonade_from_lemons | for_good |
| Celine | the_unusual_seed | water_and_soil | a_change_of_greenery | a_lost_flower |
| Eiland | the_stele | the_ruins | the_manor | the_glade |
| Hayden | a_get_together | extra_feed | real_fine_day | a_little_while_longer |
| Juniper | — | horsing_around | working_like_a_dog | potions_and_errands |
| March | surprise_me | many_hands_make_light_work | shield_of_the_realm | — |
| Reina | pie_in_the_sky | shopping_buddy | farm_fresh_sous_chef | the_aldarian_cooking_contest |
| Ryis | — (bird_song at celine h2) | a_sapling | a_birdhouse | a_duet |
| Valen | — | batch_312 | an_outside_consultant | the_panacea |
| Caldarus | — | — | — | life_in_this_form (h8) |
| Seridia | — | — | — | whatever_your_heart_desires (h8) |

**Other quest letters**: `friday_at_the_sleeping_dragon_inn` (Reina, spring day 5), `museum_donation_wanted` (Errol, spring day 2), `tea_with_hayden` (after mill repair), `unlocking_the_mines_pt_1`/`_2` (Eiland/Errol), `crafting_tutorial` (Ryis, spring day 10), `greet_the_vendors` (Nora, Saturdays after bridge), `apiaries_and_terrariums` (Luc, renown 30), `lost_and_found` (Adeline, renown 20), `meet_the_new_vendors` (Nora), `complete_the_museum` (Errol, after Mistril Star rank), `procuring_the_sealing_scroll` (Balor)

#### Recipe letters (approximately 25 letters)

Triggered by `shipped_item` requirements. Almost all from Nora. Each attaches a `recipe_scroll`.

| Trigger crop | Recipe | Sender |
|---|---|---|
| potato | baked_potato | Nora |
| turnip | sliced_turnip | Nora |
| cabbage | cabbage_slaw | Nora |
| strawberry | candied_strawberries | Nora |
| lemon | candied_lemon_peel | Nora |
| chili_pepper | spicy_water_chestnuts | Nora |
| corn | grilled_corn | Nora |
| cucumber | cucumber_salad | Nora |
| tomato | tomato_soup | Nora |
| watermelon | salted_watermelon | Nora |
| tea | rose_tea | Josephine |
| broccoli | steamed_broccoli | Nora |
| snow_peas | sauteed_snow_peas | Nora |
| peas | buttered_peas | Nora |
| carrot | braised_carrots | Nora |
| onion | onion_soup | Nora |
| sweet_potato | roasted_sweet_potato | Nora |
| pumpkin | pumpkin_stew | Nora |
| cranberry | cranberry_juice | Nora |
| beet | beet_salad | Valen |
| cauliflower | roasted_cauliflower | Nora |
| daikon_radish | simmered_daikon | Nora |
| burdock_root | braised_burdock | Nora |
| coconut | coconut_milk | Landen |
| sunflower | toasted_sunflower_seeds | Nora |
| pear | poached_pear | Elsie |
| peach | peaches_and_cream | Adeline |
| orange | orange_juice | Nora |
| apple | apple_juice | Dell |
| pomegranate | pomegranate_sorbet | Elsie |

**Museum donation recipes**: miners_mushroom_stew (Errol, upper_mines_mushroom), baked_sweetroot (Errol, sweetroot), deep_sea_soup (Reina, cave_kelp)

**Deep Woods / late-game recipes**: bell_berry_bakewell_tart (Reina), candied_walnuts (Landen), spirit_mushroom_tea (Valen), glowberry_cookies (Ryis), crystal_berry_pie (Reina)

#### Town rank milestone letters (10 letters)

All from Adeline, at renown levels 10/20/30/40/50/60/70/80/90 plus post-carpenter upgrade. Each includes reward items escalating from copper ingot to mana potion. Rank names in order: Stone Star, Copper Star, Ruby Star, Iron Star, Sapphire Star, Silver Star, Emerald Star, Gold Star, Diamond Star.

#### Shop unlock / progression letters (approximately 10 letters)

- Kitchen upgrades: Level 2 (cooking 15), Level 3 (cooking 30) — from Ryis
- Fishing rods: copper (fishing 8), iron (15), silver (20), gold (30) — from Terithia
- Tool/armor tiers: iron (mines level 21), silver (41), gold (61) — from March
- Farm buildings: medium (ranching 20), large (ranching 40) — from Ryis
- Auto-feeder (ranching 45) — from Hayden
- Seed maker — from Nora (after general store repair)
- Artifact replicator — from Errol (after completing a museum set)
- Fish trap — from Terithia (after beach bridge)
- Perpetual soup pot — from Reina (after inn repair)
- Mini mills — from Landen (after carpenter shop repair)
- Home customization — from Landen (after final home upgrade)

#### Birthday letters (39 letters)

Each romanceable NPC sends birthday letters in three tiers based on relationship status:
- Base tier (heart level 4, status undefined)
- Best friend tier (heart level 8, `<npc>_is_best_friend = true`)
- Romantic tier (heart level 8, `<npc>_is_dating` or `<npc>_is_fiance`)

NPCs with birthday letters: Adeline, Balor, Caldarus (h6 base), Celine, Eiland, Hayden, Juniper, March, Reina, Ryis, Seridia (h6 base, requires `caldarus_seridia_town`), Valen

Each tier upgrades the gift and personalizes the tone. Examples:
- March base: 4 iron ingots, terse. Best friend: 10 refined stone, warmer. Romantic: IOU for a date.
- Juniper base: pizza, dismissive. Best friend: cavern crystal lamp, playful. Romantic: "I had a dream about you."

#### Wedding gift letters (12 letters)

All from Elsie, one per spouse option. Each includes a desk, chair, and spouse-specific hobby furniture. Juniper's also includes `dozy_pet_bed`. Spouses: Adeline, Balor, Caldarus, Celine, Eiland, Hayden, Juniper, March, Reina, Ryis, Seridia, Valen.

#### Break-up letters (12 letters)

One per romanceable NPC, triggered by `<npc>_is_ex = true` and `disabled_break_up_content = false`. Each reflects the NPC's personality:
- Adeline: diplomatic, self-focused
- Seridia: "You DARE, worm?" then amused acceptance
- March: brief, awkward
- Eiland: blames it on "the romance that accompanies all major archeologic discoveries"

#### Baby cradle letters (2 letters)

From Landen, triggered by `baby_is_due`. Split into male/female variants based on which spouse (determines child gender).

#### Miscellaneous letters

- `weather_globe_letter` (Juniper) — weather crystal ball item, after stinky_stamina_potion quest
- `shooting_star_morning_letter` (Josephine) — star festival crafting recipes
- `crown_requests_unlocked` (Adeline) — at Iron Star rank
- Shooting Star Festival variants for several NPC quest lines (attended/not attended)
- `harvest_festival_patch_case` — disabled (requirements `or = []`), patch-only content
- `the_glade_hint` (Eiland) — hint to explore deeper mines, uses `invert.unlocked_deep_woods`
- `gold_ore` (Olric) — hint about gold in lower mines, uses `invert.broke_fire_seal`

## Source Absences

- **gossip.toml is effectively empty.** Only a probability parameter exists; no gossip chains, dialogue, NPC-to-NPC gossip topics, or social commentary content is present. Gossip dialogue content likely lives elsewhere (possibly in per-NPC dialogue files or a separate system).
- **flavor_text.toml contains only key references, not the actual text.** The flavor text strings themselves (what the player reads when interacting with objects) are stored in a separate localization or dialogue system, not in this file.
- **barks.toml defines bark types but contains no bark dialogue.** Barks appear to be icon-only expressions (no text content); the file is a visual/audio configuration registry.
- **letters.toml has no letters from non-NPC senders** (e.g., no royal correspondence, no anonymous letters). All mail comes from named Mistria residents.
- **No letter content from**: Darcy, Dozy, Hemlock, Henrietta, Louis, Maple, Merri, Priestess, Taliferro, Vera, Wheedle — these NPCs appear in the bark list but never send letters.
