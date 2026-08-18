# Inn Family — Shared Conversations

Extracted dialogue and flavor text mentioning Josephine, Hemlock, Luc, or Maple from four shared conversation files.

## family_planning.c.toml

Source: `source/t2/Conversations/family_planning.c.toml`

### March's Family Planning Conversation

In March's family planning dialogue (key: `family_planning_march`), kind: `gameplay_triggered`, March references the Inn family while discussing his childhood:

> **March** (portrait: sad_special): "Life was hard, even with Jo and Hemlock looking out for us. I'd never want any kid to have to go through something like that. I guess the idea kind of scares me."

Context: This line appears at node `.8` after March discusses his and Olric's difficult childhood and their parents. The conversation is triggered with action `bark = "heart"` for npc `march`.

### Seridia's Family Planning Conversation

In Seridia's family planning dialogue (key: `family_planning_seridia`), kind: `gameplay_triggered`, Seridia mentions Josephine:

> **Seridia** (portrait: think): "It is a delicate subject, and when I requested advice from Josephine on how to broach the subject, it was unhelpful. Entirely too much carrying on."

Context: This is node `.1`, the second line of the conversation, before Seridia asks the player about starting a family.

## fetch_quests.c.toml

Source: `source/t2/Conversations/fetch_quests.c.toml`

Note: Most fetch quest turn-in entries lack an explicit `speaker` field. The speaker is the NPC who posted the request, identified contextually by the quest content.

### request_for_caterpillar_turn_in

Kind: `gameplay_triggered`. Speaker mentions requesting the caterpillar for Luc.

> (portrait: neutral): "Ahh, this must be the $Caterpillar$ I requested for Luc, right?"
> (portrait: happy): "Thank you [Ari], he's going to love it. Here's your reward!"

### request_for_deep_earthworm_turn_in

Kind: `gameplay_triggered`. Speaker references Luc as an expert.

> (portrait: happy): "Oooh, is this it?"
> (portrait: sad): "It looks just like a regular worm to me though..."

Player prompt options:
- "Trust me, Luc is gonna be so impressed." (leads to node .2)
- "Yeah, me too..." (leads to node .3)

Node .2:
> (portrait: happy): "Really? Thank you, [Ari]!"

Node .3 (effect: `drop`):
> (portrait: neutral): "Well, I'm sure an expert like Luc will be able to see how cool this worm is! Thank you."

### request_for_rooster_feather_turn_in

Kind: `gameplay_triggered`. Speaker uses "our guests," consistent with Inn context.

> (portrait: happy): "What nice feathers! Refilling our pillows with these will give our guests the best night sleep they've ever had."

### request_for_noodles_turn_in

Kind: `gameplay_triggered`. Writes: `fq_n = "completed"` (expires 7d). Speaker mentions Maple.

> (portrait: happy): "What scrumptious looking $Noodles$!"
> (portrait: neutral): "Thank you, [Ari]. Whether or not Maple approves of them, I'm glad I didn't have to make them this time!"

### request_for_rice_turn_in

Kind: `gameplay_triggered`. Speaker mentions Maple and Luc.

> (portrait: happy): "My $Rice$ request! Thanks, [Ari]."
> (portrait: wink): "I'm sure Maple and Luc thank you too."

### request_for_trail_mix_turn_in

Kind: `gameplay_triggered`. Speaker mentions "the kids."

> (portrait: happy): "Doesn't that $Trail Mix$ look scrumptious! I'm sure the kids will love it."

### request_for_potted_plant_turn_in

Kind: `gameplay_triggered`. Speaker mentions Luc's bugs.

> (portrait: happy): "Heeeey now, you made this $Potted Plant$? I'm impressed, [Ari]!"
> (portrait: neutral): "Hopefully Luc's bugs like it as much as I do!"

### request_for_freshwater_oyster_turn_in

Kind: `gameplay_triggered`. Writes: `fq_fo = "completed"` (expires 7d). Speaker is Maple (self-identifies as "Queen Maple").

