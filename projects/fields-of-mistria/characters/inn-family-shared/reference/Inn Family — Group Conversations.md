# Inn Family — Group Conversations

Group conversations from the game data involving at least one Inn family member (Josephine, Hemlock, Luc, Maple).

**Source:** `source/t2/Conversations/Group Conversations/`

---

## Adeline_Balor_Celine_Hemlock_Reina

**inn_poker.c.toml**

### inn_poker
- Refresh: never
- Requires: All five NPCs present, all playing poker, same zone, location = inn
- **Hemlock** (neutral): "Celine wins! Wow, that was a nail-biter."
- **Balor** (sly): "Glad I folded early. My merchant's instinct was whispering to me."
- **Reina** (neutral): "I really thought Adeline was going to take it! How did you know, Celine?"
- **Celine** (happy) [effect: drop]: "I kind of got the feeling Adeline was keeping her cards in order, but she didn't rearrange them when she got her last card!"
- **Adeline** (mad) [effect: shock]: "Oh gosh... am I too organized?"

### inn_poker_2
- Refresh: never
- Requires: Same as above + season = summer
- **Adeline** (mad): "Okay, so to review, I'm betting a dozen roses from the manor garden."
- **Balor** (mad): "I've got a silk scarf from the Capital."
- **Celine** (mad): "I'll see that and bet you the first flush tea from my own garden."
- **Hemlock** (mad): "I'll put up a free breakfast!"
- **Reina** (wink) [effect: hearts]: "And I'll take the whole pot! Read 'em and weep, guys and gals."

### inn_poker_3
- Refresh: never
- Requires: Same base poker setup
- **Balor** (neutral): "So, how're we feeling? Any raises?"
- **Hemlock** (think): "I think it's high time for me to fold."
- **Adeline** (wink): "Hmm. I think Celine's got a winning hand."
- **Celine** (ugh): "Why would you think that!"
- **Celine** (mad): "My cards are so bad! The worst!"
- **Reina** (happy) [effect: drop]: "Ummm... yeah, I'm out too."

---

## Adeline_Dell_Hemlock_Holt_Josephine_Luc_Maple_Nora

**manor_house_dinner.c.toml**

### manor_house_dinner
- Refresh: 3m
- Requires: All eight NPCs in same zone, location = manor_house_dining_room, day_time >= 4:00pm, all activity = eat
- **Josephine** (happy): "Thank you for inviting us all over for dinner, Adeline."
- **Hemlock** (neutral): "And for watching the kids all day!"
- **Adeline** (happy): "It was fun! I think they've all got real futures in civil service."
- **Maple** (think): "I do love telling people what to do..."
- **Maple** (happy): "It'd be nice if they had to listen to me!"
- **Adeline** (ugh): "That's not quite-"
- **Luc** (mad): "If you're looking for an intern at the Museum, just let me know! I wanna help!"
- **Adeline** (happy): "I'll talk to Errol, but I see a bright future ahead of you, Luc!"
- **Nora** (neutral): "How about you Dell? Or would you rather take over the General Store?"
- **Dell** (think): "Hmm..."
- **Dell** (neutral): "Which one lets me fight more monsters?"
- **Holt** (happy): "That's my girl!"

### manor_house_dinner_2
- Refresh: 3m
- Requires: Same as above
- **Hemlock** (neutral): "Hope the kids weren't too much of a handful today, Adeline."
- **Adeline** (happy): "Not at all! They actually helped me find some files I'd lost track of. We made it into a game."
- **Dell** (mad): "Miss Adeline said she wanted help finding her spy reports!"
- **Adeline** (ugh): "Spy reports...?"
- **Josephine** (neutral): "Oh my! Well, those do sound important."
- **Holt** (happy): "You know Dell, I'm one of Adeline's spies."
- **Nora** (wink): "Me too!"
- **Luc** (mad): "You've been spying on Dell this whole time? Oh my gosh!"
- **Maple** (neutral) [effect: sparkles_dark]: "Wow... that's dastardly, Lady Adeline. I'm taking notes!"

---

## Adeline_Dell_Hemlock_Luc_Maple

**crooked.c.toml**

### crooked
- Refresh: 1y
- Requires: All five NPCs same zone, adeline_business_review = true
- **Adeline** (neutral): "How's everything at the Inn, Hemlock?"
- **Hemlock** (neutral): "Can't complain. Although maybe Ryis can take a look at the sign... I think it's crooked again."
- **Luc** (neutral): "Is it?"
- **Dell** (think): "It does look crooked."
- **Maple** (happy) [effect: drop]: "Stop tilting your head, guys."

---

## Adeline_Dell_Holt_Luc_Maple

**candy_supplier.c.toml**

### candy_supplier
- Refresh: 1y
- Requires: All five NPCs same zone, adeline_business_review = true
- **Adeline** (neutral): "Anything new to tell, Holt?"
- **Holt** (neutral): "I should be asking you! Looks like you've picked up some assistants."
- **Maple** (mad): "That's right! We're helping Lady Adeline!"
- **Dell** (mad): "And don't expect any special treatment because we're related, papa!"
- **Luc** (mad): "Let's talk about your candy supplier..."

---

## Adeline_Dell_Luc_Maple

**candy_inspection.c.toml**

### candy_inspection
- Refresh: 1y
- Requires: All four NPCs same zone
- Actions: bark sweat_drop on Adeline
- **Adeline** (think): "Dell, I'm not sure I can assign the Dragonguard to candy inspection."
- **Dell** (mad): "Well, someone's got to do it!"
- **Maple** (neutral): "What about hot chocolate inspection?"
- **Luc** (happy): "Or cake inspection?"

**dragonguard_report.c.toml**

### dragonguard_report
- Refresh: 2m
- Requires: All four NPCs same zone, adeline_business_review = true
- **Adeline** (neutral): "You three want to file a report?"
- **Dell** (neutral): "Yeah! The Dragonguard's doing great. We're helping so many people, and beating up so many bad guys!"
- **Maple** (think): "We're your eyes and ears in town, Lady Adeline! You didn't hear it from me, but I saw Lord Eiland sneak seconds on strawberry shortcake. Pretty suspicious."
- **Luc** (happy) [effect: sparkles]: "And we're all stocked up on supplies! Lots of sticks, and sweets, and spiders! Want to see my chart?"
- **Adeline** (happy): "Ooh, I love a good chart! Excellent work, Dragonguard!"

**hangout.c.toml**

### hangout
- Refresh: 3m
- Requires: All four NPCs same zone, location = manor_house_entry or adelines_office
- Actions: bark sweat_drop on Adeline
- **Luc** (neutral): "Miss Adeline, you should hang out with us. My big sister Reina says you've been working a lot lately."
- **Adeline** (think): "I suppose I have been spending a lot of time in the office..."
- **Dell** (wink): "Maple can do your job while you're playing with us!"
- **Maple** (happy) [effect: sparkles]: "I'm good at bossing people around! [Ari], I'll need 150 sticks and 200 rocks by the end of the day! For reasons!"

**queen_maple.c.toml**

### queen_maple
- Refresh: 1y
- Requires: All four NPCs same zone, location = manor_house_entry
- Writes: queen_maple = true, expires 18h
- **Maple** (mad): "[Ari]! Welcome! You stand in Queen Maple's royal court!"
- **Maple** (happy): "I'm currently consulting with my high council."
- **Luc** (mad): "Our top priority should be to begin diplomatic negotiations with the insect kingdom of Aldaria!"
- **Dell** (mad): "I disagree! Your royal-ness, we should travel to lands far beyond, to find the coolest stuff so we might bring it back for your most majestic majesty."
- **Adeline** (neutral): "Queen Maple said she was taking over the entry hall to hold court, and I couldn't say no."
- **Adeline** (happy) [effect: sweat]: "I mean, she's a queen. I'm outranked!"

**quiet_game.c.toml**

### quiet_game
- Refresh: 1y
- Requires: All four NPCs same zone, location = manor_house_entry or adelines_office
- Writes: queen_maple = true, expires 18h
- Actions: bark sweat_drop on Adeline
- **Adeline** (neutral): "Maple, Luc, Dell... I think it's in the country's best interest for us to play the quiet game. Only the Queen's quietest warriors will be rewarded!"
- **Dell** (mad): "I'm so good at the quiet game! Nobody is quieter than me, you'll see!"
- **Luc** (think): "You sound more like the Queen's loudest warrior, Dell."
- **Maple** (mad): "I royally decree that the quiet game is boring! We are now playing... the screaming game!"

---

## Adeline_Dell_Luc_Maple_March

**inspect_everything.c.toml**

### inspect_everything
- Refresh: 1y
- Requires: All five NPCs same zone, adeline_business_review = true
- Writes: asked_for_nails = true, expires 1m
- **March** (unimpressed): "What's with the kids?"
- **Adeline** (happy): "They're helping out!"
- **Dell** (mad): "We'll need to inspect everything, Mister March."
- **Maple** (mad): "Everything."
- **Luc** (mad) [effect: shock]: "Especially Olric's rock collection! It's so cool!"

---

## Adeline_Dell_Luc_Maple_Ryis

**nails.c.toml**

