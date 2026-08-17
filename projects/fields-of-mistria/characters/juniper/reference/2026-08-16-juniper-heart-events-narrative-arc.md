---
type: reference
title: Juniper — Heart Events Narrative Arc
description: 'Extracted dialogue and scene content from Juniper''s 5 heart event cutscenes
  (2/4/6/8/10 hearts), wedding ceremony, and super smart frog thread: potion experiments,
  curse transfer, romantic progression.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:21Z
resources:
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Juniper/juniper_two_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Juniper/juniper_four_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Juniper/juniper_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Juniper/juniper_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Juniper/juniper_ten_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_juniper.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Threads/Juniper/super_smart_frog.c.toml
---

# Juniper — Heart Events Narrative Arc

Source: `source/t2/Cutscenes/Heart Events/Juniper/`, `source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/`, `source/t2/Conversations/Threads/Juniper/`

## 2 Hearts — Potion Testing on Olric

Source: `Cutscenes/Heart Events/Juniper/juniper_two_hearts.c.toml`

Kind: gameplay_triggered. Olric and Juniper are present; player arrives.

Juniper is giving Olric a potion. Olric asks if it will help him "get shredded."

- Olric [think]: "Will this really help me get shredded, Juniper?"
- Juniper [sly]: "More than \"shredded\", if you can believe it. Whatever \"shredded\" means."
- Juniper [sly]: "So don't be shy... hop to it!"
- Olric [neutral]: "It... It's working! The power... it's coursing through me! I think."
- Olric [neutral]: "Do my muscles look bigger?"
- Juniper [happy]: "Colossal. I've outdone myself."
- Juniper [think]: "The effects of my potion will fade with time, though..."
- Juniper [angry_brows]: "So do come back when you feel like your oh-so-ordinary self again."
- Olric [neutral]: "You got it, Juni! I hope you can get it to taste better next time, blugh."
- Juniper [wink]: "Hmm, how does carrot-flavored sound?"
- Olric [neutral]: "Pretty good, for some reason..."

Olric leaves. Juniper addresses the player directly.

- Juniper [angry_brows]: "Now you. Come here."
- Juniper [neutral]: "[Ari]. The mysterious wanderer who came to Mistria."
- Juniper [angry_brows]: "I was wondering when you'd catch me working on my little experiments."
- Juniper [sly]: "So tell me... what brings you here, adventurer?"

**Branch 1:**
- Player: "A... bath? At the Bathhouse?"
- Juniper [annoyed]: "Oh, let's not play games. Unless... you're serious?"

**Branch 2:**
- Player: "The health tonic? From the message board?"
- Juniper [annoyed]: "You're joking. You're joking, right?"

Both merge:
- Juniper [unimpressed]: "Arcane energies flow around you, [Ari], but I see I've misunderstood their meaning."
- Juniper [unimpressed]: "I thought you were someone like me, here to stake out your territory. But it's clear to me now. You're hardly a threat."
- Juniper [think]: "Allow me to explain in terms that even you can understand. I came to Mistria because the magic here is unique. It bears studying."
- Juniper [sly]: "The villagers being so pliable... that's been a nice bonus. They drink any concoction I give them."

**Branch 3:**
- Player: "You're using the townsfolk to test your potions? You should leave them alone."
- Juniper [angry_brows]: "Oh, say it again. I'm quaking in my boots."

**Branch 4:**
- Player: "Can't we all just get along?"
- Juniper [angry_brows]: "Oh, you sweet, naive dear."

Both merge:
- Juniper [neutral]: "I have a lovely idea. I promise to leave the poor, defenseless townsfolk alone..."
- Juniper [sly]: "If YOU take their place and become my guinea pig."
- Juniper [wink]: "Yes, this could be the beginning of a beautiful... relationship."

**Branch 5:**
- Player: "Sounds fun."
- Juniper [think]: "Fun? My my... there are hidden depths to you, [Ari]."

**Branch 6:**
- Player: "Do I have a choice?"
- Juniper [sly]: "It's you or the denizens of Mistria, so... not really."

