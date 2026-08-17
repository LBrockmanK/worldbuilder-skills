---
type: reference
title: Balor — Heart Events and Narrative Arc
description: 'Extracted dialogue and scene content from Balor heart event cutscenes
  (2/4/6/8/10 hearts), wedding ceremony, and deal_gone_wrong thread: merchant identity
  arc, Wheedle confrontation, romantic progression.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Balor/balor_two_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Balor/balor_four_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Balor/balor_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Balor/balor_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Balor/balor_ten_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_balor.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Threads/Balor/deal_gone_wrong.c.toml
---

# Balor — Heart Events and Narrative Arc

Source: `source/t2/Cutscenes/Heart Events/Balor/` and related files

## 2 Hearts — Unloading Job and Nora's Suspicion

Source: `balor_two_hearts.c.toml`

Triggered by gameplay (turn-in). Location: wagon area. Participants: Balor, Nora, player.

Balor greets the player for an unloading job. Nora confronts Balor about pricing.

- Nora [mad]: "I know the market, Balor. We won't take charity!"
- Balor [happy]: "I couldn't pull the wool over your eyes if I tried, Nora. I'm making my share off your order, I assure you."
- Nora [mad]: "Balor..."
- Balor [wink]: "I do love our talks, but you'll have to excuse me. I've got business to attend to with [Ari]."
- Nora [ugh]: "Ugh, you are incorrigible."

Balor apologizes to player for using them as an excuse. Branching:
- "Why would Nora complain about low prices?" → Balor [think]: "Why indeed?"
- "Your prices don't seem that low to me..." → Balor [wink]: "Let me know the next time you're in the market for a hundred sacks of flour and I'll see what I can do."

Balor promises extra payment, asks player to carry boxes into the General Store.

Nora speaks to the player afterward:
- Nora [think]: "It's the most peculiar thing..."
- Nora [think]: "I have no idea how he does it, but Balor's the only one with a supply line into Mistria. Normally that would drive his prices up."
- Nora [mad]: "But that man... he's selling his goods for well below the new market value."
- Nora [sad, effect: drop]: "Do you think he's selling stolen merchandise?"
- Nora [think, effect: sigh]: "Maybe I'm just overthinking it."

## 4 Hearts — Balor's Journal

Source: `balor_four_hearts.c.toml`

Triggered by gameplay. Location: Sleeping Dragon Inn, then Balor's room upstairs. Participants: Hemlock, Balor, player.

Hemlock directs the player upstairs. In Balor's room, the player finds his journal open. Journal entries (no speaker attributed):

- "I've secured a reliable supply line from the Capital by adding to the bulk orders made by neighboring towns. From there, I can handle the final transport of goods to Mistria myself."
- "This will keep my prices low until Mistria stabilizes..."
- "Despite Nora's grumbling, she knows that Mistria is in a precarious position and the town needs every advantage they can muster."

Player choice: wait for Balor or continue reading. If continuing: "The next several pages feature column after column of numbers monitoring item prices and tedious order details going back several months."

Balor returns:
- Balor [sigh]: "I suppose the blame is on me for leaving my journal out."
- Balor [ugh]: "I hope I can trust your discretion on this."

Branching:
- "But there's nothing bad here..." → Balor [think]: "Mistria has been in a delicate position since the earthquake, there's no need to remind everyone."
- "It looks like you're working hard to help!" → Balor [angry_blush]: "That's-!"

- Balor [sigh, effect: sigh]: "Listen."
- Balor [think]: "I don't want you getting the wrong idea. What benefits the town benefits me, understand?"
- Balor [neutral]: "Mistria has the potential to be a major influence in Aldaria, and I want to get in on the ground floor."
- Balor [wink]: "I assume you do as well, since you moved here. Mistria will recover, we'll both make our fortunes, and then we can all go our separate ways."

Branching:
- "I guess I see your point..." → Balor [neutral]: "Excellent. I knew you were a kindred spirit the moment I met you."
- "But you seem to really like it here..." → Balor [angry_blush]: "A merchant needs to make his client's concerns his own, that's all."

