---
type: reference
title: "Josephine — Conversations"
description: 'Extracted dialogue from Josephine conversation bank: banked lines, market
  lines, museum lines, gift lines, and festival lines. All speaker attribution,
  conditions, expressions, and branching preserved.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T20:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Josephine/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Josephine/Market Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Josephine/Museum Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Josephine/Gift Lines/
- projects/fields-of-mistria/source/t2/Conversations/Festival Lines/Josephine/
---

# Josephine — Conversations

Dialogue extracted from the Josephine conversation bank and festival lines. Organized by source directory and file. Conditions, portrait expressions, effects, actions, and branching are preserved from the TOML source.

---

## Banked Lines

Source: `source/t2/Conversations/Bank/Josephine/Banked Lines/`

### adeline_works_hard.c.toml

- Refresh: never
- Requires: josephine; date_time > 4d; date_time < 21d
- Action: bark "cute_face" on josephine

Josephine [think]: "Adeline's been working so hard lately."
Josephine [sad]: "Too hard, if you ask me."
Josephine [neutral]: "Glad you're here to lend her a hand, [Ari]."

### baked_goods.c.toml

- Refresh: 1y
- Requires: josephine; baked_goods_taste_test_day = true; location = inn; time_of_day = morning OR baked_goods_taste_test = true
- Action: gives item caldosian_chocolate_cake

Josephine [neutral]: "I asked some folk to come by for a taste testing. Here, try it!"

### basement.c.toml

- Priority: basement
- Refresh: instantly
- Requires: josephine

Josephine [happy]: "Hi there! Don't be a stranger now!"

### bathhouse.c.toml

- Refresh: 1y
- Requires: josephine; building = bathhouse

Josephine [happy, cheery]: "Juniper really outdid herself, reopening the old bathhouse. I come here every chance I get!"

### beautiful_morning.c.toml

- Refresh: 1y
- Requires: josephine; weather = pleasant; time_of_day = morning

Josephine [neutral, cheery]: "It's another beautiful morning in Mistria."

### better_tidy_up.c.toml

- Source: NAR-1254 / Trellis: "Conversations/Bank/Josephine/11. Better Tidy Up"
- Refresh: 1y
- Requires: josephine; luc traveling to inn; maple traveling to inn; day_time >= 4:00pm and <= 9:00pm; location = inn

Josephine: "The kids should be home for dinner soon... I'll tidy up a little bit."

### brisk_weather_bathhouse.c.toml

- Refresh: 3m
- Requires: josephine; season = fall OR winter; location = bathhouse_change_room OR traveling from bathhouse_change_room

Josephine [happy, music_notes]: "Ooh, a hot bath in this brisk weather was just the ticket! I feel brand new!"

### bustling_town.c.toml

- Refresh: 1y
- Requires: josephine; location = town

Josephine [neutral]: "In my head, Mistria is still the bustling town it used to be before the earthquake."
Josephine [wink]: "I wish you could have seen it, [Ari]!"

### chocolate_cake.c.toml

- Refresh: 1y
- Requires: josephine; josephine_zone = inn/kitchen

Josephine [neutral]: "I'm making chocolate cake! The kids like it with extra chocolate."

### cleaning_rooms.c.toml

- Refresh: 1y
- Requires: josephine; josephine_routine = room_clean

Josephine [think, drop]: "I found a stick in here, but I'm not quite sure whether it's Luc's bug inspector or Maple's royal scepter."

### daisies_song.c.toml

- Priority: max
- Refresh: 6d
- Requires: josephine; josephine_animation = sing

Josephine [happy, music_notes]: "Picking daisies a'one, a'two ~"
Josephine [happy, music_notes]: "One for my baby and one for you ~"

### date_night.c.toml

- Refresh: 1y
- Requires: josephine; jh_date_night = true; time_of_day = night

Josephine [happy, sparkles]: "Hemlock is such a gentleman... What a perfect day with a perfect man."

### drinking_contest.c.toml

- Refresh: 1y
- Requires: josephine; josephine_zone = same as balor_zone

Josephine [neutral]: "Balor challenged me to a drinking contest."
Josephine [happy]: "He must love to lose."

### duet_with_hemlock.c.toml

- Source: NAR-651 / Trellis: "Conversations/Bank/Josephine/16. Duet with Hemlock"
- Priority: max
- Refresh: 6d
- Requires: josephine; location = inn; josephine_animation = sing; weather = rainy; jo_and_hem_performance = true

Josephine [happy, music_notes]: "Come in from the cold a while... I'll put on the mint and the chamomile..."

### eating_enough.c.toml

- Refresh: 1y
- Requires: josephine
- Action: gives item loaded_baked_potato

Josephine [sad]: "[Ari]! Are you eating enough? I won't be happy unless you take some leftovers home."

### fall_bathhouse.c.toml

- Refresh: 1y
- Requires: josephine; season = fall; location = bathhouse_change_room

Josephine [happy]: "Nothing like a hot bath to warm you up on a chilly fall day."

### fall_inn.c.toml

- Refresh: 1y
- Requires: josephine; season = fall; location = inn

Josephine [neutral]: "I know it's fall because I keep finding leaves indoors!"
Josephine [sad]: "How do they get in here?"

