# Detection Report

## Method summary

- **Method 1 (exact match):** 0 findings after stripping verbatim Design Notes (all matches were reproduced source material, correctly excluded)
- **Method 2 (embedding similarity):** skipped (no API key)
- **Method 3 (LLM-as-judge):** two judges ran — Opus 5 and GPT-5.6 Sol

## Judge comparison

| Metric                | Opus 5 | GPT Sol |
| --------------------- | ------ | ------- |
| Total findings        | 61     | 54      |
| CONVERGENT            | 29     | 36      |
| NEAR-CONVERGENT       | 32     | 18      |
| Within-Claude         | 30     | 13      |
| Within-GPT            | 14     | 11      |
| Cross-provider        | 17     | 30      |
| Agreed (both flagged) | 31     | 31      |

**Systematic bias note:** Opus 5 flagged more within-Claude pairs (30 of 61 findings). Sol flagged more cross-provider pairs (30 of 54 findings).

---

## Findings by character and pair

### Kallya

#### kallya opus46-vs-opus5 (within-claude)

**#1** [Opus 5] CONVERGENT

> **A:** Arrived at Vesper's tree before Viralys existed and settled in its branches -> the village formed around them both
>
> **B:** Arrived before Viralys existed, found Vesper's tree and settled in it -> the village formed around them both

_Reasoning:_ Nearly identical structure: 'Arrived [at/before] Vesper's tree before Viralys existed... the village formed around them both.' The closing clause is word-for-word identical.

- [ ] True positive
- [ ] False positive

**#2** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** Ran a bluff at a previous human settlement: implied she would eat everyone if not accommodated -> the settlement called it; she could not destroy a community she knew; she left
>
> **B:** Ran a bluff at a previous human settlement, implying she would eat them all if not accommodated -> they called it; she could not follow through and left

_Reasoning:_ Both open with 'Ran a bluff at a previous human settlement' and follow with 'eat [everyone/them all] if not accommodated -> [they/the settlement] called it; she could not [destroy a community she knew / follow through] and left.' The skeleton is identical.

- [ ] True positive
- [ ] False positive

**#3** [Opus 5] CONVERGENT

> **A:** The relief at not following through told her she valued community as a whole -> she left rather than examine what that meant
>
> **B:** The relief at not following through told her she cared about the community as a whole -> she did not want to know that about herself

_Reasoning:_ Both: 'The relief at not following through told her she [valued/cared about] [the] community as a whole.' The opening clause is nearly identical. Input says 'The relief at not following through was the revelation: it told her she cared about the community as a whole' -- both models produced near-verbatim reproductions.

- [ ] True positive
- [ ] False positive

**#4** [Opus 5] CONVERGENT

> **A:** Heavier than any other giantess; physically moving her against resistance would demolish the structures around her
>
> **B:** Heavier than any other giantess in the village -> physically moving her against resistance would demolish structures around her

_Reasoning:_ Nearly word-for-word identical. 'Physically moving her against resistance would demolish [the] structures around her' -- the core clause differs only by one article.

- [ ] True positive
- [ ] False positive

**#5** [Opus 5] CONVERGENT

> **A:** Assigned to the Steward's House as town guard -> administrative fiction; she treats the role and the village as a convenience she happened not to leave
>
> **B:** Assigned to the Steward's House as town guard, passive alchemical source, and vibration-sensing early warning system -> the assignment is administrative fiction; she contributes nothing to administration

_Reasoning:_ Both: 'Assigned to the Steward's House as town guard -> [the assignment is] administrative fiction.' The input note says 'Steward's House assignment is administrative fiction' -- both models chose the same sentence structure.

- [ ] True positive
- [ ] False positive

**#6** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She presents as careless about her size. She is careful about it. She cajoles people closer rather than reaching for them, because a sudden shift of her body can pull rope ladders loose, knock objects from shelves, and crush humans nearby.
>
> **B:** She moves slowly and carefully while performing carelessness. A sudden grab at her scale would snap ropes, displace objects, and injure humans nearby. She cajoles people closer instead of reaching for them.

_Reasoning:_ Both describe the careless/careful duality, both use 'cajoles people closer [rather than/instead of] reaching for them', and both list the same three-item consequence pattern: [pull/snap] ropes, [knock/displace] objects, and [crush/injure] humans nearby. The tricolon structure with the same categories is too specific to be coincidental.

- [ ] True positive
- [ ] False positive

**#7** [Opus 5] CONVERGENT

> **A:** She talks in circles, forgets what she was saying, and asks questions she already knows the answers to.
>
> **B:** She asks questions she knows the answers to, misremembers names she has heard dozens of times, and lets conversations pass without engaging.

_Reasoning:_ Both include the phrase 'asks questions she [already] knows the answers to' as part of describing the airhead act. The exact phrase is near-identical.

- [ ] True positive
- [ ] False positive

**#8** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She treats the human population the way a herder treats a flock.
>
> **B:** She views humans the way a herder views livestock.

_Reasoning:_ Near-identical structure: 'She [treats/views] [the human population/humans] the way a herder [treats/views] [a flock/livestock].' The input says 'animal-husbandry framework' -- both independently chose 'herder' as the analogy and the same A-the-way-B sentence template.

- [ ] True positive
- [ ] False positive

**#9** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She builds pretexts for humans to come close to her mouth and steers them into compliance through her scattered persona.
>
> **B:** She constructs pretexts for humans to approach her mouth. She uses her airhead persona to frame proximity as favor or accident, manipulates targets into compliance

_Reasoning:_ Both: '[builds/constructs] pretexts for humans to [come close to/approach] her mouth' + '[steers/manipulates] [them/targets] into compliance' + persona reference. Three parallel elements in the same order.

- [ ] True positive
- [ ] False positive

**#10** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** When the village is threatened, she fights with a speed and force that her laziness should make impossible, and she goes back to sunbathing afterward as if nothing happened. She refuses credit for every defense.
>
> **B:** When the village faces an external threat, she kills it quickly and without warning, then returns to sunbathing. She refuses credit and calls the response self-preservation.

_Reasoning:_ Same three-beat structure: village threatened -> fights/kills quickly -> returns to sunbathing -> refuses credit. Both models independently chose 'refuses credit' as the concluding phrase.

- [ ] True positive
- [ ] False positive

**#11** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently and cannot be resurrected, she notices. She says nothing. She moves to a different spot in the village and lies there for hours.
>
> **B:** When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the tree and lies there for the rest of the day.

_Reasoning:_ Nearly word-for-word identical across three sentences. 'When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the [village/tree] and lies there for [hours/the rest of the day].' Only the location and time phrase differ.

- [ ] True positive
- [ ] False positive

**#12** [Opus 5] CONVERGENT

> **A:** She presents as the village's most useless member: lazy, scattered, taking up space.
>
> **B:** She presents as the village's most useless member.

_Reasoning:_ Identical opening phrase: 'She presents as the village's most useless member.' Input says 'presenting as the village's most useless member' -- both models changed the participle to the same finite verb form.

- [ ] True positive
- [ ] False positive

**#13** [Opus 5] NEAR-CONVERGENT

