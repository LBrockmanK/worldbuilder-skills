# Eiland --- Calendar & Schedule

## Sources

- `fiddle/npcs/eiland.toml` --- animation cycles and routine references
- `t2/Conversations/Bank/Eiland/Banked Lines/` --- location- and time-gated dialogue
- `t2/Cutscenes/Heart Events/Eiland/` --- event locations
- `fiddle/quests/heart_quests.toml` --- quest locations
- No schedule files exist in the source data for Eiland

---

## Schedule Gap

Unlike Adeline (who has full seasonal schedule data in `t2/Schedules/`), no schedule files were found for Eiland. The daily routine information below is inferred entirely from dialogue trigger conditions (location requirements, time-of-day gates, routine names, and zone references).

---

## Inferred Daily Routine

### Routine names referenced in dialogue triggers

These routine identifiers appear in `requires` blocks and establish where Eiland spends his time:

- `eiland_office_work` --- office/desk at the Museum or his own office
- `eastern_road_archaeology` --- dig site on the Eastern Road
- `narrows_archaeology` --- dig site at the Narrows
- `western_ruins_archaeology_pit` --- dig site at the Western Ruins
- `general_store_shopping` --- shopping for supplies (Elsie's jams, replacing Adeline's honey)
- `manor_garden_wander` --- evening walks in the Manor garden
- `eiland_roommate` --- post-marriage cohabitation routine

### Typical day pattern (inferred)

**Morning:**
- Located at Manor or Museum
- Drinks: black tea or water (6am preference)
- May greet player on the way to dig sites: "heading_to_dig" dialogue

**Midday:**
- Excavation days: at Western Ruins, Eastern Road, or Narrows (pickaxe, trowel, magnify animations)
- Non-excavation days: Museum desk work, office paperwork, studying artifacts
- Drinks: green tea or latte (noon preference)

**Afternoon/Evening:**
- Returns from dig sites; may stop at Museum to catalog
- General Store shopping trips
- Manor garden walks (evening)
- Drinks: wine (4pm preference)
- Inn visits on Fridays and social evenings

**Night:**
- Manor dining and sleep
- Drinks: milk (midnight preference)
- May be caught working late: "I came back home from the Museum later than usual last night" (Eiland about Adeline, but implies his own late returns)

### Weekly patterns

- **Friday:** Friday night at the Inn with everyone; D&D sessions; anticipates early in the day
- **Sunday:** "It feels like a sleepy Sunday to me..." (sleepy_sunday)
- **Rainy days:** Covers Museum front desk so Errol can visit Landen

### Key locations

- **Museum** (desk, office): primary workspace for cataloging, translation, artifact study
- **Western Ruins:** preferred excavation site; "I could spend the rest of my life here"
- **Eastern Road / Narrows:** additional dig sites
- **Manor House:** home, piano, family dinners, office paperwork
- **Manor grounds / stele:** archaeological study site; emotionally significant
- **Inn:** social evenings, Friday nights, beer and cookies
- **Bathhouse:** practices holding breath for underwater archaeology (unsuccessfully)
- **General Store:** shopping for sweets and supplies
- **Deep Woods / Grove of Rest:** reading spot before earthquake; 8-heart event location
- **Beach:** thinks about Western Ruins when there; not a primary hangout

---

## Annual Events

### Birthday

**Date:** Summer 20

### Festivals

No Eiland-specific festival dialogue was found in the reviewed files. His festival behavior would follow the general dateable NPC pattern: potential Shooting Star Festival date partner (Summer 28), potential Harvest Festival dance partner (Fall 10).

### Heart Event Locations (progression)

| Hearts | Quest name | Location |
|--------|-----------|----------|
| 2 | The Stele | Manor grounds (town area) |
| 4 | The Ruins | Western Ruins |
| 6 | The Manor | Manor House entry |
| 8 | The Glade | Deep Woods |
| 10 | (proposal) | Back at the stele (Manor grounds) |

The locations trace an arc: home grounds -> distant ruins -> back home -> deep wilderness -> back where it started. The 10-heart return to the stele is explicitly noted: "Back where it all started... Funny that our steps naturally took us here, isn't it?"

---

## Seasonal Behavior Patterns (from dialogue triggers)

### Spring
- Fresh look at fountain engravings after winter thaw
- New research folios
- Archaeology tutorial for new players

### Summer
- Beach visits (thinks about Western Ruins)
- Birthday (Summer 20)
- Active excavation season

### Fall
- Pumpkin pie season: "Fall is pumpkin season! That can only mean one thing..."
- Continued excavation before winter: "fall_dig" dialogue
- Fall bathhouse visits

### Winter
- More indoor work (Museum desk, office)
- Inn visits for warmth: "Nothing like the warmth of a hearth on a cold night..."
- Piano playing at the Manor

---

## Q&A Block Mapping

- **Calendar Events:** birthday, seasonal patterns, heart event location progression
- **Background Q&A:** daily routine as lifestyle evidence; location preferences as character detail
- **Soul Q&A:** the stele-to-stele arc of heart event locations mirrors his thematic journey (starting point -> adventure -> return with new understanding)
