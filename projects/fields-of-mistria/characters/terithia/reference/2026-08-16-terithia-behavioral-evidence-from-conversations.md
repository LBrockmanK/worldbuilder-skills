---
type: reference
title: Terithia — Behavioral Evidence from Conversations
description: 'Extracted dialogue from Terithia group conversations: fishing life,
  storytelling, military background, social relationships, humor.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Adeline_Elsie_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Adeline_Hayden_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Adeline_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Adeline_Terithia_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Balor_Errol_Hayden_Terithia_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Balor_Hemlock_March_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Balor_March_Ryis_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Caldarus_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Dell_Luc_Maple_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Dell_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Eiland_Elsie_Errol_Juniper_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Eiland_Errol_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Juniper_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Seridia_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Errol_Hayden_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Errol_Holt_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Errol_Landen_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Errol_Landen_Terithia_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Errol_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Hayden_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Josephine_Nora/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Olric_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Landen_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/March_Olric/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/March_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Olric_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Terithia_Valen/
---

# Terithia — Behavioral Evidence from Conversations

Source: `source/t2/Conversations/Group Conversations/` — all directories containing Terithia conversations

## Adeline_Elsie_Terithia/fountain.c.toml

Refresh: 3m. Requires: fountain zone.

- Terithia [neutral]: "Ever thought about putting fish in the fountain?"
- Adeline [think]: "I... have not..."
- Elsie [think]: "Nor I..."
- Terithia [think]: "Yeah... Probably not a good idea."

## Adeline_Hayden_Terithia/biodiversity.c.toml

Refresh: never. Requires: date_time >= 1y.

- Terithia [think]: "Luc used a fancy word the other day, to describe all the different fish around Mistria."
- Terithia [neutral]: "Biodiversity, he said."
- Hayden [happy_fist]: "He sure knows his stuff! You too, Terithia. I'm comfortable saying I know a good deal about farm animals, but most fish look the same to me."
- Adeline [wink]: "You're quite knowledgeable too, Hayden. But I'll have you both know, I'm the resident expert on what animals are cutest."

## Adeline_Terithia/fishing_lessons.c.toml

Refresh: 2m. Requires: date_time > 2m.

- Terithia [wink]: "I'd be happy to give you fishing lessons any time, Adeline!"
- Adeline [happy] [effect: cheery]: "Oh, you think I can do it? I hear some fish can be feisty, but I'm very persuasive!"

## Adeline_Terithia_Valen/something_in_the_water.c.toml

Refresh: 2m.

- Adeline [neutral]: "How's fishing these days, Terithia?"
- Terithia [happy]: "It's always good in Mistria! There must be something in the water."
- Valen [think]: "Like fish."

## Balor_Errol_Hayden_Terithia_Valen/gourds.c.toml

Refresh: 3m. Requires: fall, year_time >= 2m 7d.

- Balor [neutral]: "Hayden, I'm but a humble merchant, so farming is well outside my wheelhouse."
- Balor [mad]: "However, I have to know. How do you get your pumpkins so big?"
- Valen [think]: "Well, Hayden's always had a green thumb, ever since we were kids."
- Terithia [happy]: "Sure, but judging by the size of those gourds, I'd say Hayden's got a whole green arm!"
- Errol [mad]: "And they're so brilliantly orange! Surely you have an explanation for that! Explain yourself, sir!"
- Hayden [happy]: "Now now! I'm just glad you appreciate them! Come by the farm any time and take a gander!"

## Balor_Hemlock_March_Terithia/poker.c.toml

Refresh: 3m. Requires: inn location, all 4 NPCs playing_poker = true.

**poker:**
- Balor [neutral]: "You've got a tell, March."
- March [mad]: "Don't try and psyche me out, Balor."
- Hemlock [think]: "Sorry pal, you definitely have a tell."
- Terithia [happy] [effect: sparkles]: "It's really obvious, actually."

Actions: bark annoyed on March.

**poker_2:**

Refresh: 1y. Same poker requirements.

