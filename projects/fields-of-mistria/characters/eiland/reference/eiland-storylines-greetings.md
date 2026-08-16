# Eiland --- Storylines & Greetings

## Sources

- `t2/Cutscenes/Heart Events/Eiland/` --- 5 heart event files
- `t2/Conversations/Bank/Eiland/Banked Lines/` --- situational dialogue
- `fiddle/quests/heart_quests.toml` --- quest triggers
- `fiddle/quests/story_quests.toml` --- story quest triggers
- `fiddle/letters.toml` --- invitation letters

---

## Heart Event Storylines

### The Stele (2 Hearts)

**Trigger:** Relationship reaches 2 hearts; letter invitation from Eiland
**Setting:** Manor grounds --- the ancient stele
**What happens:** Eiland takes the player to a stele on the Manor grounds and teaches them about its origins. He explains it depicts a legendary set of armor worn by the Dragonsworn, "a nearly mythical being who aided the dragons in the ancient days of the world." The player feels raised lettering on the stele surface, revealing a hidden compartment containing the Dragonsworn Greaves. Eiland takes the greaves and leaves for the Museum.
**Player choices:** Two dialogue options at key points (asking about steles vs. treasure; reacting to the Dragonsworn legend). Both paths converge. Choices affect tone, not outcome.
**Key character moment:** He leaves without saying goodbye --- absorbed by the discovery. Not rude, just consumed. This is the baseline behavior the arc will challenge.
**Emotional register:** Excited, didactic, warm. Pure archaeological enthusiasm with no visible inner conflict.
**NPCs present:** None

### The Ruins (4 Hearts)

**Trigger:** Relationship reaches 4 hearts; completion of The Stele; letter invitation
**Setting:** Western Ruins --- seaside cliff site revealed by the earthquake
**What happens:** Eiland brings the player to the Western Ruins, a site untouched for centuries. He shares what the stele text revealed: the armor pieces were believed to protect entire areas, not just the wearer. They search the ruins and discover the Dragonsworn Helmet in pristine condition, along with more hidden text.
**Player choices:** "assistant" vs. "collaborator" framing; encouragement options. He corrects "assistant" to "collaborator" regardless.
**Key character moment:** "I could spend the rest of my life here and not uncover all of its secrets." --- genuine, not melancholic. And calling the player a collaborator: "I'd say you're more of a collaborator! You've got a talent for archaeology, [Ari]."
**Emotional register:** Professional excitement at peak. The player is valued as a partner in discovery.
**NPCs present:** None during scene; Errol follow-up at Museum

### The Manor (6 Hearts)

**Trigger:** Relationship reaches 6 hearts; completion of The Ruins; letter invitation
**Setting:** Manor House --- Adeline's office, then Elsie's room
**What happens:** The trail leads to the Manor itself. Eiland is embarrassed that the "adventure" is a house search. Adeline and Elsie are present. Adeline tells the childhood story of the Caldosian signet ring: young Eiland found it in the basement, he and his mother researched the crest, it became an international incident when the Caldosians reclaimed it, but it gave him his taste for archaeology. Elsie finds the Dragonsworn Cloak folded among old blankets in her wardrobe. No inscription, no puzzle --- the trail goes cold.
**Player choices:** Reaction to the search ("What are friends for?" vs. "leave this out of the history books"); reaction to the signet ring story. Both affect emotional tone.
**Key character moment:** "I was afraid of this." (portrait: ugh) --- no clues with the cloak. But the family warmth (Adeline's storytelling, Elsie's wine toast) shows that what matters is close to home.
**Emotional register:** Deflated adventure energy offset by family warmth and shared celebration. The anti-climax is the point.
**NPCs present:** Adeline, Elsie

### The Glade (8 Hearts)

**Trigger:** Relationship reaches 8 hearts; completion of The Manor; Deep Woods unlocked; letter invitation
**Setting:** Deep Woods --- the Grove of Rest, a sacred glade with memorial trees
**What happens:** Eiland invites the player for a walk, admitting he has no lead on the remaining armor. He shows them the Guardians of the Woods (ancient conifer trees) and the Grove of Rest, where memorial trees carry stone markers skyward as they grow. He reflects on his childhood self, his parents, and the passage of time. They discover the last two armor pieces (Cuisses and Cuirass) hidden near a second stele in the grove.

After the discovery, Eiland starts to rush to the Museum --- then stops himself: "No, wait. There's no need for us to rush off. Why don't we take a break first and just... appreciate the moment?" The event branches into best friend or romantic partner.

**Player choices:**
- Two response options about feeling connected/calm (affect portrait warmth based on Shooting Star festival attendance)
- "Please, go on!" vs. "I love it when you talk about things you feel passionate about!" (both encourage him)
- "Nonsense, you're my best friend" (best friend path) vs. "I want to be with you" (romantic path)
- Logical vs. intuitive explanation for finding the armor

