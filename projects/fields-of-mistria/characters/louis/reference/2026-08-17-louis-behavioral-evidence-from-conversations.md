---
type: reference
title: Louis — Behavioral Evidence from Conversations
description: 'Extracted dialogue from Louis''s banked conversation lines, gift responses,
  and museum lines: daily talk, seasonal commentary, vendor interactions, packing
  routines, relationships with other NPCs.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Louis/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Louis/Gift Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Louis/Museum Lines/
---

# Louis — Behavioral Evidence from Conversations

Source: `source/t2/Conversations/Bank/Louis/`

## First Meeting

**greeting_ari** (priority: max, refresh: never, requires: louis_has_met = false):
- [happy]: "Greetings and salutations! My name is Louis."
- [neutral]: "If you are looking for an article of clothing, you may rest assured that I personally cut and sew every garment you'll find at my booth."
- [happy]: "My stock changes with the week, so if you find something you simply have to see yourself in, don't wait!"

**Behavioral notes:** Formal, enthusiastic introduction. Emphasizes craftsmanship pride (personally cuts and sews every garment). Uses urgency as a sales tactic ("don't wait"). Speech is elevated and polished.

## Basement Greeting

**basement_1** (priority: basement, refresh: instantly):
- [neutral]: "Good day, [Ari]."

**Behavioral notes:** Polite but minimal. The basement context is a fallback/default greeting.

## Daily Market Talk — General

These lines trigger on Saturdays when Louis is at his stall (not packing).

**charming_town** (refresh: 1y, Saturday, at town/Louis):
- [happy]: "Mistria is such a charming little town, isn't it? Everyone is so fashionable, I feel right at home."

**confidence** (refresh: 1y, Saturday, heart level >= 1):
- [neutral]: "Remember, [Ari], it's not just clothes, it's confidence. There's nothing quite like knowing how well-dressed you are!"

**excellent_prices** (refresh: 1y, Saturday, at town/Louis):
- [happy]: "I have some excellent pieces in stock today, take a look."

**loud_colors** (refresh: 1y, Saturday, at town/Louis):
- [neutral]: "Don't be shy of loud colors, [Ari]. Sometimes a pop of color is just what an outfit needs to come together."

**magnificent_outfit** (refresh: 1y, Saturday):
- [neutral]: "[Ari], what a magnificent outfit!"

**need_tailoring** (refresh: 1y, Saturday, at town/Louis):
- [neutral]: "Let me know if you need anything tailored, won't you?"

**something_special** (refresh: 1y, Saturday, at town/Louis):
- [neutral]: "I'd like to think my off the rack selection is second to none, but let me know if you're looking for something special."

**new_designs** (refresh: 1y, Saturday, at town/Louis):
- [think]: "In the Capital, I used to design much more... ceremonial clothing."
- [happy]: "It's wonderful to design things now that are meant to be worn on a busy day outdoors. So much freedom!"

**Behavioral notes:** Louis is consistently enthusiastic and encouraging about fashion. He offers compliments freely, gives unsolicited style advice, and positions himself as an expert. The "new_designs" line reveals his backstory: he designed ceremonial clothing in the Capital but now finds freedom in practical outdoor wear. He sees this as a positive change. His speech uses elevated vocabulary ("beatific," "effervescent," "salutations") and exclamation marks. He addresses Ari directly and personally.

## Seasonal Market Talk

**spring_cleaning** (refresh: 3m, Saturday, spring):
- [neutral]: "Spring cleaning should start with your wardrobe. Out with the old, and in with the new!"

**summer_wardrobe** (refresh: 3m, Saturday, summer):
- [neutral]: "Light, breathable materials are the cornerstone for any summer wardrobe."

**fall_layers** (refresh: 3m, Saturday, fall):
- [neutral]: "In the fall, your clothing should be all about layers."

**light_jacket** (refresh: 3m, Saturday, fall, at town/Louis):
- [happy]: "I do enjoy autumn. A light jacket is such a versatile garment this time of year!"

**winter_fashion** (refresh: 3m, Saturday, winter):
- [neutral]: "It's not easy to deal with winter weather and be fashionable, but we must soldier on."

**winter_needlework** (refresh: 3m, Saturday, winter):
- [neutral]: "In winter, there's nothing so relaxing as a bit of delicate needlework in front of a roaring fire."

**Behavioral notes:** Each season gets tailored fashion advice. Louis treats seasonal dressing as serious craft knowledge. In winter he reveals a domestic side: relaxing by a fire with needlework. He frames fashion challenges as things to "soldier on" through rather than surrender to.

## Packing Up Lines (End of Market Day)

These trigger on Saturday evenings when Louis is in his packing routine.