Both merge:
- Juniper [neutral]: "Well... I'm simply thrilled to reach an accord with you. Look at you... protecting your fellow villagers. How admirable. How brave!"
- Juniper [angry_brows]: "How cute."
- Juniper [laugh]: "OH HO HO HO!"

## 4 Hearts — Transformation Experiment

Source: `Cutscenes/Heart Events/Juniper/juniper_four_hearts.c.toml`

Kind: gameplay_triggered. Writes: juniper_heart_event = "four_heart" (expires 4d).

Juniper with her familiar Dozy. She expected the player to come.

- Juniper [happy]: "Well well, look who's here, Dozy! Looks like you were right."
- Juniper [sly]: "Oh, I didn't think you'd have the guts to show, but Dozy was positive you'd rush over."
- Juniper [laugh]: "Oh ho ho!"
- Juniper [neutral]: "Before I administer my concoction, it's important that you understand how brilliant I am."
- Juniper [think]: "I'm sure you've noticed the hot spring's water acts as a powerful restorative. It makes a perfect base for my potionwork."
- Juniper [sly]: "I believe this elixir will give you the power of a dragon."
- Juniper [wink]: "Maybe you'll even turn into one for me."

**Branch 1:**
- Player: "D-dragons? I don't think they exist."
- Juniper [happy]: "My, I've never met such a terrible liar, it's so charming."

**Branch 2:**
- Player: "A dragon versus a mere sorceress sounds pretty one-sided."
- Juniper [happy]: "It's so cute when you try to be threatening!"
- Juniper [sly]: "Just remember I'm the only one who could turn you back, silly."

Both merge:
- Juniper [wink]: "Whenever you're ready, [Ari]."

The potion goes wrong (implied transformation).

- Juniper [mad]: "What the-"
- Juniper [think]: "But I'm sure the recipe was correct... What went wrong?"
- Juniper [embarrassed]: "Ah yes, CLEARLY the issue lies with you, [Ari]. Willy-nilly infusions of power have unstabilized your morphogenic field."

**Branch 3:**
- Player: "Well at least I can still talk..."
- Juniper [mad]: "Y-you can still talk?"

**Branch 4:**
- Player: "Very funny, now stop horsing around, Juniper."
- Juniper [mad]: "Well at least your abysmal sense of humor is still intact..."

Both merge:
- Juniper [angry_blush]: "..."
- Juniper [unimpressed]: "This has been a complete waste of time."
- Juniper [sad]: "I'll prepare the counterspell."

**Branch 5 (both options lead to same):**
- Player: "Try to cheer Juniper up." / "Try to make Juniper mess up again."

- Juniper [sad]: "Now let's see..."
- Juniper [think]: "What are you-" [effect: surprise]
- Juniper [laugh]: "Oh ho ho!"
- Juniper [wink]: "Okay, okay. Hold still."
- Juniper [neutral]: "There, no harm done."
- Juniper [sly]: "You make an excellent test subject. I'll call on you again when I have something new to try."

**Follow-up conversation** (refresh: never, requires four_heart event):
- Juniper [think]: "How are you feeling, [Ari]? No lingering effects from that transformation, I presume?"
- Juniper [sly]: "Good. I was slightly worried when I saw you trotting toward me like that."
- Juniper [laugh]: "Oh ho ho!"

## 6 Hearts — Delivery Rounds (Body Swap)

Source: `Cutscenes/Heart Events/Juniper/juniper_six_hearts.c.toml`

Kind: gameplay_triggered. Writes: juniper_heart_event = "six_heart" (expires 4d).

Juniper tells the player to make deliveries while pretending to be her (implied body swap).

- Juniper [neutral]: "There you are!"
- Juniper [unimpressed]: "Ah, that's what you've decided to wear?"
- Juniper [think]: "Well this will hardly do. I suppose you'll have to go as me, and I'll have to borrow that unfashionably dressed body of yours in the meantime."
- Juniper [neutral]: "Your instructions and packages are on the desk."

