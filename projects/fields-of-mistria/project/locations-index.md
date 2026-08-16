# Fields of Mistria — Locations Index

Inventory of world locations for entity document creation. Each
location collapses sub-rooms into the parent building or area — the
grain is the place a player would name, not individual game rooms.

## Location document format

Each location's working document will contain:

- **Name and epithet** — display name and a one-line characterization
- **Physical description** — what the place looks like, atmosphere, season
  variations (wiki prose + flavor_text references)
- **Spatial context** — where it is relative to other locations, how you
  get there, what's adjacent (wiki + map_location data)
- **Residents and regulars** — who lives or works here, with role (NPC
  data + store assignments + zone activity names)
- **Activities and zones** — what happens here: seating areas, work
  stations, social spots, festival setups (zone definitions)
- **Commerce** — shops and services available, operating NPC
  (stores reference)
- **Events** — festivals, Friday Night gatherings, seasonal activities
  that take place here (festivals + schedule references)
- **Music and atmosphere** — associated tracks, ambience, weather effects
  (locations reference)
- **Narrative role** — story quests, town repair milestones, or plot
  events tied to this location (quest references)

## Status key

- **available** — ready for document creation
- **in-progress** — being written
- **done** — document complete

## Major outdoor areas

| Location | Display Name | Short Description | Status |
|----------|-------------|-------------------|--------|
| town | Mistria | Central town, hub of all commerce and social life. Manor on the hill to the north, inn and general store flanking the main road to the south, blacksmith and bathhouse around the fountain, clinic to the east. Saturday market stalls. Hosts Spring Festival, Harvest Festival, Shooting Star decor. | available |
| farm | The Farm | Player's homestead, offered in exchange for helping restore the town. Tillable land, animal buildings, shipping box. Connects south to town. | available |
| eastern_road | The Eastern Road | Road east of town leading to the Carpenter's Shop. Pond, work stations, porch conversations. Foraging area with water bugs. | available |
| deep_woods | The Deep Woods | Dense forest north/west of town. Caldarus' house, garden, ponds, bench. Unique bug types, forageables (bell berries, temple flowers, spirit mushrooms). Music: Deep Woods theme. | available |
| dragonsworn_glade | The Dragonsworn Glade | Clearing in the deep woods. Sparse — few bugs, no forageables, no dig sites. Deep Woods music. | available |
| narrows | The Narrows | Rocky area connecting town to the mines and museum. Ruins, fishing spots, kid hangout areas. NPC farming area. Multiple mist sights. | available |
| summit | The Summit | Mountain peak above town. Hosts the Shooting Star Festival viewing. Limited wildlife. | available |
| western_ruins | The Western Ruins | Archaeological dig site west of town. Seridia's house nearby. Pit excavation, artifact tarp, dig tours. Special dig sites. | available |
| beach | The Beach | Coastal area. Campfire benches, dock, picnic area, sand castles, towels. Terithia's Tackle Shop. Special dig sites, beach bugs and shells. | available |
| haydens_farm | Sweetwater Farm | Hayden's farm east of town. Barn, farm chat areas, statue, foraging. NPC farming area. | available |

## Town buildings

