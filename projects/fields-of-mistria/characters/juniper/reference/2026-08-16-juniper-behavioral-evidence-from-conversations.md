---
type: reference
title: Juniper — Behavioral Evidence from Conversations
description: 'Extracted dialogue from Juniper''s thread and group conversations: bathhouse
  operations, potion-making, interactions with children, dragon disciple dynamics,
  relationships with townsfolk.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Threads/Juniper/super_smart_frog.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Adeline_Eiland_Elsie_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Adeline_Elsie_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Balor_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Balor_Juniper_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Caldarus_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Celine_Elsie_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Celine_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Dell_Juniper_Luc_Maple/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Dell_Juniper_Luc_Maple_Seridia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Dozy_Juniper_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Eiland_Elsie_Errol_Juniper_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Eiland_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Hayden_Juniper_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Juniper_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Elsie_Juniper_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Hayden_Henrietta_Juniper_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Hayden_Juniper_Valen/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Josephine_Juniper/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Olric_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Ryis/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Seridia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Terithia/
- projects/fields-of-mistria/source/t2/Conversations/Group Conversations/Juniper_Valen/
---

# Juniper — Behavioral Evidence from Conversations

Source: `source/t2/Conversations/Threads/Juniper/` and `source/t2/Conversations/Group Conversations/` — all directories containing Juniper conversations

## Threads/Juniper/super_smart_frog.c.toml

**juniper_super_smart_frog_1:**

Refresh: 1y. Requires: juniper_heart_level >= 1 and < 4, juniper_super_smart_frog_finished = false.

Writes: thread_mutex = "juniper_super_smart_frog_1" (expires 1w), thread_delay = true (expires 1d).

- Juniper: "You there! Have you noticed any strange phenomena lately?"

Player choice:
- "Juniper, did you forget my name?" -> Juniper [embarrassed]: "What! No! It's... [Ari]...right...? Of course it is! Don't do that!"
- "Do you mean, like, other than you?" -> Juniper [unimpressed]: "Oh dear, is that what passes for humor among the yokels?"

Both paths continue:
- Juniper [annoyed]: "Please try and focus."
- Juniper: "While tracking ley line shifts early this morning east of town, I noticed... a frog."

Player choice:
- "Okay, and...?"
- "Wow, amazing. Listen, I have to go."

Both lead to:
- Juniper [think]: "Judging by your tone you haven't noticed any unusual amphibian behavior."
- Juniper: "This frog seemed much more intelligent then his fellows, I sense a deeper mystery at work here."
- Juniper [sly]: "It's a shame you weren't more help, but I suppose that's not a particular surprise. Let me know if you DO see anything, [Ari]."

**juniper_super_smart_frog_2:**

Refresh: instantly. Requires: thread_mutex = "juniper_super_smart_frog_1".

Writes: thread_mutex = "juniper_super_smart_frog_2" (expires 1w), thread_delay = true (expires 1d).

- Juniper: "There you are! Have you gleaned anything from your amphibian research?"

Player choice:
- "Ah, no..." -> Juniper [think]: "My own efforts have been less than fruitful as well. We are rather in the hinterlands, aren't we?"
- "What are you talking about?" -> Juniper [unimpressed]: "I suppose I shouldn't be surprised at the poor quality of assistants out here in the sticks."

Both paths continue:
- Juniper: "I managed to talk my way into Errol's good graces and obtain access to the Museum's archives."
- Juniper [annoyed]: "Unfortunately it's a mess! You'd think a curator could quickly identify all books and artifacts that are related to frogs, but frankly he looked bewildered."
- Juniper [sly]: "The man is clearly out of his depth."
- Juniper: "I'm afraid I'll have to resort to careful experimentation to tease out the secrets of this frog. Local folk tales suggest some ideas..."

Player choice:
- "Do you need any help?" -> Juniper [think]: "Oh I see how it is! NOW you want to be involved when the research is getting somewhere. No no, you had your chance."
- "You're uh, not thinking of kissing that frog are you?" -> Juniper [think]: "Well I am surprised! And here I thought I was the only one who had read that particular legend!"

Both paths continue:
- Juniper [wink]: "Just you wait, [Ari]. I think I'm onto something positively... ribbiting!"
- Juniper [wild_laugh]: "OH HO HO!"

**juniper_super_smart_frog_3:**

Refresh: instantly. Requires: thread_mutex = "juniper_super_smart_frog_2".

Writes: thread_mutex = "undefined", thread_delay = true (expires 1d), juniper_super_smart_frog_finished = true, juniper_super_smart_frog_gift_line = true (expires 1w).

- Juniper [embarrassed]: "I can't find him."

Player choice:
- "So how did your research with the frog go?"
- "Sorry, what?"

