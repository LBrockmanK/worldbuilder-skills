---
type: reference
title: Valen — Heart Events and Narrative Arc
description: 'Extracted dialogue and scene content from Valen''s 5 heart event cutscenes
  (2/4/6/8/10 hearts), wedding scene, and ancestral medical journal thread: panacea
  research arc, Juniper rivalry, romantic progression.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:22Z
resources:
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Valen/valen_two_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Valen/valen_four_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Valen/valen_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Valen/valen_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Valen/valen_ten_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_valen.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Threads/Valen/ancestral_medical_journal.c.toml
---

# Valen — Heart Events and Narrative Arc

Source: `source/t2/Cutscenes/Heart Events/Valen/`, `source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/`, `source/t2/Conversations/Threads/Valen/`

## 2 Hearts — Hayden's Twisted Ankle

Source: `valen_two_hearts.c.toml`

Location: clinic. Participants: Valen, Hayden, player. Kind: gameplay_triggered.

Hayden has twisted his ankle tripping over a sack of grain and fears the worst. Valen diagnoses a twisted ankle and prescribes two weeks off the foot.

Key dialogue:
- Hayden [ugh]: "Don't sugarcoat it, Valen! You're gonna have to take off the foot, I just know it!"
- Valen [raised_eyebrow]: "You twisted your ankle tripping over a sack of grain, Hayden."
- Valen [neutral]: "Keep off that foot for two weeks... I'll come check up on you, and we can go from there."
- Hayden [sad] [effect: sick]: "And then I'll starve to death... and my poor, dear chicken Henrietta... she'll have to arrange the funeral herself, and..."
- Valen [mad]: "Oh, hush, Hayden. You should have said as much earlier."

Valen sends the player to the basement to fetch a scoop from a barrel. Valen applies the substance to Hayden, curing him instantly.

- Hayden [happy]: "I'm CURED! You're a miracle worker, Doctor!"
- Valen [raised_eyebrow]: "Don't run, Hayden! Stay hydrated! Make sure you get plenty of rest!"

Valen then gives the player a checkup, declaring clean bill of health.

- Valen [raised_eyebrow]: "Anything else you'd like to ask me? Don't hesitate, patient confidentiality is part of a doctor's code."

Player choice:
- "What's with the creepy basement?" / "What was that powder in the barrel? Can I have some?" --> Both lead to Valen [mad]: "Is there anything about your personal health you'd like to ask me about?" (deflects the question)

## 4 Hearts — The Panacea Secret

Source: `valen_four_hearts.c.toml`

Location: clinic, then basement laboratory. Kind: gameplay_triggered. Triggered by turning in a request (peat).

- Valen [think]: "I think two hundred tesserae is fitting for such high quality peat. Thank you again, [Ari]."

Player choice:
- "What are you going to use it for?" --> Valen [raised_eyebrow]: "An experiment on the nature of the bacteria in this soil."
- "Hey, can I see your creepy basement again?" --> Valen [ugh]: "I-it's not creepy!"

Valen invites the player to see the laboratory.

- Valen [happy]: "My family have been doctors for generations, this is our laboratory. Over the years, my ancestors made many contributions to the science of medicine."
- Valen [neutral]: "One of whom invented the panacea I used to instantly cure Hayden's ankle."
- Valen [raised_eyebrow]: "She made a stockpile of it that my family has been using over the years only when there's been a real need for it."
- Valen [neutral]: "I've made it my life's work to recreate the recipe, which has been lost to time. I think I'm getting close..."

Valen asks the player to keep the secret.

- Valen [mad]: "I'm telling you this because I think I can trust you with this secret, [Ari]. I can trust you, yes?"

Player choice:
- "Your secret is safe with me." --> Valen [neutral]: "Thank you [Ari], it means a lot to me that I can trust you."
- "You wouldn't believe the secrets I'm already keeping!" --> Valen [think]: "Interesting, I didn't think this sleepy little town had any juicy secrets!"

