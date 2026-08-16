---
type: reference
title: March — Heart Events Narrative Arc
description: 'Extracted dialogue and scene content from March''s 5 heart event cutscenes
  (2/4/6/8/10 hearts) and wedding ceremony: forge craft arc, family backstory, emotional
  progression.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:15Z
resources:
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/March/march_two_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/March/march_four_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/March/march_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/March/march_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/March/march_ten_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_march.c.toml
---

# March — Heart Events Narrative Arc

Source: `source/t2/Cutscenes/Heart Events/March/`

## 2 Hearts -- Confrontation at the Farm

Source: `march_two_hearts.c.toml`

Location: gameplay-triggered. March confronts the player directly.

Key dialogue:
- March [neutral]: "I didn't think you'd actually show."
- March [think]: "I hear you've been making yourself useful around town. Everybody only has good things to say about you."
- March [unimpressed]: "Oh please. You're in way over your head. You come out here, no money, no experience, and think you can just fake your way through running a farm?"
- March [mad]: "And now everyone in town acts like it was YOU who won the first-place blacksmithing trophy three years running."
- March [neutral]: "It's all fun and games now, but the second things actually get tough, I'm sure you're going to ditch Mistria and its problems."

Player choices:
- "It's been lots of fun helping out!" -> March [ugh]: "Fun? Ugh."
- "So I guess this is where you apologize for your bad attitude." -> March [mad]: "Hah, not a chance!"
- "I'm not going anywhere!" -> March [unimpressed]: "We'll see."
- "Jealousy is an ugly thing, March." -> March [mad] [effect: angry]: "Hmph..."

March gives the player something despite his hostility:
- March [think]: "If you fail, you can't blame it on a lack of help from me."
- March [unimpressed]: "Who knows, maybe you'll surprise me. I'll be keeping an eye on you."

## 4 Hearts -- Forge Day

Source: `march_four_hearts.c.toml`

Location: the blacksmith forge. Olric starts the scene, explaining they are overwhelmed with orders. March arrives from negotiating with Balor for iron ingots.

Olric sets up the scene:
- Olric [neutral]: "March is negotiating with Balor for more iron ingots, so I'm getting everything tidy."
- Olric [neutral]: "With the bridge repaired, we don't have the same supply problems, but stuff is still like, way expensive after the earthquake."
- Olric [happy]: "So we gotta make the things the town needs right here!"

March arrives and objects to the player's presence:
- March [unimpressed]: "[Ari], what do you think you're doing here, exactly?"
- Olric [sad] [effect: drop]: "March! [Ari] heard how backed up we were and uh... volunteered to help out! Right, buddy?"
- March [ugh]: "Fine! Fine. But you'd better be able to keep up."

Working together at the forge:
- March [think]: "[Ari], let's get started! Get that forge fired up!"
- March [neutral]: "Keep the temperature steady! Steady... good."

After completing the work:
- March [happy]: "Y-yeah!"
- March [embarrassed] [effect: surprise]: "..."
- March [tsundere]: "I mean... thanks, [Ari]."
- March [unimpressed]: "I'm going inside, I need to cool down."

Follow-ups:
- Olric [think]: "Seems like you and March make a pretty good team! I hope we can count on you in the future."
- Balor [think]: "When I pointed out that I couldn't have gotten them their shipment without all the work you did repairing the bridge, March got a bit flustered."
- Landen [happy]: "We've got the nails we need and didn't have to pay inflated Capital prices on them, I can't thank you enough!"

Writes: `march_heart_event = "four_heart"` (expires 4d)

## 6 Hearts -- Shield of the Realm

Source: `march_six_hearts.c.toml`

Location: the blacksmith forge. March and Olric are discussing an overloaded schedule. March calls the player over for help.

- Olric [happy]: "You asked [Ari] for help? That's so smart of you, March!"
- March [ugh]: "I-It sped things along last time, so..."

Adeline arrives with a special commission:
- Adeline [neutral]: "My mother, Baroness Linnet, was just awarded the Shield of the Realm award for her services to the king!"
- Adeline [neutral]: "Better yet, she's requested that the shield itself be made here in Mistria!"
- March [embarrassed]: "So she wants me to make it?"
- March [happy]: "Really? That's... that's great!"

