---
type: reference
title: Maple — Conversations
description: 'Extracted dialogue from Maple''s banked conversation lines, market lines,
  museum lines, gift lines, and festival lines. Speaker attribution, trigger conditions,
  expression tags, and branching paths preserved.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Maple/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Maple/Market Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Maple/Museum Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Maple/Gift Lines/
- projects/fields-of-mistria/source/t2/Conversations/Festival Lines/Maple/
---

# Maple — Conversations

Source: `source/t2/Conversations/` — banked lines, market stall lines, museum lines, gift reactions, and festival lines.

---

## Banked Lines

Source: `Bank/Maple/Banked Lines/` (37 files)

### greeting_ari.c.toml

Source: NAR-841. Priority: max. Refresh: never. Requires: maple_has_met = false.

- "Hi! Are you the new farmer? My name's Maple!" > [happy] "Where did you live before you came here? Have you ever been to the Capital?" > [wink, sparkles] "That's where the royal family lives, you know!" > "You can ask me anything, I know aaaaaall about them."

### week_one_pt_1.c.toml

Source: NAR-1222. Priority: max. Refresh: never. Requires: date_time < 14d.

- [happy] "Lady Maple welcomes you to Mistria, and accepts tribute in the form of cash or snacks." > [wink] "Okay you got me, I'm not LADY Maple... yet. But I'll still accept any tribute in the form of snacks."

### have_you_tried_reinas_food.c.toml

Source: NAR-795. Refresh: never. Requires: date_time < 14d.

- [happy] "Have you had the food my sister Reina makes yet? It's really yummy!"

### hear_ye.c.toml

Refresh: 1y. Requires: time_of_day = morning. Writes: queen_maple = true (expires 18h).

- [mad] "Hear ye hear ye! On this morning you are in the presence of Queen Maple!" > [wink, sparkles] "That's me."

### goodnight_commoner.c.toml

Refresh: 1y. Requires: queen_maple = true, time_of_day = night or evening, traveling to maples_room.

- "Good night, [Ari]! I, Queen Maple, take my leave of you." > [happy] "Many thanks for teaching me about the life of a commoner such as yourself."

### royal_domain.c.toml

Refresh: 1y. Requires: queen_maple = true.

- [happy] "[Ari]! Accompany me as we approach my royal domain! All looks to be in order... most pleasing..."

### royal_brunch.c.toml

Refresh: 1y. Requires: time_of_day = morning.

- [happy] "I dreamt Lady Adeline invited me to a royal brunch."

### royal_dinner.c.toml

Refresh: 1y. Requires: day_time >= 4pm, traveling to inn/general_store_home/maples_room, not Friday.

- [happy] "Royal dinner... and then a royal sleep... that's what Queen Maple wants..."

### inn_dinner.c.toml

Refresh: 1y. Requires: location = inn, maple_activity = eat.

- "Did you know royalty eats with ten different kinds of spoons and twenty kinds of forks?" > [mad] "That's too many. When I become queen, I'm outlawing all that!"

### poison.c.toml

Refresh: 1y. Requires: queen_maple = true, maple_activity = eat.

- [sad] "We must always check our dinner for poison. Such is the life of a royal!"

### cleaning.c.toml

Refresh: 1y. Requires: maple_routine = inn_kids.

- "I don't mind cleaning. A good Royal should have a keen understanding of the jobs of her subjects."

### register_1.c.toml

Refresh: 1y. Requires: location = inn, maple_is_at = inn/Inn Register.

- "Hungry? Great! I accept payment in tesserae, or candy."

### register_2.c.toml

Refresh: 1y. Requires: location = inn, maple_is_at = inn/Inn Register.

- "Hi, [Ari]! I'll take today's special, and a glass of orange juice!" > [think] "Oh, I'm supposed to serve you? That's not very royal..."

### register_3.c.toml

Refresh: 1y. Requires: location = inn, maple_is_at = inn/Inn Register.

- "[Ari]! I bid you a very royal welcome to my domain!"

### being_read_to_about_royalty.c.toml

Source: NAR-806. Refresh: 1y. Requires: maple_zone = <adeline_zone>.