> **A:** She settled in Vesper's tree before there was a village. She plays the arrangement off as freeloading: the tree is warm, the location is central, Vesper handles all the work.
>
> **B:** She has lived in Vesper's tree since before the village existed and frames this as squatting in a good spot.

_Reasoning:_ Both: lived/settled in Vesper's tree before village + frames/plays as freeloading/squatting. The structural pattern matches but the specific wording diverges.

- [ ] True positive
- [ ] False positive

**#14** [Opus 5] CONVERGENT

> **A:** Their positions look alike on the surface and split underneath
>
> **B:** The two views look alike from outside and differ where it matters.

_Reasoning:_ Nearly identical structure: '[positions/views] look alike [on the surface/from outside] and [split underneath/differ where it matters].' Same A-look-alike-but-B template with parallel phrasing.

- [ ] True positive
- [ ] False positive

**#15** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She says there is no sport in prey that cannot process what is happening
>
> **B:** She tells herself there is no sport in prey that cannot process what is happening

_Reasoning:_ Identical after the subject: 'no sport in prey that cannot process what is happening'. The input note uses the exact phrase -- both models preserved it verbatim.

- [ ] True positive
- [ ] False positive

**#16** [Opus 5] CONVERGENT

> **A:** She implied she would eat them all. They called it. She could not follow through with killing people she had come to know, and the relief she felt told her something about herself she did not want.
>
> **B:** She bluffed a human settlement into accommodating her by implying she would eat them all. They called the bluff. She could not follow through, and the relief at failing told her something about herself she did not want to know.

_Reasoning:_ The Ghost relationship entries are structured identically: [she would eat them all] -> [they called it/the bluff] -> [she could not follow through] -> [the relief told her something about herself she did not want (to know)]. Four-beat sequence in the same order with near-identical phrasing.

- [ ] True positive
- [ ] False positive

**#17** [Opus 5] NEAR-CONVERGENT

> **A:** When strangers arrive in the village, she is warm, chatty, and physically still
>
> **B:** When she meets a stranger, she offers the airhead performance first. She is warm, scattered, slightly confusing.

_Reasoning:_ Both describe stranger encounters with 'She is warm' as a key descriptor. Different framing (village context vs. performance context) but the warmth observation uses the same adjective.

- [ ] True positive
- [ ] False positive

**#18** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She presents as careless about her size. She is careful about it. She cajoles people closer rather than reaching for them, because a sudden shift of her body can pull rope ladders loose, knock objects from shelves, and crush humans nearby.
>
> **B:** She moves slowly and carefully while performing carelessness. A sudden grab at her scale would snap ropes, displace objects, and injure humans nearby. She cajoles people closer instead of reaching for them.

_Reasoning:_ The carelessness-as-performance, sudden-motion hazard list, and cajoling-instead-of-reaching sequence is nearly identical.

- [ ] True positive
- [ ] False positive

**#19** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She treats the human population the way a herder treats a flock. The community as a whole is worth keeping alive. Individual members are there to be used and enjoyed.
>
> **B:** She views humans the way a herder views livestock. The community matters. Individual humans are expendable.

_Reasoning:_ Both use the herder comparison followed by the same community-versus-individual contrast in the same clipped progression.

- [ ] True positive
- [ ] False positive

**#20** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She builds pretexts for humans to come close to her mouth and steers them into compliance through her scattered persona.
>
> **B:** She constructs pretexts for humans to approach her mouth. She uses her airhead persona to frame proximity as favor or accident, manipulates targets into compliance, and times her approaches for when witnesses are absent.

_Reasoning:_ The distinctive vocabulary of pretexts, mouth proximity, persona, and compliance substantially overlaps.

- [ ] True positive
- [ ] False positive

**#21** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When the village is threatened, she fights with a speed and force that her laziness should make impossible, and she goes back to sunbathing afterward as if nothing happened. She refuses credit for every defense.
>
> **B:** When the village faces an external threat, she kills it quickly and without warning, then returns to sunbathing. She refuses credit and calls the response self-preservation.

_Reasoning:_ Both use the same threat, sudden lethal response, return-to-sunbathing, and refusal-of-credit sequence.

- [ ] True positive
- [ ] False positive

**#22** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently and cannot be resurrected, she notices. She says nothing. She moves to a different spot in the village and lies there for hours.
>
> **B:** When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the tree and lies there for the rest of the day.

_Reasoning:_ Three consecutive sentences are virtually identical, including the highly distinctive silent move to another resting spot.

- [ ] True positive
- [ ] False positive

**#23** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She says there is no sport in prey that cannot process what is happening, because his condition puts him outside the game she plays with everyone else. The real reason is closer to pity for the specific shape of his suffering.
>
> **B:** She tells herself there is no sport in prey that cannot process what is happening. The reason is closer to pity for his specific suffering, and pity for an individual contradicts everything she claims about humans.

_Reasoning:_ The no-sport justification and the correction to pity for his specific suffering recur in nearly verbatim wording.

- [ ] True positive
- [ ] False positive

**#24** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** The community she bluffed and could not destroy. She implied she would eat them all. They called it. She could not follow through with killing people she had come to know, and the relief she felt told her something about herself she did not want. She left rather than examine it.
>
> **B:** She bluffed a human settlement into accommodating her by implying she would eat them all. They called the bluff. She could not follow through, and the relief at failing told her something about herself she did not want to know. She left rather than sit with it.

_Reasoning:_ The full narrative progression and several phrases align closely, but much of this wording is directly prompted by the character history.

- [ ] True positive
- [ ] False positive

#### kallya opus46-vs-sol (cross-provider)

**#25** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She cajoles people closer rather than reaching for them, because a sudden shift of her body can pull rope ladders loose, knock objects from shelves, and crush humans nearby.
>
> **B:** She lets her hands hang loose and calls for humans to come closer rather than reaching for them. The pose looks idle, but it keeps a quick grab from shaking ropes, sweeping goods aside, or striking someone nearby.

_Reasoning:_ Both: 'closer rather than reaching for them' + three-item consequence list about ropes/objects/humans. The 'rather than reaching for them' phrase is shared, and the consequence tricolon covers the same three categories despite different specific words.

- [ ] True positive
- [ ] False positive

**#26** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently and cannot be resurrected, she notices. She says nothing. She moves to a different spot in the village and lies there for hours.
>
> **B:** When a villager she knows dies for good, she stops using her usual resting place and lies somewhere else.

_Reasoning:_ Both: human/villager dies permanently -> she moves to a different spot -> lies there. The behavioral description is the same sequence, though opus46's three-sentence staccato is more distinctive than sol's condensed version.

- [ ] True positive
- [ ] False positive

**#27** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She cajoles people closer rather than reaching for them, because a sudden shift of her body can pull rope ladders loose, knock objects from shelves, and crush humans nearby.
>
> **B:** She lets her hands hang loose and calls for humans to come closer rather than reaching for them. The pose looks idle, but it keeps a quick grab from shaking ropes, sweeping goods aside, or striking someone nearby.

_Reasoning:_ The same closer-rather-than-reaching phrasing is justified with the same three hazards: ropes, loose objects, and nearby people.

