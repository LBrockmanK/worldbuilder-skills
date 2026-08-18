---
type: reference
title: Hemlock — Conversations
description: 'Extracted dialogue from Hemlock''s conversation bank: banked ambient lines,
  market vendor lines, museum artifact lines, gift response lines, and festival lines.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T18:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Hemlock/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Hemlock/Market Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Hemlock/Museum Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Hemlock/Gift Lines/
- projects/fields-of-mistria/source/t2/Conversations/Festival Lines/Hemlock/
---

# Hemlock — Conversations

Dialogue lines extracted from Hemlock's conversation bank files. Speaker is always Hemlock unless noted. `[Ari]` is the player character's name variable. `=Item=` denotes item highlighting. `$Text$` denotes special text formatting.

## Banked Lines

Source: `source/t2/Conversations/Bank/Hemlock/Banked Lines/`

### greeting_ari (Footsie.c.toml — wrong filename, see note)

*Note: The file is named Footsie.c.toml but contains a conversation keyed `[footsie]`.*

**footsie**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = josephine_zone, jh_date_night = true, location = inn, time_of_day = evening OR night
- Source: NAR-1352
- Portrait: wink
- Hemlock: "I can always tell when Josie's had a bit to drink... she loves to play footsie."

### bartending_1.c.toml

**bartending_1**
- Refresh: 1y
- Requires: hemlock, time_of_day = evening OR night, hemlock_routine = inn_bar_service OR inn_solo_bartend
- Source: NAR-597
- Hemlock: "Nothing like a nightcap after a hard day! Can I get you anything, [Ari]?"

### bartending_2.c.toml

**bartending_2**
- Refresh: 1y
- Requires: hemlock
- Source: NAR-598
- Portrait: wink
- Hemlock: "I've been mixing drinks since I was kid, mom used to say I whipped up a mean hot chocolate."

### basement.c.toml

**basement_1**
- Priority: basement
- Refresh: instantly
- Requires: hemlock
- Portrait: neutral
- Hemlock: "Hey there, [Ari]."

### bathhouse_with_josie.c.toml

**bathhouse_with_josie**
- Refresh: 1y
- Requires: hemlock, location = bathhouse_change_room, hemlock_zone = josephine_zone
- Portrait: happy
- Hemlock: "Josie insisted we stop by the Bathhouse, and I never could say no to her!"

### blustery.c.toml

**blustery**
- Refresh: 3m
- Requires: hemlock, location = inn, season = winter
- Portrait: neutral
- Hemlock: "Blustery out there, isn't it? Why don't you warm up with some soup from the pot!"

### brewing_supplies.c.toml

**brewing_supplies**
- Refresh: 3m
- Requires: hemlock, season = fall, brewing_supplies = true
- Portrait: neutral
- Hemlock: "Hayden got me all the grain I needed! Time to get brewing!"

### bugs_in_lute.c.toml

**bugs_in_lute**
- Refresh: 1y
- Requires: hemlock, hemlock_animation = lute_play
- Portrait: ugh | Effect: drop
- Hemlock: "Luc got bugs in my lute again. Ah well... at least it's not termites this time around."

### chaperone.c.toml

**chaperone**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = dell_zone, hemlock_zone = luc_zone, hemlock_zone = maple_zone
- Portrait: happy
- Hemlock: "The kids have so much energy! Kinda makes me want to play too."

### check_the_stables.c.toml

**check_the_stables**
- Refresh: 1y
- Requires: hemlock, hemlock_is_traveling_to = town/Inn Yard
- Source: NAR-1338
- Hemlock: "I'd better check the stables, see if they need clearin' out."

### checking_on_narrows.c.toml

**checking_on_narrows**
- Refresh: 1y
- Requires: hemlock, dell/luc/maple all at location narrows in same zone, hemlock traveling to or in their zone
- Portrait: neutral
- Hemlock: "The kids are usually fine on their own, but I like to check on them when they're in the Narrows."

### clean_inn.c.toml

**clean_inn**
- Refresh: 1y
- Requires: hemlock, location = inn, hemlock_routine = inn_chores
- Portrait: happy | Effect: music_notes
- Hemlock: "A clean inn is a happy inn!"

### cleaning_rooms.c.toml

**cleaning_rooms**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = room_clean
- Portrait: think
- Hemlock: "I came in here to tidy up, but there's not much to do if I'm being honest."
- Portrait: happy
- Hemlock: "The kids have been keeping their rooms clean lately!"

### common_area.c.toml

**common_area**
- Refresh: 1y
- Requires: hemlock, josephine_animation = sweep, location = inn, josephine at inn
- Portrait: neutral
- Hemlock: "Josie likes to keep the common area so clean it shines."

### drinks_in_bathhouse.c.toml

**drinks_in_bathhouse**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = juniper_zone OR hemlock_building = bathhouse
- Portrait: think | Effect: drop
- Hemlock: "Juniper didn't take too kindly to my idea of bringing drinks into the bath. I'm just saying, I think folks would like it."
- Portrait: wink
- Hemlock: "Folks being me."

### early_morning.c.toml

**early_morning**
- Refresh: 1y
- Requires: hemlock, day_time between 6:00am and 9:00am
- Portrait: happy
- Hemlock: "When I was with the band, we got up a heck of a lot earlier than this. Up and at'em!"

