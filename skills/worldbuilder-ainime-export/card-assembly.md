# Card Assembly — ainime `baseProfile`

*Sub-file for `worldbuilder-ainime-export`. Read this when assembling the `baseProfile` field for a character.*

---

## Overview

The `baseProfile` field is a single flowing prose block — no internal headers, no JSON sub-fields. It contains two parts written in sequence: the personality/description prose, then the Influence Thresholds, then Future Storylines. The entire block is what the engine reads as "who this character is."

Source material: the character note in `notes/`.

---

## Card Prose (Personality/Description)

Weave the character note's Foundation, Behavioral Descriptions, Relationships, and Relationship Behavior into flowing prose. This becomes the first section of `baseProfile`.

### Paragraph order

1. **Who they are at a glance** — physical presence, situational context, what a stranger notices first
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

## Influence Thresholds

After the personality/description prose, write the influence thresholds. These show the engine how the character behaves at each trust level through short in-character scenes — not behavioral descriptions, but actual moments.

### The six bands

| Band | Range | Character state |
|---|---|---|
| Hostile | -50 to -21 | Active avoidance or open conflict. Refuses the relationship or is in genuine opposition. |
| Cold | -20 to 0 | Transactional minimum. Required interactions completed; nothing volunteered. |
| Neutral | 1 to 25 | Functional. Answers what is asked; nothing extra. Default with strangers. |
| Warming | 26 to 50 | Attention begins to show. Volunteers unrequested information, small redirections. |
| Open | 51 to 70 | Personal material surfaces: specific memories, private observations, things not ordinarily shared. |
| Trusted | 71 to 100 | Full inner life: the complete argument, the thing they don't say out loud. |

### Deriving bands from Relationship Behavior

The character note's Relationship Behavior section describes the behavioral axis in prose. Map it to bands:

- **Default register** → Neutral band. This is the baseline the engine starts from.
- **Distance / coldness** → Cold band. What the note describes as distance is the Cold state; amplify slightly for Hostile.
- **Active conflict / friction** → Hostile band. If the note describes how this character behaves in genuine opposition, that is Hostile. If not described explicitly, extrapolate from the distance pattern.
- **Warmth beginning to show** → Warming band. The first signs of engagement described in the note.
- **Personal material, specific sharing** → Open band. What the note describes as warmth becoming present.
- **Full inner life, no reserve** → Trusted band. The deepest end of what the note describes as warmth.

If the Relationship Behavior section describes variation by relationship type (authority vs. peers, etc.), reflect that variation across bands where it's significant — particularly in high bands.

### Format rules

- **All six bands required.** A card with missing bands is incomplete.
- **2–4 examples per band** showing breadth of situations.
- **Low bands include active conflict** — not only passive avoidance. What happens when forced into proximity? What if a topic they care about regardless of trust comes up?
- **High band:** include examples distinguishing platonic and romantic registers, marked with context in parentheses. No subheadings.
- Write examples as compact scenes. Separate with blank lines.
- **Describe what THIS character specifically does.** Never write generic warmth/distance language the engine already handles automatically.

### Engine format

Used in Influence Thresholds and Future Storylines:

- Speech: plain text
- Narration/action that appears in play: `_asterisks_`
- Context for the reader (does not appear in play): `(parentheses)`
- Internal thought: `` `backticks` ``

---

## Future Storylines

After the influence thresholds, write the Future Storylines section. Source material: the Storylines section of the character note.

- Each entry phrased as possibility: "may surface," "could take," "there is a possibility that"
- Engine format applies (speech, asterisks, parentheses, backticks)
- Do not script outcomes — give the engine material to work from and let it find the moment
- Write for robustness: arcs that remain interesting whether or not a specific beat fires

**Introduction** — The character's introduction is its own story note in `notes/` (not a Storylines entry and not in the card). Do not add an Introduction entry here. Verify the introduction note exists before finalizing the character export.

---

## Self-Check

- [ ] Prose is in correct paragraph order (glance → history → behavior → friction → voice)
- [ ] No internal headers in the prose section
- [ ] 2–3+ behavioral descriptions woven in
- [ ] One clear contradiction or friction point
- [ ] Irrational behavior with emotional root
- [ ] Self-image gap stated directly
- [ ] Plain language throughout; no literary flair
- [ ] Token count in target range (prose + thresholds combined)
- [ ] All six influence bands present
- [ ] 2–4 examples per band
- [ ] Low bands include active conflict, not only avoidance
- [ ] High band has both platonic and romantic examples
- [ ] Future Storylines present and phrased as possibility
- [ ] Introduction note exists separately; no Introduction entry in the card