**Key character moment:** The decision to stay and appreciate the moment rather than rush to the Museum. And: "The truth is... I don't want our adventure together to be over." (portrait: gloomy_special --- his only use of this expression)

**Romantic path specifics:**
- "I've been wanting to tell you how much you mean to me for some time now." (portrait: hope_special)
- "I-I'm so happy that you feel the same way." (portrait: happy_blush)

**Shooting Star Festival branch:** If the player attended the festival with Eiland, dialogue has warmer variants throughout (happy_blush instead of happy, hope_special instead of neutral, references to "the night we spent watching the stars on the summit").

**Emotional register:** Contemplative, meditative, then emotionally intense. The Grove of Rest setting mirrors the event's function: a place where things are laid to rest and lifted up.
**NPCs present:** None during scene; follow-ups from Adeline, Elsie, Errol

### The Legacy Stele (10 Hearts)

**Trigger:** Player presents engagement ring while dating Eiland
**Setting:** Walk from town to the Manor grounds stele --- back where it all started
**What happens:** Eiland reflects on their first discovery together and apologizes for dashing off at the 2-heart event. He draws a parallel between archaeology and life: "In archaeology, there is so much that only becomes evident after you've assembled the whole picture. Perhaps life is like that, too." He reveals he commissioned a Legacy Stele to commemorate their adventures --- "more permanent than a record in a book." He admits he was about to propose himself.

**Player choices:**
- Response to his enthusiasm apology: "Your enthusiasm is one of my favorite things about you" vs. "I'd forgotten about that!"
- Response to "treasure" metaphor: "I treasure you as well" vs. playful teasing
- Propose now vs. delay (can return later)

**First vs. return visit:** Dialogue differs slightly based on whether the player has seen this scene before (the stele introduction is reordered).

**Key character moment:** "I was so lost in the hunt for the Dragonsworn Armor, that I didn't initially see the treasure right in front of me. I'm referring to you, [Ari]." (portrait: hope_special -> embarrassed)

**Proposal:** "It is the greatest honor of my life to say... yes! I want nothing more than to spend the rest of my days by your side." / "I can't believe we both hoped to propose today. What are the chances?" / "This is fate, [Ari]. We were always destined to share a shining future together."

**Emotional register:** Arc resolution. Peaceful, intimate, self-aware. The return to the stele connects beginning and end.
**NPCs present:** None

### Wedding

**Trigger:** Post-proposal; scheduled ceremony
**Setting:** Ceremony location (likely gazebo, matching Adeline's parents' wedding)
**Wedding party:** Errol (spouse_party_0), Adeline (spouse_party_1), Wiscar and Linnet as guests, Wiscar as standing speaker
**Post-wedding:** Elsie sends wedding gifts letter (desk, chair, artifact shelf)
**Child:** Astrid (post-marriage)

---

## Story Quest Storylines

### Reopening the Mines

**Trigger:** Town progression milestone
**What happens:** Eiland contacts the player about reopening the Mines. Meeting at the Museum, then at the Mine entrance with Errol. Eiland provides the historical and archaeological context; Errol provides the practical mining expertise.
**Eiland's role:** Initiator and historical consultant. He frames the mines as archaeologically significant, not just economically.

### The Water Tablet

**Trigger:** Player finds tablet with strange markings in the Mines
**What happens:** Player brings the tablet to Eiland for translation. His expertise in ancient languages enables the player to progress deeper into the mines.
**Eiland's role:** Translator. This is the story quest that most directly uses his established skill set.

### The Dragonsworn Tablet

**Trigger:** Both Eiland 8-heart and Juniper 8-heart events completed
**What happens:** Eiland and Juniper collaborate to solve the mystery of the Dragonsworn Tablet, bridging archaeological knowledge and witch magic. The player receives the Dragonsworn equipment.
**Eiland's role:** Co-solver alongside Juniper. His archaeological knowledge meets her magical knowledge.

---

## Situational Greetings

### Location-specific

**Museum/Office:**
- At desk: "Forgive my preoccupation, [Ari]... Errol came across some fascinating marginalia. Isn't this one cute? Oh dear. The one after is quite crude." (museum_0)
- Donations: "[Ari]! Are you making another donation? You've truly helped to expand our collection beyond my wildest dreams." (museum_1)
- Office: "[Ari]! Nice of you to visit me at the office. Hang around as long as you'd like!" (office_paperwork_6)
- Desk work: "These two primary sources each center on the same subject, but the details don't quite line up. Very strange..." (office_paperwork_2)

**Dig sites:**
- Excavation day: "It's an excavation day! The best days of the week!" (excavation_day)
- Routine: "I haven't turned up any artifacts of earthshaking importance today, but that's part of archaeology too." (boring_archaeology)
- In situ: "Discovering something in its original context, or in situ, provides all sorts of clues that wouldn't otherwise be available." (in_situ)
- Pottery: "I've been following a thread about the Alda peoples. It's this old pottery shard that got me started." (studying_pottery_shard)

