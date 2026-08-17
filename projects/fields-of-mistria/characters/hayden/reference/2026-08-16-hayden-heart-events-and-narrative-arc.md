---
type: reference
title: Hayden — Heart Events and Narrative Arc
description: Extracted dialogue and scene content from Hayden's 5 heart event cutscenes
  (2/4/6/8/10 hearts), wedding ceremony, henrietta tales thread, and barn repair story
  event.
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:22Z
resources:
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Hayden/hayden_two_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Hayden/hayden_four_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Hayden/hayden_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Hayden/hayden_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Hayden/hayden_ten_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_hayden.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Threads/Hayden/henrietta_tales.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Story Events/Town Repair/repair_haydens_barn.c.toml
---

# Hayden — Heart Events and Narrative Arc

Source: `source/t2/Cutscenes/Heart Events/Hayden/`, `source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/`, `source/t2/Conversations/Threads/Hayden/`, `source/t2/Cutscenes/Story Events/Town Repair/`

## 2 Hearts — Game Night with Friends

Source: `hayden_two_hearts.c.toml`

Kind: gameplay_triggered. Writes: `hayden_heart_event = "two_heart"` (expires 4d).

Participants: Hayden, Valen, Ryis, March, Henrietta. Location: Hayden's house.

Hayden hosts a game night. Valen brings a veggie plate with homemade dip. Ryis brings a board game called "Well-Constructed Slides and Structurally-Sound Ladders."

- Hayden [neutral_fist]: "I was just about to pop some corn, and then we can dive in!"

March arrives late ("Got held up on an order"). Henrietta pecks at March when he tries to sit.

- March [mad]: "Hayden, you really need to get that fowl of yours under control. She can't just go snapping at people."
- Hayden [gloomy]: "Henrietta's got nearly as many blue ribbons as you do March! She's a splendid chicken."

Player choice:
- "Plenty of other places to sit, March." → March [sigh]: "That's not the- fine."
- "March has a point." → Hayden [sweat]: "W-well, I'm sure she didn't mean it! Right, Henrietta?"

Henrietta storms off. Ryis suggests she may be territorial and used to having Hayden to herself.

- Hayden [neutral_arm_down]: "Well, let's give her some time to cool down and get this party started. I'll bring her out a bowl of popcorn when it's ready."

**Follow-ups:**
- March [neutral]: "If you want to talk about Hayden and his chicken, tough. I'm no gossip."
- Valen [think]: "Don't mind Henrietta too much. She's quite attached to Hayden." / "She was the last chick that his Grandmother helped hatch, some years back." / [sad]: "Henrietta has been his closest companion since Greta passed." / [happy]: "Perhaps the same could be said for Hayden, too."
- Ryis [neutral]: "Henrietta isn't a bad bird, she's just territorial." / "You'd think March would understand that."

## 4 Hearts — Socializing Henrietta

Source: `hayden_four_hearts.c.toml`

Kind: gameplay_triggered. Writes: `hayden_heart_event = "four_heart"` (expires 4d).

Participants: Hayden, Henrietta. Location: Hayden's farm, chicken coop area.

Hayden has extra feed stacked by the coop. He expresses worry about Henrietta's behavior.

- Hayden [sad]: "You know [Ari], farmer to farmer, I'm getting a mite worried about Henrietta."
- Hayden [annoyed]: "That bad behavior with March the last time... he's not the first person she's acted up with."
- Hayden [sad]: "If I don't nip it in the bud, I'm afraid it's going to get her in real trouble one of these days at a judging."
- Hayden [ugh]: "She could get her blue ribbons taken away!"
- Hayden [gloomy]: "But it's hard to discipline her. I raised her from an egg, you know?"
- Hayden [happy]: "Smartest chicken I've ever had. Heck, smartest animal!"
- Hayden [think]: "I just wish I could show her that the folks around here would like her, given half a chance."

Player choice:
- "Maybe we need to start socializing her?" / "What if we took her on a big day out?" → Both lead to Hayden agreeing.

- Hayden [think]: "I should send away for some books on the subject. I want to do this right."
- Hayden [happy_fist]: "I'll let you know when I've got the perfect outing planned for her, alright?"

**Follow-ups:**
- Balor [neutral]: "Hayden added a half dozen books about chickens to his latest supply order." / [think]: "Not sure what else an expert like him is hoping to learn!"
- Errol [think]: "Hayden asked what the best book on chicken psychology was. I had to confess that I had no idea."