- Balor [neutral]: "And one more card on the table makes the riverbank. Now, how's the table feeling in this last go around?"
- Hemlock [neutral]: "I'm in."
- March [mad]: "Me too. And I'll raise."
- Terithia [happy]: "Oho. I'll match that, March."
- Balor [wink]: "Looks like we've got ourselves a game!"

## Balor_March_Ryis_Terithia/forge_for_warmth.c.toml

**forge_for_warmth:**

Refresh: 3m. Requires: forge_lesson zone.

Actions: bark sweat_drop on Balor, Ryis, Terithia; bark annoyed on March.

- Balor [neutral]: "What do you think, March? Can you make me a new axle for my wagon?"
- Terithia [mad]: "Hey, no cutting! He's working on my fish hooks right now!"
- Ryis [think]: "Not to interrupt, but I really need those nails, March."
- March [ugh]: "No one's getting anything if you all don't shut it. I can barely concentrate!"

**forge_for_warmth_2:**

Refresh: 1y. Requires: forge_lesson zone, winter.

- Balor [neutral]: "What do you think? He's been swinging that hammer for a while now."
- Terithia [wink]: "He's definitely getting tired. Take a break, March!"
- Ryis [happy]: "Oh, I think he heard us. Look, he's hammering faster."
- March [unimpressed]: "[Ari], please tell those gossips that they can warm themselves by the forge only if they're quiet!"

**forge_for_warmth_3:**

Refresh: 1y. Requires: forge_lesson zone, winter.

- Balor [neutral]: "Looks like we've got a group. Should we get a game of cards going?"
- Ryis [wink]: "I brought a deck! I can deal."
- Terithia [think]: "All that's left is a card table! March, we're going to need your anvil."
- March [mad] [effect: angry]: "I'm working here!"

## Caldarus_Terithia/fishing.c.toml

**fishing_0:**

Refresh: 3m. Requires: caldarus_seridia_town = true, fishing zone or terithia_animation = fish.

- Caldarus [neutral]: "Watching you draw in a fish is like a poem with words in perfect arrangement."
- Caldarus [smile]: "It is wonderful to see a mortal who has mastered her destiny."
- Terithia [neutral]: "Oho... them's some pretty words, Caldarus."
- Terithia [wink]: "I'd better get serious... we'll both look pretty silly if I let the next fish get away!"

**fishing_1:**

Refresh: 3m. Same location requirements.

- Terithia [think]: "I've been wondering, Caldarus... you're one with nature and all that."
- Terithia [sad]: "Don't it bother you that I'm out here fishing up all manner of critters?"
- Caldarus [smile]: "I am not bothered. After all, I ate great mouthfuls of fish when I was in my draconic form."
- Caldarus [neutral]: "You are judicious, and you are generous, and you are thankful. It is all one can ask."
- Caldarus [smile]: "Nature is a cycle. Life will come again."

**fishing_2:**

Refresh: 3m. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false.

- Caldarus [sad]: "I tried to catch fish with a rod like yours, Terithia, but my claws became tangled in the line. It was most vexing."
- Terithia [wink]: "Sounds like the only fish you caught was yourself!"
- Terithia [happy]: "KYA HA HA!"

## Dell_Luc_Maple_Terithia/leviathan_storytime.c.toml

Refresh: 3m. Requires: terithia_story_time = true.

- Terithia [mad] [effect: sparkles_dark]: "And that's when the leviathan breached the surface! Half shark, half kraken, half stingray!"
- Dell [mad]: "I wish I was half shark!"
- Luc [think]: "I'll be half kraken!"
- Maple [neutral]: "That's a lot of halves, Miss Terithia!"

## Dell_Luc_Maple_Terithia/mystery_storytime.c.toml

Refresh: 1y. Requires: terithia_story_time = true.