**Delivery to Celine:**
- Celine [neutral]: "Hey Juniper! If you're stopping by that means the new plant growth tonic is ready, huh?"
- Celine [happy]: "Ooh, exciting!"
- Celine [neutral]: "Before you moved to town I was the only person here who was interested in this sort of thing."
- Celine [happy]: "It's been really fun collaborating with you on this."

**Branch 1:**
- Player (as Juniper): "It's been so nice having a project with you!"
- Celine [embarrassed]: "O-oh! Thanks Juniper, it means a lot to hear you say that."

**Branch 2:**
- Player (as Juniper): "Let's not get too mushy."
- Celine [laugh]: "Haha! Okay, okay."

- Celine [wink]: "I'll let you know how the new formula works out."
- Celine [happy]: "Say hi to Dozy for me."

**Delivery to Elsie:**
- Elsie [neutral]: "Juniper! I was just about to go for a stroll, care to join me?"
- Elsie [happy]: "Ahh, making the delivery rounds? Thank you, dear."
- Elsie [neutral]: "There's something nearly magical about your skin serums, much better than anything I've used in the Capital."
- Elsie [happy]: "And I do so appreciate the home deliveries. So thoughtful!"
- Elsie [think]: "Dozy getting along alright? And how's that new friend of yours, [Ari]?"

**Branch 3:**
- Player (as Juniper): "[Ari] is a real saint."
- Elsie [happy]: "Well now! I'm glad you've finally started being a little more honest with yourself."

**Branch 4:**
- Player (as Juniper): "[Ari] is a clown."
- Elsie [wink]: "Is that so? But we could all use someone around to make us laugh."

- Elsie [neutral]: "Take it from me and treasure those who choose to spend time with you, Juniper. We all appreciate your company, that's for sure."
- Elsie [happy]: "I won't keep you. I know we both have places to be! Let's catch up later this week."

**Return to Juniper:**
- Juniper [think]: "Well, how did it go?"

**Branch 5:**
- Player: "No issues."
- Juniper [ugh]: "Seems you were right about [Ari] again, Dozy."

**Branch 6:**
- Player: "Everyone had such nice things to say about you!"
- Juniper [angry_blush]: "W-why is that a surprise?"

- Juniper [neutral]: "In any case, thank you for your help."
- Juniper [embarrassed]: "Don't let it go to your head, though!"

**Follow-up conversations:**
- Celine [neutral]: "Juniper tells me you've been giving her a hand." / Celine [happy]: "That sounds so fun!"
- Dozy: "(Dozy seems to be thanking you for helping out Juniper the other day.)"
- Elsie [neutral]: "Juniper isn't an easy person to get to know with that barbed tongue of hers, but that's half the fun, wouldn't you say?"

## 8 Hearts — Curse Transfer and Confession

Source: `Cutscenes/Heart Events/Juniper/juniper_eight_hearts.c.toml`

Kind: gameplay_triggered. Writes: juniper_heart_event = "eight_heart" (expires 5d), juniper_eight_heart_priority_bump = true (expires 5d).

**Precondition:** Player must have seen break_fire_seal cutscene. A turn-in conversation requires player to bring Breath of Flame item.

**Lead-up dialogue** (requires break_fire_seal seen, eight_hearts not yet seen):
- Juniper [sincere_special]: "Are you feeling okay, [Ari]?"
- Juniper [unimpressed]: "You seem a little... tired."
- Juniper [neutral]: "I bet a bath would help!"

**Turn-in:**
- Juniper [neutral]: "Excellent, you brought the $Breath of Flame$. Come, [Ari]. It's time to test my latest infusion."

**Main scene — bath infusion:**
- Juniper [neutral]: "So this is what you're wearing into the bath?"
- Juniper [unimpressed]: "Whatever, I can work with it. Go on in-"
- Juniper [sly]: "I've added the flower, so the water should be ready for you."
- Juniper [think]: "I'll be there in a minute, I just need to change first."
- Juniper [neutral]: "What? Didn't I mention?"
- Juniper [sly]: "This is a special bath infusion. It's formulated for two people."

**Conditional branch** (shooting_star_juniper_attended):
- If attended: Juniper [think]: "I'm thinking of it as a potential... couples spa deal."
- If not: Juniper [think]: "I'm thinking of it as a potential... two-for-one spa deal."