- [think] "Being a noble sounds rough. They should just put me in charge, I could handle it for them."

### old_diets.c.toml

Refresh: 1y. Requires: maple_zone = <errol_zone>.

- [think] "Mr. Errol told me how royalty ate in olden times. He sure knows a lot."

### dell_says_adeline_knighted.c.toml

Source: NAR-794. Refresh: 1y. Requires: maple_zone = <dell_zone>.

- [think] "Dell says Lady Adeline knighted you, [Ari]. But I thought only a king could do that..."

### sleeping_dragon_palace.c.toml

Refresh: 1y. Requires: location = celines_room, maple_zone = <celine_zone>.

- [happy] "Miss Celine's cottage is so cute. One day I'll have a house too. But mine will be more fancy, like Lady Adeline's house." > [neutral, sparkles] "I'll call it the Sleeping Dragon PALACE. I can't wait!"

### shopping_list_maple.c.toml

Refresh: 1y. Requires: maple not at same location as Balor, maple_has_a_list = true. Writes: maple_has_a_list = false.

- "[Ari], have you seen Balor? I have to find him before he goes to the Capital." > [happy, sparkles] "I have a very important list for him."

### luc_teaching_about_bees.c.toml

Source: NAR-796. Refresh: 1y. Requires: maple_zone = <luc_zone>.

- [ugh] "Luc's teaching me about bees! I just wanna hear about the Queens though."

### bugologist.c.toml

Refresh: 1y. Requires: maple_zone = <luc_zone>.

- [happy, cheery] "When we grow up, Luc is going to be a super famous bug guy! A bugologist! I just know it!"

### scared_of_bugs.c.toml

Refresh: 1y. Requires: maple_zone = <luc_zone>.

- [think] "I used to be scared of bugs, but it's hard to stay that way when you have Luc for a brother!" > [neutral] "Now I think they're kind of cute. For bugs anyway."

### queen_bee.c.toml

Refresh: 1y. Requires: luc_zone = <maple_zone>, queen_bee = true.

- [think] "The queen bee should get a little crown, don't you think?"

### luc_cant_bring_bugs.c.toml

Source: NAR-802. Refresh: 1y. Requires: maple_is_traveling = true, day_time >= 4pm and <= 9pm.

- [ugh] "Luc better not bring his bugs to dinner again..."

### mom_and_dad_love_each_other.c.toml

Source: NAR-803. Refresh: 1y. Requires: josephine_zone = <hemlock_zone>, maple_zone = <josephine_zone>.

- "Mama and Daddy sure do love each other. I know I'm supposed to be grossed out, but it just makes me happy."

### bedtime_story_reaction.c.toml

Refresh: 1y. Requires: maple_is_at = maples_room/Maple Wake Point, josephine_is_at_location = maples_room.

- Speaker: maple. [happy] "Between you and me, [Ari], momma's really good at telling stories."

### travel_to_bed.c.toml

Source: NAR-797. Refresh: 1y. Requires: location = maples_room, day_time >= 7pm.

- "Time for bed! Royalty needs their beauty sleep."

### bed.c.toml

Priority: max. Refresh: 1w. Requires: time_of_day = night, maple_is_at = maples_room/Maple Wake Point.

- [happy] "Night night, [Ari]!"
- (alternate) [neutral] "It's bedtime for Maple, [Ari]... I'm so sleepy!"

### travel_to_juniper.c.toml

Source: NAR-799. Refresh: 1y. Requires: maple_zone = <juniper_zone>.

- [happy] "We have questions about potions, and Juniper's the potion expert! PLUS she's got a big fluffy dog!"

### juniper_laugh.c.toml

Refresh: 1y. Requires: maple_zone = <juniper_zone>.

- [think] "Miss Juniper sure does have a loud laugh, huh."

### Swingset.c.toml

Source: NAR-801. Refresh: 1y. Requires: swing_play = true.

- "I want to play on the swing..."

### dells_going_in_fountain.c.toml

Source: NAR-809. Refresh: 1y. Requires: fountain_play = true, maple_zone = <dell_zone>, dell at fountain zone.

