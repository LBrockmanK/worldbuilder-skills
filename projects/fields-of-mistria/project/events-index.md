# Fields of Mistria — Events Index

Inventory of world events for entity document creation. Covers
festivals, recurring gatherings, and story milestones that shape the
world's calendar and culture.

## Event document format

Each event's working document will contain:

- **Name and date** — display name, season, day
- **Location** — where it takes place
- **Description** — what happens, atmosphere, cultural significance
- **Activities** — competitions, shopping, performances, special mechanics
- **NPC participation** — who attends, roles, date mechanics (who you
  can invite, requirements)
- **Vendor stocks** — festival-specific items and souvenirs available
- **Rewards** — competition tiers and prizes
- **Narrative context** — how this event fits the world's culture

## Status key

- **available** — ready for document creation
- **in-progress** — being written
- **done** — document complete

## Annual festivals

| Event | Display Name | Season/Day | Location | Short Description | Status |
|-------|-------------|-----------|----------|-------------------|--------|
| spring | Spring Festival | Spring 17 | town | Flower-themed competition with tiered town decoration progression. Maple runs food stall, Nora runs souvenir stall, Elsie runs clothing stall. Five competition tiers with escalating visual upgrades — top tier replaces the town fountain. No date mechanic. | available |
| harvest | Harvest Festival | Fall 10 | town | Harvest competition with dance date mechanic. 12 dateable NPCs can be invited to dance (heart level 4 required, 6 for Seridia). March has a super-accept at heart 8. All dates share one cutscene. Nora runs souvenir stall. | available |
| shooting_star | Shooting Star Festival | Summer 28 | summit | Stargazing festival at the summit. Star brooch gift item. 12 dateable NPCs with individual watching cutscenes (unlike harvest's shared dance). Solo cutscene available. Night music across all outdoor locations. Caldarus and Seridia mechanically cannot decline. | available |
| animal | Animal Festival | Winter 10 | town | Animal showcase. Small and large animal placement contests. Nora runs souvenir stall with animal cosmetics gated by which animals the player has unlocked. No competition challenge mechanic. | available |

## Recurring events

| Event | Frequency | Location | Short Description | Status |
|-------|-----------|----------|-------------------|--------|
| friday_night | Every Friday | inn | Weekly community gathering. All townspeople come to the inn. Performances (Jo singing, Hemlock playing), storytelling, bar socializing, dining. Special schedule overrides for all NPCs. | available |
| saturday_market | Every Saturday | town | Weekly market with vendor stalls. Darcy, Louis, Vera, Merri, Stillwell, Taliferro, Wheedle, Zorel set up stalls in town. Upgraded market schedule variant exists. | available |

## Story milestones

These are one-time events that change the world state. Documented
here for cross-reference; full narrative detail lives in the story
quest references.

| Event | Trigger | Effect | Status |
|-------|---------|--------|--------|
| town_repair_bridge | Story quest | Opens eastern road access | available |
| town_repair_inn | Story quest | Restores the inn | available |
| town_repair_barn | Story quest | Restores Hayden's barn | available |
| mill_restoration | Story quest | Opens the mill for processing | available |
| saturday_market_upgrade | Story quest | Upgrades market stalls, changes NPC schedules | available |
| bell_tower_repair | Late story | Opens bell tower | available |
| general_store_repair | Story quest | Unlocks additional store inventory | available |
| seal_progression | Dragon tablet quests | Opens seal chambers sequentially (water → earth → fire → ruins → void) | available |

## Source coverage

| Reference Document | Events Covered |
|-------------------|----------------|
| Festivals — Game Festival Definitions | All 4 annual festivals (full detail) |
| Story Structure — Quests and Calendar | Story milestones, quest triggers |
| Zone Definitions and NPC Routing | Festival zone layouts in town |
| Vendor Inventory Structure | Saturday market stall operators |
| Social Texture | Festival-specific barks and letters |

## Gaps

- Friday Night at the Inn has no dedicated festival data file — it's
  defined through NPC schedules and zone definitions, not festivals.toml.
- Saturday market is defined through store assignments and upgraded
  market schedules, not as a formal event.
- Story milestones are extracted from quest data but lack prose
  descriptions of what changes visually in the world.
- No seasonal events beyond the four festivals (e.g., no birthday
  celebrations, no new year event).
