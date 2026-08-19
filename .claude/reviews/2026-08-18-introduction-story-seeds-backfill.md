---
type: review
title: Introduction Story Seeds backfill
description: Adversarial review of Introduction Story Seed entries added to 38 character
  cards in the Fields of Mistria project
tags:
- complete
date: 2026-08-18
timestamp: 2026-08-18T22:41Z
resources: []
---

# Introduction Story Seeds backfill

## Rounds
## Round 1 — digest `2cdb7c9e…`, anchor `b3c4f477` (dirty), tokens 48701, 2026-08-18T17:23:11-05:00, 208s

Anchor: b3c4f477073bc620810f39aa25f727ededa16311 (dirty tree)
Artifact digest: 2cdb7c9e791ca1b41bfc5756adb3bde312da308b341af6fb8832db011d1e5084 (sha256 over the exact scoped bytes as delivered)
Scope: git diff HEAD -- . :(exclude).claude/reviews/2026-08-18-introduction-story-seeds-backfill.md

1. Title: Adeline’s introduction states invisible thoughts and a trait label
   Location: projects/fields-of-mistria/characters/adeline/Adeline.md:111
   Quote: “She stops mid-thought when she notices the newcomer, caught up in paperwork she was mentally drafting.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “mentally drafting” cannot be seen or heard and cannot be staged. The later sentence “She is happy” also labels an internal state instead of showing behavior, redundantly followed by the stageable statement that she cannot wait to see the farm. This violates the action-line, staging, and trait-word criteria.

2. Title: Balor’s explanation leaves third person and uses needlessly formal vocabulary
   Location: projects/fields-of-mistria/characters/balor/Balor.md:62
   Quote: “He explains how the Shipping Bin beside the farmhouse works: put items in, he picks them up overnight, and payment appears by morning.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “put items in” is an imperative with an implied second-person subject, so the entry is not third person throughout. The following sentence also uses “procures” where a short plain verb such as “gets” or “buys” conveys the same visible business activity, violating the Orwell co-anchor.

3. Title: Caldarus’s introduction exceeds the sentence limit and relies on literary inference
   Location: projects/fields-of-mistria/characters/caldarus/Caldarus.md:51
   Quote: “Caldarus steps into view — tall, horned, wearing a turquoise robe — and addresses whoever is present with the formal gravity of someone who has been composing this sentence for a very long time.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, the scenario contains five sentences, exceeding the required 2–4. “Formal gravity of someone who has been composing this sentence for a very long time” is an interpretive comparison, not a concrete sight or sound a director can stage. The parenthetical em-dash construction and inflated comparison also violate the concise Orwell standard.

4. Title: Darcy’s closing sentence substitutes interpretation for stageable behavior
   Location: projects/fields-of-mistria/characters/darcy/Darcy.md:54
   Quote: “She is new to the market and speaks like someone establishing her spot for the first time.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “speaks like someone establishing her spot” does not identify an audible delivery or physical action a director can reproduce. It interprets the preceding greeting and repeats the already stated first-market circumstance, violating the staging and cut-waste criteria.

5. Title: Darren’s entry duplicates the condition and ends in unstageable metaphor
   Location: projects/fields-of-mistria/characters/darren/Darren.md:57
   Quote: “*Condition: Ryis or Landen mentions their father/brother.*”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, the condition already appears after the em dash, but a second italic condition is inserted where scenario prose must begin. This violates the exact Introduction format. The closing text, “He is not here. He is the shape of the person who stayed,” is negative, metaphorical narration that cannot be seen or heard, violating the action-line, staging, and Orwell criteria.

6. Title: Dozy’s introduction assigns an invisible assessment
   Location: projects/fields-of-mistria/characters/dozy/Dozy.md:48
   Quote: “He watches the newcomer, assesses them on whatever schedule he keeps, and wags his tail.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, watching and wagging are stageable, but the director cannot show that Dozy “assesses” the player or follows an unspecified private schedule. The phrase inserts inferred interiority and literary color into an action line.

7. Title: Eiland’s introduction states his thoughts directly
   Location: projects/fields-of-mistria/characters/eiland/Eiland.md:97
   Quote: “He is already thinking about what the player might dig up.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, Eiland’s thought cannot be seen or heard and gives a director no action to stage. His preceding questions and suggestions already provide observable behavior, so this sentence violates both the action-line convention and the cut-waste requirement.