> (portrait: happy): "Yaaay, thanks, [Ari]!"
> (portrait: think): "Now let's see what's hiding in this $Freshwater Oyster$!"
> (portrait: mad): "There's no pearl in here!"
> (portrait: sad): "And mom told me I couldn't waste it, so now I gotta eat it..."
> (portrait: ugh): "This is an inauspicious day in the court of Queen Maple."

### request_for_snail_turn_in

Kind: `gameplay_triggered`. Writes: `fq_s = "completed"` (expires 7d). Speaker references "my mom."

> (portrait: happy): "Wow, [Ari]! This is it, the coolest =Snail=!"
> (portrait: neutral, effect: sparkles): "Now remember, if my mom asks, I didn't catch it!"

### request_for_singing_katydid_turn_in

Kind: `gameplay_triggered`. Speaker references "Mom" and keeping bugs in the house.

> (portrait: happy): "A $Singing Katydid$! Thank you, [Ari]!"
> (portrait: neutral): "Mom said no more loud bugs in the house, so you'll need to practice quietly, okay Katydid?"

### request_for_chili_pepper_turn_in

Kind: `gameplay_triggered`. Speaker mentions Hemlock.

> (portrait: happy): "Fresh =Chili Peppers=! Thank you, [Ari]."
> (portrait: wink): "I don't think a dish can ever have enough spice, and neither does Hemlock!"

### request_for_bell_berry_bakewell_turn_in

Kind: `gameplay_triggered`. Speaker mentions "the family."

> (portrait: happy): "If that isn't a perfectly baked $Bell Berry Bakewell Tart$! Thanks, [Ari]!"
> (portrait: wink): "This'll make a nice surprise for the family later!"

### request_for_copper_net_turn_in

Kind: `gameplay_triggered`. Speaker calls Luc "my boy."

> (portrait: neutral): "Hey, [Ari]! That's a fine looking $Copper Net$, thank you!"
> (portrait: happy): "My boy Luc will be so excited when I give this to him!"

### request_for_butterfly_turn_in

Kind: `gameplay_triggered`. Speaker is Caldarus, mentioning Luc.

> **Caldarus** (portrait: smile): "Ah, my requested $Butterfly$. Thank you, [Ari]."
> **Caldarus** (portrait: think): "Luc recently asked if $Butterflies$ and dragons were related, since we both have scales, a fact I was unaware of."
> **Caldarus** (portrait: happy): "While I am sure it is nothing but a child's imagination..."
> **Caldarus** (portrait: angry_brows): "It still bears looking into."
> **Caldarus** (portrait: sinister): "Now... who sent you $Butterfly$? Who do you work for?!"

### request_for_oyster_mushrooms_turn_in

Kind: `gameplay_triggered`. Writes: `fq_oys = "completed"` (expires 7d). Speaker mentions March in context of cooking for him, consistent with an Inn family member (likely Josephine).

> (portrait: happy): "$Oyster Mushrooms$! Big thank you, [Ari]."
> (portrait: neutral): "They're super healthy for you, you know!"
> (portrait: think): "But March hated them when he was a kid..."
> (portrait: happy): "He's gonna be totally surprised when I cook them up for him!"

## fetch_quests_follow_ups.c.toml

Source: `source/t2/Conversations/fetch_quests_follow_ups.c.toml`

### request_for_cheese_follow_up_hemlock

Refresh: `never`. Requires: npc = `hemlock`, `fq_c = "completed"`.

> **Hemlock** (portrait: think): "Luc spent all his allowance on a special $Cheese$ Request from you, huh."
> **Hemlock** (portrait: happy): "Jo isn't too happy, but I think it's a good lesson for our little scientist."

### request_for_noodles_follow_up_maple

Refresh: `never`. Requires: npc = `maple`, `fq_n = "completed"`.

> **Maple** (portrait: neutral): "My mom said you made those $Noodles$ for me, [Ari]."
> **Maple** (portrait: think): "..."
> **Maple** (portrait: happy, effect: sparkles): "Keeping working at it, and maybe I'll make you my Royal Noodle Chef."

