# Wheedle

## Basic Information

- **Name:** Wheedle
- **Aldarian Name:** WDL
- **Job:** Salesman
- **Birthday:** Winter 6
- **Dateable:** false
- **Tags:** vendor
- **Journal Portrait Offset:** [-116, -30]
- **Journal Background Color:** [255, 229, 213] (peach/salmon)
- **Date Photo Offset:** [0, 0]
- **Icon Sprite:** spr_ui_generic_icon_npc_wheedle
- **Small Icon Sprite:** spr_ui_generic_icon_npc_small_wheedle
- **Small Outlined Icon Sprite:** spr_ui_generic_icon_npc_small_outline_wheedle

## Gift Preferences

### Loved Gifts
- ancient_gold_coin
- coin_lump
- fiber
- perfect_diamond
- perfect_emerald
- perfect_gold_ore
- perfect_pink_diamond
- perfect_ruby
- perfect_sapphire
- ore_pink_diamond

### Liked Gifts
- ore_diamond
- ore_emerald
- gold_ingot
- ore_gold
- golden_alpaca_wool
- golden_bristle
- golden_bull_horn
- golden_cheesecake
- golden_cookies
- golden_duck_egg
- golden_duck_feather
- golden_egg
- golden_feather
- golden_horse_hair
- golden_rabbit_wool
- golden_sheep_wool
- dragon_forged_bracelet
- ore_ruby
- rusted_treasure_chest
- ore_sapphire

### Neutral Gifts
All gifts not in other categories and not tagged with disliked tags.

### Disliked Gift Tags
- junk
- bugs
- weird_gift

### Hated Gift
- criminal_confession

## Gossip

- **Line key:** wheedle_gossip
- **Portrait:** happy
- **Effect:** hearts

## Drink Preferences

- **Heart level 6:** coffee
- **Heart level 17:** wine

## Outfits

Seasonal variants: spring, summer, autumn, winter

No special outfits listed.

## Portrait Expressions

All expressions have seasonal variants for spring, summer, autumn, winter:

- neutral
- think
- happy
- wink
- mad
- embarrassed
- sad
- ugh

## Animation Data

### Idle Cycle
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **on_pause_speaking_turn:** true

### Walk Cycle
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **on_pause_speaking_turn:** true
- **on_pause_speaking:** idle
- **on_pause_background:** idle

### Blink Cycle
- **Default direction:** south
- **Directions:** south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear

### Sit Cycle
- **Default direction:** south
- **Directions:** north, south, east
- **is_seated:** true
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear

### Action Cycle
- **Default direction:** south
- **Directions:** north, south, east
- **Outfits:** spring, summer, autumn, winter
- **Type:** linear
- **last_frame_hold:** [240, 360]
- **on_pause_speaking:** idle

## Animation Offsets

- **Portrait:** [-127, -65]
- **Sweat:** [5, -16]
- **Hearts:** [5, -16]
- **Angry:** [3, -16]
- **Sparkles:** [1, -27]
- **Sparkles Dark:** [1, -27]
- **Sick:** [0, -16]
- **Music Notes:** [0, -27]
- **Intensity:** [2, -26]
- **Surprise:** [33, 0]
- **Shock:** [6, -24]
- **Sigh:** [0, -23]
- **Loud:** [3, -13]
- **Cheery:** [2, -18]
- **Drop:** [8, -26]

## Vendor Inventory (from stores.toml)

**Store Name:** Wheedle's Stall

### Category 1: Consumables
Icon: spr_ui_store_category_icon_consumables

Constant stock:
- poison_snake_oil
- fire_snake_oil
- ice_snake_oil

### Category 2: Player Cosmetics
Icon: spr_ui_store_category_icon_player_cosmetics

Target selections: 25 (randomly selected from pool each refresh)

Random stock pool:
- head_crown
- back_gear_sheathed_sword
- back_gear_mini_wings
- back_gear_ornate_round_shield
- back_gear_ornate_shield
- suit_court
- dress_court
- head_dancer_flower
- top_dancer
- skirt_dancer
- back_gear_rogue_cape
- head_rogue_hood
- pants_rogue
- shoes_boots_rogue
- top_rogue
- back_gear_hunter_bow
- back_gear_hunter_cape
- head_hunter_hat
- pants_hunter
- shoes_boots_hunter
- top_hunter
- head_halo

### Category 3: Furniture
Icon: spr_ui_store_category_icon_furniture

Constant stock:
- animated_snow_globe
- animated_bird_fountain
- deluxe_storage_chest_pink
- deluxe_storage_chest_red
- deluxe_storage_chest_orange
- deluxe_storage_chest_gold
- deluxe_storage_chest_green
- deluxe_storage_chest_aqua
- deluxe_storage_chest_blue
- deluxe_storage_chest_purple
- deluxe_storage_chest_black
- deluxe_storage_chest_gray
- deluxe_storage_chest_white
- deluxe_storage_chest_light_brown
- deluxe_storage_chest_dark_brown
- deluxe_icebox_white
- deluxe_icebox_pink
- deluxe_icebox_blue
- deluxe_icebox_yellow
- deluxe_icebox_green
- teleportation_pad (requires: has_upper_floor = true)

### Category 4: Miscellaneous
Icon: spr_ui_crafting_category_icon_misc

Constant stock:
- bath_soap (requires: is_dating_someone = true, seen_cutscene = "elsie_dating_tutorial")
- fast_food