Problem: the letter was delayed, so the shield must be finished today.
- March [sad]: "Adeline, you know how much it'd mean to me to craft this shield, but-"

The player volunteers. March and the player work on the shield together. Physical contact during the crafting:
- March [think]: "Give me your hand. Like this, see?"
- March [neutral]: "Hold your fingers out of the way and keep the pressure even."
- Player choice: "March, you can let go of my hand now..." -> March [tsundere]: "Ah... s-sorry."

After completing the shield:
- Adeline [wink]: "[Ari], March, thank you. You two have done something incredible."
- March [ugh]: "I could have handled it myself any other day, you know."
- March [tsundere]: "You just happened to be in the right place at the right time."

Follow-ups:
- Olric [think]: "He always talks about wanting to make his mark as a blacksmith with bigger projects like this."
- Olric [embarrassed]: "M-maybe he's just not used to sharing credit?"
- Ryis [happy]: "More importantly, look at you! Just think about your work being shown off in the Capital!"

Writes: `march_heart_event = "six_heart"` (expires 4d)

## 8 Hearts -- The Mines Collapse

Source: `march_eight_hearts.c.toml`

Location: the forge, then deep in the mines. Two-part scene. The file contains both the setup at the forge and the rescue in the mines.

**Part 1 -- At the forge:**

Olric and March close up for the day. March says he plans to visit the player's farm:
- March [think]: "I think I might head over to [farm_name]."
- March [tsundere/neutral]: "There's something I've been meaning to talk to [Ari] about..." (portrait branches on whether the player attended the Shooting Star Festival with March)

Adeline arrives with a second special commission:
- Adeline [embarrassed]: "My father, Baron Wiscar, has been awarded the $Gold Dragon Crest$ in recognition of his service as Advisor to the King!"
- Adeline [evasive_tired]: "The last time the King issued a $Gold Dragon Crest$, it was your mother who crafted it, and..."
- March [mad_special]: "No. I'll make it."
- Olric [embarrassed]: "Mom would be super proud."

March refuses help:
- March [mad_special]: "I don't need any help!"
- Olric [think]: "But... we don't have enough $Gold Ore$ for a project like this, bro."
- Olric [sad]: "And it's only found deep in the Mines."

**Part 2 -- Olric comes to the player the next morning:**

- Olric [sad]: "I-Is March here? He didn't come home last night."
- Olric [sad]: "He mentioned he had something he wanted to talk to you about before he left last night..."

**Part 3 -- The player finds March in the mines, injured:**

- March [hurt_shock]: "[Ari]...?"
- March [hurt_mad]: "Are you okay, [Ari]?"
- March [hurt_sad]: "You're not hurt, are you?"
- March [hurt_mad]: "Don't scare me like that!"

March explains what happened:
- March [hurt_tsundere]: "I came here looking for ore..."
- March [hurt_mad]: "But then the ground collapsed without warning."
- March [hurt_sad_special]: "I landed pretty hard, I guess."

The player warms March up (branching portraits based on Shooting Star Festival attendance):
- March [hurt_think]: "Why did you come looking for me, [Ari]? Now you're trapped here, too."
- Player: "Because I care about you, March!" / "Because I don't want anything bad to happen to you!"

March and the player sleep through the night trapped together. March shares forage he found. Then he opens up about his parents:
- March [hurt_think]: "Her name was Jade. She was a master blacksmith from the Capital."
- March [hurt_sad_special]: "And my Dad, Olin... He was a merchant that traded goods overseas."
- March [hurt_mad]: "They saw the potential in these Mines, so they moved to Mistria to start their own business."
- March [hurt_think]: "Mom would turn raw materials from the Mines into all sorts of showpieces."
- March [hurt_sad_special]: "And then Dad would find buyers through his network of customers."
- March [hurt_mad]: "One day, they sailed west to make a shipment... and never returned."
- March [hurt_sad_special]: "I know that they didn't really abandon me and Olric."
- March [hurt_think]: "I know that their ship was lost during a storm. That they didn't survive."
- March [hurt_mad]: "But I can't help that I'm still angry at them for leaving us!"
- March [hurt_think]: "I guess part of me always wanted to prove that I didn't need them..."
- March [hurt_closed_eyes]: "That I didn't need anyone."

