# Fields of Mistria — Cast Index

34 characters extracted from `source/fiddle/npcs/`. Adeline is the
completed vertical-slice test; the remaining 33 need source ingestion
batched by cast group.

## Ingestion batches

### Batch 1: Noble household (Adeline's family)

- **Adeline** — DONE (vertical-slice test, review applied)
- **Eiland** — noble, townsfolk, dateable. Brother, shares the Manor.
- **Elsie** — noble, townsfolk. Great-aunt figure, retired opera singer.

### Batch 2: Friend trio + close circle

- **Celine** — townsfolk, dateable, general_store_family
- **Reina** — townsfolk, dateable, inn_family
- **Nora** — townsfolk, dateable, general_store_family

### Batch 3: Inn family

- **Josephine** — townsfolk, inn_family
- **Hemlock** — townsfolk, inn_family
- **Luc** — townsfolk, child, inn_family
- **Maple** — townsfolk, child, inn_family

### Batch 4: Trade families

- **Landen** — townsfolk, carpenter_family
- **Ryis** — townsfolk, dateable, carpenter_family
- **Olric** — townsfolk, forge_family
- **March** — townsfolk, dateable, forge_family
- **Dell** — townsfolk, child, general_store_family
- **Holt** — townsfolk, general_store_family

### Batch 5: Dateable townsfolk (remaining)

- **Balor** — townsfolk, dateable, vendor
- **Errol** — townsfolk, dateable
- **Hayden** — townsfolk, dateable
- **Juniper** — townsfolk, dateable
- **Terithia** — townsfolk, dateable
- **Valen** — townsfolk, dateable

### Batch 6: Vendors and supporting cast

- **Darcy** — townsfolk, vendor
- **Louis** — townsfolk, vendor
- **Merri** — townsfolk, vendor
- **Stillwell** — townsfolk, vendor
- **Taliferro** — townsfolk, vendor
- **Vera** — townsfolk, vendor
- **Wheedle** — townsfolk, vendor
- **Zorel** — townsfolk, vendor

### Batch 7: Special characters

- **Caldarus** — townsfolk, draconic. Arrives during game (Story Beat, not Relationship for pre-game characters).
- **Seridia** — townsfolk, draconic. Arrives during game (Story Beat, not Relationship for pre-game characters).
- **Dozy** — animal
- **Henrietta** — animal

## World info sources

For location/faction ingestion (item 10):

- `source/fiddle/locations.toml` — location data
- `source/fiddle/festivals.toml` — festival/event data
- `source/fiddle/stores.toml` — vendor locations
- `source/t2/Cutscenes/` — story and festival events
- `source/fiddle/t2_location_descriptions/` — location prose