Balor pivots to business advice:
- Balor [wink]: "You've been doing a great job with your shipments. In a short period of time you've become one of my key suppliers."
- Balor [neutral]: "My advice is to continue to diversify what you sell. Mistria needs all kinds of support to get back on its feet, so focusing on just one or two areas won't cut it."
- Balor [sly]: "Remember, business comes first, alright? There's a lot of profit to be made in Mistria for those with the eye for it."
- Balor [wink]: "And after that, who knows? The world awaits!"

## 6 Hearts — Wheedle's Offer

Source: `balor_six_hearts.c.toml`

Triggered by gameplay. Writes: `balor_heart_event = "six_heart"` (expires 4d). Location: Inn. Participants: Balor, Hemlock, Wheedle, player.

Balor celebrates with the player:
- Balor [neutral]: "Hemlock, bring us over whatever the most expensive drink on the menu is."
- Hemlock [neutral]: "You got it! Seems like you're in a rare mood, Balor."
- Balor [neutral]: "Profits are up, the town's businesses are booming... I couldn't be happier."

Toast with 3 options:
- "I'll drink to that!" / "Actually, can I get a lemonade?" / "To Mistria, to raising my cut of the profits!"

Wheedle arrives:
- Balor [mad]: "Wheedle! Yes, actually." (when asked if he minds)
- Wheedle [neutral]: "I represent a consortium of merchants who have taken an interest in your work in Mistria, Balor. We're all very impressed."
- Wheedle [wink]: "You've certainly made lemonade out of lemons."
- Balor [ugh]: "Get to the point."
- Wheedle [neutral]: "This paperwork transfers your Mistrian contract rights over to my business partners, and you walk away with..."
- Balor [angry_blush, effect: shock]: "This is-!"
- Wheedle [wink]: "Well, to call it a tidy sum doesn't do it justice, does it?"

Player choices:
- "Do the contracts with the Mistrian businesses stay the same?" → Wheedle [happy]: "I'm afraid that's not for you to decide."
- "And what's my cut?" → Wheedle [happy]: "And why would you need such a thing?"

- Wheedle [neutral]: "Well I won't overstay this warm welcome. Think about it, Balor. It's everything you've ever wanted, isn't it?"
- Balor [ugh]: "Well that was unexpected."
- Balor [concerned]: "Can I have a rain check on the meal, [Ari]? I've got a lot to think about."

Player choices (both lead to same response):
- "You aren't thinking of taking Wheedle's scummy deal?" / "You should do whatever makes you happy."
- Balor [sigh]: "..."
- Balor [concerned]: "Hemlock, can you bring me a fresh bottle? Thanks."

**Follow-up lines** (refresh: never, require `balor_heart_event = "six_heart"`):
- Adeline [think]: "Wheedle has been sniffing around town, but it seems like he's up to more than his usual tricks."
- Balor [think]: "Funny isn't it? You spend your whole life working towards a dream, then it drops into your lap and suddenly..." → [sigh, effect: sigh]: "Don't mind me."
- Wheedle [neutral]: "Checking in on your pal's Balor decision? Don't worry, I'm sure he'll make the right call." → [wink]: "Which is to say, the one that makes him the most money." → [happy]: "Huhuhu!"

## 8 Hearts — Dinner, Confrontation, and Declaration

Source: `balor_eight_hearts.c.toml`

Triggered by gameplay. Writes: `balor_heart_event = "eight_heart"` (expires 4d), `balor_eight_heart_priority_bump = true` (expires 4d). Location: Inn, private dinner upstairs. Participants: Balor, Josephine, Hemlock, Wheedle, player. Branches based on `shooting_star_balor_attended`.

### Part 1 — Dinner Setup

- Balor [neutral]: "Do you like it? I had a bit of help from Hemlock and Jo getting everything set up."
- Balor [ugh]: "Maple, Luc and Dell tried to pitch in too... but it was easy enough to clean up their mess afterwards."
- Balor [happy]: "For today's menu, Reina is preparing some of her finest dishes."

