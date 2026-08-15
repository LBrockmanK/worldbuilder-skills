# Adeline — Calendar & Schedule

## Sources

- `t2/Schedules/` — seasonal schedule files (all read, Adeline sections extracted)
- `fiddle/festivals.toml` — festival definitions
- `t2/Conversations/Festival Lines/` — festival-specific Adeline dialogue
- `t2/Cutscenes/Festival Events/` — festival cutscenes
- Wiki: Calendar Events page

---

## Daily Routine by Season

Adeline's daily pattern follows a consistent structure: morning work
(office or quest board), midday business/social, evening dining or
drinks. Seasonal and weather variations shift the balance between
indoor and outdoor activities.

### Spring (Pleasant Weather)

| Day | Morning | Midday | Afternoon | Evening |
|-----|---------|--------|-----------|---------|
| Monday | 6am Bedroom → 6:21am Quest Board (writing) | 11:30am Office (desk work) | | 7:59pm Manor Dining → 12:12am Bedroom |
| Tuesday | 6am Town → 6:10am Quest Board | 11:10am Inn (work) | | 6:18pm Blacksmith → 10:12pm Bedroom |
| Wednesday | 6am Bedroom → 6:10am Office (work) | 11:12am Inn | 4:15pm Inn (drinks) | 6:33pm Manor Dining → 12:02am Bedroom |
| Thursday | 6am Bedroom → 6:01am Eastern Road (business review) | 8:52am Blacksmith → 11:33am Inn → 1:38pm Town | 3:58pm Beach | 9pm+ Beach → 12:33am Bedroom |
| Friday | (Regular schedule until evening) | | | Friday Night at the Inn |
| Saturday (Market) | 6am Town Fountain (Market Inspector) | All day at market | | 8:31pm Inn (drinks) → 12:32am Bedroom |
| Saturday (No Market) | 6am Manor (writing) | 9:34am Fountain Square | 2:12pm Bathhouse | 6:08pm Inn (food) → 12:32am Bedroom |
| Sunday | 6am Office | 10:08am Gazebo | 6:47pm Manor Garden Walk | 7:41pm Manor Dining → 1:07am Bedroom |

### Summer (Pleasant Weather)

Notable changes from Spring:
- **Monday:** Western Ruins supervisor visit (9:23am-2:49pm)
- **Wednesday:** Morning Bathhouse visit (6:21am)
- **Thursday:** Repair/restoration reviews at multiple sites
- **Sunday:** Beach day with friends — beach outfit, towel chat, beach bench (6am-3:41pm)

### Fall (Pleasant Weather)

Notable changes:
- **Monday:** Manor Garden walk (6:01am), Wagon meetup, Fountain Square
- **Monday evening:** Poker at the Inn (6:12pm)
- **Tuesday:** Museum conversation (12:23pm)
- Outdoor grant writing sessions in pleasant weather

### Winter

Schedule contracts to more indoor activities. Bathhouse visits increase.

### Rainy Day Schedule

Rain drives activities indoors. Adeline does office paperwork and may have "girls night" with Reina and Celine at the Inn or Celine's room.

---

## Weekly Recurring Events

### Friday Night at the Inn

**When:** Every Friday evening
**What:** All townspeople gather at the Inn. Live music (Josephine and Hemlock perform), socializing, drinks, games.
**Adeline's role:** Attendee, not organizer. She arrives early ("I'm so excited for Friday night, I just couldn't wait!"). Plays poker with Celine, Reina, Balor, and Hemlock. Her poker tell: keeps cards in order and forgets to rearrange them. Friends have banned her from bringing clipboards.
**Recurring activities:** Music night (claps along), poker games, Dragons & Drama tabletop sessions, socializing
**Dialogue triggers:** music_night, early_friday, dnd_follow_up

### Saturday Market

**When:** Every Saturday (after bridge repair quest complete)
**What:** Vendor stalls in the town square with Darcy (food/coffee), Louis (clothing), Merri (furniture), Vera (hairstyles). All townspeople attend.
**Adeline's role:** Saturday Market Inspector — arrives at 6am to the Town Fountain and oversees all day. Inspects conditions, manages vendor logistics, reviews budgets with Nora. The market was her initiative to revive.
**Day after:** "I'm a little worn out after the market... this calls for a hearty meal." (Inn visit)
**Pre-market Friday:** "I'm inspecting the town square in advance of the Market tomorrow."
**Dialogue triggers:** market_anticipation, day_after_market, saturday_market (with Nora)

### Sunday Rest Pattern

Adeline officially takes Sundays lighter — gazebo visits, garden walks, Manor dining. But she struggles to stop working: "I promise I'm not working on a Sunday! I'm relaxing! Really!" (sunday_work)