## 6 Hearts — Henrietta's Day Out

Source: `hayden_six_hearts.c.toml`

Kind: gameplay_triggered. Writes: `hayden_heart_event = "six_heart"` (expires 4d).

Participants: Hayden, Henrietta, Holt, Dell, Luc, Maple. Location: General Store, then outdoors.

Hayden has a picnic basket from the Inn. He brings Henrietta to the General Store to choose her own treat.

- Holt [think]: "Now Nora normally doesn't let animals in here..." / [happy]: "But I'm sure she couldn't have meant Henrietta!"

Henrietta selects corn. Holt gives her a free gift ("It's been a real pleasure to have you at our humble store").

Dell, Luc, and Maple arrive. Dell asks Henrietta to play in the mud. Henrietta goes with the children.

- Hayden [sad]: "Think she'll be okay? Maybe I should tag along."

Player reassures him.

- Hayden [gloomy]: "It's been tough, taking care of the farm and worrying about Henrietta."
- Hayden [neutral]: "It means a lot to me, that you'd take the time to help Henrietta come out of her shell like this."
- Hayden [embarrassed]: "Thanks, [Ari]."
- Hayden [happy]: "This has turned into a real fine day, hasn't it?"

**Follow-ups:**
- Dell [think]: "Henrietta is really cool, huh? I wonder if mom would let me get a chicken too..."
- Holt: "Dell's been after Nora to let her get a chicken after playing with Henrietta." / [happy]: "And I'm on Dell's side!"
- Luc [happy]: "Henrietta is really good at finding bugs!" / [mad]: "We've got competition, [Ari]!"
- Maple [happy]: "It was fun playing with Henrietta!" / [think]: "I wonder what position I should give her in my royal court..."
- Nora [mad]: "You wouldn't be interested in taking on an apprentice, would you [Ari]?" / [ugh]: "Dell has gone chicken crazy."

## 8 Hearts — Dinner and Beach Walk

Source: `hayden_eight_hearts.c.toml`

Kind: gameplay_triggered. Writes: `hayden_heart_event = "eight_heart"` (expires 4d), `hayden_eight_heart_priority_bump = true` (expires 4d).

Participants: Hayden. Location: Hayden's house, then beach.

Hayden has cooked Vegetable Quiche from his own farm ingredients. Dialogue branches based on whether the player attended the Shooting Star Festival with Hayden (`shooting_star_hayden_attended`). Romance-path responses use portrait "embarrassed" or "shy_special"; friendship-path uses "sweat" or "happy".

- Hayden [neutral]: "Thanks for making the time to come over. I know it can be hard to get away when you're running a farm."
- Hayden [happy_fist]: "Today is just for the two of us. Henrietta is out with her friends."
- Hayden [think]: "They want to induct her into the Dragonguard. Said she'd make a good watchbird."
- Hayden [neutral_fist]: "She couldn't have done it without your help, [Ari]."

They walk to the beach after dinner.

- Hayden [neutral_arm_down]: "I like to come down here when I need a break."
- Hayden [think]: "Grandma used to take me out here. Said it was a good place to be alone with your thoughts."
- Hayden [think_special]: "But you know, I think I've spent enough time alone since she passed."
- Hayden [neutral_arm_down]: "I prefer having someone to share my thoughts with."
- Hayden [happy_arm_down]: "Someone to share a meal with. And a nice walk after."

Critical branching (romance path, shooting star attended):
- "I'm glad to have a best friend like you, Hayden." → best_friend status. Hayden [gloomy]: "[Ari]..." / [happy_arm_down]: "I'm glad to call you my best friend, too."
- "I wish you'd just kiss me already, Hayden." → dating status. Hayden [shy_special]: "[Ari]!" / [embarrassed]: "Do... do you mean it?" / [shy_special]: "You've got no idea how long I've been wanting to do just that!"

Critical branching (friendship path, no shooting star):
- "I'm glad to have a best friend like you, Hayden." → best_friend status. Hayden [happy_fist]: "[Ari]..." / [laugh]: "Gya ha ha!"
- "I've been meaning to tell you... I really like you, Hayden." → dating status. Hayden [shy_special]: "Do... do you mean it?" / [embarrassed]: "Truthfully, I've been meaning to tell you the same for some time now..." / [happy]: "Maybe we can consider today... our first date?"