Valen introduces batch 312, described as "more volatile than my previous batches." Asks the player to take notes during testing in case Valen becomes incapacitated.

Player choice:
- "Then let me drink it, for science!" --> Valen [think] [effect: surprise]: "I've never had a volunteer before, that's very generous of you."
- "Can I drink it? It looks really tasty..." --> Valen [embarrassed]: "Do you think so? I uh, didn't concern myself with the elixir's taste or appearance."

The player drinks the batch. Valen [ugh]: "Oh dear." The player loses consciousness. When they come to:

Player choice:
- "I saw my life flash before my eyes..." --> Valen [sad]: "I'm sorry, [Ari]."
- "I feel great!" --> Valen [neutral]: "I should hope so, I used the last of the panacea on you after the test batch didn't work out."

- Valen [think]: "I've wanted to keep my work secret until I was successful, but with the last of the panacea gone, this has become more urgent..."
- Valen [sad]: "I promise not to risk harming your health again."
- Valen [neutral]: "I'm going to collect all my notes together and try to narrow down what's gone wrong. I'll let you know when it's time to start mixing up the next test batch."

## 6 Hearts — Consulting Juniper

Source: `valen_six_hearts.c.toml`

Location: Juniper's place. Participants: Valen, Juniper, Dozy, player. Kind: gameplay_triggered. State writes: `valen_heart_event = "six_heart"` (expires 4d).

Valen brings notes to Juniper for review.

- Valen [neutral]: "Juniper, thank you for agreeing to this meeting."
- Juniper [sly]: "After all, I haven't had a good laugh in ages."
- Juniper [neutral]: "Let's see these 'notes' of yours."
- Juniper [happy]: "What unique handwriting!"
- Juniper [unimpressed]: "Shame the content is drivel. You've made no real progress on the missing key ingredient, have you?"
- Valen [mad]: "Do you have insight that you'd care to share, or is this just your usual badmouthing?"
- Juniper [neutral]: "You would have better luck focusing on a smaller problem, something more suited to your skill level. Wart removal, perhaps?"

Player choice:
- "Valen's worked hard and made a lot of progress." / "Hey, don't be a jerk." --> Both lead to:
- Juniper [mad]: "Why Valen, your test subject speaks! Good to know your reckless experiments didn't do any permanent damage."
- Valen [mad]: "[Ari] is a valued colleague and friend. We are both here because we recognize the importance of this research."

Juniper agrees to help:
- Juniper [angry_brows]: "Very well, you have my support. Just don't expect me to do all the work."
- Juniper [mad]: "The herb you're looking for is colloquially known as Cliffblossom. I believe you can find it growing at the Western Ruins."
- Valen [mad]: "You figured that out by just... glancing at my notes?"
- Juniper [wink]: "Humbling isn't it? And you're welcome, by the way."

After Juniper leaves:
- Valen [ugh]: "Honestly, that went better than I expected."
- Dozy [neutral]: "(Dozy appears to be agreeing with Valen.)"
- Valen [embarrassed]: "It... means a lot to me. I don't think I could have done this by myself."

**Follow-ups** (refresh: never, require `valen_heart_event = "six_heart"`):
- Dozy [neutral]: "(You're not quite sure, but Dozy seems to be giving the impression that Juniper really enjoyed having Valen and you over.)"
- Juniper: does not think she did anything needing forgiveness. "Oh ho ho!"
- Valen [think]: "As much as I hate to admit it, I can see why I missed Cliffblossom as a lead." / [neutral]: "It goes by several different regional names, and is regarded as a weed with no medicinal properties." / [ugh]: "If only Juniper would use her knowledge for the general good."

## 8 Hearts — Finding the Cliffblossom

Source: `valen_eight_hearts.c.toml`

Location: Western Ruins. Kind: gameplay_triggered. State writes: `valen_heart_event = "eight_heart"` (expires 4d), `valen_eight_heart_priority_bump = true` (expires 4d).

Valen has been visiting the ruins regularly searching for Cliffblossom without luck. Has also asked Eiland and Errol to watch for it.