If shooting star attended: Balor [wink]: "It's worth enjoying a nice date since we have the time, don't you think?"
If not: Balor [neutral]: "It's worth celebrating our success since we have the time, don't you think?"

### Part 2 — Interrupted Confession

Balor tries to say something but is interrupted by Josephine bringing food, then again by Josephine pulling him aside about Wheedle.

- Josephine [think]: "Wheedle is downstairs, and he's demanding to see you."
- Josephine [mad]: "He said something about picking up your contract."
- Josephine [sad]: "Balor, surely you're not...?"
- Balor [hurt]: "I see. This is not the timing I'd hoped for."
- Balor [concerned]: "Jo... I need to talk to [Ari] first. Can you delay him?"
- Josephine [ugh]: "For you Balor, Hemlock and I will try to keep him busy. But you owe us one!"

### Part 3 — The Question

Shooting star attended (romance path):
- Balor [blush_special]: "Since the Shooting Star Festival, I've been wondering... what am I to you, [Ari]? We're more than just business partners... right?"

Shooting star not attended (friend path):
- Balor [concerned]: "About Mistria... would it matter to you if I stayed? Your business would continue to be successful, regardless. You don't really need-"

**Best friend branch:**
- Actions: `update_status = { npc = "balor", status = "best_friend" }`
- Romance path: Balor [concerned]: "Ah, of course. Thank you, [Ari]. It means a lot to hear you say that."
- Friend path: Balor [hope_special]: "Do you mean it, [Ari]? I feel the same way."
- Both: Balor [neutral/concerned]: "In this line of work, it can be hard to know who your real friends are."
- Balor [sincere_special]: "But... you've always been true to me, [Ari]. Someone I can truly rely on." / "But I've been giving it a lot of thought recently. You're someone I really trust. I know that I can rely on you."

**Dating branch:**
- Actions: `update_status = { npc = "balor", status = "dating" }`
- Romance path: Balor [blush_special]: "I... I feel the same way." → [blush]: "Honestly, I haven't been able to stop thinking about you since that evening we shared on the Summit."
- Friend path: Balor [blush_special]: "I... didn't realize you felt that way about me." → [embarrassed]: "Honestly, I felt something for you that first day when we crossed the bridge into Mistria together."
- Both: Balor [blush]: "I never planned on staying in Mistria so long, but over time... the people here won me over. You won me over, [Ari]."

### Part 4 — Confronting Wheedle

- Wheedle [neutral]: "I assume you're ready to sign that contract and leave this backwater for good?"
- Balor [mad]: "Wrong as usual, Wheedle."
- Balor [neutral]: "Mistria is my home, and its people and their livelihoods aren't chips to be bargained with."
- Wheedle [happy]: "Ah, I know a negotiation tactic when I hear one. If you sit down, I'm sure we can find a deal that works for you-"
- Balor [sincere_special]: "No amount of money would make me sign Mistria over to you and your band of crooks."

Wheedle attacks Balor's past:
- Wheedle [mad]: "And who are you exactly, to be calling me a crook? You've been stealing and cheating your way around the Capital longer than most."
- Wheedle [think]: "For the right price... there's no depths you won't sink to."
- Wheedle [sad]: "And you, [Ari]. Don't you see what's happening here? This is nothing but an act."
- Wheedle [mad]: "You'd better run while you still can. He'll turn on you the moment you stop being useful to him."

Balor's response:
- Balor [mad]: "Enough!"
- Balor [hurt]: "He's not... entirely wrong, [Ari]. I've done things in my past that I'm not proud of."
- Balor [sad_special]: "I was just a kid trying to survive. But I'm a different person now, a better person."
- Balor [sincere_special]: "I have been for a long time now. Even more so since I met you."

Player defense options (vary by romance/friend + dating status):
- Dating + romance: "I don't think so, Wheedle. (Kiss Balor)" / "Shut the hell up, Wheedle."
- Otherwise: "If you really knew him, you'd know he's changed. I believe in Balor." / "Shut the hell up, Wheedle."

