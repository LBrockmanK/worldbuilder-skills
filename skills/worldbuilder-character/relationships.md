# Relationships

*Sub-file for `worldbuilder-character`. Read this when writing the Relationships section. Have the current cast's character notes available — if not, open them before continuing.*

---

## Overview

A relationship defined by emotional tone gives the LLM nothing actionable. A relationship defined by behavioral dynamic gives the LLM an engine that fires in every scene where that person appears or is mentioned.

**The core rule:** Specify the current behavioral dynamic of each relationship, not its history. History belongs in the character's Environment section; the relationship entry contains what the relationship looks like right now and what it makes the character do.

**The most generative relationships** are those where the character wants two incompatible things from the same person simultaneously. A rival who secretly admires. A mentor who fears being surpassed. A friend who needs to betray. Every scene requires the LLM to navigate between competing impulses.

**Asymmetry is normal.** Relationships do not require reciprocation. A named relationship in A's card does not mean B must name A back. A one-sided attachment, an unnoticed rivalry, a care that isn't returned: these are realistic and generate behavioral content. Write only what this character actually experiences.

---

## The 12 Relationship Archetypes

Each archetype is defined by its behavioral signature — the specific way it changes what the character says, how they carry themselves, and what they want in a scene. Archetypes are a blueprinting tool for variety; they do not appear in the final card as labels. A single relationship can carry more than one archetype.

**1. Kin** — Family by blood, adoption, or found-family bond of equivalent depth. Behavioral signature: unconditional stakes without unconditional agreement. Cannot walk away without identity cost. Activates protective instincts, guilt, and loyalty that overrides rational calculation. Every character needs family context — if family is absent or dead, Ghost may substitute.

**2. Authority** — A structured power relationship: mentor, employer, elder, or superior upward; apprentice, subordinate, or ward downward. Behavioral signature: asymmetric obligation. Upward: deference, resentment, desire to prove oneself. Downward: responsibility, protectiveness, impatience, fear of failing them.

**3. Rival** — Someone who competes for the same thing: status, recognition, mastery of a shared domain. Behavioral signature: compulsive comparison. The character measures themselves against this person involuntarily. Need not be hostile — friendly rivalry is equally generative.

**4. Friction** — Someone whose personality, values, or habits create regular interpersonal irritation without rising to rivalry or enmity. Behavioral signature: reflexive annoyance modulated by social obligation. Must tolerate them due to shared community, workplace, or social circle.

**5. Obligation** — Someone the character owes, or who owes them. Behavioral signature: guilt-driven or expectation-driven action shaped by the debt rather than by feeling. Produces avoidance, overcompensation, resentment, or leveraging.

**6. Confidant** — Someone the character trusts with vulnerability, real feelings, or information hidden from others. Behavioral signature: selective emotional openness; more honest and more volatile with this person than anyone else. Must have a specific reason the trust was earned.

**7. Desire** — Someone the character is attracted to, in love with, or romantically entangled with, including unrequited feelings and past relationships. Behavioral signature: self-consciousness and altered presentation. Must include a specific complication to remain generative and avoid the love loop.

**8. Unease** — Someone genuinely ambiguous: distrusted but possibly trustworthy, admired but possibly dangerous, friendly but with motives the character cannot read. Behavioral signature: hypervigilance and interpretive uncertainty. Rated highest generativity for LLM output.

**9. Ideological Counterpart** — Someone who holds a genuinely different view on something the character cares about deeply. Behavioral signature: values-based friction that transcends personal feeling. The character may like this person but cannot let their position stand unchallenged.

**10. Community Thread** — A regular acquaintance defined by shared routine rather than deep bond. Behavioral signature: low-stakes social texture. Grounds the character in daily life; provides material for scenes that are not plot-significant.

**11. Ghost** — Someone absent (dead, estranged, departed) whose influence still shapes present behavior. Behavioral signature: reference and comparison. The character measures current situations against this person's memory, standards, or absence.

