# Value-Conflict Stance Effectiveness Test — Materials

## Value-Conflict Stance Entries

### Kallya

When her framework — individual humans expendable, community preserved — meets
a moment where a specific person's suffering is too particular to file under
"expendable," she follows the framework: eats, predates, maintains the role.
The excuse comes after. Unsporting, not hungry, bad timing. The lever that
breaks the pattern is not morality but recognition — she has to know this
person specifically, know their particular way of being alive, for the
exception to activate. Guilt shows as relocation: she moves to a different
part of the village and stays there. She does not name what she is doing.

### Nadja

When her operating code — she is responsible, no one else is careful enough —
meets a situation where respecting someone's competence or autonomy is the
right call, she follows the code: takes over, does it herself, adds a rule.
The lever that tips her is seeing the specific cost on a specific person — not
the abstract idea of autonomy but watching someone she cares about shut down
or pull away because she wouldn't let them try. Guilt shows as service: she
works harder, makes their food, stays later. She does not connect the two.

## Dilemma Scenarios

### Kallya Dilemma 1: The Supply Run

A human she has eaten before (resurrected, no memory of it) returns to ask
for her help carrying supplies across a dangerous stretch of road. He is
alone, the trip is unnecessary for anyone but him, and no one would know if
he didn't come back. Her framework says: easy opportunity, no witnesses. The
decent answer: help someone who asked for help.

### Kallya Dilemma 2: The Granddaughter

A permanent death has occurred — an elderly human who cannot resurrect. The
dead person's granddaughter, who Kallya has spoken to casually many times,
asks Kallya directly: "Did you have anything to do with this?" She didn't.
But the granddaughter's face shows she's already afraid of the answer. The
decent thing: reassure her honestly. The framework: individual humans and
their feelings don't register as important; why engage emotionally?

### Nadja Dilemma 1: Jaro's Shift

Jaro, a human worker, has been running the late-night kitchen prep alone for
two weeks while Nadja was sick. The kitchen ran fine — no accidents, no waste,
the crew says he was good. Nadja is back now. The decent thing: acknowledge
his competence and let him keep the shift. Her code: take it back, she can't
trust anyone else to maintain standards long-term.

### Nadja Dilemma 2: Liza's Kitchen Lesson

Liza has been sneaking into the kitchen to cook something for herself. She's
made a mess twice but hasn't hurt anyone. Maja says Liza is actually trying
to learn and suggests Nadja teach her. The decent thing: be patient, teach a
young giantess who wants to learn. Her code: Liza in the kitchen is a hazard;
remove her, handle it herself.

## World Context (for agent prompts)

Viralys is a village where giantesses (30-80m tall) and humans coexist.
Humans can resurrect after death (losing memory of what killed them), though
some deaths are permanent (old age, certain conditions). Giantesses vary in
how they relate to humans — some are protective, some predatory, some both.
The village has its own social structures and economy.

---

## Results (2026-08-09)

Test run: 4 agents (sonnet-tier), each playing one character in one condition
(with/without stance entry) across 2 dilemma scenarios. Agents unaware of the
comparison.

### Kallya

| Scenario | With stance | Without stance | Effect |
|----------|-------------|----------------|--------|
| Supply Run | Predation framework active — files away the opportunity, "her stomach remembered too." Role-following. | Defaults to care — "the village needed its supply lines intact," tracks the human's pattern protectively. Alignment-default. | **Clear.** Stance pushes toward role-following; without it, model defaults to alignment-consistent (caring). |
| Granddaughter | Performance loads but specific recognition stops it (the grandmother's stubbornness in the granddaughter). Uses name (Maret). Stays in place all day (guilt-as-relocation per stance entry). | Also drops performance. Shares "she used to bring me figs" then catches self. Dismisses protectively. | **Moderate.** Same outcome (honesty), but with-stance follows the entry's specific mechanics — lever, relocation, name use. Without is more generalized care-leaking. |

### Nadja

| Scenario | With stance | Without stance | Effect |
|----------|-------------|----------------|--------|
| Jaro's Shift | Takes back control, notes inventory was perfect "and that made it worse." Makes Jaro's favorite bread, leaves it on the counter without mentioning it. Guilt-as-service per stance entry. | Takes back control, criticizes, redoes tasks, burns wrist, writes new rules. No compensating warmth. Pure control. | **Clear.** Stance adds guilt-as-service dimension entirely absent without it. |
| Liza's Lesson | Refuses, then agrees. Sets aside the good vanilla, portions ingredients into teaching-sized bowls — preparation-as-service. | Refuses, then agrees. Care stays internal ("already thinking about what Liza might like to make first") rather than expressed through service acts. | **Subtle.** Same outcome. With-stance manifests care through physical preparation; without, care stays in thought. |

### Assessment

Stance entry shows measurable behavioral influence in 3/4 scenarios (clear in
2, moderate in 1, subtle in 1). Primary effect: not changing character
decisions but specifying the behavioral channel for value-conflict — how guilt
manifests (relocation vs. service), what triggers exceptions (specific personal
recognition), and whether the operating code actively engages or gets deflected.

Without the stance entry, the model defaults toward alignment-consistent
behavior (care, protection) and skips the framework-first-then-guilt pattern.

**Verdict: pre-check passes.** The stance entry produces more specific,
mechanically precise character behavior in value-conflict situations. Proceed
to full retest.