- Juniper [angry_brows]: "Plus, how can I write up the results of my experiment if I'm not there to observe it?"
- Juniper [sad_special]: "..."

**Branch 1:**
- Player: "It's perfect!"
- Juniper [happy]: "Good, good."
- Juniper [neutral]: "The $Breath of Flame$ is stabilizing the heat nicely."

**Branch 2:**
- Player: "I'm more concerned about the color..."
- Juniper [annoyed]: "I'll have you know I carefully selected the ingredients to create this shade."
- Juniper [wink]: "Aesthetics are important."

**Branch 3 (both options merge):**
- Player: "It's surprisingly... really nice?" / "It's very soothing!"
- Juniper [happy]: "Right? Let your stress melt away..."
- Juniper [think]: "..."
- Juniper [sincere_special]: "Okay, [Ari]. Let's get this experiment started."
- Juniper [sad_special]: "Close your eyes and relax..."

**The curse transfer:**
- Juniper [mad]: "I-it's working! I knew it!"
- Juniper [angry_blush]: "Agh!"
- Juniper [think]: "Don't... don't look at me, [Ari]."
- Juniper [closed_eyes]: "I was expecting pain, but the scales..."
- Juniper [smile]: "You're going to be okay now. The $Sealing Scroll's$ final curse... I removed it from you."

**Juniper's confession:**
- Juniper [think]: "I never should have helped you track down that scroll in the first place. I don't know what you did with it down in the Mines..."
- Juniper [closed_eyes]: "But I could feel the shift happen. You opened it, didn't you? I don't know how you survived-"
- Juniper [think]: "But I DO know these scrolls were often crafted with a secondary curse."
- Juniper [closed_eyes]: "These auxiliary curses stay hidden until it's too late, undetectable by even the most skilled magic users."
- Juniper [think]: "I learned all about them in my studies."
- Juniper [closed_eyes]: "I couldn't dispel the curse, only weaken and transfer it. To dispel it would require $Essence Magic$..."
- Juniper [smile]: "A type of magic the ancients used. Power I don't have."
- Juniper [think]: "How ironic. It serves me right."
- Juniper [think]: "I've been lying to you, [Ari]."
- Juniper [smile]: "Well, I really have been using you as a test subject."
- Juniper [think]: "It was never about potions and errands. It's YOU I've been studying."
- Juniper [closed_eyes]: "I didn't know why I'd been pulled to Mistria, at first..."
- Juniper [think]: "A sorceress is taught early to follow her intuition. Clairvoyance is one of the few magics that still pass down through human blood."
- Juniper [closed_eyes]: "I understood the pieces would fall into place when the time was right."
- Juniper [smile]: "The reason became clear after you moved to town."
- Juniper [think]: "Magic began to flow throughout Mistria, always just beyond my reach. Witchspeak artifacts started being unearthed under my very feet."
- Juniper [closed_eyes]: "The signs were there. I knew you must be hiding some kind of power."
- Juniper [think]: "The body swap, the transformation incident... I was trying to uncover it, to seize it for myself."
- Juniper [smile]: "I couldn't stop myself. Not until..."
- Juniper [think]: "Forgive me [Ari]. Even now, I want that power. But it's not worth the price. I never meant for you to get hurt."

**Branch 4 (both merge):**
- Player: "Enough, Juniper. Please just let me help you." / "I forgive you Juniper, please just let me help you."

Player cures Juniper with Essence Magic.

- Juniper [smile]: "Help me? Don't fool yourself, you can't-"
- Juniper [shocked]: "[Ari]...?"
- Juniper [embarrassed]: "I'm... I'm cured? Just like that? H-how!?"
- Juniper [annoyed]: "You. You really let me get carried away. G-go sit in the other room and wait for me."
- Juniper [embarrassed]: "I need to change and then we're going to continue this conversation."

**Post-cure conversation:**
- Juniper [sincere_special]: "That spell..."
- Juniper [ugh]: "I've never seen anything like it."
- Juniper [mad]: "I see my suspicions were well-founded... but how, [Ari]? How did you come to possess Essence Magic?"

