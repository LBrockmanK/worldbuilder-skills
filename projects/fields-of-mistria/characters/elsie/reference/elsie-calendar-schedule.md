# Elsie — Calendar & Schedule

## Sources

- `t2/Conversations/Bank/Elsie/Banked Lines/` — all 66 banked dialogue files (schedule-relevant triggers extracted)
- `fiddle/npcs/elsie.toml` — animation cycles and routine data
- `fiddle/festivals.toml` — festival dates and Elsie's vendor/quest role
- No dedicated schedule files found in `t2/Schedules/` for Elsie

---

## Schedule Data Status

**No structured schedule files exist for Elsie** in the extracted game data. Unlike Adeline (who has detailed seasonal daily schedules in `t2/Schedules/`), Elsie's routine is inferred entirely from dialogue trigger conditions. This means her daily pattern is documented from what conditions must be true for her lines to fire, not from explicit schedule tables.

The following reconstruction is evidence-based but incomplete.

---

## Daily Routine (inferred from dialogue triggers)

### Morning

- **Bathhouse visits:** Multiple lines trigger at `time_of_day = "morning"` + `location = "bathhouse_change_room"`. "Nothing quite like a morning soak to start the day right." (bathhouse_soak). Rainy variant: "There's nothing better than a long soak on a rainy day." (rainy_bathhouse_soak)
- **Travel to bathhouse:** "I'm so looking forward to a good soak at the Bathhouse. I hope Juni's around." (hope_juni_is_there; requires: traveling to bathhouse). "It's a bit of a walk to the Bathhouse, but the soak is always worth it." (bathhouse_walk)
- **Inn breakfast:** "Nothing in the Capital beats Reina's breakfast special! Delicious!" (inn_breakfast; requires: elsie eating, morning, at inn)
- **Sunday brunch:** "Sundays aren't for paperwork... they're for brunch! And mimosas. EMPHASIS mimosas." (sundays_for_mimosas; requires: Sunday, before 2pm)

### Midday / Afternoon

- **Manor garden wander:** "Sometimes an afternoon walk in the garden is just the thing! It's so lovely here." (manor_garden_beautiful; requires: `elsie_routine = "manor_garden_wander"`, town, pleasant weather, afternoon)
- **Museum visits:** "I'm visiting Eiland at the Museum today!" (walk_to_museum; requires: traveling to museum, Eiland at museum). "There's something so romantic about history, don't you think?" (museum_1; requires: `elsie_routine = "museum_visit"`)
- **General store shopping:** "There's such a variety of produce at the General Store ever since you arrived, [Ari]." (general_store; requires: `elsie_routine = "general_store_shopping"`, after 2 months)

### Evening

- **Manor dining:** "Off to dinner with the youngins and Errol!" (travel_to_dinner; requires: traveling to manor dining room, Errol and Eiland also traveling there, after 4pm)
- **Inn evening drinks:** "Nothing like some wine and chitchat to lift the spirits!" (inn_is_best; requires: inn, drinking wine). "For a cozy little country town, Hemlock runs a bar worthy of the Capital! What a selection!" (cozy_bar)
- **Nightcap:** "Well, a nightcap won't hurt." (nightcap; requires: drinking activity, night)

### Night

- **Journaling/memoir writing:** "I must record my greatest love in my journal..." (journaling; requires: write_sit animation). "Excuse me, [Ari]... I try to make notes at the end of each day" (eod_notes; requires: write_sit, night). "I thought I'd spend this winter day putting some time in on my manuscript." (winter_day_writing; requires: winter, write_sit, not night)
- **End-of-week journaling:** "Another eventful week for Great Aunt Elsie. I should do some journaling." (eow_journaling; requires: Sunday, NOT currently writing)

---

## Known Routines (named in trigger conditions)

The dialogue files reference these named routines via `elsie_routine =`:

| Routine name | Location | Evidence |
|---|---|---|
| `manor_garden_wander` | Manor garden / town | Afternoon garden walks; winter variant exists |
| `museum_visit` | Museum | Visiting Eiland; history appreciation |
| `general_store_shopping` | General Store | Produce shopping; requires 2+ months elapsed |

---

## Weekly Recurring Events

### Friday Night at the Inn

**When:** Every Friday evening (and rainy Inn nights)
**Elsie's role:** Enthusiastic attendee and social cheerleader.
- Morning anticipation: "Don't miss the evening gathering at the Inn, [Ari]. Hemlock and Josephine host quite the little soiree." (fnati_anticipation; requires: Friday or rainy_inn_night, morning)
- Pre-event: "It will be nice to see the townsfolk at the Inn tonight... I hope I can make it." (inn_will_be_fun_tonight; requires: before 3pm, Friday or rainy_inn_night, not at Inn)
- She observes couples: "Hemlock and Josephine... these two are like pieces of a puzzle that fit together." (hemlock_and_jo_are_great)

