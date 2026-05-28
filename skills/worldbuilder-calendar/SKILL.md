---
name: worldbuilder-calendar
description: Use when designing the calendar, festivals, recurring events, or daily planner directive for an AI-powered RPG or interactive fiction with time-based scene structure. Also use when events feel arbitrary, when the festival calendar lacks thematic variety, or when the daily planner directive is generating scene structures that are too repetitive or too unpredictable.
---

# RPG Calendar

## Overview

The calendar serves two functions: it structures the engine's sense of time, and it provides recurring emotional anchors that make the setting feel alive. Festivals and events are narrative directives injected into the planner on specific days — they shift the emotional register of scenes that day without scripting what happens.

---

## Calendar Fields

**Season length:** Common default is 28 days. Longer seasons feel more immersive; shorter seasons allow more annual events.

**Day segments:** Morning / Afternoon / Evening / Night. Four segments is the standard. The daily planner directive governs how the engine structures each.

**Era:** The technology/cultural reference point for the setting. A single phrase used by the engine to calibrate anachronism.

**Weather pool:** 6–8 types with varying narrative weight. Include some that are purely atmospheric (clear morning, light fog) and some that carry narrative energy (storm, oppressive heat, the first frost, unseasonable warmth). Weather affects scene mood without dictating scene content.

---

## Event Types

**Recurring annual events** repeat on the same relative day every year. Use for festivals, cultural observances, community rituals — anything that structures the calendar's emotional rhythm.

**One-time events** fire once and are done. Use for opening arc milestones, first-year setup moments, things that can only happen once.

**Daily Planner Directive** applies to every single day. It is not an event — it is standing instruction for scene structure.

---

## Festival Calendar Template

One major festival per season plus minor observances. Major festivals define the season's emotional register. Minor observances add texture without requiring full scenes.

```
SEASON 1
- Day 8:  [Major — communal, renewal theme, natural introduction opportunity]
- Day 20: [Minor — trade/market, outsiders in community]

SEASON 2
- Day 7:  [Minor — leisure, social, relaxed]
- Day 21: [Major — the one where the hidden layer is most present; night event]

SEASON 3
- Day 5:  [Minor — practical community work]
- Day 18: [Major — harvest equivalent; abundance + underlying melancholy]
- Day 26: [Minor — day of remembrance; quiet, grief-adjacent]

SEASON 4
- Day 10: [Minor — practical market, before deep cold / difficult period]
- Day 22: [Major — solstice/darkest equivalent; intimate, stories, things said in darkness]
```

Adapt the seasonal labels to the setting's actual time structure.

### Writing event descriptions

Write recurring event descriptions as atmospheric and directional, not specific. They set the stage; the engine generates contextually appropriate content based on current relationship states and player history.

The same event at year one should feel different from year three — not because the description changed, but because the relationships and history have. Don't script what happens; set the tone and permission space.

**Cover in each description:**
- The time of day and physical setting
- The community's mood and collective behavior
- What kinds of interactions are natural on this day
- Any tradition or ritual that anchors it
- The emotional register — what does this day feel like

---

## Daily Planner Directive

The directive handles scene structure for every day. It should establish:

1. **Scene purpose variety** — atmospheric/mundane scenes are valid and desirable; not every scene needs to be emotionally significant; specify that explicitly
2. **Time-of-day social rhythms** — who is naturally awake, active, and social at what point in the day
3. **Escalation ceiling** — maximum one emotionally significant beat per day under normal circumstances; multiple significant beats in a single day should feel exceptional
4. **Transition handling** — brief narrative acknowledgment between Morning / Afternoon / Evening / Night
5. **Player disruption response** — when the player drives a scene somewhere unexpected, follow their lead, then let the next scene settle before introducing new material

The directive is the structural complement to the romance pacing and pacing guidance in Story Direction. Together they prevent both flatness (no weight) and escalation addiction (too much weight, too often).

---

## Working Principles

**Events are directives, not scripts.** The engine uses them to set emotional context for that day. Describe the kind of day it is and what that makes natural — not specific things that happen.

**Minor observances have outsized texture value.** A small day-of-remembrance that most characters mark privately produces more naturalistic behavior than another major festival. Not every cultural moment needs to be a celebration.

**One-time events anchor the opening arc.** Use them for the player's introduction to specific households, community moments that establish the current state of the setting, and early beats that can only happen once.

**The daily planner directive is the most important calendar document.** Festivals are moments; the directive is the rhythm every day runs on. A well-written directive produces varied, naturalistic day structure. A poorly-written one produces either relentless sameness or chaos.