Balor reveals the contract:
- Balor [sincere_special]: "See these scraps? I tore it up weeks ago."
- Balor [wink]: "As a little memento. Proof that my heart lies here with Mistria."
- Wheedle [mad]: "You... we're done here!"

Aftermath:
- Josephine [mad]: "He didn't even pay for his drink!"
- Hemlock [mad]: "If it means we won't see him here again, it's on the house."
- Josephine [embarrassed]: "Balor dear, we're all so proud of you."
- Hemlock [happy]: "She's right. You're a true Mistrian, Balor."
- Balor [embarrassed]: "Everyone..."

**Follow-up lines** (refresh: never, require `balor_heart_event = "eight_heart"`):
- Balor [sincere_special]: "[Ari]... thank you." → [hope_special]: "It makes all the difference in the world to know you're in my corner." (Requires `balor_eight_heart_priority_bump = true`. Actions: bark relationship_status.)
- Dell/Luc/Maple: Maple: "Hey, [Ari]! Did you have a nice time with Balor?" → Luc: "He gave each of us a bar of Chocolate to not interrupt." → Dell: "Dunno why." → Dell: "I think it'd have been a lot more fun if we had been there, don't you?"
- Hemlock [think]: "I nearly stepped in when things started getting heated between Wheedle and Balor." → [neutral]: "But I know Balor. He needed to handle Wheedle himself." → [wink]: "I'm glad you spoke up for him. He's lucky to have you."
- Josephine [mad]: "That Wheedle! That he would even THINK that Balor would ever sell out Mistria for a pile of dirty coins!"
- Reina [neutral]: "I had to step out for a moment while getting your special meal ready, and mom said I missed quite the show!" → [happy]: "I'm glad you helped Balor come out of his shell, [Ari]. He seems much happier now." (Requires `reina_is_partner = false`.)
- Wheedle [neutral]: "Ah, I thought I might be seeing you again." → [happy]: "Please rest assured that despite the... unpleasantness with Balor, you're more than welcome to continue patronizing my booth."

## 10 Hearts — Proposal on the Bridge

Source: `balor_ten_hearts.c.toml`

Triggered by engagement ring. Location: Eastern Road, bridge. Participants: Balor, player.

Engagement ring trigger:
- Balor [neutral]: "Something on your mind, [Ari]?"
- Balor [wink]: "How about we wander the Eastern Road and have ourselves a chat?"

At the bridge:
- Balor [happy]: "And this bridge has a special place in my heart."
- Balor [neutral]: "I think of you every time I cross it on my way back to town..."
- Balor [hope_special]: "You remember, right? This is where we first met."

Past reflection:
- Balor [concerned]: "I was in a different place in my life, then."
- Balor [hurt]: "My time in the Capital wasn't so far behind me yet. I know that I'm not that person anymore... but I can't deny that history, either."
- Balor [sincere_special]: "I want you to know all of me, [Ari]. That includes the parts of I'm not as proud of."

Player choices:
- "I don't mind a little bit of mystery..." → Balor [blush]: "[Ari]..."
- "I know you, and you're wonderful just as you are." → Balor [hope_special]: "[Ari]... Do you really think so?"

Capital backstory:
- Balor [sad]: "Looking back, I really did have a hard life. It's not an excuse, but-"
- Balor [mad]: "I was young, angry, and desperate..."
- Balor [sad]: "Stealing and cheating were all I knew growing up. It's how I survived life in the Capital."
- Balor [hurt]: "And... I must have carried some remnant of that with me to Mistria. In the beginning, I'd convinced myself this was just another stop on the road."
- Balor [blush_special]: "That changed because of you."
- Balor [blush]: "Seeing the way you made it your business to help the people of this town... it gave me confidence that I was finally headed down the right path."
- Balor [shocked_special]: "In no small part because you just... trusted me to do the right thing. Right from the beginning."
- Balor [blush_special]: "You never doubted me, [Ari]."
- Balor [blush]: "How could I possibly disappoint someone like you?"