Both lead to:
- Juniper [annoyed]: "I SAID I have misplaced the specimen."
- Juniper [unimpressed]: "It was important to leave the frog in his natural habitat, and with his unusual behavior, I assumed he would be simple to track down again."
- Juniper [mad]: "And now he's gone! Vanished! A potentially monumental magical research subject has slipped through my fingers!"

Player choice:
- "Aww, I'm sorry Juniper. Do you want me to bring you any frogs I find?" -> Juniper [angry_blush]: "I don't need your pity! I-"
- "Looks like you need my help after all, huh?" -> Juniper [angry_blush]: "The gall! Why I oughta turn YOU into a frog-"

Both paths continue:
- Juniper [sad]: "No, that's not fair. You've been more helpful than most."
- Juniper: "Yes [Ari], I'd appreciate any frogs you come across."

**errol_super_smart_frog (side conversation, Errol speaks):**

Refresh: 1y. Requires: npc = errol, thread_mutex = "juniper_super_smart_frog_2".

- Errol [think]: "[Ari]... what do you think about the Museum adding an amphibian wing?"
- Errol [ugh]: "No no, I shouldn't let myself be swayed by every whim of the public."

## Adeline_Eiland_Elsie_Juniper/manor_dinner.c.toml

Refresh: 2m. Requires: all 4 NPCs eating or drinking, evening or night, juniper_can_drink = true.

- Elsie [wink]: "Have some more wine, Juniper!"
- Juniper [neutral]: "Oh, I really shouldn't."
- Juniper [think]: "Well... one more."
- Adeline [happy] [effect: drop]: "Juniper, don't feel obliged to keep pace with Aunt Elsie."
- Eiland [happy]: "Yes, keep pace with me and have another round of dessert!"

## Adeline_Elsie_Juniper/cauldron_gossip.c.toml

Refresh: 3m. Requires: bathhouse location, bathhouse/cauldron zone.

- Juniper [sly]: "Elsie's telling us about some of her exploits in the Capital... she's SUCH a role model."
- Elsie [wink]: "The Countess didn't give me flowers until the morning after! Can you believe it? It was so memorable... so roguish of her."
- Adeline [embarrassed]: "Wow, haha... this cauldron sure is fascinating, isn't it?!"

## Balor_Juniper/crystal_ball.c.toml

Refresh: 1y. Requires: town/wagon zone.

- Juniper [angry_brows]: "It doesn't matter how much you offer me, Balor. My crystal ball isn't for sale."
- Balor [sigh] [effect: sigh]: "A pity. A curiosity like that would fetch a pretty penny in the Capital."

## Balor_Juniper/dog_treats.c.toml

**dog_treats:**

Refresh: 1y. Requires: town/wagon zone.

- Balor [neutral]: "You want a gift for Dozy? Might I suggest this uncut emerald? It makes quite the statement."
- Juniper [unimpressed]: "Focus, Balor. I'm looking for dog treats."

**dog_treats_2:**

Refresh: 1y. Requires: town/wagon zone.

- Balor [neutral]: "These are the premium gold star treats you asked for, Juniper. I didn't know Dozy had such fancy tastes."
- Juniper [happy] [effect: sparkles]: "He doesn't, but he deserves the best."

## Balor_Juniper/nail_polish.c.toml

Refresh: 1y.

- Balor [think]: "I don't suppose you'd share the supplier for your nail polish, would you?"
- Balor [neutral]: "It would make a killing in the right markets."
- Juniper [sly] [effect: sparkles_dark]: "A lady's got to retain some of her mystique, Balor."

## Balor_Juniper/oils.c.toml

**oils:**

Refresh: 2m.

- Balor [neutral]: "You sure you don't want to export your bath oils? I'll give you a good price."
- Juniper [unimpressed]: "Hmph. My concoctions are priceless."

**oils_2:**

Refresh: 2m. Requires: not bathhouse building.

- Balor [neutral]: "How do you come up with so many different aromas at the Bathhouse? Your cabinet of scented oils must be bottomless."
- Juniper [sly]: "Trade secret."

## Balor_Juniper/soap.c.toml

Refresh: 2m. Requires: town/wagon zone.

- Balor [neutral]: "You want to sell your soap in the Capital?"
- Juniper [unimpressed]: "No, I want you to sell my soap in the Capital. I've got a bathhouse to run."

## Balor_Juniper_Valen/balor_test_subject.c.toml

Refresh: never. Requires: clinic_f1 location, balor_is_at = "clinic_f1/Top Bed".

- Juniper [wink]: "Valen won't let me give Balor one of my potions. He'd be up and about right away if he drank it. Probably."
- Valen [raised_eyebrow]: "You can't run trials on my patients, Juniper. I won't allow it."
- Juniper [sly]: "So YOU drink it!"
- Valen [wink]: "We can share it, if you like."
- Juniper [angry_blush]: "......"
- Balor [mad]: "Would you two be quiet? I'm trying to recover here!"

## Caldarus_Juniper/bathhouse.c.toml

**bathhouse_0:**

