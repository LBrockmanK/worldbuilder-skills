# Elsie — Storylines & Greetings

## Sources

- `t2/Cutscenes/Festival Events/shooting_star.c.toml` — Shooting Star Festival (full cutscene)
- `t2/Cutscenes/Story Events/elsie_dating_tutorial.c.toml` — dating tutorial
- `fiddle/quests/story_quests.toml` — gossip quest, shooting star quest
- `fiddle/quests/fetch_quests.toml` — 7 fetch quests
- `t2/Conversations/Bank/Elsie/Banked Lines/` — 66 banked dialogue files
- `t2/Conversations/Bank/Elsie/Gift Lines/` — gift responses
- `t2/Conversations/Bank/Elsie/Market Lines/` — market vendor lines

This document structures Elsie's triggerable scenarios as storylines and context-gated greetings.

---

## Primary Storyline: Shooting Star Festival

### Festival Morning — Setup

**Trigger:** Summer 28, morning. Elsie visits the player's farm.
**Setting:** Player's farmhouse door.
**What happens:** Elsie explains the Shooting Star Festival tradition — a centuries-old Mistrian custom where villagers watch the meteor shower marking the end of summer. She offers a Star Brooch to invite a romantic partner to the summit. The player can accept or decline the romantic invitation.

**Key dialogue:**
- "It's a Mistrian tradition going back centuries, you know."
- "Better yet... viewing them with a romantic partner on the summit makes an ideal date."
- "It's said that doing so will link your destinies together, just like the stars themselves."
- If player declines: "Of course dear, there's no pressure to choose a date if you're not interested. Forget I mentioned it!"

**Married variant:** Elsie adjusts pronouns for the spouse and encourages renewing the tradition. "I'm sure that [spouse] is eagerly awaiting your invitation." If declined: "Oh! Really? My apologies, [Ari]. Perhaps the timing isn't good." (portrait: sad)

**Blocked variant (summit inaccessible):** She explains the tradition but notes the summit is blocked. "Unfortunately, it seems the summit is still inaccessible, so that won't be possible this year." Redirects: "It will still be nice to enjoy the festivities around town this evening, though."

**Emotional register:** Warm and encouraging throughout. The wink portrait dominates. She is the facilitator, not the participant.
**NPCs present:** None (she visits the player alone)

### Festival Evening — The Date Scenes

**Trigger:** Player gives Star Brooch to chosen NPC + meets them after 8pm.
**Setting:** Summit, under the stars.
**What happens:** Each dateable NPC has a unique scene. Elsie is not present at the summit — she set the stage and exited.

**Elsie's structural role:** She does not appear in any date scene. She is the director who does not walk onstage. This is the clearest expression of her character: she organizes romance for others while her own romantic life exists in past tense.

**Solo option:** If the player goes to the summit alone: "It's getting cold... you'd better head home." (no_speaker — Elsie is not the narrator even here)

---

## Dating Tutorial Storyline

**Trigger:** The morning after any NPC confession / start of dating. Gameplay-triggered cutscene.
**Setting:** Player's farmhouse. Elsie arrives.
**What happens:** Elsie teaches the player about the dating system — timing (weekends), frequency (one date per week per partner), multiple dating, photo cards, date inspiration items.

**Key dialogue:**
- "A little bird told me that you and [partner] have confessed your feelings for each other... and have started Dating!" (portrait: happy + cheery)
- "I'm not here to judge, [Ari]. The only way to know if someone is right for you is to spend more time with them." (portrait: wink)
- "But do keep in mind that when the time comes... you can only marry one person." (portrait: embarrassed)
- "So make sure you choose well." (portrait: wink)

**Player choice:** At the end, the player can optionally view a Dating Tutorial overlay.

**Emotional register:** Enthusiastic and knowing. She frames polyamorous dating as practical ("the only way to know") while noting marriage is singular. The embarrassed portrait on the marriage line is a rare moment of genuine feeling breaking through the advice-giver role.
**NPCs present:** None

---

## Gossip Quest Storyline

