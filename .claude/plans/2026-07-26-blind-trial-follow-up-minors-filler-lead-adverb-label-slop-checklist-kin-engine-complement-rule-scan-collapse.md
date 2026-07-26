---
type: plan
title: 'Blind-trial follow-up minors: filler lead, adverb label, slop checklist, Kin
  engine, complement rule, scan collapse'
description: 'Eight scoped prose fixes across four instruction files: the seven follow-up
  minors from the blind-trial adoption reviews, plus a field-raised defect where the
  Archetype Distribution section directs the agent to choose labels for variety rather
  than for fit. Covers two writing-style.md corrections, a slop-phrases.md coverage
  gap, a framework.md missing example, the no-complement principle, the Kin friction
  engine, and a rewrite of the Archetype Distribution section.'
tags:
- human-ready
date: 2026-07-26
timestamp: 2026-07-26T16:56Z
resources:
- '[[2026-07-26-verified-site-inventory-for-the-blind-trial-follow-up-minors]]'
---

# Blind-trial follow-up minors: filler lead, adverb label, slop checklist, Kin engine, complement rule, scan collapse

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> core-workflow:subagent-driven-development (recommended) or
> core-workflow:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires
> this plan artifact's approval flip.

## Goal

Close the seven follow-up minors raised by the blind-trial adoption reviews, each verified against current file text in the [site inventory](../research/2026-07-26-verified-site-inventory-for-the-blind-trial-follow-up-minors.md), plus one further defect raised from field use: the Archetype Distribution section tells the agent to pick labels for variety rather than for fit.

**Architecture:** Nine scoped edits across four instruction files, grouped into five tasks by file and by whether a reviewer could accept one while rejecting its neighbour. Two corrections and one addition in `skills/writing-style.md` and `docs/slop-phrases.md`, one worked example in `framework.md`, and the rest in `relationships.md` — the no-complement principle, the Kin friction engine, and a rewrite of the Archetype Distribution section that relocates variety from the labeling step to the design step, collapses the rule's three statements into one, and adds the fit check that makes the distribution scan non-gameable.

**Tech stack:** Plain markdown instruction prose. No frontmatter in any file touched.

## Global Constraints

- **These four files use one line per paragraph — no hard wrapping.** This is the opposite of `trials/METHODOLOGY.md`. Never reflow a paragraph into wrapped lines; a replaced paragraph stays one long line.
- Surgical edits only. Touch the exact text each step names; leave every other line byte-identical.
- Shipped skill prose is model-neutral: no AI product or vendor names anywhere in `skills/` or `docs/`.
- Follows the plugin's writing doctrine: plain and concrete, no filler (`skills/writing-style.md`, checklist in `docs/slop-phrases.md`). Prose added by this plan is subject to the same rules it is editing.
- None of these files carry YAML frontmatter. Do not add any.
- `doodle` discovers `SKILL.md` files only, so none of the files edited here are linted by it. Do not run `doodle` against an individual non-SKILL.md file — it fails on missing frontmatter by design.
- The `card` vocabulary at `relationships.md:14` refers to the Export-phase artifact per `CONTEXT.md:29`; new prose in that file matches its neighbours' usage rather than introducing a synonym.

## Tasks

### Task 1: Two corrections in writing-style.md

**Files:**
- Modify: `skills/writing-style.md:72` and `skills/writing-style.md:82`

**Interfaces:**
- Produces: the corrected Cut filler lead and the renamed adverb group. Task 2 adds checklist entries for a neighbouring section but does not depend on this text.

- [ ] **Step 1: Replace the Cut filler lead sentence**

The current lead restates *No significance inflation* twelve lines above it, and describes only two of the four groups it introduces. Replace the whole line at `skills/writing-style.md:72`:

Find:

```
Delete phrases that announce importance instead of carrying it, and strip adverbs that pad a claim instead of sharpening it.
```

Replace with:

```
Delete words that take up room without doing work: openers that delay the sentence, emphasis standing in for evidence, fashionable verbs where a plain one exists, and adverbs that pad a claim instead of sharpening it.
```

