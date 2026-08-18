---
type: reference
title: Stillwell — Schedule and Events
description: 'Daily schedule patterns by season and all cutscene/quest appearances with
  context. Sources: schedule files and cutscene data.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade Two/u2_spring_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade Two/u2_summer_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade Two/u2_fall_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade Two/u2_winter_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/basement_schedule.s.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Story Events/Town Repair/upgrade_the_saturday_market_plaza.c.toml
---

# Stillwell — Schedule and Events

## Daily Schedule

### Non-Saturday / Non-Market Days

**All seasons, all days except Saturday:**

Stillwell's default location is `aldaria/default` starting at 6:00 AM (from `basement_schedule.s.toml`). He resides in Aldaria when not working the market. He has no weekday schedule in Mistria.

### Saturday Market Schedule

**Prerequisites (all seasons):**
- Day of week: Saturday
- Weather: pleasant
- Quest complete: repair_the_bridge
- Quest complete: upgrade_the_saturday_market
- Quest complete: upgrade_the_saturday_market_plaza

**Spring (no season restriction in the spring file — serves as fallback):**
- 6:00 AM — Arrives at booth (`town/Stillwell`)
- 9:32 PM — Begins packing up (routine: `stillwell_packing`)

**Summer:**
- 6:00 AM — Arrives at booth (`town/Stillwell`)
- 8:55 PM — Begins packing up (routine: `stillwell_packing`)

**Fall:**
- 6:00 AM — Arrives at booth (`town/Stillwell`)
- 9:32 PM — Begins packing up (routine: `stillwell_packing`)

**Winter:**
- 6:00 AM — Arrives at booth (`town/Stillwell`)
- 8:55 PM — Begins packing up (routine: `stillwell_packing`)

### Schedule notes
- Stillwell only appears in Mistria on Saturdays in pleasant weather.
- He arrives early (6 AM) and stays until late evening.
- Summer and winter have earlier pack-up times (8:55 PM) vs. spring and fall (9:32 PM).
- On non-market days, he is in Aldaria (the broader world) and inaccessible to the player.

## Cutscene Appearances

### Upgrade the Saturday Market Plaza

**Source:** `Cutscenes/Story Events/Town Repair/upgrade_the_saturday_market_plaza.c.toml`

**Quest trigger:** Renown level 80, at least 1 day after completing "upgrade_the_carpenters_shop."

**Summary:** Nora and Adeline meet with the player and local tradespeople (Landen, March, Olric, Ryis) to discuss expanding the Saturday Market to accommodate new vendor applicants. Stillwell is discussed but does not appear in person.

**What is said about Stillwell:**

Adeline introduces him:
> "In close second is Stillwell. He's a fortune teller-"

March immediately reacts:
> "Oh please."

Adeline defends him:
> "Well, whatever your personal opinions are about fortune telling, he's VERY popular. Even my parents have been to see him."

Nora adds:
> "In his application he writes that it's 'vitally important' he be given a booth here."
>
> "If nothing else, I believe he could be a big draw. People travel from all over Aldaria to see him in the Capital."

**What this reveals about Stillwell:**
- He applied to the Mistria Saturday Market himself, claiming it was "vitally important" — aligns with his introduction where he says he came on "urgent business" related to the fate of the world.
- He is already famous across Aldaria; people travel to the Capital specifically to see him.
- Adeline's parents have visited him, showing broad appeal.
- March is dismissive of fortune-telling, suggesting skepticism exists about Stillwell's abilities among some townspeople.
- He is grouped with Zorel as the two new Upgrade Two vendors.

**Other characters involved:** Nora, Adeline, Landen, March, Olric, Ryis.

**Follow-up quest:** The player gathers materials (50 Voidite, 20 Refined Stone, 5 Mistril Ingots, 10 Monster Cores, 5 Monster Blocks) for the new vendor booths.

### Meet the New Vendors

**Trigger:** Letter from Nora after completing the plaza upgrade, on a Saturday.

This is a quest (not a cutscene) where the player is invited to meet Stillwell and Zorel at the market. Stillwell's first-meeting conversation (`greeting_ari`) plays during this quest.

## Quest Involvement

Stillwell's primary gameplay role is posting Missions to the Mission Board. From his introduction:

> "I'll update it with Missions for you as I come to see these potential futures."

He uses his precognition to identify monster threats spawning from the Gate Between Worlds and creates missions for the player to address them. This is his stated reason for coming to Mistria, distinct from his fortune-telling business.