**Bathhouse:**
- "Ever since Terithia told me that you can find artifacts underwater, I've been practicing holding my breath in the bath. Based on my progress, I think I'll leave the diving to you, [Ari]." (bathhouse)
- "The community bathhouse is a tradition that lives in many civilizations. It's one of the places that the social fabric of a community comes together." (bathhouse_2)

**Beach:**
- "I think about the Western Ruins whenever I'm here at the Beach. This same sea breeze blows over those cliffs." (beach_0)
- "Errol told me he used to get chased by crabs when he was little. It's hard to imagine anything chasing him." (beach_1)

**Inn:**
- "Nothing like the warmth of a hearth on a cold night... That's a story as old as Aldaria." (inn)
- "I was feeling a bit social tonight, so here I am. And here you are!" (inn_2; 4+ hearts; sparkles effect)

**General Store:**
- "Great Aunt Elsie really likes her jams, so I'm buying some ingredients." (shopping)
- "I used up all of Adeline's honey sweetening my tea. I'm hoping to replace it before she notices." (shopping_4)

### Weather-responsive

- Pleasant, outdoors: "Lovely day isn't it?" (lovely_day)
- Rainy: covers Museum desk for Errol (implied by eilands_nice trigger conditions)
- Rainy indoor: "rainy_indoor_work" dialogue (not read but referenced)

### Time-sensitive

- First two weeks: "As a representative of Mistria, it's my responsibility to get you oriented. So if you have any questions... please ask my sister, Adeline. Unless you're looking for the best sweets in town... then I'm your man." (week_one_pt_1)
- First two weeks: "Have you had a chance to see Mistria off the beaten path? There are ruins and artifacts to be found everywhere... this land is rich with history." (week_one_pt_2)
- First meeting (day 1-2): "Hello! Out exploring the town? Mistria has a number of historical sites you may come across on your travels. This area is a hot spot for Archaeology, you know!" (greeting_ari)
- After one year: "It's amazing how we're still making more discoveries in the Western Ruins, year after year!" (western_ruins)
- Spring year 2: "Now that the weather's thawed, I can take a fresh look at the engravings on the fountain." (fountain_engraving)

### Activity-triggered

- Writing at desk: "Switching a pickaxe for a pen... I'd much rather be digging, though." (office_paperwork)
- Daydreaming (evening): "The two texts in question are both from the same era, but stylistically quite different... Oh! Good evening, [Ari]! Apologies, I was off in my own little world." (texts)
- Squinting at scrolls: "I spent part of yesterday squinting at some very fine print on an old scroll, so I'm giving my eyes a rest today. Although... what do you think? Do you think glasses would suit me?" (glasses)
- Sleepy Sunday: "It feels like a sleepy Sunday to me..." (sleepy_sunday)

### Relationship-gated

- 0-1 hearts: "If you have any questions about the historical details of Mistria, I'd be happy to answer them." (zero_to_one_0)
- 2-3 hearts: "You wouldn't believe how many people simply aren't interested in discussing the differences between early and late period Alda artifacts. It's one of the reasons I'm so glad you moved here, [Ari]." (two_to_three_0)
- 4-5 hearts: "The lion's share of new finds have been here in Mistria! It makes me wonder just how important this place used to be!" (four_to_five_0)
- 4+ hearts, museum: "Oh, hello [Ari]. Here to make a donation?" (donation; wink)
- 8-heart follow-up (romantic): "I still can't believe we completed the Dragonsworn Armor set, [Ari]. I admit... I haven't been able to stop thinking about it. Or about you." (hope_special)
- 8-heart follow-up (best friend): "I admit... It's hard to resist the urge to visit the Museum whenever I think about it!" (happy, drop effect)

### Social event greetings

- Friday anticipation: "Morning, [Ari]! Are you going to the Inn this afternoon? Everyone's going to be there, join us!" (friday_anticipation)
- Friday/rainy evening: "[Ari]! Will you be at the Inn tonight? Hemlock has a new beer that wonderfully pairs with chocolate chip cookies." (beer_and_cookies)
- D&D night: "Today's the day... I've got today's session of our Historical Adventure Reenactment ready! Though it's also known by its official name, Dragons & Drama." (dnd_anticipation)
- Music night: "An impromptu music night! Hemlock and Josephine love to keep us guessing. And Aunt Elsie always loves an audience!" (performance)

---

## Q&A Block Mapping

- **Future Storylines:** heart events as progression-gated relationship scenarios; story quests as archaeological problem-solving
- **Alternate Greetings:** situational dialogue as context-appropriate first messages
- **Voice/Dialogue addon:** greeting variations demonstrate register shifts (formal/historical when alone -> warm/personal at higher hearts)
