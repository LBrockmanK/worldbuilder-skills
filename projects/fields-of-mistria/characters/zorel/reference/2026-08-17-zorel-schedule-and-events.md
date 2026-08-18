---
type: reference
title: Zorel — Schedule and Events
description: 'Extracted schedule data and cutscene appearances for Zorel: Saturday
  market schedules across seasons, basement fallback, bell tower repair questline,
  market plaza upgrade involvement.'
tags:
- agent-ready
date: 2026-08-17
timestamp: 2026-08-17T00:00Z
resources:
- projects/fields-of-mistria/source/t2/Schedules/Upgraded Market Schedules/Upgrade Two/
- projects/fields-of-mistria/source/t2/Schedules/basement_schedule.s.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Story Events/Town Repair/upgrade_the_saturday_market_plaza.c.toml
- projects/fields-of-mistria/source/t2/Cutscenes/Story Events/Town Repair/repair_the_bell_tower.c.toml
---

# Zorel — Schedule and Events

## Daily Schedule

Zorel is a visiting vendor, not a Mistria resident. She appears only on Saturdays at the upgraded market plaza.

### Basement / Default Schedule

Source: `Schedules/basement_schedule.s.toml`

- `zorel."6:00am" = "aldaria/default"`

Coverage: all (fallback for any day not overridden). Zorel defaults to Aldaria when not at the Saturday Market.

### Saturday Market Schedule (Upgrade Two — All Seasons)

Source: `Schedules/Upgraded Market Schedules/Upgrade Two/`

Prerequisites for all seasonal Saturday schedules:
- Day of week: Saturday
- Weather: pleasant
- Quest completed: repair_the_bridge
- Quest completed: upgrade_the_saturday_market
- Quest completed: upgrade_the_saturday_market_plaza

**Spring Saturday** (`u2_spring_saturday.s.toml`):
- 6:00 AM: Arrives at `town/Zorel` (her booth)
- 8:55 PM: Begins packing routine (`zorel_packing`)

**Summer Saturday** (`u2_summer_saturday.s.toml`):
- 6:00 AM: Arrives at `town/Zorel`
- 9:32 PM: Begins packing routine (`zorel_packing`)

**Fall Saturday** (`u2_fall_saturday.s.toml`):
- 6:00 AM: Arrives at `town/Zorel`
- 8:55 PM: Begins packing routine (`zorel_packing`)

**Winter Saturday** (`u2_winter_saturday.s.toml`):
- 6:00 AM: Arrives at `town/Zorel`
- 9:32 PM: Begins packing routine (`zorel_packing`)

**Schedule notes:** Zorel stays later in summer and winter (9:32 PM) versus spring and fall (8:55 PM). She does not appear on non-Saturday days, rainy Saturdays, or before the plaza upgrade quest is complete. The `zorel_packing` routine triggers distinct end-of-day conversation lines.

## Cutscene Appearances

### Upgrade the Saturday Market Plaza

Source: `Cutscenes/Story Events/Town Repair/upgrade_the_saturday_market_plaza.c.toml`

**Context:** Town meeting to discuss expanding the Saturday Market to accommodate new vendors. Nora and Adeline organize the meeting with carpenters and blacksmiths.

**Zorel's role:** Zorel does not appear in the cutscene directly. She is discussed as a vendor applicant:

- Nora [neutral]: "First off is Zorel, she's a popular musician from the Capital."
- Ryis [neutral]: "I'll say she is! My sisters wrote to me about attending one of her shows last year. And she wants to open up a vendor booth?"
- Nora [think]: "That's right. She's selling Song Crystals that play music when placed inside a special device called a Crystal Resonator."
- Nora [neutral]: "I don't pretend to understand it, but she's passionate about them and wants to spread them across Aldaria."