Romance-path end:
- Hayden [blush]: "This is nice... I could watch the waves forever like this..."
- Hayden [neutral_arm_down]: "She'll be just fine. I want to be here with you."

**Follow-ups:**
- Hayden (friendship) [neutral]: "I had a great time with you, [Ari]. Let's do it again sometime soon!"
- Hayden (romance) [shy_special]: "I had a great time with you, [Ari]. Let's do it again sometime soon."
- Hemlock (romance only) [neutral]: "I've known Hayden for a long time, but I've never seen him quite this cheerful." / [happy]: "Suddenly he's buying everyone at the Inn a round of drinks! I wonder what's gotten into him?"
- Henrietta [neutral]: "(Henrietta gives a gentle coo as you draw near. She looks pleased.)"
- Luc [think]: "I can't believe it took us so long to get Henrietta into the Dragonguard." / [happy]: "She's great at finding bugs!"

## 10 Hearts — Proposal

Source: `hayden_ten_hearts.c.toml`

Kind: gameplay_triggered. Triggered by engagement ring. Location: Summit.

Engagement ring trigger dialogue:
- Hayden [think]: "You want to go somewhere to talk?"
- Hayden [confident_blush]: "Why don't we take a little walk up to the $Summit$? We should have it all to ourselves."

At the summit:
- Hayden [happy_arm_down]: "Ahhh... It's beautiful up here, ain't it?"
- Hayden [happy_arm_down_blush]: "There's no one else I'd rather share this with."
- Hayden [confident_blush]: "Pretty much anything worth doing is better when I get to do it with you."
- Hayden [confident_blush]: "I never feel alone when I'm with you."

Player choice:
- "How could you feel alone if I'm with you, silly?" / "You're not alone, Hayden. I'm always here for you." → Both lead to the same continuation.

- Hayden [sweat]: "Do you ever get a bit sad in the middle of a dinner with friends? Or maybe right afterwards?"
- Hayden [gloomy]: "A lonely little ache... that somehow gets louder when you're with other people?"
- Hayden [embarrassed]: "It's not all the time, mind you!"
- Hayden [shy_special]: "But there was less of it back when Gran was around..."
- Hayden [confident_blush]: "And there's been less of it since you became part of my life."
- Hayden [happy_arm_down_blush]: "Maybe it's a desire for a deeper connection. To really know someone, and to be known in return."
- Hayden [shy_special]: "Even when we were just friends, [Ari]... you managed to bridge the distance in a way no one else could."
- Hayden [think]: "People talk about the idea of 'found family'."
- Hayden [embarrassed]: "Well, until you became part of mine."

- Hayden [happy_arm_down_blush]: "I think the best part is that... I'll never have to stop getting to know you."
- Hayden [shy_special]: "I want to hear every funny story from when you were growing up..."
- Hayden [blush]: "I want to know what flavor tea I should make for you, if you ever catch a cold."
- Hayden [embarrassed]: "I want to find out what kind of things will make you laugh three years from now, ten years from now..."
- Hayden [confident_blush]: "Who will that version of [Ari] be? And what will I like best about them?"
- Hayden [blush]: "I just want you to understand how much you mean to me."

Gift (branches on first vs. repeat visit):
- First: Hayden [shy_special]: "Actually, on that note... I made a little something for you. Holt gave me some tips on whittling so I could get it just right." / [embarrassed]: "It's a $Carved Nest$. I wanted you to have it, so you'll never forget..."
- Repeat: Hayden [shy_special]: "That's why I made that $Carved Nest$ for you."

- Hayden [happy_arm_down_blush]: "You're family to me, [Ari]."
- Hayden [confident_blush]: "You always will be."
- Hayden [gloomy]: "And ah... there's something I want to ask you, [Ari]. Something important. But-"
- Hayden [embarrassed]: "But that's not why we came here today, is it."

Player choice:
- "I wanted to talk to you about our future together..." → proceeds to proposal
- "Let's talk about it another time..." → deferral

Proposal path:
- Hayden [shocked]: "Our-" (effect: shock)
- "I love you, Hayden. Are you going to ask me to marry you, or what?" →
- Hayden [laugh_blush]: "GYA HA HA HA!"
- Hayden [confident_blush]: "You already knew... Of course you did!"
- Hayden [blush]: "There's nothing I want more in this world, [Ari]."
- Hayden [happy_arm_down_blush]: "You will marry me, won't you?"
- Hayden [blush]: "Yes? Oh [Ari]..."
- Hayden [embarrassed]: "You've made me the happiest man in all of Aldaria."
- Hayden [happy_arm_down_blush]: "I love you so much..."
- Hayden [confident_blush]: "Now c'mere and let me hold you... my fiance!"
- Hayden [laugh_blush]: "GYA HA HA HA!"

