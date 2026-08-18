# Merri - NPC Data Profile

## Identity

- **Name:** Merri
- **Aldarian Name:** MR
- **Job:** Furniture Vendor
- **Tags:** vendor
- **Dateable:** false
- **Birthday:** Fall 6

## Gift Preferences

### Loved Gifts
- golden_alpaca_wool
- golden_bristle
- golden_bull_horn
- golden_duck_feather
- golden_horse_hair
- golden_rabbit_wool
- golden_feather
- golden_sheep_wool
- perfect_diamond
- perfect_pink_diamond

### Liked Gifts
- alpaca_wool
- basic_wood
- bristle
- bull_horn
- clay
- coral
- crystal
- ore_diamond
- duck_feather
- glass
- hard_wood
- horse_hair
- latte
- obsidian
- paper
- ore_pink_diamond
- rabbit_wool
- feather
- sheep_wool
- ore_stone

### Neutral Gifts
(No specific items listed; default category)

### Disliked Gifts
- Tags: junk, bugs, weird_gift

### Hated Gift
- snail

## Drink Preferences

- Heart level 6: coffee
- Heart level 17: wine

## Gossip

- Line key: merri_gossip
- Portrait: happy
- Effect: hearts

## Outfits

- spring
- summer
- autumn
- winter

(No special outfits listed beyond seasonal variants.)

## Portrait Expressions

All expressions have seasonal variants for spring, summer, autumn, and winter:

- neutral
- think
- happy
- wink
- mad
- embarrassed
- sad
- ugh

## Journal and UI Data

- **Journal portrait offset:** [-112, -39]
- **Journal background color:** [255, 225, 201]
- **Date photo offset:** [0, 0]
- **Icon sprite:** spr_ui_generic_icon_npc_merri
- **Small icon sprite:** spr_ui_generic_icon_npc_small_merri
- **Small outlined icon sprite:** spr_ui_generic_icon_npc_small_outline_merri

## Animation Data

### Portrait Offsets
- portrait: [-124, -65]

### Effect Offsets
- sweat: [-9, 10]
- hearts: [-9, 10]
- angry: [-5, 7]
- sparkles: [-3, 6]
- sparkles_dark: [-3, 6]
- sick: [-4, 10]
- music_notes: [-3, 6]
- intensity: [-2, -3]
- surprise: [0, 5]
- shock: [2, 4]
- sigh: [-5, 4]
- loud: [4, 6]
- cheery: [0, 11]
- drop: [-5, 5]

### Animation Cycles

**Idle:**
- Default direction: south
- Directions: north, south, east
- Outfits: spring, summer, autumn, winter
- Type: linear
- on_pause_speaking_turn: true

**Walk:**
- Default direction: south
- Directions: north, south, east
- Outfits: spring, summer, autumn, winter
- Type: linear
- on_pause_speaking: idle
- on_pause_background: idle

**Blink:**
- Default direction: south
- Directions: south, east
- Outfits: spring, summer, autumn, winter
- Type: linear

**Action:**
- Default direction: south
- Directions: south, east, north
- Outfits: spring, summer, autumn, winter
- Type: linear
- last_frame_hold: [240, 360]
- on_pause_speaking: idle

## Vendor Inventory (Merri's Stall)

Store name: "Merri's Stall"

### Category 1: Furniture (icon: spr_ui_store_category_icon_furniture)
- target_selections: 25 (random from pool each week)
- Stock is randomized; full pool includes:

**Bakery Set:** bakery_cake_case_pastel, bakery_cake_case_coffee

**Haunted Attic Set (dusty and dark variants):** armoire, bed, double_bed, chair, dress_form, nightstand, rocking_chair, table, wall_shelf, wall_window, wallpaper, flooring

**Ornate Rugs:** ornate_rug_large_square_cream, _red, _blue

**Starry/Summit:** starry_flooring_v1, _v2, summit_wallpaper_v1, _v2

**Bathroom Set (black and white variants):** sink, bench, wall_mirror, floor_mirror, toilet, bathtub, wall_sconce, curtain_stand (7 colors), small_bathmat (8 colors), large_fluffy_rug (8 colors), round_cushioned_stool (8 colors), wall_towel (7 colors), tile_wall (4 colors), herringbone_tile_floor (3 colors), square_tile_floor

**Counters:** counter_basic_v1, _v2, counter_cabin_walnut, _oak, _cherry, counter_cake_strawberry, _chocolate, _double_chocolate, counter_cottage_v1, _v2

**Cherry Set:** wallpaper, flooring, rug, chair, table

**Lemon Set:** wallpaper, flooring, rug, stool, table

**Ornate Set (no recipes):** privacy_screen (5 variants), cabinet (4 variants), coffee_table (4 variants), wallpaper (4 variants), flooring (4 variants)

### Category 2: Decorative Items (icon: spr_ui_woodcrafting_category_icon_decorative_items)
- target_selections: 25 (random from pool each week)
- Stock is randomized; full pool includes:

**Haunted Attic Decor:** candle_single (2 variants), candle_cluster (2 variants), wall_cobweb_left (2 variants), wall_cobweb_right (2 variants)

**Bakery Decor:** bread_basket (2 variants), cake_slice (2 variants), cake (2 variants), cookie_jar (2 variants), cutting_board (2 variants)

**Picnic Set:** basket (3 colors), pie_plate (3 colors), place_setting (3 colors), rug (3 colors), donut_plate, hamburger_plate, sandwich_plate, sunflower_vase (3 colors)

**Misc Decor:** weather_crystal_ball, coffee_mug (3 variants), espresso_cup (3 variants), basket, beer_mug, boxes (3 variants), candle, candle_chamberstick, various glasses (absinthe, cocktail, lemonade, milk, water, whisky), green_bottle, jars (4 variants), notepads (2 variants), paper_stack, small_vase (4 variants), teas (2 variants), wine_glass (3 variants)

**Cherry Decor:** table_lamp, fruit_bowl, bonsai

**Lemon Decor:** table_lamp, fruit_bowl, bonsai

**Ornate Decor (no recipes):** incense_burner (4 colors), incense_stick (3 variants), ornate_vase (4 colors)

### Category 3: Furniture Recipes (icon: spr_ui_store_category_icon_furniture_recipes)
- accept_recipes: true
- target_selections: 25
- Player can sell furniture recipes back to Merri

## Barks Data

- icon: spr_ui_generic_icon_npc_small_merri
- (No specific bark text lines found in barks.toml; only icon data is present)