- "Dell says she'll be good and won't jump in the fountain... yeah right!"

### basement.c.toml

Priority: basement. Refresh: instantly. Requires: npc = maple.

- [happy] "Yay, it's [Ari]!"

### rain_confusion.c.toml

Source: NAR-805. Refresh: 1y. Requires: weather = rainy, is_inside = false.

- "I don't really get what's going on anymore but the rain sure is pretty!"

### rainy_days_are_sleepy.c.toml

Refresh: 1y. Requires: weather = rainy.

- [sad] "Rainy days are kind of sleepy... yawn..."

### fnati_anticipation.c.toml

Refresh: 1y. Requires: day_of_the_week = friday.

- "Friday night always reminds me that adults need to play, too. Good for them!"

### market_anticipation.c.toml

Refresh: 1y. Requires: day_of_the_week = friday, market_is_back = true.

- [happy] "Tomorrow's the Saturday Market! Maybe I'll see Lady Adeline around!"

---

## Market Lines

Source: `Bank/Maple/Market Lines/` (26 files)

### market_darcy_1.c.toml

Source: NAR-807. Priority: max. Refresh: 1y. Requires: maple_activity = visit_darcy_stall.

- "If Dell asks you to buy her coffee, do NOT. I saw what happened last time... and no, you do NOT want to know."

### market_darcy_2.c.toml

Source: NAR-808. Priority: max. Refresh: 1y. Requires: maple_activity = visit_darcy_stall.

- "Darcy makes the BEST =Hot Chocolate=! She drew me a crown in the foam this time!"

### market_darcy_3.c.toml

Source: NAR-810. Priority: max. Refresh: 1y. Requires: maple_activity = visit_darcy_stall.

- "Darcy's been making rose hot chocolate recently... it tastes so fancy, I feel like a princess."

### market_darcy_4.c.toml

Source: NAR-811. Priority: max. Refresh: 1y. Requires: maple_activity = visit_darcy_stall.

- "I could have =Hot Chocolate= every day of the year... yum!"

### market_louis_1.c.toml

Source: NAR-816. Priority: max. Refresh: 1y. Requires: maple_activity = visit_louis_stall.

- [neutral] "I only want to see the most princessy clothes that Mister Louis has!"

### market_louis_2.c.toml

Source: NAR-817. Priority: max. Refresh: 1y. Requires: maple_activity = visit_louis_stall.

- [think] "Lady Adeline bought that dress over there... do you think Mister Louis will make it in my size?"

### market_louis_3.c.toml

Source: NAR-820. Priority: max. Refresh: 1y. Requires: maple_activity = visit_louis_stall.

- [happy] "I like to look fancy... REALLY fancy... Mister Louis understands."

### market_louis_4.c.toml

Source: NAR-818. Priority: max. Refresh: 1y. Requires: maple_activity = visit_louis_stall.

- [mad] "I keep telling Mister Louis, more bows, MORE ribbons! I demand it! Not just for me... for everyone!"

### market_merri_1.c.toml

Source: NAR-819. Priority: max. Refresh: 1y. Requires: maple_activity = visit_merri_stall.

- "I hope I hope I HOPE that Miss Merri has some princessy furniture! Pleaaaase!"

### market_merri_2.c.toml

Source: NAR-821. Priority: max. Refresh: 1y. Requires: maple_activity = visit_merri_stall.

- "I want the PERFECT bed... it should have tall posts, and a big canopy, and the inside should look like stars! And... and... and...!"

### market_merri_3.c.toml

Source: NAR-822. Priority: max. Refresh: 1y. Requires: maple_activity = visit_merri_stall.

- "Ma loves all of Miss Merri's furniture... sometimes we end up with furniture before there's a room to put it in."

### market_merri_4.c.toml

Source: NAR-823. Priority: max. Refresh: 1y. Requires: maple_activity = visit_merri_stall.

- "Miss Merri's always getting help from Mister Hayden and Mister Olric... she knows how to delegate. I admire that."

### market_stillwell_1.c.toml

