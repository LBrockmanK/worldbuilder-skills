# Card Assembly — ainime `baseProfile`

*Sub-file for `worldbuilder-ainime-export`. Read this when assembling the `baseProfile` field for a character.*

---

## Overview

The `baseProfile` field is a single flowing prose block — no internal headers, no JSON sub-fields. It contains two parts written in sequence: the personality/description prose, then Future Storylines. The entire block is what the engine reads as "who this character is."

Source material: the character note in `notes/`.

---

## Card Prose (Personality/Description)

Weave the character note's Background, Body, Soul, and Relationships into flowing prose. This becomes the first section of `baseProfile`.

### Paragraph order

1. **Who they are at a glance** — physical presence, situational context, what a stranger notices first. The Body section's appearance preamble is the source for physical presence: include it verbatim as the physical description.
2. **How they got here** — 2–4 sentences on the formative experiences that most directly explain who they are now
3. **How they behave** — behavioral descriptions woven as natural prose (not listed)
4. **The friction** — the contradiction, the mask vs. truth, the irrational behavior
5. **Voice and speech patterns** (if distinctive) — describe concretely: "Short sentences when transactional; long structured statements when arguing" not "she speaks thoughtfully"

### Register rules

- **Write plainly. No flair.** "He deflects compliments by finding something to fix" is correct. Poetic constructions that gesture at something without stating it are wrong — the card's prose style becomes the engine's narration style.
- **No internal headers** in the card body. The prose reads as a single unbroken block.
- **No literary flair or metaphor** in descriptive text — that register belongs in dialogue. "She avoids eye contact when lying" not "her gaze slides away from truth."
- **Numbers as numerals.** 27, not twenty-seven.

### Token targets

- Supporting characters: ~900 tokens
- Major characters: ~1500 tokens

These include the Influence Thresholds. If the prose section alone reaches the token target, it is too long — cut to make room for the thresholds.

---

## Engine format

Used in Future Storylines:

- Speech: plain text
- Narration/action that appears in play: `_asterisks_`
- Context for the reader (does not appear in play): `(parentheses)`
- Internal thought: `` `backticks` ``

---

## Future Storylines

After the personality/description prose, write the Future Storylines section. Source material: the Story Seeds section of the character note. Each Story Seed entry (title, trigger/condition, scenario prose) maps to one storyline: the title becomes the storyline label, the trigger/condition becomes the storyline context, and the scenario prose is reframed from definite to possibility-style.

- Each entry phrased as possibility: "may surface," "could take," "there is a possibility that"
- Engine format applies (speech, asterisks, parentheses, backticks)
- Do not script outcomes — give the engine material to work from and let it find the moment
- Write for robustness: arcs that remain interesting whether or not a specific beat fires

**Introduction** — The character's Introduction Story Seed exports as
a Future Storyline like any other seed. The trigger condition becomes
the storyline context. The scenario prose is reframed to
possibility-style, same as other Future Storylines. Every character
must have an Introduction seed before export; a missing introduction
is a blocking deficiency.

---

## Self-Check

- [ ] Prose is in correct paragraph order (glance → history → behavior → friction → voice)
- [ ] No internal headers in the prose section
- [ ] 2–3+ behavioral descriptions woven in
- [ ] One clear contradiction or friction point
- [ ] Irrational behavior with emotional root
- [ ] Self-image gap stated directly
- [ ] Plain language throughout; no literary flair
- [ ] Token count in target range (~1500 main, ~900 side)
- [ ] Future Storylines present and phrased as possibility (if Story Seeds included)
- [ ] Introduction Story Seed present and exported as a Future Storyline