Refresh: 3m. Requires: caldarus_seridia_town = true, not eastern_road or deep_woods.

Actions: bark cute_face on Juniper.

- Caldarus [neutral]: "Juniper, there is a scent I was hoping you might be able to recreate."
- Caldarus [think]: "It is not of any true importance, but it is... nostalgic."
- Juniper [wink]: "I like a challenge! Tell me more, and I'll keep it in mind when I'm out foraging."

**bathhouse_1:**

Refresh: 3m. Requires: caldarus_seridia_town = true, caldarus not in seridia's zone.

- Juniper [neutral]: "You and Seridia have very different philosophies on things, don't you?"
- Juniper [think]: "I guess it never occurred to me that dragons wouldn't be of a mind with one another."
- Caldarus [neutral]: "Of a mind? With Seridia? I do not think such a thing is possible."
- Caldarus [mad]: "To begin with, have you seen her sense of decor?"

**bathhouse_2:**

Refresh: 3m. Requires: caldarus_seridia_town = true, bathhouse location.

Actions: bark cute_face on Caldarus, bark sweat_drop on Juniper.

- Juniper [neutral]: "Dozy has always been friendly, but you get along with him more than I anticipated."
- Caldarus [neutral]: "Is that right? Perhaps he can sense my appreciation for him..."
- Caldarus [smile]: "He is a calming and stabilizing presence in this bathhouse."
- Juniper [neutral]: "That's true."
- Juniper [annoyed]: "Wait. What does that make me?"

## Caldarus_Juniper/chat.c.toml

**chat_0:**

Refresh: 3m. Requires: caldarus_seridia_town = true, eastern_road location.

- Caldarus [neutral]: "You are quite knowledgeable about what grows along the Eastern Road, Juniper."
- Juniper [angry_brows]: "Of course. I'm an expert, after all."
- Juniper [think]: "But I suppose it was Celine who showed me where to do the best foraging. That country girl is surprising."
- Caldarus [smile]: "Yes... you both have a strong connection to this land."

**chat_1:**

Refresh: 3m. Requires: caldarus_seridia_town = true.

- Juniper [angry_brows]: "[Ari] told me that you're the one who lent <he>him</he><she>her</she><they>them</they><it>it</it><none>[Ari]</none> your power."
- Juniper [unimpressed]: "It explains why I detected such unique magic emanating from <he>him</he><she>her</she><they>them</they><it>it</it><none>[Ari]</none>."
- Caldarus [sigh]: "I merely opened a door. [Ari] is capable of great things, with or without me."
- Juniper [wink]: "Still... I imagine having a dragon on your side doesn't hurt."

**chat_2:**

Refresh: 3m. Requires: caldarus_seridia_town = true, caldarus not in seridia's zone, caldarus not inside.

Actions: bark sweat_drop on Juniper.

- Caldarus [smile]: "It is quite relaxing, seeking out herbs with you."
- Caldarus [sad]: "But you do not seem relaxed, Juniper. What is the matter?"
- Juniper [ugh]: "Well, Seridia doesn't like you very much. I'm just hoping she doesn't see us foraging together."
- Caldarus [neutral]: "Oh, do not worry. I know how to deal with her."
- Caldarus [sigh]: "If she asks, I will say that you are researching my weaknesses, or something of the like."
- Caldarus [think]: "You are right to be concerned, though. She can be quite... territorial."

## Celine_Elsie_Juniper/decoration.c.toml

Refresh: 1y. Requires: bathhouse location.

- Celine [very_happy]: "I love how you've decorated the place, Juniper. It's so pretty!"
- Juniper [unimpressed]: "Oh, well... I commend your taste, Celine."
- Elsie [wink]: "Look at you! Pleased as punch! Or whatever's in that cauldron of yours."

## Celine_Elsie_Juniper/new_bath_oil.c.toml

Refresh: 3m. Requires: bathhouse location, summer.

- Elsie [neutral]: "Your new bath oil does smell nice, Juniper, but it's missing something."
- Juniper [unimpressed]: "I want it to conjure that summery ocean feeling, but it doesn't quite get there, does it? How frustrating."
- Celine [neutral]: "Try adding something citrus! I think you'll be surprised at how breezy it smells."

## Celine_Juniper/floral_aid.c.toml

**floral_aid_0:**

Refresh: never. Requires: juniper_heart_level >= 2, both Juniper and Celine on eastern_road_foraging_north routine, juniper_status = "undefined".

- Juniper [unimpressed]: "Between us, [Ari], I had written most of this village off as country bumpkins..."
- Juniper [neutral]: "But Celine really knows her stuff."

**floral_aid_1:**

Refresh: 2m. Requires: both Juniper and Celine on eastern_road_foraging_north routine.

- Celine [neutral]: "Hi, [Ari]! I'm helping Juniper forage some rare flowers for one of her potions. They can be a bit tricky to identify if you're a novice to Mistria's flora."
- Celine [think] [effect: cheery]: "Gosh, I wonder what I'm helping her make. I should probably ask!"