### fall_inn.c.toml

**fall_inn**
- Refresh: 3m
- Requires: hemlock, location = inn, season = fall
- Portrait: neutral
- Hemlock: "Fall's a good season for the Inn. Everyone wants to get cozy by the hearth and enjoy each other's company."

### fnati_busy.c.toml

**fnati_busy**
- Refresh: 1y
- Requires: hemlock, day_of_the_week = friday, time_of_day = morning, location = inn
- Portrait: happy
- Hemlock: "Today's our busiest evening of the week. Whole town's going to be here, soon enough."

### free_soup.c.toml

**free_soup**
- Refresh: 1y
- Requires: hemlock, location = inn
- Portrait: wink
- Hemlock: "The soup smells great today! Have yourself a bowl, it's always on the house!"

### fun_and_good.c.toml

**fun_and_good**
- Refresh: 1y
- Requires: hemlock, hemlock_heart_level >= 2
- Portrait: neutral
- Hemlock: "Life with the band was fun, but a family and a hearth?"
- Portrait: happy | Effect: sparkles
- Hemlock: "Now life's fun AND good. Real good."

### get_you_something.c.toml

**get_you_something**
- Refresh: 1y
- Requires: hemlock, location = inn
- Portrait: wink
- Hemlock: "Let me know if we can get you something from the kitchen, [Ari]."

### good_to_me.c.toml

**good_to_me**
- Refresh: 1y
- Requires: hemlock
- Portrait: happy
- Hemlock: "Mistria's been good to me."

### greeting_ari.c.toml

**greeting_ari**
- Priority: max
- Refresh: never
- Requires: hemlock, hemlock_has_met = false
- Source: NAR-1348
- Portrait: think
- Hemlock: "Now who do we have here? Are you the new farmer everyone's been talking about?"
- Portrait: neutral
- Hemlock: "Good to meet you, [Ari], I'm Hemlock. If you ever need a hot meal or a cold drink, be sure to stop by the $Sleeping Dragon Inn$."
- Portrait: happy
- Hemlock: "There's always a cauldron of hearty soup kept hot for anyone who wants a bowl!"

### hayden_quiet.c.toml

**hayden_quiet**
- Refresh: never
- Requires: hemlock, date_time > 4d and < 30d, valen_zone != hayden_zone, location = inn, hayden_heart_level = 1
- Actions: bark = ellipses (hemlock)
- Portrait: neutral
- Hemlock: "Hayden's a good guy."
- Portrait: sad
- Hemlock: "Gets pretty quiet when he drinks alone though."
- Portrait: think
- Hemlock: "Wonder what's on his mind?"

### henrietta_got_out.c.toml

**henrietta_got_out**
- Refresh: never
- Requires: hemlock, cutscene_seen_hayden_two_hearts = true
- Portrait: think
- Hemlock: "I heard Hayden's prize chicken got out again. Henrietta's a right rascal."

### herbal_teas.c.toml

**herbal_teas**
- Refresh: 1y
- Requires: hemlock, location = inn, time_of_day = afternoon
- Writes: hemlock_made_tea = true (expires 12h)
- Portrait: neutral
- Hemlock: "Josie's partial to herbal teas in the afternoon. Eiland recommended this one. He's got good taste."

### holt_whittling.c.toml

**holt_whittling**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = holt_zone
- Portrait: neutral
- Hemlock: "Holt's been whittling a rhinoceros beetle for Luc. He's going to go crazy for it!"

### holts_puns.c.toml

**holts_puns**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = holt_zone, holt_just_punned >= 1
- Portrait: wink
- Hemlock: "Holt's puns are so painful, they go all the way around to being funny again."
- Portrait: happy | Effect: drop
- Hemlock: "Josie says he's been like this since they were kids!"

### home.c.toml

**home**
- Refresh: 1y
- Requires: hemlock, hemlock_heart_level >= 4
- Portrait: happy | Effect: sparkles
- Hemlock: "You're really making a home for yourself here! It takes a bit of pluck, don't it?"

### hot_cup_of_tea.c.toml

**hot_cup_of_tea**
- Refresh: 1y
- Requires: hemlock, time_of_day = morning, location = inn
- Source: NAR-1209
- Portrait: wink
- Hemlock: "Morning, [Ari]! We've got a hot cup of tea on the menu... you'll wake right up!"

### how_are_you.c.toml

**how_are_you**
- Refresh: 1y
- Requires: hemlock
- Portrait: wink
- Hemlock: "[Ari], how are ya? Don't work too hard now."

### how_can_i_help.c.toml

**how_can_i_help**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_bar_service OR inn_table_service OR inn_solo_hemlock OR inn_solo_bartend
- Portrait: happy
- Hemlock: "Sleeping Dragon Inn's here to serve. How can I help you?"

### hum.c.toml

**hum**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_bar_service OR inn_table_service OR inn_solo_hemlock OR inn_solo_bartend OR inn_chores OR inn_yard_chores
- Portrait: think
- Hemlock: "I don't usually hum while I work. I get carried away and end up picking up my lute!"
- Portrait: wink
- Hemlock: "I'll leave singing on the job to Josie!"

