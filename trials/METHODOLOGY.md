# Writing-Assessment Methodology

Standing methodology for assessing character-note writing. Kits under
`trials/` instantiate it. The self-review battery inside the production
card workflow draws its mechanisms from it.

## 1. Two systems, one methodology

**The A/B trial suite** is internal. It tests methodologies or inputs
against each other — doctrine variants, packet structures, prompt
changes — and exists to improve the production workflow. Nothing in it
ships.

**The production self-review battery** is the set of automated checks
that run inside character-card generation. Plugin users run it; it is
shipped skill prose.

The two share mechanisms but are not the same system. Mechanisms flow
one way: the suite is how a check earns its place in the battery, never
the reverse. See section 5.

## 2. Standing rules

These bind both systems.

### 2.1 Cold-read author/grader separation

Whoever authors assessment material pre-commits the failure they expect,
then writes without the answer key in view. Grading happens afterward,
separately. In agent terms: author-agent and grader-agent run in
separate contexts, and neither sees the other's reasoning.

Material written to pass its own audit verifies nothing.

### 2.2 Every metric is validated individually

An agent-run metric is trusted only after a blind comparison against
human judgment on that one metric, over the same material. Whole-result
agreement does not transfer: a suite can rank correctly overall while an
individual metric inside it is inverted.

Until a metric passes, its numbers carry an explicit `unvalidated` label
wherever they appear — rubrics, results records, battery output.

This rule exists because the 2026-07-23 blind trial ranked the human's
top note last. Independent agent graders scored all six notes nearly
identically, and their preference order inverted the human's.

### 2.3 The cheapness bar

A check is cheap when it runs without a human and stays under O(n^2) in
cast or content size. Cheap checks may run on every note. Anything above
the bar needs a stated justification and a sampling strategy.

### 2.4 What assessment reads

Assessment reads notes, and output generated from notes by
self-contained probes. Full or real play sessions are out of scope: too
many uncontrolled variables, too much cost, and a human needed in the
loop. Simulated probes are in, provided they run start to finish
without human input.

Humans may grade. The system is built to need as little of that as
possible.

## 3. The A/B trial suite

### 3.1 Trial protocol

1. **Freeze one brief.** Capture it through the project's normal
   authoring flow, then treat it as read-only for the trial's life.
   Every arm sees the same brief.
2. **Build one packet per arm.** A packet is the complete instruction
   set for one condition. Packets differ only in the variable under
   test.
3. **Generate blind.** Each arm's output comes from a fresh agent seeing
   its own packet and the brief — no other arm's packet, no rubric, no
   hypothesis.
4. **Grade blind.** The grader sees outputs stripped of arm identity, in
   an order that does not encode the key.
5. **Decode last.** The arm key opens only after every rubric cell is
   filled.

A grader who knows the arms is grading the hypothesis.

### 3.2 Probe design: scenario classes

A probe set covering only the intended path proves only that the
intended path works. Design probes across six classes:

| Class | What it asks |
| --- | --- |
| On-script | The canonical beat. Rarely fails; establishes a floor. |
| Trigger collision | Two or more behaviors fire at once. Which wins, and does the note say? |
| Near-miss | A situation resembling a trigger's context that should not fire it. |
| Off-script pressure | The scene cuts against the character's grain. |
| Coverage void | Aimed where the note is silent, forcing the invention question. |
| Lull | Nothing is demanded. Does the character act on standing goals? |

These are classes of question put to a note, and of simulated probe
generated from it. None requires live play.

### 3.3 Rubric construction

A rubric fixes its dimensions before any output exists. Each dimension
states its scale, what a top score means concretely, and whether an
agent can score it. Agent-scorable dimensions carry their validation
status per section 2.2.

Record raw counts — slop hits, trait-word leakage, length — separately
from judged scales. Counts survive a metric's invalidation; judged
scales do not.

The cross-model convergence metric defined at 4.4 is available to trials
as well as to the battery, but it needs paired generations: a trial that
intends to use it must generate each arm under two models, which
single-model packets do not do.

### 3.4 Instantiating a kit

