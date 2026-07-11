---
type: reference
title: 'Causal character writing for LLM roleplay: friction, engines, and trait-word
  poisoning'
description: 'Key-info extraction from three community references on writing character
  cards for LLM roleplay: causal chains over trait lists, interaction constraint engines
  and emotional memory hooks, and the trait-word poisoning failure mode for intelligence-type
  adjectives. Includes a delta assessment against the worldbuilder character doctrine.'
tags:
- human-ready
date: 2026-07-11
timestamp: 2026-07-11T15:42Z
resources:
- https://likesumiink.substack.com/p/building-engines-and-making-hairballs
- https://www.reddit.com/r/SillyTavernAI/comments/1qopo7h/on_building_characters_with_friction/
- https://www.reddit.com/r/SillyTavernAI/comments/1upluec/how_do_i_stop_an_intelligent_character_from/
---

# Causal character writing for LLM roleplay: friction, engines, and trait-word poisoning

## Sources

Fetched 2026-07-11 (timestamp above). Ranked; higher wins on conflict. The overlap survey found no topic-level contradictions — the three sources agree on fundamentals and differ only in depth, so the ranking below is a default, not a resolution record.

1. **"Building Engines and Making Hairballs"** (likesumiink, Substack) — the deepest treatment: interaction constraint engines, emotional memory hooks, the hairball/weighted-graph model. Same author as source 2; this is the later, fuller statement.
2. **"On building characters with friction"** (huge-centipede, r/SillyTavernAI) — the compact version: traits-as-vectors, causality, the riff methodology, Egri's three dimensions. Comment thread adds the implicit-encoding nuance.
3. **Intelligent-characters thread** (r/SillyTavernAI) — community Q&A on one failure mode (trait-word poisoning). Anecdote-grade individually, but the top answers converge hard.

## Where the sources confirm existing doctrine

The core of all three sources is already the core of [worldbuilder-character](../../skills/worldbuilder-character/SKILL.md):

- **Behavioral descriptions over trait labels** — framework.md's label-vs-behavioral table is the same argument as "traits are lumber, prose is architecture."
- **Causality** — the When/Behavior/Because formula is a causal chain; the sources' cause → tension → mask-vs-truth → reason-to-change decomposition matches what the Because clause carries.
- **Required contradiction and irrational behavior** — "LLM roleplay thrives on friction" and "people are irrational; mistakes make depth" are framework.md's two required Soul entries, independently derived.
- **Egri's three dimensions** (The Art of Dramatic Writing: physiological / sociological / psychological) map cleanly onto Body / Background / Soul. External validation of the section split, and a citable ancestor for it.
- **References as sprinkles** — hard cultural references ground a character but a card that is all toppings overwhelms; matches the existing restraint on external references in Builder Context.
- **Token discipline** — sources converge on roughly 900–1500 tokens per character card (up to ~2300 for a pair), with drift beyond that. Consistent with export-phase compression assumptions.

## New principles not in current doctrine

