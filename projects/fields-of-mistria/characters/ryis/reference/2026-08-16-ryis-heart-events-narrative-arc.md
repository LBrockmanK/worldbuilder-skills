---
type: reference
title: Ryis — Heart Events Narrative Arc
description: 'Extracted dialogue and scene content from Ryis''s 5 heart event cutscenes
  (2/4/6/8/10 hearts) and wedding: birdhouse restoration arc, belonging theme, romantic
  progression.'
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T13:15Z
resources:
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Ryis/ryis_two_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Ryis/ryis_four_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Ryis/ryis_six_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Ryis/ryis_eight_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Ryis/ryis_ten_hearts.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/wedding_ryis.c.toml
---

# Ryis — Heart Events Narrative Arc

Source: `source/t2/Cutscenes/Heart Events/Ryis/` and `source/t2/Cutscenes/Heart Events/Wedding/Custom Wedding Parts/`

## 2 Hearts — The Old Birdhouse

Source: `ryis_two_hearts.c.toml`

Location: Landen's woodshop, then cottage ruins south of the shop. Triggered when the player delivers wood for Landen's request. Landen pays 150 tesserae and sends the player to find Ryis on his break.

Key dialogue:
- Ryis [neutral]: "[Ari]! This is a surprise."
- Ryis [neutral]: "Oh, you fulfilled Uncle Landen's request! You're a lifesaver [Ari]. Now we can finish up a commission that's been on hold."
- Ryis [think]: "Before the earthquake there was a tree here, with an old birdhouse in it. The birds that lived there had the prettiest songs."
- Ryis [sad]: "'Course, the earthquake took the tree down and smashed the birdhouse. Pretty sure the birds got away safely though."
- Ryis [think]: "I should really get around to setting up a new birdhouse for them... though it feels a bit silly when I've got so much work to do around Mistria as it is!"

Player choices encourage him. He asks the player to help with the birdhouse project.

- Ryis [happy]: "You know what, you're right [Ari]. It'd be a fun project! I hope I can count on your help?"

Branching:
- "What a pretty spot." → Ryis: "Isn't it? I come here to relax."
- "What were these ruins of?" → Ryis: "Eiland thinks it was someone's house a long time ago, but I just think it's relaxing being out here."

## 4 Hearts — The Hawthorn Tree

Source: `ryis_four_hearts.c.toml`

Location: Ryis's room. He has researched the birds using a book on Aldarian birds.

Key dialogue:
- Ryis [neutral]: "Welcome to my room. Sorry it's a bit cramped, I tend to bring my work upstairs with me..."
- Ryis [think]: "So according to my big book of Aldarian birds, we're dealing with a Mistrian bluebird!"
- Ryis [happy]: "Most notably, they're quite the singers!"
- Ryis [think]: "They're not picky nesters, but they seem to prefer hawthorn trees."
- Ryis [neutral]: "So what if we grew a hawthorn to put their new birdhouse in?"

Balor arrives with a hawthorn sapling he procured. They plant the sapling together.

- Balor [wink]: "You've brought [Ari] in on your project as well? I can see you want to do this right."

Player choices about helping the tree grow:
- "Check on it every day!" → Ryis [happy]: "Works for me!"
- "Give the tree compliments every day!" → Ryis [think]: "Hey uh, tree... those are some healthy looking... leaves?" → Ryis [embarrassed]: "I'll keep practicing..."

## 6 Hearts — Building the Birdhouse

Source: `ryis_six_hearts.c.toml`

Location: Landen's woodshop, then cottage ruins. State write: `ryis_heart_event = "six_heart"`, expires 4 days.

Opens with Landen and Ryis debating tool belts. Landen volunteers to take over Ryis's shop shift.

Key dialogue:
- Ryis [happy]: "This is exciting, isn't it? I've been laying aside materials for the project while we've been waiting for the tree to grow big enough."
- Ryis [neutral]: "I like working on the big town projects with you, but there's something nice about collaborating on something small, right?"

Player choice:
- "It'll be fun to get the details just so!" → Ryis [wink]: "You get it!"
- "Yeah, it's more intimate." → Ryis [embarrassed]: "Y-yeah..."

They build the birdhouse. Landen comments on the result.

- Landen [happy]: "Well now! That house is much too fine for a bird!"
- Ryis [wink]: "We might have gotten a little carried away."

Landen offers to make Coconut Cream Pie while they hang the birdhouse.

- Ryis [think]: "Feels good and secure to me."
- Ryis [neutral]: "Those bluebirds are going to be SO surprised."
- Ryis [happy]: "But for right now, I think it's time for pie!"
- Ryis [wink]: "Come on, we'd better get back before Uncle Landen decides he's tired of waiting."

## 8 Hearts — The Bluebirds Return

Source: `ryis_eight_hearts.c.toml`

Location: cottage ruins / hawthorn tree site. State writes: `ryis_heart_event = "eight_heart"` and `ryis_eight_heart_priority_bump = true`, both expire 4 days. Dialogue branches based on whether the player attended the Shooting Star Festival with Ryis (`shooting_star_ryis_attended`).