### Saturday Market

**Elsie's role:** Vendor at Spring Festival (see below); attendee at weekly market.
- Market dialogue files show her interacting with vendors: Darcy (4 lines), Louis (4), Merri (4), Stillwell (4), Vera (4), Wheedle (4), Zorel (1), Taliferro (1) — 26 market-specific dialogue files total

### Sunday Rest

- Brunch and mimosas emphasis
- End-of-week journaling
- Not working / anti-paperwork stance: "Sundays aren't for paperwork"

---

## Annual Festivals

### Shooting Star Festival (Summer 28)

**What:** Stargazing event at the Summit. Dateable NPCs can be invited as dates with Star Brooches.
**Elsie's role:** Festival organizer and quest-giver. She is the face of this event.
- Visits the player's farm in the morning to explain the tradition and distribute Star Brooches
- Three cutscene variants: standard (offers brooch), married (reminds about spouse), blocked (summit inaccessible)
- She explains the Starbinding tradition: "It's a Mistrian tradition going back centuries"
- She handles the romantic invitation mechanic but does not attend as a date herself
- Festival data: `npc_for_icon = "elsie"` in both the story quest and festival definitions
**Emotional register:** Warm, romantic, encouraging. She is the matchmaker, not the participant.

### Spring Festival (Spring 17)

**What:** Flower collection challenge.
**Elsie's role:** Vendor — runs `elsie_spring_festival` stall selling cosmetics (flower crown, earrings, festival dress/suit, flower top hat). Items are tier-gated by the player's challenge performance.
**Significance:** One of the few non-merchant NPCs with a festival vendor role, reflecting her role as social curator.

### Harvest Festival (Fall 10)

**What:** Queen Berry gathering competition, feast, and dance.
**Elsie's role:** Attendee, not organizer. No specific Elsie dialogue identified in festival triggers.

### Animal Festival (Winter 10)

**What:** Animal competition.
**Elsie's role:** Attendee. No specific Elsie dialogue identified.

---

## Birthday

**Date:** Summer 2
**Birthday gift dialogue:** "Oh, a gift? It's terribly sweet of you to remember my birthday, [Ari]." (birthday_gift)

---

## Seasonal Behavior Patterns

### Spring
- Bathhouse visits in morning (pleasant weather)
- Garden walks (manor_garden_wander routine)
- Spring Festival vendor role
- First-meeting introductions for new players

### Summer
- Beach appreciation: "I can already smell that brisk sea air!" (walk_to_beach)
- Shooting Star Festival organization (Summer 28)
- Birthday (Summer 2)
- Singing animation active (spring, summer, autumn only)

### Fall
- Museum visits increase (winter museum variant also exists)
- General store shopping
- Continued garden walks
- Last season for singing animation

### Winter
- Contracts indoors: more writing/journaling, warm Inn visits
- "It's always nice and warm in here, no matter how cold it gets outside." (warm_inn)
- "There's something so romantic about the snow, don't you think?" (romantic_snow)
- Winter garden appreciation: "Isn't the garden beautiful in winter?" (winter_garden)
- Manuscript work: "I thought I'd spend this winter day putting some time in on my manuscript." (winter_day_writing)
- No singing animation in winter

---

## Key Location Patterns

| Location | Activity | Social context |
|---|---|---|
| Manor (entry/dining) | Piano listening, dinner, journaling | Household family time |
| Bathhouse | Soaking, gossip with Juniper | Primary gossip venue |
| Inn | Breakfast, drinks, Friday nights | Social hub |
| Museum | Visiting Eiland, history appreciation | Supportive family role |
| Manor garden / Gazebo | Walking, seasonal appreciation | Reflective time |
| Beach | Seasonal visits | Appreciation of Mistria's beauty |
| General Store | Shopping | Routine task |
| Town (festival) | Vendor, festival organizer | Community role |

---

## Rainy Day Behavior

- Bathhouse soak: "There's nothing better than a long soak on a rainy day." (rainy_bathhouse_soak)
- Wine with family and friends: "A bit of wine and a lovely day with my niece and my friend... can't rain on that!" (enjoying_the_rain; requires: Adeline and Juniper in same zone)
- Triggers rainy Inn night attendance alongside Friday nights

## Q&A Block Mapping

- **Calendar Events:** festivals (Shooting Star as primary, Spring Festival vendor), birthday, weekly recurring (Friday night, Sunday brunch)
- **Background Q&A:** daily routine as lifestyle evidence, seasonal shifts, location patterns
- **Soul Q&A:** schedule patterns reveal social-driven life (bathhouse for gossip, Inn for wine, garden for reflection, museum for family)