### nails
- Refresh: 1y
- Requires: All five NPCs same zone, adeline_business_review = true, asked_for_nails = true
- Writes: asked_for_nails = false
- **Adeline** (neutral): "Low on any supplies? I can make a note of it."
- **Ryis** (think): "We can always use more nails, but I don't want to get on March's nerves..."
- **Dell** (happy): "Oh, don't worry Mister Ryis."
- **Luc** (happy): "We already got on his nerves."
- **Maple** (happy) [effect: sparkles]: "We asked for so many nails!"

---

## Adeline_Holt_Josephine

**business_review.c.toml**

### business_review
- Refresh: never
- Requires: All three NPCs same zone, adeline_business_review = true, quest_repair_the_bridge_complete = true, date_time >= 1m
- **Adeline** (think): "How are things looking? Do you have everything you need?"
- **Josephine**: "We've got a happy equilibrium going on at the Inn. And Olric is working out great as a part-timer!"
- **Holt** (think): "Maybe I should have a chat with him! We always get stretched a bit thin at the end of the week, when Nora turns her attention to the Saturday Market."

### business_review_2
- Refresh: never
- Requires: Same as above
- **Adeline** (neutral): "Is there anything the Inn or General Store need? Just say the word!"
- **Josephine** (think): "Hemlock's been sourcing new wines through Balor lately, but I think that's their little side project."
- **Holt** (wink): "Wine, you say? Maybe I should start my own side project!"

---

## Adeline_Josephine_Nora

**friday_help.c.toml**

### friday_help
- Refresh: 1y
- Requires: All three NPCs same zone, location != inn, fnati >= 1
- **Adeline**: "Friday nights have been so busy at the Inn lately! I've got a few proposals of how I could help-"
- **Josephine**: "Oh Adeline, you do more than enough! The best thing you could do is come and enjoy yourself."
- **Nora** (wink): "And remember, no clipboards allowed!"

**inn.c.toml**

### inn
- Refresh: 2m
- Requires: All three NPCs same zone, location != inn, location != general_store_store, date_time >= 1y, quest_repair_the_inn_complete = true
- **Adeline** (neutral): "How are things going at the Inn, Josephine?"
- **Josephine** (happy): "Oh, it's been good! And busy as ever, with Reina in the kitchen and Balor turning his room into a makeshift office."
- **Nora** (happy): "The General Store's been bustling, too. Mistria's come a long way since the earthquake!"

---

## Adeline_Maple

**machinations.c.toml**

### machinations
- Refresh: 3m
- Requires: Both NPCs same zone, Adeline animation = write or write_sit, location = adelines_office or maple_shadowing_adeline = true
- Actions: bark sweat_drop on Adeline
- **Adeline** (neutral): "Are you done reviewing my books, Maple? How do they look to you?"
- **Maple** (sad): "They look okay... Lady Adeline, when do we do the real royal stuff? Like in my stories?"
- **Adeline** (wink): "This is the real royal stuff, Maple. A good leader works hard!"
- **Maple** (mad) [effect: sparkles_dark]: "Sure, but what about our political machinations against neighboring fiefdoms?"

**spy_network.c.toml**

### spy_network
- Refresh: 1y
- Requires: Both NPCs same zone
- **Maple** (mad): "I think the best way to check up on townsfolk would be to use your royal spy network!"
- **Adeline** (happy) [effect: sweat]: "Um... Maple... I don't have anything like that..."
- **Maple** (wink): "Right... that's what we want them to think!"

---

## Balor_Caldarus_Hayden_Josephine_Valen

**breakfast.c.toml**

### breakfast_0
- Refresh: 3m
- Requires: All five NPCs same zone, caldarus_seridia_town = true, location = inn, time_of_day = morning, all activity = eat
- **Josephine** (neutral): "How are you all liking your breakfast?"
- **Balor** (happy): "Perfection as always, Josephine. My compliments to the chef!"
- **Hayden** (wink_arm_down): "I reckon there's no better breakfast in Mistria! What do you think, Caldarus?"
- **Valen** (raised_eyebrow): "I'd say he's too busy eating to voice his thoughts on the matter."
- **Caldarus** (sigh): "If I had to summarize..."
- **Caldarus** (happy): "May I have seconds?"

### breakfast_1
- Refresh: 3m
- Requires: Same as above
- Actions: bark sweat_drop on Balor, Caldarus, Josephine, Valen
- **Josephine** (neutral): "I'm writing up next week's brunch menu. Tell me... how do you folks like your eggs?"
- **Caldarus** (neutral): "Any preparation of egg suits me... but my favorite is perhaps a fluffy quiche."
- **Balor** (wink): "Fried over easy, on top of some of your famous curry!"
- **Valen** (think): "I prefer them hard-boiled and diced into a salad."
- **Hayden** (happy_fist): "I like an egg any which way... but my favorite's gotta be when it's whipped up into a $Mayonnaise$!"
- **Balor** (concerned): "But... don't you want that to accompany something?"
- **Hayden** (think): "If you want to get all fancy about it!"

### breakfast_2
- Refresh: never
- Requires: Same base + caldarus_seridia_town_timer = false
- **Valen** (neutral): "As a doctor, I cannot help but be curious about your physiology, Caldarus."
- **Valen** (think): "I see your tail and the unique structure of your legs, but you otherwise don't seem so different from the rest of us."
- **Josephine** (wink): "Your appetite's the same as the rest of us, that's for sure!"
- **Balor** (happy): "Who can resist a good meal?"
- **Hayden** (happy_arm_down): "Especially with friends!"
- **Caldarus** (neutral): "I suspect you and the others are correct on all points, Valen."
- **Caldarus** (smile): "A good meal, with good company... it makes the heart warm, no matter who we are."

---

## Balor_Celine_Hemlock_Reina

**inn_poker.c.toml**

### inn_poker
- Refresh: 1y
- Requires: All four NPCs same zone, all playing poker, location = inn
- Actions: bark sweat_drop on Balor, cute_face on Celine, sweat_drop on Hemlock
- **Hemlock** (neutral): "Read 'em and weep, kiddos."
- **Balor** (wink): "Not so fast, Hemlock. That hand doesn't beat my triple."
- **Celine** (annoyed): "But my hand does, right Balor?"
- **Celine** (happy): "What did Hemlock just say? Read them and cry, children!"
- **Reina** (mad) [effect: cheery]: "This is riveting, [Ari]!"

---

## Balor_Dell_Luc_Maple

**chocolate_shipment.c.toml**

### chocolate_shipment
- Refresh: 3m
- Requires: All four NPCs same zone
- Writes: kids_got_chocolate += 1, expires 1w
- **Dell** (mad): "The Dragonguard is here to protect your chocolate shipment, Balor."
- **Luc** (mad): "I drew up defensive plans, and Maple made the necessary arrangements."
- **Balor** (wink): "To say I'm grateful to the Dragonguard would be an understatement, so allow me to thank you with some samples from the shipment."
- **Maple** (happy): "Yaaaay!"

**economics.c.toml**

### economics
- Refresh: 3m
- Requires: All four NPCs same zone
- **Balor** (ugh): "Maple, I have to say... you have a surprising grasp of a kingdom's economics."
- **Maple** (happy) [effect: sparkles_dark]: "Well of course! I must know how to tax my citizens in a manner that brings money into the royal treasury, without enraging the people."
- **Luc** (sad): "I don't want to do taxes anymore..."
- **Dell** (happy): "That's what Mom said the other day!"

---

## Balor_Hemlock

**poker.c.toml**

### poker
- Refresh: 1y
- Requires: Both NPCs same zone, both playing poker, location = inn
- Actions: bark ellipses on Balor and Hemlock
- **Hemlock** (wink): "I think you're bluffing, merchant."
- **Balor** (wink): "Hah... big words, bartender. We'll flip our hands on three. One... two... three!"

### poker_planning
- Refresh: 1y
- Requires: Both NPCs same zone, both not playing poker
- **Balor** (neutral): "What do you think? Is it time to get another night of cards going?"
- **Hemlock** (wink): "Balor, it's always time for cards."

**saturday_no_market.c.toml**

### saturday_no_market
- Refresh: never
- Requires: Both NPCs same zone, quest_repair_the_bridge not complete but in progress
- **Balor**: "Mistria's only had access to local produce since the earthquake, but the Inn has still managed to have a nice and varied menu every day."
- **Hemlock** (happy): "That's our Reina! She's always coming up with new recipes."

---

## Balor_Hemlock_Holt

**kids_love_museum.c.toml**

### kids_love_museum
- Refresh: 2m
- Requires: All three NPCs same zone, building != museum, museum_total_count >= 30
- **Balor** (neutral): "That museum of Eiland's is coming along nicely."
- **Hemlock** (neutral): "I tell you, the kids are obsessed. And then they always come back and tell us about it!"
- **Holt** (wink): "I bet they know more about Mistria's history than us grown-ups!"

---

## Balor_Hemlock_Josephine_Reina

**taste_test.c.toml**

### taste_test
- Refresh: 1y
- Requires: All four NPCs same zone, balor/hemlock/josephine taste_test = true
- **Reina** (happy): "Okay, everyone! Tell me what you think!"
- **Hemlock** (happy): "Mm! It's delicious."
- **Balor** (think): "Oh, this reminds me of something I ate in the Capital, at a little cafe tucked away behind the market."
- **Josephine** (neutral): "You sound nostalgic, Balor."
- **Balor** (wink): "Not quite. Reina's done the dish better!"

---

## Balor_Hemlock_March_Terithia

**poker.c.toml**