### inn_breakfast.c.toml

**inn_breakfast**
- Refresh: 1y
- Requires: hemlock, time_of_day = morning, hemlock_activity = eat, location = inn, hemlock_was_last_spoken_to > 6h ago
- Portrait: wink
- Hemlock: "Morning, [Ari]! I'm just finishing up breakfast, but let me know if you need anything."

### inn_tonight.c.toml

**inn_tonight**
- Refresh: 1y
- Requires: hemlock, location != inn, day_time <= 4:00pm, day_of_the_week = friday
- Portrait: wink
- Hemlock: "You coming to the Inn tonight? The company will be good and the drinks even better!"

### josie_is_the_best.c.toml

**josie_is_the_best**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = josephine_zone
- Portrait: happy | Effect: hearts
- Hemlock: "Josie's a beauty with a generous heart, but her voice was what first got me. I was like a moth to the flame."

### lute_tuning.c.toml

**lute_tuning**
- Refresh: 1y
- Requires: hemlock, hemlock_tired_after_performance = true, jo_and_hem_performance = false, jo_and_hem_performance_night = true
- Portrait: think
- Hemlock: "My lute could use tuning, but I'll leave it for tomorrow. Sleep's callin'."

### making_tea_for_jo.c.toml

**making_tea_for_jo**
- Refresh: 1y
- Requires: hemlock, location = inn, josephine_is_traveling_to_location = inn
- Writes: hemlock_made_tea = true (expires 12h)
- Source: NAR-599
- Hemlock: "Hey [Ari], make yourself comfortable! I gotta get the tea going, I like to have it ready for Jo when she comes back."

### march_post_8h_lines.c.toml

**march_post_8h_ambient**
- Refresh: never
- Requires: hemlock, march_is_dating = true
- Actions: bark = cute_face (hemlock)
- Portrait: neutral
- Hemlock: "March has really taken a shine to you, hasn't he?"
- Portrait: wink
- Hemlock: "Good on you. I knew you'd crack that shell sooner or later!"

### market_present.c.toml

**market_present**
- Refresh: 1y
- Requires: hemlock, market_is_back = true, day_of_the_week = friday
- Portrait: think
- Hemlock: "Market's tomorrow... maybe I'll stop in and find a little gift for Josie."

### meal_and_bed.c.toml

**meal_and_bed**
- Refresh: 1y
- Requires: hemlock, location = inn
- Portrait: wink
- Hemlock: "You won't find a hotter meal or a fluffier bed than at the Sleeping Dragon Inn!"

### morning_breakfast.c.toml

**Morning Breakfast**
- Refresh: 1y
- Requires: hemlock, time_of_day = morning, location = inn
- Source: NAR-1344
- Portrait: happy
- Hemlock: "Morning, [Ari]! Some breakfast for you? We've got fresh butter in from Hayden's farm!"

### need_anything.c.toml

**need_anything**
- Refresh: 1y
- Requires: hemlock, location = inn
- Portrait: wink
- Hemlock: "Anyone need anything, you just say the word! That includes you, [Ari]!"

### order.c.toml

**order**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_bar_service OR inn_table_service OR inn_solo_hemlock OR inn_solo_bartend OR inn_chores
- Portrait: neutral
- Hemlock: "Just getting things in order around here. Let me know if I can get you something."

### outdoor_playing.c.toml

**outdoor_playing**
- Refresh: 1y
- Requires: hemlock, hemlock_animation = lute_play, time_of_day = morning, not spoken to in 6h, hemlock at playground zone with dell/luc/maple all at playground zones, is_inside = false
- Source: NAR-595
- Hemlock: "Morning! Wish the audience was more attentive, but you can't beat the venue!"

### performance.c.toml

**perfomance** (sic — typo in source key)
- Priority: max
- Refresh: 6d
- Requires: hemlock, jo_and_hem_performance = true, hemlock_animation = lute_play
- Portrait: wink
- Hemlock: "Hope you're enjoying the performance, [Ari]!"

### put_your_feet_up.c.toml

**put_your_feet_up**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_bar_service OR inn_table_service OR inn_solo_hemlock OR inn_solo_bartend
- Portrait: wink
- Hemlock: "Hey [Ari]! You're lookin' like you could use a good meal. Why don't you put your feet up?"

### rain_brings_people_together.c.toml

**rain_brings_people_together**
- Refresh: 1y
- Requires: hemlock, weather = rainy, time_of_day = morning, location = inn, rainy_inn_night = true
- Portrait: neutral
- Hemlock: "Rain tends to bring people together, which is why a rainy morning is all hands on deck at the Sleeping Dragon Inn."
- Portrait: happy
- Hemlock: "We've got to get the place ready for the folks who come by in the evening!"

### rainy_bartending.c.toml

**rainy_bartending**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_bar_service, weather = rainy, ari_utero = false
- Portrait: happy | Effect: cheery
- Hemlock: "Nothing like mulled cider on a rainy day, [Ari]!"

### rainy_day_soup.c.toml

**rainy_day_soup**
- Refresh: 1y
- Requires: hemlock, location = inn, weather = rainy
- Portrait: wink
- Hemlock: "Rainy days are perfect for some hot soup. Feel free to help yourself! The pot's open to all."