Each clause now maps to one of the four groups listed below it, in the same order.

- [ ] **Step 2: Rename the mislabelled adverb group**

`actually`, `honestly` and `genuinely` are stance markers, not adverbs of degree; the group mixes two categories, in a file that demands the simplest precise word. Replace the line at `skills/writing-style.md:82`:

Find:

```
- Adverbs of degree: "really," "just," "genuinely," "truly," "deeply," "actually," "simply," "honestly."
```

Replace with:

```
- Padding adverbs: "really," "just," "genuinely," "truly," "deeply," "actually," "simply," "honestly."
```

The word list is unchanged — only the group name.

- [ ] **Step 3: Verify both edits landed and nothing else moved**

Run:

```bash
grep -n 'Delete words that take up room\|Padding adverbs' skills/writing-style.md && grep -c 'Adverbs of degree\|announce importance instead of carrying' skills/writing-style.md; git diff --stat skills/writing-style.md
```

Expected: the first grep prints two lines (72 and 82). The second grep prints `0` — both old strings gone. The diff stat shows `2 insertions(+), 2 deletions(-)`, proving no other line moved.

- [ ] **Step 4: Confirm the four groups still read in order**

Run: `sed -n '72p;79,82p' skills/writing-style.md`
Expected: the new lead, then the four group bullets — throat-clearers, emphasis crutches, jargon standing in for a plain verb, padding adverbs — in that order, so the lead's four clauses match the list order.

- [ ] **Step 5: Commit**

```bash
git add skills/writing-style.md
git commit -m "Correct the Cut filler lead and the adverb group name

The lead restated No significance inflation directly above it and
described only two of the four groups it introduces; it now names all
four in list order. The adverb group called just/actually/honestly
adverbs of degree, which they are not - they are stance markers. Renamed
to Padding adverbs, which is accurate and drops a grammatical claim the
file does not need. Word list unchanged."
```

### Task 2: Add the vague-declarative checklist group

**Files:**
- Modify: `docs/slop-phrases.md` (insert a section after `Significance inflation`, which ends at line 70)

**Interfaces:**
- Consumes: nothing. The gap is against `writing-style.md:68`, which already exists.

- [ ] **Step 1: Read the section boundary you are inserting between**

Run: `sed -n '68,76p' docs/slop-phrases.md`
Expected: the tail of `Significance inflation` (its last bullet and its `Fix:` line), then a `---` separator, then the `## Copula avoidance` heading. Insert between the separator and that heading.

- [ ] **Step 2: Insert the new section**

`writing-style.md:68` bans vague declaratives in sentence form, but this checklist lists only single words and phrases, so those sentence forms have no entry. Insert this section immediately before `## Copula avoidance`, matching the file's existing shape — heading, one-line description, bullet list, `Fix:` line:

```markdown
## Vague declaratives

The sentence form of significance inflation. Announces that something matters without saying what it is.

- "the stakes are high"
- "the reasons are structural"
- "the implications are significant"
- "the dynamic is complex"
- "there is history there"

Fix: cut the sentence and state the fact it was standing in for.

---
```

The first three come from `writing-style.md:68`. The last two are the same construction in character-note register, which is what this checklist is scanned against.

**Exact resulting layout.** The file separates sections with a blank line, `---`, then another blank line. After the insert, the region must read:

```
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
```

Note the blank line after the new `---` and before `## Copula avoidance` — without it the separator butts against the heading and breaks the file's pattern.

- [ ] **Step 3: Verify the section landed in the right place**

Run:

```bash
grep -n '^## ' docs/slop-phrases.md
```

Expected: seven headings, with `## Vague declaratives` sitting between `## Significance inflation` and `## Copula avoidance`.

- [ ] **Step 4: Verify all three doctrine phrases are present**

Run:

```bash
python -c "import io; t=io.open('docs/slop-phrases.md',encoding='utf-8').read(); m=[p for p in ['the stakes are high','the reasons are structural','the implications are significant'] if p not in t]; print('MISSING:',m) if m else print('ALL DOCTRINE PHRASES PRESENT')"
```