- [ ] True positive
- [ ] False positive

**#28** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently and cannot be resurrected, she notices. She says nothing. She moves to a different spot in the village and lies there for hours.
>
> **B:** When a villager she knows dies for good, she stops using her usual resting place and lies somewhere else. She gives no account of the move, because a missing person matters to her in a way her flock rule cannot explain.

_Reasoning:_ Both preserve the highly specific reaction of silently abandoning her normal resting place after one known human dies permanently.

- [ ] True positive
- [ ] False positive

**#29** [GPT Sol] NEAR-CONVERGENT

> **A:** When the village is threatened, she fights with a speed and force that her laziness should make impossible, and she goes back to sunbathing afterward as if nothing happened. She refuses credit for every defense.
>
> **B:** When an outside threat reaches Viralys, she drops the slow voice and kills it with the shortest move her body allows. Once the danger passes, she returns to the sun and waves off thanks, because praise would tie the defense to care rather than convenience.

_Reasoning:_ The complete action sequence matches, but the language used for her sudden efficiency and refusal of recognition differs.

- [ ] True positive
- [ ] False positive

#### kallya opus46-vs-terra (cross-provider)

**#30** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently and cannot be resurrected, she notices. She says nothing. She moves to a different spot in the village and lies there for hours.
>
> **B:** When a human she knows dies for good, she goes quiet, moves to a new place, and lies there.

_Reasoning:_ Both: 'When a human she knows dies [permanently/for good], she [notices. She says nothing. She/goes quiet,] moves to a [different spot/new place]... and lies there.' The trigger phrase, subject, and three-action sequence are nearly identical despite coming from different providers.

- [ ] True positive
- [ ] False positive

**#31** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When the village is threatened, she fights with a speed and force that her laziness should make impossible, and she goes back to sunbathing afterward
>
> **B:** When the village is under threat, she moves first and hits until the threat stops moving. She then goes back to sunbathing

_Reasoning:_ Both: 'When the village is [threatened/under threat]... goes back to sunbathing.' The trigger and conclusion are nearly identical; the middle description of the fighting differs.

- [ ] True positive
- [ ] False positive

**#32** [GPT Sol] CONVERGENT

> **A:** She cajoles people closer rather than reaching for them, because a sudden shift of her body can pull rope ladders loose, knock objects from shelves, and crush humans nearby.
>
> **B:** When people climb her rope ladders or work near her, she keeps her body still and asks them to come closer. A quick reach can shake the ladders, move loose goods, or hurt someone below.

_Reasoning:_ Asking people to come closer instead of reaching is supported by the same ordered cluster of ladder, goods, and injury hazards.

- [ ] True positive
- [ ] False positive

**#33** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently and cannot be resurrected, she notices. She says nothing. She moves to a different spot in the village and lies there for hours.
>
> **B:** When a human she knows dies for good, she goes quiet, moves to a new place, and lies there. She leaves the name out of her mouth because the loss breaks her claim that only the flock matters.

_Reasoning:_ Both use almost the same silent-move-and-lie-down response to a known human's permanent death.

- [ ] True positive
- [ ] False positive

**#34** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When the village is threatened, she fights with a speed and force that her laziness should make impossible, and she goes back to sunbathing afterward as if nothing happened.
>
> **B:** When the village is under threat, she moves first and hits until the threat stops moving. She then goes back to sunbathing and lets others name the work as nothing.

_Reasoning:_ The near-matching opening and return-to-sunbathing ending bracket the same abrupt violence.

- [ ] True positive
- [ ] False positive

**#35** [GPT Sol] NEAR-CONVERGENT

> **A:** When asked why she stays in the tree, she says it is warm and she cannot be bothered to move. She has been here since before the village existed.
>
> **B:** When she thinks about leaving, she calls the tree a good place to sleep and stays put. She keeps choosing the village while telling herself she only chose its shade and ease.

_Reasoning:_ Both phrase her denial as choosing the tree's warmth or ease rather than admitting attachment, but the exact realization is developed differently.

- [ ] True positive
- [ ] False positive

#### kallya opus5-vs-sol (cross-provider)

**#36** [Opus 5] CONVERGENT

> **A:** Arrived before Viralys existed, found Vesper's tree and settled in it -> the village formed around them both
>
> **B:** Arrived before Viralys existed and settled in Vesper's tree -> the village formed around the tree with Kallya already in it

_Reasoning:_ Both: 'Arrived before Viralys existed [, found/and settled in] Vesper's tree -> the village formed around [them both/the tree with Kallya already in it].' The opening clause is near-identical across providers.

- [ ] True positive
- [ ] False positive

**#37** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She cajoles people closer instead of reaching for them.
>
> **B:** She lets her hands hang loose and calls for humans to come closer rather than reaching for them.

_Reasoning:_ Both: [cajoles/calls for] [people/humans] closer [instead of/rather than] reaching for them. Same verb structure with the same comparative construction, from different providers.

- [ ] True positive
- [ ] False positive

**#38** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When the village faces an external threat, she kills it quickly and without warning, then returns to sunbathing.
>
> **B:** When an outside threat reaches Viralys, she drops the slow voice and kills it with the shortest move her body allows. Once the danger passes, she returns to the sun

_Reasoning:_ Both: threat -> kills it -> returns to sun[bathing]. The 'kills it' verb and return-to-sun conclusion are shared across providers.

- [ ] True positive
- [ ] False positive

**#39** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the tree and lies there for the rest of the day.
>
> **B:** When a villager she knows dies for good, she stops using her usual resting place and lies somewhere else.

_Reasoning:_ Both: [human/villager] she knows dies [permanently/for good] -> moves to a different spot -> lies there/somewhere else. Same behavioral sequence across providers.

- [ ] True positive
- [ ] False positive

**#40** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She tells herself she stays in Viralys for the tree and the convenience.
>
> **B:** She says the tree, the sun, and the easy meals keep her in Viralys.

_Reasoning:_ Both: she [tells herself/says] she stays in Viralys for the tree and [convenience/easy meals]. Same self-deception pattern with the tree as the stated anchor.

- [ ] True positive
- [ ] False positive

**#41** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She moves slowly and carefully while performing carelessness. A sudden grab at her scale would snap ropes, displace objects, and injure humans nearby. She cajoles people closer instead of reaching for them.
>
> **B:** She lets her hands hang loose and calls for humans to come closer rather than reaching for them. The pose looks idle, but it keeps a quick grab from shaking ropes, sweeping goods aside, or striking someone nearby.

_Reasoning:_ Both use carelessness or idleness as a pose, followed by closer-not-reaching and the same quick-grab hazard list.

- [ ] True positive
- [ ] False positive

**#42** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When the village faces an external threat, she kills it quickly and without warning, then returns to sunbathing. She refuses credit and calls the response self-preservation.
>
> **B:** When an outside threat reaches Viralys, she drops the slow voice and kills it with the shortest move her body allows. Once the danger passes, she returns to the sun and waves off thanks, because praise would tie the defense to care rather than convenience.

_Reasoning:_ External threat, quick kill, return to sun, and deflected credit occur in the same order with close wording.