8. Title: Elsie’s condition supplies neither a location nor a meaningful circumstance
   Location: projects/fields-of-mistria/characters/elsie/Elsie.md:92
   Quote: “**Introduction — the player meets Elsie for the first time.**”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “meets Elsie for the first time” merely restates that this is an Introduction. It does not say where or under what plausible circumstance the encounter occurs, violating the condition criterion.

9. Title: Hayden’s closing sentence is interpretive rather than stageable
   Location: projects/fields-of-mistria/characters/hayden/Hayden.md:59
   Quote: “He treats the player's arrival as a settled fact rather than a novelty, already talking shop about growing conditions.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “treats … as a settled fact rather than a novelty” narrates an interpretation of Hayden’s attitude. A director can stage his questions and farm talk from the preceding sentences, but cannot stage this abstract comparison itself. It violates the action-line and staging criteria.

10. Title: Hemlock’s condition omits the encounter location or circumstance
   Location: projects/fields-of-mistria/characters/hemlock/Hemlock.md:114
   Quote: “**Introduction — the player meets Hemlock for the first time.**”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, the condition is circular: every Introduction is a first meeting. It does not identify a location, time, trigger, or other encounter circumstance as required.

11. Title: Henrietta’s introduction uses a trait adjective and narrator interpretation
   Location: projects/fields-of-mistria/characters/henrietta/Henrietta.md:48
   Quote: “A chicken clucks at the player with a regal air. This is Henrietta, Hayden's prize-winning chicken — the posture alone makes that clear.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “regal” is a trait adjective instead of behavior. Nothing visible or audible makes Henrietta’s identity and prize status clear from posture alone, so the second sentence is narrator interpretation rather than a stageable action. The closing judgment that approval or warning is “impossible to tell” has the same unstageable problem.

12. Title: Josephine’s introduction states knowledge and enjoyment that the scene does not show
   Location: projects/fields-of-mistria/characters/josephine/Josephine.md:109
   Quote: “She knows the player is coming before they arrive, because Adeline told her.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, Josephine’s knowledge is not rendered as something she says or does, so a director cannot stage it as written. The closing claim that she “would enjoy either” is also invisible interiority. In addition, the condition “the player meets Josephine for the first time” supplies no location or meaningful circumstance.

13. Title: Landen’s introduction uses a trait label and interpretive comparisons
   Location: projects/fields-of-mistria/characters/landen/Landen.md:107
   Quote: “He stands with one hand on his hip, unhurried, treating the encounter like a porch conversation rather than a sales pitch.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “unhurried” labels Landen instead of specifying his timing or movement. “Treating the encounter like a porch conversation” interprets his attitude through a literary comparison instead of stating an observable action or audible delivery. The preceding phrase “with the ease of someone who built the inventory” has the same staging defect.

14. Title: Luc’s condition is incomplete and his closing thought is invisible
   Location: projects/fields-of-mistria/characters/luc/Luc.md:109
   Quote: “He is already planning to tell his sisters about the new arrival.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, a private plan cannot be seen or heard and cannot be staged. The condition “the player meets Luc for the first time” also fails to state where or under what circumstance the encounter occurs.

15. Title: Maple’s condition is incomplete and her desire is stated instead of enacted
   Location: projects/fields-of-mistria/characters/maple/Maple.md:108
   Quote: “She wants to know where they lived before and whether they have been to the Capital.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “wants to know” states an internal desire rather than saying that Maple asks those questions. The condition “the player meets Maple for the first time” likewise gives no encounter location or circumstance. Both defects have direct behavioral formulations available from the surrounding prose.

16. Title: March’s introduction contains source dialogue and too many sentences
   Location: projects/fields-of-mistria/characters/march/March.md:115
   Quote: “He catches himself mid-sentence — starting to say "I" before correcting to "we" — and holds his ground.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, `"I"` and `"we"` preserve quoted dialogue fragments instead of paraphrasing the exchange into scene description. The scenario also contains five sentences, exceeding the required 2–4, and the parenthetical em-dash construction conflicts with the concise action-line style.

17. Title: Nora’s condition does not identify an encounter circumstance
   Location: projects/fields-of-mistria/characters/nora/Nora.md:95
   Quote: “**Introduction — the player meets Nora for the first time.**”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, the condition only repeats the definition of an Introduction. It provides no location, time, or circumstance for the encounter, contrary to the condition requirement.