Writes on acceptance: breakup_bump (expires 3d), engagement_bump (expires 2d), engagement_delay (expires 20h), engagement_cap = false (expires 3d). Action: can_talk hayden.

Deferral paths:
- First no: "Oh! Sure, that's no problem."
- Second no: "Oh! O-of course."
- Hayden [blush]: "You just let me know, okay? I can always make the time to come up here for a chat."

## Wedding

Source: `wedding_hayden.c.toml`

Kind: gameplay_triggered. 3 parts: ceremony, reception, departure.

**Ceremony (wedding_hayden_0):**

Participants: Hayden, Elsie (officiant).

- Hayden [embarrassed]: "[Ari]! H-hey. Happy... happy wedding... day."
- Hayden [shy_special]: "Ahem! Sorry, got a bit nervous there!"

Player choice:
- "Hayden, you look incredible!" / "Your hair's tied up! I like it." → Both: Hayden [embarrassed]: "Aww, shucks."

- Hayden [neutral]: "Hemlock and Holt swung by this morning and helped me with the suit, even took care of the animals for me!"

Elsie performs the ceremony with candle lighting.

- Hayden [happy_arm_down]: "Your light... It's like the glow of dawn! I feel as if I'm wrapped up in it."

Vows:
- Hayden [embarrassed]: "[Ari], your light fills a lonesome place in my heart that I never realized was made to hold it."
- Hayden [think]: "I bask in the warmth of your glow... So does this land, its people and its animals..."
- Hayden [gloomy]: "You are the sun in my sky. The love of my life. My family."
- Hayden [confident_blush]: "I want nothing more than to spend the rest of my days with you."

Player choice:
- "I love you, Hayden, and I want the same thing." / "I love you, Hayden. You're my family, too." → Hayden [confident_blush]: "I love you too."

**Reception (wedding_hayden_1):**

Valen gives the toast:
- Valen [happy]: "To Hayden, one of my oldest friends. Caring. Generous. Full of laughter..."
- Valen [think_smile]: "I've seen for myself just how much Hayden has opened up with you by his side."
- Valen [embarrassed]: "I am so happy to call you both my friends."

**Departure (wedding_hayden_2):**

- Hayden [neutral]: "What a day! I haven't laughed that much in ages."
- Hayden [happy_arm_down]: "Why, we ought to get married more often!"
- Hayden [neutral]: "Feels a bit odd, don't it? Everything's changed, and yet... I've never felt more content or more comfortable."
- Hayden [happy_arm_down]: "You know, as late as it is, I'm still full of vim and vigor!"
- Hayden [embarrassed]: "Though I don't mind telling you that the sooner I'm out of this starchy suit, the happier I'll be."
- Hayden [confident_blush]: "Let's call it a night, shall we?"

## Personal Thread — Henrietta Tales

Source: `Threads/Hayden/henrietta_tales.c.toml`

3-part thread. Requires: heart level >= 3 and < 8. Refresh: 1y (part 1), instantly (parts 2-3). Thread mutex system with 1w expiry, 1d delay between parts.

**Part 1:**
- Hayden [annoyed]: "Henrietta's been at the seed corn again. I keep telling her she can just ASK but that's a Featherbottom for you!"
- Player: "Uh... Featherbottom?" / "Wow, she's a Featherbottom?!"
- Hayden [happy]: "She's from the most award winning lineage to ever grace chickendom. Henrietta Jubilation Featherbottom!"
- Hayden [neutral_arm_down]: "It's been an honor and privilege to raise her, but sometimes I wonder if all those blue ribbons and first place trophies have gone to her head..."
- Hayden [gloomy]: "If she's not careful that could cost her a win one of these days."

**Part 2:**
- Hayden: "Been trying to teach Henrietta some better manners."
- Hayden [neutral_arm_down]: "Wiping her claws off before she comes inside the house, using her napkin at meal times, not interrupting when someone else is talking..."
- Hayden [embarrassed]: "You know. Manners!"
- Hayden: "Well I won't lie to you, she's a prideful lady. And not without cause!"
- Hayden [neutral_fist]: "But I'm trying to get her to understand that you can't be an award winner without award winning manners!"
- Hayden [neutral_arm_down]: "I gotta talk to Jo, I bet one of Henrietta's favorite meals will make her a bit more agreeable to the whole subject of decorum."

