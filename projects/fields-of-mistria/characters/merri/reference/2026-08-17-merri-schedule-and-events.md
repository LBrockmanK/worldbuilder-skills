# Merri - Schedule and Events

## Daily Schedule

Merri only appears in Mistria on Saturdays during the Saturday Market. She has no weekday schedule entries in the game data. On non-Saturday days and non-market conditions, she is not present in town.

### Saturday Market Schedule (All Seasons)

The Saturday Market requires: day = Saturday, weather = pleasant, quest_repair_the_bridge_complete = true.

Merri's schedule is identical across all four seasons:

| Time | Location | Activity |
|------|----------|----------|
| 6:00 AM | town/Merri | At her market stall (vendor) |
| 8:13 PM | town/Merri | Begins packing routine (merri_packing) |

She arrives at her stall at 6:00 AM and sells furniture all day. At 8:13 PM she transitions to her packing routine at the same location. She does not visit any other locations (inn, homes, etc.) during the Saturday schedule -- she remains at her stall the entire day.

### Basement Schedule

Merri has a basement schedule entry where all NPCs are sent to "aldaria/default" at 6:00 AM. This appears to be a fallback/override schedule with full NPC coverage.

### Notable Schedule Observations

- Merri is the only vendor who stays exclusively at her stall with no evening social activities in town (Darcy, Louis, and Vera also stay at their stalls but have packing routines starting at different times)
- Her packing time (8:13 PM) is earlier than some other vendors (Louis packs at 8:21-9:11 PM depending on season, Vera at 8:35-9:11 PM)
- She has no home location in Mistria -- she appears to travel in from elsewhere, consistent with her dialogue about "travel" and "getting home"

## Festival Appearances

### Animal Festival

Merri attends the Animal Festival with the following schedule:

| Time | Location |
|------|----------|
| 6:00 AM | town/af_east_chat_2 |
| 2:08 PM | town/af_large_booth_2 |
| 4:11 PM | town/af_podium_chat |
| 8:36 PM | inn/Storyteller Duo 1 |

She moves through the festival grounds throughout the day: starting at an eastern chat area, visiting a large booth, then the podium chat area, and finally going to the inn in the evening (Storyteller Duo 1 position). This is one of the few times Merri is seen at the inn.

## Cutscene Appearances

### Animal Festival - Large Animal Bracket Results

Merri's horse, **Swiftwind**, is a recurring competitor in the Animal Festival's large animal bracket. Swiftwind appears in every outcome variant:

**When player places 1st:** Swiftwind takes 3rd place.
> [happy] "Wow! Thank you everyone!"

**When player places 2nd:** Swiftwind takes 3rd place.
> [happy] "Wow! Thank you everyone!"

**When player places 3rd:** Swiftwind takes 2nd place.
> [happy] "Wow! Thank you everyone!"

**When player does not place:** Swiftwind takes 2nd place.
> [happy] "Wow! Thank you everyone!"

Merri's response is the same regardless of Swiftwind's placement -- always gracious and happy. The data reveals Merri owns a horse, which connects to her needing a horse to transport furniture to the Saturday Market.

### Josephine's Cooking Class

Merri is listed in the can_talk actions for the animal festival ceremony scenes (she's freed up to be talked to after the cutscene), but she does not have a speaking role in Jo's cooking class. She is not a participant in that event.

## Quest Involvement

No quest-specific data for Merri was found in the searched files. Her presence depends on the bridge repair quest being complete (which enables the Saturday Market), but she has no personal quest lines in the available data.

## Key Observations for Card Writing

1. **Merri is not a Mistria resident.** She travels to Mistria specifically for the Saturday Market and departs afterward. She has no home, bedroom, or weekday schedule in town.

2. **She owns a horse named Swiftwind** that she enters in the Animal Festival's large animal bracket. This horse likely also serves as her transportation for hauling furniture.

3. **Her social connections are commercial and craft-based.** She interacts with Mistria residents primarily through the market: learning carpentry from Ryis and Landen, getting furniture sourced through Balor, selling to Jo and Hemlock, and potentially collaborating with Errol on color work.

4. **She is one of four travelling Saturday Market vendors** alongside Darcy, Louis, and Vera. She sells furniture and decorative items; her stock rotates weekly from a large randomized pool.

5. **Her evening after the Animal Festival** is spent at the inn (Storyteller Duo 1 position alongside Louis at Storyteller Duo 2), suggesting she may stay overnight on festival days rather than traveling home.
