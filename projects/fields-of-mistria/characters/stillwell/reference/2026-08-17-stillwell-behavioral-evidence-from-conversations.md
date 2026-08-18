---
type: reference
title: Stillwell — Behavioral Evidence from Conversations
description: 'All dialogue organized by context with trigger conditions and behavioral
  analysis. Sources: conversation bank files, gift lines, gossip, letters.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Banked Lines/greeting_ari.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Banked Lines/fortunes.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Banked Lines/fortune_denied.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Banked Lines/packing_up.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Banked Lines/basement.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Banked Lines/seridia.c.toml
- projects/fields-of-mistria/source/t2/Conversations/Bank/Stillwell/Gift Lines/gift_lines.c.toml
- projects/fields-of-mistria/source/fiddle/letters.toml
---

# Stillwell — Behavioral Evidence from Conversations

## First Meeting / Introduction

**Trigger:** First time meeting Stillwell (stillwell_has_met = false). Plays once, never repeats.

> "Hey [Ari]. Hmm? No, we haven't met before."
>
> "Me? The name's Stillwell. I can see the past, present, and future. All at once. It's a lot."
>
> "I've come to Mistria on urgent business..."
>
> "The fate of Aldaria... perhaps even the fate of the world is at stake!"
>
> "As you well know, the Magic flowing from the Gate Between Worlds continues to spawn Monsters underground."
>
> "Without your help to keep them in check, any number of terrible calamities may come to pass."
>
> "Trust me... we must prevent those alternate timelines at all costs."
>
> "See the Mission Board over there?"
>
> "I'll update it with Missions for you as I come to see these potential futures."

Player can ask either "Wait... what's your booth for, then?" or "Why are you at the Saturday market, though?"

Both paths lead to:

> "To sell fortunes to the villagers, of course."
>
> "A guy's gotta make a living."
>
> "Saving the world, while critical, doesn't pay my rent."
>
> "In any case, I'm looking forward to working with you."
>
> "And yes, I do mean that literally."
>
> "Thank you in advance for your assistance."

### Behavioral notes
- Knows the player before meeting them (precognition played casually).
- Immediately establishes his dual role: world-saving seer and working fortune teller.
- Self-deprecating humor about money ("doesn't pay my rent," "a guy's gotta make a living").
- Tone is dry and understated, not grandiose despite the cosmic stakes he describes.
- Uses "literally" as a punchline about his foresight.
- Refers to himself casually ("the name's Stillwell") despite claiming to see all of time.

## Basement Greeting

**Trigger:** Stillwell is present; priority = "basement"; refreshes instantly.

> "Good fortune to you, [Ari]."

### Behavioral notes
- Brief, formal well-wishing. Uses "fortune" as both a blessing and a professional reference.

## Fortune-Telling Service Lines

**Trigger:** Saturday, in town, Stillwell at booth ("town/Stillwell"), player has 100+ tesserae. Each fortune set refreshes after 1 year. 8 unique fortune sets cycle through.

### Opening line (all sets)

> "A fortune can be yours for a mere hundred tesserae..."

Player chooses "I'll take it" or "No thanks."

### Decline response (all sets)

> "I knew you would decline, but fate decreed that the question still be asked..."

### Fortune Set 1 — Introductory patter

> "Money, Friendship or Love... I'll peer into the void and pluck out a fortune just for you, [Ari]."

- **Money:** "I see it... a golden shimmer at your shoulder, a season of ambition."
- **Friendship:** "All around, the trees form a canopy to keep you in their shade. It's a time for gratitude."
- **Love:** "I'm having a vision... of roses in bloom, a cardinal tapestry that never wilts."

### Fortune Set 2

> "Would you like a fortune, [Ari]? Let me pierce the veil for you..."

- **Money:** "Let it be known... You walk the mosaic path, on a bridge of tesserae."
- **Friendship:** "It's a time to mind the elderly and care for the young. Let it be known."
- **Love:** "I see pale blossoms turn in the wind. I see a petal lie on your shoulder."

### Fortune Set 3

> "The three pillars of fortune-telling are Money, Friendship, and Love... which can I share with you today?"

- **Money:** "The fates tell me this is an auspicious time for you. Wealth and industry go hand in hand. Take note."
- **Friendship:** "I see a thread connecting you to the others in Mistria, and as you speak, that thread is woven into cord."
- **Love:** "In my eyes you are cast in warm shade, a blush of comfort."

### Fortune Set 4 — Balor commentary