**Branch 5 (both merge):**
- Player: "(Give her the long version)" / "(Give her the short version)"

- Juniper [think_special]: "Wow."
- Juniper [sincere_special]: "I hardly know what to say. Caldarus... the seals... your magic."
- Juniper [think]: "It's really no wonder why-"

**Conditional branch** (shooting_star_juniper_attended):
- If attended: Juniper [think_special]: "I feel this way about you."
- If not: Juniper [sad_special]: "I felt myself drawn to you."

- Juniper [sincere_special]: "I'm sorry for everything."

**Critical branching:**
- "We're best friends, Juniper. I forgive you." -> best_friend status (action: update_status npc juniper status best_friend)
  - Juniper [neutral]: "[Ari]... thank you."
  - Juniper [think]: "I promise I won't try to take your power again."
  - Juniper [angry_brows]: "But I'm absolutely going to make you spill all the details from now on!"

- "I have feelings for you too, Juniper." (romantic path, attended) -> dating status
  - Juniper [think_special]: "You have feelings for me? I didn't think you felt the same way."
  - Juniper [blush]: "I- I promise I won't try to take your power again."

- "My feelings for you haven't changed, Juniper." (romantic path, not attended) -> dating status
  - Juniper [blush]: "Your feelings for me? I didn't think you felt the same way."
  - Juniper [think_special]: "I- I promise I won't try to take your power again."

Both romantic paths merge:
- Juniper [embarrassed]: "But I'm absolutely going to make you spill all the details from now on!"

**All paths merge:**
- Juniper [think]: "In the meantime... we should keep all this to ourselves. I don't think these backwater-"
- Juniper [ugh]: "Er- the fine townspeople of Mistria-"
- Juniper [neutral]: "Are quite ready to learn what's been going on right underneath their noses."
- Juniper [think]: "But... I sense that time will come."

**Final line conditional** (juniper_is_partner):
- If dating: Juniper [blush]: "Things are going to get interesting from here, [Ari]. I have to admit I'm looking forward to it."
- If not: Juniper [wink]: "Things are going to get interesting from here, [Ari]. I have to admit I'm looking forward to it."

**Follow-up conversations:**
- Juniper [think]: "The power of the dragon... Caldarus." / Juniper [happy]: "Perhaps a little walk in the woods is in order." (writes: juniper_seeks_out_caldarus = true)
- After seeking Caldarus — Juniper [unimpressed]: "I met up with that, er, rather tall friend of yours, [Ari]." / Juniper [mad]: "He's... not what I expected." / Juniper [annoyed]: "I thought he'd be fierce, powerful, overflowing with arcane energy." / Juniper [unimpressed]: "But instead he demurely served me these little burnt cookie things with oversteeped tea." / Juniper [ugh]: "He wouldn't stop apologizing when he saw I couldn't stomach either." / Juniper [annoyed]: "He's... kind of a nerd, [Ari]." / Juniper [laugh]: "Oh ho ho ho!"
- Caldarus [think]: "I had the pleasure of meeting your friend, Juniper." / Caldarus [ugh]: "She walked through the woods calling \"Dragon! Here Dragon!\"." / Caldarus [sigh]: "I caught up with her and then invited her in for tea... but it did not go as well as it could have." / Caldarus [embarrassed]: "I do not think she liked my cooking." / Caldarus [happy]: "All the same, it was nice to have company."
- Dozy gives player a stick, thanking them for saving Juniper while he was out. (action: item basic_wood count 1)

## 10 Hearts — Proposal

Source: `Cutscenes/Heart Events/Juniper/juniper_ten_hearts.c.toml`

Kind: gameplay_triggered. Triggered by engagement ring. Juniper suggests walking to the Summit.

- Juniper [neutral]: "It's so peaceful..."
- Juniper [happy_blush]: "What did I tell you? It's just the two of us up here today."
- Juniper [think]: "I don't get the chance to come to the Summit often."
- Juniper [neutral]: "The scenery is something else..."
- Juniper [happy]: "Mistria really is a special place, isn't it?"
- Juniper [unimpressed]: "I used to think it was just another backwater village."
- Juniper [think_special]: "Turns out I just couldn't see what was right in front of me."

