---
type: plan
title: Author the standing writing-assessment methodology document
description: 'Implementation plan for trials/METHODOLOGY.md: the standing A/B trial
  suite, the production self-review battery designs with validation status, the graduation
  rule, and the convergence-metric validation path, plus a back-pointer from the 2026-07
  kit as the first instance.'
tags:
- human-ready
date: 2026-07-26
timestamp: 2026-07-26T15:51Z
resources:
- '[[2026-07-26-standing-writing-assessment-methodology-a-b-trial-suite-and-production-self-review-battery]]'
- '[[2026-07-26-implementation-research-standing-methodology-document-conventions]]'
---

# Author the standing writing-assessment methodology document

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> core-workflow:subagent-driven-development (recommended) or
> core-workflow:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires
> this plan artifact's approval flip.

## Goal

Author `trials/METHODOLOGY.md`, the standing writing-assessment methodology, per the [approved spec](../specs/2026-07-26-standing-writing-assessment-methodology-a-b-trial-suite-and-production-self-review-battery.md). Research dossier: [document conventions](../research/2026-07-26-implementation-research-standing-methodology-document-conventions.md).

**Architecture:** One prose document at `trials/METHODOLOGY.md`, sectioned so the two systems stay visibly distinct: standing rules that bind both, then the A/B trial suite, then the production battery designs, then the graduation rule and status table that connect them. A back-pointer is added to the 2026-07 kit so the standing-document/instance relationship is discoverable from either side. No code, no `skills/` edits, no changes to the kit's working files.