Key dialogue:
- Ryis [happy]: "I was so excited when I spotted that blue feather by our tree!"
- Ryis [closed_eyes_smile_blush / closed_eyes_smile]: "I always thought it was my thing, but... it's really nice that it's our thing."

Ryis shares his backstory:
- Ryis [thoughtful]: "I grew up in a lively house..."
- Ryis [closed_eyes]: "So whenever I wanted some solitude, I'd go walking all over the Capital."
- Ryis [thoughtful]: "People-watching was fun, but observing the pigeons, starlings, and sparrows..."
- Ryis [neutral]: "It always made me feel calm and more connected to nature."
- Ryis [thoughtful]: "Working with wood and stone from the forest, the quiet focus required of the craft..."
- Ryis [happy_blush / happy]: "I guess I'm just drawn toward this kind of thing."

They wait and watch. A Mistrian bluebird appears in the birdhouse, already nesting. Ryis spots a clover-shaped marking.

- Ryis [surprised]: "I think it's the same bird that nested here before the earthquake!"
- Ryis [sad]: "But... I guess it's unrealistic to think her mate's still around, too..."
- Ryis [starry_eyed]: "[Ari]! Oh, wow... I'd recognize that plumage anywhere!"
- Ryis [happy_blush / happy]: "It's him! Her partner!"
- Ryis [starry_eyed]: "They did it, [Ari]. They found their way back to each other..."

Ryis reflects on belonging:
- Ryis [think]: "I've often wondered if I'd end up back in the Capital one day."
- Ryis [sincere_special]: "I wasn't sure if and when Mistria would really become \"home\" to me."
- Ryis [happy_blush / happy]: "And then one day, I realized... I've been on it the whole time."
- Ryis [thoughtful_blush / thoughtful]: "Mistria has become my home."

Critical branching:
- "What are best friends for?" → best_friend status. Ryis: "You're my best friend too, [Ari]." → "With a friend like you by my side... It's really no wonder that Mistria feels like home."
- "I've realized it too. We both belong here... together." → dating status. Ryis [starry_eyed]: "[Ari]... do you mean it?" → Ryis [happy_blush]: "I'm so happy that you feel the same way." → "Here with you, side by side... Where else could my home be?"

Follow-up conversations (NPC reactions, conditional on romantic/friend path):
- Errol [neutral/wink]: "Bringing back a local ecological niche all for a species of bird is quite admirable."
- Landen (romantic) [happy]: "You know, I don't ever think I've seen Ryis in such a good mood before."
- Landen (friend) [neutral]: "Ryis told me all about how you finally coaxed those bluebirds back to Mistria!"
- Ryis (romantic) [blush_special]: "Still can't believe we brought back the Mistrian Bluebirds..." → "Let's plan a birdwatching date sometime soon, okay [Ari]?"
- Ryis (friend) [neutral]: "Still can't believe we brought back the Mistrian Bluebirds." → "It makes me wonder what other rare birds are waiting to be found in Mistria!"
- Terithia [think]: "Landen never had any children of his own..." → "I'm sure you've noticed how he dotes on his nephew." → (romantic): "He's so happy that Ryis has found someone special in you, [Ari]." / (friend): "He's so happy that Ryis has made a friend as good as you, [Ari]."

## 10 Hearts — Proposal and the Potted Hawthorn

Source: `ryis_ten_hearts.c.toml`

Location: hawthorn tree site. Triggered by engagement ring. Ryis suggests visiting the tree.

- Ryis [happy]: "Sure, I have time to talk. For you, I always have time."
- Ryis [thoughtful]: "Why don't we go by the $Hawthorn Tree$? We can check in on it and have ourselves a chat."

Key dialogue:
- Ryis [happy]: "It's nice to see our tree looking so healthy. Our birdhouse is holding up well, too!"
- Ryis [think]: "If it weren't for you, these would still be empty ruins. No tree, no birdhouse..."
- Ryis [closed_eyes]: "The Mistrian Bluebirds would still be searching for \"home\". Maybe I'd still be searching, too."
- Ryis [embarrassed]: "You were helping me more than I realized."

Ryis reflects:
- Ryis [think]: "You know, [Ari]... You're really special."
- Ryis [embarrassed]: "Seriously! When we first met, I already knew there was something different about you."
- Ryis [happy]: "You saw me for me. Right from the get-go."
- Ryis [blush_special]: "And you keep seeing me."
- Ryis [neutral]: "You really helped me figure things out."
- Ryis [thoughtful_blush]: "And I feel confident in finally putting down my roots."

Gift (branches on first vs. repeat viewing):
- First: "I have something for you. It took a bit to grow, but it's finally ready." → "It's a $Potted Hawthorn Tree$, grown from a cutting of our big tree here." → "It's got a matching birdhouse too. So our Mistrian Bluebird family will have room to grow."
- Repeat: "That's why I wanted you to have that potted $Hawthorn Tree$." → "It's like a memento of what we did together."