### general_store.c.toml

- Refresh: 1y
- Requires: josephine; not at general_store; time_of_day = morning; not traveling from general_store

Josephine [think]: "I wonder what fresh produce they've got over at the General Store. Maybe I'll drop by later."

### getting_ready_to_sing.c.toml

- Source: NAR-1373 / Trellis: "Conversations/Bank/Josephine/15. Getting ready to sing"
- Refresh: 1y
- Requires: josephine; jo_and_hem_performance_night = true; location = inn; josephine_zone = same as hemlock_zone

Josephine [wink]: "Hemlock talked me into a song... he's still got a silver tongue, that one."

### greeting_ari.c.toml

- Source: NAR-692 / Trellis: "Conversations/Bank/Josephine/54. Greeting Ari"
- Priority: max
- Refresh: never
- Requires: josephine; josephine_has_met = false

Josephine [neutral]: "Well, you must be our new farmer! Adeline mentioned you'd be arriving soon."
Josephine [happy]: "Delighted to meet you [Ari]. You can call me Josephine, though I also go by Jo."
Josephine [neutral]: "I run the $Sleeping Dragon Inn$ with my husband, Hemlock, and our children, Reina, Maple and Luc. Have you met them all yet?"
Josephine [happy]: "Stop by anytime dear. You're always welcome whether you need a meal or just want a chat."
Josephine [wink]: "It'd be my pleasure to serve up either!"

### hem_and_balor_play_cards.c.toml

- Source: NAR-1371 / Trellis: "Conversations/Bank/Josephine/9. Hemlock and Balor playing cards"
- Refresh: 1y
- Requires: josephine; location = inn; hemlock_playing_poker = true; balor_playing_poker = true; hemlock at inn; balor at inn

Josephine: "Hemlock's pretty good at cards, but Balor seems like a bit of a shark. Of course Terithia's the biggest shark of them all, she'd clean them both out!"

### hemlock_cleans.c.toml

- Refresh: 1y
- Requires: josephine; hemlock_routine = inn_chores

Josephine [neutral]: "Thank goodness Hemlock loves a tidy inn."
Josephine [wink, hearts]: "Personally, I love a husband who cleans!"

### hemlock_fine.c.toml

- Refresh: 1y
- Requires: josephine; josephine same location as hemlock

Josephine [neutral]: "Hemlock's so handsome, isn't he? We've been together for ages, but he's aged like a fine wine."

### hemlock_gave_her_tea.c.toml

- Source: NAR-1211 / Trellis: "Conversations/Bank/Josephine/8. Hemlock gave her tea"
- Refresh: 1y
- Requires: josephine; hemlock_made_tea = true; location = inn
- Writes: hemlock_made_tea = false

Josephine [happy]: "Hemlock's a sweetheart, he always has tea waiting for me at the beginning of my shift."

### hemlock_is_on_shift.c.toml

- Source: NAR-1253 / Trellis: "Conversations/Bank/Josephine/6. Hemlock is on shift"
- Refresh: 1y
- Requires: josephine; hemlock at inn/Inn Register; josephine_zone = town/inn_yard_chores OR town/inn_yard_chat

Josephine: "Hemlock's on the till for a bit, perfect time to tidy the yard!"

### hope_kids_arent_at_fountain.c.toml

- Source: NAR-1259 / Trellis: "Conversations/Bank/Josephine/7. Hope Kids Aren't At Fountain"
- Refresh: 1y
- Requires: josephine; fountain_play = true; josephine not in same building as dell, luc, or maple

Josephine [think]: "I wonder what the kids are up to... I hope they're not playing in the fountain again, they never remember to dry their shoes."

### hot_tea.c.toml

- Refresh: 3m
- Requires: josephine; season != summer; josephine_routine in [inn_table_service, inn_bar_service, inn_solo_josephine, inn_solo_bartend, inn_chores]

Josephine [neutral]: "Nothing like a hot cup of tea while you're doing the day's work!"

### in_kitchen_try_this.c.toml

- Source: NAR-649 / Trellis: "Conversations/Bank/Josephine/2. In Kitchen Try This"
- Refresh: 1y
- Requires: josephine; josephine_zone = inn/kitchen
- Action: gives item strawberry_shortcake

Josephine: "Reina's the rising star, but the whole family can whip up something special in the kitchen. In fact, try this!"

### inn_bustling.c.toml

- Refresh: 1y
- Requires: josephine; day_time >= 8:00pm; location = inn; inn_counter >= 8

Josephine [happy]: "My my, the Inn is bustling tonight!"

### inn_is_awake.c.toml

- Refresh: 1y
- Requires: josephine; time_of_day = morning; location = inn

Josephine [happy, cheery]: "The Sleeping Dragon Inn... is awake!"

### inn_running_is_hard.c.toml

- Source: NAR-1363 / Trellis: "Conversations/Bank/Josephine/0. Inn Running is Hard"
- Refresh: 1y
- Requires: josephine

Josephine [happy]: "Big inn like ours takes a lot of running, but I take pride in all of it!"

### keep_moving.c.toml

- Refresh: 3m
- Requires: josephine; is_inside = false; season = winter

