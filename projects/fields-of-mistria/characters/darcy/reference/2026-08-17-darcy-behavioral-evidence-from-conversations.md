---
type: reference
title: Darcy — Behavioral Evidence from Conversations
description: 'Extracted dialogue from Darcy''s banked lines and gift lines: market
  day greetings, vendor interactions, seasonal talk, packing-up reflections, gift
  reactions, gossip about others.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Darcy/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Darcy/Gift Lines/
---

# Darcy — Behavioral Evidence from Conversations

Source: `source/t2/Conversations/Bank/Darcy/`

## First Meeting

**greeting_ari** (priority: max, refresh: never, requires: darcy_has_met = false):
- Darcy: "Hello there! Welcome to $Darcy's Cafe$!"
- Darcy [wink]: "Yes... I'm Darcy."
- Darcy: "If you're ever in the mood for a nice cup of coffee or a sweet treat, be sure to stop by."
- Darcy [happy]: "Everything is made fresh!"

**Behavioral notes:** Warm, welcoming introduction. Leads with her business identity. The wink on "Yes... I'm Darcy" suggests playful self-awareness, as if the cafe's name already gave her away. Emphasizes freshness as a selling point.

## Greetings and Daily Talk — Saturday Market (Active)

All lines require: npc = darcy, day_of_the_week = saturday, darcy_is_at = "town/Darcy", darcy_routine != darcy_packing (i.e., stall is still open).

**ready_to_order** (refresh: 1y):
- Darcy [happy]: "I had a feeling you'd be stopping by today, [Ari]!"
- Darcy [neutral]: "Just let me know when you're ready to order."

**morning_coffee** (refresh: 1y, time_of_day = morning):
- Darcy [happy]: "I've got some hot coffee for your sleepy Saturday morning, [Ari]!"

**fresh_pot_of_coffee** (refresh: 1y):
- Darcy [neutral]: "Good timing, I've got a fresh pot of coffee brewing!"

**other_drinks** (refresh: 1y):
- Darcy: "I have a lot of drinks on offer, if coffee's not your thing. Check out my menu!"

**rotating** (refresh: 1y):
- Darcy: "If nothing on the menu catches your interest this week, come by next time you see me."
- Darcy [wink]: "I'm always rotating in new drinks."

**experimenting** (refresh: 1y, heart_level <= 0.2):
- Darcy: "I've been experimenting with some new drinks since the last time I was at the Saturday Market. Take a look at the new menu!"

**Behavioral notes:** Friendly and business-oriented. Addresses the player by name. Actively promotes her menu and encourages browsing. The experimenting line appears at low friendship, functioning as an early sales pitch.

## Coffee Craft and Philosophy

**aromatics** (refresh: 1y, Saturday, stall open):
- Darcy [wink]: "I do a fresh grind for every order! It really brings out the aromatics."

**new_roasting** (refresh: 1y, Saturday, stall open):
- Darcy [neutral]: "If your coffee tastes different, let me know, I'm trying a different roasting technique."
- Darcy [happy]: "I think you'll like it!"

**new_drink** (refresh: 1y, Saturday, stall open):
- Darcy [neutral]: "If you're wondering how I choose what goes on my menu, well..."
- Darcy [happy]: "It's what I want to drink that day!"

**tolerance** (refresh: 1y, Saturday, stall open, heart_level >= 0.4):
- Darcy [think]: "My caffeine tolerance is actually pretty low, [Ari]... I'm down to five shots of espresso."

**Behavioral notes:** Takes genuine pride in her craft — grinding fresh, experimenting with roasting techniques, rotating the menu. The tolerance line (unlocked at higher friendship) reveals dry humor and self-awareness: "down to five shots" delivered deadpan as if that is low. Menu choices are personal ("what I want to drink that day"), suggesting an artisan approach rather than purely commercial thinking.

## Capital and Mistria — Background

**mistria_great** (refresh: 1y, Saturday, stall open):
- Darcy [think]: "The Capital has a long tradition of coffee, but that also makes it a bit rigid."
- Darcy [happy, cheery]: "I'm glad I can experiment with new drinks here in Mistria! Now, where did I put that spice blend..."

**Behavioral notes:** Darcy moved from the Capital to Mistria. She values creative freedom over tradition. The Capital's coffee culture is established but constraining; Mistria gives her room to experiment. The trailing thought about the spice blend shows her as hands-on and a little scattered in an endearing way.

## Seasonal Lines — Summer

**heat** (refresh: 3m, Saturday, summer, stall open):
- Darcy [neutral]: "Don't let the heat stop you from ordering something hot, sweating cools you off too!"

**hot_year_round** (refresh: 3m, Saturday, summer, stall open):
- Darcy [think]: "I like to rotate my menu to keep up with the season, but there are some folks who like a hot drink any time of year."