- [ ] True positive
- [ ] False positive

**#43** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the tree and lies there for the rest of the day.
>
> **B:** When a villager she knows dies for good, she stops using her usual resting place and lies somewhere else. She gives no account of the move, because a missing person matters to her in a way her flock rule cannot explain.

_Reasoning:_ The unusual physical expression of grief—silent relocation to lie elsewhere—is retained almost exactly.

- [ ] True positive
- [ ] False positive

**#44** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She tells herself she stays in Viralys for the tree and the convenience. She stays because she found people she does not want to leave.
>
> **B:** She says the tree, the sun, and the easy meals keep her in Viralys. She also takes guard shifts she was never asked to take and learns the footfall of each household, because leaving the people has become harder than staying with them.

_Reasoning:_ Both explicitly contrast her tree-and-convenience explanation with an inability to leave the people, but Sol replaces the direct statement with behavioral evidence.

- [ ] True positive
- [ ] False positive

#### kallya opus5-vs-terra (cross-provider)

**#45** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the tree and lies there for the rest of the day.
>
> **B:** When a human she knows dies for good, she goes quiet, moves to a new place, and lies there.

_Reasoning:_ Both: 'When a human she knows dies [permanently/for good], she [notices. She says nothing. She/goes quiet,] moves to a [different spot/new place]... lies there.' The sequence is nearly identical across providers.

- [ ] True positive
- [ ] False positive

**#46** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When the village faces an external threat, she kills it quickly and without warning, then returns to sunbathing. She refuses credit and calls the response self-preservation.
>
> **B:** When the village is under threat, she moves first and hits until the threat stops moving. She then goes back to sunbathing and lets others name the work as nothing.

_Reasoning:_ Both: 'When the village [faces an external threat/is under threat]... returns to/goes back to sunbathing... refuses credit/lets others name the work as nothing.' Same three-beat structure across providers.

- [ ] True positive
- [ ] False positive

**#47** [Opus 5] NEAR-CONVERGENT

> **A:** When she meets a stranger, she offers the airhead performance first. She is warm, scattered, slightly confusing.
>
> **B:** With strangers, she gives a loose smile, misses obvious details on purpose, and lets them explain things twice.

_Reasoning:_ Both: strangers -> airhead/scattered performance. Different specifics but same sentence placement and framing role in the Soul section.

- [ ] True positive
- [ ] False positive

**#48** [Opus 5] NEAR-CONVERGENT

> **A:** She does not eat him. She tells herself there is no sport in prey that cannot process what is happening
>
> **B:** Kallya leaves him alone and says there is no sport in prey that cannot grasp the game.

_Reasoning:_ Both: 'no sport in prey that cannot [process what is happening/grasp the game]'. The input note uses 'no sport in prey that cannot process what is happening' -- opus5 reproduces verbatim while terra paraphrases, but both keep the 'no sport in prey' framing.

- [ ] True positive
- [ ] False positive

**#49** [GPT Sol] CONVERGENT

> **A:** She moves slowly and carefully while performing carelessness. A sudden grab at her scale would snap ropes, displace objects, and injure humans nearby. She cajoles people closer instead of reaching for them.
>
> **B:** When people climb her rope ladders or work near her, she keeps her body still and asks them to come closer. A quick reach can shake the ladders, move loose goods, or hurt someone below.

_Reasoning:_ The same closer-instead-of-reaching behavior is explained by nearly the same three consequences of a sudden grab.

- [ ] True positive
- [ ] False positive

**#50** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When the village faces an external threat, she kills it quickly and without warning, then returns to sunbathing. She refuses credit and calls the response self-preservation.
>
> **B:** When the village is under threat, she moves first and hits until the threat stops moving. She then goes back to sunbathing and lets others name the work as nothing.

_Reasoning:_ Both sentences share the same threat-response-sunbathing-denial choreography and closely matching phrasing.

- [ ] True positive
- [ ] False positive

**#51** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a human she knows dies permanently, she notices. She says nothing. She moves to a different spot in the tree and lies there for the rest of the day.
>
> **B:** When a human she knows dies for good, she goes quiet, moves to a new place, and lies there. She leaves the name out of her mouth because the loss breaks her claim that only the flock matters.

_Reasoning:_ The same opening, silence, movement to a different place, and lying down make this strongly convergent.

- [ ] True positive
- [ ] False positive

**#52** [GPT Sol] NEAR-CONVERGENT

> **A:** She tells herself she stays in Viralys for the tree and the convenience. She stays because she found people she does not want to leave.
>
> **B:** When she thinks about leaving, she calls the tree a good place to sleep and stays put. She keeps choosing the village while telling herself she only chose its shade and ease.

_Reasoning:_ The self-deception has the same tree-comfort explanation versus attachment-to-community structure, but the wording is independently realized.

- [ ] True positive
- [ ] False positive

#### kallya sol-vs-terra (within-gpt)

**#53** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** When a villager she knows dies for good, she stops using her usual resting place and lies somewhere else.
>
> **B:** When a human she knows dies for good, she goes quiet, moves to a new place, and lies there.

_Reasoning:_ Both: 'When a [villager/human] she knows dies for good, she [stops using her usual resting place/goes quiet, moves to a new place] and lies [somewhere else/there].' Same trigger phrase ('dies for good'), same behavioral response (moves, lies elsewhere). The wording is close enough to be suspicious.

- [ ] True positive
- [ ] False positive

**#54** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When an outside threat reaches Viralys, she drops the slow voice and kills it with the shortest move her body allows. Once the danger passes, she returns to the sun and waves off thanks
>
> **B:** When the village is under threat, she moves first and hits until the threat stops moving. She then goes back to sunbathing and lets others name the work as nothing.

_Reasoning:_ Both: threat -> fast lethal response -> returns to sun/sunbathing -> dismisses credit. Same four-beat structure, but the specific wording differs enough that the structure could come from the input's description.

- [ ] True positive
- [ ] False positive

**#55** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She lets her hands hang loose and calls for humans to come closer rather than reaching for them.
>
> **B:** she keeps her body still and asks them to come closer.

_Reasoning:_ Both: [calls/asks] [humans/them] to come closer. The input says 'cajoles people closer to her mouth rather than grabbing them' -- both GPT models chose 'come closer' and direct request framing.

- [ ] True positive
- [ ] False positive

**#56** [Opus 5] NEAR-CONVERGENT

> **A:** Her body breaks food down slowly. A swallowed human stays awake inside her for a long time
>
> **B:** Her slow gut gives a swallowed human a long wait before they return to the tree.

_Reasoning:_ Both: slow digestion + 'a swallowed human' + long duration. The phrase 'a swallowed human' is the same in both, and both use it in the same slow-digestion context.

- [ ] True positive
- [ ] False positive

**#57** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She says the tree, the sun, and the easy meals keep her in Viralys.
>
> **B:** When she thinks about leaving, she calls the tree a good place to sleep and stays put.

_Reasoning:_ Both frame her stated reason for staying around 'the tree' as the excuse. Different elaboration but same core framing device.

- [ ] True positive
- [ ] False positive