Expected: `ALL DOCTRINE PHRASES PRESENT`.

- [ ] **Step 5: Commit**

```bash
git add docs/slop-phrases.md
git commit -m "Add a vague-declarative group to the slop checklist

writing-style.md:68 bans vague declaratives in sentence form, but this
checklist carried only single words and phrases, so a reviewer scanning
with it would miss every one of them. Two entries beyond the doctrine's
three are the same construction in character-note register, which is the
material this file is actually scanned against."
```

### Task 3: Add the missing non-competence example

**Files:**
- Modify: `skills/worldbuilder-character/framework.md` (insert after line 84)

**Interfaces:**
- Consumes: the trait rule at `skills/writing-style.md:143`, which `framework.md:81` already points to. That rule is not edited by this plan.

- [ ] **Step 1: Read the insertion point**

Run: `sed -n '81,86p' skills/worldbuilder-character/framework.md`
Expected: the trait-ban paragraph at 81, a blank line, the `Wrong:`/`Right:` pair at 83-84 (a competence case — "highly intelligent and analytical"), then the `### Knowledge boundaries` heading. Insert between the pair and that heading.

- [ ] **Step 2: Insert the non-competence pair**

The rule has two branches — competence and non-competence — but this example-driven file works only the competence one. Insert after line 84, before the blank line preceding `### Knowledge boundaries`:

```markdown

The rule's other branch covers traits that are not competences: name the behavior that makes people reach for the word, and what it costs.

- Wrong: "He is arrogant and dominant."
- Right: "He finishes other people's sentences wrong, then corrects them on the correction. His team stopped bringing him problems early, so he hears about them once they are expensive."
```

- [ ] **Step 3: Verify placement and that the competence pair is intact**

Run:

```bash
sed -n '81,92p' skills/worldbuilder-character/framework.md && git diff --stat skills/worldbuilder-character/framework.md
```

Expected: the original competence pair still at 83-84 unchanged, the new paragraph and pair following it, then `### Knowledge boundaries`. The diff stat shows insertions only — `0 deletions(-)`.

- [ ] **Step 4: Verify the new example carries a cost clause**

Run:

```bash
python -c "import io; t=io.open('skills/worldbuilder-character/framework.md',encoding='utf-8').read(); print('NON-COMPETENCE PAIR PRESENT' if 'He is arrogant and dominant' in t and 'once they are expensive' in t else 'INCOMPLETE')"
```

Expected: `NON-COMPETENCE PAIR PRESENT`. The rule demands both the behavior and its cost; the second string is the cost clause.

- [ ] **Step 5: Commit**

```bash
git add skills/worldbuilder-character/framework.md
git commit -m "Work the trait rule's non-competence branch

The rule at writing-style.md:143 has two branches and this file, which
carries the character-specific worked cases, exercised only the
competence one - in a file with a four-row table and two other
Wrong/Right pairs. The new pair shows the behavior that earns the word
and the cost it produces, which is what the branch asks for."
```

### Task 4: The no-complement principle and the Kin friction engine

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md:14` (insert a paragraph after it) and `skills/worldbuilder-character/relationships.md:25`

**Interfaces:**
- Produces: the no-complement principle, which Task 5 does not depend on. Both tasks edit this file; run Task 4 first so Task 5's line numbers are checked against the updated file.

- [ ] **Step 1: Insert the no-complement principle**

`relationships.md:14` guarantees that relationships need not be reciprocated, but says nothing about the *archetype* on the other side. Left unstated, the model assumes every relationship is mirrored by its complement, which collapses the space of relationships worth writing. Insert this as a new paragraph immediately after line 14, before the `**Perspective-focus and cross-character capture apply simultaneously.**` paragraph:

```markdown

