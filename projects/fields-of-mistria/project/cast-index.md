# Fields of Mistria — Cast Index

34 characters extracted from `source/fiddle/npcs/`. Adeline is the
completed vertical-slice test; the remaining 33 need source ingestion
batched by cast group.

## Status key

- **available** — ready for ingestion, not claimed
- **in-progress (session)** — claimed by a session; other sessions skip
- **extracted** — source ingestion complete, card not yet written
- **card-done** — card written, review not yet run
- **review-done** — review gate passed, card finalized
- **done** — complete, no further work needed

A session claims a character by changing its status to
`in-progress` and committing. On session close, update to the
appropriate completion status.

## Ingestion batches

### Batch 1: Noble household (Adeline's family)

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Adeline | done | noble, dateable | Vertical-slice test, review applied |
| Eiland | done | noble, dateable | Brother, shares the Manor |
| Elsie | done | noble | Great-aunt figure, retired opera singer |

### Batch 2: Friend trio + close circle

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Celine | review-done | dateable, general_store_family | Gardener, Codex Mistria researcher |
| Reina | review-done | dateable, inn_family | Head Cook, culinary competition arc |
| Nora | review-done | general_store_family | Supporting character — not dateable, Chamber of Commerce head |

### Batch 3: Inn family

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Josephine | available | inn_family | |
| Hemlock | available | inn_family | |
| Luc | available | child, inn_family | |
| Maple | available | child, inn_family | |

### Batch 4: Trade families

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Landen | review-done | carpenter_family | Semi-retired carpenter, uncle to Ryis |
| Ryis | review-done | dateable, carpenter_family | Carpenter, birdhouse arc |
| Olric | review-done | forge_family | Part-timer at forge, father of March |
| March | review-done | dateable, forge_family | Blacksmith, Shield of the Realm arc |
| Dell | review-done | child, general_store_family | Dragon-obsessed child |
| Holt | review-done | general_store_family | General Store co-owner, dad jokes |

### Batch 5: Dateable townsfolk (remaining)

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Balor | card-done | dateable, vendor | |
| Errol | card-done | townsfolk | Not dateable — no heart events, date lines, or wedding in source data |
| Hayden | card-done | dateable | |
| Juniper | card-done | dateable | |
| Terithia | card-done | townsfolk | Not dateable — no heart events, date lines, or wedding in source data |
| Valen | card-done | dateable | |

### Batch 6: Vendors and supporting cast

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Darcy | available | vendor | |
| Louis | available | vendor | |
| Merri | available | vendor | |
| Stillwell | available | vendor | |
| Taliferro | available | vendor | |
| Vera | available | vendor | |
| Wheedle | available | vendor | |
| Zorel | available | vendor | |

### Batch 7: Special characters

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Caldarus | available | draconic | Arrives during game — Story Beat, not Relationship for pre-game characters |
| Seridia | available | draconic | Arrives during game — Story Beat, not Relationship for pre-game characters |
| Dozy | available | animal | |
| Henrietta | available | animal | |

## World info sources

Ingested sources (reference documents in locations/, events/, concepts/):

- `source/fiddle/locations.toml` — location definitions
- `source/fiddle/t2_location_descriptions.toml` — zone definitions and NPC routing
- `source/fiddle/festivals.toml` — festival/event data
- `source/fiddle/stores.toml` — vendor inventories
- `source/fiddle/weather.toml` — seasonal weather system
- `source/fiddle/spells.toml` — magic system
- `source/fiddle/artifacts.toml` — collectible lore objects
- `source/fiddle/songs.toml` — in-world music
- `source/fiddle/gossip.toml` — NPC social gossip
- `source/fiddle/flavor_text.toml` — world atmospheric text
- `source/fiddle/barks.toml` — ambient NPC expressions
- `source/fiddle/letters.toml` — in-world correspondence
- `source/fiddle/quests/` — story, heart, fetch, and challenge quests
- `source/fiddle/dates.toml` — calendar system
- `source/fiddle/monsters/` — mine creatures
- `source/fiddle/forageables.toml` — wild flora
- `source/fiddle/museum_wings/` — museum collections
- `source/fiddle/cameos/` — visiting characters
- `source/fiddle/ranching/` — domesticated animals
- `source/fiddle/items/fish/` — fish species by habitat
- `source/fiddle/spouse.toml` — marriage mechanics
- `source/fiddle/children.toml` — child NPC system

Not yet ingested (character-specific, handled by character ingestion):

- `source/fiddle/npcs/` — per-character data (35 files)
- `source/t2/Cutscenes/` — story and festival event scripts
- `source/t2/Conversations/` — NPC dialogue
- `source/t2/Schedules/` — NPC daily routines