### rainy_shopping.c.toml

**rainy_shopping**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = general_store_shopping, weather = rainy
- Portrait: neutral
- Hemlock: "We were a little low on ingredients at the Inn, so I popped on over to pick some things up."

### reina_got_ahead.c.toml

**reina_got_ahead**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_bar_service OR inn_table_service OR inn_solo_hemlock OR inn_solo_bartend, time_of_day = morning
- Portrait: happy
- Hemlock: "Reina chopped all the ingredients last night... she's always one step ahead of me!"

### reina_is_gone.c.toml

**reina_is_gone**
- Refresh: 1y
- Requires: hemlock, reina_is_traveling_to_location = inn, location = inn
- Source: NAR-1208
- Hemlock: "Reina ought to be back soon, if you were looking for her."

### reina_made_good_soup.c.toml

**reina_made_good_soup**
- Refresh: 1y
- Requires: hemlock, location = inn, hemlock_routine = inn_solo_hemlock OR inn_bar_service OR inn_table_service
- Hemlock: "Reina really outdid herself on today's soup. Take a gander, grab a bowl!"

### saturday_no_market.c.toml

**saturday_no_market**
- Refresh: never
- Requires: hemlock, quest_repair_the_bridge_complete = false, quest_repair_the_bridge_in_progress = true, day_of_the_week = saturday
- Portrait: sad
- Hemlock: "Normally we'd be having a Saturday Market in the town square right now, but it's been anything but normal since the earthquake."

### seridia.c.toml

**seridia_silverware**
- Refresh: 1y
- Requires: hemlock, caldarus_seridia_town = true, caldarus_seridia_town_timer = false, seridia_market_count >= 2, hemlock_zone != seridia_zone, location = inn
- Portrait: neutral
- Hemlock: "Seridia always insists on the finest dishes and silverware when she eats here."
- Portrait: think
- Hemlock: "When I told her we didn't have anything that special, she insisted I check again... and we did!"

### settling_in.c.toml

**settling_in**
- Refresh: never
- Requires: hemlock, hemlock_heart_level >= 2
- Portrait: happy
- Hemlock: "Settling in alright, [Ari]? I was new to Mistria once, too. Don't be shy if you need someone to show you the ropes."

### stay_awhile.c.toml

**stay_awhile**
- Refresh: 1y
- Requires: hemlock, location = inn
- Hemlock: "Sleeping Dragon Inn, at your service! Kick your feet up and stay awhile."

### stove.c.toml

**stove**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = inn/kitchen
- Portrait: neutral
- Hemlock: "Did I ever tell you the story of how we got this stove?"
- Portrait: think
- Hemlock: "It all started when we won a bet with March and Olric's old man..."

### thaw_yourself.c.toml

**thaw_yourself**
- Refresh: 3m
- Requires: hemlock, season = winter, location = inn
- Portrait: happy
- Hemlock: "Menu's looking good today! Grab a seat and thaw yourself out!"

### tidying.c.toml

**tidying**
- Refresh: 1y
- Requires: hemlock, hemlock_routine = inn_chores OR room_clean OR inn_yard_chores
- Portrait: neutral
- Hemlock: "Hey, [Ari]. I'm just tidying up- let me know if you need something."

### time_for_dinner.c.toml

**time_for_dinner**
- Refresh: 1y
- Requires: hemlock, day_time between 6:00pm and 9:30pm
- Source: NAR-600
- Hemlock: "It's about time for dinner, I think. There's always room at our table, [Ari]!"

### travel_to_inn.c.toml

**travel_to_inn**
- Refresh: 1y
- Requires: hemlock, hemlock_is_traveling_to_location = inn, josephine at inn
- Source: NAR-602
- Hemlock: "Can't talk now, [Ari]! Promised I'd take over for Josie at the register."

### walk_to_duet.c.toml

**walk_to_duet**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = josephine_zone
- Source: NAR-603
- Hemlock: "It doesn't take too much effort to talk Josie into a duet, hah. Stick around a while and we'll serenade you!"

### wash_dishes.c.toml

**wash_dishes**
- Refresh: 1y
- Requires: hemlock
- Portrait: think
- Hemlock: "I washed so many dishes while I was touring with the band."
- Portrait: happy | Effect: drop
- Hemlock: "Sometimes a show just didn't cover room and board."

### watching_the_kids.c.toml

**watching_the_kids**
- Refresh: 1y
- Requires: hemlock, hemlock_zone = dell_zone, hemlock_zone = luc_zone, hemlock_zone = maple_zone
- Source: NAR-601
- Portrait: wink
- Hemlock: "These kids sure do a great job of keeping Mistria safe... from getting too boring."

### week_one_drink.c.toml

**week_one_drink**
- Priority: max
- Refresh: never
- Requires: hemlock, location = inn, day_time <= 5:00pm, date_time < 14d
- Portrait: neutral
- Hemlock: "Stop by for a drink some evening, won't you?"
- Portrait: think
- Hemlock: "Our selection is more limited than it used to be..."
- Portrait: neutral
- Hemlock: "But scarcity breeds ingenuity!"

### week_one_pt_1.c.toml

