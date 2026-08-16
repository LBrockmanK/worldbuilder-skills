## Round 1 — digest `8b82e14b…`, anchor `5e9e69a9` (dirty), tokens 108656, 2026-08-15T20:26:10-05:00, 369s

Anchor: 5e9e69a9b6c66d5750b4e8b165d395ed8ac83ca6 (dirty tree)
Artifact digest: 8b82e14b5591276ec2e55a73d95f494486afb1fd996d39909701e4dae4e0d98d (sha256 over the exact scoped bytes as delivered)
Scope: projects/fields-of-mistria/locations/the-inn.md, projects/fields-of-mistria/locations/mistria-town.md, projects/fields-of-mistria/locations/the-farm.md, projects/fields-of-mistria/locations/the-eastern-road.md, projects/fields-of-mistria/locations/the-deep-woods.md, projects/fields-of-mistria/locations/the-narrows.md, projects/fields-of-mistria/locations/the-summit.md, projects/fields-of-mistria/locations/the-western-ruins.md, projects/fields-of-mistria/locations/the-beach.md, projects/fields-of-mistria/locations/sweetwater-farm.md, projects/fields-of-mistria/locations/the-manor.md, projects/fields-of-mistria/locations/the-blacksmith.md, projects/fields-of-mistria/locations/the-bathhouse.md, projects/fields-of-mistria/locations/the-clinic.md, projects/fields-of-mistria/locations/the-museum.md, projects/fields-of-mistria/locations/caldarus-house.md, projects/fields-of-mistria/locations/seridias-house.md, projects/fields-of-mistria/locations/the-mines.md, projects/fields-of-mistria/events/harvest-festival.md, projects/fields-of-mistria/events/spring-festival.md, projects/fields-of-mistria/events/shooting-star-festival.md, projects/fields-of-mistria/events/animal-festival.md, projects/fields-of-mistria/events/friday-night-at-the-inn.md, projects/fields-of-mistria/events/saturday-market.md, projects/fields-of-mistria/concepts/town-restoration.md, projects/fields-of-mistria/concepts/the-seals.md, projects/fields-of-mistria/concepts/magic.md, projects/fields-of-mistria/concepts/artifacts.md, projects/fields-of-mistria/concepts/the-calendar.md, projects/fields-of-mistria/concepts/weather.md, projects/fields-of-mistria/concepts/farming.md, projects/fields-of-mistria/concepts/ranching.md, projects/fields-of-mistria/concepts/fishing.md, projects/fields-of-mistria/concepts/mining.md, projects/fields-of-mistria/concepts/the-museum.md, projects/fields-of-mistria/concepts/flora.md, projects/fields-of-mistria/concepts/fauna.md, projects/fields-of-mistria/concepts/the-homestead.md

1. Valen is repeatedly misgendered
   Location: projects/fields-of-mistria/locations/the-clinic.md:3,11
   Quote: “*Where Valen heals what he can and studies what he cannot.*” / “The ground floor serves as Valen's medical practice — a desk for consultations, a bed for patients, and a corner where he sometimes watches over children.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Valen uses she/her pronouns. Both masculine references provide incorrect character information to downstream roleplay.

2. Saturday Market simultaneously has eight and fewer than eight vendors
   Location: projects/fields-of-mistria/events/saturday-market.md:18-22
   Quote: “Every Saturday, eight vendors set up stalls around the town square.” / “The market starts modest. Early on, a handful of familiar faces run the stalls. As the town is restored and the market is formally upgraded, new vendors arrive and the selection expands.” / “A story quest early on introduces the player to the original four vendors: Merri, Darcy, Vera, and Louis. Later, Stillwell, Taliferro, Wheedle, and Zorel join after additional restoration work.”
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The unconditional “Every Saturday” statement contradicts the later progression in which only four vendors attend initially. It must be qualified as the fully expanded market or rewritten to reflect the current restoration state.

3. The documents disagree about the deepest mine environment
   Location: projects/fields-of-mistria/locations/the-mines.md:11; projects/fields-of-mistria/concepts/mining.md:11,19
   Quote: “At the lowest levels, the Lava Caves burn with subterranean heat.” / “The mines beneath the Narrows descend through five distinct environments” / “**The Ruins** — Ancient constructed spaces at the deepest level.”
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: One document identifies the Lava Caves as the lowest level, while another places the Ruins below them as the fifth and deepest environment. The location document’s hierarchy needs to include the Ruins below the Lava Caves.