- Terithia [mad] [effect: sparkles_dark]: "And what Seville didn't see in the storm was a HUGE BLACK SHADOW passin' under the belly of the boat! Then we all started hearing the strangest noise..."
- Maple [think]: "That can't be true, right [Ari]? Nothing could be that big..."
- Luc [think]: "Actually, the ocean is full of mysteries. Really big mysteries."
- Dell [mad]: "WOW! It sounds so cool! I wanna fight it!"

## Dell_Luc_Maple_Terithia/treasure_fishing.c.toml

Refresh: 1y.

- Maple [neutral]: "Have you ever fished up treasure, Miss Terithia?"
- Luc [think]: "Or ancient books?"
- Dell [mad]: "Or a skull?"
- Terithia [sad]: "Maple, Luc... why is Dell always asking me about dredging up skulls?"
- Dell [mad]: "Because they're so cool!"

## Dell_Terithia/more_sharks.c.toml

Refresh: 1y. Requires: terithia_animation = fish.

- Dell [think]: "Miss Terithia, I appreciate you teaching me how to fish, and I'm learning lots and lots..."
- Terithia [neutral]: "But?"
- Dell [mad]: "I thought we'd be catching more sharks!"

## Dell_Terithia/patience.c.toml

Refresh: 2m. Requires: terithia_animation = fish.

- Terithia [neutral]: "Fishing is all about patience, Dell! Patience, and then a quick strike!"
- Dell [sad]: "Patience? No wonder I'm so bad at fishing..."
- Terithia [wink]: "A warrior needs patience most of all, Dell."
- Dell [neutral]: "Really? Wow..."
- Dell [mad] [effect: sparkles]: "I'll be the most patient warrior ever! You'll see!"

## Eiland_Elsie_Errol_Juniper_Terithia/rum.c.toml

Refresh: 1y. Requires: evening or night, juniper_can_drink = true.

- Eiland [ugh]: "Help me, [Ari]! Terithia is making us try some rum she fished out of the bay!"
- Errol [happy]: "No need to be worried, Lord Eiland. The rum is perfectly safe, I assure you."
- Elsie [wink]: "I think Eiland's more worried because rum goes straight to his head."
- Juniper [annoyed]: "Ugh, me too."
- Juniper [wink]: "But it's hard to pass up a drink of such unique circumstance."
- Terithia [happy]: "That's the spirit! Bottoms up!"

## Eiland_Errol_Terithia/soup_season.c.toml

Refresh: 3m. Requires: winter, not inn.

- Eiland [think]: "In winter, hot meals are just the thing. Soup with breakfast, soup with lunch, and soup with dinner."
- Errol [happy] [effect: drop]: "He calls it soup season."
- Terithia [think]: "Soup season, eh? Maybe I'll get myself a helping from the pot in the Inn..."

## Elsie_Juniper_Terithia/poisoned_wine.c.toml

Refresh: 1y. Requires: after 6:00pm, all 3 NPCs activity = drink.

Actions: bark cute_face on Elsie, Juniper, Terithia.

- Elsie [think]: "Oh, it hasn't all been fun and romance..."
- Elsie [ugh]: "A jilted lover once sent me a bottle of poisoned wine."
- Juniper [sly]: "Well now! You can count on me to taste the first glass tonight, Elsie."
- Terithia [wink] [effect: sparkles]: "In fact, we'd better check the whole bottle just to be safe!"
- Terithia [happy]: "KYA HA HA!"

## Elsie_Seridia_Terithia/beach.c.toml

**beach_0:**

Refresh: 1y. Requires: caldarus_seridia_town = true.

- Seridia [neutral]: "I have vivid memories of flying on high, before plunging down into the water to seize my prey."
- Terithia [wink]: "Maybe that's my problem with trying to catch the Big One... it's too suspecting!"
- Elsie [happy]: "Oh, but keep at it Terithia. You'll have such a tale to tell when you catch it!"

**beach_1:**

Refresh: 1y. Requires: caldarus_seridia_town = true, beach location.