**week_one_pt_1**
- Priority: max
- Refresh: never
- Requires: hemlock, date_time < 14d
- Source: NAR-1349
- Portrait: neutral
- Hemlock: "How do you like town so far, [Ari]?"
- Portrait: think
- Hemlock: "I know it could do with some repairs and a fresh coat of paint or two..."
- Portrait: neutral
- Hemlock: "But I think you'll find it's a nice place to live!"

### week_one_pt_2.c.toml

**week_one_pt_2**
- Priority: max
- Refresh: never
- Requires: hemlock, date_time < 14d
- Source: NAR-626
- Portrait: think
- Hemlock: "Now that you've moved in, it's only a matter of time before my oldest will have you taste testing her dishes."
- Portrait: happy
- Hemlock: "Reina gets everyone eventually!"

### welcome.c.toml

**welcome**
- Refresh: 1y
- Requires: hemlock, location = inn
- Portrait: neutral
- Hemlock: "Welcome to the Sleeping Dragon Inn. Kick your feet up a while!"

### welcome_in_from_rain.c.toml

**welcome_in_from_rain**
- Refresh: 1y
- Requires: hemlock, location = inn, weather = rainy, hemlock_was_last_spoken_to > 12h ago
- Source: NAR-1353
- Hemlock: "Welcome to the Sleeping Dragon Inn! Forget about the rain and warm up with food and friends."

### welcome_to_inn.c.toml

**welcome_to_inn**
- Refresh: 1y
- Requires: hemlock, location = inn
- Portrait: happy
- Hemlock: "Welcome to the Sleeping Dragon Inn! Best inn in Mistria."
- Portrait: wink
- Hemlock: "Might be biased, though."

### winter_work.c.toml

**winter_work**
- Refresh: 3m
- Requires: hemlock, location = inn, season = winter
- Portrait: wink
- Hemlock: "The Inn's a little cozier in winter, isn't it? Funny how that works."

### worked_up_an_appetite.c.toml

**worked_up_an_appetite**
- Refresh: 1y
- Requires: hemlock, hemlock_is_traveling_from = narrows/supervisor_2 OR narrows/supervisor_1
- Source: NAR-604
- Hemlock: "Whew! Worked up an appetite trying to keep up with the kids."

### working_at_inn.c.toml

**working_at_inn**
- Refresh: 1y
- Requires: hemlock, location = inn
- Source: NAR-596
- Portrait: happy
- Hemlock: "Take a load off! The drinks are cold and the cooking is unbelievable!"

### you_get_it.c.toml

**you_get_it**
- Refresh: 1y
- Requires: hemlock, hemlock_heart_level >= 8
- Portrait: happy | Effect: hearts
- Hemlock: "You get it, right? How special it is to come to Mistria from afar and make it your home."

### you_hungry.c.toml

**you_hungry**
- Refresh: 1y
- Requires: hemlock, location = inn, hemlock_routine = inn_solo_hemlock OR hemlock_activity = attend_register OR hemlock_routine = inn_table_service
- Hemlock: "You hungry? Let me know if we can whip something up for you!"

### you_thirsty.c.toml

**you_thirsty**
- Refresh: 1y
- Requires: hemlock, location = inn, hemlock_routine = inn_solo_hemlock OR hemlock_activity = attend_register OR hemlock_routine = inn_bar_service
- Hemlock: "All that running around must have worked up a thirst. Let me know if I can get you anything!"

---

## Market Lines

Source: `source/t2/Conversations/Bank/Hemlock/Market Lines/`

### market_darcy_1.c.toml

**market_darcy_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_darcy_stall
- Source: NAR-605
- Hemlock: "I like =Coffee= well enough, but I wonder if Darcy's got a dark =Beer= back there..."

### market_darcy_2.c.toml

**market_darcy_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_darcy_stall
- Source: NAR-1354
- Hemlock: "Josie loves tea, but I somehow never got a taste for it. =Coffee=, however... I do like a bit in the evening, from time to time."

### market_darcy_3.c.toml

**market_darcy_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_darcy_stall
- Source: NAR-1355
- Hemlock: "I think I'm a medium roast guy... I'm medium about most things."

### market_darcy_4.c.toml

**market_darcy_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_darcy_stall
- Source: NAR-606
- Hemlock: "Milk, no milk... I like =Coffee= either way."

### market_louis_1.c.toml

**market_louis_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_louis_stall
- Source: NAR-610
- Portrait: neutral
- Hemlock: "Jo's a knockout, and Louis' outfits are the sucker punch!"

### market_louis_2.c.toml

**market_louis_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_louis_stall
- Source: NAR-611
- Portrait: neutral
- Hemlock: "Louis could sell me a vest, sight unseen. They're always a hit with me."

### market_louis_3.c.toml

**market_louis_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_louis_stall
- Source: NAR-613
- Portrait: neutral
- Hemlock: "Louis really gets the difference between trend and style."

### market_louis_4.c.toml

**market_louis_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_louis_stall
- Source: NAR-612
- Portrait: neutral
- Hemlock: "You ever shop for clothes with Reina? Might be fun for the two of you."

### market_merri_1.c.toml