> "Balor said my Money fortune pays for itself... he said I should charge more..."
>
> "Would a worm charge a premium for the dirt he burrows through every day? I think not..."

- **Money:** "I've seen something promising, [Ari]. A dragon sheds a scale for you, and it becomes a tessera on your palm."
- **Friendship:** "Around you I see flowers of every kind, blooming in every color. Bloom with them, [Ari]."
- **Love:** "My foresight sees you mantled in soft whispers, and a gaze of special affection."

### Fortune Set 5

> "Friendship is a candle in the darkness, [Ari]. Let me know if you'd like a reading..."

- **Money:** "The petals of a lotus, the scales of a dragon. I see prosperous symbols all around you."
- **Friendship:** "I see an earthquake shake the foundation apart. I see your hands bind it back together."
- **Love:** "I hear the music of hearts in harmony with your own, the echo of steps side by side."

### Fortune Set 6 — Love popularity

> "Love fortunes are my most popular, by far."
>
> "Who's asking? That's a secret, and I'll keep your secret too."

- **Money:** "Show me your palm, [Ari]. This is your wealth line... this week, you'll see it grow like a shadow at dusk."
- **Friendship:** "Seek out harmony; speak to your fellow, and they will smile upon you."
- **Love:** "A kiss imagined, a daring touch of words to the heart. It's a time to be bold, [Ari]."

### Fortune Set 7

> "I foresaw your arrival, [Ari]... welcome..."

- **Money:** "My second sight tells me many things... there is opportunity on your horizon, rising like the sun."
- **Friendship:** "There's an amity in belonging, and an amity in helping others belong. It's a good time to be generous in all things."
- **Love:** "Listen for the wistful sigh and the murmur of affection. Seek the smile in a throng of stars."

### Fortune Set 8 — Espresso joke

> "Hmm. Is this feeling of impending doom a premonition, or is it Darcy's triple shot espresso?"

- **Money:** "You wish for a divination of wealth, and I see it in your future. Trust in the earth, and in your own hands."
- **Friendship:** "The stars envy you, they are so far apart. They see you find strength shoulder to shoulder, in merry community."
- **Love:** "I see your hand reach into the flame, and I see the flame welcome you. This fire is nothing to fear, [Ari]."

### Behavioral notes — Fortune-telling overall
- Language is consistently poetic and metaphor-heavy: dragons, mosaics, petals, flame, void.
- The "mad" portrait is used most often during fortune delivery — suggests intense concentration or a trance-like state, not anger.
- Humor bleeds through the mysticism: the Balor exchange, the espresso joke, the worm analogy.
- He charges 100 tesserae but philosophically objects to charging more — values his craft over profit.
- The decline line ("fate decreed that the question still be asked") maintains the seer persona even when the player refuses.
- References to Darcy (espresso) and Balor (business advice) show social connections.
- Keeps client confidentiality ("I'll keep your secret too").
- Fortune imagery draws on nature, cosmos, and physical sensation rather than specific predictions.

## Fortune Denied (Insufficient Gold)

**Trigger:** At booth, player has fewer than 100 tesserae.

> "Apologies, [Ari]... without tesserae to light the way, I can't see what will come to pass."

### Behavioral notes
- Polite refusal. Frames money as a mystical requirement ("light the way") rather than a simple fee.

## Packing Up Lines (End of Saturday Market)

**Trigger:** Saturday, in town, stillwell_routine = "stillwell_packing". 8 lines, each refreshes after 1 year.

> 1. "I'm closing up, but the third eye is always open for you, [Ari]."
>
> 2. "Breaking down the booth is such a hassle... why is everything so heavy..."
>
> 3. "Fate has decreed... that I pack up my booth..."
>
> 4. "I'm too sleepy to do booth breakdown... help..."
>
> 5. "You're up late, [Ari]... how do you have so much energy?"
> "Well, be sure to find your way home... before fate intervenes..."
>
> 6. "The stars can have many hidden meanings..."
> "But sometimes seeing them simply means it's time to go home."
>
> 7. "I inherited these robes, and this booth from my grandmother... they don't make mythical tents like this anymore."
>
> 8. "Nora said I couldn't leave my booth here until next Saturday Market, even if I sleep behind the table..."
> "Sigh. Better get packed up."