### poker
- Refresh: 3m
- Requires: All four NPCs same zone, all playing poker, location = inn
- Actions: bark annoyed on March
- **Balor** (neutral): "You've got a tell, March."
- **March** (mad): "Don't try and psyche me out, Balor."
- **Hemlock** (think): "Sorry pal, you definitely have a tell."
- **Terithia** (happy) [effect: sparkles]: "It's really obvious, actually."

### poker_2
- Refresh: 1y
- Requires: Same as above
- **Balor** (neutral): "And one more card on the table makes the riverbank. Now, how's the table feeling in this last go around?"
- **Hemlock** (neutral): "I'm in."
- **March** (mad): "Me too. And I'll raise."
- **Terithia** (happy): "Oho. I'll match that, March."
- **Balor** (wink): "Looks like we've got ourselves a game!"

---

## Caldarus_Dell_Hemlock_Luc_Maple

**chat.c.toml**

### chat_0
- Refresh: never
- Requires: All five NPCs same zone, caldarus_seridia_town = true, location = eastern_road or narrows
- **Dell** (neutral): "And over there, that's an important Mistrian landmark..."
- **Dell** (happy): "That's where I fell into the water chasing a frog!"
- **Luc** (mad): "Like true Dragonguards, Maple and I went in after her. In case she needed help with the frog."
- **Maple** (neutral): "Afterwards Miss Juniper even let us clean off all the mud in the Bathhouse!"
- **Maple** (wink): "She was gonna kick us out... but lucky for us I had been practicing making my cutest faces!"
- **Maple** (happy) [effect: sparkles]: "To manipulate grown-ups."
- **Hemlock** (neutral): "Jo and I owed Juniper a week's worth of dinners for the amount of mud they tracked around."
- **Hemlock** (wink): "Not a bad trade, if you ask me."
- **Caldarus** (think): "I see... In this town, one can barter a slight inconvenience for free meals."
- **Caldarus** (neutral): "Thank you. This is excellent knowledge to have. And Maple..."
- **Caldarus** (smile): "Perhaps you can teach me how you make these powerful faces."

### chat_1
- Refresh: 3m
- Requires: Same as above
- Actions: bark cute_face on Hemlock
- **Luc** (think): "Mister Caldarus, why don't you and Miss Seridia get along?"
- **Dell** (neutral): "Is it because you two are arch rivals, and it's your destiny to always beat each other up?"
- **Maple** (neutral): "Or is it because one of you is a traitor who can never ever be forgiven?"
- **Hemlock** (happy) [effect: drop]: "Caldarus, speaking as an old pro of letting bygones be bygone..."
- **Hemlock** (wink): "You don't have to answer that."
- **Caldarus** (sigh): "Ah... then for the sake of brevity, I shall abstain."
- **Hemlock** (wink): "Sure... but don't hesitate to tell me later, okay?"

### chat_2
- Refresh: 3m
- Requires: Same base + season = winter
- **Dell** (mad): "Mister Caldarus, why don't you wear shoes? My mom and dad make me wear shoes every day!"
- **Luc** (neutral): "Dad, I want to run around in the snow without shoes like Mister Caldarus!"
- **Hemlock** (happy) [effect: drop]: "Luc, it's freezing out. You have to keep your shoes on."
- **Maple** (neutral): "Dad, I like my shoes and don't want to take them off."
- **Hemlock** (happy): "Thank goodness."
- **Maple** (mad): "But... I would like to formally petition for Dell and Luc's right to not wear shoes."
- **Caldarus** (sigh): "I apologize, Hemlock. Though unwitting, I have brought calamity upon your household."

---

## Celine_Dell_Luc_Maple

**garden.c.toml**

### garden
- Refresh: 1y
- Requires: All four NPCs same zone, celine_zone = town/celine_garden or town/celine_garden_chat
- **Celine** (neutral): "What does the Dragonguard think of my garden?"
- **Maple** (happy): "It's so pretty!"
- **Luc** (happy): "Yes, and it makes a wonderful habitat for our insect friends."
- **Dell** (mad) [effect: shock]: "This garden is Dragonguard approved!"

**general_store_dinner.c.toml**

### general_store_dinner
- Refresh: 1y
- Requires: All four at general_store_home, kids eating, time_of_day = evening or night
- **Celine** (neutral): "I'm no Reina, but I hope you liked dinner all the same!"
- **Dell** (think): "Your dinners are like Reina's, but... greener."
- **Luc** (happy): "More leafy. I feel like a caterpillar when I have dinner at your house."
- **Maple** (happy): "I like to pretend I'm the princess of the veggie kingdom!"

### general_store_dinner_2
- Refresh: 1y
- Requires: Same as above
- **Maple** (neutral): "Eat your vegetables, Dell! How else will you grow up to be a big strong knight?"
- **Luc** (happy): "It's important! You have to eat them, even if you think they're the ickiest thing ever!"
- **Dell** (mad): "My big sister says bullying is wrong! Tell them, Celine!"
- **Celine** (happy): "Eat your vegetables, Dell."

**who_gave_them_chocolate.c.toml**

### who_gave_them_chocolate
- Refresh: 1y
- Requires: All four NPCs same zone, kids_got_chocolate >= 1, time_of_day = morning or night
- **Celine** (think): "Who gave the kids chocolate at his hour?"
- **Dell** (mad) [effect: sparkles]: "It's a secret, Celine."
- **Luc** (mad) [effect: sparkles]: "Classified."
- **Maple** (mad) [effect: sparkles]: "We'll tell you if you join the Dragonguard!"

---

## Celine_Dell_Luc_Maple_Reina

**gardening.c.toml**

### gardening
- Refresh: 3m
- Requires: All five NPCs in celine_garden zones
- **Celine** (neutral): "How are you kids doing? Getting the hang of gardening?"
- **Dell** (neutral): "Yeah! I'm going to grow so many hot peppers!"
- **Luc** (happy): "I'm going to grow lots of flowers so the insects have something to pollinate!"
- **Maple** (mad): "I'm growing potatoes... so many potatoes... this is where my potato empire begins!"
- **Reina** (happy): "I'll have to think of a special meal to cook with all three when it's harvest time!"

### gardening_2
- Refresh: 1y
- Requires: Same as above
- **Maple** (mad): "More dirt! More dirt, I say!"
- **Dell** (happy): "Yes, Queen Maple!"
- **Luc** (happy): "Royal dirt for your royal highness!"
- **Celine** (wink): "Thank you all so much for helping out! I'll think of you every time I look out at my garden."
- **Reina** (happy) [effect: drop]: "Are you sure it's not Queen Maple's garden?"

---

## Celine_Elsie_Josephine_Nora

**flowers_talk.c.toml**

### flowers_talk
- Refresh: 1y
- Requires: All four NPCs same zone
- **Elsie** (neutral): "Did you know that there's a language of flowers, Celine?"
- **Celine** (mad) [effect: shock]: "Really? Flowers talk to each other? The Codex Mistria didn't cover this..."
- **Josephine** (think): "I don't think that's quite where Elsie was going with it, Celine."
- **Nora** (happy): "It's more like a language of romance, isn't it?"

---

## Celine_Hemlock

**ale_florals.c.toml**

### ale_florals
- Refresh: 3m
- Requires: Both NPCs same zone, season != spring
- **Hemlock** (neutral): "I was thinking about the ale for next spring. Can you think of anything that might give it a light floral taste? I think Josie would like that."
- **Celine** (think): "Hmm, I'm not sure. Hops and barley are strong flavors to balance."
- **Celine** (happy): "I'll sleep on it and get back to you!"

**dragonguard.c.toml**

### dragonguard
- Refresh: 3m
- Requires: Both NPCs same zone, time_of_day != night, not in zone with Dell/Luc/Maple, date_time >= 1y
- Actions: bark ellipses on both
- **Celine** (happy): "Dell said the Dragonguard was on important business today!"
- **Celine** (think): "That always makes me nervous..."
- **Hemlock** (wink): "Hah! Don't worry, Maple and Luc will keep her out of trouble."
- **Hemlock** (think): "Well... Luc will keep Maple and Dell out of trouble. Right?"

**tea.c.toml**

### tea
- Refresh: 2m
- Requires: Both NPCs same zone, not in Josephine's zone
- **Celine** (neutral): "How did the tea-making go? Did Josephine like your special blend?"
- **Hemlock** (happy): "She loved it. Thanks again for letting me raid your garden, I've always wanted to make her fresh tea!"

### tea_2
- Refresh: 2m
- Requires: Same as above
- **Celine** (neutral): "How did Josephine like the new tea?"
- **Hemlock** (happy): "It went over great! Thanks again for telling me where I could forage that stuff... doing it all myself made it more special."

---

## Dell_Elsie_Luc_Maple

**story.c.toml**

### story
- Refresh: 3m
- Requires: All four NPCs same zone
- **Maple** (happy): "I want to hear a story about a princess!"
- **Dell** (happy): "A princess who's also a master swordsman!"
- **Luc** (happy): "With a praying mantis familiar!"
- **Elsie** (wink): "My, my! Such imaginations! Are you sure you don't want to tell me a story instead?"

---

## Dell_Errol_Luc_Maple_Olric

**western_ruins.c.toml**