**market_merri_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_merri_stall
- Source: NAR-1356
- Hemlock: "I'd rather stand than sit, so I didn't really get why Jo was so crazy about the armchairs we got from Merri... but my baby is right. That's a comfortable chair."

### market_merri_2.c.toml

**market_merri_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_merri_stall
- Source: NAR-1357
- Hemlock: "Merri says she's got an ottoman that looks like a beetle... I've gotta show Luc."

### market_merri_3.c.toml

**market_merri_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_merri_stall
- Source: NAR-614
- Hemlock: "Jo asked me to set a furniture allowance after she went on a buying spree at Merri's a while back... I don't really have the heart to enforce it, though."

### market_merri_4.c.toml

**market_merri_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_merri_stall
- Source: NAR-1358
- Hemlock: "Maple wants furniture that screams princess... I'm keeping my eyes peeled."

### market_stillwell_1.c.toml

**market_stillwell_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_stillwell_stall
- Source: NAR-615
- Hemlock: "Can you help me make heads or tails of this money fortune? \"All that glitters is not gold, unless the glitter leaps from gold.\" Stillwell should come with a manual, if I'm being honest."

### market_stillwell_2.c.toml

**market_stillwell_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_stillwell_stall, reina_is_partner = false, reina_is_ex = false
- Source: NAR-616
- Hemlock: "I'll leave the love fortunes for Reina... what better fortune could I have than marrying my sweetheart Josie?"

### market_stillwell_3.c.toml

**market_stillwell_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_stillwell_stall
- Source: NAR-1346
- Hemlock: "I try to tell Luc not to ask for fortunes for all his little bug friends... it upsets Stillwell. He must be a bug fan, too."

### market_stillwell_4.c.toml

**market_stillwell_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_stillwell_stall
- Source: NAR-617
- Hemlock: "In Stillwell's words, \"the creaking of the wheel is the voice of reason\". In my words, \"I want my money back.\""

### market_taliferro.c.toml

**market_taliferro_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_taliferro_stall
- Portrait: neutral
- Hemlock: "That Taliferro has a pretty impressive coiffe, doesn't he?"
- Portrait: think
- Hemlock: "I should ask him what kind of pomade he uses..."

**market_taliferro_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_taliferro_stall
- Portrait: neutral
- Hemlock: "Taliferro talks big when he's running his $Cooking Challenge$..."
- Portrait: wink
- Hemlock: "But there's no way he could deal with a regular working kitchen... he'd crack in a heartbeat!"

**market_taliferro_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_taliferro_stall
- Portrait: think
- Hemlock: "You can't go hiring someone like Taliferro for your average kitchen."
- Portrait: happy | Effect: drop
- Hemlock: "His cooking skills are top-notch, but his personality? No, that's the kind of fella who needs a restaurant with his name on the sign."

**market_taliferro_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_taliferro_stall
- Portrait: happy
- Hemlock: "I'm proud of Reina for having her cooking recognized by a fancy chef like Taliferro..."
- Portrait: wink
- Hemlock: "But one day she'll be the one giving out the recognition. Mark my words!"

### market_vera_1.c.toml

**market_vera_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_vera_stall
- Source: NAR-1066
- Portrait: ugh
- Hemlock: "Maple's been going on about dyeing her hair pink. Kids ought to express themselves, but I don't know..."

### market_vera_2.c.toml

**market_vera_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_vera_stall
- Source: NAR-1063
- Portrait: neutral
- Hemlock: "Vera and Josie are longtime friends, and they love an excuse to catch up. A haircut's as good a reason as any!"

### market_vera_3.c.toml

**market_vera_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_vera_stall
- Source: NAR-622
- Portrait: neutral
- Hemlock: "Josie said she's thinking about dyeing her hair purple... I bet she'd look great."

### market_vera_4.c.toml

**market_vera_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_vera_stall
- Source: NAR-621
- Portrait: neutral
- Hemlock: "My hair was purple for a while, back when I toured with the band... might be fun to dye it again, take a little trip down memory lane."

### market_wheedle_1.c.toml

**market_wheedle_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_wheedle_stall
- Portrait: think
- Hemlock: "Surprised that Nora let Wheedle set up at the Saturday Market."
- Portrait: neutral
- Hemlock: "Last I heard, he had his business license revoked for selling the Royal Guard an expensive box of =White Wine=."
- Portrait: wink
- Hemlock: "It was a fine vintage... if you like vinegar."

### market_wheedle_2.c.toml

**market_wheedle_2**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_wheedle_stall
- Portrait: think
- Hemlock: "Whenever I see Wheedle, I always remember another one of his old business ventures..."
- Portrait: ugh
- Hemlock: "There was the time he opened a stall in the Capital that sold only tomatoes."
- Portrait: neutral
- Hemlock: "He called them Dragon Tomatoes, because these tomatoes were scaly like a dragon..."
- Portrait: wink
- Hemlock: "At least until the grand opening got rained on. All that green paint washed right into the gutter, along with Wheedle's credibility."

### market_wheedle_3.c.toml

**market_wheedle_3**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_wheedle_stall
- Portrait: think
- Hemlock: "I told myself I wouldn't buy anything from Wheedle, but I think Josie might like that $Snow Globe$..."

### market_wheedle_4.c.toml