Source: NAR-824. Priority: max. Refresh: 1y. Requires: maple_activity = visit_stillwell_stall.

- "I asked Mister Stillwell whether it's my destiny to be a princess and he started mumbling about the signs in the stars... what do the stars have to do with it?"

### market_stillwell_2.c.toml

Source: NAR-825. Priority: max. Refresh: 1y. Requires: maple_activity = visit_stillwell_stall.

- "Is Mister Stillwell okay? I mean in general..."

### market_stillwell_3.c.toml

Source: NAR-826. Priority: max. Refresh: 1y. Requires: maple_activity = visit_stillwell_stall.

- "When I become a princess, Mister Stillwell is going to be my royal fortune-teller... and also my royal wailer. He's really good at wailing..."

### market_stillwell_4.c.toml

Source: NAR-827. Priority: max. Refresh: 1y. Requires: maple_activity = visit_stillwell_stall.

- "You know, I think Mister Stillwell likes darkness... if he likes it so much, he should marry it."

### market_taliferro.c.toml

Priority: max. Refresh: 1y. Requires: maple_activity = visit_taliferro_stall. Contains four conversations:

**market_taliferro_1:**
- [neutral] "Mister Taliferro's teeth sure are shiny." > [think] "I bet his mom washed his mouth out with soap." > [happy] "A lot."

**market_taliferro_2:**
- [think] "If Mister Taliferro is such a good cook, why is he asking everyone to cook for him?" > [mad] "When do I get to judge HIS cooking?"

**market_taliferro_3:**
- [neutral] "When I'm queen, Reina will be my royal chef, obviously." > [happy] "But I'll make Mister Taliferro HER royal chef, and he'll have to wait on her all day long!"

**market_taliferro_4:**
- [think] "Why do you think Mister Taliferro is so mean?" > [sad] "Maybe when he was little, a $Cooking Challenge$ bullied him and called him names..."

### market_vera_1.c.toml

Source: NAR-1117. Priority: max. Refresh: 1y. Requires: maple_activity = visit_vera_stall.

- [happy] "Lady Adeline and I are going to get our hair done together someday... she promised! Yay!"

### market_vera_2.c.toml

Source: NAR-833. Priority: max. Refresh: 1y. Requires: maple_activity = visit_vera_stall.

- [think] "I want to try dyeing my hair too! How about.... pink!"

### market_vera_3.c.toml

Source: NAR-832. Priority: max. Refresh: 1y. Requires: maple_activity = visit_vera_stall.

- [neutral] "What color is the most royal color for hair? Mom says it's mine!"

### market_vera_4.c.toml

Source: NAR-831. Priority: max. Refresh: 1y. Requires: maple_activity = visit_vera_stall.

- [think] "What color would a queen dye her hair? No really, I need to know."

### market_wheedle_1.c.toml

Priority: max. Refresh: 1y. Requires: maple_activity = visit_wheedle_stall.

- [neutral] "When I'm Queen of all Aldaria, I'll make Mister Wheedle my deceitful minister." > [happy] "Every queen needs at least one advisor who she suspects will betray her... it makes things interesting!"

### market_wheedle_2.c.toml

Priority: max. Refresh: 1y. Requires: maple_activity = visit_wheedle_stall.

- [think] "I was looking at Mister Wheedle's suit and wondering... do you think the Dragonguard can arrest someone for fashion crimes?" > [mad] "I think we should."

### market_wheedle_3.c.toml

Priority: max. Refresh: 1y. Requires: maple_activity = visit_wheedle_stall.

- [neutral] "I didn't really believe in dungeons until I met Mister Wheedle." > [think] "He just seems like he belongs in there, you know?"

### market_wheedle_4.c.toml

Priority: max. Refresh: 1y. Requires: maple_activity = visit_wheedle_stall.

- [think] "Mister Wheedle said he doesn't sell his wares to little babies." > [mad] "How dare he speak to his future liege lord in such a tone!" > [neutral] "We'll see who the baby is when he's crying at the bottom of my oubliette!"

### market_zorel_1.c.toml