### western_ruins
- Refresh: 3m
- Requires: All five NPCs same zone, location = western_ruins
- **Errol** (neutral): "And these are the remains of an ancient pot, depicting events from a past age!"
- **Maple** (happy): "Is that a queen? She has a crown!"
- **Luc** (neutral): "What's this language? It looks like branches!"
- **Dell** (mad): "Is that a dragon? So cool!"
- **Olric** (happy): "Wow! Is it blowing fire all over the place?"
- **Errol** (happy) [effect: drop]: "Olric, aren't you supposed to be giving this tour with me?"

---

## Dell_Hayden_Luc_Maple

**farm_inspection.c.toml**

### farm_inspection
- Refresh: 3m
- Requires: All four NPCs same zone, location = haydens_farm
- **Dell** (mad): "Make way, make way! I'm the captain of Queen Maple's royal guard! Her Majesty is here to inspect your farm, Mister Hayden."
- **Luc** (mad): "The Queen seeks a royal steed. Show us your finest riding animals!"
- **Hayden** (think): "Oh! Well actually, I think they're all fine animals. I don't think I could play favorites."
- **Maple** (happy) [effect: sparkles_dark]: "Your politicking is most clever, Mister Hayden. Queen Maple is pleased to have such cunning subjects."

**pumpkins.c.toml**

### pumpkins
- Refresh: 3m
- Requires: All four at pumpkin_patch routines, season = fall, year_time >= 2m 7d
- **Dell** (mad): "Look at this pumpkin! It's so big!"
- **Luc** (mad): "This one's so round! And look, the symmetry..."
- **Maple** (mad): "And this pumpkin's so orange! Mister Hayden, how'd you get them so big and round and orange?"
- **Hayden** (wink): "Well now, that's a farmer's secret!"

### pumpkins_2
- Refresh: 3m
- Requires: Same as above
- **Dell** (think): "I'm naming this pumpkin Mortimer."
- **Maple** (neutral): "I dub this pumpkin... Lucretia!"
- **Luc** (mad): "Behold... Gary!"
- **Hayden** (happy_fist): "Who wants to bake their new friends into a pie?"
- **Dell** (happy) [effect: sparkles]: "Yaaaay!"

### pumpkins_3
- Refresh: 3m
- Requires: Same as above
- **Dell** (neutral): "That pumpkin looks kind of like Mister Errol, it's so shiny!"
- **Maple** (happy): "This one looks just like Mister Landen."
- **Luc** (neutral): "This one looks like you, Mister Hayden!"
- **Hayden** (wink): "So it does! Nature's got a funny sense of humor, don't she?"
- **Hayden** (laugh): "GYA HA HA!"

---

## Dell_Hemlock_Luc_Maple

**bradley.c.toml**

### bradley
- Refresh: 3m
- Requires: All four NPCs same zone, is_inside = false, season = winter
- **Dell** (neutral): "We're playing hide and seek with Luc's friend, Bradley!"
- **Maple** (think): "Bradley's really good at hiding, though. We've been searching forever!"
- **Hemlock** (happy) [effect: drop]: "Bradley is a Winterpillar..."
- **Luc** (neutral): "We're going to find you, Bradley!"
- **Luc** (mad) [effect: shock]: "Unless you've already undergone metamorphosis... a scenario I had not considered!"

**winter_patrol.c.toml**

### winter_patrol
- Refresh: 3m
- Requires: All four NPCs same zone, is_inside = false, season = winter
- **Dell** (mad): "Hi, [Ari]! The Dragonguard is on winter patrol!"
- **Luc** (neutral): "So let us know if you see anything suspicious."
- **Maple** (happy): "Or if you see anything fun, like a really big pile of snow."
- **Hemlock** (wink): "Definitely let them know if you see something fun."

---

## Dell_Juniper_Luc_Maple

**cauldron.c.toml**

### cauldron
- Refresh: 3m
- Requires: All four NPCs, location = bathhouse, Dell at bathhouse/cauldron zone, date_time >= 1y
- Writes: cauldron_emergency = true
- **Juniper** (annoyed): "Repeat after me, children. \"I will not drink out of the Bathhouse cauldron.\""
- **Maple** (happy): "I will not..."
- **Luc** (think): "Drink out of the Bathhouse cauldron..."
- **Dell** (happy): "Unless it's an emergency!"
- **Juniper** (happy): "Very good."
- **Juniper** (mad): "Wait a minute..."

### cauldron_2
- Refresh: 1y
- Requires: Same + cauldron_emergency = true
- Writes: cauldron_emergency = false
- **Juniper** (annoyed): "What emergency could possibly warrant drinking out of the cauldron, Dell?"
- **Dell** (mad): "Lots of stuff!"
- **Luc** (neutral): "Such as?"
- **Dell** (think): "Well... what if I need powers?"
- **Maple** (ugh): "Like what? The power of bad breath?"

### cauldron_3
- Refresh: 3m
- Requires: Same base (no emergency flag)
- Actions: bark cute_face on Dell, Luc, Maple; annoyed on Juniper
- **Juniper** (mad): "Dell, stop putting sticks in the cauldron."
- **Dell** (happy): "But I'm helping!"
- **Maple** (happy): "She's helping, Miss Juniper."
- **Luc** (happy): "She's sooo helpful!"

**dares.c.toml**

### dares
- Refresh: 3m
- Requires: Same base + season = winter
- **Juniper** (unimpressed): "Don't let yourselves freeze, children."
- **Juniper** (ugh): "Warm yourselves by the cauldron, or I'll get a lecture from your parents."
- **Dell** (neutral): "Can I get IN the cauldron?"
- **Maple** (neutral): "I dare you, Dell. I double dare you."
- **Luc** (mad): "I double dog dragon dare you!"
- **Juniper** (mad): "No dares in the Bathhouse! Don't make me put up a new sign!"

**fireplace.c.toml**

### fireplace
- Refresh: 3m
- Requires: Same base + season = winter
- **Juniper** (annoyed): "Shouldn't you kids find a fireplace or something? There's one at the Inn, you know."
- **Dell** (neutral): "But your bubbling cauldron is so toasty, Miss Juniper!"
- **Luc** (happy): "It's the perfect temperature for warming up after our snow patrol!"
- **Maple** (happy): "I'm even getting used to the smell!"

**potion_of_night_vision.c.toml**

### potion_of_night_vision
- Refresh: 3m
- Requires: All four NPCs, juniper_babysits = true, location = bathhouse, all same zone
- **Dell** (think): "What are you doing Miss Juniper?"
- **Juniper** (unimpressed): "I'm making a potion of superior night vision."
- **Maple** (think): "Why do you need a potion of super venison?"
- **Juniper** (think): "It will help me see in the dark. Superiorly."
- **Luc** (ugh): "Why does it smell like that?"
- **Juniper** (annoyed): "That's the sulfur."
- **Maple** (ugh): "And are you going to DRINK it?"
- **Juniper** (mad): "No."
- **Dell** (happy) [effect: sparkles]: "Can *I* drink it?"
- **Juniper** (angry_brows): "Tempting, but your mother would absolutely kill me."

**warm_up.c.toml**

### warm_up
- Refresh: 3m
- Requires: Same base + season = winter
- **Luc** (mad): "In the name of the Dragonguard, we're commandeering this cauldron!"
- **Dell** (mad): "Good work, Luc. Now, Dragonguard... get yourselves warmed up!"
- **Juniper** (unimpressed): "There's no need to commandeer my belongings, children. I'm not going to stop you from thawing yourselves out."
- **Maple** (happy) [effect: cheery]: "Sorry, this cauldron is definitely ours now."

---

## Dell_Juniper_Luc_Maple_Seridia

**bathhouse.c.toml**

### bathhouse_0
- Refresh: never
- Requires: All five NPCs at bathhouse, same zone, caldarus_seridia_town = true
- **Luc** (neutral): "Miss Seridia, I've been wondering... what's the evolutionary advantage for having red claws?"
- **Maple** (happy): "They look pretty!"
- **Dell** (wink): "I bet it's because they look cool!"
- **Juniper** (happy) [effect: drop]: "Children, don't bother Lady Seridia..."
- **Seridia** (closed_eyes): "Ah, but the child is correct. It is because they look... cool."

### bathhouse_1
- Refresh: 1y
- Requires: Same + Dell at bathhouse/cauldron zone
- **Dell** (neutral): "Miss Juniper, can you make a potion to turn the Dragonguard into real dragons?"
- **Luc** (think): "We could each be a dragon, or we could combine into one big dragon!"
- **Maple** (happy): "Only if Miss Seridia approves, of course!"
- **Seridia** (sly): "Oh, I approve."
- **Juniper** (happy) [effect: drop]: "I don't have a dragon potion, but tell me... how do you feel about horses?"

### bathhouse_2
- Refresh: 2m
- Requires: Same base
- **Seridia** (neutral): "Tell me, children... why do you take up so much of Miss Juniper's time?"
- **Dell** (neutral): "She pretends like she doesn't like us..."
- **Maple** (wink): "But she TOTALLY does."
- **Luc** (happy): "It's funny!"
- **Seridia** (closed_eyes): "My disciple... is this true?"
- **Juniper** (embarrassed): "NO... certainly not..."

---

## Dell_Luc_Maple

**adeline_posted_a_quest.c.toml**