Josephine [sad, sigh]: "Oh, but I do miss the summer! We'd both better keep moving if we want to stay warm!"

### kitchens_open.c.toml

- Refresh: 1y
- Requires: josephine; josephine_routine in [inn_solo_josephine, inn_table_service, inn_bar_service, inn_josephine_fnati]

Josephine [neutral]: "Kitchen's open if you're hungry, [Ari]! Just let me know what you'd like."

### little_to_do.c.toml

- Refresh: 1y
- Requires: josephine; josephine_routine in [inn_table_service, inn_solo_josephine, inn_chores, inn_bar_service, inn_solo_bartend, inn_yard_chores]

Josephine [neutral]: "There's always a little more to do when you run an Inn, but that's why I like it! It keeps me busy!"

### luc_and_maple_like_broccoli.c.toml

- Source: NAR-1260 / Trellis: "Conversations/Bank/Josephine/10. Luc and Maple like broccoli"
- Refresh: 1y
- Requires: josephine

Josephine [wink]: "Luc and Maple have been really into broccoli lately... I better make the most of it while it lasts!"

### luc_and_maple_sleep.c.toml

- Refresh: 1y
- Requires: josephine

Josephine [neutral]: "It was tough getting Maple and Luc to sleep the other night. They were too excited about some adventure they had!"

### lullaby.c.toml

- Refresh: 1y
- Requires: josephine; not in maples_room; not in lucs_room; time_of_day = evening OR night

Josephine [neutral]: "You know, used to be a time that Luc and Maple wouldn't fall asleep unless I sang them a lullaby."
Josephine [embarrassed]: "They grow up so quickly!"

### march_post_8h_lines.c.toml

**march_post_8h_follow_up_steak**
- Refresh: never
- Requires: josephine; march_post_8h_steak = true

Josephine [neutral]: "Did March give you that =Mushroom Steak Dinner=? Don't tell him I told you, but he worked so hard on that."
Josephine [happy]: "The plates kept piling up because he kept remaking it..."
Josephine [wink]: "He wanted it to be perfect. Eventually, there was nothing to do but shoo him out of the kitchen!"

**march_post_8h_ambient**
- Refresh: never
- Requires: josephine; march_is_dating = true
- Action: bark "cute_face" on josephine

Josephine [neutral]: "I've known March since he was a little one, so I can read him like a book."
Josephine [sad]: "He's not the best at communicating his feelings. He's always been like that."
Josephine [happy]: "But it looks like he's getting better... Congratulations on getting through to him!"

### mistria_lively.c.toml

- Refresh: 1y
- Requires: josephine; date_time <= 2w

Josephine [happy, cheery]: "Mistria's been a little more lively since you arrived, [Ari]. It makes my heart swell!"

### negotiation.c.toml

- Refresh: 1y
- Requires: josephine; time_of_day = morning

Josephine [neutral]: "I told the kids they had to help me clean today, and it turned into a negotiation."
Josephine [think]: "On the one hand, troublesome. On the other hand, I admire their initiative."

### pickup.c.toml

- Refresh: 1y
- Requires: josephine; reina at haydens_farm OR haydens_house; josephine_routine = general_store_shopping; time_of_day != night

Josephine [neutral]: "It takes a lot to run an Inn! Reina's picking up about half of it from Hayden, and I'm picking up the other half just now. Now, did Reina say tomato or potato?"
Josephine [sad, sweat]: "Suppose I'll just have to get both!"

### quiche.c.toml

- Refresh: 1y
- Requires: josephine; farm_groceries = true; reina at inn; location = inn

Josephine [happy]: "Reina made =Quiche= out of some of the eggs she got from Hayden. Mm-mm!"

### rain_fire_crackle.c.toml

- Refresh: 1y
- Requires: josephine; weather = rainy; location = inn

Josephine [happy]: "The sound of rain on the roof! The crackle of the fire! How lovely."

### rainy_bathhouse_inviting.c.toml

- Refresh: 1y
- Requires: josephine; weather = rainy; location = bathhouse_change_room

Josephine [think]: "The bathhouse somehow becomes MORE inviting when it rains. What's up with that?"

### rainy_inn_is_busy.c.toml

- Source: NAR-1372 / Trellis: "Conversations/Bank/Josephine/12. Rainy Inn is busy"
- Refresh: 1y
- Requires: josephine; reina at general_store_store; location = inn; weather = rainy

Josephine: "Rainy days tend to be busy for us... Reina's gone to the General Store to stock up."

### reading_bee_book_to_luc.c.toml

- Source: NAR-650 / Trellis: "Conversations/Bank/Josephine/4. Reading Bee Book to Luc"
- Refresh: 1y
- Requires: josephine; location = lucs_room; luc at lucs_room/Luc Bed; day_time >= 7:00pm

Josephine: "\"A large component of honeybee communication is in a complex dance language-\""

### register_1.c.toml

- Refresh: 1y
- Requires: josephine; location = inn; josephine_routine in [inn_solo_josephine, inn_table_service, inn_bar_service]

Josephine: "[Ari]! So nice to see you. Make yourself comfortable, and let me know if I can get you anything!"

### register_2.c.toml

- Refresh: 1y
- Requires: josephine; location = inn; josephine_routine in [inn_solo_josephine, inn_table_service, inn_bar_service]

