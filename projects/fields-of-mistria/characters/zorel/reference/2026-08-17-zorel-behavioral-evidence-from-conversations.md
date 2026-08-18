---
type: reference
title: Zorel — Behavioral Evidence from Conversations
description: 'Extracted dialogue from Zorel''s banked conversation lines, gift responses,
  and supplementary data: booth vendor lines, packing-up lines, greeting, gift reactions,
  gossip references, letters.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Zorel/
- projects/fields-of-mistria/source/fiddle/letters.toml
---

# Zorel — Behavioral Evidence from Conversations

Source: `source/t2/Conversations/Bank/Zorel/`, `source/fiddle/letters.toml`

## First Meeting / Greeting

Source: `Banked Lines/greeting_ari.c.toml`

Triggers: First meeting only (`zorel_has_met = false`), max priority, never refreshes.

- Zorel [neutral]: "Hey there, I'm Zorel!"
- Zorel [think]: "Probably wondering what all these crystals I'm selling are for, huh?"
- Player chooses from: "Healing... maybe?" / "Cute decor?" / "They have captured songs inside them?"
  - If wrong guess: Zorel [embarrassed]: "Haha, nah."
  - If correct: Zorel [embarrassed]: "I can see you've heard of me! Well, let me give you the business spiel anyway."
- Zorel [happy]: "These are Song Crystals!"
- Zorel [neutral]: "With a Crystal Resonator-"
- Zorel [wink]: "Which I also sell-"
- Zorel [neutral]: "You can play the music hidden inside each crystal wherever you choose to place the resonator!"
- Zorel [happy]: "Pretty cool, right?"
- Zorel [neutral]: "I'm also a musician by trade, so it seemed like the perfect opportunity for me to make some music that really lasts!"
- Zorel [think]: "If any of that caught your interest, come and pick out a Crystal Resonator that matches your style!"

**Behavioral notes:** Casual, friendly first impression. Uses "hey" and "huh" naturally. Enthusiastic about her product but not pushy. Self-identifies as a musician first, vendor second. Slight embarrassment when the player already knows about her, suggesting some self-awareness about her reputation.

## Booth Lines (Saturday Market — Active Selling)

Source: `Banked Lines/booth_lines.c.toml`

All require: Saturday, Zorel at her booth (`town/Zorel`), not in packing routine. Each refreshes yearly unless noted.

### General booth lines (no season requirement)

- booth_0 [neutral]: "Heeey, [Ari]! Great day to listen to some new tunes, huh?"
- booth_1 [happy]: "Seems like a lot of people are in the mood for a new Song Crystal today." -> [wink]: "How about you, [Ari]?"
- booth_2 [think]: "Mistria is such a mysterious place..." -> [neutral]: "When I listen closely, I can almost hear music on the air." -> [happy]: "So cool."
- booth_3 [neutral]: "There's a lot of interesting music tastes in Mistria." -> [happy]: "Which is great, cause I've got all kinds of music!"
- booth_5 [neutral]: "Got some new Song Crystals up if you're in the market, [Ari]."
- booth_7 [neutral]: "If you pick a Song Crystal, let me know what you think after you listen to it." -> [happy]: "I love talking music with folks!"
- booth_9 [neutral]: "Let me know if you need any recommendations." -> [happy]: "Otherwise I'll just be working on a new song."
- booth_10 [neutral]: "Good music makes any tough job go by faster." -> [happy]: "Pick out a Song Crystal and give it a try yourself, [Ari]!"
- booth_11 [neutral]: "Don't be afraid to try out music in a genre you don't normally listen to, [Ari]." -> [wink]: "There's so much groovy stuff out there!"
- booth_13 [neutral]: "Let me know if you're looking for any kind of Song Crystal in particular, [Ari]." -> [happy]: "I might even be able to take requests!"
- booth_15 [think]: "Hey... just so you know [Ari], don't try putting regular stones and stuff in a Crystal Resonator." -> [sad]: "Olric was by earlier after he broke his trying to make 'rock music'."

### Seasonal booth lines

- booth_4 (summer, 3-month refresh) [neutral]: "Nothing like a cool tune to beat this summer heat, am I right?"
- booth_6 (not winter, 3-month refresh) [neutral]: "I'm glad my stall is up on this rise." -> [happy]: "Feel that nice breeze?"
- booth_8 (fall, 3-month refresh) [neutral]: "Isn't fall just the perfect season to listen to some tunes?" -> [wink]: "Let's hang out and vibe, [Ari]."
- booth_12 (winter, 3-month refresh) [neutral]: "Hey, [Ari]!" -> [happy]: "Why not pick up a new song?" -> [wink]: "Nothing like some music to help warm you up!"
- booth_14 (winter, 3-month refresh) [think]: "I can play all kinds of instruments but..." -> [sad]: "Not when my hands are this cold!"