### request_for_freshwater_oyster_follow_up_reina

Refresh: `never`. Requires: npc = `reina`, `fq_fo = "completed"`. Mentions Maple.

> **Reina** (portrait: sad): "Poor Maple!"
> **Reina** (portrait: neutral, effect: sweat): "You should have seen the look on her face when I told her a $Freshwater Oyster$ would never have a pearl in it."

### request_for_oyster_mushrooms_follow_up_march

Refresh: `never`. Requires: npc = `march`, `fq_oys = "completed"`. Follow-up to a quest where the requester cooked oyster mushrooms for March.

> **March** (portrait: mad): "Olric let it slip you brought him those horrible mushrooms."
> **March** (portrait: sigh): "He means well, but I just don't like them."

Note: "He means well" refers to the quest requester (likely Josephine or Hemlock, who cooked the mushrooms for March).

## flavor_text.c.toml

Source: `source/t2/Conversations/flavor_text.c.toml`

### Inn Main Area

**inn_flower_pot** (kind: `gameplay_triggered`, no_speaker):
> "Freshly cut flowers fill the vase. You wonder if Celine brought them in."

**inn_banner** (kind: `gameplay_triggered`, no_speaker):
> "An old woven tapestry featuring a sleeping dragon design."

**inn_cabinet** (kind: `gameplay_triggered`, no_speaker):
> "The cabinet is full of glassware and various bottles."
> "An empty mason jar features a worn and peeling label which reads 'BEES - DO NOT TOUCH'."

**inn_locked_door** (kind: `gameplay_triggered`, no_speaker):
> "The door is locked."

### Hemlock and Josephine's Room

**inn_hemlock_lute** (kind: `gameplay_triggered`, no_speaker):
> "Hemlock's prized lute seems very well cared for."

**inn_hemlock_vanity** (kind: `gameplay_triggered`, no_speaker):
> "Hair care products sit on top of Hemlock's bureau."

**inn_jo_vanity** (kind: `gameplay_triggered`, no_speaker):
> "Cosmetics and accessories sit on top of Josephine's bureau."

### Luc's Room

**inn_luc_net** (kind: `gameplay_triggered`, no_speaker):
> "Luc's bug net. You're probably not powerful enough to wield it."

**inn_luc_terrarium** (kind: `gameplay_triggered`, no_speaker):
> "A small terrarium sits on top of the bureau. There are a variety of cute bugs living inside!"

**inn_luc_artwork** (kind: `gameplay_triggered`, no_speaker):
> "Dermaptera Diptych
> Crayon & Paper
> 8.5" x 11""

### Maple's Room

**inn_maple_artwork** (kind: `gameplay_triggered`, no_speaker):
> "A drawing of Prince Rabbit, rendered in colored pencil."

**inn_maple_plushies** (kind: `gameplay_triggered`, no_speaker):
> "Prince Rabbit and Duke Frog oversee Queen Maple's room."

**inn_maple_bear** (kind: `gameplay_triggered`, no_speaker):
> "Marchioness Bear sits plotting next to Maple's toy chest."

## Source Absences

- **family_planning.c.toml**: No family planning conversation exists for Josephine, Hemlock, Luc, or Maple (they are not romanceable characters). They appear only as references in other characters' conversations.
- **fetch_quests.c.toml**: Most turn-in dialogues lack an explicit `speaker` field, making definitive attribution to a specific Inn family member impossible from this file alone. Contextual clues (references to "my boy Luc," "the kids," "our guests," "Queen Maple") suggest some are spoken by Josephine or Hemlock, but the file does not confirm this.
- **fetch_quests_follow_ups.c.toml**: Hemlock and Maple have named follow-up entries with explicit NPC requirements. Josephine and Luc do not appear as named follow-up speakers in this file.
- **flavor_text.c.toml**: Balor's room and Reina's room flavor text entries also exist under the Inn building but are excluded as those characters are not part of the Inn family scope (Josephine, Hemlock, Luc, Maple). No flavor text entry names Josephine directly beyond `inn_jo_vanity`.