| Location | Display Name | Building | Short Description | Key NPCs | Status |
|----------|-------------|----------|-------------------|----------|--------|
| inn | The Inn | inn | Social hub — bar, kitchen, dining tables, performance stage, balcony. Friday Night at the Inn gathering. Hosts storytelling, music performances, cooking tutorials. | Hemlock, Josephine, Reina (family); Maple, Luc (children); Balor (room) | available |
| general_store_store | General Store | general_store | Seeds, ingredients, tools, furniture. Family home attached. | Nora, Holt (owners); Celine, Dell (family) | available |
| blacksmith_store | Blacksmith's Shop | blacksmith | Tool upgrades, armor, ores. Fireplace seating, workbench. Forge area outside in town. | Olric, March (brothers) | available |
| bathhouse | Bathhouse | bathhouse | Cauldron baths, front desk, changing room. Restores health/energy. | Juniper, Dozy | available |
| clinic_f1 | Clinic | clinic | Medical care, syrups. Where player wakes after fainting in mines. Babysitting area. Basement with mysterious ambience. | Valen | available |
| manor_house_entry | Manor House | manor_house | Noble household on the hill. Dining room, offices, bedrooms, couch area. Garden and gazebo outside. | Adeline, Eiland, Elsie | available |
| museum_entry | Museum | museum | Four collection wings (archaeology, insect, fish, flora). Chat areas, desk. | — | available |
| mill | The Mill | mill | Goods processing (milk → cheese/butter). Unlocked via story quest. Windmill ambience. | — | available |
| bell_tower_f1 | Bell Tower | bell_tower | Unlocked late in main story. Woodcrafting workbench in courtyard outside. | — | available |

## Outlying buildings

| Location | Display Name | Area | Short Description | Key NPCs | Status |
|----------|-------------|------|-------------------|----------|--------|
| landens_house_f1 | Carpenter's Shop | eastern_road | Carpentry, furniture, materials, building plans. Kitchen, worktable, register. | Landen, Ryis | available |
| terithias_house | Tackle Shop | beach | Fishing rods, fish, cooking recipes. Couch seating. | Terithia | available |
| haydens_house | Hayden's Shop | haydens_farm | Animal supplies, accessories, toys. Bench, living room, table. | Hayden | available |
| celines_room | Celine's Cottage | town (south) | Celine's home just outside town. Living room with armchair and couch. | Celine | available |
| errols_bedroom | Errol's Cabin | narrows | Errol's solitary home in the narrows. | Errol | available |
| caldarus_house | Caldarus' House | deep_woods | Dragon scholar's house. Firepit with poufs, scroll shelves, dragon statue, tree areas. Tea service. Deep Woods music. | Caldarus | available |
| seridias_house | Seridia's House | western_ruins | Seridia's home near the ruins. Back room with void ambience. Personal NPC music track. | Seridia | available |

## Mines and dungeons

| Location | Display Name | Short Description | Status |
|----------|-------------|-------------------|--------|
| mines_entry | Mines Entrance | Gateway to the underground. Cave ambience, day/night music. Connects to narrows. | available |
| dungeon | The Mines | Multi-level dungeon: Upper Mines (floors 1-19), Tide Caverns (21-39), Deep Earth (41-59), Lava Caves (61-79). Monsters, forageables, ores, fish. Mine bugs. | available |
| seals | The Seals | Five elemental seal chambers (Water, Earth, Fire, Ruins, Void). Story progression locations. Seal music and cave ambience. | available |
| priestess_quarters | The Priestess' Quarters | Seridia's underground chambers. Void ambience, no music. Has farmable soil. | available |
| secret_caves | Secret Caves | Narrows Cave and Beach Cave. Hidden locations, no tilemap replacement. | available |

## Player spaces

Player home and farm buildings are documented as part of The Farm
location rather than as separate entities — they're customizable
spaces without fixed world lore.

## Source coverage

| Reference Document | Locations Covered |
|-------------------|-------------------|
| Game Location Definitions | All — properties, music, building assignments |
| Zone Definitions and NPC Routing | 30 locations with activity zones |
| Vendor Inventory Structure | 12 store locations |
| Weather | Affects all outdoor locations |
| Festivals | town, summit (Shooting Star) |
| Story Structure | Mines/seals, town repair locations |
| Wiki (Mistria page) | Town buildings — prose descriptions, spatial layout |

## Gaps

- No prose location descriptions in game data — wiki is the primary
  source for physical descriptions and spatial relationships.
- Wiki covers town buildings well but has limited coverage of
  outlying areas (deep woods, western ruins, eastern road).
- No location-specific dialogue extracted yet — NPC conversations
  that reference places are in character-specific sources.
- Aldaria appears in locations.toml with no properties and no wiki
  page. Purpose unknown.