Critical branching:
- "I did mean it. You're my best friend, March." -> best_friend status. March [hurt_tsundere]: "I've been wanting to tell you... you're my best friend, too." / "I've been wanting to tell you that you're my best friend, too."
- "I do care about you. More than anyone..." -> dating status. March [hurt_blush]: "I want to be with you, [Ari]." Player: "I want to be with you, too." / "(Kiss him)"

Both paths include apology:
- March [hurt_sad_special]: "And I'm sorry that I've been such a jerk."
- March [hurt_think]: "I was wrong to give you such a hard time when you just moved to Mistria."
- March [hurt_tsundere]: "I hope that you can forgive me."

Errol and Olric rescue them:
- Olric [happy]: "Hang tight. We're coming to get you!"
- March sees the player found the gold ore: March [hurt_happy_blush/hurt_happy]: "Thank you, [Ari]."

Follow-ups:
- Adeline [sigh]: "I never expected he would run off to get the ore for the $Gold Dragon Crest$ by himself."
- Valen [mad]: "He could have gotten hypothermia if you hadn't known what to do."
- Olric [think]: "Doctor Valen said it was lucky you found March when you did."
- Romantic follow-up -- March [tsundere]: "Do you want to take a break with me...?"
- Best friend follow-up -- March [sigh]: "Olric said that since we're best friends now, that means he's your best-friend-in-law."

Writes: `march_heart_event = "eight_heart"`, `march_eight_heart_priority_bump = true` (both expire 4d)

## 10 Hearts -- Proposal and the Mistrian Shield

Source: `march_ten_hearts.c.toml`

Location: the Summit. Triggered by engagement ring. March suggests the Summit.

- March [eight_heart_happy]: "Wow, it's so nice up here..."
- March [tsundere]: "Maybe we should make an effort to hike up to the Summit more often."
- March [eight_heart_happy]: "Looking out over the town with you, everything seems more..."
- March [tsundere]: "Well, more beautiful than before."

March reflects on the player:
- March [eight_heart_flustered]: "There's just something about you, [Ari]."
- March [eight_heart_flustered]: "You make me see things differently than I used to. I wouldn't have guessed that was possible, back when we first met."

Player choice branches:
- "Back then, I hoped one day you might one day see me differently, too..." -> March [tsundere]: "I uh... I always noticed certain things about you. Even if I didn't care to mention them at the time." March [eight_heart_flustered]: "The way your eyes light up when you smile. The way your cheeks flush near the heat of the forge..." March [tsundere]: "Your unwavering persistence in the face of, er... stubbornness."
- "When we first met, I wouldn't have thought it possible either..." -> Same sequence with slightly different lead-in.

March reflects on his emotional arc:
- March [sad_special]: "I don't know what compelled you to give me a second chance back then-"
- March [tsundere]: "Or a third, or a fourth..."
- March [sad_special]: "My heart was closed off, when you first arrived."
- March [eight_heart_think]: "It had been, for a long time already."
- March [eight_heart_blush]: "I didn't like the thought of anything, anyone breaking through."
- March [eight_heart_flustered]: "But you just kept chipping away. With each hello, with each smile."
- March [eight_heart_happy_blush]: "Until before I knew it... You'd changed me."

March struggles to open up:
- March [eight_heart_think]: "It's still not easy for me to open up, you know."
- March [tsundere]: "There are times I have to fight myself, to keep myself from pushing you away."
- March [eight_heart_blush]: "Not because I don't want you-"
- March [eight_heart_flustered]: "But because of how intensely I DO want you."
- March [eight_heart_blush]: "I want you here by my side, always. I want to see your smile..."
- March [eight_heart_happy_blush]: "And I want to protect you from anything that might threaten to make it disappear."

The Mistrian Shield gift (branches on first vs. repeat viewing):
- First: "But first, there's something I want to give you. Something I put my heart into forging for you." "I call it the $Mistrian Shield$." "It's my promise to you. To protect you, and your happiness, no matter what."
- Repeat: "That's why I crafted the $Mistrian Shield$ for you." "It represents my promise..." "To protect you, and your happiness, no matter what."