### adeline_posted_a_quest
- Refresh: 2m
- Requires: All three at town/quest_board_looking
- **Maple**: "Lady Adeline posted a quest!"
- **Luc**: "That's not a quest, it's a request."
- **Dell**: "Well, what's the difference?"
- **Maple**: "Most quests don't want you to mop, I do enough \"questing\" at home as it is."

**another_quest.c.toml**

### another_quest
- Refresh: 2m
- Requires: Same as above
- **Maple** (neutral): "Lady Adeline posted a request!"
- **Luc** (sad): "I don't know, it looks kind of hard..."
- **Dell** (think): "What about this one?"
- **Maple** (ugh): "That one's even harder, Dell!"

**beach_monster.c.toml**

### beach_monster
- Refresh: 1y
- Requires: All three same zone, location = beach, kids_beach_day = true
- **Maple** (embarrassed) [effect: shock]: "There! In the distance! It's a giant SEA MONSTER!"
- **Luc** (mad) [effect: shock]: "A megalodon giganticus! Incredible!"
- **Dell** (mad): "We have to draw it away from the town! Dragonguard, execute formation delta!"

**best_friend.c.toml**

### best_friend
- Refresh: 3m
- Requires: All three same zone, date_time < 3m, all heart levels < 4
- **Dell** (mad): "I'm gonna make [Ari] my best friend!"
- **Luc** (neutral): "But I was gonna make [him/her/them/it/[Ari]] my best friend!"
- **Maple** (sad): "Oh Dell... oh Luc... so young, so naive..."
- **Maple** (neutral): "When I make [him/her/them/it/[Ari]] my best friend, I'll order [him/her/them/it/[Ari]] to defeat all [his/her/their/its/[Ari]'s] other best friends..."
- **Maple** (happy) [effect: sparkles]: "And then I'll be the last best friend standing!"

**eggs.c.toml**

### eggs
- Refresh: 1y
- Requires: All three same zone, time_of_day = morning, all activity = eat
- **Dell** (happy): "I like my eggs scrambled!"
- **Maple** (neutral): "I like them sunnyside up."
- **Luc** (think): "I prefer an omelette, personally."
- **Luc** (happy): "Eggs sure are versatile, aren't they?"

**find_frog.c.toml**

### find_frog
- Refresh: 3m
- Requires: All three same zone, is_inside = false
- **Maple** (mad): "Find me another frog!"
- **Dell**: "I'm on it!"
- **Luc** (sad): "I keep telling you, the story says that'll only work if you're a princess!"
- **Luc** (ugh): "Come on, I want to play pirates instead!"

**freeze_tag.c.toml**

### freeze_tag
- Refresh: 2m
- Requires: All three same zone, is_inside = false, season = fall or winter
- **Maple** (neutral): "I think the rules of freeze tag are that if you get tagged, you have to stand still."
- **Dell** (mad): "But I don't wanna stand still! That's boring!"
- **Luc** (think): "And how do you get unfrozen? Do you have to wait until spring?"

**hayden_dad.c.toml**

### hayden_dad
- Refresh: 2m
- Requires: All three same zone
- **Maple** (think): "Don't you think Mister Hayden is kind of like a dad?"
- **Dell** (neutral): "And the animals are his kids!"
- **Luc** (happy) [effect: cheery]: "His kids are so cute!"

**hot_chocolate.c.toml**

### hot_chocolate
- Refresh: 3m
- Requires: All three same zone, location = inn, all activity = drink, season = winter
- **Maple** (happy) [effect: sparkles]: "So? How do you like Reina's special hot chocolate recipe?"
- **Dell** (mad): "It's so good! So good!"
- **Luc** (happy): "And nice and warm! I'm ready for more snow!"

**inn_dinner.c.toml**

### inn_dinner
- Refresh: 3m
- Requires: All three same zone, time_of_day = evening, season = winter, Dell activity = drink or eat
- **Dell** (happy): "Nothing like a cold drink after a long days work."
- **Luc** (think): "Ignore Dell, [Ari]. She keeps saying that because she learned it from her dad."
- **Maple** (sad): "Her drink isn't even cold! That's hot chocolate! And Dell doesn't even have a job!"

**lucs_the_leader.c.toml**

### lucs_the_leader
- Refresh: 1m
- Requires: All three same zone, time_of_day = evening or night
- **Dell** (think): "It's Luc's turn to decide what we do tomorrow."
- **Maple** (neutral): "What do you want to do, Luc?"
- **Luc** (embarrassed) [effect: drop]: "Oh, this is a lot of pressure. Is this what it's like being leader of the Dragonguard, Dell?"

**maple_bad_at_hgs.c.toml**

### maple_bad_at_hgs
- Refresh: 1y
- Requires: All three same zone, hide_and_go_seek = false
- **Dell** (think): "Hide and seek is a little different when Maple's hiding."
- **Luc** (happy) [effect: drop]: "She doesn't really hide, she just commands us not to look at her."
- **Maple** (mad): "I see you looking, [Ari]!"

**new_supplies.c.toml**

### new_supplies
- Refresh: 1y
- Requires: All three same zone, location = general_store_store
- **Maple**: "Hi [Ari]! We're getting supplies for the Dragonguard! Now everyone, pool your money! I have two tesserae."
- **Dell** (mad): "I have four pebbles. This one's red!"
- **Luc** (happy): "I have a leaf!"

**official_chef.c.toml**

### official_chef
- Refresh: 3m
- Requires: All three same zone, all activity = eat, location = inn, reina_is_at_location = inn
- **Dell** (happy): "This is so tasty! Your sister is really good at food, guys! Can she be the Dragonguard's official chef?"
- **Luc** (think): "Well, the Dragonguard is part of Mistria, and Reina is essentially Mistria's royal chef..."
- **Maple** (happy) [effect: sparkles]: "So yes!"

**pancakes.c.toml**

### pancakes
- Refresh: 1y
- Requires: All three same zone, time_of_day = morning, all activity = eat
- **Luc** (neutral): "Dell, you have to eat all kinds of foods if you want to grow up big and strong. It's been proven. By science."
- **Dell** (mad) [effect: sparkles_dark]: "What about all kinds of pancakes? Maybe that's the same!"
- **Maple** (happy): "Come on Luc, let's run a pancake experiment! For science!"

**pocket_frog.c.toml**

### pocket_frog
- Refresh: 1y
- Requires: All three same zone, is_inside = false
- **Maple** (mad): "[Ari], please tell Dell she's not allowed to put more frogs in her pockets."
- **Luc** (sad): "Last time they all got loose in the Inn and Mom and Dad had us chasing frogs in the kitchen until bedtime."
- **Dell** (think): "But what's the point of pockets if they don't have frogs in them?"

**pumpkin_pie.c.toml**

### pumpkin_pie
- Refresh: 3m
- Requires: All three same zone, day_time >= 4:00pm, all activity = eat, season = fall
- **Dell** (mad): "I don't see why we can't have pumpkin pie for dinner."
- **Luc** (sad): "Grown-ups are so unreasonable."
- **Maple** (mad): "Seriously! Pumpkin is a vegetable!"

**rain_or_shine.c.toml**

### rain_or_shine
- Refresh: 2m
- Requires: All three same zone, weather = rainy
- **Maple**: "The Dragonguard gathers, rain or shine! Duty is very important to an aspiring royal."
- **Dell** (mad): "We can't only defend Mistria when it's nice out... what kind of protectors would we be!"
- **Luc** (ugh): "Dry protectors, for one."

**rain_wizard.c.toml**

### rain_wizard
- Refresh: 1y
- Requires: All three same zone, weather = rainy
- **Dell** (think): "This rain must be the work of an evil wizard!"
- **Maple** (happy): "You've got to help us, [Ari]!"
- **Luc** (happy): "Give us your best Dragon Smash!"

**rainy_frogs.c.toml**

### rainy_frogs
- Refresh: 3m
- Requires: All three same zone, weather = rainy
- **Luc**: "A lot of fascinating insects come out during the rain, [Ari]."
- **Dell**: "LIKE FROGS!"
- **Maple**: "Frogs aren't bugs, Dell..."

**snowman.c.toml**

### snowman
- Refresh: 3m
- Requires: All three same zone, is_inside = false, season = winter
- **Dell** (mad): "Well, what do you think, Head Scientist Luc? Has the Dragonguard done a good job?"
- **Luc** (mad) [effect: sparkles]: "Operation Snow Guy is proceeding very nicely."
- **Maple** (happy) [effect: hearts]: "He's so cute!"

### snowman_2
- Refresh: 3m
- Requires: Same as above
- **Dell** (happy): "More snow! More snow!"
- **Maple** (neutral): "You heard her! More snow, Luc!"
- **Luc** (happy): "Yay!"

---

## Dell_Luc_Maple_Olric

**use_the_forge.c.toml**

### use_the_forge
- Refresh: 1y
- Requires: All four NPCs same zone
- **Dell** (neutral): "Mister Olric, can I use the forge? I want to make the coolest sword in all of Mistria."
- **Olric** (happy): "I don't see why not! We'll just need some iron."
- **Dell** (neutral): "There's lot of iron stuff at the kitchen at the Inn! Let's go borrow some!"
- **Maple** (ugh): "This seems like a bad idea..."
- **Luc** (ugh): "My sister needs that stuff for making snacks and stuff! Sorry Dell."

---

## Dell_Luc_Maple_Reina

**cooking_lesson.c.toml**