**Branch 1:**
- Player: "You were too busy keeping your eyes on me..."
- Juniper [embarrassed]: "[Ari]!"
- Juniper [think_special]: "Well... you're not wrong."

**Branch 2:**
- Player: "We've both grown a lot since coming to Mistria, haven't we?"
- Juniper [neutral]: "I suppose you're right."

Both merge:
- Juniper [closed_eyes]: "It's funny, looking back on those days."
- Juniper [sad_special]: "I never wanted to admit it at the time, but I was actually pretty lonely when I first moved here."
- Juniper [unimpressed]: "I've always had a tendency to keep people at a distance."
- Juniper [neutral]: "I used to, anyway."
- Juniper [neutral_blush]: "That started to change after I met you, [Ari]."
- Juniper [think_special]: "Somewhere along the way, I began to let other people in."
- Juniper [sad_special]: "The truth is, if it wasn't for you..."
- Juniper [sincere_special]: "I'm not sure how things might have turned out. I was selfish, inconsiderate-"

**Branch 3:**
- Player: "It's thanks to you that I'm alive and well!"
- Juniper [embarrassed]: "O-oh. Well..."

**Branch 4:**
- Player: "Well if it weren't for you, I might be a lizard by now!"
- Juniper [embarrassed]: "A lizard!?"

Both merge:
- Juniper [think_special]: "You're talking about the $Sealing Scroll$, right?"
- Juniper [sad]: "Removing the curse from you was the least I could do."
- Juniper [think_special]: "But you know, [Ari]... it's funny you should bring that up."
- Juniper [angry_blush]: "I've spent a lot of time reflecting on everything that happened."
- Juniper [think_special]: "I realized that I should have done more to protect you in the first place."
- Juniper [sad]: "If anything were to ever happen to you, I-"
- Juniper [angry_blush]: "Well, I won't ever let anything like that happen to you again!"

**Conditional branch** (cutscene_seen_juniper_ten_hearts — repeat visit):
- If repeat: Juniper [happy_blush]: "That's why I made that $Protection Scroll$ for you." / "It's a kind of good-luck charm." / "I just wanted you to know... I'll always be here for you, [Ari]."
- If first: Juniper [happy_blush]: "Here. It took longer than I planned, but I made this for you." / "Consider it something of a good-luck charm." / "It's my way of saying... I'll always be here for you, [Ari]."

- Juniper [think_special]: "Whatever life throws your way, I'll help you get through it."
- Juniper [sincere_special]: "Even if your magic is stronger than mine. It doesn't matter."
- Juniper [happy_blush]: "If it came to it, I'd give it all up if it meant you'd stay safe by my side."
- Juniper [think_special]: "A-anyway. There was something else you wanted to talk about, right?"

**Branch 5:**
- Player: "I wanted to talk to you about our future together..."
- Juniper [embarrassed]: "Our-"
- Juniper [neutral_blush]: "Our future together?"

**Branch 6:**
- Player: "I love you, Juniper. Will you marry me?"

State writes: breakup_bump (3d), engagement_bump (2d), engagement_delay (20h), engagement_cap = false (3d). Action: can_talk juniper.

- Juniper [teary_blush]: "[Ari]..."
- Juniper [happy_blush]: "Yes!"
- Juniper [embarrassed]: "YES!"
- Juniper [wild_laugh_blush]: "OH HO HO HO HO!"
- Juniper [embarrassed]: "I can't believe this is really happening... I'm going to be your wife!"
- Juniper [teary_blush]: "I'm so happy, [Ari]!"
- Juniper [neutral_blush]: "I love you so much!"
- Juniper [happy_blush]: "I can't wait to start planning our wedding!"

**Decline path:**
- Player: "Let's talk about it another time..."
- Juniper [unimpressed]: "Oh? Sure, that's no problem."
- Juniper [blush]: "Whenever you want to talk, you know where to find me."

## Wedding