Josephine [happy]: "Make yourself right at home, [Ari]. We'll bring you a meal when you're ready."

### reina_cooking.c.toml

- Refresh: 1y
- Requires: josephine; location = inn; reina at inn; reina_zone = inn/kitchen

Josephine [happy, cheery]: "Do you smell that? Reina's cooking something good."

### reina_new_ideas.c.toml

- Refresh: 1y
- Requires: josephine; josephine_zone = same as reina_zone; location = inn

Josephine [wink]: "Ooh, Reina's got some fresh ideas for the menu next week, wait till you see them."

### reina_sets_the_menu.c.toml

- Source: NAR-1261 / Trellis: "Conversations/Bank/Josephine/13. Reina sets the menu"
- Refresh: 1y
- Requires: josephine; time_of_day = morning OR afternoon; reina_routine in [inn_table_service, inn_solo_reina, inn_reina_fnati]

Josephine: "Reina's setting the menu today! She's so reliable, Hemlock and I are lucky."

### reina_writes.c.toml

- Refresh: never
- Requires: josephine; josephine_zone != reina_zone; reina_heart_level >= 1 and < 5

Josephine [neutral]: "Reina always makes sure to write down a recipe idea whenever one comes to her..."
Josephine [happy]: "But my favorite is when she adds some of the story behind how she came up with it, too."
Josephine [embarrassed]: "She's so creative. In many ways, she reminds me of a younger Hemlock!"

### scales.c.toml

- Priority: max
- Refresh: 1y
- Requires: josephine; josephine_animation = sing; not at inn/Jo Singing; jo_and_hem_performance = false

Josephine [think, music_notes]: "Do re mi fa so la ti do!"
Josephine [happy, music_notes]: "Do ti la so fa mi re do!"

### shopping.c.toml

- Refresh: 1y
- Requires: josephine; josephine_routine = general_store_shopping

**shopping:** Josephine [think]: "Just picking up some veggies for today's soup."

**shopping_2:** Josephine [think]: "I'll want some extra potatoes for next week's soup, and Reina was asking after flour... oh, and honey for my tea..."

### sing_tonight.c.toml

- Refresh: 1y
- Requires: josephine; jo_and_hem_performance_night = true; elsie_performance_night = true; time_of_day = morning OR afternoon

Josephine [happy]: "Hemlock and I are thinking of doing a little music night at the Inn. Elsie might even join in!"

### sing_with_me.c.toml

- Refresh: 1y
- Requires: josephine; weather = pleasant; is_inside = false; josephine_animation = sing

Josephine [happy, music_notes]: "Sunny days make me want to sing! Sing with me, [Ari]!"

### singing.c.toml

- Priority: max
- Refresh: 6d
- Requires: josephine; josephine_animation = sing; jo_and_hem_performance = true
- no_speaker = true

"(Jo is busy performing, you shouldn't interrupt her.)"

### singing_practice.c.toml

- Source: NAR-1252 / Trellis: "Conversations/Bank/Josephine/5. Singing Practice"
- Priority: max
- Refresh: 6d
- Requires: josephine; josephine_animation = sing

Josephine [music_notes]: "And when the wind comes by to blow / The silver seeds dance to and fro,"
Josephine: "And you and I will come and go, / Dancing to and fro..."

### soup_today.c.toml

- Refresh: 1y
- Requires: josephine; location = inn; josephine_routine in [inn_solo_josephine, inn_table_service, inn_bar_service]

Josephine: "Hi, [Ari]! Have you tried the soup today? Get yourself a big helping from the pot!"

### spatula.c.toml

- Refresh: 1y
- Requires: josephine; josephine_zone = inn/kitchen

Josephine [think]: "Now where did I put that spatula?"

### special_today.c.toml

- Refresh: 1y
- Requires: josephine; location = inn; josephine_routine in [inn_solo_josephine, inn_table_service, inn_bar_service]

Josephine: "Have you seen the special, [Ari]? Reina would love if you tried it."

### summer_mornings.c.toml

- Refresh: 3m
- Requires: josephine; location = inn; season = summer; time_of_day = morning

Josephine [happy]: "On summer mornings, the first thing I do is throw open the windows to get a nice, cool cross-breeze going."

### thawed_out.c.toml

- Refresh: 3m
- Requires: josephine; location = inn; season = winter

Josephine [wink]: "Stick around and get yourself thawed out!"

### tidy_inn.c.toml

- Refresh: 1y
- Requires: josephine; josephine_routine = inn_chores

Josephine [neutral]: "Keeping the Inn all shipshape is a full-time job! Luckily, the whole family pitches in."

### time_for_luc_sleep.c.toml

- Source: NAR-1370 / Trellis: "Conversations/Bank/Josephine/3. Time for Luc Sleep"
- Refresh: 1y
- Requires: josephine; josephine traveling to lucs_room; day_time >= 7:00pm

Josephine [think]: "Time to put Luc to bed. He likes to hear bug facts as he drifts off to sleep..."

### trail_mix.c.toml

- Refresh: 1y
- Requires: josephine; health_percent <= 0.5
- Action: gives item trail_mix