Player choices (both lead to same next):
- "You make me want to be a good person, too." / "You always work hard to make Mistria better... I want to do the same."

- Balor [embarrassed]: "I'm setting a good example? For you?"
- Balor [embarrassed]: "That means a lot to me."

**Polished Gem gift** (branches on whether scene has been seen before):

First time:
- Balor [blush]: "That reminds me... I have something for you."
- Balor [hope_special]: "I found a piece of sea glass out by the Beach when I first arrived to Mistria."
- Balor [think]: "It was a humble little thing, probably washed in from the Capital..."
- Balor [blush]: "After we met, I began to polish it... and lately, it shines like a sapphire. Here, I want you to have this Polished Gem."

Second time:
- Balor [blush]: "That's why I gave you that Polished Gem."
- Balor [hope_special]: "It started out as a piece of sea glass I found by the Beach when I first came to Mistria."
- Balor [think]: "It was a humble little thing, probably washed in from the Capital..."
- Balor [blush]: "But after we met, I began to polish it... and now it shines like a sapphire."

Both paths:
- Balor [think]: "I don't know whether I'll ever truly shine the way it does... the way that you do."
- Balor [blush]: "But you make me want to try."

**Proposal sequence:**
- Balor [blush]: "There was something else you wanted to talk about, wasn't there?"
- Player: "I wanted to talk to you about our future together..."
- Balor [hope_special]: "Does that mean...?"
- Player: "I love you, Balor. Will you marry me?"

Writes: `breakup_bump = true` (3d), `engagement_bump = true` (2d), `engagement_delay = true` (20h), `engagement_cap = false` (3d). Actions: `can_talk = "balor"`.

- Balor [shocked_special]: "Marry-"
- Balor [hope_special]: "Marry you...?"
- Balor [blush_special]: "Are you sure? Really?"
- Balor [happy_blush]: "There's nothing I've ever wanted more!"
- Balor [embarrassed]: "Yes. I will!"
- Balor [blush]: "I love you, [Ari]."
- Balor [embarrassed]: "I never expected to meet someone like you..."
- Balor [blush]: "You're so much more than I ever bargained for."
- Balor [happy_blush]: "And I mean that in the best way possible."
- Balor [embarrassed]: "I get the feeling you'll be keeping me busier than ever from now on!"
- Balor [happy_blush]: "And now we have a wedding to plan, don't we? Let's go all out!"

**Decline path:**
- Balor [shocked]: "Oh? Sure thing."
- Balor [neutral]: "You know where to find me if you ever want to talk."

## Wedding Ceremony

Source: `wedding_balor.c.toml`

Three parts: ceremony, reception, outside the house. Officiant: Elsie. Reception speech: Josephine. Toasts: Hemlock, Maple, Luc.

### Ceremony (wedding_balor_0)

- Balor [happy_blush]: "[Ari], can you believe it? The whole town is here!"
- Balor [neutral]: "Although it wouldn't surprise me if they were mostly here for you."
- Balor [embarrassed]: "I certainly can't keep my eyes off you."

Player choices lead to:
- Balor [happy_blush]: "Oh, I don't know if 'like' fully covers it." → [embarrassed]: "It seems like every day that goes by, I fall more in love with you, [Ari]."
- OR Balor [embarrassed]: "If there was ever an occasion for it, it's our wedding." → [neutral]: "I wanted everything to be... perfect."

Elsie officiates: "We are gathered here today to celebrate the union of Balor and [Ari], as they join their light in matrimony."

Candle lighting:
- Balor [happy_blush]: "Your light... It's amazing! It seems like all of Mistria has lit up!"

Vows:
- Balor [sincere_special]: "[Ari]... you are the light that brightens my world."
- Balor [neutral]: "Driving away the shadows that once lingered in my heart."
- Balor [embarrassed]: "Your love has inspired me to embrace my true self. To never stop striving to make things better."
- Balor [happy_blush]: "I want nothing more than to share this life with you. To be yours, forevermore."

### Reception (wedding_balor_1)