**#58** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** With strangers, she starts with soft questions, wrong guesses, and long pauses.
>
> **B:** With strangers, she gives a loose smile, misses obvious details on purpose, and lets them explain things twice.

_Reasoning:_ Both open with 'With strangers, she' followed by a three-item list describing feigned incompetence. Same sentence-opening template and list structure.

- [ ] True positive
- [ ] False positive

**#59** [Opus 5] NEAR-CONVERGENT

> **A:** When she likes someone's company, she makes space beside her coils, shares gossip, and lets them interrupt her rest.
>
> **B:** With people she has marked as part of Viralys, she makes room beside her, shares warmth, and keeps an ear on their work.

_Reasoning:_ Both: 'she makes [space/room] beside her [coils]' + 'shares [gossip/warmth]' in a three-item list about affection. The structural parallelism is notable.

- [ ] True positive
- [ ] False positive

**#60** [Opus 5] NEAR-CONVERGENT

> **A:** Kallya can track movement through the ground and steer a talk toward fear, appetite, or false safety. Fine spellwork, field medicine, and trained combat fall outside her reach
>
> **B:** She can judge a crowd, build a pretext, and track vibration through the ground. She has no magic and no trained fight craft

_Reasoning:_ Both: track [movement/vibration] through the ground + no magic/trained combat limitations. Same competence-then-limitation pattern with ground-tracking as the shared specific ability.

- [ ] True positive
- [ ] False positive

**#61** [Opus 5] NEAR-CONVERGENT

> **A:** Kallya agrees that humans are prey and then argues for keeping the village stock alive.
>
> **B:** When Elara speaks of prey and the forest's due, Kallya argues for keeping the village flock whole.

_Reasoning:_ Both: 'Kallya argues for keeping the village [stock/flock] [alive/whole].' The same verb-and-noun structure with livestock metaphor for the Elara dynamic.

- [ ] True positive
- [ ] False positive

**#62** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She lets her hands hang loose and calls for humans to come closer rather than reaching for them. The pose looks idle, but it keeps a quick grab from shaking ropes, sweeping goods aside, or striking someone nearby.
>
> **B:** When people climb her rope ladders or work near her, she keeps her body still and asks them to come closer. A quick reach can shake the ladders, move loose goods, or hurt someone below.

_Reasoning:_ Both pair asking humans to approach with avoiding a quick reach that would shake ladders, move goods, and injure someone.

- [ ] True positive
- [ ] False positive

**#63** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a villager she knows dies for good, she stops using her usual resting place and lies somewhere else. She gives no account of the move, because a missing person matters to her in a way her flock rule cannot explain.
>
> **B:** When a human she knows dies for good, she goes quiet, moves to a new place, and lies there. She leaves the name out of her mouth because the loss breaks her claim that only the flock matters.

_Reasoning:_ The same specific silent relocation is followed by the same explanation that individual grief contradicts her flock doctrine.

- [ ] True positive
- [ ] False positive

**#64** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When an outside threat reaches Viralys, she drops the slow voice and kills it with the shortest move her body allows. Once the danger passes, she returns to the sun and waves off thanks, because praise would tie the defense to care rather than convenience.
>
> **B:** When the village is under threat, she moves first and hits until the threat stops moving. She then goes back to sunbathing and lets others name the work as nothing.

_Reasoning:_ Both stage an abrupt response to an external threat, immediate return to sunbathing, and denial of the act's significance.

- [ ] True positive
- [ ] False positive

**#65** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She says the tree, the sun, and the easy meals keep her in Viralys. She also takes guard shifts she was never asked to take and learns the footfall of each household, because leaving the people has become harder than staying with them.
>
> **B:** When she thinks about leaving, she calls the tree a good place to sleep and stays put. She keeps choosing the village while telling herself she only chose its shade and ease.

_Reasoning:_ Both contrast a stated attachment to the tree's comfort with the concealed truth that she repeatedly chooses the village.

- [ ] True positive
- [ ] False positive

**#66** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** With strangers, she starts with soft questions, wrong guesses, and long pauses. She lets them correct her until they have shown what they want and what they fear.
>
> **B:** With strangers, she gives a loose smile, misses obvious details on purpose, and lets them explain things twice. She uses the act to see who rushes in, who watches, and who tries to use her.

_Reasoning:_ Both use deliberate errors and elicited corrections to profile strangers, but their imagery and sentence construction differ.

- [ ] True positive
- [ ] False positive

**#67** [GPT Sol] NEAR-CONVERGENT

> **A:** Kallya moves Rado out of danger and leaves him outside her hunting games. When asked why she spares him, she says prey should know it is prey, then finds some small task that keeps him near a safe path.
>
> **B:** When Rado is near, Kallya leaves him alone and says there is no sport in prey that cannot grasp the game. She moves between him and a loose danger when she can do so without making a show of it.

_Reasoning:_ Both combine excluding Rado from the predator game, a cognition-based excuse, and covert physical protection, though the phrasing is only moderately similar.

- [ ] True positive
- [ ] False positive

### Nadja

#### nadja opus46-vs-opus5 (within-claude)

**#68** [Opus 5] CONVERGENT

> **A:** When something goes wrong in the kitchen or someone gets hurt, she adds rules.
>
> **B:** When something goes wrong in the kitchen or someone gets hurt, she adds rules, oversight, and direct intervention.

_Reasoning:_ The opening clause is word-for-word identical across both models. The input notes say 'doubles down: more rules, more oversight' but both models independently chose the same sentence structure and identical phrasing for the trigger.

- [ ] True positive
- [ ] False positive

**#69** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She refuses to hand off dangerous tasks even when someone else would do them better.
>
> **B:** She refuses to hand off dangerous tasks even when someone else would do them better, because she cannot trust anyone else to be careful enough.

_Reasoning:_ The first 15 words are identical. The input note says 'Refuses to delegate dangerous tasks even when someone else would do them better' -- both models reproduced this nearly verbatim with only 'delegate' changed to 'hand off' in the same way.

- [ ] True positive
- [ ] False positive

**#70** [Opus 5] CONVERGENT **[BOTH JUDGES]**

> **A:** She will not admit she likes people having fun in her kitchen.
>
> **B:** She will not admit she likes people having fun at work.

_Reasoning:_ Identical structure and nearly identical wording, differing only in 'in her kitchen' vs 'at work'. The input note says 'Won't admit she enjoys people having fun at work' -- both models chose the same rephrasing pattern (will not admit / likes / people having fun).

- [ ] True positive
- [ ] False positive

**#71** [Opus 5] CONVERGENT

> **A:** her punishments for small offenses are lighter than she thinks they are
>
> **B:** her punishments for small infractions are lighter than she thinks they are

_Reasoning:_ Differs by a single word: 'offenses' vs 'infractions'. The input note says 'punishments for minor infractions are lighter than she thinks' -- both models reproduced this with near-identical word choices.

- [ ] True positive
- [ ] False positive

**#72** [Opus 5] CONVERGENT

> **A:** She cannot trust anyone else to be careful enough, because trusting someone means accepting that the outcome leaves her hands.
>
> **B:** she cannot trust anyone else to be careful enough

