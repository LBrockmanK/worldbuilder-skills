# Relationships

*Sub-file for `worldbuilder-character`. Read this when writing the Relationships section. Have the current cast's character notes available — if not, open them before continuing.*

---

## Overview

A relationship defined by emotional tone gives the LLM nothing actionable. A relationship defined by behavioral dynamic gives the LLM an engine that fires in every scene where that person appears or is mentioned.

**The core rule:** Specify the current behavioral dynamic of each relationship, not its history. History belongs in the character's Background section; the relationship entry contains what the relationship looks like right now and what it makes the character do.

**The most generative relationships** are those where the character wants two incompatible things from the same person simultaneously. A rival who secretly admires. A mentor who fears being surpassed. A friend who needs to betray. Every scene requires the LLM to navigate between competing impulses.

**Asymmetry is normal.** Relationships do not require reciprocation. A named relationship in A's card does not mean B must name A back. A one-sided attachment, an unnoticed rivalry, a care that isn't returned: these are realistic and generate behavioral content. Write only what this character actually experiences.

**No relationship requires a complement.** A character who sees someone as an Authority does not oblige a Charge on that person's side. The complement may even be true and still not belong: a teacher who shaped a student profoundly may see one student among many, formative to no particular degree. The story pressure runs from the student's end, and that is enough to write. What the card fixes is the starting state — the other character may grow into the relationship later, and that is a story event rather than a card entry.

**Perspective-focus and cross-character capture apply simultaneously.** "Write only what this character experiences" governs the relationship entry — it keeps the voice consistent and prevents the LLM from acting on unverifiable claims about another character's interior. It does not mean that insights about the other character are discarded. When writing a relationship entry reveals something true about the other person — a behavioral pattern, a motivation, a likely reaction — that insight goes into that character's cast plan entry as a Blueprint note in the cast plan in `project/plan.md`. The two rules do not conflict: the relationship entry stays perspective-focused, and the insight finds a home where it can be acted on later.

---

## The 12 Relationship Archetypes

Each archetype is defined by its behavioral signature — the specific way it changes what the character says, how they carry themselves, and what they want in a scene. Archetypes are a blueprinting tool for variety; they do not appear in the final card as labels. A single relationship can carry more than one archetype.

**1. Kin** — Family by blood, adoption, or found-family bond of equivalent depth. Behavioral signature: unconditional stakes without unconditional agreement. Cannot walk away without identity cost. Activates protective instincts, guilt, and loyalty that overrides rational calculation. Protection here is refused as often as it is accepted: family resists being handled by family, and the refusal costs more than a stranger's would. Every character needs family context — if family is absent or dead, Ghost may substitute.

**2. Authority** — Someone who holds structured power over the character: a mentor, employer, elder, or superior. Behavioral signature: deference, resentment, and the desire to prove oneself. The label always points upward. For the downward direction, use Charge.

**3. Rival** — Someone who competes for the same thing: status, recognition, mastery of a shared domain. Behavioral signature: compulsive comparison. The character measures themselves against this person involuntarily. Need not be hostile — friendly rivalry is equally generative.

**4. Friction** — Someone whose personality, values, or habits create regular interpersonal irritation without rising to rivalry or enmity. Behavioral signature: reflexive annoyance modulated by social obligation. Must tolerate them due to shared community, workplace, or social circle.

**5. Obligation** — Someone the character owes, or who owes them. Behavioral signature: guilt-driven or expectation-driven action shaped by the debt rather than by feeling. Produces avoidance, overcompensation, resentment, or leveraging.

**6. Confidant** — Someone the character trusts with vulnerability, real feelings, or information hidden from others. Behavioral signature: selective emotional openness; more honest and more volatile with this person than anyone else. Must have a specific reason the trust was earned.

**7. Desire** — Someone the character is attracted to, in love with, or romantically entangled with, including unrequited feelings and past relationships. Behavioral signature: self-consciousness and altered presentation. Must include a specific complication to remain generative and avoid the love loop.