### Behavioral notes
- Physically lazy or low-energy: complains about heavy things, sleepiness, wanting to skip packing.
- Uses fortune-telling language sarcastically about mundane tasks ("fate has decreed... I pack up").
- Inherited his robes and booth from his grandmother — family lineage in the trade.
- Nora enforces market rules on him (can't leave booth overnight), suggesting he'd prefer not to bother.
- Contrasts the player's energy with his own tiredness — portrays himself as low-stamina.
- Warm toward the player even when tired ("third eye is always open for you").

## Seridia Commentary

**Trigger:** Saturday, Seridia is visiting the market (caldarus_seridia_town = true, seridia_market_count >= 1, dragon_market = "seridia"). Plays once (refresh = "never").

> "Everytime Seridia comes to my booth, she starts saying what I'm about to say, right before I say it."
>
> "I'd be impressed if it wasn't so annoying."

### Behavioral notes
- Seridia (a dragon) can apparently match or outdo his precognition.
- Acknowledges her ability but is irritated rather than threatened.
- Competitive about his craft.

## Gift Reactions

### Loved Gifts

**General loved (two variants):**

> "Ah... could it really be? A surprise...? Now that's rare. I love it, [Ari]."
>
> "I foresaw that a figure would come before me, and here you are. What I did not foresee was the depth of your generosity. I thank you, [Ari]."

**Red wine (specific loved):**

> "The future always seems a little more bearable with a good glass of wine. Thank you, [Ari]."

**Edible loved (crystal_berry_pie, spell_fruit_parfait):**

> "Ah yes, one of my favorite foods, replete with the tartness of melancholy. This is exquisite. Thank you."

**Mystery items (fog_orchid, weightless_stone):**

> "This thing, this object of mystery... I adore it, [Ari], and long will I contemplate it. Thank you."

**Spooky items (ancient_crystal_goblet, black_tablet, crystal_apple, fog_orchid, weightless_stone):**

> "There's something... unsettling about this."
> "I love it."

### Liked Gifts

**General liked (two variants):**

> "Thank you [Ari]. I see that your intuition has revealed what I like."
>
> "I never expect others to know my tastes, but this is quite to my liking. Thank you, [Ari]."

**Crystal items (crystal, crystal_berries, crystal_rose, crystal_wing_moth, crystalline_cricket):**

> "The crystalline seems so unreal... and yet, it reminds us of the natural order of things. Thank you for this wisdom, [Ari]."

**Monster items (monster_cookie):**

> "There's something about this that defies the cosmic order... I like it."

**Night/dark items (night_queen, shadow_flower):**

> "The night, the moon, the stars, and the mysteries therein... all of these spark my interest. Thank you, [Ari]."

### Neutral Gift

> "Ah, thank you."

### Disliked Gift

> "Thanks... I think?"

### Hated Gift (sunflower)

> "The only thing worse than receiving this gift was knowing it was coming."

### Birthday Gift

**Trigger:** Within 24 hours after Stillwell's birthday; gift is neutral, liked, or loved.

> "A birthday gift? I didn't see any sign of this!"
>
> "Thank you, [Ari]... for showing me that the future is not always written."

### Behavioral notes — Gifts overall
- Genuinely surprised by gifts — remarkable for someone who claims to see the future. The birthday line makes this explicit: surprises are meaningful to him because they prove the future isn't fixed.
- Drawn to the mysterious, unsettling, and dark: loves spooky objects, night flowers, crystals.
- The red wine line reveals a melancholic streak ("the future always seems a little more bearable").
- Describes favorite food as having "the tartness of melancholy" — frames even pleasure through a somber lens.
- Hated gift reaction is perfectly in-character: he foresaw the bad gift and resents it.
- Philosophical even in casual thanks (crystalline items prompting thoughts about "the natural order").

## Letters

### From Nora (mentions Stillwell)

**Letter: "Meet the New Vendors"**
**Trigger:** After completing the Saturday Market Plaza upgrade quest, on a Saturday.

> "[Ari],
>
> I wanted to thank you again for helping our market grow, and also invite you to say hello to the new vendors, Stillwell and Zorel.
>
> I think you'll find both of their booths quite interesting! Come find me afterwards for an additional reward."

Starts quest: meet_the_new_vendors.

### Behavioral notes
- Stillwell does not send any letters himself. He is referenced by Nora as one of two new Saturday Market vendors alongside Zorel.

## Gossip

The NPC data registers a gossip line key (`stillwell_gossip`) with portrait "happy" and effect "hearts." The actual gossip text was not found in a separate gossip text file — it may be embedded elsewhere in the conversation system or defined at runtime.

## Barks

Stillwell is registered in `barks.toml` with his small icon sprite. No specific bark text lines were found in the data beyond the icon entry. His greeting introduction triggers a bark action (`cute_face`).