**No relationship requires a complement.** A character who sees someone as an Authority does not oblige that person's card to carry a Charge. The complement may even be true and still not belong: a teacher who shaped a student profoundly may see one student among many, formative to no particular degree. The story pressure runs from the student's end, and that is enough to write. What the card fixes is the starting state — the other character may grow into the relationship later, and that is a story event rather than a card entry.
```

Remember the global constraint: this is one line, not wrapped.

- [ ] **Step 2: Give Kin its resist-protection engine**

Charge produces "conflict when the charge resists protection" and explicitly excludes family, so the one archetype covering family protection has no friction engine and cannot borrow one. Replace the Kin line at `skills/worldbuilder-character/relationships.md:25`:

Find:

```
**1. Kin** — Family by blood, adoption, or found-family bond of equivalent depth. Behavioral signature: unconditional stakes without unconditional agreement. Cannot walk away without identity cost. Activates protective instincts, guilt, and loyalty that overrides rational calculation. Every character needs family context — if family is absent or dead, Ghost may substitute.
```

Replace with:

```
**1. Kin** — Family by blood, adoption, or found-family bond of equivalent depth. Behavioral signature: unconditional stakes without unconditional agreement. Cannot walk away without identity cost. Activates protective instincts, guilt, and loyalty that overrides rational calculation. Protection here is refused as often as it is accepted: family resists being handled by family, and the refusal costs more than a stranger's would. Every character needs family context — if family is absent or dead, Ghost may substitute.
```

One sentence added mid-line; everything else identical.

- [ ] **Step 3: Verify both edits and that nothing else moved**

Run:

```bash
grep -n 'No relationship requires a complement\|refused as often as it is accepted' skills/worldbuilder-character/relationships.md && git diff --stat skills/worldbuilder-character/relationships.md
```

Expected: two matching lines printed. The diff stat shows `3 insertions(+), 1 deletion(-)` — the new paragraph plus its blank line, and the Kin line replaced.

- [ ] **Step 4: Verify no line was wrapped**

Run:

```bash
python -c "import io; ls=io.open('skills/worldbuilder-character/relationships.md',encoding='utf-8').read().split(chr(10)); print('SHORT PARAGRAPH LINES:',[i+1 for i,l in enumerate(ls) if l.startswith('**No relationship') and len(l)<200] or 'none')"
```

Expected: `SHORT PARAGRAPH LINES: none` — the new paragraph is a single long line, matching the file. A hit here means the paragraph was wrapped and must be rejoined.

- [ ] **Step 5: Commit**

```bash
git add skills/worldbuilder-character/relationships.md
git commit -m "State the no-complement rule and give Kin a friction engine

Asymmetry was already guaranteed, but nothing said the other character
need not carry the complementary archetype. Unstated, the model assumes
every Authority implies a Charge, which collapses the relationship space;
the teacher who sees one student among many is the ordinary case, not the
exception. Kin meanwhile absorbed all family protection while Charge kept
the resist-protection engine and explicitly excluded kin, so family
protection had no friction to generate scenes from."
```

### Task 5: Rewrite the Archetype Distribution section

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md` — the whole `## Archetype Distribution` section (the goal paragraph, the ideal-is-no-repeats paragraph, and the self-check paragraph), plus the `Archetype distribution scan` item under `## Coverage Validation`

**Interfaces:**
- Consumes: Task 4's edits shift this file's line numbers by roughly two. Locate every target by its text, not by the line numbers quoted here.

Two problems in one section. First, the goal paragraph tells the agent to choose archetypes for distribution rather than for fit — which makes relabeling the cheapest way to satisfy the variety check, and produces entries whose archetype does not describe the relationship. Second, the same distribution rule is stated three times: in the ideal-is-no-repeats paragraph with its arithmetic, again in the self-check, and again in Coverage Validation, all firing at the same moment.

The decision: variety moves from the labeling step to the design step, all standing instruction gathers in the ideal-is-no-repeats paragraph, the self-check is deleted outright, and the enforceable cap lives in Coverage Validation.

- [ ] **Step 1: Relocate variety from labeling to design**

Replace the goal paragraph. Find:

```
**The goal is variety, not accurate labeling.** When assigning archetypes, the question is not "which archetype fits this person best?" but "does the full set of relationships cover a wide range of behavioral modes?" A character whose relationships are all Community Thread, Kin, and Confidant will produce narrow, repetitive LLM output regardless of how accurately each label fits.
```