- Seridia [smile]: "I battled a gigantic crab, once. On a beach much like this one."
- Seridia [closed_eyes_smile]: "It ultimately fled from my might, but I expect some day it will return to finish our dance of death."
- Terithia [think]: "Huh... I also tangled with a beast of a crab in my younger days. It also scuttled off... wonder if it was the same fella!"
- Elsie [happy]: "Wouldn't that be something?"
- Elsie [wink] [effect: cheery]: "It's too bad, the only giant crab I've ever met is March!"

**beach_2:**

Refresh: 1y. Requires: caldarus_seridia_town = true.

- Terithia [neutral]: "You and I spent our youth on fightin', Seridia..."
- Terithia [wink]: "It's nice, retiring from that part of our lives."
- Seridia [closed_eyes]: "The problem with retirement is that there's always some problem that brings you out of it."
- Elsie [happy]: "Ooh... I read a book like that, once!"
- Elsie [think]: "It had lots of explosions..."

## Elsie_Terithia/bathhouse.c.toml

Refresh: 2m. Requires: bathhouse_change_room location.

- Terithia [think]: "I've always preferred a cold, salty brine, but these days warm water and bath salts does have its appeal."
- Elsie [happy]: "You're speaking my language, Terithia."

## Elsie_Terithia/inventory.c.toml

Refresh: 2m.

- Elsie [think]: "We get plenty of imports in the Capital, but I had no idea there were so many kinds of fish."
- Terithia [happy]: "It's a big wide world, Elsie! There's even fish I've never seen before, I'm sure of it!"

## Elsie_Terithia/romantic.c.toml

Refresh: 3m.

- Terithia [sad]: "I'm not much of a romantic, Elsie! I don't have a way with words."
- Elsie [neutral] [effect: cheery]: "You're a woman of the sea, Terithia! What's more romantic than the salty stoicism of the fisherwoman?"

## Elsie_Terithia/sailing.c.toml

Refresh: 1y. Requires: terithias_house or beach location.

- Elsie [think]: "You've done quite a bit of sailing in your day, haven't you Terithia?"
- Terithia [wink]: "Sure have! I don't miss the long hauls, though. Happy to trade it in for this pretty piece of Mistria's coastline!"

## Elsie_Terithia/shells.c.toml

Refresh: 2m.

- Elsie [neutral]: "Terithia tells me all manner of lovely shells wash up on this beach. Isn't that right?"
- Terithia [wink]: "Sure is. Just gotta keep your eyes peeled!"

## Elsie_Terithia/underwater_wine.c.toml

Refresh: 1y. Requires: both NPCs activity = drink.

- Elsie [happy]: "I'm so glad you're enjoying the wine, Terithia! I tried to find a vintage you'd like."
- Elsie [wink]: "You know, they age this one by submerging it in the sea! They call it underwater wine."
- Terithia [wink]: "No wonder I like it so much!"

## Errol_Hayden_Terithia/hayden_dinner.c.toml

**hayden_dinner:**

Refresh: 2m. Requires: haydens_house location, evening or night.

- Errol [neutral]: "Thank you for having us over for dinner, Hayden."
- Terithia [happy]: "Yes! You're a right thoughtful host!"
- Hayden [wink]: "Shucks! Food's always better when you got company!"

**hayden_dinner_2:**

Refresh: 2m. Same requirements.

- Hayden [neutral]: "Thank you both for coming over! It's nice to have company."
- Errol [happy]: "It's nice to be company!"
- Terithia [wink]: "I'm just here for the gossip!"
- Terithia [happy]: "KYA HA HA!"

## Errol_Holt_Terithia/mustache.c.toml

Refresh: 1y. Requires: bathhouse_change_room location.

- Errol [neutral]: "I must say, Holt, you've done well for yourself. I was admiring your mustache from across the room."
- Holt [wink]: "Well, I learned from the best. You've had a magnificent 'stache for as long as I can remember!"
- Terithia [think]: "These men and their mustaches..."

## Errol_Landen_Terithia/dug_up_wine.c.toml

Refresh: 3m. Requires: all 3 NPCs activity = drink, not terithias_house.

