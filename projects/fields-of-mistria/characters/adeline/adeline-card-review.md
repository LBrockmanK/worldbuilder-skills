## Round 1 — digest `46c99e42…`, anchor `3c431a74` (dirty), tokens 55488, 2026-08-15T13:53:39-05:00, 308s

Anchor: 3c431a74e01faf194a6944dc72a2929680beb916 (dirty tree)
Artifact digest: 46c99e42bd398f12d2d273cec7a3e7c506e72cc97d1758d19d67c5935192b7cf (sha256 over the exact scoped bytes as delivered)
Scope: Adeline-test-card.md

1. Body preamble is formatted as a behavioral entry
   Location: Adeline-test-card.md:15
   Quote: `- Pink hair past her shoulders, wavy, with a bow on top. Purple eyes, brown skin. Her spring outfit is a magenta bodice over white puffed sleeves, dark navy skirt with floral embroidery — the outfit changes with the season but the bow stays`
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The format grants the staging exemption only to appearance prose before the first bullet. This text is a bullet, so it is formally a Body entry containing static fragments that a director cannot stage.

2. First Body behavior is neither one sentence nor present-tense action
   Location: Adeline-test-card.md:16
   Quote: `- She always has something to write with. A pen at the desk, a clipboard at the quest board, a notepad at the bathhouse — she once dropped a pencil in the bath to jot down an infrastructure idea, and the bathhouse owner gave her a look that could curdle milk`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The entry combines a universal claim, a sentence fragment, and a past anecdote. It violates the one-stageable-sentence format and the present-tense action-line convention; “could curdle milk” also substitutes metaphor for observable action.

3. Second Body behavior states an internal emotion
   Location: Adeline-test-card.md:17
   Quote: `- Her hair goes frizzy in the rain. She asks friends for homemade hair oil and schedules bathhouse visits partly to manage it, partly because the lavender makes her happy before she is even through the door`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Makes her happy” cannot be seen or heard, and Body has no Because-clause exemption for internal state. The bullet also contains multiple sentences instead of one physical action line.

4. Third Body behavior relies on hidden state and unstageable universals
   Location: Adeline-test-card.md:18
   Quote: `- When she is caught off guard emotionally, a blush rises before she can redirect the conversation. She tries every time. She fails every time`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: A director can stage the blush, but not “caught off guard emotionally,” an unrealized attempt, or the claims about every occurrence. The three-sentence bullet also violates Body’s one-sentence entry format.

5. Core-want entry announces significance instead of showing action
   Location: Adeline-test-card.md:22
   Quote: `The want shows in her daily rounds — every business check-in, every grant proposal, every request-board posting is her making the town safer and happier one task at a time`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “The want shows” and “is her making” interpret the listed acts for the reader. They are outside the exempt Because clause and cannot themselves be staged, violating Soul’s observable action-line rule and the requirement to cut significance commentary.

6. False-belief entry lacks a behavioral trigger and leaves action-line tense
   Location: Adeline-test-card.md:24
   Quote: `- She believes that if she stops working, everything falls apart. She schedules her bath time, writes grant proposals outdoors so relaxation counts as productivity, and treats an empty to-do list as a nightmare she once literally had — because unstructured time without a task is time that could have been spent keeping something from breaking *(false belief)*`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The conditional is the content of her belief, not a trigger for the listed behavior, so the entry lacks the When component. “She believes” is an internal assertion outside the Because clause, while “once literally had” and “could have been spent” leave present-tense action.

7. Value-conflict entry has no underlying Because and uses abstractions
   Location: Adeline-test-card.md:25
   Quote: `- When duty and self-care collide, she follows duty until her body forces the question. The lever that tips her is someone else's concern, never her own — she deflects a friend's warning, apologizes for "spoiling" a date when she collapses, and frames recovery as getting back to work faster. Guilt shows up as minimization and a quick redirect to the next agenda item *(value-conflict stance)*`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The entry supplies a trigger, choice, tipping condition, and guilt behavior, but never gives the underlying reason required by When/Behavior/Because. “Her body forces the question,” “lever,” and “minimization” are abstractions rather than observable action.