- Valen [happy]: "We'll want to look for a pink flower, with four petals."
- Valen [happy]: "It's a bit like something out of a mystery novel, isn't it?"

After searching fails:
- Valen [sad]: "Research is all about persistence. I suppose we'll just have to come back another time."

Player choice:
- "Why don't we check the ruins themselves?" --> Valen [think]: "Hmm... despite the name of the plant, I suppose we were simply told the 'Western Ruins', weren't we?"
- "But I want to spend more time with you." --> Branches based on `shooting_star_valen_attended`:
  - If true: Valen [neutral_blush]: "I'd... I'd like that as well."
  - If false: Valen [happy]: "I'd like that as well."

They spot a Cliffblossom out of reach. Valen climbs a ladder, retrieves it. The stonework collapses and the player is hit.

- Valen [panic] [effect: shock]: "[Ari]!"
- Valen [sad]: "Please, hold on just a little longer, [Ari]. This panacea must work... I'll stake my life on it!"
- Valen [think]: "There's no getting around it, I'll have to test it on myself."
- Valen [teary]: "It has to work... it just has to."
- Valen [sad]: "Come on, Doc. Get it together!"
- Valen [panic]: "It works!"
- Valen [teary]: "Hold on, I'm coming, [Ari]!"

After healing the player:
- Valen [neutral]: "Thankfully, I just used a fresh batch of panacea to heal you."

Valen asks why the player jumped in the way.

**Critical branching:**
- "Because you're my best friend!" --> `update_status: best_friend`
  - Valen [neutral]: "I couldn't ask for a better best friend."
  - Valen [sad]: "No more putting yourself in danger for my sake."
- "Because I care about you... more than anyone!" --> `update_status: dating`
  - Valen [embarrassed]: "Oh! [Ari]... do you mean it?"
  - Branches on `shooting_star_valen_attended`:
    - If true: Valen [think_blush]: "I have been wondering if you felt the same since our evening together under the stars..."
    - If false: Valen [think_blush]: "I care about you too. I didn't realize you felt the same way."
  - Valen [happy_blush]: "I'm so happy!"

Both paths converge:
- Valen [happy]: "I can't thank you enough for everything you've done, [Ari]."
- Valen (blush variant if shooting_star attended): "I feel that I can finally rest easy..."
- Valen: "Knowing that we can protect the people of Mistria... together."

**Follow-ups** (refresh: never, require `valen_heart_event = "eight_heart"`):
- Balor: "She put me on the hunt as well, but all I could learn about it was that it was rare, finicky, and doesn't travel well."
- Celine: "Valen told me all about your adventures finding a Cliffblossom! You're both so brave!"
- Eiland [surprised]: "So you and Valen found the Cliffblossom? Incredible work!"
- Errol (requires `valen_eight_heart_priority_bump`): "Valen told me about what happened, I'm relieved you're alright, [Ari]." / "Eiland and I have already cleaned the site and repaired the damage to the wall."
- Juniper: "Please extend my congratulations to you and Valen on finding the last ingredient for her little poultice."
- Valen (best_friend path, requires `valen_eight_heart_priority_bump`): "I feel such a sense of relief, now that we have recovered the panacea's recipe." / "Now I just need to figure out why it loses its effectiveness if it's taken outside of Mistria..."
- Valen (romantic path, requires `valen_eight_heart_priority_bump`, action: bark heart): Same relief dialogue, then [neutral_blush]: "I suppose it's another mystery for us to unravel."

## 10 Hearts — Proposal

Source: `valen_ten_hearts.c.toml`

Location: Western Ruins. Kind: gameplay_triggered. Triggered by engagement ring.

Pre-scene:
- Valen [neutral]: "You have a pensive look, [Ari]."
- Valen [think_smile]: "I have time, and I wouldn't mind a walk in the Western Ruins."