- Errol [neutral]: "This wine's not bad, you two! Where'd you dig it up?"
- Landen [think]: "I'm not sure... Terithia brought it with her."
- Terithia [neutral]: "This one's from the bottom of the bay!"
- Terithia [wink]: "And this next one I found in a sand dune on the Beach."
- Errol [happy] [effect: drop]: "So you quite literally dug them up... I see..."

## Errol_Landen_Terithia_Valen/saturday_no_market.c.toml

Refresh: never. Requires: quest_repair_the_bridge_complete = false, quest_repair_the_bridge_in_progress = true.

- Errol: "Remember the Saturday Market? We used to spend our entire day there. All the hustle and bustle, and there was always something new to eat!"
- Landen [think]: "Like that bakery that always had something new from the Capital!"
- Landen: "We used to make the rounds with Valen's father, you remember that doc?"
- Valen [raised_eyebrow]: "I do. You always snuck me sweets when my father wasn't looking."
- Terithia [happy]: "KYA HA HA!"
- Terithia: "You boys are making me nostalgic!"

## Errol_Terithia/the_big_one_sighting.c.toml

Refresh: 1y. Requires: not western_ruins.

- Errol: "Terithia tells me she saw the Big One this week..."
- Terithia: "It was out along the coast, towards the ruins... I could never mistake that shadow beneath the waves!"

## Hayden_Terithia/bite.c.toml

Refresh: 1m. Requires: beach location.

- Hayden [neutral]: "Any bites?"
- Terithia [think]: "I thought I had a bit of action, but it was just the current playing tricks."
- Terithia [wink]: "Some days are more of a waiting game!"

## Hayden_Terithia/boat_races.c.toml

Refresh: never.

- Terithia [neutral]: "You know, when we were between soldiering, some of the lads and I would race boats!"
- Hayden [wink]: "Boat races! That must have been a sight! And I imagine you had to know the currents pretty well to get to the head of the pack."
- Terithia [wink]: "Oho, you're right! And I won my share of races. The sea's a friend to me!"

## Hayden_Terithia/fishing.c.toml

Refresh: 2m.

- Hayden [neutral]: "I'm not sure fishing is for me, but it's neighborly of you to ask!"
- Terithia [wink]: "I respect that. Now, give me the latest about Henrietta! Is she still quarreling with that cow of yours?"

## Hayden_Terithia/pumpkins.c.toml

Refresh: 3m. Requires: fall, year_time >= 2m 7d.

- Hayden [neutral]: "You're welcome to any of the pumpkins I've got growing! I don't think they'll get much bigger."
- Terithia [happy]: "Oh, but what if they do? I want to see just how big they'll get!"

## Juniper_Olric_Terithia/odd_jobs.c.toml

Refresh: never. Requires: date_time >= 3m.

- Juniper [mad]: "Why am I seeing you everywhere these days, Olric? It's suspicious!"
- Terithia [wink]: "I don't know about suspicious, but Juni's right. The General Store, the Inn, the Blacksmith's, the Museum... you're everywhere!"
- Olric [happy]: "Aw, you noticed? I picked up some odd jobs. Life is all about the journey, you know?"

## Juniper_Terithia/favorite_fish.c.toml

Refresh: never.

- Terithia [neutral]: "What do you think, Juniper? Do you have a favorite fish?"
- Juniper [think]: "You know... I can't say I've given it much thought. I'm more of a dog person."

## Juniper_Terithia/fish_in_the_bathhouse.c.toml

Refresh: never.

- Terithia [think]: "If you think about it, fish are always in the Bathhouse... of life."
- Juniper: "That's very deep, Terithia."

## Juniper_Terithia/laugh.c.toml

Refresh: never.

Actions: bark sweat_drop on Terithia.

- Terithia [neutral]: "It's like this."
- Terithia [happy]: "KYA HA HA!"
- Terithia [wink]: "Now, you try it."
- Juniper [angry_brows]: "Okay, here I go. Kya... kya..."
- Juniper [wild_laugh]: "OH HO HO!"