**What this reveals about Zorel:**
- Confirmed female ("she")
- From the Capital
- Popular musician with a reputation that reaches across Aldaria (Ryis's sisters in another region attended her shows)
- Wants to spread Song Crystals across Aldaria — a mission, not just commerce
- Passionate enough about the technology that others note it even when they do not understand it

### Repair the Bell Tower (Parts 1 and 2)

Source: `Cutscenes/Story Events/Town Repair/repair_the_bell_tower.c.toml`

**Prerequisites:** Renown level 90, completed `meet_the_new_vendors` quest. Zorel sends the initiating letter.

#### Part 1 — Planning the Repair

**Present:** Zorel, Adeline, Landen, player. Zorel is the initiator.

- Zorel [happy]: "[Ari], you came!"
- Zorel [neutral]: "I know this seems out of the blue, but I've got such good memories of this Bell Tower from when my family would visit Mistria."
- Zorel [happy]: "Hearing the bell ring out over the town every time evening fell... it was magical."
- Zorel [sad]: "I know the bell still works, but I'd really like to help out and get the rest of the tower fixed up!"

Adeline calls it "inspiring" and explains the tower was damaged in the earthquake but deprioritized since it remained functional.

Landen assesses the damage:
- Woodwork needs refreshing
- Foundation needs shoring up
- The Tower's Crystal Resonator is damaged — Landen lacks expertise with them

When Landen suggests there is no rush:
- Zorel [mad]: "Landen-"

Landen quickly volunteers free labor. Zorel [happy]: "Now we're talking!"

Zorel contributes technical knowledge about materials needed:
- Zorel [think]: "We'll need a Dragon-Forged Fang and a Dragon-Forged Core to fix the Crystal Resonator, too."
- Zorel [neutral]: "But when it's working again, I can make some upgrades so you can change the sound of the Bell's toll!"
- Zorel [happy]: "You'll even be able to play Sound Crystals in town, if you'd like. I've already got some really fun melodies in mind."

**Follow-up line (Part 1):**
- Zorel [neutral]: "Thanks again for helping out with the Bell Tower, [Ari]."
- Zorel [sad]: "It makes my heart hurt to hear the bell the way it is now."

#### Part 2 — Completing the Repair

**Present:** Landen, Ryis, Adeline, Zorel, player. Zorel handles the Crystal Resonator repair.

- Ryis [neutral]: "Zorel, it's safe to come in and fix the Crystal Resonator!"
- Zorel [happy]: "The resonator is fully repaired! I've already put in some new bell tunes if anyone wants to play around with it later."
- Zorel [neutral]: "And before we go..."

**Follow-up line (Part 2):**
- Zorel [neutral]: "The bell's sounding great now, huh?"
- Zorel [happy]: "It's nice to think my melodies will sound out over Mistria from now on."

**What these cutscenes reveal about Zorel:**
- Childhood connection to Mistria through family visits — not a stranger to the town
- Deep emotional attachment to the Bell Tower's sound specifically
- Technical expertise with Crystal Resonators — she is the one who repairs it, not the carpenters
- Shows impatience/frustration (rare "mad" portrait) when Landen is dismissive about urgency
- Takes pride in her craft: prepares melodies in advance, wants her music to become part of Mistria's daily life
- Leadership: she organized the meeting, recruited town officials, contributed the technical plan
- Legacy-minded: "my melodies will sound out over Mistria from now on" echoes the packing-up line about performances lasting hundreds of years

## Quest Involvement

### Quest: Upgrade the Saturday Market Plaza
- Zorel is a beneficiary (gains a booth) but does not appear in the planning cutscene
- Materials required for new vendor booths: 50 Voidite, 20 Refined Stone, 5 Mistril Ingots, 10 Monster Cores, 5 Monster Blocks

### Quest: Meet the New Vendors
- Triggered by letter from Nora after plaza upgrade
- Player visits Zorel (and Stillwell) at the market for the first time

### Quest: Repair the Bell Tower
- Initiated by Zorel's letter at renown 90
- Zorel is the driving force and Crystal Resonator specialist
- Materials: 20 Refined Stone, 30 Hardwood, 1 Dragon-Forged Fang, 1 Dragon-Forged Core
- Reward: Player can change bell sound and play Sound Crystals in town