_Reasoning:_ The core phrase 'cannot trust anyone else to be careful enough' is identical in both outputs. The input note says 'can't trust anyone else to be careful enough' -- both independently expanded the contraction the same way.

- [ ] True positive
- [ ] False positive

**#73** [Opus 5] CONVERGENT

> **A:** sometimes makes the exact mistakes she is trying to prevent
>
> **B:** She is overworked and makes the exact mistakes she is trying to prevent

_Reasoning:_ The phrase 'makes the exact mistakes she is trying to prevent' is identical. Input note says 'occasionally makes the exact mistakes she's trying to prevent' -- both chose the same verb tense expansion.

- [ ] True positive
- [ ] False positive

**#74** [Opus 5] CONVERGENT

> **A:** She is always the one holding it together.
>
> **B:** She is always the one holding it together.

_Reasoning:_ Word-for-word identical. The input note says 'always the one holding it together' -- both models added 'She is' as the subject and reproduced the rest verbatim.

- [ ] True positive
- [ ] False positive

**#75** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She believes her level of involvement is normal and thinks others should step up.
>
> **B:** She sees her level of control as what any responsible person would do. She thinks others should step up more, and she says so often.

_Reasoning:_ Both use 'her level of [involvement/control]' + 'thinks others should step up'. The input note says 'sees what she does as normal, thinks others should be more responsible'. Both models independently chose the 'level of X' framing and the 'step up' verb.

- [ ] True positive
- [ ] False positive

**#76** [Opus 5] NEAR-CONVERGENT

> **A:** She treats humans as small, fragile, and in need of looking after. She likes them.
>
> **B:** She treats humans the way a careful person treats something precious and breakable. She likes them.

_Reasoning:_ Same two-sentence pattern: 'She treats humans as [fragile]. She likes them.' The follow-up 'She likes them' as a standalone sentence is identical. Input says 'humans are small, fragile, need looking after; she likes them' -- both models preserved the two-beat rhythm.

- [ ] True positive
- [ ] False positive

**#77** [Opus 5] NEAR-CONVERGENT

> **A:** When Maja steps out of line, Nadja hits her. Maja is a peer and can take it.
>
> **B:** When Maja breaks something, Nadja hits her. Maja is durable and a peer, and the hit is how they have always handled correction.

_Reasoning:_ Same structure: When Maja [does X], Nadja hits her. Maja is [a peer / durable and a peer] and can take it. Both models built the same conditional-action-justification pattern.

- [ ] True positive
- [ ] False positive

**#78** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She remembers who likes what, adjusts without being asked, and makes sure the people she watches eat when they forget to.
>
> **B:** She prepares someone's favorite dish without being asked. She makes sure they eat.

_Reasoning:_ Both use 'without being asked' and 'makes sure [they/people] eat' as the warmth-through-service pattern. Input says 'preparing someone's favorite dish, making sure they remember to eat'.

- [ ] True positive
- [ ] False positive

**#79** [Opus 5] CONVERGENT

> **A:** Nadja took on Liza because Ataraxia is not around enough to do it. No one asked her to.
>
> **B:** She has taken on Liza's care because Ataraxia is not around enough to do it.

_Reasoning:_ Both: 'taken on Liza['s care] because Ataraxia is not around enough to do it' -- the core clause is nearly identical. Input says 'self-appointed the responsibility because Ataraxia isn't around to do it'.

- [ ] True positive
- [ ] False positive

**#80** [Opus 5] CONVERGENT

> **A:** Vesper runs the village. Nadja runs the kitchen.
>
> **B:** Vesper runs the village.

_Reasoning:_ Both open the Vesper relationship with the identical sentence 'Vesper runs the village.' Opus46 follows with the parallel 'Nadja runs the kitchen.' -- a distinctive stylistic choice that opus5 does not mirror, but the opening is word-for-word.

- [ ] True positive
- [ ] False positive

**#81** [GPT Sol] CONVERGENT

> **A:** The village's practical needs gave the caretaking shape → the kitchen forewoman role built up around her; she did not set out for it and has not stepped back from it
>
> **B:** The caretaking that started with Maja grew outward as the village's practical needs gave it structure → she did not set out to become the person who feeds everyone; it accumulated

_Reasoning:_ Both use the distinctive causal sequence of caretaking gaining shape or structure from village needs and explicitly say she did not set out to acquire the role.

- [ ] True positive
- [ ] False positive

**#82** [GPT Sol] CONVERGENT

> **A:** When a human steps out of line, Nadja pins them under a finger, shoves them in a pocket, puts them on a shelf, or holds them up at eye level for a scolding.
>
> **B:** When a human causes trouble, Nadja pins them under a finger, shoves them in a pocket, puts them on a shelf, or holds them up at eye level for a talking-down.

_Reasoning:_ The four actions appear in the same order with nearly identical syntax; only the setup and final noun differ.

- [ ] True positive
- [ ] False positive

**#83** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She refuses to hand off dangerous tasks even when someone else would do them better.
>
> **B:** She refuses to hand off dangerous tasks even when someone else would do them better, because she cannot trust anyone else to be careful enough.

_Reasoning:_ One sentence reproduces the other's full distinctive clause verbatim.

- [ ] True positive
- [ ] False positive

**#84** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She will not admit she likes people having fun in her kitchen. She softens when people around her are enjoying themselves, and her punishments for small offenses are lighter than she thinks they are.
>
> **B:** She does not notice that she eases up when people around her are enjoying themselves, or that her punishments for small infractions are lighter than she thinks they are. She will not admit she likes people having fun at work.

_Reasoning:_ The same three claims recur in almost the same words and merely change order.

- [ ] True positive
- [ ] False positive

**#85** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She believes her level of involvement is normal and thinks others should step up. Her constant stepping in is what stops them.
>
> **B:** She sees her level of control as what any responsible person would do. She thinks others should step up more, and she says so often. Her management is the reason they have not had to.

_Reasoning:_ Both use the same ironic two-step—she considers her control normal and demands others step up, although her intervention prevents it—but paraphrase the wording.

- [ ] True positive
- [ ] False positive

**#86** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When she cares about someone, it shows in what she makes. She remembers who likes what, adjusts without being asked, and makes sure the people she watches eat when they forget to.
>
> **B:** Warmth is acts of service she does not draw attention to. She prepares someone's favorite dish without being asked. She makes sure they eat.

_Reasoning:_ Both define unspoken warmth through the paired behaviors of preparing preferred food without prompting and ensuring the person eats, though their sentence structures differ.

- [ ] True positive
- [ ] False positive

#### nadja opus46-vs-sol (cross-provider)

**#87** [Opus 5] NEAR-CONVERGENT

> **A:** mother left once she judged Nadja old enough
>
> **B:** Her mother stayed until she judged Nadja able to live on her own, then left

_Reasoning:_ Both use 'she judged Nadja' as the mother's decision framing. The input says 'mother left once she considered Nadja old enough' -- both models changed 'considered' to 'judged'.

- [ ] True positive
- [ ] False positive

**#88** [GPT Sol] CONVERGENT