**Part 3:**
Writes: hayden_henrietta_tales_finished = true.

- Hayden [happy]: "Think I'm finally getting through to Henrietta, [Ari]! She's been real helpful lately, helping me find stuff that I've misplaced."
- Hayden [laugh]: "Now that's manners!"
- Hayden [neutral_arm_down]: "In fact, I think I'll treat her to her favorite meal tonight, =Corn= on the cob!"
- Player: "Do you normally lose stuff?" → Hayden [think]: "Well now that you mention it, it's been a pretty recent thing actually..."
- Player: "... do you always reward her when she finds things for you?" → Hayden [happy]: "Of course! Gotta have positive reinforcement, don't you?"
- Hayden [annoyed]: "You don't think... Henrietta's been hiding my stuff so she can bring it back for a reward do you?" (effect: drop)
- Hayden [laugh]: "Gya ha ha!"
- Hayden [wink_fist]: "I told you she was a smart chicken, [Ari]! Looks like she even managed to outsmart me!"

## Story Event — Repair Hayden's Barn

Source: `repair_haydens_barn.c.toml`

2 parts. Town repair quest chain.

**Part 1 (repair_haydens_barn_pt_1):**

Kind: gameplay_triggered. Writes: `rhb = "part_1"`.

Participants: Adeline, Hayden, Henrietta.

- Adeline [think]: "Grain rates are determined by the king's high council, but you make a compelling argument about a sliding scale for imports, Henrietta."
- Hayden [neutral]: "Now don't belabor the point Henrietta! You know these things can't move quickly."
- Hayden [neutral_arm_down]: "I've been excited since I got your letter! The new General Store has been the talk of the town."
- Hayden [gloomy]: "But I can't think of what we could do around this old farm that'd match..."

Adeline proposes expanding the barn and coop to accommodate new animals.

- Hayden [happy_arm_down]: "Why, that'd be a dream come true! Just think of the possibilities!"
- Hayden [neutral]: "Sheep and horses... heck, maybe even rabbits!"
- Hayden [happy_fist]: "And just imagine how cute they'd all be!"
- Hayden [neutral]: "Don't think for a minute I'd leave you out of this, [Ari]. Any new animals I start raising I'll make available to you as well."

Resources required: 400 Wood, 500 Stone, 8 Iron Ingots, 4000t. Donation Box placed next to barn.

Follow-ups:
- Hayden [neutral]: "I've been familiarizing myself with all the new animals I'll have in stock after the upgrade is done." / [happy_fist]: "Henrietta's been quizzing me!"
- Balor [think]: "Hayden let slip Adeline's little plan. Do you know how much a thoroughbred Aldarian race horse sells for?"

**Part 2 (repair_haydens_barn_pt_2):**

Kind: gameplay_triggered. Writes: `rhb = "part_2"` (expires 4d).

Participants: Hayden, Ryis, Landen, Adeline, Henrietta.

- Landen [neutral]: "This barn sure takes me back. You've kept my work in great condition, Hayden!"
- Hayden [embarrassed]: "I appreciate hearing that from you, Landen."

Construction scene with Ryis, Landen, and player.

- Hayden [happy]: "Would you look at that, Henrietta!"
- Hayden [neutral_arm_down]: "And I can't wait! Time to get the new animals settled."
- Hayden [happy_fist]: "You come on by any time you like for your own, [Ari]!"

Follow-ups:
- Hayden [neutral]: "I really can't thank you enough, [Ari]. Repairing the bridge, then the Mill, and now the new barn and coop..." / [happy]: "Have you just been repaying me back for those turnip seeds I gave you when you moved in?" / [laugh]: "Gya ha ha!"
- Henrietta [neutral]: "(Henrietta seems to be thanking you for the new coop)"

## Source Absences

- No pre-farm backstory scenes (how Hayden came to run the farm, life before grandmother Greta passed)
- No scenes showing Hayden's daily farm routine outside of the Henrietta arc and barn repair
- Heart events focus on the Henrietta socialization arc and romantic progression; no separate personal ambition or conflict arc beyond farm/loneliness
- No dialogue revealing Hayden's parents or how he came to be raised by his grandmother
