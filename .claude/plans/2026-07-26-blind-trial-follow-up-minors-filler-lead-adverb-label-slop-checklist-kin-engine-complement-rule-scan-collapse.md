---
type: plan
title: 'Blind-trial follow-up minors: filler lead, adverb label, slop checklist, Kin
  engine, complement rule, scan collapse'
description: 'Seven scoped prose fixes across four instruction files, closing the
  follow-up minors raised by the blind-trial adoption reviews: two writing-style.md
  corrections, a slop-phrases.md coverage gap, a framework.md missing example, and
  three relationships.md changes including the no-complement principle and the archetype-scan
  duplication collapse.'
tags:
- human-ready
date: 2026-07-26
timestamp: 2026-07-26T16:39Z
resources: []
---

# Blind-trial follow-up minors: filler lead, adverb label, slop checklist, Kin engine, complement rule, scan collapse

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> core-workflow:subagent-driven-development (recommended) or
> core-workflow:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires
> this plan artifact's approval flip.

## Goal

Close the seven follow-up minors raised by the blind-trial adoption reviews, each verified against current file text in the [site inventory](../research/2026-07-26-verified-site-inventory-for-the-blind-trial-follow-up-minors.md).

**Architecture:** Seven scoped edits across four instruction files, grouped into five tasks by file and by whether a reviewer could accept one while rejecting its neighbour. Two corrections and one addition in `skills/writing-style.md` and `docs/slop-phrases.md`, one worked example in `framework.md`, and three changes in `relationships.md` — the no-complement principle, the Kin friction engine, and the archetype-scan duplication collapse. No behaviour changes, no new sections beyond one checklist group.

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

### Task 5: Collapse the archetype-scan duplication

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md` — the self-check paragraph (`**Self-check before finalizing:**`) and the `Archetype distribution scan` item under `## Coverage Validation`

**Interfaces:**
- Consumes: Task 4's edits shift this file's line numbers by roughly two. Locate both targets by their text, not by the line numbers quoted here.

The same rule is currently stated three times: the paragraph beginning `**The ideal is no repeats.**` carries the arithmetic and the hard cap, the self-check restates it, and Coverage Validation restates it again. The decision is to keep the hard check in Coverage Validation, soften the self-check to a preference, and leave the `**The ideal is no repeats.**` paragraph untouched.

- [ ] **Step 1: Soften the self-check**

Find this line (it begins `**Self-check before finalizing:**`):

```
**Self-check before finalizing:** Scan the full relationship list and count how many times each archetype appears, counting every tag on every entry. Every repeat is worth revisiting. An archetype appearing three or more times is wrong and must be fixed. If Community Thread appears more than once, reconsider the weaker entry. The ideal is that no archetype appears twice anywhere in the set, whether or not an entry carries more than one tag.
```

Replace with:

```
**Self-check before finalizing:** Scan the full relationship list and count each archetype, counting every tag on every entry. Favor unique archetypes over repeats: a repeat is a signal to look for a more specific archetype, not a failure on its own. The hard cap is checked at Coverage Validation.
```

The numeric threshold and the Community Thread clause both leave this paragraph — the threshold is enforced at Coverage Validation, and Community Thread's single-use guidance already has its own paragraph directly above.

- [ ] **Step 2: Restate the cap in Coverage Validation**

Find the `Archetype distribution scan` item:

```
2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, counting every tag on every entry. The ideal is no repeats: flag every repeat for reconsideration, and treat any archetype used three or more times as wrong and fix it. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.
```

Replace with:

```
2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, counting every tag on every entry. The ideal is no repeats: flag every repeat for reconsideration. No archetype may appear more than twice — fix any that does. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.
```

This phrases the cap as "more than twice", matching the wording already used in the `**The ideal is no repeats.**` paragraph. The threshold is unchanged in effect: three or more occurrences remain a defect.

- [ ] **Step 3: Verify the hard threshold now appears in exactly one validation site**

Run:

```bash
grep -n 'three or more\|more than twice' skills/worldbuilder-character/relationships.md
```

Expected: exactly two lines — the `**The ideal is no repeats.**` paragraph and the Coverage Validation item, both saying `more than twice`. No line says `three or more`.

- [ ] **Step 4: Verify the self-check no longer carries a threshold or a Community Thread clause**

Run:

```bash
python -c "import io; l=[x for x in io.open('skills/worldbuilder-character/relationships.md',encoding='utf-8') if x.startswith('**Self-check before finalizing:**')][0]; bad=[s for s in ['three or more','more than twice','Community Thread'] if s in l]; print('LEFTOVER:',bad) if bad else print('SELF-CHECK IS SOFT GUIDANCE ONLY')"
```

Expected: `SELF-CHECK IS SOFT GUIDANCE ONLY`.

- [ ] **Step 5: Run the test suite to confirm no collateral damage**

Run: `python -m pytest tests -q`
Expected: `13 passed`.

- [ ] **Step 6: Commit**

```bash
git add skills/worldbuilder-character/relationships.md
git commit -m "Collapse the triplicated archetype-distribution rule

The cap was stated three times: in the ideal-is-no-repeats paragraph
with its arithmetic, again in the self-check, and again in Coverage
Validation, all firing at the same moment. The self-check is now a
preference - favor unique archetypes, a repeat is a signal not a failure
- and the enforceable cap lives in Coverage Validation alone, phrased as
'more than twice' to match the paragraph that derives it. Community
Thread's single-use guidance leaves the self-check because the paragraph
directly above it already covers that."
```

## Out of scope

Named here so an executor does not drift into them:

- The `**The ideal is no repeats.**` paragraph. It carries the arithmetic the cap is derived from and is deliberately left as the single place that explains *why* the cap is two.
- Adding the Cut filler groups (throat-clearers, emphasis crutches, jargon verbs, padding adverbs) to `docs/slop-phrases.md`. The verified gap is vague declaratives only; whether the checklist should also mirror the filler groups is a separate question.
- Any change to the trait rule itself at `skills/writing-style.md:143`. Task 3 adds a worked example for its existing second branch; the rule text stands.
- Rewriting `relationships.md:16` (perspective-focus and cross-character capture), which sits adjacent to Task 4's insertion point and is not part of these findings.