## Juniper_Terithia/seawater_bathhouse.c.toml

Refresh: 2m.

- Juniper [neutral]: "You want me to add seawater to the baths? So it smells like the ocean?"
- Terithia [wink]: "Sure! I can show you how to make a nice seaweed extract. But we'll need to add a big fish to get the ambiance just right."
- Terithia [happy]: "KYA HA HA!"

## Landen_Terithia/count_fish.c.toml

Refresh: 1y.

- Landen [neutral]: "How many fish do you think you've caught in your life?"
- Terithia [wink]: "What a question! Why, I suppose I never kept track."
- Terithia [think]: "Should I start counting now?"

## Landen_Terithia/inn_special.c.toml

Refresh: 1y. Requires: inn location, both NPCs animation = eat.

- Landen [wink]: "So when you said I should try the special, you meant you wanna eat off my plate!"
- Terithia [neutral]: "Oh, hush up and give me another bite!"
- Terithia [happy]: "KYA HA HA!"

## Landen_Terithia/winter_fishing.c.toml

Refresh: 3m. Requires: winter.

- Landen [neutral]: "You don't stop fishing? Even in the winter?"
- Terithia [wink]: "I sure don't! There's all kinds of fish that only come out in the winter!"

## March_Terithia/hook_project.c.toml

Refresh: never. Writes: terithia_hook_project = true.

- March [neutral]: "You'll want your hooks to be made with a sturdy metal, but I think blending ores might get you a more flexible fishing rod."
- March [think]: "Can you give me some time with this? It's an interesting problem."
- Terithia [neutral]: "Take all the time you want!"

## March_Terithia/sashimi.c.toml

Refresh: never. Requires: march_heart_level >= 4.

- Terithia [happy]: "I didn't take you for the type to enjoy sashimi, March!"
- March [think]: "I respect the skill it takes to prepare it."
- March [neutral]: "And it tastes pretty good too."

## Olric_Terithia/custom_reel.c.toml

Refresh: 2m. Requires: olric not in march's zone.

- Olric [neutral]: "March has the pieces of your reel all finished. He's just gotta put them together."
- Terithia [neutral]: "Oh, he's a lifesaver. My ol' fishing rod jams a lot these days, and that's how the fish get away!"

## Terithia_Valen/fish_oil_good.c.toml

Refresh: 2m.

- Valen [think]: "Did you know? Fish oil is very good for the brain, [Ari]."
- Terithia [wink]: "That explains why I'm such a genius!"
- Terithia [happy]: "KYA HA HA!"

## Terithia_Valen/picture_of_health.c.toml

Refresh: 2m. Requires: clinic_f1 location.

- Valen [happy]: "You're the picture of health, Terithia. Fishing keeps you young!"
- Terithia [wink]: "We've got a flatterer here!"
- Terithia [happy]: "KYA HA HA!"

## Josephine_Nora/terithia_tells_stories.c.toml

Refresh: 1y. Requires: dell, luc, maple all at beach location. Terithia not present in the scene.

- Nora: "The children sure do have big imaginations."
- Josephine: "Terithia's stories always get them fired up."
- Josephine [happy]: "Honestly, me too. That lady's seen things!"

## March_Olric/terithia_stories.c.toml

Refresh: 2m. Requires: inn location, terithia_story_time = true. Terithia not present in the scene.

- March [unimpressed]: "Terithia's telling one of her ridiculous yarns again..."
- Olric [embarrassed]: "Shush, bro. I forget how this one ends."

## Source Absences

- No heart event files exist for Terithia (consistent with dateable = false in NPC data)
- No personal thread conversations found (Threads/Terithia/ directory not present)
- No conversations with Celine, Reina, or Seridia as a pair (Terithia appears with Seridia only in the Elsie_Seridia_Terithia trio)
- The `terithia_story_time` flag is referenced in conversation requirements but its trigger/source is not in these files