### cooking_lesson
- Refresh: 3m
- Requires: All four NPCs in inn/kitchen or inn/kitchen_tutorial zones
- **Reina** (neutral): "Okay, so we're learning to cook this morning! Who wants to cut the veggies?"
- **Dell** (mad): "Do I get to use a sword?"
- **Luc** (sad) [effect: sweat]: "Swords are not for the kitchen, Dell!"
- **Maple** (happy): "Unless you open your own restaurant! Dell's Sword and Grill..."

### cooking_lesson_2
- Refresh: 3m
- Requires: Same as above
- **Reina** (wink): "You're almost done with your cooking lesson, Dragonguard! Now, who wants to add a pinch of salt?"
- **Maple** (neutral): "How much is a pinch? This much?"
- **Dell** (happy) [effect: sparkles]: "It's this much!"
- **Luc** (mad): "No, no, it's this much!"
- **Reina** (happy) [effect: drop]: "Oh dear... Now let me show you how to balance out too much salt."

**peas.c.toml**

### peas
- Refresh: 3m
- Requires: All four same zone, kids eating, time_of_day = evening or night
- **Reina** (neutral): "You want more peas, Dell?"
- **Dell** (mad): "I would like less peas, Miss Reina."
- **Luc** (neutral): "Then eat the peas you already have, Dell. Trust me."
- **Maple** (sad): "The more you complain about peas, the more peas you'll get."

**play.c.toml**

### play
- Refresh: never
- Requires: All four same zone, Dell outside, none in hgs_it routine
- **Reina** (neutral): "Watching the kids play reminds me of when I used to play make-believe with Celine and Adeline."
- **Dell** (mad) [effect: sick]: "Cough cough... I can't believe I was betrayed... by my own second-in-command... poisoned... to DEATH..."
- **Maple** (happy) [effect: sparkles_dark]: "You shouldn't have crossed me, Dell... you're too pure of heart. You never stood a chance against Blood Queen Maple's royal poisoner, Luc the Venomous."
- **Luc** (think): "And you are too sure of yourself, Blood Queen Maple. The poison I extracted from my beetles, the poison that now courses through Knight Dell's veins..."
- **Luc** (mad): "It's the same poison in your tea! Long live the insect kingdom!"
- **Reina** (happy) [effect: drop]: "Actually, this is pretty different."

**taste_testing.c.toml**

### taste_testing
- Refresh: never
- Requires: All four same zone, kids eating, location = inn, all taste_test = true
- Actions: item sour_lemon_cake
- **Reina**: "Hey [Ari]! The kids are trying out my new sour lemon cake with a sugar crust."
- **Maple** (happy): "And it's SOUR!"
- **Luc** (happy): "SUPER SOUR!"
- **Dell** (think): "But is it sour enough?"
- **Reina** (wink): "Here you go, [Ari]! I think you'll find it refreshing."

---

## Dell_Luc_Maple_Ryis

**project.c.toml**

### project
- Refresh: 2m
- Requires: All four same zone, Dell at eastern_road/work_station_teaching
- **Maple** (neutral): "What're you building, Mister Ryis?"
- **Ryis** (neutral): "It's a barstool. Your mom wanted another for the Inn."
- **Dell** (mad): "I'll help! I can use a hammer. Or a saw! I'm allowed, because I'm in the Dragonguard."
- **Luc** (think): "Dell is very not allowed."
- **Ryis** (happy) [effect: drop]: "I had a feeling."

### project_2
- Refresh: 1y
- Requires: All four same zone, location = landens_house_f1 or eastern_road/work_station_teaching
- **Dell** (mad): "Let's make a pirate ship!"
- **Luc** (happy): "With an ant colony inside!"
- **Maple** (mad): "The captain's quarters are the biggest room, right? I call dibs!"
- **Ryis** (happy) [effect: drop]: "What if we started with a simpler project first? Like maybe one we can fit in the shop?"

---

## Dell_Luc_Maple_Seridia

**kids.c.toml**

### kids_0
- Refresh: never
- Requires: All four same zone, caldarus_seridia_town = true
- **Dell** (mad): "Miss Seridia, don't worry! The Dragonguard is here to protect you!"
- **Seridia** (ugh): "Protect me?"
- **Luc** (happy): "Yes, for conservation purposes!"
- **Seridia** (neutral): "Conservation...?"
- **Seridia** (ugh): "I am not an animal."
- **Seridia** (closed_eyes_brow): "I am a dragon. A higher being!"
- **Maple** (think): "But Mister Caldarus says humans and dragons are just like birds and sheep. He says we're all animals that coexist in delicate harmony!"
- **Luc** (mad): "And if an animal is endangered, we should protect it!"
- **Seridia** (mad): "Mister Caldarus... is an ant."
- **Luc** (think): "Oh."
- **Luc** (happy) [effect: cheery]: "No wonder I like him so much!"

### kids_1
- Refresh: never
- Requires: Same as above
- Actions: bark sweat_drop on Seridia
- **Seridia** (neutral): "Tell me, children. What do your Dragonguard duties entail?"
- **Seridia** (serious): "Are you responsible for keeping peace in the town?"
- **Seridia** (sly): "Are you granted power to punish those who break that peace?"
- **Luc** (think): "Well, one time I accidentally left the door to my cricket terrarium open..."
- **Maple** (neutral): "And we had to spend the whole day catching crickets down in the kitchen!"
- **Dell** (think): "So in that way we kind of kept the peace..."
- **Luc** (happy) [effect: sparkles]: "And I got sent to my room afterwards! So the person responsible was punished, too!"

### kids_2
- Refresh: never
- Requires: Same + caldarus_seridia_town_timer = false
- **Maple** (neutral): "Lady Seridia, I was wondering..."
- **Maple** (happy): "What can I do to be more royal?"
- **Dell** (wink): "Oh, that's easy! You just have to order people around!"
- **Luc** (happy): "And you have to be really mean about it!"
- **Maple** (mad): "Dell, Luc... I ORDER you to shut up! I'm asking Lady Seridia!"
- **Seridia** (smile): "In my opinion, you are already off to a marvelous start."

---

## Dell_Luc_Maple_Terithia

**kraken_storytime.c.toml**

### leviathan_storytime
- Refresh: 3m
- Requires: All four same zone, terithia_story_time = true
- **Terithia** (mad) [effect: sparkles_dark]: "And that's when the leviathan breached the surface! Half shark, half kraken, half stingray!"
- **Dell** (mad): "I wish I was half shark!"
- **Luc** (think): "I'll be half kraken!"
- **Maple** (neutral): "That's a lot of halves, Miss Terithia!"

**mystery_storytime.c.toml**

### mystery_storytime
- Refresh: 1y
- Requires: Same as above
- **Terithia** (mad) [effect: sparkles_dark]: "And what Seville didn't see in the storm was a HUGE BLACK SHADOW passin' under the belly of the boat! Then we all started hearing the strangest noise..."
- **Maple** (think): "That can't be true, right [Ari]? Nothing could be that big..."
- **Luc** (think): "Actually, the ocean is full of mysteries. Really big mysteries."
- **Dell** (mad): "WOW! It sounds so cool! I wanna fight it!"

**treasure_fishing.c.toml**

### treasure_fishing
- Refresh: 1y
- Requires: All four same zone
- **Maple** (neutral): "Have you ever fished up treasure, Miss Terithia?"
- **Luc** (think): "Or ancient books?"
- **Dell** (mad): "Or a skull?"
- **Terithia** (sad): "Maple, Luc... why is Dell always asking me about dredging up skulls?"
- **Dell** (mad): "Because they're so cool!"

---

## Dell_Luc_Maple_Valen

**field_dressing.c.toml**

### field_dressing
- Refresh: 3m
- Requires: All four same zone, valen_babysits = true, location = clinic_f1
- **Valen** (raised_eyebrow): "The children want me to demonstrate how to field-dress a wound."
- **Dell** (mad): "For when we have to fight a monster!"
- **Luc** (sad): "Can we just... not fight the monster?"
- **Maple** (neutral): "I'm with Luc. Let's make friends with the monster!"

**grievously_injured.c.toml**

### grievously_injured
- Refresh: 3m
- Requires: Same as above
- **Valen** (neutral) [effect: sigh]: "So you were grievously injured in a great battle? And only I can heal you?"
- **Dell** (mad) [effect: sick]: "Cough... yes... I think this is the end of the road for me... avenge me..."
- **Maple** (ugh): "I'm not doing all that."
- **Luc** (sad): "Avenging someone is a lot of work, Dell!"

**skeleton.c.toml**

### skeleton
- Refresh: 3m
- Requires: Same as above
- Writes: dell_skeleton = true
- **Valen** (neutral): "Did you know, children? Each of us has a skeleton inside us."
- **Maple** (happy): "Not me."
- **Dell** (mad): "Really? Why not?"
- **Maple** (ugh): "Because it's gross..."
- **Valen** (happy): "It's actually quite normal."
- **Luc** (think): "But is Maple normal?"

**skull.c.toml**

### skull
- Refresh: 3m
- Requires: Same as above
- Writes: dell_skeleton = true
- **Valen** (raised_eyebrow): "I can see you're fascinated with the Clinic's skeleton, children. Can you tell me what bone this is?"
- **Dell** (mad): "The skull!"
- **Luc** (happy): "Skull!"
- **Maple** (mad): "Skull! Skull! Skull!"
- **Valen** (wink) [effect: sparkles]: "I see we have some skull fans in the Clinic! Me too."