## Celine_Juniper/herbs.c.toml

Refresh: 3m. Requires: bathhouse location.

- Celine [happy]: "I brought you those herbs you wanted, Juniper!"
- Celine [neutral]: "These are good for tea, and these are good for extracts."
- Juniper [sly]: "Perfect. And do you want payment in tesserae, or bath coupons?"
- Celine [sweat] [effect: drop]: "Tesserae, please!"

## Dell_Juniper_Luc_Maple/cauldron.c.toml

**cauldron:**

Refresh: 3m. Requires: bathhouse location, bathhouse/cauldron zone, date_time >= 1y.

Writes: cauldron_emergency = true.

- Juniper [annoyed]: "Repeat after me, children. \"I will not drink out of the Bathhouse cauldron.\""
- Maple [happy]: "I will not..."
- Luc [think]: "Drink out of the Bathhouse cauldron..."
- Dell [happy]: "Unless it's an emergency!"
- Juniper [happy]: "Very good."
- Juniper [mad]: "Wait a minute..."

**cauldron_2:**

Refresh: 1y. Requires: bathhouse location, bathhouse/cauldron zone, date_time >= 1y, cauldron_emergency = true.

Writes: cauldron_emergency = false.

- Juniper [annoyed]: "What emergency could possibly warrant drinking out of the cauldron, Dell?"
- Dell [mad]: "Lots of stuff!"
- Luc [neutral]: "Such as?"
- Dell [think]: "Well... what if I need powers?"
- Maple [ugh]: "Like what? The power of bad breath?"

**cauldron_3:**

Refresh: 3m. Requires: bathhouse location, bathhouse/cauldron zone.

Actions: bark cute_face on Dell, Luc, Maple; bark annoyed on Juniper.

- Juniper [mad]: "Dell, stop putting sticks in the cauldron."
- Dell [happy]: "But I'm helping!"
- Maple [happy]: "She's helping, Miss Juniper."
- Luc [happy]: "She's sooo helpful!"

## Dell_Juniper_Luc_Maple/dares.c.toml

Refresh: 3m. Requires: bathhouse location, bathhouse/cauldron zone, date_time >= 1y, winter.

- Juniper [unimpressed]: "Don't let yourselves freeze, children."
- Juniper [ugh]: "Warm yourselves by the cauldron, or I'll get a lecture from your parents."
- Dell [neutral]: "Can I get IN the cauldron?"
- Maple [neutral]: "I dare you, Dell. I double dare you."
- Luc [mad]: "I double dog dragon dare you!"
- Juniper [mad]: "No dares in the Bathhouse! Don't make me put up a new sign!"

## Dell_Juniper_Luc_Maple/fireplace.c.toml

Refresh: 3m. Requires: winter, bathhouse location, bathhouse/cauldron zone.

- Juniper [annoyed]: "Shouldn't you kids find a fireplace or something? There's one at the Inn, you know."
- Dell [neutral]: "But your bubbling cauldron is so toasty, Miss Juniper!"
- Luc [happy]: "It's the perfect temperature for warming up after our snow patrol!"
- Maple [happy]: "I'm even getting used to the smell!"

## Dell_Juniper_Luc_Maple/potion_of_night_vision.c.toml

Refresh: 3m. Requires: juniper_babysits = true, bathhouse location.

- Dell [think]: "What are you doing Miss Juniper?"
- Juniper [unimpressed]: "I'm making a potion of superior night vision."
- Maple [think]: "Why do you need a potion of super venison?"
- Juniper [think]: "It will help me see in the dark. Superiorly."
- Luc [ugh]: "Why does it smell like that?"
- Juniper [annoyed]: "That's the sulfur."
- Maple [ugh]: "And are you going to DRINK it?"
- Juniper [mad]: "No."
- Dell [happy] [effect: sparkles]: "Can *I* drink it?"
- Juniper [angry_brows]: "Tempting, but your mother would absolutely kill me."

## Dell_Juniper_Luc_Maple/warm_up.c.toml

Refresh: 3m. Requires: winter, bathhouse location, bathhouse/cauldron zone.

- Luc [mad]: "In the name of the Dragonguard, we're commandeering this cauldron!"
- Dell [mad]: "Good work, Luc. Now, Dragonguard... get yourselves warmed up!"
- Juniper [unimpressed]: "There's no need to commandeer my belongings, children. I'm not going to stop you from thawing yourselves out."
- Maple [happy] [effect: cheery]: "Sorry, this cauldron is definitely ours now."

## Dell_Juniper_Luc_Maple_Seridia/bathhouse.c.toml

**bathhouse_0:**

Refresh: never. Requires: bathhouse location, caldarus_seridia_town = true.