Josephine [sad]: "Oh my goodness, look at you, you're exhausted. Don't worry, I keep an emergency snack for the kids. You have it."

### travel_to_shift.c.toml

- Source: NAR-1210 / Trellis: "Conversations/Bank/Josephine/1. Travel to Shift"
- Refresh: 1y
- Requires: josephine; josephine traveling to inn; reina at inn; reina_routine = inn_table_service; time_of_day != morning

Josephine: "Time for my shift in the kitchen. Reina's been working on a new recipe all morning, she needs a break!"

### try_the_soup.c.toml

- Refresh: 1y
- Requires: josephine; location = inn

Josephine [wink]: "Don't forget to try the soup, [Ari]!"

### watch_reina_cook.c.toml

- Source: NAR-1262 / Trellis: "Conversations/Bank/Josephine/14. Watch Reina cook"
- Refresh: 1y
- Requires: josephine; reina_routine = inn_table_service; location = inn

Josephine: "Watch Reina closely, [Ari]... this kitchen is where the magic happens!"

### week_one_pt_1.c.toml

- Source: NAR-694 / Trellis: "Conversations/Bank/Josephine/55. Week one pt 1"
- Priority: max
- Refresh: never
- Requires: josephine; last spoken to > 8h ago; date_time < 14d

Josephine [neutral]: "Oh [Ari]! Have you had anything to eat yet?"
Josephine [think]: "Don't forget to take a big bowl of soup from the Inn's pot, Reina changes the recipe daily!"

### week_one_pt_2.c.toml

- Source: NAR-693 / Trellis: "Conversations/Bank/Josephine/56. Week one pt 2"
- Priority: max
- Refresh: never
- Requires: josephine; date_time < 14d

**week_one_pt_2:**
Josephine [think]: "You must be working so hard down on the farm, [Ari]!"
Josephine [sad]: "Are you eating enough? Sleeping enough?"

**week_two:**
- Priority: max
- Refresh: never
- Requires: josephine; location = inn; adeline_heart_level <= 8; date_time > 10d and < 21d
- Action: gives item coffee x2

Josephine [neutral]: "Oh, [Ari]!"
Josephine [embarrassed]: "Would you mind doing me a little favor?"
Josephine [think]: "I've been a bit worried about Adeline..."
Josephine [sad]: "She's been working so hard since she took over managing the town in her parents' absence."
Josephine [neutral]: "Why don't you bring her a =Coffee=? I feel like she could use a pick-me-up."
Josephine [wink]: "And while I'm at it... I feel like you could, too."

### week_two_mill.c.toml

- Refresh: never
- Requires: josephine; date_time > 7d and < 17d; quest_repair_the_mill_complete = false
- Action: bark "sweat_drop" on josephine

Josephine [think]: "The price of $Flour$ keeps going up..."
Josephine [embarrassed, drop]: "But with the Mill out of commission, what can we do?"

### welcome.c.toml

- Refresh: 1y
- Requires: josephine; location = inn

**welcome:**
Josephine [neutral]: "Welcome to the Sleeping Dragon Inn!"
Josephine [happy]: "Oh, it's you [Ari]! Hanging in there?"

**welcome_2:**
Josephine [happy]: "Welcome to the Sleeping Dragon Inn, [Ari]! Make yourself at home!"

---

## Market Lines

Source: `source/t2/Conversations/Bank/Josephine/Market Lines/`

### market_darcy_1.c.toml

- Source: NAR-1257 / Trellis: "Conversations/Bank/Josephine/18. Market Darcy 1"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_darcy_stall

Josephine: "I always visit Darcy's booth when she's here... she has so many =Teas=, there's always a new one to try."

### market_darcy_2.c.toml

- Source: NAR-652 / Trellis: "Conversations/Bank/Josephine/19. Market Darcy 2"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_darcy_stall

Josephine: "I'd say that Hemlock gets about 8 out of 10 gifts for me from Darcy... she has so many =Teas=, he's always able to surprise me."

### market_darcy_3.c.toml

- Source: NAR-1255 / Trellis: "Conversations/Bank/Josephine/20. Market Darcy 3"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_darcy_stall

Josephine: "Be sure to try some of Darcy's flower teas... She gets her ingredients right from Celine's garden. A real Mistrian specialty!"

### market_darcy_4.c.toml

- Source: NAR-653 / Trellis: "Conversations/Bank/Josephine/21. Market Darcy 4"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_darcy_stall

Josephine: "I'm supposed to be running errands, but Hemlock bullied me into visiting Darcy when he heard she was in town. He knows I love my =Teas=!"

### market_louis_1.c.toml

- Source: NAR-657
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_louis_stall

Josephine [neutral]: "Did you know Louis made my wedding dress? He designed the whole thing around a flower I brought him."

### market_louis_2.c.toml

- Source: NAR-1100
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_louis_stall

Josephine [neutral]: "Between you and me, Louis does NOT take well to haggling. Pay the man what he asks, [Ari]."

### market_louis_3.c.toml

- Source: NAR-1094
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_louis_stall

Josephine [neutral]: "I saw a cardigan that would look SO adorable on Hemlock, it's even in his colors!"

### market_louis_4.c.toml

- Source: NAR-1090
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_louis_stall

