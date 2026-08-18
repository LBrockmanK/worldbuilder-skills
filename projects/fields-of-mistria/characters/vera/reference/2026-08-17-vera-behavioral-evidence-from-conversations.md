---
type: reference
title: Vera — Behavioral Evidence from Conversations
description: 'Extracted dialogue from Vera''s banked conversation lines and gift lines:
  greetings, shop talk, seasonal lines, packing-up lines, commentary on other characters,
  gift reactions.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Vera/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Vera/Gift Lines/
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml
---

# Vera — Behavioral Evidence from Conversations

Source: `source/t2/Conversations/Bank/Vera/`

## First Meeting

**greeting_ari** (priority: max, refresh: never, requires: vera_has_met = false):
- [happy] "Hello! If you're looking for a new hairstyle, you're talking to the right person!"
- [neutral] "The name's Vera. I'm a traveling hair stylist, I've been all over Aldaria!"
- [wink] "I'd be happy to teach you any hairstyle I know, just pick what you want and put down your coins!"

**Behavioral notes:** Vera introduces herself with confidence and warmth. She immediately frames herself as a professional and a traveler. Her language is direct and inviting, with a salesperson's energy. The phrase "traveling hair stylist" and "all over Aldaria" establish her as someone from outside Mistria who visits regularly.

## Shop Talk and Sales Lines (While Stall Is Open)

These lines play on Saturdays when Vera is at her stall and not packing up.

**more_exciting** (refresh: 1y):
- [neutral] "Here for a trim, [Ari]? Or something a little more exciting?"

**screams_ari** (refresh: 1y):
- [neutral] "I've got a hairstyle that just screams \"[Ari]\" today!"

**something_new** (refresh: 1y):
- [neutral] "Have you ever thought about dyeing your hair a new color? Sky's the limit!"

**great_fashion** (refresh: 1y):
- [neutral] "Great fashion starts with great hair!"

**fresh_challenge** (refresh: 1y):
- [neutral] "Everyone's hair is different, but I love a fresh challenge."

**favorite_stop** (refresh: 1y):
- [neutral] "Mistria is definitely one of my favorite stops on my route."

**before_times** (refresh: 1y):
- [wink] "You should ask some of the folk here what their hair was like before I started showing up."

**gossips** (refresh: 1y):
- [neutral] "You know everyone gossips with me, and some of the stories they tell about you, well... if half of them are true, I'm impressed!"

**next_time** (refresh: 1y, plays at stall or during packing):
- [neutral] "I'm always getting new hair styles in. If you don't see something this week, be sure to stop by next time!"

**stray_hair** (refresh: 1y):
- [think] "You wouldn't believe the places you find stray hair when you're a stylist."
- [happy, effect: drop] "Talk about bringing your work home with you!"

**Behavioral notes:** Vera is enthusiastic about her craft and always upselling. She positions herself as creative ("something a little more exciting," "sky's the limit") and takes pride in being a fixture of the community ("one of my favorite stops on my route"). She enjoys being a gossip hub and wears it openly. The stray-hair comment shows self-deprecating humor about the realities of her job.

## Seasonal Lines (While Stall Is Open)

**new_year** (spring, refresh: 3m, requires: date_time > 1y):
- [wink] "A new year calls for a new hairstyle!"

**hot_new_looks** (summer, refresh: 3m):
- [wink] "Have some hot new looks today, be sure to check them out!"

**summer_heat** (summer, refresh: 3m):
- [neutral] "Why not take the edge off that summer heat with a fresh hairstyle?"

**off_your_neck** (summer, refresh: 3m):
- [neutral] "If you're looking to do something with long hair, a braid or a bun can help keep it off your neck."

**cool_drink** (summer, refresh: 3m, requires: Darcy at stall):
- [neutral] "Glad Darcy's here, I'm just steps away from a cool drink!"

**cold** (winter, refresh: 3m):
- [neutral] "Let me take your mind off the cold with a great new cut!"

**wait_til_spring** (winter, refresh: 3m):
- [neutral] "Don't wait till spring to get your hair done!"

**Behavioral notes:** Vera adapts her sales pitch to the season. In summer she focuses on practical styling advice (braids, buns to beat heat). She appreciates Darcy's proximity for drinks. In winter she reframes cold weather as a reason to visit. She consistently ties seasonal context back to selling her services.

## Packing-Up / End-of-Day Lines

