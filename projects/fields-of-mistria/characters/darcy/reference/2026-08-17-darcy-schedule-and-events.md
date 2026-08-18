---
type: reference
title: Darcy — Schedule and Events
description: 'Extracted schedule data and cutscene appearances for Darcy: Saturday
  Market patterns across all seasons, basement schedule, and appearances in Reina
  and Seridia heart events.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Schedules/Spring Schedules/spring_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Summer Schedules/summer_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Fall Schedules/fall_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Winter Schedules/winter_saturday.s.toml
- projects/fields-of-mistria/source/t2/Schedules/basement_schedule.s.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Seridia/seridia_eight_hearts.c.toml
---

# Darcy — Schedule and Events

## Daily Schedule Patterns

Darcy appears only in Saturday Market schedules and the basement (Aldaria) fallback schedule. She has no weekday schedules in the extracted data, meaning she is only present at the Saturday Market and in the basement/Aldaria context.

### Saturday Market — All Seasons

All Saturday schedules require: day_of_the_week = saturday, weather = pleasant, quest_repair_the_bridge_complete = true.

| Season | Stall Opens | Packing Begins | Notes |
|--------|------------|----------------|-------|
| Spring | 6:00 AM | 8:35 PM | Earliest packing time |
| Summer | 6:00 AM | 8:55 PM | Later packing (longer summer days) |
| Fall   | 6:00 AM | 8:55 PM | Same as summer |
| Winter | 6:00 AM | 8:55 PM | Same as summer/fall |

**Spring Saturday:**
- 6:00 AM: Arrives at "town/Darcy" (her stall location)
- 8:35 PM: Returns to "town/Darcy" with routine = "darcy_packing"

**Summer Saturday:**
- 6:00 AM: Arrives at "town/Darcy"
- 8:55 PM: Returns to "town/Darcy" with routine = "darcy_packing"

**Fall Saturday:**
- 6:00 AM: Arrives at "town/Darcy"
- 8:55 PM: Returns to "town/Darcy" with routine = "darcy_packing"

**Winter Saturday:**
- 6:00 AM: Arrives at "town/Darcy"
- 8:55 PM: Returns to "town/Darcy" with routine = "darcy_packing"

**Schedule notes:**
- Darcy's schedule is the simplest of all NPCs in the Saturday Market files. She has exactly two time slots: arrival and packing.
- She does not leave her stall during the day. No lunch break, no inn visit, no evening social time at the bar.
- Unlike other market vendors (Louis, Merri, Vera) who have separate packing routines, Darcy's packing happens at the same location as her stall.
- She has no post-market destination (no home, no inn). Her schedule simply ends at packing. This suggests she either lives off-map or her home location is not implemented in the extracted data.
- Spring has an earlier packing time (8:35 PM vs 8:55 PM for other seasons).

### Basement / Aldaria Schedule

Source: `Schedules/basement_schedule.s.toml`

- 6:00 AM: "aldaria/default"

This is a global fallback schedule that applies to all NPCs, including Darcy, when they are in the basement/Aldaria area. All NPCs share the same default position.

## Cutscene Appearances

### Reina's Eight Hearts Event — Aldarian Cooking Contest

Source: `Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml`

**Context:** Darcy serves as one of three judges (alongside Taliferro and Vera) for the Aldarian Cooking Contest, which is the centerpiece of Reina's eight-heart event.

**Darcy's dialogue as judge:**

Pre-contest:
- Darcy [neutral]: "I've been looking forward to this. Haven't ever had a bad meal at the Sleeping Dragon Inn."

Taliferro's response:
- Taliferro [mad]: "Hmph. Let's keep it professional and try for a little impartiality, Darcy."

Judging the main course:
- Darcy [neutral]: "So rich and savory, what a good start to the meal."
- Darcy [neutral]: "It's a shame I need to leave room for dessert, or I'd ask for a second helping."
- Darcy [wink]: "Are judges allowed to ask for take-home containers?"

Judging the dessert:
- Darcy [happy]: "The berries are so sweet. What a perfect taste of Mistria!"

Deliberation:
- Darcy [neutral]: "Judges, let's confer."
- Darcy [mad]: "Especially by one judge in particular..."
  (referring to Taliferro's difficult behavior during deliberation)

Announcement:
- Darcy [happy]: "Well done, both of you. I think I speak for all of the judges when I say that we'll be looking forward to where you go from here!"

**Follow-up conversation** (post-event banked line, refresh: never):
- Darcy [neutral]: "I couldn't believe it when I was nominated to help as a judge for the Aldarian Cooking Contest."
- Darcy [happy]: "It's been so fun! Aldaria has a lot of hidden cooking talent."
- Darcy [ugh]: "Too bad it means I need to work with Taliferro, though."

**What this reveals about Darcy:**
- She is respected enough in the culinary community to be chosen as a cooking contest judge.
- She is openly biased toward the Inn's food ("Haven't ever had a bad meal at the Sleeping Dragon Inn") and Taliferro calls her out for it.
- She is enthusiastic and genuine in her judging — she wants seconds, asks about take-home containers.
- She takes a leadership role ("Judges, let's confer") and pushes back on Taliferro's obstruction.
- She uses "a perfect taste of Mistria" when praising the dessert — she values local identity in food.
- Post-event, she expresses frustration about working with Taliferro (ugh expression) but frames the experience positively overall.
- She was surprised to be nominated, suggesting she does not think of herself as prominent despite her skill.

### Seridia's Eight Hearts Event

Source: `Cutscenes/Heart Events/Seridia/seridia_eight_hearts.c.toml`

**Context:** Seridia (a dragon) mentions Darcy's bakery in passing.

- Seridia [happy]: "Delivered directly from Darcy's bakery."

**What this reveals:** Seridia refers to Darcy's stall as a "bakery," and orders delivery from it. This confirms Darcy has a reputation beyond the Saturday Market stall — even the dragon knows her by name and orders from her. The fact that Seridia gets delivery suggests Darcy provides that service, at least for special customers.

## Quest Involvement

No quest-specific data for Darcy was found in the extracted files. Her Saturday Market schedule requires `quest_repair_the_bridge_complete = true`, meaning she only appears after the bridge repair quest is finished (this applies to the entire Saturday Market, not just Darcy).

## Notable Absences

- Darcy has no weekday schedule in the extracted data. She is only present on Saturdays and in the Aldaria basement fallback.
- She has no home location or bedroom destination in any schedule.
- She has no festival-specific schedule entries beyond the Saturday Market.
- She does not appear in any inn or social gathering schedules.
- Her life outside Market day is entirely off-screen in the available data.