---

## Annual Festivals

### Spring Festival (Spring 17)

**What:** Flower collection challenge — townspeople gather Breath of Spring flowers.
**Adeline's role:** Challenge participant (not organizer for once).
**Her dialogue:** "Isn't this wonderful? It feels like Mistria has come back to life!" — if player places first, she congratulates on collection.
**Emotional register:** Joy at community celebration; the festival represents Mistria's recovery.

### Shooting Star Festival (Summer 28)

**What:** Stargazing event at the Summit. Romanceable NPCs can be invited as dates (requires heart level 4+).
**Adeline's role:** Potential date partner.
**Pre-festival (4-7 hearts):** Explains the tradition, mentions the Summit has the best view.
**If invited:** "Hi [Ari]! Are you ready to walk up to the Summit together?"
**If not invited but attending:** Watches the stars alone and thinks of her parents: "I wonder if Mother and Father in the Capital are watching too..."
**Post-date (if partner):** "The stars were so beautiful, weren't they? I'm already looking forward to next year." Brings coffee the next morning as a pick-me-up.
**Significance:** The Summit is emotionally loaded — her mother's picnic spot, the 10-heart proposal location. Watching stars there with her adds layers.

### Harvest Festival (Fall 10)

**What:** Queen Berry gathering competition (starts Fall 7), feast, and dance.
**Adeline's role:** Challenge participant; potential dance partner.
**Pre-festival (8+ hearts, partner):** "Eiland's all about collecting Queen Berries for the Harvest Festival, but I'm more interested in the dance. I used to take lessons, you know."
**Festival day:** "Happy Harvest Festival, [Ari]! Look at all those smiling faces..."
**Dance mechanic:** Heart level 4+ for basic accept; 8+ for "super accept" (partnership-level dance).
**Post-festival:** Comments on berry collection results and time management.

### Animal Festival (Winter 10)

**What:** Animal competition — enter one large and one small animal.
**Adeline's role:** Enthusiastic attendee.
**Her dialogue:** "Hey, [Ari]! I hope you're having fun! I know I sure am!"
**At chicken cutout:** "These cutouts are such a good addition to the festival! I wish we had them when I was a kid."
**Post-festival:** Specific congratulations for 1st/2nd/3rd placement in each animal category.

---

## Birthday

**Date:** Winter 18
**Pre-birthday dialogue:** "A Lady is not supposed to speak of her birthday, so I won't." → "It's tomorrow." (portrait: think → blush)
**Birthday behavior:** Player can give gifts (birthday multiplier on friendship points). Multiple dialogue variants for birthday interactions.
**Player's birthday:** Adeline has specific dialogue acknowledging the player's birthday with gift offers.

---

## Seasonal Behavior Patterns

These patterns emerge from schedule data and dialogue triggers:

### Spring
- Administrative renewal: fresh quest board postings, new year project lists
- "I love doing the grocery shopping! It means I get to pick out the snacks."
- Delivers nails list to March for the year's projects

### Summer
- Beach tension: wants to go but needs work pretexts; friends drag her
- Longer outdoor work sessions; bathhouse visits increase
- Sunday beach days with friend groups
- Western Ruins supervisor visits (infrastructure oversight)

### Fall
- Outdoor grant writing: "The weather is so pretty in the fall, and it's my last chance to work out of doors before winter"
- Manor garden appreciation: "The manor garden is so pretty in autumn! Celine's really outdone herself."
- Poker nights at the Inn (Monday evenings)
- Festival planning with Nora (preliminary notes and costing)

### Winter
- Contracts indoors; more office time
- Nostalgic: childhood memories surface (snow models, mother's desk)
- Birthday season (Winter 18)
- Cozy register: "A bit of hot Coffee is especially nice in the winter. The warm mug keeps my hands cozy too!"

---

## Dates (Player-Initiated)

**When:** Saturdays and Sundays, twice per week maximum
**Mechanic:** Player-initiated; requires sufficient heart level
**Adeline's date behavior:** Informed by her personality — likely to suggest structured activities but secretly enjoys unstructured time. The 6-heart inspection walk is her "accidental date" prototype.

## Q&A Block Mapping

- **Calendar Events (Ainime):** festivals, weekly recurring events, birthday, seasonal patterns
- **Future Storylines:** festival dates as relationship-progression scenarios (Shooting Star → Summit date)
- **Background Q&A:** daily routine as lifestyle evidence; seasonal shifts as character detail
- **Soul Q&A:** schedule patterns reveal work/rest tension (Saturday Market all-day vs. Sunday struggle to rest)