A kit is a directory at `trials/<YYYY-MM>-<topic>/` holding the frozen
brief, one packet per arm, the rubric, the arm key, and a runner README.
The kit records what one trial did; this document records what every
trial does. A kit that restates a standing rule has copied it — link
instead.

First instance: `trials/2026-07-writing-doctrine/`.

## 4. The production self-review battery

Mechanism designs. Status is in section 5; nothing here is shipped prose
until it graduates.

### 4.1 Dilemma test and anti-convergence probe

**Run.** Write one scenario putting the character's highest-ranked value
against common decency. Answer it from the note alone.

**Pass:** the note decides. **Fail:** the author had to decide — the
motive content is underwritten and the value is decoration.

**Anti-convergence half.** Put the same dilemma to the character this
one was declared to be built against. The answers must differ in what
the characters do, not in how they sound. Same action in a different
accent is a fail.

**Cost:** O(1) per note. The probe targets the one declared contrast
character, not every pair.

**Caveat.** RoleCDE (arXiv:2606.01552) reports that role-conditioned
agents default to alignment-consistent choices over role-specific ones
when the two collide, and its demonstrated mitigation is fine-tuning,
not prompting. Expect a partial effect. This test verifies that
value-conflict material works rather than assuming it does.

### 4.2 Blind-line voice test, scatter-shot

**Run.** Take probe-generated dialogue, strip speaker attribution, and
have an agent assign each line to a character. Score as classification
accuracy.

**Sampling.** When a cast is large enough that all-pairs comparison
exceeds the section 2.3 bar, draw random subsets of characters and run
the test within each subset, repeating across different subsets rather
than completing the matrix.

**Pass:** accuracy meaningfully above chance for the subset size.
**Fail:** at-chance accuracy. The failure is homogenization across the
cast, not infidelity in any one note.

**Not adopted:** the full cross-character distinctiveness matrix. It is
O(n^2), and sampling answers the same question.

### 4.3 Counterfactual probe and the not-binding verdict

**Run.** For a behavior the note is supposed to compel, cite both the
generated line and the note line that produced it. Then ask whether that
same note line would equally permit the opposite behavior.

**Pass:** the note line rules the failing version out.
**Verdict `present but not binding`:** the material is there and permits
either outcome. The fix is directive language or a missing context
qualifier, not more prose.

**Status.** The most judgment-laden mechanism here. Its agent-run
verdicts need section 2.2 validation before they are trusted.

### 4.4 Cross-model convergence check

**Run.** Generate the same section from two models. Flag sentences the
two produce identically or near-identically.

**Reading.** Cross-model agreement marks a sentence as the model's voice
rather than the author's, so high convergence is a slop signal.

**Requires** paired generations, which single-model packets do not
produce. Enters the battery only if section 6 validates it.

**Not adopted:** AI detectors. They measure whether prose fools a
detector built for human readers, which is irrelevant to a note written
for a model to read.

## 5. Mechanism status and the graduation rule

A mechanism ships in the production battery only after the trial suite
has validated it under section 2.2. Adopting one ahead of measured data
stays possible, but it is an explicit human call recorded at the time —
never a default, never silent.

| Mechanism | Status |
| --- | --- |
| Dilemma test and anti-convergence probe (4.1) | Designed, pending validation |
| Blind-line voice test, scatter-shot (4.2) | Designed, pending validation |
| Counterfactual and not-binding verdict (4.3) | Designed, pending validation |
| Cross-model convergence check (4.4) | Designed, validation path in section 6 |

Nothing has graduated. No shipped skill implements this battery yet.

## 6. Convergence-metric validation path

**Step 1, same-family pilot.** Regenerate the six arms of the 2026-07-23
trial under two model tiers from the same family. Compute arm-level
convergence and correlate it against the human preference ranks already
recorded for those arms.

Same-family agreement is a weak signal: shared training makes two models
converge for reasons unrelated to authorial voice. The pilot is read as
a relative measure across arms, and it can only disqualify the metric or
support it provisionally.

**Step 2, cross-provider confirmation.** Rerun the correlation with
models from different providers once that access exists. Only this step
can move the metric to validated.

Until step 2 passes, the metric is labeled `unvalidated` per section 2.2.