Priority: max. Refresh: 1y. Requires: maple_activity = visit_zorel_stall.

- [neutral] "I asked Zorel if she could get the Aldarian National Anthem on a $Song Crystal$." > [happy] "It'll make good background music next time I'm pretending I'm the Queen!"

---

## Museum Lines

Source: `Bank/Maple/Museum Lines/` (9 files)

### bell_berry.c.toml

Refresh: 1y. Requires: museum_donated_bell_berry = true, not in museum.

- [happy] "Did you donate that $Bell Berry$ at the Museum?" > [wink, music_notes] "It's cute when a thing looks like another thing, isn't it?"

### criminal_confession.c.toml

Source: NAR-194. Refresh: 1y. Requires: museum_donated_criminal_confession = true, not in museum.

- [think] "Mister Balor said that the $Criminal Confession$ in the Museum is HIS." > [sad, drop] "I don't believe him, though. He's too busy playing cards with Pa to write all that."

### crystal_wing_moth.c.toml

Refresh: 1y. Requires: museum_donated_crystal_wing_moth = true, not in museum.

- [neutral] "Luc was so excited to show me the $Crystal Wing Moth$ at the Museum! He said it looked just like a tiara!" > [happy, sparkles] "And he was right!"

### fossilized_mandrake_root.c.toml

Refresh: 1y. Requires: museum_donated_fossilized_mandrake_root = true, not in museum.

- [think] "That $Fossilized Mandrake Root$ sure is unsettling to look at." > [neutral] "I wonder what it was used for?" > [mad] "Scaring people, I bet!"

### hermit_snail.c.toml

Refresh: 1y. Requires: museum_donated_hermit_snail = true, not in museum.

- [think] "Y'know, [Ari], that $Hermit Snail$ at the Museum makes me think of Mister Balor." > [happy, cheery] "He also pulls his home around with him!"

### rainbow_geode.c.toml

Refresh: 1y. Requires: museum_donated_rainbow_geode = true, not in museum.

- [happy] "The $Rainbow Geode$ at the Museum is sooo pretty! And it changes colors depending on how you look at it!" > [mad] "Just like a royal advisor who can't be trusted."

### ritual_scepter.c.toml

Refresh: 1y. Requires: museum_donated_ritual_scepter = true, not in museum.

- [happy] "The $Ritual Scepter$ at the Museum is so fancy! It looks like it belonged to someone super royal!"

### sea_grapes.c.toml

Refresh: 1y. Requires: museum_donated_sea_grapes = true, not in museum.

- [think] "Reina says the $Sea Grapes$ at the Museum probably have a more salty taste, like the ocean." > [mad] "I like my grapes super sweet, thank you very much."

### stone_shell.c.toml

Refresh: 1y. Requires: museum_donated_stone_shell = true, not in museum.

- [think] "The =Stone Shell= at the Museum is so pretty! Did you know, in olden times queens would blow on a shell to call their armies down on their enemies?" > [happy, sparkles] "I have to get down to the beach soon..."

---

## Gift Lines

Source: `Bank/Maple/Gift Lines/gift_lines.c.toml`

### Specific Gift Reactions

**lost_crown_of_aldaria** (loved, refresh 2w):
- [neutral] "Oh my gosh! [Ari]! Thank you so so much!" > [happy, sparkles] "I finally have my own crown."

**berries_and_cream** (loved, refresh 2w):
- [happy, hearts] "I love =Berries and Cream=! It's a dessert fit for royalty!"

**peat** (hated):
- [mad, sparkles_dark] "$Peat$? $PEAT$? You insult Princess Maple! Begone, peasant!"

### General Gift Reactions

**loved_gift:**
- [happy] "It's so pretty! Thank you, I love it!" > [mad, hearts] "I mean, Princess Maple thanks you for your tribute."

**loved_gift_2:**
- [mad] "Princess Maple acknowledges your contribution to her royal treasury and graciously extends her most gracious gratitude!" > [happy, sparkles] "Thanks, [Ari]!"