**packing_1** (refresh: 1y):
- [happy]: "What a perfect end to a perfect day! I tell you, this hamlet has the most agreeable weather in all of Aldaria."

**packing_2** (refresh: 1y):
- [neutral]: "Ah, the plights and delights of the traveling tailor! I delight in working with new customers, but packing my wares at the end of the day... that's a plight, to be sure."

**packing_3** (refresh: 1y):
- [happy]: "It warms my heart to leave lighter than when I arrived! I hope my pieces bring joy and a touch of style to their new homes."

**packing_4** (refresh: 1y):
- [neutral]: "As always, it was delightful to see you, [Ari]. I hope to wow you with my selection the next time we meet!"

**packing_5** (refresh: 1y):
- [neutral]: "And so we come to cut the thread of another day. Dressing others... oh, it's an exhilarating life, [Ari]."

**packing_6** (refresh: 1y):
- [neutral]: "Another Market Day comes to its fruitful conclusion! I wish you a splendid and stylish evening, [Ari]."

**packing_7** (refresh: 1y):
- [think]: "Before I close up, I must ask... are you making certain to wear appropriate footwear?"
- [neutral]: "Practicality and fashion must walk hand in hand, especially when you work the earth!"

**packing_8** (refresh: 1y):
- [neutral]: "Evening, [Ari]. I'm just getting packed up."
- [think]: "Now, where did I put my sewing kit...?"

**packing_9** (refresh: 1y):
- [neutral]: "A bit of advice while I'm packing up, [Ari]. It does a young person good to learn a bit of sewing, no matter their station."
- [happy]: "Repairing your own buttons builds appreciation of the garment, and a patch makes it truly one of a kind."

**Behavioral notes:** Packing lines reveal Louis as a traveling tailor who comes and goes. He refers to Mistria as a "hamlet," uses poetic turns of phrase ("cut the thread of another day"), and genuinely enjoys his work ("exhilarating life"). He values practicality alongside fashion (footwear advice, sewing skills). He is warm and personal with Ari, always wishing them well. He occasionally loses track of his belongings (sewing kit). The phrase "no matter their station" implies awareness of class distinctions.

## Seasonal Packing Lines

**summer_packing_1** (refresh: 3m, summer):
- [neutral]: "What effervescent summer weather we've had today! I hope future Market Days bring more of the same."

**summer_packing_2** (refresh: 3m, summer):
- [neutral]: "It's still summer of course, but once I return to the workshop I must work on the autumn collection!"
- [happy]: "My days, linen and cotton! My nights, canvas and velvet!"

**fall_packing_1** (refresh: 3m, fall):
- [neutral]: "This evening weather is turning a bit brisk, isn't it? It's nearly time to bring out the wool and down!"

**winter_packing_1** (refresh: 3m, winter):
- [happy]: "I'm especially happy to sell out of things in the winter. Wool is a bit heavy to carry, and it means someone in Mistria is keeping warm!"

**Behavioral notes:** Louis works on the next season's collection at his workshop (implying he has a workspace elsewhere, not in Mistria). He is knowledgeable about textiles (linen, cotton, canvas, velvet, wool, down). The winter line shows genuine care for the townspeople's wellbeing beyond commerce.

## Mentions of Other NPCs

**errol_delight** (refresh: 1y, Saturday, when Errol visits stall):
- [neutral]: "Errol is such a delight to tailor for!"
- [wink]: "He's better at tying his cravat than some nobles."

**holt_sweaters** (refresh: 1y, Saturday, packing):
- [happy, sparkles]: "It was such a delight to see Holt today! He has a positively enviable collection of sweaters, and a fanny pack for truly every occasion."

**ryis_stopped_by** (refresh: 1y, Saturday, packing):
- [happy]: "It was good of Ryis to stop by today."
- [neutral]: "The gentleman has such an eye for color and silhouette! He always surprises me in the ways he mixes and matches my pieces."

**seeing_elsie** (refresh: 1y, Saturday, packing):
- [neutral]: "It was wonderful to see Elsie today. She is a vision, is she not?"
- [happy]: "You know, she was one of my favorite customers in the Capital! It's a dream to be dressing her once more."

**merri_chat** (refresh: 1y, Saturday, when Merri is in town):
- [neutral]: "Merri and I were chatting earlier, she suggested I go hunting for older pieces to renew..."
- [happy]: "It does sound fun."

**seridia_fashion** (refresh: 1y, Saturday, requires Seridia in town + dragon market):
- [think]: "That Seridia... simply impeccable fashion sense."
- [neutral]: "Not everyone can incorporate bones in their outfits, but she works it!"