**market_wheedle_4**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_wheedle_stall
- Portrait: neutral
- Hemlock: "I feel like I met Wheedle a dozen times over while touring with the old band, but every time he was going by a different name."
- Portrait: think
- Hemlock: "It's hard to forget a guy in a shiny three-piece suit going by the name 'Greedle.'"

### market_zorel_1.c.toml

**market_zorel_1**
- Priority: max | Refresh: 1y
- Requires: hemlock, hemlock_activity = visit_zorel_stall
- Portrait: happy
- Hemlock: "Make sure you say hello to Zorel, [Ari]! She's an old family friend."
- Portrait: neutral
- Hemlock: "Me and her Dad go way back. That man played the meanest saxophone you ever heard."

---

## Museum Lines

Source: `source/t2/Conversations/Bank/Hemlock/Museum Lines/`

### ancient_crystal_goblet.c.toml

**ancient_crystal_goblet**
- Refresh: 1y
- Requires: hemlock, museum_donated_ancient_crystal_goblet = true, building != museum
- Hemlock: "Errol tells me that $Ancient Crystal Goblet$ at the Museum is a very rare find, and probably was used in rituals."
- Portrait: think
- Hemlock: "Between you and me though... I'd love to drink a beer out of it."

### clay_amphora.c.toml

**clay_amphora**
- Refresh: 1y
- Requires: hemlock, museum_donated_clay_amphora = true, building != museum
- Portrait: think
- Hemlock: "That $Clay Amphora$ at the Museum is something else, huh?"
- Portrait: neutral
- Hemlock: "Just think of what kind of wine used to be in it!"

### mine_cricket.c.toml

**mine_cricket**
- Refresh: 1y
- Requires: hemlock, museum_donated_mine_cricket = true, building != museum
- Hemlock: "I was over at the Museum and saw that $Mine Cricket$! I bet it plays a pretty little tune. The acoustics down there must be killer."

### mist_flute.c.toml

**mist_flute**
- Refresh: 1y
- Requires: hemlock, museum_donated_mist_flute = true, building != museum
- Portrait: think
- Hemlock: "That $Mist Flute$ that got added to the Museum's collection... it lets out a little tune every so often."
- Portrait: wink
- Hemlock: "It might be fun to lug my lute out there and play a little duet."

### ritual_chalice.c.toml

**ritual_chalice**
- Refresh: 1y
- Requires: hemlock, museum_donated_ritual_chalice = true, building != museum
- Portrait: think
- Hemlock: "Eiland thinks the $Ritual Chalice$ at the Museum probably only held water..."
- Portrait: wink
- Hemlock: "But as a bartender, that just doesn't sound right to me!"

### tin_lunchbox.c.toml

**tin_lunchbox**
- Refresh: 1y
- Requires: hemlock, museum_donated_tin_lunchbox = true, building != museum
- Hemlock: "Holt and I saw that $Tin Lunchbox$ at the Museum and started making bets on who would eat whatever was inside."
- Portrait: sad
- Hemlock: "We were so disappointed when Errol said it was empty!"

---

## Gift Lines

Source: `source/t2/Conversations/Bank/Hemlock/Gift Lines/gift_lines.c.toml`

### Specific Gift Reactions

**crayfish_etouffee** (loved, specific)
- Refresh: 2w
- Requires: hemlock, gift_desire = loved, gift_given = crayfish_etouffee
- Portrait: happy | Effect: hearts
- Hemlock: "You got me =Etouffee=? Josie and I love this, it's one of our favorites! Can't wait to share it with her. Thanks, [Ari]."

**newt** (hated, specific)
- Requires: hemlock, gift_desire = hated, gift_given = newt
- Portrait: sad | Effect: sick
- Hemlock: "Come on now, not even Dell hands out newts as gifts."

### General Gift Reactions

**loved_gift**
- Requires: hemlock, gift_desire = loved
- Portrait: happy
- Hemlock: "This is mighty thoughtful of you, [Ari]. Thanks, I'm going to enjoy it."

**loved_gift_2**
- Requires: hemlock, gift_desire = loved
- Portrait: happy | Effect: sparkles
- Hemlock: "Would you look at that! I was just daydreaming about this. Thanks, [Ari]!"

**loved_gift_drinks**
- Refresh: 1w
- Requires: hemlock, gift_desire = loved, gift_given = beer OR hot_toddy OR white_wine
- Portrait: happy | Effect: sparkles
- Hemlock: "You know me so well! I'll make time to properly toast you with Josie later."

**loved_gift_edible**
- Refresh: 1w
- Requires: hemlock, gift_desire = loved, gift_given = chili_coconut_curry OR crayfish_etouffee OR crispy_fried_earthshroom OR incredibly_hot_pot OR spicy_corn OR wild_grapes
- Portrait: wink | Effect: sparkles
- Hemlock: "Hot dang, that smells amazing! This is something worth changing your dinner plans for, eh?"

**liked_gift**
- Requires: hemlock, gift_desire = liked
- Portrait: happy
- Hemlock: "This is for me? I gotta show Josie!"

