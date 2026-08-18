---
type: reference
title: Louis — Schedule and Events
description: 'Extracted schedule data and cutscene appearances for Louis: Saturday
  market schedules across all seasons, animal festival, basement schedule, wedding
  cutscene references.'
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
- projects/fields-of-mistria/source/t2/Schedules/Festivals/animal_festival.s.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/wedding_0.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_reina.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Festival Events/the_animal_festival.c.toml
---

# Louis — Schedule and Events

## Daily Schedule Patterns

Louis only appears in Saturday market schedules and the basement/festival schedules. He has no weekday schedule, consistent with being a traveling vendor who visits Mistria on Saturdays.

All Saturday schedules require: pleasant weather, bridge repair quest complete.

### Spring Saturday

- **6:00 AM:** Arrives at `town/Louis` (his market stall position)
- **8:21 PM:** Begins packing routine at `town/Louis` (routine: louis_packing)

Total market hours: approximately 14 hours.

### Summer Saturday

- **6:00 AM:** Arrives at `town/Louis`
- **9:11 PM:** Begins packing routine at `town/Louis`

Total market hours: approximately 15 hours (longer summer day).

### Fall Saturday

- **6:00 AM:** Arrives at `town/Louis`
- **9:11 PM:** Begins packing routine at `town/Louis`

Total market hours: approximately 15 hours.

### Winter Saturday

- **6:00 AM:** Arrives at `town/Louis`
- **8:35 PM:** Begins packing routine at `town/Louis`

Total market hours: approximately 14.5 hours.

### Schedule Notes

Louis's schedule is the simplest of any NPC: arrive at stall, work all day, pack up. He does not visit any other location during market day (no inn trips, no socializing elsewhere). Other vendors (Darcy, Merri, Vera) have similarly simple schedules. Louis stays at his stall position the entire day until packing begins.

Unlike most NPCs, Louis has no evening social activities. He presumably departs Mistria after packing up (he is described as a traveling tailor with a workshop elsewhere).

### Basement Schedule

- **6:00 AM:** `aldaria/default`

This is a catch-all schedule that places Louis at the default Aldaria location, used when none of the seasonal Saturday conditions are met.

## Festival Appearances

### Animal Festival

Source: `Schedules/Festivals/animal_festival.s.toml`

Louis attends the Animal Festival as a guest (not as a vendor).

- **6:00 AM:** `town/af_east_chat_1`
- **1:23 PM:** `town/af_souvenir_booth_2`
- **5:42 PM:** `town/af_south_chat_3`
- **8:38 PM:** `inn/Storyteller Duo 2`

He moves between chat areas and the souvenir booth throughout the day, ending the evening at the inn as part of a "Storyteller Duo" pair (the other half is Merri at `inn/Storyteller Duo 1`).

### Animal Festival Cutscene — Louis's Rabbit, Mortimer

Source: `Cutscenes/Festival Events/the_animal_festival.c.toml`

Louis owns a rabbit named **Mortimer** that competes in the small animal bracket. In all four outcome variants:

- **Player wins 1st place:** "Louis' rabbit, Mortimer!" places 3rd. Louis [happy]: "How wonderful!"
- **Player wins 2nd place:** "Louis' rabbit, Mortimer!" places 3rd. Louis [happy]: "How wonderful!"
- **Player wins 3rd place:** "Louis' rabbit, Mortimer!" places 2nd. Louis [happy]: "How wonderful!"
- **Player does not place:** "Louis' rabbit, Mortimer!" places 2nd. Louis [happy]: "How wonderful!"

Louis always reacts the same way regardless of his rabbit's placement: a simple, happy "How wonderful!" He is a consistent placer in the competition (2nd or 3rd depending on the player's performance).

**Behavioral notes:** Louis owns and raises a rabbit (Mortimer), which fits his textile interests (rabbit wool is among his loved gifts as golden_rabbit_wool and liked gifts as rabbit_wool). His gracious, unvarying reaction to any placement suggests he enters for enjoyment rather than competition.

## Wedding Cutscenes

### General Wedding (wedding_0)

Source: `Cutscenes/Heart Events/Wedding/wedding_0.c.toml`

Louis is mentioned but does not appear on-screen with dialogue. Josephine says:

> "And besides, it was Elsie who coordinated today's wardrobe options! With Louis, of course."

This confirms Louis provides wedding fashion for the player's ceremony. Elsie coordinated the selections, drawing on Louis's expertise and likely his Capital connections.

### Reina's Wedding (wedding_reina)

Source: `Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_reina.c.toml`

Reina mentions Louis directly:

> "Mom said Louis went all out for our wedding..."
> "What do you think of the dress he made for me?"

Louis designed and made Reina's wedding dress. This is described as him going "all out," indicating he puts significant effort into special occasion work. The dress is presented as something Reina actively chose ("I'm glad I picked it then").

**Behavioral notes:** Louis's role in weddings confirms his standing as the town's go-to tailor for important occasions. His connection to Elsie (former Capital customer) and his craftsmanship are valued enough that he is entrusted with wedding attire.

## Quest Involvement

No dedicated quest files reference Louis. His presence is tied to the Saturday market system (requires bridge repair quest completion) and festival events.