Replace with:

```
**Variety is a property of the relationships, not of the labels.** A character whose relationships are all Community Thread, Kin, and Confidant will produce narrow, repetitive LLM output however well each label fits. The fix is never to relabel. An archetype that does not describe the relationship makes the entry wrong, and the behavior generated from it wrong with it. A narrow spread means the relationships themselves are too alike: go back and change what one of them is — who the person is to this character, and what the character wants from them. Label each relationship as what it actually is, and read a monotonous distribution as the symptom that sends you back to the relationship.
```

This is the substantive change in the task. The old text asked "does the set cover a wide range?" at the moment of assigning a label, which authorizes picking a label the relationship does not earn. The distribution scan then measures labels rather than relationships, and passes.

- [ ] **Step 2: Fix the relabeling nudge in the ideal-is-no-repeats paragraph**

This paragraph is now the section's single standing guide, so its own repeat-handling advice must point at the relationship too. Find:

```
Treat every repeat as a signal to reconsider before accepting it: is the framing too loose, or is there a more specific archetype that would better serve behavioral variety?
```

Replace with:

```
Treat every repeat as a signal to reconsider the relationship before accepting it: is the framing too loose, or is this relationship doing the same work as another one in the set?
```

Everything else in that paragraph — the arithmetic, the second-tag rule, and the `no archetype may appear more than twice` cap — stays exactly as it is.

- [ ] **Step 3: Delete the self-check paragraph**

Every clause in it already exists elsewhere: the count and the repeat signal in the ideal-is-no-repeats paragraph, the Community Thread limit in the paragraph directly above it, and the cap in Coverage Validation. Delete this line and the blank line that follows it:

```
**Self-check before finalizing:** Scan the full relationship list and count how many times each archetype appears, counting every tag on every entry. Every repeat is worth revisiting. An archetype appearing three or more times is wrong and must be fixed. If Community Thread appears more than once, reconsider the weaker entry. The ideal is that no archetype appears twice anywhere in the set, whether or not an entry carries more than one tag.
```

Nothing is carried over from it. After the deletion the section runs: goal paragraph, ideal-is-no-repeats paragraph, Community Thread paragraph, then the `---` separator.

- [ ] **Step 4: Update the Coverage Validation item**

Find:

```
2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, counting every tag on every entry. The ideal is no repeats: flag every repeat for reconsideration, and treat any archetype used three or more times as wrong and fix it. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.
```

Replace with:

```
2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, counting every tag on every entry. The ideal is no repeats: flag every repeat and reconsider the relationship behind it, not the label on it. No archetype may appear more than twice — fix any that does. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.
```

The cap is phrased as `more than twice` to match the paragraph that derives it. The threshold is unchanged in effect: three or more occurrences remain a defect.

- [ ] **Step 5: Add the archetype fit check to Coverage Validation**

Rewriting the goal paragraph tells the author to label accurately, but nothing currently checks that they did — the distribution scan counts labels and cannot tell a fitting one from a filler. Add a fourth numbered item after the `Cast web check` item and before the Community Thread blockquote:

```markdown

4. **Archetype fit check:** Read each entry's archetype against the relationship it tags: does that archetype's behavioral signature describe what this relationship actually does? A label that does not fit is a defect however well it serves the distribution — fix it by changing the archetype to the one that fits, or by changing the relationship so the archetype is earned. Where an anchor type from the targets above has no relationship that genuinely carries it, flag that gap rather than tagging a near-miss to fill the slot.
```

This is what makes the distribution scan non-gameable: distribution and fit are now both checked, and fit wins. The final clause covers the anchor types listed under `**Major characters:**` and `**Supporting characters:**` — a missing anchor is reported, not papered over.

- [ ] **Step 6: Verify the section now has three paragraphs and no self-check**

Run:

```bash
python -c "import io; t=io.open('skills/worldbuilder-character/relationships.md',encoding='utf-8').read(); s=t.split('## Archetype Distribution')[1].split('---')[0]; paras=[p for p in s.split(chr(10)) if p.strip()]; print('PARAGRAPHS:',len(paras)); print('SELF-CHECK PRESENT' if 'Self-check before finalizing' in t else 'SELF-CHECK REMOVED')"
```

