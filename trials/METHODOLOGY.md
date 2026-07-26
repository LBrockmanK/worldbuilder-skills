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