**loved_gift_edible** (refresh 1w; triggers for: berries_and_cream, chocolate, hot_cocoa, lemon_pie, mont_blanc):
- [happy] "Princess Maple loves only the fanciest and most royal of desserts! [Ari]'s offering pleases her greatly."

**loved_gift_royal** (refresh 1w; triggers for: ancient_horn_circlet, lost_crown_of_aldaria, middlemist, monarch_butterfly):
- [happy] "Princess Maple's influence grows with the many symbols of her kingdom!" > [mad, sparkles] "She's gonna become, like... so powerful!"

**liked_gift:**
- [neutral] "BY ROYAL DECREE, I DECLARE... that Princess Maple is most pleased with your gift, [Ari]."

**liked_gift_2:**
- [neutral] "Princess Maple thanks you for your generosity, [Ari]."

**liked_gift_edible** (refresh 1w; triggers for: blackberry, cheese, glowberry_cookies, golden_cookies, grilled_cheese, ice_cream_sundae, jam_sandwich, pomegranate_sorbet, pudding, strawberry_shortcake, trail_mix, wildberry_pie, wintergreen_ice_cream):
- [neutral] "Princess Maple is always happy to accept a tasty treat!"

**liked_gift_royal** (refresh 1w; triggers for: blue_conch_shell, daisy, pink_scallop_shell, sand_dollar, spirula_shell):
- [happy] "Princess Maple appreciates your offering. She thinks it's really pretty!"

**neutral_gift:**
- [neutral] "BY ROYAL DECREE, I DECLARE... that this gift is okay!"

**disliked_gift:**
- [ugh] "BY ROYAL DECREE, I DECLARE... this to be kind of a whatever gift, [Ari]."

**birthday_gift** (priority max; requires gift_desire = neutral/liked/loved, maple_birthday after 24h):
- [happy, hearts] "You remembered my birthday! Thank you [Ari]! I feel like a queen!"

---

## Festival Lines

Source: `Conversations/Festival Lines/Maple/` (4 files)

### animal_festival.c.toml

**animal_festival_anticipation** (refresh 3m; requires: animal_festival_date within 3d):
- [happy] "Did you know that the Animal Festival will have a PETTING ZOO?" > [think] "I mean, I guess Mister Hayden lets us play with his animals when we visit his farm..." > [neutral] "But these will be new animals!"

**animal_festival_0** (priority max, refresh 3m; requires: animal_festival_today = true):
- [neutral] "I asked Adeline if the royal family has their own petting zoo, and she said she didn't think so." > [mad] "Another thing to add to my to-do list when I'm Queen!"

### harvest_festival.c.toml

**harvest_festival_anticipation** (refresh never; requires: harvest_festival_setup = true):
- [think] "$Queen Berries$, huh." > [neutral] "I bet they're important if you want to be the next Queen... I mean, it's right there in the name!"

**harvest_festival_0** (refresh 3m, priority max; requires: harvest_festival_date after 1d):
- [think] "I spent all my time gathering $Queen Berries$ so now I get a bigger slice of pie..." > [mad] "But I could have spent the last couple of days taste testing for Reina and gotten to eat all the pie I wanted!"

### shooting_star.c.toml

**shooting_star_reina_follow_up_maple** (priority max, refresh 3m; requires: shooting_star_date_status = reina_went, shooting_star_festival_date after 2d, reina_is_spouse = false):
- [neutral] "Did you know that there are all sorts of interesting political implications to consider when courting a queen's sister?"

### spring_festival.c.toml

**try_something** (priority max, refresh 3m; requires: spring_festival_date after 1d):
- [happy] "Try something, [Ari]! It's all reaaaaally good. I've taste tested all of it myself!"

---

## Source Absences

- No group conversation files found for Maple (other characters have files in `Group Conversations/`).
- No thread/heart event conversation files found for Maple (consistent with `dateable = false`).
- The `shooting_star.c.toml` file references a scenario where the player took Reina to the Shooting Star festival, implying Maple reacts to courtship of her sister, but no other Shooting Star lines exist for Maple.
- The `shopping_list_maple.c.toml` contains several empty requirement objects `{ }` — possibly placeholder or unused conditions in the source data.