**liked_gift_edible**
- Refresh: 1w
- Requires: hemlock, gift_desire = liked, gift_given = basil OR chili_pepper OR coffee OR crunchy_chickpeas OR dried_squid OR grape_juice OR honey OR lemon OR roasted_chestnuts OR rock_salt OR sesame_broccoli OR spicy_cheddar_biscuit OR spicy_crab_sushi OR spicy_water_chestnuts OR summer_salad OR tea OR thyme OR toasted_sunflower_seeds OR trail_mix OR water_chestnut_fritters
- Portrait: wink
- Hemlock: "Looks delicious! Thanks, [Ari]."

**neutral_gift**
- Requires: hemlock, gift_desire = neutral
- Portrait: neutral
- Hemlock: "Hey, thanks."

**disliked_gift**
- Requires: hemlock, gift_desire = disliked
- Portrait: ugh
- Hemlock: "You sure this is for me? Well, if you say so..."

**birthday_gift**
- Priority: max
- Requires: hemlock, gift_desire = neutral OR liked OR loved, hemlock_birthday after 24h
- Portrait: neutral
- Hemlock: "Oh, you got me something for my birthday? I can't wait to show Josie!"
- Portrait: happy | Effect: sparkles
- Hemlock: "Thanks, [Ari]!"

---

## Festival Lines

Source: `source/t2/Conversations/Festival Lines/Hemlock/`

### animal_festival.c.toml

**animal_festival_0**
- Priority: max | Refresh: 3m
- Requires: hemlock, animal_festival_today = true, location = town, time_of_day != night
- Portrait: neutral
- Hemlock: "Even with all my years of bartending, I can't figure out why the =Chicky Hot Chocolate= tastes extra good!"
- Portrait: think
- Hemlock: "Maybe I'd better have another... for science..."

### harvest_festival.c.toml

**harvest_festival_0**
- Priority: max | Refresh: 3m
- Requires: hemlock, harvest_festival_date after 1d, location = town, time_of_day != night
- Portrait: neutral
- Hemlock: "It's great that we have so much help in the kitchen this year!"
- Portrait: wink
- Hemlock: "That'll make it easier for me to steal Josie away for a dance or two!"

### shooting_star.c.toml

**shooting_star_anticipation**
- Refresh: 3m
- Requires: hemlock, shooting_star_festival_date before 3d, quest_repair_the_summit_stairs_complete = true
- Portrait: neutral
- Hemlock: "The Shooting Star Festival is one of my favorites. Jo and I used to watch it every year together, before we got married..."
- Portrait: happy
- Hemlock: "And now we get to watch those same stars with the family we've built together. Warms my heart."

**shooting_star_anticipation_no_summit**
- Refresh: 3m
- Requires: hemlock, shooting_star_festival_date before 3d, quest_repair_the_summit_stairs_complete = false
- Portrait: neutral
- Hemlock: "The Shooting Star Festival is one of my favorites. Jo and I used to watch it at the Summit every year together, before we got married..."
- Portrait: think
- Hemlock: "It's a little sad the young folks won't be able to do the same this year, $with the Summit inaccessible$..."

**shooting_star_day_of**
- Priority: max | Refresh: 3m
- Requires: hemlock, shooting_star_festival_date after 1d, day_time < 8:00pm, hemlock not at town/star_festival_hemlock
- Portrait: neutral
- Hemlock: "Hey, [Ari], looking forward to watching the stars tonight?"

**shooting_star_balor_follow_up_hemlock**
- Priority: max | Refresh: 3m
- Requires: hemlock, shooting_star_date_status = balor_went, shooting_star_festival_date after 7d, balor_is_spouse = false
- Portrait: think
- Hemlock: "Balor doesn't like to talk about his past much, but he's mentioned that he had to fend for himself a lot growing up."
- Portrait: neutral
- Hemlock: "Traveling merchants tend to be drifters, but I think Balor genuinely cares about making sure people have what they need to get by."

**shooting_star_reina_follow_up_hemlock**
- Priority: max | Refresh: 3m
- Requires: hemlock, shooting_star_date_status = reina_went, shooting_star_festival_date after 2d, reina_is_partner = false
- Portrait: neutral
- Hemlock: "Well well, look who it is!"
- Portrait: wink
- Hemlock: "Reina asked me not to tease, so I won't..."
- Portrait: neutral
- Hemlock: "But next time you two decide to make tea at midnight, don't forget to put your cups in the sink after."

### spring_festival.c.toml

**tune**
- Priority: max | Refresh: 3m
- Requires: hemlock, spring_festival_date after 1d
- Portrait: neutral
- Hemlock: "Like the tune, [Ari]? It's been a Mistria festival staple for ages, Jo taught it to me!"
- Portrait: wink
- Hemlock: "She says that when I play it the song really swings!"

---

## Source Absences

- No heart event / thread conversation files found in the Bank directory (heart events may exist elsewhere in the source tree)
- No group conversation files extracted (those would be in `source/t2/Conversations/Group Conversations/` directories involving Hemlock)
- The birthday_gift entry in gift_lines.c.toml contains an empty requirement object `{ }` in the requires array, which may be a data artifact
- The Footsie.c.toml filename does not match the Trellis conversion comment pattern used in most other files (comment says "10. Footsie" suggesting a numbered sequence)
- The `[perfomance]` key in performance.c.toml contains a typo (missing "r")