Source: `Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_juniper.c.toml`

Kind: gameplay_triggered. 3 sections: ceremony, reception, post-wedding.

**Section 0 — Ceremony:**

- Juniper [neutral]: "[Ari]... You..."
- Juniper [sly]: "You've outdone yourself."

**Branch 1:**
- Player: "Speak for yourself. I'm breathless."
- Juniper [happy]: "I'm happy you're pleased."
- Juniper [sly]: "These bridal silks were woven long ago and far away, using a technique lost to time."
- Juniper [sincere_special]: "I brought this dress among other heirlooms when I came to Mistria..."
- Juniper [neutral]: "I never thought the day would come that I'd get to wear it."
- Juniper [think_special]: "Look at me, prattling on. You got me carried away, [Ari]. I thought I wasn't nervous."

**Branch 2:**
- Player: "I was hoping you'd like it."
- Juniper [happy]: "V-very much so."
- Juniper [think_special]: "Seeing you dressed up like this, it's finally starting to feel real..."
- Juniper [neutral]: "We're really doing this, [Ari]!"
- Juniper [happy]: "I'm so happy!"

Elsie officiates:
- Elsie [neutral]: "Welcome, one and all. We are gathered here today to celebrate the union of Juniper and [Ari], as they join their light in matrimony."
- Elsie [closed_eyes]: "Two brilliant souls-"
- Elsie [neutral]: "Swept to Mistria by the tides of fate."
- Elsie [embarrassed]: "Destined to meet, to unite as one."
- Elsie [neutral]: "Please go ahead and light your candles."

Vows:
- Juniper [sly]: "This light of mine shines for you."

**Branch 3:**
- Player: "And mine for you."
- Juniper [sincere_special]: "I'll never let it go out."

**Branch 4:**
- Player: "And I'll protect it with everything I have."
- Juniper [neutral]: "[Ari]..."

- Juniper [neutral]: "[Ari]... With your light, you have cast warmth and love into my life."
- Juniper [sincere_special]: "Illuminating even the deepest recesses of my heart."
- Juniper [sly]: "A magic only you are capable of conjuring."
- Juniper [neutral]: "With these words, I bind my heart to yours for all that may come..."

**Branch 5:**
- Player: "I love you, Juniper. I am eternally under your spell."
- Juniper [happy]: "I love you too, [Ari]."

**Branch 6:**
- Player: "I love you, Juniper. My heart is yours."
- Juniper [sly]: "I love you too, [Ari]."

Elsie [neutral] [effect: cheery]: "I now pronounce you married!"

**Section 1 — Reception:**

Celine, Elsie, Dell, Maple, and Luc give toasts.

- Celine [blush_special]: "Um... c-can I have your attention, everyone? I prepared a toast!"
- Dell [happy]: "We want to make some toast, too!"
- Maple [wink]: "Yeah, you should let us go! We've been friends with Juniper the longest!"
- Luc [happy]: "And [Ari] too! He's/She's/They've been my protege since he/she/they first came to Mistria!"
- Dell [happy]: "Congrats Juniper, congrats [Ari]!"
- Dell [happy] [effect: sparkles]: "May your lives be happy, and your cauldrons normal-smelling."
- Luc [embarrassed]: "I haven't cried this much since my mantises got married..."
- Maple [happy]: "Queen Maple hereby congratulates you on your nuptials!"
- Maple [happy]: "And may your enemies' positions be weakened as a result."

**Section 2 — Post-wedding:**

- Juniper [neutral]: "I can hardly believe today was real..."
- Juniper [think_special]: "Marrying you... and being celebrated by so many people..."
- Juniper [sly]: "It's like a dream."
- Juniper [sincere_special]: "But it's not a dream, is it? Here you are, standing right in front of me."
- Juniper [happy]: "I'm... so happy I can't stand it."

**Branch 7:**
- Player: "Me too, Juniper." / "Welcome home, Juniper."

- Juniper [sly]: "[Ari]..."
- Juniper [think_special]: "The mysterious wanderer who came to Mistria..."
- Juniper [sly]: "Now I have a lifetime to unravel you."