**8. Unease** — Someone genuinely ambiguous: distrusted but possibly trustworthy, admired but possibly dangerous, friendly but with motives the character cannot read. Behavioral signature: hypervigilance and interpretive uncertainty. Rated highest generativity for LLM output.

**9. Ideological Counterpart** — Someone who holds a genuinely different view on something the character cares about deeply. Behavioral signature: values-based friction that transcends personal feeling. The character may like this person but cannot let their position stand unchallenged.

**10. Community Thread** — A regular acquaintance defined by shared routine rather than deep bond. Behavioral signature: low-stakes social texture. Grounds the character in daily life; provides material for scenes that are not plot-significant.

**11. Ghost** — Someone absent (dead, estranged, departed) whose influence still shapes present behavior. Behavioral signature: reference and comparison. The character measures current situations against this person's memory, standards, or absence.

**12. Charge** — Someone the character holds responsibility for from the stronger position: an apprentice, subordinate, or ward where the role is formal, or someone more vulnerable they have taken on themselves. Not kin — family responsibility is Kin. Behavioral signature: worry and preemptive action. Produces unwanted intervention, sacrifice, and conflict when the charge resists protection. Where the responsibility is formal, the duty is the setup and the behavior is what the character does beyond it. This is the downward counterpart to Authority.

---

## Coverage Requirements

**Major characters:** at least 8 named relationships. What those relationships are comes from the Q&A, not from a list here.

**Supporting characters:** at least 5 named relationships.

Counts are per-character. A relationship in A's list does not require a matching entry in B's list, and no archetype on one side obliges a complement on the other.

---

## Archetype Distribution

**Variety is a property of the relationships, not of the labels.** A character whose relationships are all Community Thread, Kin, and Confidant will produce narrow, repetitive LLM output however well each label fits. The fix is never to relabel. An archetype that does not describe the relationship makes the entry wrong, and the behavior generated from it wrong with it. A narrow spread means the relationships themselves are too alike: go back and change what one of them is — who the person is to this character, and what the character wants from them. Label each relationship as what it actually is, and read a monotonous distribution as the symptom that sends you back to the relationship.

**The ideal is no repeats.** No archetype should appear twice across a character's full relationship list, counting every tag on every entry. With 12 archetypes and 8 named relationships for a major character, one tag per entry leaves room to spare. Two tags on every entry does not: 16 tags against a pool that Community Thread's single-use cap already narrows will force repeats. Give an entry a second archetype only where the second one earns its place. Treat every repeat as a signal to reconsider the relationship before accepting it: is the framing too loose, or is this relationship doing the same work as another one in the set? Where a repeat survives that check, no archetype may appear more than twice.

**Community Thread is a last resort.** It is the lowest-generativity archetype and the easiest one to over-apply because it fits almost any low-intensity relationship. Use it only for relationships where no higher-generativity archetype is even partially applicable. If you find yourself reaching for Community Thread more than once on a single character, stop — the relationship likely has a more specific texture worth naming.

---

## Writing Relationship Entries

A relationship entry is a behavioral specification, not a narrative. It tells the LLM what this character does, avoids, or becomes when the other person is present or mentioned. It is written from this character's perspective: what they notice, how they read it, what it makes them do.

### What an entry is

Each entry states the behavioral dynamic of one relationship in 1-3 sentences. One sentence is the default. A complex relationship earns a second or third sentence when the additional sentence adds a behavioral pattern or cost the first sentence cannot carry. Do not expand to fill space.

**The entry is the thesis.** Form one claim per relationship about what the relationship reveals about this character. Not about the other person. About this character. Every sentence in the entry must serve this claim. When working from source material, derive the claim from the reference documents directly. Do not read the character's existing Core sections (Background, Body, Soul) while forming entries. Pre-written prose creates attractor patterns that override the claim.

### What an entry is not

**Not a scene narration.** Do not recount specific exchanges, quote dialogue, or narrate what happened in a particular conversation. The entry describes repeatable behavioral patterns, not events. Specific interactions are evidence for the writer; they do not appear in the output. The LLM needs to know what the character does whenever this person appears, not what happened one time.