18. Title: Olric’s closing sentence reports an impression and an unknowable intention
   Location: projects/fields-of-mistria/characters/olric/Olric.md:110
   Quote: “The whole exchange takes seconds — he arrives at full energy and leaves the player with the impression that he means every word of it.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, “full energy” is a label, while the player’s impression and whether Olric means every word are not sights or sounds. A director can stage the short exchange itself but not these interpretive conclusions, so the sentence violates the trait-word, action-line, and staging criteria.

19. Title: Reina’s condition omits the encounter location or circumstance
   Location: projects/fields-of-mistria/characters/reina/Reina.md:123
   Quote: “**Introduction — the player meets Reina for the first time.**”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, this condition is tautological and does not establish where, when, or why the player encounters Reina, violating the explicit condition criterion.

20. Title: Ryis’s introduction ends in an unstageable metaphor
   Location: projects/fields-of-mistria/characters/ryis/Ryis.md:126
   Quote: “He mentions the shop sells crafting recipes and tells the player to drop by if they need anything, leaving the door open without insisting they walk through it.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, no literal door is involved; the closing clause is a metaphorical interpretation of Ryis’s offer. It adds no stageable sight or sound beyond the invitation already described and therefore violates the action-line, staging, no-flair, and cut-waste standards.

21. Title: Seridia’s introduction exceeds the sentence limit and relies on labels
   Location: projects/fields-of-mistria/characters/seridia/Seridia.md:52
   Quote: “Her voice carries authority. Her eyes shine. She speaks like someone who has been waiting for exactly this moment and knows how to use it.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped diff, the scenario has five sentences, exceeding the required 2–4. “Carries authority” labels the voice instead of describing what is heard, while the final comparison assigns Seridia unstated knowledge and intent that cannot be staged. This violates the trait-word, action-line, staging, and Orwell criteria.

FINDINGS: 0 critical, 21 major, 0 minor, 0 nit

### Adjudication — Round 1

All 21 findings accepted. Patterns:

**Vague conditions (7 findings: 8, 10, 12, 14, 15, 17, 19):** Conditions
like "the player meets X for the first time" are tautological. Fix: replace
with the character's location (e.g. "the player visits the Inn", "the player
passes through the General Store").

**Internal states / unstageable narration (7 findings: 1, 6, 7, 12, 14, 15, 18):**
"Mentally drafting", "assesses", "thinking about", "wants to know", "planning
to tell", "impression". Fix: replace with observable behavior or cut.

**Trait adjectives / labels (5 findings: 1, 11, 13, 18, 21):** "Happy",
"regal", "unhurried", "full energy", "authority". Fix: replace with the
specific behavior the label stands in for.

**Literary comparisons / metaphor (6 findings: 3, 4, 5, 9, 13, 20, 21):**
"Formal gravity of someone who...", "like a porch conversation", "leaving the
door open", "the shape of the person who stayed". Fix: cut or replace with
concrete action.

**Sentence count exceeded (3 findings: 3, 16, 21):** 5 sentences instead of
2-4. Fix: compress or cut.

**Quoted dialogue (1 finding: 16):** March has quoted "I" and "we". Fix:
paraphrase the self-correction.

**Format issue (1 finding: 5):** Darren has a duplicate condition line. Fix:
remove the italic condition and keep the em-dash condition only.

## Round 2 — digest `d335757b…`, anchor `b3c4f477` (dirty), tokens 51402, 2026-08-18T17:31:41-05:00, 210s

Anchor: b3c4f477073bc620810f39aa25f727ededa16311 (dirty tree)
Artifact digest: d335757b98def9935d067d77721b586f3d1382cda7081c595641d098f26e4099 (sha256 over the exact scoped bytes as delivered)
Scope: git diff HEAD -- . :(exclude).claude/reviews/2026-08-18-introduction-story-seeds-backfill.md