---

## Eiland_Hemlock_Holt

**beer.c.toml**

### beer
- Refresh: 3m
- Requires: All three same zone, date_time >= 2m
- **Eiland** (neutral): "You know Hemlock, there are some historians who say that the history of $Beer$ is the history of civilization."
- **Hemlock** (wink): "I'm always saying that."
- **Eiland** (think): "$Beer$ was a significant development for ancient people. It was a staple food, and even used as currency!"
- **Hemlock** (happy): "I'm always saying that too!"
- **Holt** (wink): "I'm happy for you, buddy."

---

## Errol_Luc

**categorize.c.toml**

### categorize
- Refresh: 3m
- Requires: Both NPCs same zone, building = museum
- **Luc** (neutral): "Wouldn't it be more sensible to categorize the Museum's fauna by genus, rather than alphabet?"
- **Errol** (neutral): "You know, I think you're onto something young master Luc."

**teaching.c.toml**

### teaching
- Refresh: 3m
- Requires: Both NPCs same zone, building = museum
- **Luc** (mad): "You can even identify ancient species of insects by observing the shape of the wings on the imprint they've left behind!"
- **Errol** (happy): "Wonderful!"
- **Errol** (happy) [effect: drop]: "But, erm, young master Luc... aren't I supposed to be teaching you?"

---

## Hayden_Hemlock

**brewing_supplies_give.c.toml**

### brewing_supplies_give
- Refresh: 3m
- Requires: Both NPCs same zone, location = haydens_farm or haydens_house
- Writes: brewing_supplies = true, expires 1m
- **Hayden** (neutral): "Here you go, Hemlock! Plenty of grain and hops for your next round of brewing."
- **Hemlock** (wink): "Much obliged, Hayden. There's a barrel with your name on it when I'm done!"

---

## Hayden_Luc_Maple

**king.c.toml**

### king
- Refresh: 1y
- Requires: All three same zone, location = haydens_farm
- **Maple** (happy): "You're like the king of cows and chickens, Mister Hayden!"
- **Hayden** (laugh): "GYA HA HA!"
- **Hayden** (wink): "I consider myself more of a friend of cows and chickens, personally."
- **Luc** (think): "Yeah... Henrietta's definitely the real royalty around here."

---

## Hemlock_Holt

**beach_cook_out.c.toml**

### beach_cook_out
- Refresh: 3m
- Requires: Both NPCs same zone, season = summer, location != beach, both beach_day = false
- **Holt** (neutral): "Two words:"
- **Holt** (mad): "Beach. COOKOUT."
- **Hemlock** (mad): "The two most important words of the season."

**snow_sage.c.toml**

### snow_sage
- Refresh: 3m
- Requires: Both NPCs same zone, season = winter
- **Holt** (wink): "I'm telling you, Hemlock, you'll never shovel up more snow than me! When I was growing up, they called me the Snow King."
- **Hemlock** (think): "Oh, I did a lot of shoveling when I was on the road with the band. Side jobs, you know?"
- **Hemlock** (wink): "That's why they called me the Snow Sage! And in my sagely wisdom, I can tell you: I've definitely shoveled more than you."

**spicy_scramble.c.toml**

### spicy_scramble
- Refresh: 1y
- Requires: Both NPCs same zone, location = inn, Holt animation = eat
- **Holt** (sad) [effect: sweat]: "Oh, this scramble is SPICY. What's in here, fire peppers?"
- **Hemlock** (ugh): "Holt, that's the plain scramble."

---

## Hemlock_Holt_Josephine_Nora

**dinner.c.toml**

### dinner
- Refresh: 3m
- Requires: All four same zone, not in Celine's zone, time_of_day = evening or night, all activity = eat
- **Hemlock** (neutral): "I walked by Celine's cottage the other day! She's doing great on her own."
- **Holt** (neutral): "She is! I'm proud of her, though I know Nora frets."
- **Nora** (sad): "Oh, I can't help it. She's struck out on her own much earlier than I did."
- **Josephine** (happy) [effect: hearts]: "Oh, Nora! She's not so far away! And we're even eating greens from her garden!"
- **Nora** (think): "True... that does save us a lot of money."
- **Nora** (embarrassed) [effect: hearts]: "And it's nice to have her so close."

---

## Hemlock_Josephine

**garden_stroll.c.toml**

### garden_stroll
- Refresh: 2m
- Requires: Both NPCs same zone, jh_date_night = true, both activity = manor_garden_wander, time_of_day = evening
- **Hemlock**: "Evening, [Ari]. We were just enjoying a romantic walk."
- **Josephine** (happy) [effect: cheery]: "It really is so pretty out here. Celine's been outdoing herself with the gardening!"

---

## Hemlock_Josephine_Luc_Maple_March_Olric_Reina

**inn_dinner.c.toml**

### inn_dinner
- Refresh: 3m
- Requires: All seven NPCs at inn, same zone
- Actions: bark annoyed on March
- **Maple** (neutral): "Mister March, why are you always frowning like that?"
- **March** (mad): "Frowning? I don't frown..."
- **Reina** (mad): "Maple, mind your manners!"
- **Reina** (embarrassed): "And you do frown, March. Like, a little."
- **Hemlock** (think): "More like a lot."
- **Josephine** (ugh): "Honey, manners!"
- **Luc** (happy): "I have good manners, so I'm not going to talk about how Mister March frowns all day, every day. I'm going to keep that thought to myself."
- **Olric** (happy): "Wow, Luc! You're such a grown-up!"

### inn_dinner_2
- Refresh: 1y
- Requires: All seven at inn, same zone, all activity = eat or drink
- **March** (neutral): "Can someone pass the salt?"
- **Hemlock** (neutral): "Honey, can you slide over the salt?"
- **Josephine** (neutral): "Luc, would you be a sweetheart and give me the salt?"
- **Luc** (neutral): "I think Maple has it?"
- **Maple** (think): "I don't have it."
- **Olric** (happy): "Here it is!"
- **Reina** (happy) [effect: drop]: "That's sugar, Olric."

---

## Hemlock_Josephine_March_Olric

**baked_goods_taste_test.c.toml**

### baked_goods_taste_test
- Refresh: 3m
- Requires: All four at inn, same zone, baked_goods_taste_test = true
- **Hemlock** (happy): "Oh, this is delicious!"
- **Josephine** (neutral): "Sweetheart, you wouldn't tell me even if it tasted bad. That's why March is here, to give his honest opinion. What do you think, March?"
- **March** (think): "It's okay, I guess."
- **Josephine** (wink): "And Olric is here to translate!"
- **Olric** (happy): "That means he loves it, and he wants seconds!"

---

## Hemlock_Josephine_March_Olric_Reina

**baked_goods_taste_test_2.c.toml**

### baked_goods_taste_test_2
- Refresh: 3m
- Requires: All five at inn, same zone, baked_goods_taste_test = true
- **Josephine** (neutral): "So? Tell me what you think and be honest!"
- **Hemlock** (happy) [effect: sparkles]: "It's tart and sweet, just like you darling!"
- **Reina** (neutral): "Mm, I love it. I might use less sugar and more cocoa."
- **March** (think): "The cherries are my favorite part."
- **Olric** (happy): "Seconds, please!"

### baked_goods_taste_test_3
- Refresh: 1y
- Requires: Same as above
- Actions: bark sweat_drop on March, cute_face on Olric and Reina
- **March** (think): "This new dish... it's good..."
- **Olric** (happy): "Have mine too, bro!"
- **Hemlock** (wink): "Wow, that's a rave review from March."
- **Reina** (neutral): "That's why I like asking March to taste test my new dishes! He's a tough critic."
- **Josephine** (happy): "One of the toughest we've got!"

### baked_goods_taste_test_4
- Refresh: 1y
- Requires: Same as above
- **Josephine** (neutral): "So? What do you think? Does Reina's revised dish taste better?"
- **Olric** (wink): "And remember, bro... you can't say that it needs more salt."
- **March** (ugh): "But it needs more salt."
- **Hemlock** (happy): "Hah!"
- **Reina** (neutral): "You always say that! Give me something to work with, March."

---

## Hemlock_Josephine_Nora

**saturday_no_market.c.toml**

### saturday_no_market
- Refresh: never
- Requires: All three same zone, quest_repair_the_bridge not complete but in progress
- **Hemlock**: "How's the Saturday Market revival coming along?"
- **Nora** (happy): "It's looking promising! Adeline is all in."
- **Josephine**: "With her and [Ari] here, it's only a matter of time! Soon we'll have those bustling Saturdays back again."

---

## Hemlock_Landen

**wobbly_chair.c.toml**

### wobbly_chair
- Refresh: 2m
- Requires: Both NPCs same zone, Ryis not in same zone as Landen
- **Hemlock** (happy) [effect: drop]: "Not a rush, but one of our barstools has developed a bit of a wobble."
- **Landen**: "Well, we can't have that! I'll pass it on to Ryis, he'll drop by and take a look."

---

## Hemlock_March

**cauldron.c.toml**

### cauldron
- Refresh: never
- Requires: Both NPCs same zone
- **March** (neutral): "Juniper won't empty that cauldron so I can get a closer look at it."
- **March** (think): "I bet I can learn something about foreign metalworking if I could just inspect it."
- **Hemlock** (wink): "I'd give up on that, March. If there's two things Juniper's protective of, it's Dozy and that cauldron of hers."
- **Hemlock** (think): "Three, if you're counting her shoe collection."