**Behavioral notes:** Consistently upbeat and enthusiastic about music. Uses casual slang ("Heeey," "huh," "groovy," "vibe"). Addresses the player by name frequently, creating a personal sales approach without being aggressive. Shows genuine love for music beyond just selling it (works on songs at the booth, talks about music on the air in Mistria). The Olric "rock music" anecdote shows she tells stories about other townspeople with gentle humor. Multi-instrumentalist (claims to play "all kinds of instruments"). Sensitive to weather and seasons in a casual way.

## Packing Up Lines (Saturday Market — End of Day)

Source: `Banked Lines/packing_up.c.toml`

All require: Saturday, Zorel in packing routine (`zorel_packing`). Each refreshes yearly unless noted.

- packing_up_0 [neutral]: "I got a melody I want to work on when I get back home." -> [happy]: "Can't wait to try it out!"
- packing_up_1 [neutral]: "[Ari]!" -> [happy]: "Some good jamming out today."
- packing_up_2 [neutral]: "Hemlock's friends with my parents, they were always hanging out together in the Capital's music scene." -> [happy]: "I'm glad he still keeps playing at festivals and stuff in Mistria, way awesome."
- packing_up_3 [neutral]: "Got lucky that Vera made some time for me before we packed up for the night." -> [happy]: "She's the best stylist in the Kingdom!"
- packing_up_4 [think]: "Starting to run a little low on Song Crystals..." -> [neutral]: "I'll have to see about increasing my stock!"
- packing_up_5 [think]: "It's cool to think that with Song Crystals, my performances might be heard hundreds of years from now."
- packing_up_6 [neutral]: "Sooo glad that Darcy's booth is right around the corner." -> [happy]: "She's always got a refreshing Mushroom Brew at the ready for me!"
- packing_up_7 [think]: "Whew, I'm tired." -> [neutral]: "Maybe I'll just rent a room at the Inn tonight." -> [happy]: "It'd be nice to catch up with Hemlock and Jo."
- packing_up_9 [think]: "I wonder if there are any really big Song Crystals out there..." -> [neutral]: "Maybe I could record a whole album on one!"
- packing_up_10 [think]: "I was working on a song early today, just couldn't seem to get a note right..." -> [neutral]: "Suddenly Stillwell yelled out 'B Sharp'!" -> [happy]: "I didn't know he had such an ear for music."
- packing_up_11 [think]: "Terithia picked up a Song Crystal earlier..." -> [neutral]: "And then right after, Landen came by and asked for the same one!" -> [embarrassed]: "And then Errol did the same thing!"
- packing_up_13 [think]: "Wheedle came by earlier and asked if buying a Song Crystal means he's also buying the song rights." -> [mad]: "What a snake!"
- packing_up_14 [think]: "You've been living in Mistria for a while now, huh [Ari]?" -> [neutral]: "That's so cool!" -> [happy]: "I like roaming around too much to settle down. Maybe someday."
- packing_up_15 [neutral]: "Louis makes my lute cases, you know." -> [happy]: "He wasn't sure about taking on the project until I told him it was like a 'coat for instruments'."

### Seasonal packing-up lines

- packing_up_8 (fall, 3-month refresh) [neutral]: "Mmm, this evening wind is crisp." -> [happy]: "It's nice to feel the season's changing though."
- packing_up_12 (winter, 3-month refresh) [think]: "Maybe I'll stop by the Inn for a hot drink after I'm done packing up..."

**Behavioral notes:** The packing-up lines reveal the most about Zorel's life and relationships:

- **Family:** Parents are friends with Hemlock from the Capital's music scene. Musical family background.
- **Lifestyle:** A roamer, not settled anywhere. Travels to Mistria for the Saturday Market. Does not live in Mistria — rents Inn rooms when tired, goes "back home" otherwise.
- **Relationships with other NPCs:**
  - Hemlock and Josephine ("Jo"): Family friends. Glad Hemlock still plays music. Wants to catch up with both at the Inn.
  - Darcy: Neighboring booth vendor. Drinks Mushroom Brew from her.
  - Vera: Uses her stylist services. Considers her "the best stylist in the Kingdom."
  - Stillwell: Fellow plaza vendor. The "B Sharp" anecdote is ambiguous (music pun or genuine advice).
  - Wheedle: Strong negative reaction. Called him "a snake" for trying to acquire song rights through a purchase.
  - Louis: Commissioned him for lute cases. Persuaded him by framing it as "a coat for instruments."
  - Terithia, Landen, Errol: Customers with overlapping taste in music.
  - Olric: Customer who broke a Crystal Resonator trying to make "rock music."
- **Musician identity:** Plays lute (has cases made). Works on melodies and songs actively. Thinks about legacy — performances lasting hundreds of years. Dreams of recording a whole album on one crystal.
- **Mushroom affinity:** Loves Mushroom Brew from Darcy's booth. Aligns with gift preferences (morel_mushroom loved, many mushrooms liked).