Josephine [happy]: "A little bird told me Louis had some new dresses at his booth... I can't wait to try them on!"

### market_merri_1.c.toml

- Source: NAR-1256 / Trellis: "Conversations/Bank/Josephine/30. Market Merri 1"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_merri_stall

Josephine: "Merri is our first stop when we're furnishing the Inn... she's great at restoring furniture."

### market_merri_2.c.toml

- Source: NAR-658 / Trellis: "Conversations/Bank/Josephine/31. Market Merri 2"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_merri_stall

Josephine: "The screen and armchairs in our bedroom are a set we got from Merri several seasons back. She even reupholstered the chairs so nicely!"

### market_merri_3.c.toml

- Source: NAR-1375 / Trellis: "Conversations/Bank/Josephine/32. Market Merri 3"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_merri_stall

Josephine: "Maple wants the most princessy everything... I've been on the lookout for a canopy bed. Maybe I'll put in a request with Merri..."

### market_merri_4.c.toml

- Source: NAR-659 / Trellis: "Conversations/Bank/Josephine/33. Market Merri 4"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_merri_stall

Josephine: "My goodness, how does Merri get her booth set up? Everything looks so heavy!"

### market_stillwell_1.c.toml (COMMENTED OUT)

- Source: NAR-660 / Trellis: "Conversations/Bank/Josephine/34. Market Stillwell 1"
- Entire conversation block is commented out in source

Josephine: "Once upon a time, Stillwell predicted a mysterious stranger with a big appetite would come to Mistria... and the next day you rolled into town!"

### market_stillwell_2.c.toml (COMMENTED OUT)

- Source: NAR-661 / Trellis: "Conversations/Bank/Josephine/35. Market Stillwell 2"
- Entire conversation block is commented out in source

Josephine: "I always bring Stillwell lunch when he's working the Saturday Market... something about that one makes you want to take care of him. It might be all the wailing."

### market_stillwell_3.c.toml

- Source: NAR-662 / Trellis: "Conversations/Bank/Josephine/36. Market Stillwell 3"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_stillwell_stall

Josephine: "Stillwell said \"Welcome the visitor in blue, or face calamity upon calamity\"... Luc's new beetle is blue... coincidence?"

### market_stillwell_4.c.toml

- Source: NAR-663 / Trellis: "Conversations/Bank/Josephine/37. Market Stillwell 4"
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_stillwell_stall

Josephine: "Nora always asks for a money fortune... well, she is very pragmatic..."

### market_taliferro.c.toml

- Priority: max; Refresh: 1y (all entries)
- Requires: josephine; josephine_activity = visit_taliferro_stall

**market_taliferro_1:**
Josephine [neutral]: "I'm not so interested in Taliferro's $Cooking Challenge$, but his kitchen? It's a beauty!"

**market_taliferro_2:**
Josephine [neutral]: "Are you thinking of entering Taliferro's $Cooking Challenge$? You ought to!"
Josephine [happy]: "You've practiced so much to build up your skills! Reina's always saying so!"

**market_taliferro_3:**
Josephine [wink]: "The Sleeping Dragon Inn doesn't need a traveling kitchen, but if we did, I bet Taliferro's would do the trick!"

**market_taliferro_4:**
Josephine [neutral]: "Say what you will about Taliferro..."
Josephine [wink]: "And I say a LOT..."
Josephine [happy]: "But he does run a clean kitchen. Gotta respect that."

### market_vera_1.c.toml

- Source: NAR-686
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_vera_stall

Josephine [neutral]: "Maple keeps saying she wants to try out pink hair. Where do you suppose she got that idea?"

### market_vera_2.c.toml

- Source: NAR-670
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_vera_stall

Josephine [neutral]: "Vera usually asks me to schedule in advance with her when I want to get my hair done."
Josephine [happy]: "It does take a while, but really it's an excuse to catch up!"

### market_vera_3.c.toml

- Source: NAR-669
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_vera_stall

Josephine [neutral]: "When I told Hemlock I might have Vera dye my hair purple, he got so excited... that sweet man does love when I express my artistic side."

### market_vera_4.c.toml

- Source: NAR-668
- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_vera_stall

Josephine [neutral]: "Reina says she's thinking of dyeing her hair... It might be a fun mother-daughter activity."

### market_wheedle_1.c.toml

- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_wheedle_stall

Josephine [neutral]: "Sweet Hemlock told me not to trust a word out of Wheedle's mouth, but I don't even need to hear that man talk."
Josephine [mad]: "That smile is too sneaky, [Ari]! I just don't trust it!"

### market_wheedle_2.c.toml

- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_wheedle_stall

Josephine [think]: "When Hemlock and I were in the band, we had some flashy looks..."
Josephine [happy, drop]: "But when you put those looks on a guy like Wheedle, it tells a whole different story, doesn't it?"

### market_wheedle_3.c.toml

- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_wheedle_stall

Josephine [think]: "Wheedle figured out that I like tea, so now he's always trying to sell me some new kind of blend from some faraway place."
Josephine [mad]: "But I saw him pull that grass up on his way into town! And I can do that myself, thank you very much."

### market_wheedle_4.c.toml

- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_wheedle_stall

