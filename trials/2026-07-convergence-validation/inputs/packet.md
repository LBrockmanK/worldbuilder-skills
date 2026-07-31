# Character Generation Instruction Packet

## Skill Instructions

### skills/worldbuilder-character/SKILL.md

---
name: worldbuilder-character
description: Use when building or developing a character for an AI-powered RPG or collaborative fiction — creating from scratch, deepening an existing character note, or fixing a character who feels flat, inconsistent, or generating repetitive LLM output.
---

# Character Blueprint

*All prose this skill produces follows `../writing-style.md`. Read it before writing.*

## Overview

A character for an LLM-powered game is not a description — it is a behavioral specification. The engine handles generic social warmth and distance; the character note supplies the specific: what this character carries privately, what they do when trust is low or high, what their contradiction is.

The character note is the comprehensive single source of truth for a character in the Wide phase. It is richer than any export format can hold — it contains everything true about the character, including material that won't appear in any platform output. Export skills derive their output from this note.

**Description field:** the cast navigation summary — who this character is in the world, their key traits, and their place in the social ecosystem. Described, not prescribed: no relationship recommendations, no design rationale. Written last, after the full blueprint is complete; other agents scan it across the roster to understand each character without opening their notes.

---

## Character Note Structure

Work through sections in order. Do not skip sections because the character seems simple — every section exists to catch what the others miss.

| Section | Sub-file | Notes |
|---|---|---|
| Design Notes | — | Builder record; H3 subheadings; excluded from exports |
| Background | `framework.md` | Declarative context; different in kind from behavioral sections |
| Body | `framework.md` | Physical behavioral descriptions |
| Soul | `framework.md` | Psychological + social behavioral descriptions |
| Relationships | `relationships.md` | Named relationships; bullet format |
| Intimate Dynamics (if flagged) | `intimate.md` | Only if flagged in project plan |

Frontmatter is defined by the project's OKF registry; `new_doc.py` stamps it at creation and the generated rules describe it. The script produces a date-prefixed filename; rename the fresh note to the character's name itself (e.g. `notes/Maren Holt.md`) before adding content — the filename convention the templates state, and safe while nothing links to the note yet.

---

## Design Notes

Design Notes is the builder record — it captures what drove the design of this character. Excluded from all exports. Two H3 subheadings:

### Session Notes

Q&A capture: what the user said they wanted this character to be. Written during the Q&A phase, before any note sections are drafted. Raw intent, plain language, bullet points. Future agents revisiting this character read Session Notes first to understand original intent before examining the behavioral sections.

### Builder Context

Narrative function, external references, design decisions, open questions. Bullet points. Leave blank if there is nothing worth capturing — do not pad.

Typical bullets for Builder Context:
- Narrative function: what this character uniquely contributes to the setting; what tensions or themes they embody
- External references: named real people, fictional characters, or combinations that shaped the design; what specifically was drawn from each
- Design decisions and constraints: choices made that would be confusing without context
- Open questions: unresolved decisions to revisit in future sessions

Imported character cards: judge by behavioral specificity, negative-track content, and connections; a card failing more than one needs the full pass, not transcription.

---

## Session Flow

Before writing any note section, conduct a Q&A with the user. Ask one question at a time — this is a conversation, not a checklist delivered in bulk.

**Technique:**

- **One question at a time.** Ask one, wait for the answer, ask the next.
- **Offer a hypothesis.** After each answer, surface what it implies: "Based on that, she might be afraid of being truly seen — does that sound right?" Give the user something to confirm, redirect, or build on.
- **Follow threads.** When an answer opens something up, pursue it before moving topics. A Background answer that implies a Soul pattern should be surfaced immediately: "You said she was the reliable one — that might mean her irrational behavior is overcommitting even when she can't afford to. Does that track?"
- **Sharpen vague answers.** "She has trouble trusting people" is not enough. Ask what that looks like: does she test people, avoid closeness, or extend trust and then panic when it's taken seriously?
- **Check Intimate Dynamics flag first.** Before beginning Q&A, check whether the character is flagged for Intimate Dynamics in the project plan. If flagged, include intimate coverage in the Q&A (see coverage list below). If not flagged, do not raise it.

**Coverage before writing begins:**