Expected: `PARAGRAPHS: 3` then `SELF-CHECK REMOVED`.

- [ ] **Step 7: Verify no instruction anywhere still sends the agent to the label**

Run:

```bash
grep -n 'goal is variety\|three or more\|more specific archetype that would better serve' skills/worldbuilder-character/relationships.md; echo "exit:$?"
```

Expected: no matching lines and `exit:1`. Each of those three strings is a place that either stated the old goal or nudged toward relabeling.

- [ ] **Step 8: Verify the cap survives in exactly two places and the fit check landed**

Run:

```bash
grep -c 'more than twice' skills/worldbuilder-character/relationships.md && grep -n '^4\. \*\*Archetype fit check' skills/worldbuilder-character/relationships.md
```

Expected: `2` — the ideal-is-no-repeats paragraph and the Coverage Validation item — then one line showing the new item 4.

- [ ] **Step 9: Verify Coverage Validation reads 1-4 in order**

Run: `grep -n '^[0-9]\. \*\*' skills/worldbuilder-character/relationships.md`
Expected: four lines numbered 1 through 4 — behavioral coverage check, archetype distribution scan, cast web check, archetype fit check.

- [ ] **Step 10: Run the test suite to confirm no collateral damage**

Run: `python -m pytest tests -q`
Expected: `13 passed`.

- [ ] **Step 11: Commit**

```bash
git add skills/worldbuilder-character/relationships.md
git commit -m "Move relationship variety from the label to the relationship

The section opened by telling the agent the goal is variety rather than
accurate labeling, and that the question is not which archetype fits
best. Read literally - which is how it gets read - that authorizes
relabeling a relationship to fill a gap in the spread, so the
distribution scan ends up measuring labels instead of relationships and
passes on a cast that has not changed. Observed in field use.

Variety is now stated as a property of the relationships themselves, and
a narrow spread is named as the symptom that sends the author back to
what the relationship is. The repeat-handling advice points the same way.

A fit check joins Coverage Validation, because telling the author to
label accurately means nothing while the only check counts labels. Fit
outranks distribution, and an anchor type with no relationship carrying
it is flagged rather than filled with a near-miss.

The distribution rule was also stated three times at the same moment.
The self-check paragraph is deleted with nothing carried over - every
clause in it already existed in the paragraph above, the Community
Thread paragraph, or Coverage Validation. Standing guidance now lives in
the ideal-is-no-repeats paragraph and the enforceable cap in Coverage
Validation, phrased as 'more than twice' to match."
```

## Out of scope

Named here so an executor does not drift into them:

- The arithmetic inside the `**The ideal is no repeats.**` paragraph — the 12-archetypes-against-8-relationships count, the second-tag rule, and the cap sentence. Task 5 Step 2 changes one sentence in that paragraph and nothing else; it remains the single place explaining *why* the cap is two.
- The archetype definitions themselves, apart from Kin in Task 4. Task 5 changes how archetypes are chosen, not what any of them mean.
- The anchor-type targets under `**Major characters:**` and `**Supporting characters:**`. They stay as written; Task 5's fit check is what catches an anchor filled by a near-miss. Relocating those targets into the user Q&A that precedes blueprint generation is the better fix and is queued separately — this plan does not anticipate it.
- Splitting validation into a separate grader agent. The checks this plan adds are written as instructions to whoever runs them; who runs them is a separate design question, queued.
- Adding the Cut filler groups (throat-clearers, emphasis crutches, jargon verbs, padding adverbs) to `docs/slop-phrases.md`. The verified gap is vague declaratives only; whether the checklist should also mirror the filler groups is a separate question.
- Any change to the trait rule itself at `skills/writing-style.md:143`. Task 3 adds a worked example for its existing second branch; the rule text stands.
- Rewriting `relationships.md:16` (perspective-focus and cross-character capture), which sits adjacent to Task 4's insertion point and is not part of these findings.