4. The Harvest Festival competition is misdescribed as a crop showcase
   Location: projects/fields-of-mistria/events/harvest-festival.md:20,28
   Quote: “The competition is a harvest showcase — participants present what they've grown, and the town judges the results.” / “Queen berry season peaks around the festival, and the advance notice is a natural prompt to start gathering them.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The event’s challenge is based on collecting Queen Berries, not presenting crops participants have grown. This substitutes a different festival activity and will generate incorrect scenes.

5. Soundtrack implementation metadata permeates the entity documents
   Location: every scoped location document’s `Music` section; every scoped event document’s `Setting` section
   Quote: “- Default: "Music/Location Tracks/InnLessBusy"” / “- Basement: "SoundEffects/Environment/ValenBasementLoop"” / “- **Music:** "Music/Events/ShootingStarNight" (plays across the entire world at night)” / “- No dedicated location track.”
   Type: other
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Asset identifiers, sound-effect paths, world playback rules, and notes about absent tracks are implementation data rather than roleplay scene-setting. This directly violates criterion 2 across all 18 location documents and all six event documents.

6. The Farm location explains upgrade mechanics
   Location: projects/fields-of-mistria/locations/the-farm.md:11-13
   Quote: “A shipping box near the road connects the farm's output to the wider world.” / “The farmhouse itself starts modest and can be extended with wings and an upper floor. A greenhouse allows year-round growing, sealed off from the seasons outside.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Shipping, house-upgrade paths, and greenhouse season bypasses are player-system explanations. They should be recast as the homestead’s present physical condition and atmosphere.

7. Harvest Festival reads as relationship and preparation guidance
   Location: projects/fields-of-mistria/events/harvest-festival.md:22,28
   Quote: “Anyone can invite someone to dance with them, and whether they accept depends on the relationship — a casual acquaintance will politely decline, while a close friend or romantic interest will say yes.” / “The player should be notified in advance so they can prepare too.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: These passages expose acceptance gating and tell the system when to notify the player. That is game-guide behavior rather than an in-world account suitable for scene generation.

8. Spring Festival explicitly documents a game mechanic
   Location: projects/fields-of-mistria/events/spring-festival.md:18,22,26
   Quote: “The results are cumulative — the better the town does collectively, the more the square transforms.” / “There is no date mechanic at this festival” / “The player should be warned in advance so they can gather flowers and prepare their contribution.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Cumulative result tiers, explicit absence of a “date mechanic,” and player-warning instructions make this a systems guide. The prose should describe the celebration and its visible variations in-world.

9. Shooting Star Festival exposes relationship gates and branching
   Location: projects/fields-of-mistria/events/shooting-star-festival.md:20,22,26
   Quote: “Whether they accept depends on the closeness of the relationship — a near-stranger will turn it down, but a friend will say yes. A partner gets a different, more personal response.” / “Going alone is also an option.” / “The player should be notified in advance so they have time to decide who to invite and prepare a star brooch.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The document enumerates acceptance conditions, partner branches, the solo branch, and notification timing. Those are gameplay mechanics, not roleplay scene-setting.

10. Animal Festival documents inventory gating and player preparation
   Location: projects/fields-of-mistria/events/animal-festival.md:22,26
   Quote: “What is available depends on which animals the player has raised.” / “The festival is announced a few days in advance, giving the player time to groom and prepare their animals.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Conditional shop inventory and preparation instructions expose game-state behavior. They should be replaced with in-world descriptions of the stall, judging, and festival anticipation.

11. Friday Night at the Inn describes tutorial sequencing
   Location: projects/fields-of-mistria/events/friday-night-at-the-inn.md:20,24,28
   Quote: “This is where gossip spreads, friendships deepen, and the player learns what is really going on in town.” / “early in the story, a special introductory event welcomes the player to their first Friday Night” / “For the player, it is the easiest way to feel like part of the community.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The text explains the event’s tutorial function and player utility instead of remaining in the world’s perspective.