Main scene:
- Valen [neutral_blush]: "Walking around these ruins always reminds me of you, and the time we went searching for the Cliffblossom together."
- Valen [think]: "I suppose I've never articulated this, but... there aren't many people I can turn to for help."
- Valen [sincere_special]: "I'm a doctor, and the townsfolk are my patients."
- Valen [sad]: "As a professional, it stands to reason that I try not to speak much about my own troubles."
- Valen [neutral]: "That line of thinking began at my practice, but eventually it appeared in most facets of my life."
- Valen [think]: "And over time I simply... got used to thinking that way. Perhaps I even began to prefer it."
- Valen [embarrassed]: "I took it as a fact of life, that I had to do things alone... until you walked into my Clinic."

Player choice:
- "What did you even think of me, walking in straight from my work in the fields?" --> Valen [happy_blush]: "That you were awfully cute, with that smudge of dirt on your cheek and the sweat on your brow."
- "I'm glad I came in for a checkup that day." --> Valen [happy_blush]: "Me too."

- Valen [sad]: "When we first met, rediscovering the formula for the Panacea was weighing on me every day."
- Valen [think]: "My research was a secret. My own burden to bear."
- Valen [raised_eyebrow]: "But you surprised me. You assisted me with Hayden, helped me handle Juniper, and joined me in the search for the elusive Cliffblossom."
- Valen [neutral]: "You made it so easy to ask for help. Sometimes, I didn't even need to ask."
- Valen [think]: "Don't misunderstand, I like that I can depend on myself."
- Valen [neutral]: "But being self-sufficient doesn't need to mean... being alone."

Panacea Jar gift (branches on whether scene has been seen before):
- First time: Valen [think_smile]: "Which reminds me... I have something for you. It's a Panacea Jar."
- Repeat: Valen [think_smile]: "That's why I gave you the Panacea Jar."
- Valen [neutral]: "The Panacea is still quite rare, but I want you to always have some on hand."
- Valen [think_blush]: "So you'll always be safe. That's important to me."
- Valen [think]: "I care for all the townsfolk, but..."
- Valen [embarrassed]: "It's different, with you."
- Valen [think_blush]: "I suppose I am, ah... more personally invested in your well-being."
- Valen [happy] [effect: drop]: "Sorry... I don't know what's gotten into me today."
- Valen [embarrassed]: "I'm not usually one to be so talkative, nor to have so much trouble with my words..."

Player choice:
- "I wanted to talk to you about our future together..." -->
  - "I love you, Valen. Will you marry me?" -->
    - State writes: breakup_bump (3d), engagement_bump (2d), engagement_delay (20h), engagement_cap = false (3d). Action: can_talk valen.
    - Valen [embarrassed] [effect: surprise]: "..."
    - Valen [teary]: "You want to... marry me?"
    - Valen [happy_blush]: "Yes! Of course I will!"
    - Valen [caring_special]: "There's nothing I want more."
    - Valen [happy_blush]: "I'm so happy I can hardly think straight!"
    - Valen [embarrassed]: "I love you, [Ari]!"
    - Valen [happy_blush]: "I love you so much!"
  - "Actually, let's talk about it more another day." --> deferred
- "Let's talk about it another time..." --> Valen [happy]: "Come find me whenever you'd like to talk. I'm always here for you."

## Wedding

Source: `wedding_valen.c.toml`

3 scenes: ceremony, reception, post-wedding.

**Ceremony (wedding_valen_0):**
- Valen [happy_blush]: "[Ari], can you believe it? Our big day is finally here!"
- Valen [embarrassed]: "You look fantastic..."

Player choice:
- "Do you like my outfit?" --> Valen [happy_blush]: "Very much so." / Valen [caring_special]: "Although I personally think you look good in anything..."
- "Love the suit, Valen." --> Valen [happy_blush]: "You do? Me too." / Valen [embarrassed]: "It's nice to get dressed up, sometimes."

Elsie officiates. Ceremony text:
- Elsie [neutral]: "Welcome, one and all. We are gathered here today to celebrate the union of Valen and [Ari], as they join their light in matrimony."
- Elsie [closed_eyes]: "Two radiant souls-"
- Elsie [neutral]: "Beacons of hope and generosity, offering care and assistance to all who may need it."
- Elsie [embarrassed]: "Shining their light as one, destined to live this life together in the service of a greater good."