**soup_pot.c.toml**

### soup_pot
- Refresh: 2m
- Requires: Both NPCs same zone
- **Hemlock** (embarrassed): "Think you could make me a new pot? The kids burnt the other one trying to make Dragonguard soup."
- **March** (neutral): "I can make the pot, but I need to know..."
- **March** (think): "How was the soup?"

---

## Hemlock_Olric

**brewing.c.toml**

### brewing
- Refresh: 3m
- Requires: Both NPCs same zone, brewing_supplies = true, location = inn or inn yard zones, time_of_day = morning or afternoon
- **Hemlock** (neutral): "We're brewing today, Olric! The first step is mashing... we need to crush the grains so we can mix them up to make the mash."
- **Olric** (happy): "You got it, boss!"

**brewing_supplies_lift.c.toml**

### brewing_supplies_lift
- Refresh: 3m
- Requires: Both NPCs same zone, brewing_supplies = true, location = inn or inn yard zones
- **Hemlock** (neutral): "Thanks for the assist, Olric. I think this beer brewing project is going to be big!"
- **Olric** (wink): "Any time! I'm not much for beer, but I do love picking up heavy stuff!"

**shift.c.toml**

### shift
- Refresh: 1m
- Requires: Both NPCs same zone
- **Hemlock** (neutral): "I've got another open shift at the Inn coming up, if you've got time in your schedule."
- **Olric** (wink): "For sure, boss! Just say the word and I'm there!"

---

## Hemlock_Reina

**out_of_towner.c.toml**

### out_of_towner
- Refresh: never
- Requires: Both NPCs same zone, date_time < 2m
- **Hemlock** (think): "I was once an out-of-towner like [Ari]... I hope we're giving [him/her/them/it/[Ari]] a warm enough welcome!"
- **Reina** (neutral): "I'd like to think so! But maybe we should give [him/her/them/it/[Ari]] an extra big helping of soup the next time [he comes/she comes/they come/it comes/[Ari] comes] through."

---

## Josephine_Juniper

**looking_after_kids.c.toml**

### looking_after_kids
- Refresh: 1y
- Requires: Both NPCs same zone
- **Josephine** (neutral): "You get on so well with the kids! Thanks for keeping an eye on them every once in a while."
- **Juniper** (annoyed): "It's more like they won't leave, no matter how many times I ask."
- **Josephine** (happy) [effect: drop]: "Huh?"
- **Juniper** (happy): "I said, no problem! Any time!"

**soup.c.toml**

### soup
- Refresh: 1y
- Requires: Both NPCs same zone, location != inn
- **Josephine** (happy): "Oh, yes... the pot at the Inn is open to anyone who needs a bowl. Hadn't you noticed?"
- **Juniper** (unimpressed): "Ah... that explains why the children keep running to my cauldron and yelling FREE SOUP!"

**wine.c.toml**

### wine
- Refresh: 2m
- Requires: Both NPCs same zone, location != inn, juniper_can_drink = true
- Writes: new_vintage = true
- **Josephine** (neutral): "We got in that wine you were asking for, Juniper! Come by any time and we'll pour you a glass."
- **Juniper** (sly): "Oho! I'll stop by as soon as I can."

### wine_2
- Refresh: 1y
- Requires: Both NPCs same zone
- **Josephine** (think): "You're such a wine aficionado, I'm surprised you don't offer wine at the Bathhouse."
- **Juniper** (angry_brows): "Dozy won't let me have wine in the bath, and if I can't do it, then no one can!"

---

## Josephine_Luc

**bug_bedtime.c.toml**

### bug_bedtime
- Refresh: 1y
- Requires: Both NPCs same zone, time_of_day = night, luc_is_at = lucs_room/Luc Bed
- **Josephine** (neutral): "And so, the princess was able to identify the mysterious species of insect."
- **Josephine** (wink): "She became known as the Mantis Queen, and established the Royal Society of Entomologists."
- **Luc** (neutral) [effect: sparkles]: "Wowww! The Mantis Queen!"

---

## Josephine_Luc_Maple_March_Olric_Reina

**kids_table.c.toml**

### kids_table
- Refresh: 1y
- Requires: All six NPCs same zone, Josephine at inn/north_table or inn/south_table
- **March** (neutral): "Hey, how did we end up at the kid's table?"
- **Maple** (mad): "Mister March, how do you know Luc and I aren't sitting at the grown-ups table?"
- **Luc** (neutral): "That's true. There's no empirical evidence to prove it one way or the other."
- **Olric** (neutral): "You sure know a lot of big words, Luc!"
- **Reina** (think): "I think he learned that one at the Museum."
- **Josephine** (happy): "Errol does like to turn their visits into impromptu lessons."

---

## Josephine_Nora

**bath.c.toml**

### bath
- Refresh: 2m
- Requires: Both NPCs same zone, location = bathhouse_change_room
- **Josephine** (happy): "That bath always makes me feel like a queen! The stone dragon is so majestic..."
- **Nora** (think): "It looks quite old... I wonder if Eiland's had a look at it."

**horned_beetle.c.toml**

### horned_beetle
- Refresh: 1y
- Requires: Both NPCs same zone
- **Josephine** (neutral): "Luc is very into horned beetles right now. I never knew there were so many kinds!"
- **Nora** (think): "Ah, that explains why Dell's been muttering about the dragonguard practicing their beetle formation."

**money_for_school.c.toml**

### money_for_school
- Refresh: 1y
- Requires: Both NPCs same zone
- **Josephine**: "Nora's helping me put away some tesserae for Luc's schooling. I'm sure he'll want to study in the Capital one day."
- **Nora**: "I'm doing the same for Dell."
- **Nora** (happy) [effect: sweat]: "Although knowing her, she'll spend the money on a sword instead of books."

**sing_tonight.c.toml**

### sing_tonight
- Refresh: 2m
- Requires: Both NPCs same zone, jo_and_hem_performance_night = true, jo_and_hem_performance = false, time_of_day = morning or afternoon
- **Josephine** (think): "I think we might sing a little tonight."
- **Nora** (happy): "Really? I can't wait! Holt and I will be there!"

**take_kids_to_beach.c.toml**

### take_kids_to_beach
- Refresh: 3m
- Requires: Both NPCs same zone, season = summer, kids_beach_day = false
- **Josephine** (neutral): "We should take the kids down to the Beach soon, don't you think?"
- **Nora** (think): "The kids are a great excuse to get us to the Beach, too."

**terithia_tells_stories.c.toml**

### terithia_tells_stories
- Refresh: 1y
- Requires: Both NPCs same zone, Dell/Luc/Maple all at beach
- **Nora**: "The children sure do have big imaginations."
- **Josephine**: "Terithia's stories always get them fired up."
- **Josephine** (happy): "Honestly, me too. That lady's seen things!"

---

## Josephine_Valen

**delicious.c.toml**

### delicious
- Refresh: 1y
- Requires: Both NPCs same zone, location = inn, Valen activity = eat, Reina on inn routine, date_time >= 1y
- **Valen** (neutral): "This is delicious, Josephine. Reina's handiwork, I presume?"
- **Josephine** (neutral): "Oh, thank you Valen! She's really blossomed into an exceptional chef, hasn't she?"

**same_idea.c.toml**

### same_idea
- Refresh: 1y
- Requires: Both NPCs same zone, location = bathhouse_change_room, bathhouse_counter >= 3, Juniper not at bathhouse_change_room
- **Josephine** (happy): "I see we all had the same idea, coming to the Bathhouse. How fun!"
- **Valen** (think): "The bathhouse is quite rejuvenating. The proprietor, however..."

---

## Luc_Maple

**bug_knight.c.toml**

### bug_knight
- Refresh: 1y
- Requires: Both NPCs same zone
- **Maple** (neutral): "Arise, Sir Luc. I dub thee, my Royal Bug Guy."
- **Luc** (mad): "Insect!"
- **Maple** (sad): "Don't talk back to your Queen!"

**dragonguard_business.c.toml**

### dragonguard_business
- Refresh: 1m
- Requires: Both NPCs same zone, swing_play = true
- **Luc**: "We're on official Dragonguard business, [Ari]."
- **Maple**: "Inspecting the swingset to make sure it's safe."

---

## Maple_Reina

**bedtime_story.c.toml**

### bedtime_story
- Refresh: 1y
- Requires: Both NPCs same zone, time_of_day = night, maple_is_at = maples_room/Maple Wake Point
- **Reina** (happy): "And that's how the prince and the pauper fell in love!"
- **Maple** (mad): "That's nice, but can you tell me more about their socioeconomic circumstances?"

---

## Source Absences

No group conversation directories were found for the following potential Inn family pairings (this does not mean conversations do not exist elsewhere in the data, only that no dedicated group conversation directory exists under this source path):

- Hemlock_Luc (no standalone directory; appears in multi-character directories)
- Hemlock_Maple (no standalone directory; appears in multi-character directories)
- Josephine_Maple (no standalone directory; appears in multi-character directories)
- Josephine_Hemlock_Luc_Maple (no standalone directory for the nuclear family as a four-person unit)
- Hemlock_Luc_Maple (no standalone directory; Dell is always present when Hemlock appears with both children)