8. Unresolved-tension entry lacks a trigger and is mostly internal
   Location: Adeline-test-card.md:26
   Quote: `- She genuinely loves paperwork — she dreams about it, finds triple-checking tax documents satisfying, writes in pink berry ink because it makes her notes pretty. But she also uses productivity to avoid sitting with what she feels. The thing she hides behind is the thing she authentically enjoys, and letting go of one means risking the other *(unresolved tension)*`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: There is no When trigger for the overall pattern. Loving, finding something satisfying, avoiding feelings, authentic enjoyment, and perceived risk are internal claims outside a qualifying Because clause. “Genuinely” and “authentically” repeat emphasis without adding behavior.

9. Values-with-costs entry is historical summary, not When/Behavior/Because
   Location: Adeline-test-card.md:27
   Quote: `- She values order and preparation. The cost: three separate people in her life have had to set rules — Valen banned all-nighters, Elsie and Eiland forbade office napping, her friends staged an intervention over late-night coffee — and she still worked to the point of fainting during tea with the person she cares about most *(values with costs)*`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The doctrine content is present, but the Soul entry has neither a trigger nor an underlying reason. It begins with an internal value label and then switches to past-tense history, violating both required structure and the present-tense action-line convention.

10. Paperwork-joke entry puts hidden states outside the causal exemption
   Location: Adeline-test-card.md:28
   Quote: `- When emotion gets too close to the surface, she makes a joke about paperwork before anyone can ask whether she is serious. "I had the strangest dream — I ran out of paperwork. How horrible!" The framing is real amusement and real anxiety simultaneously, and she offers it first so no one has to choose which one to respond to`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Emotion gets too close” is an internal trigger, and the assertion of simultaneous amusement and anxiety is narrator interpretation. Only the causal reason may name a specific internal state; the rest of the Soul action line must remain observable or audible.

11. Child-interaction entry labels internal intent as observable behavior
   Location: Adeline-test-card.md:29
   Quote: `She reviews their reports with genuine interest, lets an eight-year-old hold court in the manor entry hall, and cannot bring herself to outrank a child who has declared herself queen`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Reviewing reports and allowing court are stageable. “Genuine interest” and “cannot bring herself” assert hidden intent outside the Because clause, so the entry does not wholly follow the observable action-line convention.

12. Background pair replaces its result with a trait label
   Location: Adeline-test-card.md:6
   Quote: `- Her mother rejected Wiscar's noble proposal at first because she did not want to marry into nobility; they eloped → Adeline inherited both the duty her mother married into and the practical streak that almost refused it`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Practical streak” is a banned trait label, not a concrete fact made true by the elopement. “Inherited” also asserts an unsupported causal transfer instead of supplying a verifiable second half of the fact pair.

13. Background retains a competence adjective
   Location: Adeline-test-card.md:7
   Quote: `posted the call for a "capable adventurer"`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Capable” is a competence label rather than behavior. The acceptance criterion bans trait adjectives anywhere, without an exception for quoted in-world wording.

14. Eiland Background entry contains ongoing behavioral framing
   Location: Adeline-test-card.md:9
   Quote: `- Brother Eiland shares the Manor and the work, but his attention drifts toward archaeology → she assigns him paperwork he finds archaic and budgets around his cookie proposals, carrying the administrative load when he wanders`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The right side describes repeated interaction behavior—assigning, budgeting, carrying work—rather than a fact the formative circumstance made true. That material belongs in a behavioral section, not Background.

15. Childhood Background pair ends in abstract interpretation
   Location: Adeline-test-card.md:10
   Quote: `her bond to Mistria is sensory and rooted in childhood, not abstract obligation`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: This announces the meaning of the memories and an internal source of attachment. It is not a concrete, verifiable fact produced by the childhood events, so the pair fails Background’s required form.