Candle lighting:
- Valen [happy_blush]: "Your light... It's incredible! It feels so warm..."

Valen's vows:
- Valen [think]: "You've brought me light and hope on even the darkest of days..."
- Valen [embarrassed]: "Times at which it would have been easier for me to give up than to push forward."
- Valen [teary]: "I have never met anyone as selfless, caring, and brave as you. You are my everything."

**Reception (wedding_valen_1):**
Hayden gives the toast, introduced as "Valen's oldest friend."
- Hayden [neutral_fist]: "There isn't a soul in town who hasn't been helped by our doctor."
- Hayden [think]: "She's certainly saved my skin more times than I can count!"
- Hayden [neutral_arm_down]: "Why, I'd say you two are a perfect match."

**Post-wedding (wedding_valen_2):**
- Valen [neutral]: "I never thought I could be so happy."
- Valen [embarrassed]: "It seems that all my dreams have come true..."
- Valen [caring_special]: "Well, shall we head inside?"

## Ancestral Medical Journal (Thread)

Source: `Conversations/Threads/Valen/ancestral_medical_journal.c.toml`

3-part conversation thread. Requires: heart level >= 3 and < 8. Refresh: part 1 yearly, parts 2-3 instantly (sequential unlock via thread_mutex). Writes `valen_ancestral_medical_journal_finished = true` on completion.

**Part 1:**
- Valen: "My family has a long tradition of keeping records of various medical cases, for the benefit of future generations of doctors."
- Valen [think]: "Some journal entries are rather outlandish, listen to this:"
- Valen [raised_eyebrow]: "'Punmania, a most grievous affliction that causes the victim to uncontrollably spout wordplay of a most disagreeable variety.' Ridiculous!"
- Valen [mad]: "Wait."
- Valen [happy] [effect: drop]: "I need to talk to Holt."

**Part 2:**
- Valen: "I came upon another case record from my great great grandmother, a respected physician in her time..."
- Valen [mad]: "But the case itself seems a little light on the science. A disease that causes 'churlish behavior disruptive to family and society'."
- Valen [think] [effect: drop]: "I should pay March a visit..."

**Part 3:**
- Valen: "I've been combing over some of the old family medical journals and found another oddity..."
- Valen [think]: "My great grandmother describes a type of laughing sickness..."
- Valen [mad]: "'Wherein one laughs uncontrollably, at a high, piercing volume, as though with their entire being and in a manner that spreads malaise in the receiver'."
- Valen [ugh]: "Now this one definitely feels familiar... I wonder why."

**Follow-up reactions from other NPCs:**
- Holt (requires thread_mutex part 1): "Valen came by earlier and asked me a laundry list of questions about my puns..." / "Do you suppose the doctor is working on her sense of humor, [Ari]?"
- March (requires thread_mutex part 2): "Valen came by and asked me how often I engage in 'uncivil' and 'surly' behavior. Then she wrote a bunch of notes..." / "Uncivil? There's no one more civil than me!"
- Juniper (requires journal finished + same day): "Valen spoke to me earlier... she seemed fixated on my laugh."
  - "Do you laugh like that to annoy Valen?" --> Juniper [think]: "Wouldn't you like to know." / Juniper [laugh]: "OH HO HO HO!"
  - "Valen thinks you might be afflicted with laughing sickness..." --> Juniper [happy]: "Oh, was she concerned?" / Juniper [wild_laugh]: "OH HO HO HO!"

## Source Absences

- No pre-arrival backstory for Valen (how she came to run the clinic, what happened to her father)
- No scenes showing Valen's daily medical practice or routine outside the panacea arc
- The panacea's limitation (loses effectiveness outside Mistria) is mentioned in a follow-up line but not explored in any heart event
- No detail on Valen's time studying in the Capital (mentioned in group conversations but not in heart events)