Arc reflection:
- Ryis [blush_special]: "I came to Mistria thinking I'd be helping out Uncle Landen..."
- Ryis [closed_eyes_smile_blush]: "But together, we ended up helping the whole town."
- Ryis [starry_eyed]: "And we found our own sense of belonging in the process."
- Ryis [blush_special]: "I want to keep on putting my roots down here in Mistria. With you by my side."

Proposal:
- Ryis [closed_eyes_blush]: "Oh man, I'm having that dream again."
- Ryis [shocked]: "Wait, this is real?"
- Ryis [embarrassed]: "[Ari]... Yes!"
- Ryis [starry_eyed]: "YES!"
- Ryis [happy_blush]: "You just made me the happiest guy in the world, [Ari]! I love you so much!"
- Ryis [thoughtful_blush]: "What if we eloped? Right now? No... calm down, Ryis. [Ari] deserves a beautiful wedding."

State writes on acceptance: breakup_bump (3d), engagement_bump (2d), engagement_delay (20h), engagement_cap = false (3d).

Decline path: "Let's talk about it another time..." → Ryis [shocked]: "Oh... really?" → Ryis [neutral]: "That's cool. I can always make time to talk, okay?"

## Wedding

Source: `wedding_ryis.c.toml`

Three phases: ceremony, reception, post-reception.

**Ceremony:**
- Ryis [starry_eyed]: "You look amazing."
- Player choice "You look so dashing..." → Ryis [blush_special]: "I wanted to look good for you." → Ryis [embarrassed]: "I saw you, and my heart got wings."
- Player choice "Thank you." → Ryis [blush_special]: "Just... look at me a second. I want to fix this in my memory forever." → Ryis [blush_special]: "I saw you, and my heart got wings."

Elsie officiates. Candle ceremony.

- Ryis [starry_eyed]: "Your light's more beautiful than a Mistrian morning."

Vows:
- Ryis [neutral]: "[Ari]... you're the light in everything."
- Ryis [closed_eyes_smile_blush]: "I see you in the sun and the moon. I see you in the river's glint, and the dappled trees."
- Ryis [blush_special]: "I promise to shelter that light, one day at a time, with everything I am."
- Ryis [neutral]: "I can't wait to build a shining future with you."

Player vow choices:
- "I love you, Ryis." → Ryis [blush_special]: "I love you, [Ari]."
- "You lit a flame for me, so I could fly home to you." → Ryis [starry_eyed]: "I love you, [Ari]."

**Reception (Wynne's toast):**
- Wynne [wink]: "I'm Wynne, and I'd like to propose a toast for my baby brother on the day of his wedding."
- Wynne [think]: "When I was little, my sister and I begged my parents for a brother every day..."
- Darren [happy]: "And as their father, let me just say that it's a bit more difficult than baking a loaf of bread."
- Wynne [wink]: "It worked, didn't it? You're welcome for being born, Ryis!"
- Darren [neutral]: "Call me biased, but Ryis is basically the kindest, most helpful son you could ask for."
- Darren [think]: "We were always trying to spoil him, especially his sisters, but we never could. He always wanted to help out."
- Darren [closed_eyes]: "That's also part of why he came to Mistria. He heard my brother, Landen, needed a hand around the shop... and he wanted to make a difference."
- Darren [sad]: "I was sad, but... man, I was so proud to see him step up like that."
- Wynne [sad]: "When I heard, I bawled my eyes out. Baby Ryis was leaving? With no sisters to look out for him?"
- Wynne [think]: "And then he started writing us about someone new who came to town."
- Wynne [wink]: "And... listen, I'm his big sister. I can read between the lines. I KNOW a crush when I see one."
- Wynne [neutral]: "I realized that Ryis was meant to make his way to Mistria..."
- Wynne [happy]: "He was meant to meet you, [Ari]."
- Darren [happy]: "Let's raise a glass to that. Welcome to the family, [Ari]!"

**Post-reception:**
- Ryis [closed_eyes_smile_blush]: "What an unreal day..."
- Ryis [neutral]: "I'm so happy you could meet my dad."
- Ryis [happy_blush]: "And Wynne. They're crazy about you!"
- Ryis [embarrassed]: "And now... you and I are family, too, [Ari]. We get to have a home together."
- Ryis [blush_special]: "I'm so happy."
- Ryis [blush_special]: "Tomorrow we'll wake up to birdsong, and to the rest of our lives together."

## Source Absences

- No pre-arrival backstory scenes (Ryis's life in the Capital before moving to Mistria)
- No scenes showing Ryis's daily carpentry routine outside the birdhouse project
- No scenes with Ryis's mother (mentioned in letters but not present; Wynne and Darren attend the wedding)
- Children cutscenes exist (player_delivery_ryis, great_bird_1_ryis) but are not extracted here as they are post-marriage content
- Heart events focus on the birdhouse/bluebird restoration arc and the question of home