12. Saturday Market documents quests, unlocks, and request availability
   Location: projects/fields-of-mistria/events/saturday-market.md:20-26,30
   Quote: “As the town is restored and the market is formally upgraded, new vendors arrive and the selection expands.” / “A story quest early on introduces the player” / “Some fetch requests from townsfolk are only available on market days.” / “For the player, it is the weekly shopping trip”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Upgrade state, quest sequencing, availability gates, and player utility are guide content. The market can still evolve narratively without exposing these systems.

13. Town Restoration uses unlock and farming-sim terminology
   Location: projects/fields-of-mistria/concepts/town-restoration.md:22-24,35
   Quote: “a full restoration unlocks the inventory the town actually needs.” / “opens goods processing. Raw products can be refined into higher-value items” / “Town restoration gives the farming-sim loop a purpose beyond personal wealth.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Inventory unlocking, product-value processing, and “farming-sim loop” are explicitly game-facing. They break both the roleplay detail criterion and the shared in-world register.

14. The Seals documents progression order and item requirements
   Location: projects/fields-of-mistria/concepts/the-seals.md:15,21
   Quote: “The progression runs Water, Earth, Fire, Ruins, and finally Void — though in freeform the order can bend to the story's needs. Breaking a seal requires gathering items native to that domain: creatures, minerals, plants, and fish” / “The Dragonsworn Tablet on the lowest floor is the final piece — reaching it requires not just breaking seals but building trust”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: This gives an unlock sequence, fetch requirements, a floor milestone, and permission to bend progression. Those are scenario-running/game-guide instructions rather than lore.

15. Magic is presented as a player ability list
   Location: projects/fields-of-mistria/concepts/magic.md:11,13-19
   Quote: “the player learning to cast spells is unusual” / “## The five spells” / “**Full Restore** — A healing wave that mends exhaustion and injury. The kind of magic that keeps you on your feet when the mines go deep.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The enumerated ability catalogue and player-progression framing read like a skill guide. An in-world account could retain the known forms of magic without presenting them as the player’s unlocked toolkit.

16. Artifacts describes loot pools and collection progression
   Location: projects/fields-of-mistria/concepts/artifacts.md:17,21
   Quote: “The dig sites across the region each yield their own pools.” / “Donating them to the museum builds a visible record of the region's buried history — and the deeper the player digs, the stranger and more significant the objects become.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Pools,” donation progression, and depth-based reward escalation describe collectible-distribution mechanics rather than the artifacts’ in-world significance.

17. The Calendar explains NPC and player systems
   Location: projects/fields-of-mistria/concepts/the-calendar.md:17,21
   Quote: “NPCs swap outfits with the seasons, adjust their routines, and respond to the weather.” / “they shape what the player can do on any given day and create natural arcs of activity: planting seasons, harvest windows, fishing runs, foraging opportunities.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “NPCs” and constraints on player activities are game-system terminology. The same facts can be expressed through how townspeople dress and how seasonal work changes.

18. Weather exposes generation frequency
   Location: projects/fields-of-mistria/concepts/weather.md:11
   Quote: “But four to six days each season bring inclement weather: rain in spring, summer, and fall; snow in winter. Heavy storms roll in less often”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The exact number of inclement-weather days is occurrence-rate metadata analogous to the prohibited spawn-rate example. Roleplay prose only needs the seasonal pattern and relative rarity.

19. Farming explains failure conditions and economy loops
   Location: projects/fields-of-mistria/concepts/farming.md:11,15,21
   Quote: “planting the wrong thing at the wrong time means nothing comes up.” / “Greenhouses bypass seasonal constraints” / “Farming is the player's economic foundation and daily anchor.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Crop failure rules, season bypassing, and player-economy framing make this a farming guide rather than roleplay scene-setting.

20. Ranching is a mechanics walkthrough
   Location: projects/fields-of-mistria/concepts/ranching.md:15,19,21
   Quote: “The player needs animal housing on their farm — a coop for small animals” / “Animals that are well cared for over time produce finer goods. Breeding introduces variety: rare color variants appear” / “Small animals — chickens, ducks, rabbits, capybaras — can be picked up and carried.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Prerequisites, output-quality progression, breeding variants, and interaction affordances are detailed gameplay rules.