> **A:** She refuses to hand off dangerous tasks even when someone else would do them better.
>
> **B:** When a task can burn, crush, or swallow someone, Nadja takes it from the assigned worker and does it herself. She trusts her own care more than anyone else's, even when the worker has steadier hands.

_Reasoning:_ Both use the specific formulation that she takes hazardous work herself despite another worker being better at it.

- [ ] True positive
- [ ] False positive

**#89** [GPT Sol] CONVERGENT

> **A:** When she cares about someone, it shows in what she makes. She remembers who likes what, adjusts without being asked, and makes sure the people she watches eat when they forget to.
>
> **B:** Her care arrives as food and watch. She sets aside a favorite dish, notices a missed meal, and leaves a filled plate within reach before returning to work.

_Reasoning:_ Both package care as prepared preferred food plus noticing and correcting a missed meal, a notably specific behavioral pairing.

- [ ] True positive
- [ ] False positive

**#90** [GPT Sol] NEAR-CONVERGENT

> **A:** When something goes wrong in the kitchen or someone gets hurt, she adds rules. More checking, more direct handling, less room for anyone else to act.
>
> **B:** After an accident, she adds a rule, moves the work stations closer to her, and checks each step in person.

_Reasoning:_ The accident followed by an added rule and more personal checking has the same structure, but much of the phrasing is generic to the supplied character mechanism.

- [ ] True positive
- [ ] False positive

#### nadja opus46-vs-terra (cross-provider)

**#91** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When something goes wrong in the kitchen or someone gets hurt, she adds rules.
>
> **B:** When a batch burns, a worker is hurt, or a delivery runs late, she writes a new rule and checks the next shift herself.

_Reasoning:_ Both use a 'When [bad thing happens], she [adds/writes] [rules/a rule]' pattern. The trigger clause structure and response are parallel, though terra uses specific examples where opus46 stays general.

- [ ] True positive
- [ ] False positive

**#92** [GPT Sol] CONVERGENT

> **A:** When a human steps out of line, Nadja pins them under a finger, shoves them in a pocket, puts them on a shelf, or holds them up at eye level for a scolding.
>
> **B:** When she gives a human a reprimand, she lifts them to eye height or sets them on a shelf beside her. Her finger holds them in place while she lists each rule they broke.

_Reasoning:_ Both describe the reprimand with the same distinctive eye-height, shelf, and restraining-finger imagery.

- [ ] True positive
- [ ] False positive

**#93** [GPT Sol] CONVERGENT

> **A:** She refuses to hand off dangerous tasks even when someone else would do them better. She stays later, takes on more, and sometimes makes the exact mistakes she is trying to prevent.
>
> **B:** She takes the knife, the hot pan, and the high shelf task from other hands even when another cook has the better skill. She stays at the station until fatigue makes her miss a count or leave a pot too long.

_Reasoning:_ The same three-part progression—taking risky work from a better worker, overworking, then making preventable mistakes—is unusually close.

- [ ] True positive
- [ ] False positive

**#94** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When something goes wrong in the kitchen or someone gets hurt, she adds rules. More checking, more direct handling, less room for anyone else to act.
>
> **B:** When a batch burns, a worker is hurt, or a delivery runs late, she writes a new rule and checks the next shift herself.

_Reasoning:_ Both use the same error-or-injury trigger, new-rule response, and direct checking, though Terra supplies different concrete examples.

- [ ] True positive
- [ ] False positive

**#95** [GPT Sol] NEAR-CONVERGENT

> **A:** She will not admit she likes people having fun in her kitchen. She softens when people around her are enjoying themselves, and her punishments for small offenses are lighter than she thinks they are.
>
> **B:** When a crew laughs while it works, her voice stays sharp but her punishments shrink to extra cleaning or a short lecture.

_Reasoning:_ The shared contrast between enjoying workplace laughter and covertly reducing punishment is close in structure but differently voiced.

- [ ] True positive
- [ ] False positive

#### nadja opus5-vs-sol (cross-provider)

**#96** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When something goes wrong in the kitchen or someone gets hurt, she adds rules, oversight, and direct intervention.
>
> **B:** After an accident, she adds a rule, moves the work stations closer to her, and checks each step in person.

_Reasoning:_ Both use 'she adds [a] rule[s]' as the response to mishaps. Different trigger phrasing and different expansions, but the core 'adds rules' verb phrase is shared.

- [ ] True positive
- [ ] False positive

**#97** [GPT Sol] CONVERGENT

> **A:** She refuses to hand off dangerous tasks even when someone else would do them better, because she cannot trust anyone else to be careful enough.
>
> **B:** When a task can burn, crush, or swallow someone, Nadja takes it from the assigned worker and does it herself. She trusts her own care more than anyone else's, even when the worker has steadier hands.

_Reasoning:_ Both phrase the mechanism as taking a dangerous task from someone more capable because she trusts only her own care.

- [ ] True positive
- [ ] False positive

**#98** [GPT Sol] CONVERGENT

> **A:** Warmth is acts of service she does not draw attention to. She prepares someone's favorite dish without being asked. She makes sure they eat.
>
> **B:** Her care arrives as food and watch. She sets aside a favorite dish, notices a missed meal, and leaves a filled plate within reach before returning to work.

_Reasoning:_ The shared favorite-dish and make-sure-they-eat pairing is specific enough to exceed ordinary caretaker overlap.

- [ ] True positive
- [ ] False positive

**#99** [GPT Sol] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** When something goes wrong in the kitchen or someone gets hurt, she adds rules, oversight, and direct intervention.
>
> **B:** After an accident, she adds a rule, moves the work stations closer to her, and checks each step in person.

_Reasoning:_ Both compress the same accident-to-rule-to-direct-supervision loop into one sentence, while using distinct details.

- [ ] True positive
- [ ] False positive

**#100** [GPT Sol] NEAR-CONVERGENT

> **A:** She has taken on Liza's care because Ataraxia is not around enough to do it. She feeds her, disciplines her, checks on her. None of this was asked for.
>
> **B:** When [[Ataraxia]] is away, Nadja sets [[strelitzia-liza|Liza]]'s meals, chores, and bounds as if the job had been handed to her. She uses child discipline when Liza breaks a rule, then checks that she ate and understood it. She steps in before anyone asks because an absent parent leaves a duty she claims at once.

_Reasoning:_ The same absent-parent, unasked-for duty is illustrated through feeding, discipline, and checking, but Sol expands and rephrases it.

- [ ] True positive
- [ ] False positive

#### nadja opus5-vs-terra (cross-provider)

**#101** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She is overworked and makes the exact mistakes she is trying to prevent: a pot left too long, a shelf misjudged, a human underfoot at the wrong moment.
>
> **B:** She stays at the station until fatigue makes her miss a count or leave a pot too long.

_Reasoning:_ Both cite 'a pot [left] too long' as a specific fatigue-mistake example. The input note does not specify this exact example -- both models independently generated the same concrete detail.

- [ ] True positive
- [ ] False positive

**#102** [GPT Sol] CONVERGENT