Josephine's speech:
- "They both came to this village as strangers, during its time of greatest need."
- "A time when many had already left, and few would venture to come here..."
- "But they did. And despite the challenges that faced them, they stayed."
- "Through their tireless hard work, they not only helped to improve the town, but became a treasured part of it."
- "You are truly part of the family."

- Balor [embarrassed]: "Jo... everyone, thank you. I think I speak for [Ari] and I both when we say that we're lucky to call Mistria our home."

Toasts:
- Hemlock [happy]: "To [Ari] and Balor! May the care you show us all return to you tenfold."
- Maple [happy]: "May mom let me take over Balor's old room! Expanding my territory twofold!"
- Luc [embarrassed]: "May your life together be like a legendary bug... one of a kind!"

### Outside the House (wedding_balor_2)

- Balor [think]: "We've done something worthwhile here, haven't we [Ari]?"
- Balor [neutral]: "Somewhere along the way, it became about more than just helping Mistria..."
- Balor [embarrassed]: "It became about making a home for the two of us."

Player choices:
- "You always did dream big." → Balor [happy_blush]: "You're the only person I've met who dreams as big as I do, [Ari]."
- "I'd say... this is only the beginning." → Balor [happy_blush]: "That's just one of the things I love about you, [Ari]. You always know how to get me fired up."

- Balor [embarrassed]: "Shall we head inside and continue the celebration?"

## Personal Thread — Deal Gone Wrong

Source: `Conversations/Threads/Balor/deal_gone_wrong.c.toml`

4-part sequential thread. Requires: `balor_heart_level >= 3` and `< 8`. Uses thread_mutex system with 1-week expiry and 1-day delays between parts.

**Part 1** (refresh: 1y):
- Balor [wink]: "Want to hear a secret, [Ari]?"
- "I've got a line on a good deal... I'm meeting my contact tonight, and if everything goes well then yours truly will be rolling in it by the time the deal is done."
- Player: "Sounds kind of shady..." → Balor [wink]: "Don't worry, I'll be careful."
- Player: "Good luck!" → Balor [wink]: "Thanks, [Ari]. Luck is the one thing money can't buy..." → [think]: "Or was that love...?"

**Part 2** (refresh: instantly):
- Balor [think]: "That deal I was chasing took an odd turn... my contact says their client is crazy for strawberry milk? In exchange for raw, uncut gems?"
- [think, effect: sweat]: "He sounds eccentric... and just how much milk are we talking here?"

**Part 3** (refresh: instantly):
- Balor [think]: "[Ari], I could use your advice... this deal I've been working on is puzzling. Raw gems for strawberry milk?"
- [ugh]: "Even 50 gallons of strawberry milk isn't worth what we're trading for. What do you think?"
- Player: "It definitely seems suspicious..." → "You think so too, eh? Hmm... I'll have to look into it."
- Player: "Sounds like an easy deal... go for it!" → "That's what I don't like about it. It's too easy... I'll have to look into it."

**Part 4** (refresh: instantly, writes `balor_deal_gone_wrong_finished = true`):
- Balor [think]: "You know that deal I was working on? The gems for the milk?"
- [annoyed]: "I trailed my contact, and it turns out he was trying to trick a kid into parting with the find of a lifetime."
- [mad]: "Some people don't have a heart."
- Player: "Sounds like you've got a heart." → Balor [wink]: "Haha, is that wishful thinking, [Ari]?"
- Player: "How did things turn out?" → "I sent my contact packing and I introduced the kid's parents to an appraiser I trust. Came out empty-handed, but it's not about money ALL the time..." → [wink]: "Just most of it."

## Source Absences

- No pre-Mistria backstory scenes (Capital life referenced but not shown)
- No scenes showing Balor's daily merchant work or travel routes
- No Shooting Star Festival scene included in heart event files (referenced as a branching condition in 8 hearts)
- Heart events focus on the Wheedle contract arc and romantic progression
- The deal_gone_wrong thread is the only personal thread in the Threads/Balor/ directory