- Luc [neutral]: "Miss Seridia, I've been wondering... what's the evolutionary advantage for having red claws?"
- Maple [happy]: "They look pretty!"
- Dell [wink]: "I bet it's because they look cool!"
- Juniper [happy] [effect: drop]: "Children, don't bother Lady Seridia..."
- Seridia [closed_eyes]: "Ah, but the child is correct. It is because they look... cool."

**bathhouse_1:**

Refresh: 1y. Requires: bathhouse location, bathhouse/cauldron zone, caldarus_seridia_town = true.

- Dell [neutral]: "Miss Juniper, can you make a potion to turn the Dragonguard into real dragons?"
- Luc [think]: "We could each be a dragon, or we could combine into one big dragon!"
- Maple [happy]: "Only if Miss Seridia approves, of course!"
- Seridia [sly]: "Oh, I approve."
- Juniper [happy] [effect: drop]: "I don't have a dragon potion, but tell me... how do you feel about horses?"

**bathhouse_2:**

Refresh: 2m. Requires: bathhouse location, caldarus_seridia_town = true.

- Seridia [neutral]: "Tell me, children... why do you take up so much of Miss Juniper's time?"
- Dell [neutral]: "She pretends like she doesn't like us..."
- Maple [wink]: "But she TOTALLY does."
- Luc [happy]: "It's funny!"
- Seridia [closed_eyes]: "My disciple... is this true?"
- Juniper [embarrassed]: "NO... certainly not..."

## Dozy_Juniper_Valen/checkup.c.toml

**checkup:**

Refresh: 3m. Requires: dozy_checkup = true.

- Juniper [sad]: "Dozy just kept sneezing! So I thought you could take a look at him."
- Juniper [unimpressed]: "You know, since you're not busy or anything."
- Valen [neutral]: "So this is how you ask for help, hm? Well, the good news is that Dozy simply has a dust allergy."
- Valen [raised_eyebrow]: "The bad news is that I prescribe sweeping around here every once in a while."
- Dozy [happy] [effect: shock]: "(Dozy sneezes.)"

**checkup_2:**

Refresh: 3m. Requires: dozy at bathhouse, dozy_checkup = true.

- Juniper [annoyed]: "You already finished Dozy's checkup, so why are you still here? Don't you have patients or whatever?"
- Valen [happy]: "Oh, but Dozy and I are getting on so well. Aren't we, friend?"
- Dozy [neutral] [effect: sparkles]: "(Dozy gleefully wags his tail.)"
- Juniper [mad]: "Traitor..."

**checkup_3:**

Refresh: 3m. Requires: dozy_checkup = true.

- Juniper [mad]: "Maybe you should check him a third time, Valen."
- Valen [raised_eyebrow]: "I know you think I'm a quack, Juniper, but I assure you... I wouldn't misdiagnose a patient. Dozy is perfectly healthy."
- Valen [happy]: "Just a little sleepy."
- Dozy [neutral_closed]: "(Dozy gives Juniper and Valen a drowsy look, as though asking if he can go back to bed.)"

**checkup_4:**

Refresh: 3m. Requires: dozy at bathhouse, dozy_checkup = true.

- Dozy [happy]: "(Dozy excitedly wags his tail at Valen. He seems happy to see her.)"
- Juniper [unimpressed]: "Oh, he... likes you. Well, don't let it go to your head."
- Valen [raised_eyebrow]: "I wouldn't dream of it."

## Eiland_Elsie_Errol_Juniper_Terithia/rum.c.toml

Refresh: 1y. Requires: evening or night, juniper_can_drink = true.

- Eiland [ugh]: "Help me, [Ari]! Terithia is making us try some rum she fished out of the bay!"
- Errol [happy]: "No need to be worried, Lord Eiland. The rum is perfectly safe, I assure you."
- Elsie [wink]: "I think Eiland's more worried because rum goes straight to his head."
- Juniper [annoyed]: "Ugh, me too."
- Juniper [wink]: "But it's hard to pass up a drink of such unique circumstance."
- Terithia [happy]: "That's the spirit! Bottoms up!"

## Eiland_Juniper/manor_stones.c.toml

Refresh: never. Requires: date_time >= 1y.

- Juniper [think]: "My theory is that some of the foundation stones used to build the manor were carried over from the Western Ruins."
- Juniper [neutral]: "I get the sense that parts of the Manor House vastly predate others."
- Eiland [happy]: "Fascinating! You may be onto something. Let's investigate further!"
- Juniper [annoyed]: "Ah. If we must."

## Elsie_Hayden_Juniper_Valen/hayden_shares_food.c.toml

Refresh: 3m. Requires: inn location, evening or night, all 4 NPCs activity = eat.

- Elsie [happy]: "Hayden always shares his food with everyone! What a generous man."
- Valen [neutral]: "He's always been like that, in my recollection. I suppose it's the farmer in him... like he wants to share the bounty."
- Juniper [sly]: "Hayden, your order is delicious! Here, trade plates with me."
- Hayden [wink]: "I'm not that generous!"
- Hayden [laugh]: "GYA HA HA!"