**summer_packing_1** (refresh: 3m, Saturday, summer, packing):
- Darcy [neutral]: "It's such a relief when the weather cools off at the end of Market day."
- Darcy [happy]: "Packing up is so much easier!"

**Behavioral notes:** Pragmatic about the summer heat. Justifies hot drinks in warm weather with humor. Acknowledges seasonal preferences of customers while maintaining her own menu philosophy.

## Seasonal Lines — Fall

**fall_packing_1** (refresh: 3m, Saturday, fall, packing):
- Darcy [neutral]: "Folks love a hot drink in the fall, don't they!"
- Darcy [happy]: "It's nice thinking back on a long day and remembering all the smiles."

**Behavioral notes:** Reflective and sentimental. Fall is good for business (hot drinks) but she values the emotional reward — the smiles — as much as the sales.

## Seasonal Lines — Winter

**warm_up** (refresh: 3m, Saturday, winter, stall open):
- Darcy [neutral]: "Hey, [Ari]! I've got just the thing to warm you up."

**hot_drinks** (refresh: 3m, Saturday, winter, stall open):
- Darcy [happy]: "Sure is easy to sell hot drinks in this kind of weather."

**steamed_milk** (refresh: 3m, Saturday, winter, stall open):
- Darcy [think]: "I pay special attention to how I steam the milk in winter. A nice hot drink really helps you get through the day."
- Darcy [neutral]: "In fact, I could go for one right now!"

**hot_cup** (refresh: 3m, Saturday, winter, stall open, requires adeline_activity = visit_darcy_stall):
- Darcy [neutral]: "Adeline asked me if I had any special cup that could keep her coffee hot all day."
- Darcy [think]: "Maybe I should talk to March, could be a nice addition to the drinks business."

**winter_packing_1** (refresh: 1y, Saturday, winter, packing):
- Darcy [neutral]: "Oh, hi [Ari]! I'm just reviewing today's sales. You know, there's always one or two folks who want an iced drink, even when it's cold."
- Darcy [wink]: "Luckily I don't have to worry about the ice in the winter!"

**Behavioral notes:** Winter is her strongest season for sales. She adjusts her technique (steamed milk). The hot_cup line reveals she collaborates across the community: Adeline is a customer, March (the blacksmith) could make a special insulated cup. She thinks about product development. Winter packing line shows she finds humor in unusual customer preferences and is resourceful about logistics.

## Packing Up — End of Market Day

All lines require: npc = darcy, day_of_the_week = saturday, darcy_routine = darcy_packing.

**packing_up_1** (refresh: 1y):
- Darcy [happy]: "It's so nice when the big bag of coffee beans is empty at the end of the day!"

**packing_up_2** (refresh: 1y):
- Darcy [happy, sparkles]: "Whenever I need more energy for packing up the booth, I make myself another cup of coffee!"
- Darcy [think]: "Valen says I have a problem..."

**packing_up_3** (refresh: 1y):
- Darcy: "Evening, [Ari]. I was just breaking down the booth. Another Saturday Market in the bag!"

**packing_up_4** (refresh: 1y):
- Darcy: "Once I'm out of coffee beans, that's that!"
- Darcy [wink]: "But don't worry, I've got enough for your order yet, [Ari]!"

**packing_up_5** (refresh: 1y):
- Darcy [embarrassed]: "Almost done packing up... this barista misses her bed!"

**packing_up_6** (refresh: 1y):
- Darcy: "I worked at coffee shops in the Capital here and there, but nothing beats running your own booth."
- Darcy [happy, drop]: "That's what I tell myself every time I have to pack up."

**packing_up_7** (refresh: 1y):
- Darcy [happy]: "That was a very successful Saturday! I hope yours was good too, [Ari]!"
- Darcy [wink]: "Now let's both get some rest!"

**packing_up_8** (refresh: 1y, heart_level >= 0.5):
- Darcy [think]: "Packing up the booth always makes me reflect on things."
- Darcy [embarrassed, cheery]: "I'm so glad the Saturday Market got going again! Running this shop is a dream come true."

**packing_up_9** (refresh: 1y):
- Darcy [neutral]: "You wouldn't believe how many people stop by for more coffee while I'm packing up."
- Darcy [happy]: "So I made sure I pack up the coffee pot last!"

**packing_up_10** (refresh: 1y):
- Darcy [think]: "Sometimes I do a shot of espresso right before breaking down the booth."
- Darcy [mad, shock]: "I know I shouldn't when it's late, but I swear it helps me pack faster!"

**packing_up_11** (refresh: 1y):
- Darcy [think]: "The problem with selling coffee is you tell yourself you're just going to have a little cup while you work."
- Darcy [neutral]: "And then you have little cups all day, and then it's evening and you're buzzing!"