**Tech stack:** Plain markdown. No frontmatter (matching the kit's other files). Hard wrap at ~72 characters.

## Global Constraints

- The document lives at `trials/METHODOLOGY.md` — repo prose, not a vault document. No YAML frontmatter.
- Hard-wrap body prose at ~72 characters, max 76. Table rows and paths are exempt.
- Headings: `#` once, then `## N. Title` numbered sections, `###` for subsections. Matches `trials/2026-07-writing-doctrine/`.
- Model-neutral prose throughout: no product or vendor names, even though this file is internal. Say "two model tiers from the same family", never a vendor.
- Follows the plugin's writing doctrine: plain and concrete, no filler (`skills/writing-style.md`, checklist in `docs/slop-phrases.md`).
- Every mechanism in section 4 carries an explicit validation status. None is described as ready to ship.
- **Verification is structural, not test-driven.** `trials/` is outside the doodle glob and outside CI (dossier, Results), so there is no lint or test suite to appeal to. TDD does not apply to a prose deliverable; each task instead ends with exact commands whose output cannot be fabricated — heading lists, wrap-width checks, required-string greps.

## Tasks

### Task 1: Skeleton and standing rules

**Files:**
- Create: `trials/METHODOLOGY.md`

**Interfaces:**
- Produces: sections `## 1.` and `## 2.`, and the subsection anchors `2.1`–`2.4` that later sections cite as "§2.2" and "§2.3".

- [ ] **Step 1: Create the file with the header and section 1**

```markdown
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
```

- [ ] **Step 2: Append section 2, the standing rules**

```markdown
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
```

- [ ] **Step 3: Verify structure and wrap width**

Run:

```bash
cd trials && grep -n '^#\{1,3\} ' METHODOLOGY.md && python -c "import io; bad=[(i,len(l.rstrip())) for i,l in enumerate(io.open('METHODOLOGY.md',encoding='utf-8'),1) if len(l.rstrip())>76 and not l.lstrip().startswith('|') and '](' not in l]; print(bad if bad else 'WRAP OK')"
```

Expected: the heading list shows `# Writing-Assessment Methodology`, `## 1. Two systems, one methodology`, `## 2. Standing rules`, `### 2.1` through `### 2.4`; then `WRAP OK`.

- [ ] **Step 4: Confirm no frontmatter leaked in**

Run: `head -1 trials/METHODOLOGY.md`
Expected: `# Writing-Assessment Methodology` (not `---`).

- [ ] **Step 5: Commit**

```bash
git add trials/METHODOLOGY.md
git commit -m "Start the standing writing-assessment methodology

Sections 1-2: the internal suite / shipped battery distinction and the
rules binding both, including the per-metric validation rule that the
2026-07-23 rank inversion made necessary."
```

### Task 2: The A/B trial suite

**Files:**
- Modify: `trials/METHODOLOGY.md` (append section 3)

**Interfaces:**
- Consumes: section 2 anchors (cites "section 2.2" for agent-scorable dimensions).
- Produces: section `## 3.` with subsections `3.1` protocol, `3.2` scenario classes, `3.3` rubric construction, `3.4` kit instantiation.

- [ ] **Step 1: Append section 3**

````markdown
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
````

- [ ] **Step 2: Verify the section landed with its subsections**

Run: `grep -n '^### 3\.' trials/METHODOLOGY.md`
Expected: exactly four lines — `3.1 Trial protocol`, `3.2 Probe design: scenario classes`, `3.3 Rubric construction`, `3.4 Instantiating a kit`.

- [ ] **Step 3: Verify all six scenario classes are present**

Run:

```bash
python -c "import io; t=io.open('trials/METHODOLOGY.md',encoding='utf-8').read(); m=[c for c in ['On-script','Trigger collision','Near-miss','Off-script pressure','Coverage void','Lull'] if c not in t]; print('MISSING:',m) if m else print('ALL 6 CLASSES PRESENT')"
```

Expected: `ALL 6 CLASSES PRESENT`.

- [ ] **Step 4: Re-run the wrap check**

Run:

```bash
python -c "import io; bad=[(i,len(l.rstrip())) for i,l in enumerate(io.open('trials/METHODOLOGY.md',encoding='utf-8'),1) if len(l.rstrip())>76 and not l.lstrip().startswith('|') and '](' not in l]; print(bad if bad else 'WRAP OK')"
```

Expected: `WRAP OK`.

- [ ] **Step 5: Commit**

```bash
git add trials/METHODOLOGY.md
git commit -m "Add the standing A/B trial protocol and probe taxonomy

Generalizes the 2026-07 kit's procedure into a five-step protocol and
adds the six scenario classes, restated as note-interrogation classes
rather than the live-play audit they came from."
```

### Task 3: The production self-review battery

**Files:**
- Modify: `trials/METHODOLOGY.md` (append section 4)

**Interfaces:**
- Consumes: section 2.3 (cheapness bar) for the sampling rationale in 4.2; section 2.2 for the validation note in 4.3.
- Produces: subsection anchors `4.1`–`4.4`, cited by the section 5 status table.

- [ ] **Step 1: Append section 4**

````markdown
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
````

- [ ] **Step 2: Verify subsections and the model-neutrality constraint**

Run:

```bash
grep -n '^### 4\.' trials/METHODOLOGY.md && python -c "import io,re; t=io.open('trials/METHODOLOGY.md',encoding='utf-8').read(); h=re.findall(r'(?i)anthropic|openai|gpt-?[0-9]|claude|gemini|llama|mistral|pangram|gptzero',t); print('VENDOR NAMES FOUND:',set(h)) if h else print('MODEL-NEUTRAL OK')"
```

Expected: four `### 4.x` headings, then `MODEL-NEUTRAL OK`.

- [ ] **Step 3: Re-run the wrap check**

Run:

```bash
python -c "import io; bad=[(i,len(l.rstrip())) for i,l in enumerate(io.open('trials/METHODOLOGY.md',encoding='utf-8'),1) if len(l.rstrip())>76 and not l.lstrip().startswith('|') and '](' not in l]; print(bad if bad else 'WRAP OK')"
```

Expected: `WRAP OK`.

- [ ] **Step 4: Commit**

```bash
git add trials/METHODOLOGY.md
git commit -m "Design the production self-review battery

Four mechanisms at design level only, none shipped: the dilemma test
with its anti-convergence half, the scatter-shot voice test replacing an
O(n^2) matrix, the not-binding counterfactual, and the convergence check
pending validation. Records what was deliberately rejected - AI
detectors and the full distinctiveness matrix - so neither returns as a
fresh idea."
```

### Task 4: Graduation rule, status table, and the validation path

**Files:**
- Modify: `trials/METHODOLOGY.md` (append sections 5 and 6)

**Interfaces:**
- Consumes: the `4.1`–`4.4` anchors from Task 3 and the `2.2` anchor from Task 1.
- Produces: the finished document.

- [ ] **Step 1: Append sections 5 and 6**

````markdown
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
````

- [ ] **Step 2: Verify the status table covers every section 4 mechanism**

Run:

```bash
python -c "import io,re; t=io.open('trials/METHODOLOGY.md',encoding='utf-8').read(); tbl=t.split('## 5.')[1]; missing=[a for a in ['(4.1)','(4.2)','(4.3)','(4.4)'] if a not in tbl]; print('MISSING FROM TABLE:',missing) if missing else print('ALL 4 MECHANISMS IN STATUS TABLE')"
```

Expected: `ALL 4 MECHANISMS IN STATUS TABLE`.

- [ ] **Step 3: Verify no mechanism is described as shipped**

Run: `grep -n 'graduated\|shipped' trials/METHODOLOGY.md`
Expected: every hit states the negative — "Nothing has graduated", "No shipped skill implements this battery yet", "nothing here is shipped prose until it graduates", plus the section 1 definition. No hit claims a mechanism is live.

- [ ] **Step 4: Full-document structural check**

Run:

```bash
grep -c '' trials/METHODOLOGY.md && grep -n '^## ' trials/METHODOLOGY.md && python -c "import io; bad=[(i,len(l.rstrip())) for i,l in enumerate(io.open('trials/METHODOLOGY.md',encoding='utf-8'),1) if len(l.rstrip())>76 and not l.lstrip().startswith('|') and '](' not in l]; print(bad if bad else 'WRAP OK')"
```

Expected: a line count in the 240–330 range; six `## N.` headings in order 1–6; `WRAP OK`.

- [ ] **Step 5: Commit**

```bash
git add trials/METHODOLOGY.md
git commit -m "Add the graduation rule and convergence validation path

Section 5 states the one-way flow from suite to battery and the status
of all four mechanisms, none graduated. Section 6 records why the
same-family pilot can only disqualify or provisionally support the
metric - shared training makes convergence likely for reasons unrelated
to voice - so only the cross-provider pass can validate it."
```

### Task 5: Point the first instance at the standing document

**Files:**
- Modify: `trials/2026-07-writing-doctrine/README.md` (add a pointer near the top of `## 1. What this is`)

**Interfaces:**
- Consumes: the finished `trials/METHODOLOGY.md`.

The kit's working files are otherwise untouched — this adds a cross-reference, not a rewrite.

- [ ] **Step 1: Read the current section**

Run: `sed -n '1,16p' trials/2026-07-writing-doctrine/README.md`
Expected: the `# Trial Runner` heading and the `## 1. What this is` section, to see the exact prose the pointer follows.

- [ ] **Step 2: Insert the pointer as the last line of `## 1. What this is`**

Add this paragraph at the end of that section, before the `## 2. Setup` heading:

```markdown
Standing rules for every trial — the blind protocol, probe classes,
rubric construction, and the metric-validation rule — live in
`../METHODOLOGY.md`. This kit is that document's first instance and
records only what is specific to this trial.
```

- [ ] **Step 3: Verify the pointer landed inside section 1**

Run:

```bash
python -c "import io; t=io.open('trials/2026-07-writing-doctrine/README.md',encoding='utf-8').read(); s1=t.split('## 2.')[0]; print('POINTER IN SECTION 1' if '../METHODOLOGY.md' in s1 else 'POINTER MISPLACED OR MISSING')"
```

Expected: `POINTER IN SECTION 1`.

- [ ] **Step 4: Verify the relative path resolves**

Run:

```bash
python -c "import os; print('PATH OK' if os.path.exists('trials/2026-07-writing-doctrine/../METHODOLOGY.md') else 'BROKEN PATH')"
```

Expected: `PATH OK`.

- [ ] **Step 5: Confirm nothing else in the kit changed**

Run: `git diff --stat`
Expected: one file changed — `trials/2026-07-writing-doctrine/README.md` — with roughly 5 insertions and 0 deletions.

- [ ] **Step 6: Commit**

```bash
git add trials/2026-07-writing-doctrine/README.md
git commit -m "Link the 2026-07 kit to the standing methodology

Makes the standing-document/instance relationship discoverable from the
kit side. The kit's procedure files are left as-is: they are the record
of what that trial actually ran, and rewriting them to match the
generalized protocol would falsify that record."
```

## Out of scope

Named here so an executor does not drift into them:

- Any edit under `skills/` or `docs/`. The battery is designed, not implemented; implementation is gated on validation per section 5.
- Running the section 6 pilot, or any regeneration of the 2026-07-23 arms.
- Rewriting the 2026-07 kit's `brief-procedure.md` or `rubric.md` to match the generalized protocol.
- Extending doodle-lint or CI coverage to `trials/`. Investigated and rejected on evidence, not deferred: doodle-lint is a skill linter and fails any file without SKILL.md frontmatter (`parse/missing-frontmatter`, `desc/too-short`, exit 2). `trials/METHODOLOGY.md` has no frontmatter by design, so linting it would fail CI on two inapplicable errors. Do not revisit this without a different tool.
