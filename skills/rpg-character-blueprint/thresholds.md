# Influence Thresholds — Part 4

*Sub-file for `rpg-character-blueprint`. Read this when writing the Influence Thresholds section.*

---

## Part 4: Influence Thresholds

Combine behavioral stage guidance with brief in-character scenes. Show behavior — don't describe it. A brief scene at a given trust level gives the LLM a behavioral sample it can calibrate from.

### The six bands

| Band | Range | Character state |
|---|---|---|
| Hostile | -50 to -21 | Active avoidance or open conflict. Refuses the relationship or is in genuine opposition. |
| Cold | -20 to 0 | Transactional minimum. Required interactions completed; nothing volunteered. |
| Neutral | 1 to 25 | Functional. Answers what is asked; nothing extra. Default with strangers. |
| Warming | 26 to 50 | Attention begins to show. Volunteers unrequested information, small redirections. |
| Open | 51 to 70 | Personal material surfaces: specific memories, private observations, things not ordinarily shared. |
| Trusted | 71 to 100 | Full inner life: the complete argument, the thing they don't say out loud. |

### Format rules

- **All six bands required.** A blueprint with missing bands is incomplete.
- **2–4 examples per band** showing breadth of situations. One example per band is insufficient.
- **Low bands include active conflict** — not only passive avoidance. What happens when forced into proximity? What if a topic they care about regardless of trust level comes up?
- **High band:** include examples distinguishing platonic and romantic registers, marked with context in parentheses — no subheadings.
- Write examples as compact paragraphs. Brief continuous scenes. Separate with blank lines.
- **Engine format:** speech as plain text; narration/action as _asterisks_; context for the reader as (parentheses); internal thought as `backticks`.
- **Describe what THIS character specifically does.** Never write generic warmth/distance language the engine already handles automatically.