## Elsie_Juniper/best_stories.c.toml

Refresh: 2m. Requires: manor_house building.

- Elsie [wink] [effect: hearts]: "Juni came to visit me! I always save my best stories for her."
- Juniper [think]: "Elsie's one of a kind. The stories she has to tell... steamier than the Bathhouse, I daresay."

## Elsie_Juniper/glass_of_wine.c.toml

Refresh: 2m. Requires: not morning, neither NPC activity = drink, juniper_can_drink = true.

- Juniper [sly]: "I won't lie to you, Elsie... I could use a glass of wine."
- Elsie [happy] [effect: sparkles]: "Juniper, dear... you're among friends."

## Elsie_Juniper/running_a_bathhouse.c.toml

**running_a_bathhouse:**

Refresh: 2m. Requires: bathhouse location.

- Elsie: "Running a bathhouse seems like hard work. Everyone else relaxes while Juniper keeps it running."
- Juniper [think]: "Honestly Dozy's a big help."

**running_a_bathhouse_2:**

Refresh: 1y. Requires: bathhouse location, date_time >= 2m.

- Juniper [neutral]: "In the circles I run in, you could become a powerful woman, Elsie."
- Elsie [neutral]: "Oh? While I appreciate a good bathhouse, I'm not sure I can see getting myself into the business."
- Juniper [ugh] [effect: drop]: "Ah, r-right. That's a shame."

## Elsie_Juniper/saturday_no_market.c.toml

Refresh: never. Requires: quest_repair_the_bridge_complete = false, quest_repair_the_bridge_in_progress = true.

- Juniper [think]: "It's too bad about the Market being closed. I'd love to go shopping at Louis'. Elsie said she'd show me how to dress for high society."
- Elsie [wink]: "I think you'd do just fine in high society as you are, my dear. But perhaps you can show me where you got those boots!"

## Elsie_Juniper/sorcerer.c.toml

Refresh: 1y.

- Elsie [neutral]: "I once had a dalliance with a man who claimed to be a sorcerer!"
- Elsie [think]: "We were so busy canoodling, I never did figure out if he was telling the truth."
- Juniper [happy] [effect: drop]: "Ahaha! A sorcerer! What an outlandish thing to say! A-anyway..."

## Elsie_Juniper_Terithia/poisoned_wine.c.toml

Refresh: 1y. Requires: after 6:00pm, all 3 NPCs activity = drink.

Actions: bark cute_face on Elsie, Juniper, Terithia.

- Elsie [think]: "Oh, it hasn't all been fun and romance..."
- Elsie [ugh]: "A jilted lover once sent me a bottle of poisoned wine."
- Juniper [sly]: "Well now! You can count on me to taste the first glass tonight, Elsie."
- Terithia [wink] [effect: sparkles]: "In fact, we'd better check the whole bottle just to be safe!"
- Terithia [happy]: "KYA HA HA!"

## Elsie_Juniper_Valen/drop_in.c.toml

Refresh: 3m.

- Juniper [annoyed]: "Elsie, would you please ask Valen why she insists on being here?"
- Valen [raised_eyebrow]: "Elsie, it might be prudent to inform Juniper that I'm here at your invitation. But I do wonder why she's here, too."
- Elsie [happy] [effect: cheery]: "Well, the Capital is known for the fireworks shows it puts on, and I was wondering how I might see something similar out in the country..."

## Hayden_Henrietta_Juniper_Valen/post_beach_dinner.c.toml

Refresh: 3m. Requires: group_two_beach_day = true, evening or night, all human NPCs eating or drinking, valen_can_drink = true, juniper_can_drink = true.

- Hayden [happy]: "What's better than a day at the Beach? Dinner with friends, that's what!"
- Juniper [annoyed]: "Friend, singular. That would be you, Hayden. Please ask that one to pass the pepper."
- Valen [happy] [effect: angry]: "This one heard you just fine. Here, the pepper. Now, are you going to share that wine or drink it all on your own?"
- Hayden [happy] [effect: sparkles]: "They're getting on well, aren't they [Ari]?"
- Henrietta [neutral]: "(Henrietta clucks to herself. She seems... unconvinced.)"

## Hayden_Juniper_Valen/toast.c.toml

Refresh: 3m. Requires: haydens_house location, evening or night, all 3 NPCs eating or drinking.

- Hayden [happy] [effect: cheery]: "Let's have a toast! To friendship!"
- Juniper [happy] [effect: cheery]: "To be clear, I'm only toasting you, Hayden."
- Valen [happy] [effect: cheery]: "Funny, I was thinking the same thing."

## Josephine_Juniper/looking_after_kids.c.toml

Refresh: 1y.