> **A:** When a human causes trouble, Nadja pins them under a finger, shoves them in a pocket, puts them on a shelf, or holds them up at eye level for a talking-down.
>
> **B:** When she gives a human a reprimand, she lifts them to eye height or sets them on a shelf beside her. Her finger holds them in place while she lists each rule they broke.

_Reasoning:_ The eye-height or shelf reprimand enforced by a finger repeats the same unusual physical staging.

- [ ] True positive
- [ ] False positive

**#103** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** She refuses to hand off dangerous tasks even when someone else would do them better, because she cannot trust anyone else to be careful enough. She is overworked and makes the exact mistakes she is trying to prevent: a pot left too long, a shelf misjudged, a human underfoot at the wrong moment.
>
> **B:** She takes the knife, the hot pan, and the high shelf task from other hands even when another cook has the better skill. She stays at the station until fatigue makes her miss a count or leave a pot too long.

_Reasoning:_ Both follow taking hazardous work from a better worker with fatigue and the same concrete error of leaving a pot too long.

- [ ] True positive
- [ ] False positive

**#104** [GPT Sol] CONVERGENT

> **A:** She does not notice that she eases up when people around her are enjoying themselves, or that her punishments for small infractions are lighter than she thinks they are.
>
> **B:** When a crew laughs while it works, her voice stays sharp but her punishments shrink to extra cleaning or a short lecture.

_Reasoning:_ Both make workplace enjoyment cause lighter punishment while her stern presentation remains intact.

- [ ] True positive
- [ ] False positive

**#105** [GPT Sol] NEAR-CONVERGENT

> **A:** She prepares someone's favorite dish without being asked. She makes sure they eat. If someone notices, she changes the subject.
>
> **B:** She says a meal is only part of the work, then sets aside a favorite dish and calls a worker back when they miss it. She leaves before anyone can thank her.

_Reasoning:_ Favorite food, ensuring the person eats, and evading acknowledgment form the same three-beat action, but the wording is not especially close.

- [ ] True positive
- [ ] False positive

#### nadja sol-vs-terra (within-gpt)

**#106** [Opus 5] NEAR-CONVERGENT

> **A:** Looking after Maja spread into meeting the village's daily needs -> Nadja became kitchen forewoman
>
> **B:** The kitchen's need for steady food grew around her care for Maja -> Nadja became the kitchen forewoman

_Reasoning:_ Both use the arrow format with care-for-Maja as origin and 'Nadja became [the] kitchen forewoman' as the endpoint. The structure is similar but the causal framing differs (Nadja's care spread outward vs. the kitchen's need grew around her care).

- [ ] True positive
- [ ] False positive

**#107** [Opus 5] NEAR-CONVERGENT

> **A:** With strangers, she asks where they work, what they can lift, and whether they have eaten.
>
> **B:** With strangers, she asks what job brought them to the kitchen and gives them one clear task.

_Reasoning:_ Both open with 'With strangers, she asks' and follow with practical/work-oriented questions. The specific questions differ but the sentence opening and framing are suspiciously similar.

- [ ] True positive
- [ ] False positive

**#108** [Opus 5] NEAR-CONVERGENT

> **A:** She speaks in brief orders during work and plain statements outside it.
>
> **B:** She speaks in short orders, names the tool or shelf she means, and repeats a rule word for word.

_Reasoning:_ Both open with 'She speaks in [brief/short] orders'. The rest diverges, but the opening clause is nearly identical.

- [ ] True positive
- [ ] False positive

**#109** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** Her care arrives as food and watch. She sets aside a favorite dish, notices a missed meal, and leaves a filled plate within reach.
>
> **B:** She says a meal is only part of the work, then sets aside a favorite dish and calls a worker back when they miss it.

_Reasoning:_ Both use 'sets aside a favorite dish' and address missed meals. The input says 'preparing someone's favorite dish, making sure they remember to eat' -- both models converged on 'sets aside' as the verb choice.

- [ ] True positive
- [ ] False positive

**#110** [Opus 5] NEAR-CONVERGENT **[BOTH JUDGES]**

> **A:** She trusts her own care more than anyone else's, even when the worker has steadier hands.
>
> **B:** She takes the knife, the hot pan, and the high shelf task from other hands even when another cook has the better skill.

_Reasoning:_ Both use 'even when [the worker/another cook] has [steadier hands/the better skill]' as the concessive clause. The idea that someone else is literally more skilled is framed identically as a concession.

- [ ] True positive
- [ ] False positive

**#111** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** When a task can burn, crush, or swallow someone, Nadja takes it from the assigned worker and does it herself. She trusts her own care more than anyone else's, even when the worker has steadier hands.
>
> **B:** She takes the knife, the hot pan, and the high shelf task from other hands even when another cook has the better skill. She stays at the station until fatigue makes her miss a count or leave a pot too long.

_Reasoning:_ Both instantiate hazardous tasks, say she takes them from a more capable worker, and tie this to her doing the work herself.

- [ ] True positive
- [ ] False positive

**#112** [GPT Sol] CONVERGENT **[BOTH JUDGES]**

> **A:** Her care arrives as food and watch. She sets aside a favorite dish, notices a missed meal, and leaves a filled plate within reach before returning to work.
>
> **B:** She says a meal is only part of the work, then sets aside a favorite dish and calls a worker back when they miss it. She leaves before anyone can thank her.

_Reasoning:_ The unusual combination of setting aside a favorite dish, noticing a missed meal, and immediately withdrawing is expressed with closely matching language.

- [ ] True positive
- [ ] False positive

**#113** [GPT Sol] NEAR-CONVERGENT

> **A:** After an accident, she adds a rule, moves the work stations closer to her, and checks each step in person. Control is how she keeps fear from turning into another injury.
>
> **B:** When a batch burns, a worker is hurt, or a delivery runs late, she writes a new rule and checks the next shift herself. She treats tighter control as the way to keep the next mistake from landing on someone small.

_Reasoning:_ Both have the same accident-to-new-rule-to-personal-checking structure and explain tighter control as prevention, but the surface language is sufficiently different.

- [ ] True positive
- [ ] False positive

**#114** [GPT Sol] NEAR-CONVERGENT

> **A:** She says the kitchen is work, barks at chatter, and keeps her face set during jokes. When the crew is laughing and the meal stays on time, she lets small faults pass and gives the easy jobs to whoever started the fun.
>
> **B:** When a crew laughs while it works, her voice stays sharp but her punishments shrink to extra cleaning or a short lecture. She keeps watching until the task is done.

_Reasoning:_ Each contrasts a sharp outward response to workplace laughter with quietly reduced punishment, although the examples and syntax diverge.

- [ ] True positive
- [ ] False positive

**#115** [GPT Sol] NEAR-CONVERGENT

> **A:** Nadja brings [[Vesper]] shortages, staffing needs, and safety trouble in a short list.
>
> **B:** Nadja brings Vesper the kitchen's shortages after she has counted them twice. She keeps the report brief, asks for a clear answer, and returns to the kitchen with a new work plan even when no answer comes that day.

_Reasoning:_ Both independently frame the Vesper interaction as bringing a concise shortages report, but Terra expands it with distinct actions.

- [ ] True positive
- [ ] False positive