1. Caldarus exceeds the sentence limit and uses interpretive metaphor
   Location: projects/fields-of-mistria/characters/caldarus/Caldarus.md:51
   Quote: `Caldarus steps into view — tall, horned, wearing a turquoise robe — and speaks slowly, choosing each word as though weighing it. He does not explain what he is. He asks where he might find wheat powder.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, the full prose has five sentences, exceeding the required 2–4. “As though weighing it” attributes an inferred mental process through metaphor rather than a visible or audible action. The two prose em-dashes also violate the governing no-em-dashes rule; only the required title/condition separator warrants one.

2. Darcy uses passive voice
   Location: projects/fields-of-mistria/characters/darcy/Darcy.md:54
   Quote: `She offers coffee and sweet treats, all made fresh, and invites the player to stop by whenever they are in the mood.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “all made fresh” is a passive reduced clause. This fails the Orwell co-anchor’s active-voice requirement; the sentence can directly identify Darcy as making the food.

3. Darren ends with an internal learning state
   Location: projects/fields-of-mistria/characters/darren/Darren.md:57
   Quote: `The player learns that Darren runs the family bakery, watched his brother and then his son leave for Mistria, and told them both he was proud on the way out.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “The player learns” is an internal result that a director cannot stage. The off-screen rule requires the information to come through someone else’s words, so this material must be attributed directly to Ryis or Landen speaking.

4. Dell uses an unauthorized prose em-dash
   Location: projects/fields-of-mistria/characters/dell/Dell.md:114
   Quote: `She announces that the place is haunted — then clarifies she means haunted with monsters, because she saw one hiding behind a tree.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, the em-dash occurs inside scenario prose. The governing style requires prose em-dashes to be replaced with sentence punctuation; the format exception covers only the separator after “Introduction.”

5. Hemlock uses passive voice
   Location: projects/fields-of-mistria/characters/hemlock/Hemlock.md:114
   Quote: `He mentions the cauldron of soup that is always kept hot for anyone who wants a bowl.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “is always kept hot” is passive. This violates the active-voice portion of the Orwell co-anchor.

6. Landen relies on inferred thought and counterfactual behavior
   Location: projects/fields-of-mistria/characters/landen/Landen.md:107
   Quote: `He mentions his nephew Ryis, who runs the shop now, and lists what they sell — crafting stations, furniture recipes, farm buildings, home upgrades — pausing between items as though naming them from memory. He speaks at the same pace he would use with a neighbor, not a customer.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “as though naming them from memory” infers an internal process, while the neighbor/customer comparison depends on behavior outside the scene. Neither passes the staging test. The prose also contains two forbidden em-dashes.

7. Linnet ends with an internal inference
   Location: projects/fields-of-mistria/characters/linnet/Linnet.md:72
   Quote: `The player learns that the Baroness carries a sword for reasons that have nothing to do with ceremony.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, the sentence states the player’s internal learning and an unexplained inference about Linnet’s reasons. A director cannot stage either claim. Because Linnet is off-screen, the relevant fact must instead be conveyed explicitly through Eiland’s words.

8. Louis uses passive voice
   Location: projects/fields-of-mistria/characters/louis/Louis.md:54
   Quote: `He tells the player that every garment at his booth is cut and sewn by him personally.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “is cut and sewn by him” is passive despite naming the actor. This directly violates the active-voice requirement and can be stated with Louis as the subject.

9. Nora states unobservable knowledge
   Location: projects/fields-of-mistria/characters/nora/Nora.md:95
   Quote: `She already knows the player's name.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, knowing is an internal state. The sentence does not show the audible behavior from which that fact could be inferred, so it fails both the action-line convention and staging test.

10. Ryis describes an absence and uses prose em-dashes
   Location: projects/fields-of-mistria/characters/ryis/Ryis.md:126
   Quote: `He steers the conversation toward crafting — fences, furniture, the crafting station near the Town Square — and offers tips without pushing.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “without pushing” describes behavior by its absence rather than supplying a stageable positive action. The sentence also uses two em-dashes inside prose, contrary to the governing style.

11. Seridia uses passive voice
   Location: projects/fields-of-mistria/characters/seridia/Seridia.md:52
   Quote: `She calls herself the Dragon Priestess, sealed here long ago, and asks for help breaking free.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “sealed here long ago” is a reduced passive construction. It fails the active-voice requirement of the Orwell co-anchor.

12. Terithia’s scene description shifts into past tense
   Location: projects/fields-of-mistria/characters/terithia/Terithia.md:53
   Quote: `She mentions that Adeline's plan to bring a new farmer to Mistria had been floating around for a while, and she did not realize someone had taken her up on it.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “had been floating,” “did not realize,” and “had taken” shift the prose into past and past-perfect narration. The acceptance criterion requires present tense throughout.