Josephine [ugh]: "Take it from me, [Ari]... never accept an IOU from Wheedle."
Josephine [mad]: "You wouldn't believe the tab that man has racked up at the Sleeping Dragon Inn."

### market_zorel_1.c.toml

- Priority: max; Refresh: 1y
- Requires: josephine; josephine_activity = visit_zorel_stall

Josephine [happy]: "Goodness, it is so nice to have Zorel in town!"
Josephine [neutral]: "We're friends with her folks you know, back when Hemlock used to be in that band of his."
Josephine [happy]: "I've known her since she was Luc's age!"

---

## Museum Lines

Source: `source/t2/Conversations/Bank/Josephine/Museum Lines/`

### caldosian_drinking_horn.c.toml

- Source: NAR-82
- Refresh: 1y
- Requires: josephine; museum_donated_caldosian_drinking_horn = true; not at museum

Josephine: "I was looking at that =Caldosian Drinking Horn= they've got on exhibit at the Museum, [Ari]. It's so dashing!"
Josephine [happy]: "I thought I might commission March to make one =for Hemlock=."

### crystalline_cricket.c.toml

- Refresh: 1y
- Requires: josephine; museum_donated_crystalline_cricket = true; not at museum

Josephine [neutral]: "Olric came in here the other day, asking me to teach him how to sing."
Josephine [think]: "He heard that $Crystalline Cricket$ at the Museum sings to stones, and now he wants to do it too!"

### flame_pepper.c.toml

- Refresh: 1y
- Requires: josephine; museum_donated_flame_pepper = true; not at museum

Josephine [think]: "The $Flame Pepper$ at the Museum... apparently, it's quite spicy."
Josephine [wink]: "I'd like to be the judge of that!"

### spirit_mushroom.c.toml

- Refresh: 1y
- Requires: josephine; museum_donated_spirit_mushroom = true; not at museum

Josephine [neutral]: "The luminescent $Spirit Mushroom$ at the Museum... I'd never seen one before. What a color!"
Josephine [think]: "I wonder if it makes a nice tea?"

---

## Gift Lines

Source: `source/t2/Conversations/Bank/Josephine/Gift Lines/gift_lines.c.toml`

### Specific Gift Reactions

**crayfish_etouffee** (loved)
- Refresh: 2w
- Requires: josephine; gift_desire = loved; gift_given = crayfish_etouffee

Josephine [happy, hearts]: "Oh, =Etouffee=! I love etouffee! I'm going to share this with Hemlock, he loves it too!"

**worm** (hated)
- Requires: josephine; gift_desire = hated; gift_given = worm

Josephine [sad, sick]: "I get bugs two, sometimes three times a day from Luc. I don't need a $Worm$ from you!"

### Generic Gift Reactions

**loved_gift:**
Josephine [happy, hearts]: "Oh, that smells wonderful! Thank you so much, dear!"

**loved_gift_2:**
Josephine [happy, sparkles]: "Aren't you a good egg, [Ari]! You know just what I like!"

**loved_gift_edible** (refresh 1w; for chili_coconut_curry, crayfish_etouffee, incredibly_hot_pot, quiche):
Josephine [happy, sparkles]: "Mm, smell those spices! Incredible! Thank you for sharing, [Ari]. You have a big heart!"

**loved_gift_tea** (refresh 1w; for cup_of_tea, green_tea, jasmine_tea, lavender_tea, roasted_rice_tea, rose_tea):
Josephine [happy, cheery]: "Goodness, the fragrance of this tea is divine! Perfect for my next break. Thank you!"

**liked_gift:**
Josephine [happy]: "Oh, aren't you a good one. Thank you, [Ari]."

**liked_gift_2:**
Josephine [neutral]: "Oh, how helpful! Thank you, [Ari]."

**liked_gift_flowers** (refresh 1w; for breath_of_fire, essence_blossom, jasmine, rose, sunflower):
Josephine [happy]: "Flowers! For me? Why thank you, [Ari]."
Josephine [wink]: "You know, he still surprises me with flowers! It's like he's still courting me, and I don't mind one bit."

**liked_gift_ingredients** (refresh 1w; for chili_pepper, curry_powder, flour, honey, oil, rice, soy_sauce, sugar):
Josephine [neutral]: "Thank you, [Ari]! This is perfect for the kitchen."

**neutral_gift:**
Josephine [neutral]: "Thank you!"

**disliked_gift:**
Josephine [think]: "I see. Well, maybe Luc or Maple can do something with this..."

**birthday_gift** (priority max; for neutral/liked/loved gifts on birthday):
Josephine [happy]: "A birthday gift? Aren't you a sweetheart!"
Josephine [neutral]: "Thank you, [Ari]."

Note: The birthday_gift entry has an empty condition `{ }` in its requires array, which may be a placeholder or formatting artifact in the source.

---

## Festival Lines

Source: `source/t2/Conversations/Festival Lines/Josephine/`

### animal_festival.c.toml

**animal_festival_greeting**
- Priority: max; Refresh: 3m
- Requires: josephine; animal_festival_today = true; josephine at town/af_podium; small_animal_place = undefined; large_animal_place = undefined
- Writes: jo_explained_animal_festival = true (expires 20h)

