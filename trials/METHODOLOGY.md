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

Assessment reads notes, and output generated from notes by self-
contained probes. Full or real play sessions are out of scope: too many
uncontrolled variables, too much cost, and a human needed in the loop.
Simulated probes are in, provided they run start to finish without human
input.

Humans may grade. The system is built to need as little of that as
possible.