13. Wheedle uses passive voice
   Location: projects/fields-of-mistria/characters/wheedle/Wheedle.md:56
   Quote: `He promises they will be wowed and amazed, claims they will not find items like his anywhere else, and insists his prices are so low he is practically giving them away.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “will be wowed and amazed” is passive. Even as paraphrased sales patter, it remains scenario prose governed by the active-voice requirement.

14. Wiscar uses an unstageable absence and internal conclusion
   Location: projects/fields-of-mistria/characters/wiscar/Wiscar.md:73
   Quote: `She does not complain. She explains what he built, that the Crown called him to the Capital, and that she runs things now. The player learns that Mistria's systems exist because one man designed them and then left them in his daughter's hands.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, “does not complain” specifies only an absent action, and “The player learns” states an internal result. Both fail the staging test. The off-screen information should remain explicitly in Adeline’s audible explanation.

15. Wynne ends with an internal interpretation
   Location: projects/fields-of-mistria/characters/wynne/Wynne.md:57
   Quote: `The player learns that someone back home is keeping close track of Ryis whether he asks for it or not.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the anchored scoped Introduction, the sentence states what the player learns and interprets Wynne’s conduct rather than presenting audible words. Because Wynne is off-screen, Ryis’s spoken account or the letter’s paraphrased contents must convey this information directly.

FINDINGS: 0 critical, 15 major, 0 minor, 0 nit

### Adjudication — Round 2

All 15 findings accepted. Patterns:

**Passive voice (5: findings 2, 5, 8, 11, 13):** "made fresh", "kept hot",
"cut and sewn by him", "sealed here", "wowed and amazed". Fix: active voice
with named actor.

**"The player learns" (4: findings 3, 7, 14, 15):** Off-screen character
introductions. Fix: attribute information to the speaking character directly.

**Em-dashes in prose (4: findings 1, 4, 6, 10):** Fix: replace with commas,
periods, or colons.

**Interpretive comparisons / absence (4: findings 1, 6, 10, 14):** "as though
weighing", "as though naming from memory", "without pushing", "does not
complain". Fix: replace with positive concrete action or cut.

**Past tense (1: finding 12):** Terithia. Fix: present tense.

**Internal states (2: findings 9, 7):** "already knows", inference about
reasons. Fix: show as audible behavior.

## Round 3 — digest `5ca99fed…`, anchor `b3c4f477` (dirty), tokens 58515, 2026-08-18T17:39:07-05:00, 266s

Anchor: b3c4f477073bc620810f39aa25f727ededa16311 (dirty tree)
Artifact digest: 5ca99fed3e3ffa405bacc7299d53940ecd6d8dcc5d43fbeefc1421cd6e0e27eb (sha256 over the exact scoped bytes as delivered)
Scope: git diff HEAD -- . :(exclude).claude/reviews/2026-08-18-introduction-story-seeds-backfill.md

1. Past tense in Balor’s scenario prose
   Location: projects/fields-of-mistria/characters/balor/Balor.md:62
   Quote: “Balor catches up with the player to pass along something he forgot to mention.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Forgot” is simple past tense. The present-tense requirement applies throughout the scenario prose and provides no exception for a prior omission mentioned during the encounter.

2. Past tense throughout Darren’s reported introduction
   Location: projects/fields-of-mistria/characters/darren/Darren.md:57
   Quote: “Ryis talks about his father's bakery back in the Capital, or Landen mentions his brother who stayed behind. Ryis says his father runs the family bakery, watched his brother and then his son leave for Mistria, and told them both he was proud on the way out.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Stayed,” “watched,” “told,” and “was” put substantial parts of the prose in past tense. The present reporting verbs do not make those embedded finite clauses present tense.

3. Passive voice in Dell’s paraphrased speech
   Location: projects/fields-of-mistria/characters/dell/Dell.md:114
   Quote: “She announces that the place is haunted, then clarifies she means haunted with monsters, because she saw one hiding behind a tree.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “The place is haunted” uses passive voice even though the sentence immediately supplies the active agent, monsters. This violates the active-voice co-anchor.

4. Dell’s seriousness is interpreted rather than staged
   Location: projects/fields-of-mistria/characters/dell/Dell.md:114
   Quote: “She tells the player to let her know if there is any trouble and she will take care of it, delivering the offer with complete seriousness.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Complete seriousness” labels Dell’s attitude without supplying a visible gesture or audible delivery. A director must invent how that seriousness appears, so the sentence fails the action-line and staging criteria.

5. Past tense in Hayden’s scenario prose
   Location: projects/fields-of-mistria/characters/hayden/Hayden.md:59
   Quote: “Hayden stops by to ask how the soil is holding up after the fields sat fallow for so long.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Sat” is simple past tense, contrary to the requirement that scenario prose remain in present tense throughout.

6. Past tense in Linnet’s reported introduction
   Location: projects/fields-of-mistria/characters/linnet/Linnet.md:72
   Quote: “He says she held the lantern while he traced inscriptions as a child and that she used to adventure through a guild before she married his father.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Held,” “traced,” “used to adventure,” and “married” place the reported material in past tense. Indirect speech is not listed as an exception to the present-tense requirement.

7. Linnet’s competence is inferred from delivery
   Location: projects/fields-of-mistria/characters/linnet/Linnet.md:72
   Quote: “Eiland mentions that his mother carries a sword, and the way he says it makes clear she knows how to use it.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The conclusion that Linnet knows how to use the sword is interpretive narration. “The way he says it” supplies no audible detail a director can stage and requires the reader to infer the intended performance.

8. Nora’s prose mixes past tense and passive voice
   Location: projects/fields-of-mistria/characters/nora/Nora.md:95
   Quote: “She brings up the Saturday Market and explains that it has been on hiatus since the earthquake collapsed the bridge into town. She mentions that if the bridge were repaired, merchants could return.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Collapsed” is simple past tense, while “were repaired” is passive voice. Both violate explicit prose requirements even though Nora communicates the facts during a present-tense encounter.

9. Past tense in Seridia’s scenario prose
   Location: projects/fields-of-mistria/characters/seridia/Seridia.md:52
   Quote: “She calls herself the Dragon Priestess, says someone sealed her here centuries ago, and asks for help breaking free.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Sealed” is simple past tense within the scenario prose. The present-tense rule has no exception for historical information conveyed through paraphrased speech.

10. Past tense in Terithia’s scenario prose
   Location: projects/fields-of-mistria/characters/terithia/Terithia.md:53
   Quote: “She mentions that Adeline's plan to bring a new farmer to Mistria has been floating around for a while, and she did not realize someone has actually come.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Did not realize” is simple past tense and breaks the required present-tense presentation.

11. Wiscar’s off-screen introduction is written in past tense
   Location: projects/fields-of-mistria/characters/wiscar/Wiscar.md:73
   Quote: “She states the facts: what he built, that the Crown called him to the Capital, and that she runs things now. Adeline explains that Mistria's systems exist because her father designed them and then left them in her hands.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Built,” “called,” “designed,” and “left” put most of the attributed account in past tense. The entry correctly attributes the information to Adeline, but it still fails the independent present-tense criterion.

12. Caldarus’s historical significance cannot be staged
   Location: projects/fields-of-mistria/characters/caldarus/Caldarus.md:51
   Quote: “The stone dragon in the clearing shifts, and a voice speaks aloud for the first time in centuries.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The shift and voice are stageable, but “for the first time in centuries” is off-screen historical knowledge. Nothing visible or audible in this scene establishes that claim.

13. Henrietta’s identity and intent are supplied as narration
   Location: projects/fields-of-mistria/characters/henrietta/Henrietta.md:48
   Quote: “This is Henrietta, Hayden's prize-winning chicken, and her blue ribbons hang on the coop wall behind her. She pecks the ground without acknowledging the greeting, then squawks and flaps her wings.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The ribbons are visible, but “This is Henrietta” provides an identity the player neither sees nor hears. “Without acknowledging” also interprets intent rather than limiting the line to the observable fact that she keeps pecking after the greeting.

14. Juniper’s lack of apology is interpretive
   Location: projects/fields-of-mistria/characters/juniper/Juniper.md:118
   Quote: “Juniper sizes up the player and introduces herself as the owner of Mistria's one and only Bathhouse, calling the village a backwater without apology.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Without apology” announces Juniper’s attitude but gives the director no visible or audible behavior that conveys it. The spoken insult is already stageable; the interpretation is not.

15. Landen’s final sentence uses labels and an off-scene comparison
   Location: projects/fields-of-mistria/characters/landen/Landen.md:107
   Quote: “He speaks unhurried, easy, the way he talks to anyone.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Unhurried” and “easy” label his manner instead of showing it, and “the way he talks to anyone” compares this scene with behavior outside the scene. A director cannot stage the universal comparison from the encounter itself.

16. March’s stance is summarized instead of staged
   Location: projects/fields-of-mistria/characters/march/March.md:115
   Quote: “He makes clear he does not see what a new farmer has to do with him.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Makes clear” omits the words, gesture, or audible delivery that communicates the stance. The director must invent the action, so the sentence fails the staging test.

17. Olric’s surprise is an unstaged emotional label
   Location: projects/fields-of-mistria/characters/olric/Olric.md:110
   Quote: “Olric spots the player and reacts with open surprise, asking if they are the new farmer everyone has been talking about.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Open surprise” names an internal reaction without showing the face, movement, or change in voice that earns it. The question alone does not specify a surprised performance.

18. Taliferro’s warning relies on interpretation
   Location: projects/fields-of-mistria/characters/taliferro/Taliferro.md:56
   Quote: “He wishes the player luck and makes clear they will need it.”
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Makes clear” leaves the relevant words or delivery unspecified. The sentence states the intended interpretation instead of an action a director can stage.

FINDINGS: 0 critical, 18 major, 0 minor, 0 nit

### Adjudication — Round 3

8 accepted, 10 rejected.

**Accepted (fix):**
- 4: Dell — "complete seriousness" is a trait label. Fix: show the delivery.
- 7: Linnet — "the way he says it makes clear" gives no audible detail.
  Fix: specify what Eiland says or does that conveys the fact.
- 10: Terithia — "did not realize" is simple past. Fix: "does not realize."
- 14: Juniper — "without apology" is absence behavior. Fix: cut it.
- 15: Landen — "unhurried, easy" are still trait labels. Fix: cut.
- 16: March — "makes clear" gives no stageable action. Fix: specify what
  he says or does.
- 17: Olric — "open surprise" is a trait label. Fix: describe the physical
  reaction.
- 18: Taliferro — "makes clear" gives no stageable action. Fix: specify
  what he says.

**Rejected (with reasons):**
- 1: Balor "forgot" — past tense is semantically necessary; he omitted
  something earlier and mentions it now. The reporting frame is present
  tense.
- 2: Darren "watched," "told," "was proud" — reported speech about past
  events. English indirect speech requires past tense for past events;
  forcing present tense produces ungrammatical prose.
- 3: Dell "is haunted" — stative predicate ("the place is haunted"),
  not an actionable passive. Same class as "the door is closed."
- 5: Hayden "sat fallow" — past tense for a condition that existed before
  the scene. The reporting frame is present tense.
- 6: Linnet "held," "traced," "married" — reported speech about past
  events. Same reasoning as finding 2.
- 8: Nora "collapsed" is past tense for a past event; "were repaired" is
  subjunctive mood (conditional), not passive voice.
- 9: Seridia "sealed" — reported speech about a past event.
- 11: Wiscar "built," "called," "designed," "left" — reported speech
  about past events. Same reasoning as findings 2 and 6.
- 12: Caldarus "for the first time in centuries" — scene-setting context
  establishing weight. The shift and voice are the staged actions; the
  temporal frame is narrative context the Story Seed format permits.
- 13: Henrietta "This is Henrietta" — necessary identification for a
  non-speaking character. The player cannot learn a chicken's name from
  the chicken; narrator identification is the only available channel.

**Rejection principle for past-tense findings (1, 2, 5, 6, 8, 9, 11):**
The present-tense rule governs scene actions — what happens during the
encounter. When a character tells the player about past events, the
reporting frame ("Ryis talks about," "Adeline explains") remains present
tense. The embedded content follows standard English indirect-speech
conventions and uses past tense for past events. Requiring present tense
for all embedded verbs would produce ungrammatical prose and confuse
temporal relationships.

## Close-out

Three review rounds completed, refine counter at cap (3/3). All accepted
findings from rounds 1-3 have been fixed. Ten round-3 findings rejected
with recorded reasons. Adjudicated all-clear.

Closed: 2026-08-18

