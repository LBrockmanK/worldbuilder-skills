---
type: reference
title: Taliferro — Schedule and Events
description: 'Daily schedule patterns by season and day, cutscene appearances, and
  quest involvement extracted from schedule and cutscene source files.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Schedules/basement_schedule.s.toml
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade One/
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade Two/
- projects/fields-of-mistria/source/t2/Cutscenes/Story Events/Town Repair/upgrade_the_saturday_market.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Reina/reina_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml
---

# Taliferro — Schedule and Events

## Daily Schedule

### Basement / Default (all days, all seasons)

From `basement_schedule.s.toml` (coverage: all):

- **6:00 AM:** aldaria/default

Taliferro's default location is in Aldaria (the Capital). He is not present in Mistria on non-Saturday days or when schedule conditions are not met.

### Saturday — Upgrade One (after market upgrade quest)

Requires: Saturday, pleasant weather, bridge repair complete, Saturday market upgrade complete.

**Spring** (`u1_spring_saturday.s.toml`):
- 6:00 AM — Arrives at town/Taliferro (booth)
- 9:05 PM — Packing routine begins (taliferro_packing)

**Summer** (`u1_summer_saturday.s.toml`):
- 6:00 AM — Arrives at town/Taliferro (booth)
- 8:05 PM — Packing routine begins (earlier due to summer heat)

**Fall** (`u1_fall_saturday.s.toml`):
- 6:00 AM — Arrives at town/Taliferro (booth)
- 8:45 PM — Packing routine begins

**Winter** (`u1_winter_saturday.s.toml`):
- 6:00 AM — Arrives at town/Taliferro (booth)
- 8:45 PM — Packing routine begins

### Saturday — Upgrade Two (after market plaza upgrade)

Requires: Saturday, pleasant weather, bridge repair complete, both market upgrades complete.

In the Upgrade Two schedule files, Taliferro is **not listed** — the Upgrade Two Saturday slots are filled by Stillwell and Zorel instead. This suggests that Taliferro and Wheedle rotate out when the market expands further, replaced by new vendors.

### Schedule Summary

- Taliferro is a **Saturday-only** NPC in Mistria
- Present only in pleasant weather
- Arrives at 6:00 AM every Saturday (consistent across seasons)
- Packing time varies by season: earliest in summer (8:05 PM), latest in spring (9:05 PM)
- In Upgrade Two, replaced by Stillwell — not present at the expanded market
- All other days: remains at default location in Aldaria

## Cutscene Appearances

### 1. Upgrade the Saturday Market (Story Event — Town Repair)

**File:** `upgrade_the_saturday_market.c.toml`

**Context:** Adeline and Nora discuss a letter from the Aldarian Merchant's Guild. The guild is impressed with Mistria's Saturday Market and offers to send two Capital vendors: Taliferro and Wheedle.

**Taliferro's role:** Mentioned by name but not physically present. Adeline describes him as "the Royal Chef whose Cooking Challenge booth has been a huge hit across Aldaria." Nora has heard of him ("Supposedly, they're both real characters"). The booth requires expensive materials including gold ingots — establishing Taliferro's luxury expectations before the player ever meets him.

**What it reveals:** Taliferro is famous across Aldaria. His arrival is treated as a milestone for the town. The material costs hint at his demanding nature. Both Nora and Adeline are cautious about his reputation.

**Other characters involved:** Adeline, Nora, Landen, March, Ryis (follow-up lines about building the booths).

### 2. Reina's Six Hearts Event

**File:** `reina_six_hearts.c.toml`

**Context:** Reina asks the player to be her sous chef for a cooking contest. Balor arrives with news that Taliferro has been selected as the final judge.

**Taliferro's role:** Not physically present — discussed as an offstage figure. The announcement that he is judging changes Reina's entire approach. She scraps her menu and tries to cook "elevated" food in his style (extra-sweet curry, chili-infused chocolate cake, agar-thickened drinks). The taste test with her family goes poorly — the food "tastes like something Taliferro might serve" but nobody enjoys it.