- Josephine [neutral]: "You get on so well with the kids! Thanks for keeping an eye on them every once in a while."
- Juniper [annoyed]: "It's more like they won't leave, no matter how many times I ask."
- Josephine [happy] [effect: drop]: "Huh?"
- Juniper [happy]: "I said, no problem! Any time!"

## Josephine_Juniper/soup.c.toml

Refresh: 1y. Requires: not inn location.

- Josephine [happy]: "Oh, yes... the pot at the Inn is open to anyone who needs a bowl. Hadn't you noticed?"
- Juniper [unimpressed]: "Ah... that explains why the children keep running to my cauldron and yelling FREE SOUP!"

## Josephine_Juniper/wine.c.toml

**wine:**

Refresh: 2m. Requires: not inn location, juniper_can_drink = true.

Writes: new_vintage = true.

- Josephine [neutral]: "We got in that wine you were asking for, Juniper! Come by any time and we'll pour you a glass."
- Juniper [sly]: "Oho! I'll stop by as soon as I can."

**wine_2:**

Refresh: 1y.

- Josephine [think]: "You're such a wine aficionado, I'm surprised you don't offer wine at the Bathhouse."
- Juniper [angry_brows]: "Dozy won't let me have wine in the bath, and if I can't do it, then no one can!"

## Juniper_Olric_Terithia/odd_jobs.c.toml

Refresh: never. Requires: date_time >= 3m.

- Juniper [mad]: "Why am I seeing you everywhere these days, Olric? It's suspicious!"
- Terithia [wink]: "I don't know about suspicious, but Juni's right. The General Store, the Inn, the Blacksmith's, the Museum... you're everywhere!"
- Olric [happy]: "Aw, you noticed? I picked up some odd jobs. Life is all about the journey, you know?"

## Juniper_Ryis/inspection.c.toml

Refresh: 3m. Requires: bathhouse/cauldron zone or town/bathhouse_exterior zone.

- Ryis [neutral]: "Got the inspection all done, Juniper. Might do some weatherproofing on the exterior, but that's just about being prepared."
- Ryis [happy]: "The bathhouse is looking pretty good overall."
- Juniper [wink]: "Music to my ears. And please, enjoy your next five baths free of charge."

## Juniper_Seridia/bathhouse.c.toml

**bathhouse_0:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false.

- Juniper [neutral]: "Seridia, I'm always admiring your nails! How do you get them so brilliantly red?"
- Seridia [sly_think]: "Oh, these? I was simply born into this world with talons crimson as the blood moon."
- Seridia [sly]: "Were you not also born with your intricately colored nails?"
- Seridia [sly_think]: "I presumed it to be an innate characteristic."

**bathhouse_1:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false.

- Seridia [smile]: "I have noticed your extensive collection of heeled boots, Juniper."
- Seridia [sly]: "They were an evergreen fashion in my royal court, worn by followers of all stripes."
- Seridia [closed_eyes_smile]: "I believe they wished to mimic the tall heel of my draconic gait."
- Juniper [sly]: "Evergreen indeed!"

**bathhouse_2:**

Refresh: 1y. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false.

- Seridia [closed_eyes]: "I do not understand why you will not incorporate bones into your wardrobe, my disciple."
- Juniper [think]: "I'll suffer for fashion up to point, but Lady Seridia..."
- Juniper [sad] [effect: sweat]: "Defeating a great beast so I can wear its bones? That's so much work!"

## Juniper_Seridia/disciple.c.toml

**disciple_0:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false, bathhouse location.

Actions: bark sweat_drop on Seridia.

- Seridia [neutral]: "I am adept at many schools of magic... but potions? I am not so familiar."
- Seridia [think]: "Smelling the contents of this cauldron... I am not sure that I would like to be."
- Juniper [happy] [effect: drop]: "The kids say the same thing..."
- Juniper [think]: "It probably needs more lilac."

**disciple_1:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false, bathhouse location, dozy at bathhouse.

Actions: bark sweat_drop on Juniper.

- Juniper [happy] [effect: drop]: "Er... is something the matter, Seridia?"
- Juniper [think]: "You've been watching me for a while now."
- Seridia [neutral]: "I wished to observe you at work, my disciple."
- Seridia [serious]: "I have a dragon's instinct for hierarchy, and yet my confusion only grows."
- Seridia [mad]: "Dozy is your familiar... but also your boss?"

**disciple_2:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false, bathhouse location, dozy at bathhouse.

Actions: bark sweat_drop on Juniper.

- Seridia [neutral]: "Your familiar is suspicious of me, my disciple."
- Seridia [closed_eyes]: "What can I do to win his trust?"
- Juniper [neutral]: "Dozy? Petting him usually does the trick."
- Seridia [serious]: "If he comes to me, he will receive pets."
- Juniper [happy] [effect: drop]: "I think you have to go to him..."
- Seridia [closed_eyes]: "Then it seems... we are at an impasse."

**disciple_3:**

Refresh: never. Requires: caldarus_seridia_town = true.

