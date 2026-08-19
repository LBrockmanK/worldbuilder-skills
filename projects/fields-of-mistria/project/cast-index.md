# Fields of Mistria — Cast Index

38 characters across eight batches. All cards complete.

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
| Celine | done | dateable, general_store_family | Gardener, Codex Mistria researcher |
| Reina | done | dateable, inn_family | Head Cook, culinary competition arc |
| Nora | done | general_store_family | Supporting character — not dateable, Chamber of Commerce head |

### Batch 3: Inn family

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Josephine | done | inn_family | |
| Hemlock | done | inn_family | |
| Luc | done | child, inn_family | |
| Maple | done | child, inn_family | |

### Batch 4: Trade families

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Landen | done | carpenter_family | Semi-retired carpenter, uncle to Ryis |
| Ryis | done | dateable, carpenter_family | Carpenter, birdhouse arc |
| Olric | done | forge_family | Part-timer at forge, brother of March |
| March | done | dateable, forge_family | Blacksmith, Shield of the Realm arc |
| Dell | done | child, general_store_family | Dragon-obsessed child |
| Holt | done | general_store_family | General Store co-owner, dad jokes |

### Batch 5: Dateable townsfolk (remaining)

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Balor | done | dateable, vendor | |
| Errol | done | townsfolk | Not dateable — no heart events, date lines, or wedding in source data |
| Hayden | done | dateable | |
| Juniper | done | dateable | |
| Terithia | done | townsfolk | Not dateable — no heart events, date lines, or wedding in source data |
| Valen | done | dateable | |

### Batch 6: Vendors and supporting cast

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Darcy | done | vendor | |
| Louis | done | vendor | |
| Merri | done | vendor | |
| Stillwell | done | vendor | |
| Taliferro | done | vendor | |
| Vera | done | vendor | |
| Wheedle | done | vendor | |
| Zorel | done | vendor | |

### Batch 7: Special characters

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Caldarus | done | draconic | Arrives during game — Story Beat. Bent-rules arrival relationships with Hayden, Juniper. |
| Seridia | done | draconic | Arrives during game — Story Beat. Bent-rules arrival relationships with Juniper, Celine. |
| Dozy | done | animal | Golden retriever. Cannot talk — body language only. Relationship with Valen (pre-story). |
| Henrietta | done | animal | Cannot talk — stage directions only. Relationship with March (pecking target). |

### Batch 8: Off-screen family

| Character | Status | Tags | Notes |
|-----------|--------|------|-------|
| Darren | done | carpenter_family, off-screen | Baker in the Capital. Father of Ryis and Wynne, brother of Landen. Not in Mistria. |
| Wiscar | done | noble, off-screen | Baron of Mistria, advisor to the King in the Capital. Father of Adeline and Eiland, husband of Linnet. |
| Linnet | done | noble, off-screen | Baroness of Mistria, Crown service in the Capital. Former guild adventurer. Mother of Adeline and Eiland, wife of Wiscar. |
| Wynne | done | carpenter_family, off-screen | Baker in the Capital. Daughter of Darren, sister of Ryis, niece of Landen. |

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