**Behavioral notes:** Louis judges people primarily through the lens of fashion and style. He admires Errol's cravat skill (comparing him favorably to nobles), Holt's sweater collection, Ryis's creative mixing of outfits, Elsie's beauty, and even Seridia's unconventional bone accessories. The Elsie line is significant: she was his customer in the Capital, establishing a pre-Mistria relationship and confirming his Capital backstory. He appreciates Merri's creative suggestion about renewing vintage pieces. Louis calls Ryis "the gentleman" -- he uses formal, respectful language about everyone.

## Museum Lines

**porcelain_figurine** (refresh: 1y, requires museum donation, not in museum):
- [neutral]: "That $Porcelain Figurine$ at the Museum... what an outfit!"
- [happy]: "I'm so inspired!"

**Behavioral notes:** Even museum artifacts are viewed through a fashion lens. He draws design inspiration from the figurine's outfit.

## Gift Responses

### Loved Gift Reactions

**red_wine** (specific):
- [happy, sparkles]: "Oh, what an enchanting =Red Wine=! Behold that luster, like the deepest of velvets. I will enjoy this, [Ari]!"

**white_wine** (specific):
- [happy, cheery]: "What a delightful =White Wine=! Now, whatever shall I pair it with? I must be sure to draw out its complexities..."

**loved_gift_quality** (golden animal products):
- [happy, sparkles]: "Materials of this caliber beg to be transformed into the finest of goods! I feel inspired! Touched by the divine! My deepest gratitude to you, [Ari]!"

**loved_gift_wine** (generic wine):
- [wink, sparkles]: "Ahh, Mistrian soil truly makes for the finest vintage! Thank you, this is an elegant gift!"

**loved_gift** (generic):
- [happy, sparkles]: "How beatific! How exceptional! I shan't forget this gift, [Ari]!"

**loved_gift_2** (generic):
- [happy, sparkles]: "You have my sincerest thanks, [Ari]. I will make most excellent use of this!"

**Behavioral notes:** Wine gifts trigger connoisseur reactions (comparing red wine to velvet, pondering food pairings). Golden materials trigger creative ecstasy ("Touched by the divine!"). His vocabulary in emotional moments is especially elevated: "beatific," "enchanting," "shan't." He compares wine color to fabric (velvet) naturally.

### Liked Gift Reactions

**crystal** (specific):
- [happy]: "A =Crystal=! Lovely! What should I use it for? Beads? Buttons? Perhaps an adornment..."

**lilac** (specific):
- [happy]: "What a charming bloom! =Lilacs= have the loveliest scent, and they make fetching lapel flowers."

**liked_gift_flower** (generic flower):
- [neutral]: "How lovely! There are some flowers that truly accentuate everything around them, don't you think?"

**liked_gift_materials** (generic materials):
- [neutral]: "Splendid! I'll be sure to turn this into something that shines."

**liked_gift** (generic):
- [happy]: "A most thoughtful gift, [Ari]. Thank you."

**liked_gift_2** (generic):
- [neutral]: "You have a generous heart, [Ari]. My thanks."

**Behavioral notes:** Louis immediately thinks about what he can make with materials (beads, buttons, adornments). Flowers become lapel accessories in his mind. Everything is filtered through craft potential.

### Neutral Gift Reactions

**neutral_gift:**
- [neutral]: "I thank you for your kindness."

**neutral_gift_2:**
- [neutral]: "Oh, for me? It's a nice thought."

### Disliked Gift Reactions

**disliked_gift:**
- [think]: "Ah, I suppose I can find some space for it in my bags..."

**Behavioral notes:** Even when displeased, Louis remains polite and measured. No harshness.

### Hated Gift Reaction

**fuzzy_moth** (specific):
- [ugh, sweat]: "Oh no no no [Ari], this will not do! I can't abide such a thing near my fabrics! A $Fuzzy Moth$ is a harbinger of disaster!"

**Behavioral notes:** The only time Louis drops his composure. Moths near fabrics is a professional nightmare for a tailor. "Harbinger of disaster" is characteristically dramatic phrasing.

### Birthday Gift

**birthday_gift** (priority: max, on birthday, any non-disliked gift):
- [embarrassed, sparkles]: "Oh, you're a thoughtful one. Thank you for thinking of me on my birthday."

**Behavioral notes:** Embarrassment at personal attention on his birthday. Gentle and appreciative rather than effusive.

## Gossip Lines

No gossip conversation file found for `louis_gossip`. The NPC data references this line key with portrait "happy" and effect "hearts," but the dialogue text was not located in the conversation files.

No entries found in `gossip.toml` or `letters.toml` referencing Louis beyond his barks icon.

## Letters

No letters to or from Louis found in `letters.toml`.