March tries to propose but stumbles:
- March [super_flustered]: "[Ari], I wanted to ask you-"
- March [eight_heart_blush]: "To ask if you would-"
- March [tsundere]: "I mean, will... will you......?"

Acceptance:
- Player: "I love you, March. Of course I'll marry you!"
- March [super_flustered]: "You will?"
- March [drunk]: "You'll marry me?"
- March [eight_heart_happy_blush]: "You're serious? You're not just teasing me, right?"
- March [drunk]: "I love you, [Ari]!"
- March [super_flustered]: "I thought so much about how I was going to ask you, the whole time I was working on your $Mistrian Shield$..."
- March [tsundere]: "And I thought about a hundred different ways you might say 'no'."
- March [eight_heart_happy_blush]: "But now it seems ridiculous that I was ever afraid. E-even if it was hard to get the words out."
- March [drunk]: "I'm going to marry you, [Ari]! You're mine! I'm so happy!"

Decline paths available at two points, both deferrals rather than rejections.

Writes on acceptance: breakup_bump (3d), engagement_bump (2d), engagement_delay (20h), engagement_cap = false (3d)

## Wedding Ceremony

Source: `Custom Wedding Parts/wedding_march.c.toml`

Three parts: ceremony, speech, arrival at home.

**Ceremony (wedding_march_0):**

- March [embarrassed]: "[Ari]... You look..."
- March [eight_heart_happy_blush]: "You look incredible."
- March [think]: "I had a hard time remembering which way I comb my hair... Er."
- March [tsundere]: "Seeing you all dressed up like this... it's kind of unfair."
- March [eight_heart_blush]: "You're taking my breath away."

Elsie officiates:
- Elsie [wink]: "I do so hate to interrupt March's flirting, but if you two are ready... shall we begin the ceremony?"
- Elsie [neutral]: "Welcome, one and all. We are gathered here today to celebrate the union of March and [Ari], as they join their light in matrimony."
- Elsie [neutral]: "Brilliant sparks, cast into the world by the strike of eternity's hammer."

Candle lighting:
- March [sincere_special]: "[Ari]..."
- March [eight_heart_blush]: "Your light. It's... beautiful."

March's vows:
- March [sincere_special]: "[Ari]. The flame in my heart burns only for you."
- March [neutral]: "I promise to offer you my light when the day is dark."
- March [embarrassed]: "To share my warmth when the day is cold."
- March [eight_heart_flustered]: "To forge our future together, side by side."
- March [mad]: "And to love you fiercely, for all my days."

Player vow choices:
- "I love you, March. You are everything to me." -> March [embarrassed]: "I love you too, [Ari]."
- "I love you, March. I promise that I'll always stay by your side." -> March [teary]: "I love you too."

**Speech (wedding_march_1):**

Olric gives the toast:
- Olric [neutral]: "March, you're the best brother a guy could ask for."
- Olric [happy]: "It's been an honor to watch you grow up and stuff..."
- Olric [embarrassed]: "And now, seeing you move on to this next stage of your life... I'm super proud of you."
- Olric [sad]: "My one and only little bro..."
- Olric [mad] [effect: sparkles]: "Then [he/she/they]'re officially my bro, too!"
- Olric [happy]: "I'm totally gaining another one! Cool!"

**Arrival at home (wedding_march_2):**

- March [drunk]: "What an amazing night!"
- March [embarrassed]: "I can hardly believe it. We really did it. We got married!"
- March [eight_heart_flustered]: "It's strange to think I'll be living here now, too..."
- March [eight_heart_happy_blush]: "A home of my own, a family of my own."
- March [teary]: "I'm... I'm really happy, [Ari]"

## Source Absences

- No pre-game backstory scenes (childhood with Olric after parents' death, how they managed the forge)
- No scenes showing March's relationship with the broader town outside the forge context
- Children cutscenes exist (player_delivery_march, great_bird_1_march) but are not extracted here as they are post-marriage content
- Heart events reference the Shooting Star Festival as a branching condition but the festival scene itself is not in these files
- No detail on the Gold Dragon Crest crafting process after the ore is recovered
