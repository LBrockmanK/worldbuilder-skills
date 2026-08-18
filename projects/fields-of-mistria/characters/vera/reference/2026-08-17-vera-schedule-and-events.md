---
type: reference
title: Vera — Schedule and Events
description: 'Vera''s schedule data across all seasons and her cutscene appearances.
  She appears only on Saturday Market days and has no weekday schedule.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Schedules/Spring Schedules/spring_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Summer Schedules/summer_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Fall Schedules/fall_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Winter Schedules/winter_saturday.s.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml
---

# Vera — Schedule and Events

## Schedule Overview

Vera appears **only on Saturdays** when the Saturday Market is active. The market requires:
- Day of the week: Saturday
- Weather: pleasant
- Quest complete: quest_repair_the_bridge_complete = true
- Summer and fall schedules additionally require season = summer/fall

Vera has no weekday schedule entries in any season. She is not a Mistria resident; she is a traveling vendor who visits for the market.

## Daily Schedule by Season

All four seasons follow the same pattern with minor time variations for packing up.

### Spring Saturday
| Time | Location | Action |
|------|----------|--------|
| 6:00 AM | town/Vera | At stall (market open) |
| 8:55 PM | town/Vera | vera_packing routine |

### Summer Saturday
| Time | Location | Action |
|------|----------|--------|
| 6:00 AM | town/Vera | At stall (market open) |
| 8:35 PM | town/Vera | vera_packing routine |

### Fall Saturday
| Time | Location | Action |
|------|----------|--------|
| 6:00 AM | town/Vera | At stall (market open) |
| 8:35 PM | town/Vera | vera_packing routine |

### Winter Saturday
| Time | Location | Action |
|------|----------|--------|
| 6:00 AM | town/Vera | At stall (market open) |
| 9:11 PM | town/Vera | vera_packing routine |

**Schedule notes:** Vera's schedule is identical across all seasons: she arrives at her stall at 6:00 AM and begins packing up in the evening. The only variation is the packing time, which ranges from 8:35 PM (summer/fall) to 9:11 PM (winter). She stays at her stall location the entire day with no breaks, meals elsewhere, or evening social visits (unlike most Mistria residents who go to the Inn or visit homes after market hours). In winter she stays latest, possibly because the market opens later or she has fewer customers and more time. She has no schedule entry for leaving town, suggesting she departs off-screen or stays somewhere unspecified.

## Cutscene Appearances

### Reina's Eight-Heart Event: Aldarian Cooking Contest

**Source:** `source/t2/Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml`

**Context:** Vera serves as one of three judges for the Aldarian Cooking Contest, alongside Darcy and Taliferro. The contest is triggered as Reina's eight-heart event at the Sleeping Dragon Inn.

**What happens:**
1. Reina and the player prepare the Inn for the contest, with help from Hemlock, Josephine, Maple, and Luc.
2. Vera arrives with Darcy and Taliferro as the judging panel.
3. The judges taste three courses: Dragon Horn Mushroom & Thyme (starter), Mistrian Vegetable Curry (main), and Wildberry Pie (dessert).
4. Vera provides positive, specific feedback on each course. Taliferro is reluctantly impressed. Darcy is openly supportive.
5. Vera presses Taliferro to admit he enjoyed the food ("Out with it, Taliferro") and teases him with the nickname "Tali."
6. After deliberation, Vera formally announces the Aldarian Star award to Reina.

**Other characters involved:** Reina (contestant), player (sous chef), Hemlock, Josephine, Maple, Luc (Inn family support), Darcy (co-judge), Taliferro (co-judge).

**What it reveals about Vera:**
- She has authority and standing in the wider Aldarian culinary/cultural world, being selected as a judge.
- She knows Taliferro personally and is comfortable teasing him, suggesting they share social circles outside Mistria.
- She balances warmth with professionalism: enthusiastic but provides specific observations (flavor, aroma, crust texture).
- She is the one who delivers the official announcement, suggesting she may be the lead judge or at least the spokesperson.
- She has prior familiarity with Reina's cooking ("I always knew Reina could cook").

## Quest Involvement

Vera has no dedicated quest line. Her availability is gated behind the bridge repair quest (`quest_repair_the_bridge_complete`), which is a prerequisite for the Saturday Market to operate. Her early dialogue ("I'm so happy to be cutting hair in Mistria again" / "Gotta catch up on all the gossip I missed while the bridge was out") confirms the bridge being repaired is what allows her to resume visiting.

## Notes on Absence

Vera does not appear:
- On any weekday
- On Saturdays with bad weather
- Before the bridge repair quest is complete
- In any location other than "town/Vera" (her stall)

She has no home, bedroom, or indoor location in the game data. She is purely a Saturday Market vendor with no off-market presence except in Reina's cutscene.