Josephine [happy]: "Welcome to the Animal Festival, [Ari]!"
Josephine [neutral]: "If you're looking to enter one of your animals into either of the brackets, you can do so at the booths behind me!"
Josephine [wink]: "A little tip, I hear the judging panel's biggest considerations are how high the animal's heart level is, and how rare their coat color is."
Josephine [happy]: "Once you're ready, come talk to me again and we'll start the judging!"

### harvest_festival.c.toml

**harvest_festival_anticipation**
- Refresh: never
- Requires: josephine; harvest_festival_setup = true

Josephine [think]: "It seems like just yesterday I was taking over the $Harvest Festival$ kitchen from my mother. I couldn't have been prouder..."
Josephine [happy]: "And now it's Reina's turn to run the kitchen. How time flies!"

**harvest_festival_0**
- Refresh: 3m; Priority: max
- Requires: josephine; harvest_festival_date after 1d; location = town; time_of_day != night

Josephine [neutral]: "Reina has always helped me out at the Harvest Festival kitchen from the time she was little."
Josephine [happy, cheery]: "Now I get to help her out!"

### shooting_star.c.toml

**shooting_star_anticipation**
- Refresh: 3m
- Requires: josephine; shooting_star_festival_date before 3d; quest_repair_the_summit_stairs_complete = true; has_spouse = false; has_fiance = false

Josephine [neutral]: "Planning to celebrate the Shooting Star Festival, [Ari]?"
Josephine [happy]: "Whether you watch it solo or with a date, it really is a magical experience."

**shooting_star_anticipation_no_summit**
- Refresh: 3m
- Requires: josephine; shooting_star_festival_date before 3d; quest_repair_the_summit_stairs_complete = false

Josephine [neutral]: "Looking forward to the Shooting Star Festival, [Ari]?"
Josephine [happy]: "It might not be possible to view them from the Summit with a date this year, but we can still enjoy the atmosphere around town with friends and family!"

**shooting_star_day_of**
- Priority: max; Refresh: 3m
- Requires: josephine; shooting_star_festival_date after 1d; day_time < 8:00pm; josephine not at town/star_festival_josephine

Josephine [neutral]: "Reina was busy in the kitchen again this morning."
Josephine [happy]: "She always makes some snacks to enjoy while we watch the stars!"

**shooting_star_balor_follow_up_josephine**
- Priority: max; Refresh: 3m
- Requires: josephine; shooting_star_date_status = balor_went; shooting_star_festival_date after 2d; balor_is_partner = false

Josephine [think]: "I noticed the light was on in Balor's room late into the night... Maybe he couldn't sleep?"

**shooting_star_balor_8h_follow_up_josephine**
- Priority: max; Refresh: 3m
- Requires: josephine; shooting_star_date_status = balor_went; shooting_star_festival_date after 2d; balor_is_partner = true

Josephine [happy]: "It does my heart good to see you and Balor taking care of each other."
Josephine [wink]: "It means I can worry less... about both of you!"

**shooting_star_march_follow_up_josephine**
- Priority: max; Refresh: never
- Requires: josephine; shooting_star_date_status = march_went; shooting_star_festival_date after 6d; march_is_partner = false
- Player choice prompts

Josephine [neutral]: "Oh, you wanted to ask me something? What is it, dear?"

Player choice:
- "What exactly is the deal with March?"
- "Is there something I should know about March's family?"

Both lead to:
Josephine [think]: "Ah... well, I suppose you wouldn't know, would you?"
Josephine [sad]: "Despite how things might seem, March hasn't always had it easy. He and Olric lost their parents pretty young, back when they were still new to town."
Josephine [think]: "Don't let March's attitude get to you, [Ari]. He's been through a lot, and he's a kinder person than he lets on..."
Josephine [neutral]: "You just have to give him time."

**shooting_star_reina_follow_up_josephine**
- Priority: max; Refresh: 3m
- Requires: josephine; shooting_star_date_status = reina_went; shooting_star_festival_date after 2d; reina_is_spouse = false

Josephine [neutral]: "Hi, [Ari]!"
Josephine [happy]: "Did you have a nice time with Reina yesterday?"
Josephine [neutral]: "Thanks for making sure to walk her home."

### spring_festival.c.toml

**enjoying_yourself**
- Refresh: 3m; Priority: max
- Requires: josephine; spring_festival_date after 1d

Josephine [happy]: "Hope you're enjoying everything the festival has to offer, [Ari]! I know I am!"

---

## Source Absences

- **No Heart Event files** found in this extraction scope (heart events may exist elsewhere in the conversation tree; Josephine is not dateable so romantic heart events are not expected)
- **No Thread conversations** found for Josephine in this extraction scope (threads may exist in a separate directory)
- **No Group Conversation files** included in this extraction scope (group conversations involving Josephine may exist under other NPC directories)
- **market_stillwell_1 and market_stillwell_2** are entirely commented out in source — the dialogue text exists but the conversation blocks are disabled
- **birthday_gift** requires array contains an empty object `{ }` which may be incomplete
- Several banked lines lack explicit portrait tags (e.g., hem_and_balor_play_cards, rainy_inn_is_busy, several market lines) — these would use the NPC's default portrait