## Basement Line

Source: `Banked Lines/basement.c.toml`

Trigger: Basement priority, refreshes instantly.

- Zorel [happy]: "Hey, nice to see you."

**Behavioral notes:** Minimal line for a fallback/basement context. Friendly default.

## Seridia Line

Source: `Banked Lines/seridia.c.toml`

Trigger: Saturday, Caldarus/Seridia in town, Seridia has visited market at least once, dragon market is Seridia. Refreshes yearly.

- Zorel [neutral]: "I really like it when Seridia stops by."
- Zorel [happy]: "She knows these melodies that are out of this world!"

**Behavioral notes:** Genuinely impressed by Seridia's musical knowledge. The phrase "out of this world" may be literal given Seridia's nature.

## Gift Reactions

Source: `Gift Lines/gift_lines.c.toml`

### Loved gifts
- [wink, sparkles]: "Thanks, [Ari]. This is really special."
- [happy]: "[Ari]! This is super thoughtful!" -> [neutral, cheery]: "I'm glad we're on the same wavelength. Very cool of you!"
- **Loved artifact** (ancient_crystal_goblet, crystal_apple, metal_leaf) [neutral, sparkles]: "Hey, this is nice. I'll tuck it into the corner of my lute-case, so I'll always have it with me."
- **Loved edible** (crispy_fried_earthshroom, crystal_berry_pie, miners_mushroom_stew, mushroom_brew, mushroom_rice, mushroom_steak_dinner, pineshroom_toast) [happy, sparkles]: "Oh, nice. I'm partial to meals like this. Thanks, [Ari]."

### Liked gifts
- [happy]: "Oh, nice. I like it... thanks, you."
- [neutral]: "Oh, this is cool. Thanks, [Ari]."
- [happy]: "Oh! This is so nice!" -> [wink]: "Thanks, [Ari]."
- **Liked crystal** (crystal, crystal_berries, crystal_rose, crystal_wing_moth, crystalline_cricket) [think]: "Crystalline stuff like this always makes me think of music, y'know? Something about the way it shimmers. Thanks, [Ari]."
- **Liked mushroom** (ash_mushroom, glowing_mushroom, morel_mushroom, oyster_mushroom, pineshroom, red_toadstool, upper_mines_mushroom, wild_mushroom) [neutral]: "Oh, nice. Mushrooms are my jam."

### Neutral gift
- [neutral]: "Heeey, thanks."

### Disliked gifts
- [think]: "Can you leave it over there? I'll check it out once I'm done tuning..."
- [sad]: "I dunno [Ari]... do you think this is really my deal?" -> [think]: "I'm not feeling it, but I'll do some soul searching."

### Hated gift
- [ugh]: "This gift, [Ari]... the vibes are in shambles."

### Birthday gifts (neutral/liked/loved only)
- [neutral]: "You got me something for my birthday? That's cool." -> [embarrassed, sparkles]: "Thanks, [Ari]."
- [happy]: "A birthday gift? That's so cool of you!" -> [neutral, cheery]: "Thanks so much, [Ari]!"

**Behavioral notes:** Gift language is consistently casual and music-inflected: "wavelength," "vibes," "soul searching," "my jam," "tuning." Keeps treasured artifacts in her lute-case — the instrument is always with her. Mushroom preference confirmed across reactions. Crystal gifts remind her of music. Disliked gifts are deflected politely but with discomfort. The hated-gift line uses "vibes" vocabulary. Birthday reactions are understated — "cool" rather than effusive.

## Letters

Source: `source/fiddle/letters.toml`

### Letter: "Meet the New Vendors" (from Nora)

- Nora writes to the player: "I wanted to thank you again for helping our market grow, and also invite you to say hello to the new vendors, Stillwell and Zorel."
- Triggers quest `meet_the_new_vendors` on a Saturday after completing the plaza upgrade.

### Letter: "Repairing the Bell Tower" (from Zorel)

- Zorel writes: "Hey [Ari], As a fellow music fan I wanted to ask for your help. Everyone says you can really get things done, and I'm hoping you can help my chances of getting Mistria's Bell Tower repaired. Can you meet me at the Bell Tower? I've asked for Adeline and Landen to meet us there as well, so we can hopefully figure something out!"
- Requires renown level 90, completed `meet_the_new_vendors` quest.
- Triggers quest `repair_the_bell_tower`.

**Behavioral notes:** Zorel's letter voice matches her dialogue: casual ("Hey"), direct, music-focused ("fellow music fan"). She takes initiative on the bell tower project, organizing a meeting with town leadership. Shows she can rally people and cares about Mistria's musical heritage despite not living there.

## Gossip

No gossip lines by Zorel about others found in `gossip.toml`. No gossip lines by others about Zorel found. The NPC data references `zorel_gossip` as a gossip line key but the text content was not located in the searched files.