- Background: origin, class/culture, key formative events, current situation and how they feel about it
- Body: appearance, any notable physical self-consciousness, embodied habits
- Soul (psychological): core want beneath the surface want, core fear, self-image gap, irrational behavior and its root
- Soul (social behavior): how they are with strangers, what warmth looks like, what distance or friction looks like
- Relationships: who the named cast is, which relationships matter most to this character, the behavioral dynamic of each — what it makes them do when that person is present or mentioned. Then as separate questions: who counts as family, who they answer to, who depends on them, who they clash with, who they would tell the truth to. An absence here is an answer: note it and move on.
- Intimate Dynamics: if the character is flagged for intimate dynamics (check project plan first), also cover how they express attraction, what makes them hold back, and any specific dynamic that drives their intimate behavior

The Q&A ends when the agent has confident, specific answers across all coverage areas. Capture answers in Design Notes → Session Notes before moving to note writing.

---

## Writing Rules

These rules apply to all behavioral sections (Body, Soul, Relationships, Intimate Dynamics). Two bans reach every section, Background included: the rule below on deciding what not to specify, and the ban on heavy trait adjectives in `../writing-style.md`.

**Make decisions, don't hedge.** Every fact in the note is a decision. Never write "X or Y" or "grew up somewhere, perhaps Y" unless the ambiguity is a deliberate mystery being preserved. If you don't know, ask the user.

**Decide what not to specify.** This is not the same as the hedging rule above: hedging governs what you commit to when you do write a fact, and this governs which facts you decline to write at all. See *Decide what not to specify* in `../writing-style.md`.

**Write plainly. No flair.** Write each behavioral description the way a screenplay writes action lines: present tense, only what can be seen or heard, no internal states, short plain sentences. If a director cannot stage the sentence, rewrite it. For vocabulary: shortest Anglo-Saxon word that works, active voice, cut every word that can go. See `../writing-style.md` for the full style model.

**Write what characters ARE, not what they aren't.** Positive statements give the LLM something to act on. Negative constructions define by absence — the LLM has to invent the positive case itself. State the fact directly. Factual negatives are fine when the un-done thing is the meaningful information: "she has not sent the letter," "he hasn't asked."

**The note describes the character's starting state.** Nothing in the note may reference events that haven't happened yet. Check: has this already happened before the player meets this character? If not, create a story note or cut it.

**Section discipline.** Each section carries information the others don't:
- Background: where they came from (facts, not behavior)
- Body: behaviors grounded in physical experience
- Soul: general psychological and social patterns
- Relationships: behaviors specific to named individuals

Physical description (appearance, carriage, notable physical traits) belongs in Body — it is the physical reality that produces behavior, not a separate Appearance section.

If a behavior is primarily about one specific relationship, it belongs in Relationships. If a behavioral pattern is general (appears with many people), it belongs in Soul. Redundancy between sections means content is in the wrong place.

**Asymmetry in relationships is normal.** A named relationship does not require the other character to name it back. Write only what this character actually experiences.

---

## Background, Body & Soul

See `framework.md` for construction format, coverage requirements, the When/Behavior/Because formula, and examples for all three sections.

---

## Relationships

See `relationships.md` for the full relationship archetypes, coverage requirements, generativity hierarchy, perspective-focus rules, and entry format.

---

## Story Notes

**Story notes instead of inline storylines.** Story possibilities for this character live in separate story notes, not in the character note. When you have enough clarity on a character's arc, create a story note with intention scope and link it back to this character. See `worldbuilder-story` for story note structure.

The introduction note is also a story note (introduction scope). When you have enough character clarity to know where and how the player would first meet this character, create it then.

---

## Intimate Dynamics

Check the project plan before starting any blueprint. If the character is flagged for intimate dynamics, read `intimate.md` before beginning the Soul section. If the flag is absent, skip `intimate.md` entirely — do not prompt for it or ask about it.

---

## Post-Group Sync Pass

After completing a household group or batch of characters, run a relationship sync pass before moving on. Characters develop during the blueprinting sequence — a character written later may shift in ways that make an earlier character's relationship entry inaccurate. Check the group's notes against each other: are named relationships still consistent? Update when the sequence reveals something that changes the picture.

---

## Self-Check Before Marking Complete

The note stays on an open status tag while work is in progress; mark it `complete` when every item below passes.

**Frontmatter**
- [ ] Fields match the generated rules; `factions` links to this character's faction notes

**Design Notes**
- [ ] `### Session Notes` present with Q&A capture
- [ ] `### Builder Context` present as applicable; not padded

**Background**
- [ ] Declarative fact pairs only — no behavioral content, no prose elaboration

**Body**
- [ ] Entries grounded in physical experience
- [ ] No forced entries — thin is acceptable if nothing is distinctive