**Behavioral notes:** The packing lines are the richest source of personality. Key patterns:
- **Coffee dependency played for humor:** Multiple lines about drinking too much coffee. Valen (the doctor) says she has a problem. She does espresso shots late at night. She drinks "little cups all day" and ends up buzzing. This is her most consistent character trait.
- **Background:** Worked at coffee shops in the Capital before coming to Mistria. Running her own booth is a dream come true (high-friendship reveal at 50%).
- **Self-identification:** Calls herself "this barista" — it is her identity, not just her job.
- **Emotional warmth:** Wishes the player a good Saturday, tells them to rest. Inclusive language ("let's both get some rest").
- **Practical cleverness:** Packs the coffee pot last because people keep ordering during breakdown.
- **Relationship with Valen:** He comments on her coffee consumption, suggesting a friendly dynamic.

## Dell and Coffee

**dell_coffee** (refresh: 1y, Saturday, packing):
- Darcy [neutral]: "Another Market day spent watching vigilantly to make sure Dell doesn't get into the coffee."
- Darcy [think]: "She's way too conniving for her age."

**Behavioral notes:** Darcy actively keeps Dell (a child) away from coffee. Describes Dell as "conniving" — not mean-spirited, but amused and a little exasperated. Protective instinct toward the community's children while recognizing Dell's craftiness.

## Seridia (Dragon) Interactions

**seridia_stomach** (refresh: 1y, Saturday, requires caldarus_seridia_town = true, seridia_market_count >= 1, dragon_market = seridia):
- Darcy [neutral]: "Seridia seems like she's got a bottomless stomach..."
- Darcy [think]: "Every time she comes by, she gets one of everything."
- Darcy [happy]: "I made her her very own loyalty card!"

**Behavioral notes:** Darcy is unfazed by a dragon being her customer. Her response is purely entrepreneurial — she made Seridia a loyalty card. No fear, no awe, just good customer service. This is one of Darcy's most characterful moments: she treats everyone the same, even a dragon.

## Basement Line

**basement_1** (priority: basement, refresh: instantly, requires: npc = darcy):
- Darcy [neutral]: "Hiya, [Ari]!"

**Behavioral notes:** Simple greeting used in the basement/Aldaria context. Casual and friendly. "Hiya" is informal, consistent with her approachable personality.

## Gift Reactions

Source: `Bank/Darcy/Gift Lines/gift_lines.c.toml`

### Hated Gift — Ant
- Darcy [mad]: "Don't you dare bring $Ants$ near my stall! They'll get into everything!"

### Loved Gifts (specific items: chocolate, coconut_milk, cow_milk, crystal_berries, golden_cheesecake, golden_cookies, golden_egg, golden_cow_milk, spell_fruit, sugar)
- Darcy [happy, hearts]: "Ooh, thanks [Ari]! This is exactly what I need for a new recipe I'm working on!"

### Loved Gifts (generic)
- Darcy [happy, sparkles]: "I was just thinking I should stock up, and this is exactly what I needed! You're so on it, [Ari]!"

### Liked Gifts (generic)
- Darcy [happy]: "I really like this, [Ari]! Thanks, you're so generous!"

### Liked Gifts (specific items: fruits, egg, flour, tea, berries, grapes)
- Darcy [neutral]: "Oh, this looks nice. I'm gonna make it into something tasty!"

### Neutral Gifts (generic)
- Darcy [neutral]: "For me? Thank you."

### Neutral Gifts (coffee and tea items: coffee, cup_of_tea, floral_tea, green_tea, iced_coffee, jasmine_tea, latte, lavender_tea, mocha, roasted_rice_tea, rose_tea)
- Darcy [neutral]: "Oh, thank you [Ari], but I get more than enough coffee and tea in my line of work. I do appreciate the thought, though."

### Disliked Gifts
- Darcy [think]: "Ah, is this for me...?"

### Birthday Gift (neutral/liked/loved, after birthday)
- Darcy [embarrassed, sparkles]: "You knew it was my birthday? Gosh, [Ari]! Thank you!"

**Behavioral notes:** Gift reactions reinforce her identity as a baker/barista:
- Loved gifts tie directly to recipes she is working on — gifts are ingredients, not luxuries.
- The coffee/tea neutral response is distinctive: she politely declines because she already has plenty, but does not want to hurt feelings. This is the only NPC who rejects their own product category as gifts.
- Birthday reaction shows genuine surprise and gratitude ("Gosh") — she does not expect to be remembered.
- The ant reaction is her strongest negative emotion in the data — protective of her stall.

## Gossip Lines

No entries for Darcy found in `source/fiddle/gossip.toml` (no lines where Darcy gossips about others or others gossip about Darcy in this file).

The NPC data references a gossip system (line = "darcy_gossip", portrait = "happy", effect = "hearts") but the gossip text itself is not present in the extracted data files.

## Letters

No letters to or from Darcy found in `source/fiddle/letters.toml`.

## Barks

Darcy has a barks system entry (icon: spr_ui_generic_icon_npc_small_darcy) in `source/fiddle/barks.toml`, but no specific bark text is included in the data file.