**Trigger:** Quest available on request board.
**Setting:** Various locations (Balor, Juniper, Dell for gossip collection; Elsie for turn-in).
**What happens:** Elsie posts a quest asking for gossip. The player visits three information nodes — Balor (merchant news), Juniper (bathhouse gossip), Dell (children's intelligence network) — and reports back.

**Quest description (Elsie's voice):** "Do you have a nose for news? An ear for the exciting? I love Mistria, but I do miss all the gossip of the big city..."
**Objective:** "Talk to Balor, Juniper, and Dell to collect gossip. Afterwards, tell Elsie what you learned."
**Rewards:** 20 renown

**Significance:** This quest mechanizes Elsie's core social behavior. She is a gossip network operator who recruits the player as a field agent. The choice of sources reveals her social map: a trader (outside news), a bathhouse owner (intimate local gossip), and a child (unfiltered observation).

---

## Fetch Quest Storylines (7 quests)

### Recipe Exchange Quests

**Blackberries (x6):**
- "I just love blackberry jam but I'm nearly out. If you can bring me some, I'll teach you how to make your own!"
- Rewards: blackberry jam recipe

**Wild Berries (x6):**
- "There are many ways to use the Mistrian Wild Berry, but in my opinion there's no finer way than in a fresh scone!"
- Rewards: wildberry scone recipe

**Orange:**
- "Would someone be a dear and fetch me an Orange? I need to make a fresh batch of my famous Marmalade."
- Rewards: marmalade recipe

### Capital Connection Quest

**Silver Ingot:**
- "A personal friend in the Capital, who happens to be a rather famous jeweler, has been complaining about the silver shortage."
- Rewards: 500 gold

### Personal Indulgence Quests

**Roses (x12):**
- "Could someone bring me a dozen Roses? I quite like the flower, but I'm not much of a fan of the actual picking, too many thorns."
- Rewards: 300 gold

**Blueberry Jam (x3):**
- "I'm quite partial to Blueberry Jam, could I request a few jars?"
- Rewards: 1000 gold

### Botanical Quest

**Snowdrop Anemone:**
- "If you wouldn't mind bringing me one of those lovely flowers that grows by the Western Ruins, I can provide you with seeds to grow more."
- Rewards: 3 snowdrop anemone seeds

---

## Situational Greetings

### First Meeting / Early Game

- **First encounter:** "Oh my, now who do we have here?" -> "[Ari]? That's a nice name." -> Self-introduction as Great Aunt, not by blood, "simply born aunties." -> Capital background. -> "Be sure to stop by for a chat anytime, dear. I can share the latest gossip and even some romantic advice, if you need it." (greeting_ari)
- **Week one (introduction):** "Have you met my darling Eiland and Adeline? I'm their Great Aunt. Well, not by blood." -> "Some of us are simply born aunties, you see." (week_one_pt_1)
- **Week one (Mistria pitch):** "I know to some, Mistria may seem a tiny backwater town, but keep an open mind..." -> "It has charms the Capital could never offer." (week_one_pt_2)
- **Week two (gossip hook):** Elsie reports strange noises at Valen's clinic. "Do tell me if you notice anything strange yourself, [Ari]." (week_two — with cute_face bark)
- **Early Juniper intro:** "Have you been to the Bathhouse yet?" -> "You might find its proprietress a touch... antisocial, at first." -> "But I've found that Juniper does warm up if you make an effort with her." -> "Particularly if that effort involves a glass of wine or two!" (juniper_effort)
- **Early Adeline concern:** "What am I going to do with that niece of mine?" -> "Adeline needs to relax and have more fun!" -> "See if you can't encourage her a little, [Ari]." (adeline_should_relax)

### Weather-Responsive

- **Pleasant weather, outdoors, traveling:** "It's good to see you out and about! A day like this is meant for enjoying." (out_and_about)
- **Summer, beach day triggered:** "Have you been to the Beach yet, [Ari]? There's nothing more lovely than gazing at the ocean on a beautiful day." (beach_is_beautiful)
- **Winter, snowy:** "There's something so romantic about the snow, don't you think?" (romantic_snow)
- **Rain, with Adeline and Juniper:** "A bit of wine and a lovely day with my niece and my friend... can't rain on that!" (enjoying_the_rain)

### Location-Specific

- **Bathhouse (morning):** "Nothing quite like a morning soak to start the day right. All your worries just melt away!" (bathhouse_soak)
- **Bathhouse (rainy):** "There's nothing better than a long soak on a rainy day. It saps the weariness right out of your bones." (rainy_bathhouse_soak)
- **Bathhouse (traveling to):** "I'm so looking forward to a good soak at the Bathhouse. I hope Juni's around." (hope_juni_is_there)
- **Bathhouse (traveling to/from):** "It's a bit of a walk to the Bathhouse, but the soak is always worth it." (bathhouse_walk) / "What's better than a trip to the Bathhouse? I love my little chats with Juni." (trip_to_bathhouse)
- **Inn (morning, eating):** "Nothing in the Capital beats Reina's breakfast special! Delicious!" (inn_breakfast)
- **Inn (drinking wine):** "Nothing like some wine and chitchat to lift the spirits!" (inn_is_best)
- **Inn (winter):** "It's always nice and warm in here, no matter how cold it gets outside." -> "It must be a well-constructed building, but I imagine the company has something to do with it as well." (warm_inn)
- **Manor entry (Eiland at piano):** "I simply adore Eiland's piano-playing. I could listen for hours!" -> "Did you know, he's been playing since he was tall enough to reach the keys." (eiland_piano)
- **Manor entry (anyone at piano):** "Oh, that's a lovely melody! I'm so glad they keep that grand piano tuned." (piano_music + music_notes effect)
- **Manor garden (afternoon, pleasant):** "Sometimes an afternoon walk in the garden is just the thing! It's so lovely here." -> "Between you and me, Celine volunteered to handle the ground's garden, and she's done a great job!" (manor_garden_beautiful)
- **Manor garden (winter):** "Oh, it's so nice to see you out here [Ari]! Isn't the garden beautiful in winter?" (winter_garden)
- **Museum (20+ donations):** "Goodness, Mistria certainly has a lot of history, doesn't it?" (at_museum)
- **Museum (general):** "This is a grand museum, isn't it?" (grand_museum)
- **Museum (visiting Eiland):** "I'm visiting Eiland at the Museum today! He's been working so hard! I'm proud of him." (walk_to_museum)
- **General Store (2+ months elapsed):** "There's such a variety of produce at the General Store ever since you arrived, [Ari]. A veritable cornucopia!" (general_store)
- **Traveling to beach:** "I can already smell that brisk sea air! I do so love the shore." (walk_to_beach)
- **Traveling to dinner (with Errol and Eiland):** "Off to dinner with the youngins and Errol! I do love to see their enthusiasm for Mistria." (travel_to_dinner)
- **Returning from museum:** "All that time at the Museum really inspired me. I'm going home to record my own history!" (travel_from_museum)

### Activity-Triggered

- **Singing animation:** "(Elsie is occupied with her singing, you shouldn't interrupt her.)" (singing — no_speaker, max priority)
- **Writing/journaling (seated):** "I'm working on my memoirs." -> "There are so many ways to describe a blush!" (memoirs)
- **Writing/journaling (seated):** "[Ari], I was just journaling about my favorite operas." -> "'The Romance of the Prince and the Tailor' was a Capital favorite. I played Queen Celia a few years back! Standing ovations every night." (journaling_memories)
- **Writing (seated, night):** "Excuse me, [Ari]... I try to make notes at the end of each day" -> "Now let's see... I received the most scandalous letter, and then-" (eod_notes)
- **Writing (seated, winter, not night):** "I thought I'd spend this winter day putting some time in on my manuscript." (winter_day_writing)
- **Sunday, not writing:** "Another eventful week for Great Aunt Elsie. I should do some journaling." (eow_journaling + sparkles)
- **Eating, evening:** "Your palate does change as you get older. In my youth I preferred something rich, but now something distinctive is more to my taste." -> "Oh, were we talking about dinner? My mistake." (palate)
- **Drinking, night:** "Well, a nightcap won't hurt." (nightcap; portrait: wink)
- **Pond wander, spring, pleasant:** "These springs take me back... Why, I remember taking a very romantic swim with a certain handsome Count..." (memory_of_a_dip_in_the_pond)

### Romantic Memory Lines (gated: children not present)

- **Frederick 1:** "I dreamt about sweet Frederick last night! Oh, he wasn't like today's men..." -> "He knew how to WORK a pair of tights." (frederick; happy + hearts)
- **Frederick 2:** "I have such fond memories of Frederick!" -> "Except for the beard era. Not sure what that was about." (frederick_2)
- **Warlord:** "Some decades ago a warlord held me for ransom, until she got to know me." -> "We were on and off for quite a few years. She still writes me on the holidays." (warlord)
- **Rodrigo:** "I was lost in thought about an old flame, Rodrigo." -> "A beautiful light in the chandelier of my life!" (rodrigo; happy + hearts)
- **Dev:** "Once upon a time, I met Dev at a royal gala... no one told me he was a prince!" -> "Or such a good kisser." (dev; happy + hearts)

### Relationship-Gated

- **4+ hearts:** "You always take the time to listen, [Ari]. You're such a sweetheart." (thanks_for_listening; happy + sparkles)
- **Any NPC at 4+ hearts:** "You're Mistria's most eligible, [Ari]!" (eligible)
- **Any NPC at 6+ hearts:** "Goodness, [Ari], the way you're stealing hearts in Mistria reminds of myself at your age. Bravo!" (steal_hearts)

### Time-Sensitive / Recurring

- **Friday/rainy inn night (morning):** "Don't miss the evening gathering at the Inn, [Ari]. Hemlock and Josephine host quite the little soiree." (fnati_anticipation)
- **Friday/rainy inn night (before 3pm):** "It will be nice to see the townsfolk at the Inn tonight... I hope I can make it." (inn_will_be_fun_tonight)
- **Sunday (before 2pm):** "Sundays aren't for paperwork... they're for brunch! And mimosas. EMPHASIS mimosas." (sundays_for_mimosas)

### Family / NPC Observation Lines

- **About Adeline:** "Adeline has really grown to fill the shoes her mother and father left behind." -> "Mistria is lucky to have such a civic-minded leader." (adeline_grown)
- **About Adeline:** "Adeline has so many grand plans for Mistria! I'm looking forward to seeing how her vision unfolds!" (adeline_plans)
- **About Eiland:** "I've known Eiland since before he could peek over the keys of a piano." -> "It's been a joy to see him grow up so well!" (known_eiland)
- **About Eiland:** "Eiland is quite a talent at the piano. He'd be a hit at the Capital." (eiland_is_great_at_piano)
- **About parents:** "The Baron and Baroness will be so proud to see what Adeline's accomplished in their absence!" (parents_proud)
- **About March:** "That March is a fiery one, isn't he? But take it from me, he's all bluster." (march)
- **About Hemlock/Josephine (both at Inn):** "Hemlock and Josephine... these two are like pieces of a puzzle that fit together. Warms my heart to see it." (hemlock_and_jo_are_great)
- **About Mistria:** "I thought I'd miss the Capital more, but Mistria's been kind to me." (mistria_is_kind)
- **About the player:** "[Ari], I think we're more alike than most people know! We both love an adventure!" (we_like_adventure)
- **About court gossip:** "[Ari]! A letter from a friend in the Capital just arrived, and I've got all the latest gossip about the court!" (letter_from_court)

### Basement / Fallback

- **Minimum priority:** "Lovely to see you, my dear." (basement_1)

## Q&A Block Mapping

- **Future Storylines:** Shooting Star Festival as primary romantic event; dating tutorial as relationship-progression scenario; gossip quest as social-connector scenario; fetch quests as recipe-sharing scenarios
- **Alternate Greetings:** situational dialogue as context-appropriate first messages (location, weather, activity, time, relationship level)
- **Voice/Dialogue addon:** greeting variations demonstrate register consistency (warm, knowing, wink-punctuated) across all contexts