**Soul**
- [ ] 3–5 psychological behavioral entries minimum
- [ ] 2–3 general social behavior entries minimum
- [ ] One contradiction stated as a behavioral description
- [ ] Irrational behavior with emotional root present
- [ ] Self-image gap expressed as behavioral description
- [ ] Speech patterns described concretely if distinctive
- [ ] Because clauses trace to the user's stated wants, fears, or experiences from Session Notes — if a Because clause didn't emerge from the Q&A, ask the user before writing
- [ ] Plain language throughout — no literary flair, no Latinate vocabulary
- [ ] No heavy trait adjectives anywhere in the note; each replaced by the behavior that earned it
- [ ] Where the blueprint states an expertise, it also states where that expertise stops
- [ ] At least one standing pressure of the character's own, shown through what they do about it
- [ ] The character's direction is left unresolved: competing pulls, no chosen future
- [ ] Across every section, details that do not change behavior are left unwritten
- [ ] No negative-led characterization (state what they ARE)
- [ ] No forward references (starting state only)

**Relationships**
- [ ] Coverage requirements met: 8 named relationships for major characters, 5 for supporting; required anchor types present (family or Ghost, Authority or Charge, friction or rivalry, Confidant; see `relationships.md` for full requirements)
- [ ] Each entry in bullet format with `**Name — Archetype(s):**` prefix
- [ ] Each entry describes behavioral dynamic, not history or emotional label
- [ ] Each entry describes this character's experience only, not the other person's traits

**Intimate Dynamics (if flagged)**
- [ ] Behavioral entries covering attraction expression, hesitation/limits, specific dynamic if present
- [ ] One friction point present

**Story Notes**
- [ ] Story notes created or flagged as pending for any known character arcs
- [ ] Introduction note created or flagged as pending

**Pre-Handoff Scan**
- [ ] Before moving to the next character, scan the session for any decisions made about characters who do not yet have a complete note
- [ ] Record any such decisions as a Blueprint note in that character's cast plan entry in `project/plan.md`

**Description**
- [ ] `description` written last and reflects the completed character; no recommendations, no design rationale


### skills/worldbuilder-character/framework.md

# Character Framework — Background, Body & Soul

*Sub-file for `worldbuilder-character`. Read this when working on the Background, Body, and Soul sections.*

---

## Background

Where this character comes from. This section is different in kind from the sections that follow — it is causal context, not behavioral output. Read it to understand why behavioral descriptions exist; do not restate its content in Body or Soul.

**Format:** Bullet list. One entry per fact pair:

- [Formative fact] → [what it made true]

No prose, no elaboration beyond the pair. No behavioral framing — if the fact implies a behavioral pattern, that pattern belongs in Body or Soul as a behavioral description.

*Example pair (correct — stays factual):*
- Grew up working-class in a trade city, left at eighteen → never returned to the neighborhood, never explained why

*Anti-example (wrong — crosses into behavioral framing):*
- Grew up working-class → learned to hide vulnerability and distrust people who have things too easy