## Thread — Super Smart Frog

Source: `Conversations/Threads/Juniper/super_smart_frog.c.toml`

3-part thread. Requires heart level 1-3 (below 4). Thread mutex system with 1-week expiry between parts, 1-day delay between conversations.

**Part 1:**
- Juniper: "You there! Have you noticed any strange phenomena lately?"

**Branch 1:**
- Player: "Juniper, did you forget my name?"
- Juniper [embarrassed]: "What! No! It's... [Ari]...right...? Of course it is! Don't do that!"

**Branch 2:**
- Player: "Do you mean, like, other than you?"
- Juniper [unimpressed]: "Oh dear, is that what passes for humor among the yokels?"

- Juniper [annoyed]: "Please try and focus."
- Juniper: "While tracking ley line shifts early this morning east of town, I noticed... a frog."
- Juniper [think]: "Judging by your tone you haven't noticed any unusual amphibian behavior."
- Juniper: "This frog seemed much more intelligent then his fellows, I sense a deeper mystery at work here."
- Juniper [sly]: "It's a shame you weren't more help, but I suppose that's not a particular surprise. Let me know if you DO see anything, [Ari]."

**Part 2:**
- Juniper: "There you are! Have you gleaned anything from your amphibian research?"
- Juniper [think]: "My own efforts have been less than fruitful as well. We are rather in the hinterlands, aren't we?"
- Juniper: "I managed to talk my way into Errol's good graces and obtain access to the Museum's archives."
- Juniper [annoyed]: "Unfortunately it's a mess! You'd think a curator could quickly identify all books and artifacts that are related to frogs, but frankly he looked bewildered."
- Juniper [sly]: "The man is clearly out of his depth."
- Juniper: "I'm afraid I'll have to resort to careful experimentation to tease out the secrets of this frog. Local folk tales suggest some ideas..."

**Branch 3:**
- Player: "Do you need any help?"
- Juniper [think]: "Oh I see how it is! NOW you want to be involved when the research is getting somewhere. No no, you had your chance."

**Branch 4:**
- Player: "You're uh, not thinking of kissing that frog are you?"
- Juniper [think]: "Well I am surprised! And here I thought I was the only one who had read that particular legend!"

- Juniper [wink]: "Just you wait, [Ari]. I think I'm onto something positively... ribbiting!"
- Juniper [wild_laugh]: "OH HO HO!"

**Part 3:** (writes: juniper_super_smart_frog_finished, juniper_super_smart_frog_gift_line expires 1w)
- Juniper [embarrassed]: "I can't find him."
- Juniper [annoyed]: "I SAID I have misplaced the specimen."
- Juniper [unimpressed]: "It was important to leave the frog in his natural habitat, and with his unusual behavior, I assumed he would be simple to track down again."
- Juniper [mad]: "And now he's gone! Vanished! A potentially monumental magical research subject has slipped through my fingers!"

**Branch 5:**
- Player: "Aww, I'm sorry Juniper. Do you want me to bring you any frogs I find?"
- Juniper [angry_blush]: "I don't need your pity! I-"

**Branch 6:**
- Player: "Looks like you need my help after all, huh?"
- Juniper [angry_blush]: "The gall! Why I oughta turn YOU into a frog-"

- Juniper [sad]: "No, that's not fair. You've been more helpful than most."
- Juniper: "Yes [Ari], I'd appreciate any frogs you come across."

**Cross-NPC follow-up:**
- Errol [think]: "[Ari]... what do you think about the Museum adding an amphibian wing?"
- Errol [ugh]: "No no, I shouldn't let myself be swayed by every whim of the public."

## Source Absences

- No pre-Mistria backstory (how Juniper learned sorcery, her coven, her life before arriving)
- No scenes showing Juniper's daily bathhouse operations outside the heart event contexts
- Heart events reference a Sealing Scroll quest line and Caldarus relationship that are part of the main story, not fully represented in these files
- The "beach_accident" outfit referenced in the NPC data is not explained in any heart event scene
- No detail on what "Witchspeak artifacts" are or how they connect to the broader lore beyond Juniper's mention