16. Office Background pair announces symbolism
   Location: Adeline-test-card.md:11
   Quote: `even her workspace is a decision about discipline over comfort`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The right side interprets the office choice as symbolic evidence of two abstract qualities. It neither states a concrete resulting fact nor lets behavior earn the characterization.

17. Celine entry summarizes Celine instead of defining Adeline’s behavior
   Location: Adeline-test-card.md:35
   Quote: `- **Celine** — The gentle third of her friend trio. Celine brings flowers for the manor, makes berry-pigment ink for Adeline's color-coded notes, and invites her foraging. Celine's support is practical: she solves the hair problem with homemade oil, identifies trees Ryis can't name, and spots Adeline's poker tell before anyone else`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Every action belongs to Celine; the entry gives no specific action Adeline takes with or because of her. “Gentle” and “practical” are also trait labels, so the entry violates both the relationship-dynamics rule and trait-word ban.

18. Reina is introduced with a trait adjective
   Location: Adeline-test-card.md:36
   Quote: `The insistent third of the friend trio.`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Insistent” labels Reina before the subsequent behavior earns that conclusion. The trait-word ban applies throughout the note, including descriptions of related characters.

19. Every relationship prefix omits its required archetype
   Location: Adeline-test-card.md:33-40
   Quote:
       `- **Eiland** —`
       `- **Elsie** —`
       `- **Celine** —`
       `- **Reina** —`
       `- **Nora** —`
       `- **The Dragonguard (Dell, Maple, Luc)** —`
       `- **Landen** —`
       `- **Seridia** —`
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The card-format standard requires `**Name — Archetype(s):**` inside the bold prefix. All eight entries use only a bold name followed by an external dash, preventing the required relationship coverage and distribution checks.

20. Doctrine annotations expose builder-layer vocabulary
   Location: Adeline-test-card.md:22-27
   Quote:
       `*(core want)*`
       `*(core fear)*`
       `*(false belief)*`
       `*(value-conflict stance)*`
       `*(unresolved tension)*`
       `*(values with costs)*`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: These labels name the builder’s doctrine slots instead of describing Adeline. Working annotations may exist during drafting, but the explicit acceptance criterion forbids builder abstraction vocabulary in the delivered artifact.

21. Design Notes contain extensive builder abstraction vocabulary
   Location: Adeline-test-card.md:113-125
   Quote:
       `Source material ingestion test case using extracted game assets from Fields of Mistria (NPC data, 103 dialogue files, 76 group conversations, 9 heart events, 22 story events, full seasonal schedules, wiki cross-reference, portrait analysis). Autonomous Q&A pass — reference documents substituted for human answers.`
       `- Storylines/greetings and calendar events documented in separate reference files — these feed the platform's future-storylines and calendar-events systems rather than the character card itself.`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Ingestion,” “Q&A pass,” “reference documents,” “export targets,” “addon blocks,” “Builder Context,” “knowledge boundaries,” mappings, and platform-system routing are builder-layer terms. Although the repository normally treats Design Notes as a non-exported builder record, the supplied acceptance criteria exempt only the Body preamble from one rule and give Design Notes no exemption from the meta-vocabulary ban.

22. Spec prose repeatedly uses banned em-dash constructions
   Location: Adeline-test-card.md:8, 15-16, 22, 24-29, 33-40
   Quote:
       `Elsie — a retired opera singer from the Capital, not a blood relative despite the title "Great Aunt" — took up residence at the Manor after the earthquake`
       `The lever that tips her is someone else's concern, never her own — she deflects a friend's warning`
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The writing standard requires distinct thoughts to be split into short sentences and expressly rejects em dashes in spec prose. These constructions join explanations, asides, and actions into long sentences, violating the Orwell co-anchor’s requirements to use direct structure and cut waste.

FINDINGS: 0 critical, 22 major, 0 minor, 0 nit