1. **Trait-word poisoning.** A single heavy adjective — "intelligent," "analytical," "arrogant," "dominant" — can outweigh a whole card of behavioral description and drag output into the trope statistically welded to that word (jargon-spewing robot, UN spokesman, emotionless android). The fix is never a softer adjective: specify the *domain* of competence ("remembers the C99 spec verbatim"), the *drive* behind it, and a cost or flaw it produces. Strongest formulation: the thread's consensus that you cannot use these words *anywhere* in the card — the description can't outvote them.
2. **Knowledge boundaries.** State what a character knows *and where they have no insight*. Unbounded competence plus an LLM's own knowledge produces omniscient characters (the book nerd who knows thread counts). Per-topic depth beats a global trait.
3. **Unresolved states.** A resolved fact ("became a DSA member") is a shortcut the model can cheat through; an unresolved tension ("can't commit because…") forces the model to *find* the character's position each time, which is what produces liveliness. Deliberately leave the character's direction open — multiple supported futures, none chosen. Related to but distinct from the existing starting-state rule: that rule bans future events; this one says the *present* should contain live, competing pulls.
4. **The specification boundary is a design decision.** For every detail: does it matter for behavior, or can the model fill it in? Specifying locks it and costs tokens; leaving it open lets the model average — which is fine when the average is fine. The current "make decisions, don't hedge" rule governs what you write; this governs what you deliberately don't.
5. **Anchor repetition / graph density.** Densely interconnecting a character's anchors (the mentor linked to the sword, the pottery, the clothing, the loneliness) gives the model multiple activation routes to the same material — "more connections make her more reachable," stability under pressure. The sources deliberately repeat key anchors at several points in the card. This is in tension with the current section-discipline rule (redundancy between sections means content is in the wrong place) — see Tensions.
6. **Emotional memory hooks / cinematic compression.** A compressed, specific, unresolved sensory fragment ("the last thing she remembers of her mother: lowering her yukata's collar, one word — run") carries more weight than a paragraph of explanation, because dramatic-moment patterns are dense in training data. Defined: a compressed, specific, unresolved sensory or narrative detail the model can activate and expand outward from.
7. **Implicit encoding beats explicit subtext.** Writing "she wears a bubbly mask to hide her trauma" produces narrator trauma-dumping in the first vaguely related scene. Two working alternatives from the friction thread: build the full causal ramp so the mask is *derivable*, or place the outward presentation and the backstory *near each other without connecting them* and let the model do the linking. Causality is for the author to think through, not necessarily to hand to the model spelled out.
8. **The character has a life in motion.** Rent going up, arguments with parents, missed opportunities, the option of rejecting the player entirely. Independent ongoing pressure is what gives the model "action" beyond reacting to the user.
9. **Names carry weight.** A generically fantasy-adjacent name pulled a dwarf out of nowhere in the source's test. Name choice is itself a vector.
10. **Battle-test the card.** Run the happy path and an adversarial path ("take her to Tahiti") and watch where it breaks. Testing doctrine for characters does not currently exist.
11. **Card-to-greeting ramp.** The card is the skateboard, the first message sets the trajectory: tone, situation, a visible clip of personality for the model to expound on. Placing the character somewhere they wouldn't normally be adds friction. Export-phase relevant.

## Tensions with current doctrine

- **Plain style vs. sensory hooks.** writing-style.md prescribes screenplay action lines — observable, plain, no flair. The emotional-memory-hook technique argues a few dense cinematic fragments are the highest-leverage tokens in a card. These are reconcilable (hooks are still observable and concrete — a collar, one word — not Latinate abstraction), but the style doctrine as written would likely flag them. Needs a deliberate call.
- **Section discipline vs. anchor repetition.** framework.md treats cross-section redundancy as misplacement; the hairball model treats deliberate anchor repetition as grounding. Possible resolution: no *content* duplication, but anchors may be *referenced* from multiple entries. Needs a deliberate call.
- **Positive-statement rule vs. prompt-level bans.** Some thread answers fix trait poisoning with negative instructions ("forbid technical language"). Existing doctrine (write what characters ARE) and the higher-ranked sources both point the other way; keep the doctrine, note the disagreement.

## Candidate applications

Each is a doctrine edit; none applied yet. **Gated on an A/B trial (decided 2026-07-11):** apply new-doctrine and current-doctrine versions to the same character brief with two independent agents, compare the resulting notes blind, then decide what folds in. The two Tensions calls ride on the same trial. A parallel blind trial gates the separate stop-slop evaluation (see inbox); the two trials run as one combined exercise — produce the instruction sets, apply each with an independent agent, compare all results side by side.

- `skills/worldbuilder-character/framework.md`: add trait-word poisoning to the label-vs-behavioral section (name the dangerous word class); add unresolved-states as a Soul construction principle; add knowledge-boundaries coverage prompt.
- `skills/worldbuilder-character/SKILL.md`: battle-test step in the self-check (happy path + one adversarial probe); "life in motion" coverage in the Q&A list.
- `skills/writing-style.md`: rule on the hook exemption — when a compressed sensory fragment is allowed to break plainness.
- `skills/worldbuilder-ainime-export/SKILL.md`: first-message/greeting ramp guidance; token-budget calibration against the sources' 900–1500 range.
- `docs/slop-phrases.md`: no change — "data point"-style output slop is a symptom; the fix is upstream in the card.

The two Tensions items need decisions before their edits; the rest are additive.