These play on Saturdays when Vera is running the "vera_packing" routine (evening, after market closes).

**packing_1** (refresh: 1y):
- [neutral] "Another day, another fluffy pile of hair to tidy up!"

**packing_2** (refresh: 1y):
- [wink] "See you next time, [Ari]! You better believe I'll have some eye-catching styles for you."

**fresh_air** (refresh: 1y):
- [neutral] "It's so nice to be out in the fresh air cutting hair!"

**day_flies** (refresh: 1y, requires: date_time < 1m — early in the game):
- [happy] "The day flies by when you're having fun! I'm so happy to be cutting hair in Mistria again."
- [wink] "Gotta catch up on all the gossip I missed while the bridge was out!"

**summer_packing_1** (refresh: 1y):
- [wink] "Another day of seeing my favorite customers! And getting the gossip, of course."

**sack_out** (refresh: 1y, requires: Merri at town):
- [think] "What a day! Do you think Merri will let me sack out on one of her carpets?"

### Seasonal Packing Lines

**spring_packing_1** (spring, refresh: 3m):
- [wink] "Another Saturday Market in the bag."
- [happy] "Spring calls for fresh starts, and I'm always happy to help everyone look their best!"

**fresh_spring_cuts** (spring, refresh: 3m):
- [happy] "I was so busy today! Everyone wanted their fresh spring cuts."

**come_by_again** (summer, refresh: 3m):
- [wink] "Come by again some time, I'll give you an easy breezy cut!"

**summer_packing_2** (summer, refresh: 3m, requires: Darcy at town):
- [happy] "Weather was warm today, wasn't it? I must've had four of those iced teas from Darcy's!"

**time_flies** (winter, refresh: 3m):
- [happy] "The day's over! Heck, the year's almost over! Time flies, doesn't it?"

**Behavioral notes:** At the end of the day Vera is cheerful and tired. She references gossip repeatedly as a perk of the job. The sack_out line suggests she does not have a permanent residence in Mistria and may sleep rough or with other vendors. The day_flies line confirms the bridge being out interrupted her visits to Mistria, and she was eager to return. She buys drinks from Darcy during market day.

## Commentary on Other Characters' Hair

**eilands_hair** (refresh: 1y, requires: Eiland visiting stall):
- [wink] "Eiland's hair would be the perfect canvas for some wild colors! Imagine him rocking neon green!"

**junipers_hair** (refresh: 1y):
- [think] "What do you think are the chances that Juniper lets me do something wild with her hair next time?"
- [mad] "She'd look killer as a blonde!"

**march_hair** (refresh: 1y):
- [think] "I love dyeing March's hair, but do you think he'll ever want something other than red?"
- [wink] "I'll sound him out next time he needs a touch up!"

**trim_holt** (refresh: 1y):
- [think] "I got to trim Holt's hair today. He's always had that cowlick, you know."
- [wink] "And Dell had to go and inherit it!"

**va_va_voom** (refresh: 1y, requires: Elsie visiting stall):
- [wink] "It takes a special hand to keep Elsie's hair the way she likes it! She likes that va-va-voom, if you know what I mean."

**chatting_with_jo** (refresh: 1y, requires: Josephine visiting or packing):
- [neutral] "I love getting into it with Jo when I do her hair!"
- [wink] "She sees everything that happens from behind that bar of hers, and I live to hear about it!"

**seridias_hair** (refresh: 1y, requires: Seridia in town, dragon market):
- [think] "Seridia asked me to dye her hair..."
- [neutral] "And then later that day I saw her walking around the Market with her original color!"
- [mad] "How!?"

**Behavioral notes:** Vera has opinions about everyone's hair and is not shy about sharing them. She sees hair as a creative canvas and pushes for bolder choices (neon green for Eiland, blonde for Juniper). She has an ongoing professional relationship with March (dyeing his red hair), Holt (the cowlick), and Elsie (high-maintenance styling). She and Josephine have a close gossip-sharing friendship. The Seridia line shows frustration at magical hair — her professional skill rendered irrelevant.

## Basement / Fallback Line

**basement_1** (priority: basement, refresh: instantly):
- [neutral] "Always nice to see you."

**Behavioral notes:** The absolute fallback line is warm but generic. Even in the lowest-priority case, Vera is friendly.

## Gift Reactions

### Loved Gift Lines

