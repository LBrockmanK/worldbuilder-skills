# Assembly Guide — Part 3

*Sub-file for `rpg-character-blueprint`. Read this when writing the Personality/Description prose and when finalizing the card.*

---

## Part 3: Assembly Guide

Weave Parts 1 and 2 into flowing prose. This becomes the Personality/Description field — the core of the card.

### Paragraph order

1. **Who they are at a glance** — physical, situational, immediately visible
2. **How they got here** — 2–4 sentences on the formative experiences that most directly explain who they are now
3. **How they behave** — behavioral descriptions woven as natural prose (not listed)
4. **The friction** — the contradiction, the mask vs. truth, the irrational behavior
5. **Voice and speech patterns** (if distinctive) — describe concretely: "Short sentences when transactional; long structured statements when arguing" not "she speaks thoughtfully"

### Formatting rules

- **The blueprint register is functional, not literary.** Plain, direct language throughout. The blueprint is a spec document, not a draft of the card prose. "He deflects compliments by finding something to fix" is a blueprint sentence. If a sentence sounds like it belongs in a novel, rewrite it as a plain statement.
- **Overly poetic usually means overly vague.** Poetic constructions tend to gesture at something without stating it. State it.
- **Section discipline.** Each section carries information the others don't. Soul and behavioral descriptions describe general patterns — if a behavior is primarily about one specific relationship, it belongs in Relationships, not here. History and formative events using named people belong in Environment. Redundancy between sections usually means content is in the wrong place.
- **No literary flair or metaphor in descriptive text** — that register belongs in dialogue. "She avoids eye contact when lying" not "her gaze slides away from truth." The card's register becomes the LLM's narration register.
- **No internal headers inside the final card's prose field.** The card reads as unbroken text.
- **Numbers as numerals.** 27, not twenty-seven.
- **Token target.** ~900 tokens for supporting characters; ~1500 tokens for major characters.

### Engine format for in-character content

Used in Influence Thresholds and Future Storylines:
- Speech: plain text
- Narration/action that appears in play: _asterisks_
- Context setting for the reader (does not appear in play): (parentheses)
- Internal thought: `backticks`

---

## Self-Check Before Finalizing

Run this before marking the blueprint complete.

**Personality/Description**
- [ ] Prose, not a list of traits
- [ ] 2–3+ behavioral descriptions woven in
- [ ] One clear contradiction or friction point
- [ ] Irrational behavior with emotional root
- [ ] Self-image gap stated directly
- [ ] Speech patterns described concretely if distinctive
- [ ] Plain language throughout — no literary flair in narration
- [ ] ~900 (supporting) or ~1500 (major) tokens

**Influence Thresholds**
- [ ] All six bands present
- [ ] 2–4 examples per band
- [ ] Low bands include active conflict, not only avoidance
- [ ] High band has both platonic and romantic examples

**Future Storylines**
- [ ] Introduction entry present
- [ ] All entries phrased as possibility, not script

**Metadata**
- [ ] Events noted if applicable
- [ ] All core fields present
- [ ] Appearance consistent with description
- [ ] Sprite Sets listed (artwork states, not expressions)