- Seridia [neutral]: "I have been curious... Are you able to sense the leylines in Mistria clearly, my disciple?"
- Juniper [neutral]: "More clearly here than anywhere else... even back at the coven."
- Seridia [neutral]: "Even during my reign, there were few able to sense leylines in this way."
- Seridia [closed_eyes]: "Take pride in it, my disciple."
- Juniper [shocked]: "Oh."
- Juniper [neutral] [effect: sparkles]: "I... I will!"

**disciple_4:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false.

Actions: bark sweat_drop on Juniper, bark cute_face on Seridia.

- Seridia [closed_eyes]: "Your familiar."
- Juniper [think]: "Dozy?"
- Seridia [neutral]: "Contrary to his name, he dozes sparingly and works quite vigorously."
- Seridia [think]: "Whereas you..."
- Juniper [annoyed] [effect: sweat]: "I'm not switching names with Dozy!"

**disciple_5:**

Refresh: never. Requires: caldarus_seridia_town = true, caldarus_seridia_town_timer = false.

- Seridia [smile]: "Do you have a bath oil that utilizes the =Night Queen=, Juniper? The smell pleases me."
- Seridia [closed_eyes_smile]: "Floral, yet somehow... dark."
- Juniper [think]: "I could make one... let me think on what might complement it."
- Seridia [closed_eyes]: "It is wise that you possess talents beyond magic, Juniper."
- Seridia [sly]: "A single-minded fervor is well and good, but diversions breed insight."

## Juniper_Seridia/first.c.toml

Refresh: never. Priority: max. Requires: juniper_seridia_first_convo = false, caldarus_seridia_town = true.

Writes: juniper_seridia_first_convo = true.

Actions: bark cute_face on Juniper, bark cute_face on Seridia.

- Juniper [closed_eyes]: "Y-your Majesty..."
- Juniper [think]: "Er. Your Holiness?"
- Juniper [ugh]: "Um... what is the appropriate way for me to address you?"
- Juniper [angry_brows]: "Unholy Dragon Seridia? The Witch Queen? Perhaps Dark Goddess?"
- Seridia [neutral]: "I have gone by all these names and more, my disciple."
- Seridia [closed_eyes_smile]: "For the time being, I have agreed to forgo such titles."
- Seridia [serious]: "You will call me Seridia."

## Juniper_Seridia/western_ruins.c.toml

**western_ruins_0:**

Refresh: never. Requires: caldarus_seridia_town = true, western_ruins location.

- Seridia [neutral]: "You seem familiar with these ruins, my disciple."
- Juniper [think]: "I scoured them searching for clues about the Witch Queen..."
- Seridia [smile]: "And lo, she has appeared."
- Juniper [wink]: "Thanks to [Ari], I would say. <he>He has</he><she>She has</she><they>They have</they><it>It has</it><none>[Ari] has</none> been full of surprises, to say the least."

**western_ruins_1:**

Refresh: never. Requires: caldarus_seridia_town = true, western_ruins location.

- Juniper [think]: "The location of the Witch Queen's palace was a mystery for the ages..."
- Juniper [happy]: "To think, she lived in Mistria's backyard all along!"
- Seridia [smile]: "Well, I would call this more of a summer home..."
- Juniper [think]: "So the mystery stands..."

**western_ruins_2:**

Refresh: 1y. Requires: caldarus_seridia_town = true, western_ruins location.

- Juniper [think]: "Ever since your return, the leyline that runs through these ruins has been very active."
- Seridia [neutral]: "It stands to reason. I have resumed my research and experimentation of magic..."
- Seridia [closed_eyes_smile]: "It pleases me to make the leylines sing again."

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

## Juniper_Valen/follow.c.toml

Refresh: 1y. Requires: town/clinic zone.

- Juniper [angry_brows]: "Are you following me?"
- Valen [happy]: "Juniper, we're outside my clinic."

## Juniper_Valen/riff_raff.c.toml

Refresh: never. Requires: inn location, both NPCs animation = drink, evening or night, juniper_heart_level < 4.

- Juniper [sly]: "[Ari]! You wouldn't believe what some of the locals are drinking tonight, it's really quite embarrassing."
- Valen [wink]: "Don't mind Juniper, that's just her way of being friendly."
- Juniper [mad]: "It's NOT."

## Source Absences

- No heart event files were extracted here (heart events are in a separate source directory)
- The `juniper_can_drink` flag is referenced in multiple conversation requirements but its trigger/source is not in these files
- The `juniper_babysits` flag is referenced in potion_of_night_vision requirements but its trigger/source is not in these files
- The `dozy_checkup` flag is referenced in checkup requirements but its trigger/source is not in these files
- The `group_two_beach_day` flag is referenced in post_beach_dinner requirements but its trigger/source is not in these files
- No conversations found between Juniper and: Holt, Landen, March, Nora, Reina as pairs