**What it reveals about Taliferro:**
- "There isn't a chef more acclaimed in all of Aldaria" — highest possible culinary authority
- "Prickly" (Josephine), "arrogant and overcritical" (Balor) — reputation among those who know of him
- Likes "elevated" food and "innovative textures" — his restaurant is known for this
- His mere reputation causes Reina to abandon her authentic cooking style
- The family's negative reaction to Taliferro-style food suggests his tastes are at odds with Mistrian values

**Other characters involved:** Reina, Balor, Josephine, Hemlock, Maple, Luc.

### 3. Reina's Eight Hearts Event — Aldarian Cooking Contest

**File:** `reina_eight_hearts.c.toml`

**Context:** The Aldarian Cooking Contest takes place at the Sleeping Dragon Inn. Taliferro serves as one of three judges alongside Vera and Darcy. Reina (having abandoned the "elevated" approach) serves authentic Mistrian dishes.

**Taliferro's role:** Physically present as a judge. This is his most substantial character appearance in the game.

**Key dialogue moments:**

1. **Professionalism demand:** "Hmph. Let's keep it professional and try for a little impartiality, Darcy." — positions himself as the standard-bearer.

2. **Appetizer reaction (Dragon Horn Mushroom & Thyme):** "What mundane plating. I'd prefer something more unexpected..." then "Ah-" — his criticism is cut short when the flavor hits. This is his most revealing moment: caught between his instinct to criticize presentation and his professional obligation to acknowledge quality.

3. **Main course reaction (Mistrian Vegetable Curry):** "A... respectable depth of flavor, considering." — grudging praise with the qualifier "considering" (implying he expected less from Mistria).

4. **Dessert reaction (Wildberry Pie):** Goes silent. Vera pushes: "Out with it, Taliferro." He concedes: "Well, I must concede... it's pretty good." Then defends himself: "I pride myself in my taste as a chef. To deny good food is to deny my own abilities." Deflects with a critique: "the presentation still leaves much to be desired. Would it kill you to serve it with a scoop of ice cream?"

5. **Name insistence:** Vera calls him "Tali." He responds: "Please refer to me by my full name, Vera."

6. **Stakes declaration:** "The culinary prestige of Aldaria rests on our shoulders, Darcy!" — reveals he takes the role extremely seriously.

7. **To Maple about the Aldarian Star:** "It's not a real star, small child." — blunt, literal, zero warmth toward children.

**What the contest reveals:** Taliferro's professional integrity is real — he will not deny good food even when it comes from a place he looks down on. His concession is framed as an act of professional duty, not generosity. He always retreats to a secondary critique (presentation) when forced to admit the substance was good.

**Follow-up lines (post-event):**

Taliferro to player: "Oh, it's you. I'm not going to call you 'Chef' just because you assisted in the cooking competition, you know. You've yet to earn that title as far as I'm concerned."

Darcy: "Too bad it means I need to work with Taliferro, though."

**Other characters involved:** Reina, Vera, Darcy, Josephine, Hemlock, Maple, Luc, Adeline (follow-up).

## Quest Involvement

### Cooking Challenges (recurring weekly quests)

Taliferro runs the Cooking Challenge system at his Saturday Market booth. The player must complete each challenge in sequence. Challenges include: Rice Ball, Crispy Fried Earthshroom, Crystal Berry Pie, Chocolate Cake, Tide Salad, Omelet, Bell Berry Bakewell Tart, Herb Salad, Incredibly Hot Pot, Veggie Sub Sandwich.

Each challenge has an associated NPC who also attempts it (and fails), generating commentary dialogue.

### Upgrade the Saturday Market (prerequisite quest)

The player must gather materials (8 Gold Ingots, 20 Obsidian, 20 Crystal, 100 Hard Wood, 50 Refined Stone) to build booths for Taliferro and Wheedle. Taliferro's arrival is gated behind this quest completion.

## Narrative Arc Summary

Taliferro exists at the intersection of two functions: a weekly gameplay vendor (Cooking Challenge booth) and a narrative figure in Reina's cooking storyline. In gameplay, he is an unchanging judge whose standards nobody meets. In Reina's arc, he serves as the ultimate test — the most acclaimed and most difficult chef in Aldaria. Reina's growth comes from choosing not to cook for his tastes but to cook authentically, and his grudging approval validates that choice. He never softens — his post-contest line to the player is as dismissive as his first — but his professional concession during the contest is the closest he comes to respect.