**Generic loved:**
- [happy, sparkles] "[Ari], you nailed it! I really needed a pick-me-up!"
- [happy, sparkles] "You're so sweet, thinking of me! This is just what I needed!"

**Generic loved (edible, refresh: 1w):**
- [wink, sparkles] "Thanks [Ari]! You wouldn't believe how much energy it takes to cut hair all day!"

**Specific — gazpacho:**
- [wink, sparkles] "[Ari] how did you know? Gazpacho is the perfect meal! What's better than a smoothie... but savory?"

**Specific — summer_salad:**
- [happy, sparkles] "What a gorgeous Summer Salad! So refreshing! Just the thing for a day on my feet!"

### Liked Gift Lines

**Generic liked:**
- [happy] "How'd you know I like this? Thanks, [Ari]!"
- [wink] "You're the best, [Ari]! Thanks!"
- [neutral] "Ooh, for me? Don't mind if I do! Thanks for looking out, [Ari]."

**Specific — coconut_milk:**
- [wink] "Coconut Milk is so versatile! I could have a fancy drink... or maybe I'll make a hair mask!"

**Specific — cranberry_juice:**
- [happy] "Ooh thank you! I can't resist a tart drink! The best Cranberry Juice makes your whole jaw tingle."

**Specific — orange_juice:**
- [happy] "A fresh Orange Juice was exactly what I needed! You're a sweetie, [Ari]."

**Specific — pomegranate:**
- [neutral] "What a beautiful Pomegranate! You know, the nutrients in these are really good for your hair and skin."

### Neutral Gift Line

- [neutral] "Aw, thanks for thinking of me."

### Disliked Gift Line

- [ugh] "I'm not saying I hate it, but I'm not saying I like it either..."

### Hated Gift — Clam

- [ugh, sick] "Ugh this is so slimy, it throws off my whole vibe! Shellfish belong in the river!"

### Birthday Gift

(Priority: max, requires: within 24h after vera_birthday)
- [neutral] "Ooh, I bet I know what this is!"
- [embarrassed, sparkles] "A birthday gift! Thanks, [Ari]."

**Behavioral notes:** Gift reactions reinforce Vera's character. She values hearty, vegetable-forward meals and refreshing drinks — foods that sustain someone on their feet all day. The coconut milk line shows she blends personal care with professional knowledge (hair masks). The pomegranate line connects beauty nutrients to her expertise. She strongly dislikes slimy textures (clam). Her birthday reaction is modest and a little flustered, contrasting her usual confidence. She addresses the player warmly and frequently by name.

## Cutscene Dialogue (Reina's Eight Hearts)

Source: `source/t2/Cutscenes/Heart Events/Reina/reina_eight_hearts.c.toml`

Vera appears as one of three judges (alongside Darcy and Taliferro) in the Aldarian Cooking Contest at the Sleeping Dragon Inn.

**Arrival:**
- [happy] "Hi, everyone!"
- [neutral] "We're the judges for the Aldarian Cooking Contest!"

**Tasting the starter (Dragon Horn Mushroom & Thyme):**
- [happy, cheery] "I've never had a mushroom with so much flavor!"

**Tasting the main (Mistrian Vegetable Curry):**
- [happy] "What an aromatic blend of spices!"

**Tasting dessert (Wildberry Pie):**
- [neutral] "Crisp crust, no soggy bottom on this pie."

**Pressing Taliferro for his opinion:**
- [neutral] "Out with it, Taliferro."

**Reacting to Taliferro's grudging praise:**
- [happy] "Well well, I haven't seen Tali this happy with a meal in-"

**After Taliferro objects to the nickname:**
- (Taliferro: "Please refer to me by my full name, Vera.")

**Announcing deliberation:**
- [think] "After much deliberation."

**Awarding the Aldarian Star:**
- [happy] "We are delighted to award the Sleeping Dragon Inn and its head chef Reina, an Aldarian Star."

**Follow-up line (after event, refresh: never):**
- [neutral] "I always knew Reina could cook, but she really pulled out all the stops!"
- [happy] "That Aldarian Star was well earned!"

**Behavioral notes:** In the judging role, Vera is warm and enthusiastic but also fair. She gives specific culinary observations (flavor, aroma, crust quality) rather than vague praise. She has a teasing familiarity with Taliferro, calling him "Tali" despite his objection, suggesting she knows him from outside Mistria through the traveling-vendor or culinary circuit. She takes the role seriously but keeps the mood light. She is the one who formally announces the award.