**Not a neutral description.** A relationship entry is not an objective account of what two people do together. It is one character's experience of the other. This character's interpretations of what they observe are legitimate content. "She reads his visits as excuses to check on her" is perspective. "He visits with invented ailments" is neutral narration that belongs on his card, not hers.

**The swap test:** if you can swap the two names and use the entry on the other character's card, the perspective is too neutral. Rewrite it.

### Format

Bullet list. One entry per relationship. Bold `**Name:**` prefix inline on the bullet, followed by prose. Archetype annotations are working aids for distribution checking. Append them after the entry in italics during drafting; export strips them. Evidence citations follow the archetype annotation in parentheses during drafting; export strips them.

*Example — simple dynamic (1 sentence):*
```
- **Balor:** She guards her trade secrets against Balor's offers and
  uses his merchant network when it serves her. *(Friction)*
```

*Example — competing pulls (2 sentences):*
```
- **Valen:** She contests Valen's medical expertise and seeks her out
  to do it. She insists the attention is strictly professional.
  *(Friction, Desire)*
```

*Example — perspective that could not appear on the other card:*
```
- **Hayden:** She has known him since childhood, and she checks
  whether he is hurt before she registers he came to visit. She
  treats every one of his social calls as a medical encounter.
  *(Kin)*
```

### Generativity

**Highest:** Relationships where the character wants two incompatible things from the same person. A rival who secretly admires. A mentor who fears being surpassed. A friend who needs to betray.

**Low:** Settled positive relationships without tension; simple antagonism. Both provide one behavioral mode and collapse quickly.

> **The love loop:** LLMs default toward romantic and submissive behavior. Include explicit complication in every Desire entry. Non-romantic relationships need explicit anti-romantic framing where appropriate.

> **The ally collapse:** "Close friends with X" is the least generative entry. Identify the specific tension, asymmetry, or behavioral obligation that makes it more than mutual warmth.

### Per-entry self-review

After drafting each entry, run three checks:

**1. Internal-state check:** Does any sentence describe what the other character thinks, feels, or concludes internally? If yes, that content does not belong here. Log it as a Blueprint note for the other character's card.

**2. Swap check:** Could you swap the two names and use this entry on the other character's card? If yes, it has no perspective. Rewrite it.

**3. Scene-narration check:** Does any sentence recount a specific exchange, quote dialogue, or narrate an event? If yes, replace it with the behavioral pattern the event reveals.

Each entry describes only what *this* character experiences. The other character's internal life is not observable and belongs in *their* card or in their cast plan, not here.

**Remove** any claim that the other character:
- interprets, hears, reads, or takes something in a particular way
- is motivated by something internally (unless they've stated it aloud)
- feels something toward this character that hasn't been expressed behaviorally

**Displaced content** — anything you remove — should be logged as a Blueprint note in the other character's entry in the cast plan in `project/plan.md`, not simply deleted.

---

## Coverage Validation

Before marking the relationships section complete:

1. **Behavioral coverage check:** "If this character appeared in a scene with any named cast member, does the card give the LLM a specific behavioral instruction for that interaction?"

2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, reading from the working annotations on each entry. The ideal is no repeats: flag every repeat and reconsider the relationship behind it, not the annotation on it. No archetype may appear more than twice — fix any that does. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.

3. **Cast web check:** At least 2 relationships should be with other named cast members (not offscreen figures), keeping the cast's social web interconnected.

4. **Archetype fit check:** Read each entry's archetype annotation against the relationship it tags: does that archetype's behavioral signature describe what this relationship actually does? An annotation that does not fit is a defect however well it serves the distribution — fix it by changing the archetype to the one that fits, or by changing the relationship so the archetype is earned. Where a relationship the Q&A established has no entry carrying it, that is a gap worth flagging. This check imposes no list of its own: the session decides what should be present.

> **Community Thread is a last resort**, not a gap-filler. It provides the least behavioral specificity of any archetype. Prefer any other archetype — including Friction, Obligation, or even a weak Unease — over defaulting to Community Thread.
