# Wheedle

## Daily Schedule

### Baseline (All Days)

From `basement_schedule.s.toml` (coverage: all):
- **6:00am:** aldaria/default

Wheedle's baseline location is Aldaria (the Capital). He does not live in Mistria and has no daily schedule in town outside of Saturdays.

### Saturday Market -- Upgrade One

Requires: Saturday, pleasant weather, bridge repair complete, market upgrade complete.

**Spring:**
- 6:00am: Arrives at town/Wheedle (his booth)
- 8:45pm: Begins packing routine (wheedle_packing)

**Summer:**
- 6:00am: Arrives at town/Wheedle
- 8:25pm: Begins packing routine

**Fall:**
- 6:00am: Arrives at town/Wheedle
- 8:05pm: Begins packing routine

**Winter:**
- 6:00am: Arrives at town/Wheedle
- 9:18pm: Begins packing routine

Schedule notes: Wheedle's booth hours vary by season. Summer has the earliest closing (8:25pm), fall even earlier (8:05pm), while winter has the latest (9:18pm). Spring is middle ground (8:45pm). He only appears on Saturdays in pleasant weather.

### Saturday Market -- Upgrade Two

The Upgrade Two schedule files (requiring quest_upgrade_the_saturday_market_plaza_complete) add Stillwell and Zorel to the market. Wheedle is not mentioned in these files, meaning his Upgrade One schedule continues unchanged after the second market upgrade.

## Cutscene Appearances

### 1. Upgrade the Saturday Market (Story Event: Town Repair)

**File:** `Cutscenes/Story Events/Town Repair/upgrade_the_saturday_market.c.toml`

**Context:** Adeline receives a letter from the Aldarian Merchant's Guild. The guild wants to add two vendors to Mistria's Saturday Market: Taliferro (Royal Chef) and Wheedle.

**Wheedle's role:** He does not appear in person. He is described by others:
- Adeline: "And uh... Wheedle. He's apparently very high up in the Merchant's Guild, specializing in extremely high-end goods."
- Nora: "You're right, I have heard about them. Supposedly, they're both real characters."
- Nora: "But I shouldn't let rumors stand in the way of letting everyone in Mistria enjoy their booths."
- The player can choose: "If it'll get my old pal Wheedle back in town, count me in!" (to which Adeline responds with surprise: "I didn't know you and Wheedle were such good friends!")

**What it reveals:** Wheedle has a pre-existing reputation. Adeline's hesitant "And uh..." and Nora's reference to "rumors" suggest his reputation is mixed at best. He is high-ranking in the Merchant's Guild. The player can optionally claim a prior friendship with him. The market upgrade requires expensive materials (8 Gold Ingots, 20 Obsidian, 20 Crystal, 100 Hard Wood, 50 Refined Stone) partly because the Merchant's Guild has "exacting requirements" for booth construction.

### 2. Balor Six Hearts (Heart Event)

**File:** `Cutscenes/Heart Events/Balor/balor_six_hearts.c.toml`

**Context:** Balor invites the player for drinks at the Inn to celebrate Mistria's business success. Wheedle interrupts uninvited.

**Who is involved:** Balor, the player, Wheedle, Hemlock (bartender)

**What happens:**
1. Balor and the player toast to Mistria's success
2. Wheedle appears uninvited: "Well doesn't this look cozy! Mind if I join?"
3. Balor is hostile: "Wheedle! Yes, actually." (meaning he does mind)
4. Wheedle ignores this and presents a contract: he represents a consortium of merchants wanting to buy out Balor's Mistrian contract rights for a large sum
5. The player can ask about the existing Mistrian businesses or their own cut; Wheedle dismisses both
6. Wheedle leaves the paperwork and departs: "Think about it, Balor."
7. Balor is visibly shaken and asks for a rain check on the meal

**What it reveals about Wheedle:** He operates as a middleman for a merchant consortium. He is willing to ambush people in social settings to close deals. He completely ignores consent and social boundaries. He knows about Balor's business operations in detail. He frames a hostile corporate takeover as a generous offer.

### 3. Balor Eight Hearts (Heart Event)

**File:** `Cutscenes/Heart Events/Balor/balor_eight_hearts.c.toml`

**Context:** Balor has arranged a special dinner for the player at the Inn. Mid-meal, Josephine interrupts to say Wheedle is downstairs demanding to see Balor about "picking up your contract."

**Who is involved:** Balor, the player, Wheedle, Josephine, Hemlock

**What happens:**
1. Balor and the player are having dinner; Balor is about to say something important
2. Josephine reports Wheedle is downstairs demanding the signed contract
3. Hemlock and Josephine try to delay Wheedle while Balor talks to the player
4. Balor asks the player what they mean to each other (friendship or romance branch)
5. Balor and the player go downstairs to confront Wheedle
6. Wheedle assumes Balor will sign: "I assume you're ready to sign that contract and leave this backwater for good?"
7. Balor refuses; Wheedle tries to negotiate, then turns hostile
8. Wheedle reveals knowledge of Balor's criminal past: "You've been stealing and cheating your way around the Capital longer than most"
9. Wheedle tries to turn the player against Balor: "This is nothing but an act. You'd better run while you still can."
10. Balor tears up the contract; Wheedle storms out without paying his tab
11. Josephine and Hemlock affirm Balor as "a true Mistrian"

**What it reveals about Wheedle:** He is persistent and escalates when denied. He has detailed knowledge of Balor's past crimes in the Capital. He views Mistria with contempt ("backwater"). When his charm fails, he resorts to personal attacks and attempts to sow distrust. He ultimately loses and retreats. Despite this confrontation, he continues operating his booth (per his follow-up line). His commercial identity overrides personal grudges.

## Quest Involvement

Wheedle is not a quest-giver. His presence in Mistria is the result of the "Upgrade the Saturday Market" quest, which the player completes by donating construction materials. He is a catalyst/antagonist in Balor's heart event storyline (six and eight hearts), where he represents external commercial interests threatening Mistria's independence.