21. Fishing reveals passive-catch and rare-condition mechanics
   Location: projects/fields-of-mistria/concepts/fishing.md:15-17,21
   Quote: “Fish traps work passively, catching whatever wanders in overnight. Legendary fish appear only under specific rare conditions: a blizzard, a thunderstorm, cherry blossoms on the wind.” / “Weather-dependent fish reward paying attention to the world's rhythms.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: This tells the player how passive traps and legendary-fish conditions work and describes them in reward terms. It is actionable guide content.

22. Mining is organized as a level-by-level resource guide
   Location: projects/fields-of-mistria/concepts/mining.md:13-19,23
   Quote: “## The five levels” / “Copper and iron are found here” / “Silver and gold veins thread through the walls.” / “Practically, it supplies the ores, gems, and materials that fuel the town's restoration and the player's livelihood.”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The document inventories resources and threats per progression tier, then explains their player-economy function. That structure serves navigation and resource optimization rather than roleplay.

23. The Museum concept exposes collection-state mechanics
   Location: projects/fields-of-mistria/concepts/the-museum.md:11,22
   Quote: “It starts sparse and fills as the player donates specimens and artifacts from across the region. Each donation adds to a visible, growing record” / “Completing the museum means understanding Mistria more thoroughly”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Donation-driven display state and museum completion are collectible progression mechanics, not solely in-world museum lore.

24. Fauna contains combat behavior and vulnerability data
   Location: projects/fields-of-mistria/concepts/fauna.md:16-19,24
   Quote: “Green mushrooms explode when defeated. Blue essence bats are stronger and faster than their upper-level cousins.” / “Flame spirits drift and teleport, firing homing projectiles.” / “Void cats lurk in the darkness, vulnerable to light.” / “Fighting through them is part of understanding the place”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Defeat effects, relative enemy strength, projectile behavior, and vulnerabilities are combat-guide information expressly outside the requested detail level.

25. The Homestead addresses players and prescribes freeform branches
   Location: projects/fields-of-mistria/concepts/the-homestead.md:15,19
   Quote: “There's no fixed path: some players will expand the house first; others will build animal housing before they even have a proper kitchen.” / “A player who spends most of their time in the mines, or fishing at the beach, or socializing in town still lives here”
   Type: other
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: This is advice about playstyles and construction-order branches, not an in-world description of the homestead.

26. The three entity types do not share one voice
   Location: projects/fields-of-mistria/locations/the-western-ruins.md:15-17; projects/fields-of-mistria/events/spring-festival.md:22; projects/fields-of-mistria/concepts/town-restoration.md:35
   Quote: “There is a sense of listening here — as though the earth has something to say and the dig is the act of leaning closer.” / “There is no date mechanic at this festival” / “Town restoration gives the farming-sim loop a purpose beyond personal wealth.”
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Locations use immersive, lyrical world prose, while events and concepts abruptly switch to design-document language such as “date mechanic,” “player,” “NPCs,” and “farming-sim loop.” This directly violates the requirement that all three entity types use the same voice/register.

FINDINGS: 0 critical, 26 major, 0 minor, 0 nit

### Adjudication

All 26 accepted. Findings 6-26 share one root cause: builder-produced
documents used game-guide voice instead of the in-world register
established in the three hand-revised vertical slices (the-inn.md,
harvest-festival.md, town-restoration.md). The fix is systematic: rewrite
all builder-produced events and concepts to match that register.

- **1 (Valen pronouns):** accept, fix — use they/them (pronouns not confirmed in source data)
- **2 (vendor count):** accept, fix — qualify as the full market or drop the number
- **3 (mine ordering):** accept, fix — Ruins is below Lava Caves
- **4 (harvest misdescription):** accept, fix — competition details are freeform in our version; rewrite to avoid claiming it's a crop showcase. Queen berry gathering lead-up is intentional per user direction
- **5 (music asset paths):** accept in part — replace engine paths with track names from soundtrack-index.md. Music sections stay (user-directed ainime OST integration)
- **6-25 (game-guide language):** accept all — rewrite to in-world voice. Lead-up sections and player notification stay (user-directed) but reframed in-world. Remove: "the player," "NPCs," "farming-sim loop," "date mechanic," "unlocks," exact spawn/frequency numbers, combat stats, prerequisite gates, tutorial sequencing
- **26 (voice inconsistency):** accept — meta-finding resolved by fixing 6-25