(The anti-example's second half belongs in Soul, not Background.)

**What to cover:**
- Origin: where they grew up, what class and culture shaped them, what was valued and looked down on
- Formative events: key experiences and turning points that changed their trajectory
- Current situation: where they are now and how they feel about it (content, stuck, restless)

---

## Body

Physical behavioral descriptions — how this character's physicality shapes behavior in the world.

**Format:** Bullet list. One behavioral description per bullet, written as a prose sentence. The When/Behavior/Because structure is a writing guide — do not label the parts in the output. The sentence embeds all three elements naturally.

**Coverage prompts** (not all require an entry — only those where the character has distinctive behavior related to their physicality, regardless of whether the physical trait itself is unusual):
- Appearance and how it draws or deflects attention
- Physical self-consciousness or pride and what it produces in behavior
- Embodied habits: how they carry themselves, what they do with their hands, how they occupy space

Thin Body sections are acceptable when nothing about a character's physicality is distinctive. Do not force entries.

*Example:*

- When she enters a room she doesn't know, she finds a wall or corner first. She grew up visible in ways she didn't choose, and learned to make herself an observer before becoming a subject.

---

## Soul

Psychological and general social behavioral descriptions. Three coverage areas written together as a single bullet list — no subheadings.

**Format:** Bullet list. One behavioral description per bullet, written as a prose sentence.

### The Formula

> When [trigger], they [behavior], because [underlying reason].

The formula is a construction guide. Write prose sentences that embed all three elements naturally — do not label the parts.

**The staging test:** Can a director stage the behavior in this sentence? If not, rewrite it. Internal states are not stageable — convert them into observable action.

- Fails: "She has no language for it."
- Passes: "When this comes up, she goes quiet and doesn't re-engage until the subject passes."

The Because clause earns a limited exemption. It may name an internal state if the state is specific: "because the last time she trusted someone fully, they left anyway" — not "because something in her resists."

### Why behavioral descriptions outperform trait labels

| Trait | Label (avoid) | Behavioral (use) |
|---|---|---|
| Confident | "She is confident." | "When challenged, she responds with certainty, treating doubt as a personal insult rather than a reasonable position." |
| Stubborn | "He is stubborn." | "When someone pushes back, he doubles down. Changing his mind feels like losing, and he does not lose." |
| Kind | "They are kind." | "When someone is struggling, they drop everything to help, partly because they care, partly because being needed is the only time they feel valuable." |
| Nervous | "She is anxious." | "In new social situations she over-prepares what to say, then abandons all of it and talks too fast. She apologizes for things that are not her fault." |

Labels give the LLM one word to repeat. Behavioral descriptions force it to generate language that fits the behavior — dramatically more varied output.

**Heavy trait adjectives are banned outright**, in every section. The ban and the replacement formula are in *Describe behavior, not labels* in `../writing-style.md`. The table above and the example below are the character-specific worked cases.

- Wrong: "She is highly intelligent and analytical."
- Right: "She rereads every contract twice and catches the clause everyone else missed, because one bad signature cost her a job at 24. She cannot sign off on anything without checking it three times, which makes her slow under pressure."

The rule's other branch covers traits that are not competences: name the behavior that makes people reach for the word, and what it costs.

- Wrong: "He is arrogant and dominant."
- Right: "He finishes other people's sentences wrong, then corrects them on the correction. His team stopped bringing him problems early, so he hears about them once they are expensive."

### Knowledge boundaries

Wherever the blueprint states the character has expertise, state where that expertise stops. Unbounded competence produces a character who somehow knows everything about everything, because nothing in the note says otherwise. Per-topic depth beats a global claim of intelligence. The boundary goes in the Soul bullet list as a behavioral description, not as a standalone note.

- Wrong: "She's the smartest person in the room and can handle anything that comes up."
- Right: "She can price a shipment of grain to the coin and knows which merchants are lying about a bad harvest. She has never read a legal contract and hands those to someone else without embarrassment."

### A life in motion

The character carries ongoing pressures of their own — money, family, obligations — that move on their own timeline whether or not the player is present. These give the character something to act on beyond reacting to the player. They are standing pressures in the present, not scheduled events: a debt already owed and a letter already unanswered are starting state, while a betrayal the character has not yet committed is a forward reference and belongs in a story note. The pressure goes in the Soul bullet list as a behavioral description, not as a standalone note.

- Wrong: a character whose only stated concerns are things the player raises first.
- Right: "She counts the rent money twice a week and moves the short amount between two jars. When her brother's name comes up she changes the subject and starts sorting the mail."

### Coverage

Soul covers three areas. Write them together as a single bullet list with no subheadings.

**Psychological patterns (3–5 entries minimum):**
- Emotional triggers and responses
- Core drives in action — what does wanting to be respected actually look like when they're in a room?
- Irrational behavior with its emotional root (required — separate entry from contradiction)
- Self-image gap expressed as behavioral description
- Contradiction between presented self and actual self (required — a second separate entry; names the gap between what they present and what is actually true)

> **Why the irrational behavior entry matters most:** LLMs default to writing rational, helpful-assistant-style characters. An irrational behavior with a clear emotional root forces the LLM to generate responses that feel human rather than algorithmic. It is the single most effective thing in this framework.

**General social behavior (2–3 entries minimum):**
- Default mode with strangers — what a first encounter with this character feels like
- What warmth looks like when it appears — specific behavior, not "they become warm"
- What distance or friction looks like — specific behavior, not "they become cold"
- Relationship-type variation if it exists (with authority figures vs. peers vs. someone they're protecting)

*Example social behavior entry:*
- When meeting someone new, she asks questions and lets them fill the space. She learned early that people reveal more when they think they're not being evaluated.

**Boundaries and ongoing pressures:**
- A standing pressure of the character's own, shown through what they do about it (1 entry minimum)
- Where a stated expertise stops — what the character does when a question falls outside it. Required for each expertise the blueprint states; omit if it states none.

If the character has a distinctive speech pattern, include one entry describing it concretely.

### Contradictions

The most interesting characters contain contradictions. A character with no friction between what they want and what they do gives the LLM nothing to work with. The contradiction must appear as a behavioral description in the Soul bullet list — not as a standalone note.

- What do they present vs. what is actually true?
- What would make them change — what experience, person, or realization could break the pattern?

**Leave the direction unresolved.** The present must hold live competing pulls, not settled facts. A resolved fact is a shortcut around the work of finding out who the character is right now; an unresolved tension forces that discovery in every scene. Leave multiple futures open, none of them chosen.

- Wrong: "She has decided to leave the guild once the debt is paid."
- Right: "She keeps a half-packed bag under her bed and adds to the guild's ledger anyway. Some weeks she counts the debt down. Some weeks she pays more than she owes."

### The Because clause

The Because clause carries the psychological root. Draw it from the Q&A session capture in Design Notes — do not invent psychology the user has not provided. If no session note speaks to a specific behavior's root, ask before writing. If no Design Notes exist yet, provide a reasoned psychological root and flag it for user review.


### skills/worldbuilder-character/relationships.md

﻿# Relationships

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

Each entry is 2–4 sentences describing the character's own experience of this person and the behavioral dynamic between them. Write the character's side, not a neutral summary.

**Format:** Bullet list. One entry per relationship. Bold `**Name — Archetype(s):**` prefix inline on the bullet, followed by behavioral description as prose sentence(s).

*Example bullet:*
```
- **Mira — Kin:** When Mira dismisses her ideas in front of others, she doesn't argue — she brings the idea back later, one-on-one, where Mira has room to change her mind without losing face.
```

### The Fiske relational model lens

Consider which relational model the character applies to each relationship:

- **Communal Sharing** — what's mine is yours; violation = betrayal or exclusion
- **Authority Ranking** — hierarchy with pastoral care downward, deference upward; violation = tyranny or insubordination. This is a lens on how the relationship works, not an archetype label: the archetype for the downward direction is Charge, not Authority.
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

### Per-entry self-review: internal state check

After drafting each entry, read it back and ask: **does any sentence describe what the other character thinks, feels, or concludes internally?** If yes, that content does not belong here.

Each relationship entry describes only what *this* character experiences — what they observe, how they interpret it, and what it makes them do. The other character's internal life is not observable and belongs in *their* entry or in their cast plan, not here.

**Remove** any claim that the other character:
- interprets, hears, reads, or takes something in a particular way
- is motivated by something internally (unless they've stated it aloud)
- feels something toward this character that hasn't been expressed behaviorally

**Displaced content** — anything you remove — should be logged as a Blueprint note in the other character's entry in the cast plan in `project/plan.md`, not simply deleted. It may be accurate; it just doesn't belong in this character's voice.

**Worked example — Friction entry (Sophie's card, about Vesper):**

> Wrong: "Sophie pushes back on Vesper's decisions and Vesper hears it as normal grousing."

> Right: "Sophie pushes back on Vesper's decisions; Vesper doesn't change course."

The wrong version tells us how Vesper internally classifies Sophie's pushback ("normal grousing"). Sophie cannot know that. The right version reports only what Sophie observes — Vesper's behavior — and leaves Vesper's internal interpretation where it belongs: in Vesper's card.

This check applies to all entries, not just conflict-laden ones. Even positive relationships can slip into describing the other person's interior ("she knows Vesper cares about her") when only the behavior is visible ("Vesper checks in after every hard session").

---

## Coverage Validation

Before marking the relationships section complete:

1. **Behavioral coverage check:** "If this character appeared in a scene with any named cast member, does the card give the LLM a specific behavioral instruction for that interaction?"

2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, counting every tag on every entry. The ideal is no repeats: flag every repeat and reconsider the relationship behind it, not the label on it. No archetype may appear more than twice — fix any that does. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.

3. **Cast web check:** At least 2 relationships should be with other named cast members (not offscreen figures), keeping the cast's social web interconnected.

4. **Archetype fit check:** Read each entry's archetype against the relationship it tags: does that archetype's behavioral signature describe what this relationship actually does? A label that does not fit is a defect however well it serves the distribution — fix it by changing the archetype to the one that fits, or by changing the relationship so the archetype is earned. Where a relationship the Q&A established has no entry carrying it, that is a gap worth flagging. This check imposes no list of its own: the session decides what should be present.

> **Community Thread is a last resort**, not a gap-filler. It provides the least behavioral specificity of any archetype. Prefer any other archetype — including Friction, Obligation, or even a weak Unease — over defaulting to Community Thread.


### skills/worldbuilder-character/intimate.md

﻿# Intimate Dynamics (Optional Section)

*Sub-file for `worldbuilder-character`. Only read this if the character's roster entry is flagged `Intimate Dynamics: Yes`. If the flag is absent, skip this file entirely.*

---

## Overview

Intimate dynamics follow the same principles as all other sections: behavioral descriptions, friction, and causality produce better results than labels. "Dominant" gives the LLM three stock phrases on loop. A behavioral description of how and why the character takes control — and when they don't — produces dynamic, varied interactions.

Exploration questions (what the dynamic gives them emotionally, how it connects to their history, what would go wrong) belong in the Q&A session and Design Notes, not in this section.

The decision about whether to include intimate dynamics is made once at project planning, recorded in the project plan, and reflected in the roster. It is not revisited character by character.

---

## Format

Bullet list. One behavioral description per bullet, written as a prose sentence. Same format as Soul — When/Behavior/Because embedded naturally, no visible labels.

---

## Coverage

Write entries covering:

- **Attraction expression:** How they show interest — direct or indirect, obvious or subtle, testing or charging forward
- **Hesitation and limits:** What makes them slow down, pull back, or hold a line — this is where tension and pacing come from
- **Specific dynamic (if present):** If the character is built around a specific dynamic, what is its behavioral signature — what do they do, and what emotional need does it serve

**Required:** One friction point — a contradiction in their intimate behavior. Someone who craves physical closeness but pulls back when it becomes emotionally real. Someone who performs confidence but needs reassurance before going further. Friction prevents the LLM from settling into a loop of escalation with no variation.

*Example entries:*

- When a partner moves slowly and waits for her, she relaxes in a way she doesn't elsewhere — being met rather than pursued is the only context where she stops managing how she comes across.
- When an encounter starts to feel scripted, she disengages and gets quiet — she needs it to be real, and performance from the other person collapses the thing she came for.


---

## Writing Doctrine

### skills/writing-style.md

# Writing Style

*Shared reference for all Wide phase documents: world notes, character blueprints, story direction, lore notes, event descriptions, calendar.*

These documents are functional specifications for an AI game master. Every sentence should state something that can be acted on. Clarity outranks style in every case.

Prose guidelines for Export phase outputs (character cards, intro text, etc.) live in the export skill, not here.

These rules govern sentence prose. Where a section mandates a format, such as the Background fact pairs or the relationship entry prefix, the format wins and is reproduced exactly as written.

---

## Style Model

Write behavioral descriptions the way a screenplay writes action lines: present tense, only what can be seen or heard in a scene, no internal states or significance announcements, short plain sentences.

**The staging test:** Can a director stage this sentence? If not, rewrite it.

- Fails: "She carries grief she has never articulated."
- Passes: "She changes the subject and starts wiping down the counter."

For vocabulary, apply Orwell's rule from "Politics and the English Language": shortest Anglo-Saxon word that does the job, active voice, cut every word that can go.

---

## Word Choice

### Use the simplest precise word

If a plain word does the job, use it. Don't reach for a longer or more formal word to sound authoritative.

| Avoid | Use instead |
|---|---|
| perceive, observe | see, notice |
| demonstrate | show |
| melancholic | sad |
| contemplative | thoughtful |
| gregarious | outgoing |
| reticent | quiet, guarded |
| reside | live |
| endeavour | try |
| facilitate | help |
| utilize | use |
| exhibits | shows |
| maintains | keeps, has |

When in doubt: would a plain-spoken person use this word in a work meeting? If not, find the word they would.

### Use "is" and "has": avoid copula avoidance

Use "is" and "has" directly. Don't substitute elaborate constructions.

- Wrong: "The settlement serves as a waypoint for traders."
- Right: "The settlement is a waypoint for traders."
- Wrong: "The building boasts three floors and a cellar."
- Right: "The building has three floors and a cellar."

"Serves as," "stands as," "functions as," "boasts," "features" are circumlocutions. The simple verb is clearer.

### No significance inflation

Don't add statements about importance, legacy, or meaning. If something matters, the facts make that clear without announcement.

- Wrong: "The founding betrayal is a pivotal moment that underscores the community's enduring wound."
- Right: "Three families left after the betrayal. The ones who stayed have never discussed it publicly."

"Pivotal," "enduring," "testament," "underscores," "highlights," "reflects broader": cut them. They add length without adding information.

Vague declaratives are the same move in sentence form: "the stakes are high," "the reasons are structural," "the implications are significant." Each one announces that something matters without saying what it is. Cut the sentence and state the fact it was standing in for.

### Cut filler

Cut words and phrases that stall, inflate, obscure, or dilute a sentence.

- Wrong: "It's worth noting that she essentially runs the kitchen."
- Right: "She runs the kitchen."

Cut these groups outright:

- Throat-clearers: "here's the thing," "it's worth noting," "the truth is," "let me be clear."
- Emphasis crutches: "full stop," "make no mistake," "let that sink in," "I promise."
- Jargon standing in for a plain verb: "navigate," "unpack," "lean into," "deep dive," "circle back."
- Filler words: "really," "just," "genuinely," "truly," "deeply," "actually," "simply," "honestly."

- Wrong: "She genuinely just wants to help, honestly."
- Right: "She wants to help."

---

## Sentence Structure

### Write positive statements

State what something IS. Don't open with "not X."

- Wrong: "She is not warm or friendly at first."
- Right: "She is guarded with strangers. She is watchful, brief, slow to smile."

Negative constructions give the AI one mode (avoidance) instead of something to generate from. Positive statements give behavioral texture.

### Prefer verbs over nominalizations

Keep actions as verbs. Don't convert them into nouns.

- Wrong: "The implementation of the change resulted in a reduction in complaints."
- Right: "The change cut complaints."

### Keep sentences short enough to parse on first read

One idea per sentence when ideas are distinct. If a sentence has two clauses, check whether the second earns its place or whether it reads cleaner on its own.

### No em-dashes

Em-dashes are not used in spec documents. Use periods instead. When two thoughts are joined by an em-dash, split them into two sentences.

**Hedging clause pattern:**

- Wrong: "She is guarded with strangers — watchful, brief, slow to smile — and opens up only when she feels safe."
- Right: "She is guarded with strangers. She is watchful, brief, slow to smile. She opens up only when she feels safe."

**Mid-sentence interruption pattern:**

- Wrong: "He runs the market — has for twenty years — and knows every trader by name."
- Right: "He has run the market for twenty years. He knows every trader by name."

### Numbers as numerals

Write 27, not twenty-seven. Write day 8, not the eighth day.

---

## Content Standards

### Describe behavior, not labels

Name what something *does*, not what it *is* in the abstract.

- Label: "She tends to be evasive."
- Behavior: "She deflects personal questions by turning them back on the asker."

Labels give the AI a category to file under. Behaviors give it something to enact.

**Heavy trait adjectives are banned outright.** "Intelligent," "analytical," "arrogant," "dominant," "majestic," "bustling," and words of that weight may not appear anywhere in a note. One of them outvotes a page of behavioral description and pulls the subject toward the stock type welded to that word. A softer adjective is not the fix. Replace the label with the behavior that earned it. Where the trait is a competence, name three things: the domain the subject is competent in, the drive behind that competence, and a cost or flaw the competence produces. Where it is not a competence, write what happens that makes people reach for the word, and what it costs.

### Make claims verifiable or behavioral

A spec claim should be something that can be checked against the world or enacted in a scene. Abstract claims are weak. Concrete claims are strong.

- Weak: "The region has a troubled history."
- Strong: "Three of the four founding families lost someone in the flood of Year 12."

Ask: what would the AI do differently in a scene because of this statement? If the answer is "nothing specific," the statement is probably too abstract.

### Decide what not to specify

For each detail, ask whether it changes behavior. Specify the details that lock behavior and leave the rest unwritten.

- Wrong: "The house was pale green with a red door on the third street past the mill, and the family kept a gray cart horse named Birch." None of it changes how anyone behaves.
- Right: "The house was cramped and the walls were thin." That fact alone explains why someone raised there does not sleep with a door closed.

### No flair

Metaphor, evocative language, and atmospheric color belong in prose outputs. In spec documents they are noise. State the thing directly.

- Wrong: "Her silence stretches like frost across the room."
- Right: "She goes quiet when this subject comes up and doesn't re-engage until it passes."

### No -ing padding

Don't tack present participle phrases onto sentences to add apparent depth.

- Wrong: "He keeps to himself, reflecting his distrust of outsiders and underscoring the community's broader insularity."
- Right: "He keeps to himself. He doesn't trust outsiders. Most of the community is the same way."

Each thought is its own sentence.

### Single source of truth

Each fact lives in one place. Other documents reference it by naming it, not by restating it.

Don't describe a character in a location note because they're connected to that location. Name the connection; keep the description in the character's own document. Don't paraphrase what another note says. Link to it by name.

### Don't describe one entity in another entity's document

A character note describes that character's experience. A location note describes the location. A relationship entry describes what *this* character feels, thinks, and does. It is not a description of the other party.

- Wrong (in Mira's notes): "Jonas is a quiet, solitary man who keeps to himself."
- Right (in Mira's notes): "She trusts Jonas more than she admits, and resents that she does."

The description of Jonas belongs in Jonas's own notes.

---

## Structure

Structure is expected in spec documents. Use headers, bullets, and tables where they help clarity and scanning. Don't use them decoratively.

Use bullets for discrete parallel items. Use prose for reasoning, relationships, or anything where the connection between ideas matters.

---

## Four Failure Modes

Check for all four before finalizing any document.

**1. Latinate or formal vocabulary.**
Scan for -tion, -ity, -ence, -ance endings and formal synonyms. Replace with plain equivalents.

**2. Negative constructions.**
Search for "not," "never," "without," "lacks," "no X" in descriptions. Rewrite as positive behavioral statements.

**3. Labels without behaviors.**
Any word or phrase that names a quality without showing how it manifests. What does the character *do* because they are "ambitious"? That's the statement worth keeping.

**4. Literary flair.**
Metaphor, atmospheric construction, or evocative phrasing in a spec context. Say the thing directly.

For a phrase-level review checklist of known slop patterns, see `docs/slop-phrases.md` at the plugin root (review reference, not skill instruction).


### docs/slop-phrases.md

# Slop Phrases

Review reference for character note output. Not a skill instruction — agents do not load this file.

Use this as a checklist when reading generated character notes. Each group names a quality problem, then lists the phrases that signal it.

---

## Interpretive narration

Sounds like literary criticism of the character rather than characterization. The AI is narrating its reading of the character instead of specifying the character's reality.

- "reads [X] as" / "reads the situation as" / "reads this as"
- "she reads him as" / "he reads her as"
- "frames [X] as" / "frames this as"
- "positions [X] as"

Fix: replace with a direct interpretation verb — "sees," "takes," "interprets," "understands."

---

## Soul section hedging

Psychological avoidance stated as avoidance rather than as behavior. These phrases describe the character not knowing or not naming something, which tells the AI nothing to act on.

- "she hasn't examined this"
- "she has never named [X] to herself"
- "runs just below conscious examination"
- "keeps below the surface" / "lies below conscious awareness"
- "[X] she has never articulated"
- "she doesn't think of it in those terms"
- "something she has never put into words"
- "she has no language for it"
- "she doesn't have that framework"
- "a [low/quiet] [feeling] she doesn't examine"

Fix: state the behavioral reality directly — what does she do, avoid, or react to?

---

## Vague interiority

States an inner state without behavioral implication. The phrase sounds meaningful but gives the AI nothing to enact.

- "something in her" / "something about him"
- "a part of her" / "a part of him"
- "there is a sense that"
- "there is something [X] about"
- "she carries [X]" (when X is abstract — "she carries grief," "she carries doubt")

Fix: name the specific feeling and the behavior it produces.

---

## Significance inflation

Announces importance without adding information. Cut on sight.

- "pivotal"
- "enduring"
- "testament to"
- "underscores"
- "highlights"
- "reflects broader"
- "speaks to"
- "a defining moment"
- "the weight of [X]"
- "load-bearing" (as in "this is load-bearing for both notes")

Fix: if it matters, the facts make it clear. Remove the announcement.

---

## Vague declaratives

The sentence form of significance inflation. Announces that something matters without saying what it is.

- "the stakes are high"
- "the reasons are structural"
- "the implications are significant"
- "the dynamic is complex"
- "there is history there"

Fix: cut the sentence and state the fact it was standing in for.

---

## Copula avoidance

Circumlocutions that replace "is" or "has" with something elaborate.

- "serves as"
- "stands as"
- "functions as"
- "acts as"
- "boasts"
- "features"

Fix: use "is" or "has."

---

## AI vocabulary

Words that appear constantly in AI-generated text but rarely in how real people describe other people or relationships. Their presence signals the AI is generating rather than observing.

- "gap" / "the gap between them" / "bridge the gap"
- "register" (in the communication sense — "same register," "the register she runs with")

Fix: name what is actually different or distant. "She stopped pushing" is more specific than "the gap was too wide." For "register," describe the actual behavior or tone directly.


---

## Generation Directive

Write a complete character note following the skill instructions above. Work through every section in order: Design Notes (reproduce the provided session notes and builder context), Background, Body, Soul, Relationships, Intimate Dynamics (if flagged). Apply the writing doctrine throughout. Do not skip sections. Do not ask questions — all inputs are provided.