**12. Charge** — Someone the character feels self-appointed responsibility for who is not their kin and not a formal subordinate. Behavioral signature: worry and preemptive action. Produces unwanted intervention, sacrifice, and conflict when the charge resists protection.

---

## Coverage Requirements

**Major characters:** target 8 named relationships. Anchor types that should be present: a family or family-equivalent tie (Kin or Ghost), at least one power-asymmetric relationship (Authority), at least one rivalry or friction relationship, at least one Confidant. Additional entries should include at least one genuine friction source beyond rivalry — Obligation, Unease, or Ideological Counterpart.

**Supporting characters:** target 5 named relationships. Anchor types: a family or family-equivalent tie, one power-asymmetric relationship, one friction or rivalry relationship.

---

## Archetype Distribution

**The goal is variety, not accurate labeling.** When assigning archetypes, the question is not "which archetype fits this person best?" but "does the full set of relationships cover a wide range of behavioral modes?" A character whose relationships are all Community Thread, Kin, and Confidant will produce narrow, repetitive LLM output regardless of how accurately each label fits.

**Per-character repetition limit:** No single archetype should appear more than once or twice across a character's full relationship list. If an archetype is applied more than twice, treat that as a signal to reconsider: is the framing too loose, or is there a more specific archetype that would better serve behavioral variety?

**Community Thread is a last resort.** It is the lowest-generativity archetype and the easiest one to over-apply because it fits almost any low-intensity relationship. Use it only for relationships where no higher-generativity archetype is even partially applicable. If you find yourself reaching for Community Thread more than once on a single character, stop — the relationship likely has a more specific texture worth naming.

**Self-check before finalizing:** Scan the full relationship list and count how many times each archetype appears. If any archetype appears three or more times, revisit those entries. If Community Thread appears more than once, reconsider the weaker entry. Aim for at least 4–5 distinct archetypes across the full set.

---

## Writing Relationship Entries

Each entry is 2–4 sentences describing the character's own experience of this person and the behavioral dynamic between them. Write the character's side, not a neutral summary.

**Format:** Archetype label(s) and name as a table row or bold header; behavioral description in the entry.

### The Fiske relational model lens

Consider which relational model the character applies to each relationship:

- **Communal Sharing** — what's mine is yours; violation = betrayal or exclusion
- **Authority Ranking** — hierarchy with pastoral care downward, deference upward; violation = tyranny or insubordination
- **Equality Matching** — reciprocity, turn-taking, score-keeping; violation = failure to reciprocate
- **Market Pricing** — cost-benefit assessment; violation = exploitation or breach of contract

When two characters apply different models to the same relationship, the mismatch is a built-in friction source without any explicit conflict needed.

---

## Generativity Hierarchy

**Highest:** Relationships with competing obligations; relationships in transition (slowly developing a crush, recently betrayed, testing whether to trust).

**Strong:** Asymmetric relationships (one cares more, one holds a secret). Conditional alliances (allies only in specific contexts).

**Low:** Settled positive relationships without tension; simple antagonism. Both provide one behavioral mode and collapse quickly.

> **The love loop:** LLMs default toward romantic and submissive behavior. Include explicit complication in every Desire entry. Non-romantic relationships need explicit anti-romantic framing where appropriate.

> **The ally collapse:** "Close friends with X" is the least generative relationship entry. Identify the specific tension, asymmetry, or behavioral obligation that makes it more than mutual warmth.

---

## Coverage Validation

Before marking the relationships section complete:

1. **Behavioral coverage check:** "If this character appeared in a scene with any named cast member, does the card give the LLM a specific behavioral instruction for that interaction?"

2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list. Flag any archetype used three or more times for revision. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.

3. **Cast web check:** At least 2 relationships should be with other named cast members (not offscreen figures), keeping the cast's social web interconnected.

> **Community Thread is a last resort**, not a gap-filler. It provides the least behavioral specificity of any archetype. Prefer any other archetype — including Friction, Obligation, or even a weak Unease — over defaulting to Community Thread.
