---
type: plan
title: 'Blind-Trial Adoption: Cut Filler, Additive Principles, Relationship Labels'
description: Implementation plan folding the stopslop Cut Filler rules and the five
  additive doctrine principles into shipped skills, and fixing the relationship archetype
  label contradiction plus the Authority/Charge direction split.
tags:
- complete
date: 2026-07-25
timestamp: 2026-07-25T17:11Z
resources: []
---

# Blind-Trial Adoption: Cut Filler, Additive Principles, Relationship Labels

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> core-workflow:subagent-driven-development (recommended) or
> core-workflow:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires
> the plan artifact's approval flip.

**Goal:** Fold the stopslop Cut Filler rules and the five additive
doctrine principles into shipped skill content, and stop relationship
archetypes from being rendered as visible labels while splitting
Authority and Charge by direction.

**Architecture:** Every task is a prose edit to shipped skill markdown.
Two threads share `skills/worldbuilder-character/SKILL.md`, so they are
sequenced in one plan rather than split: the relationship-archetype
fixes first (Tasks 2 and 6), then the doctrine adoption (Tasks 3–5,
acting on a single-cell human preference).

**Execution order: 2, 6, 3, 4, 5.** Task 1 is void — it was implemented
on a wrong premise and reverted; see its entry for the reason. Task 6
was added after Task 1's review and runs directly after Task 2 because
both edit `relationships.md`.

**Tech Stack:** Markdown skill content, Python 3 build script
(`scripts/build-okf.py`), pytest, doodle-lint 1.0.0.

**Research dossier:**
[2026-07-25-blind-trial-adoption-implementation-research.md](../research/2026-07-25-blind-trial-adoption-implementation-research.md).
Trial outcome:
[2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md](../research/2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md).

## Global Constraints

- Never name a specific AI model in shipped content — "for future
  agents", never a product name.
- `defaults/okf.json` is generated. Edit `defaults/okf.base.json` and
  `defaults/templates/*.md`, then run `python scripts/build-okf.py`.
  Never hand-edit `defaults/okf.json`.
- All prose written into `skills/` obeys `skills/writing-style.md` and
  the checklist in `docs/slop-phrases.md`. That includes prose this plan
  adds: no em-dashes where the shipped rule forbids them, no
  significance inflation, plain vocabulary.
- `doodle --strict skills` must pass. Any new project word must be added
  to the allowlist in `.doodle.toml`, not spelled around.
- `python -m pytest tests -q` must pass (13 tests).
- Do not edit anything under `trials/2026-07-writing-doctrine/`. The kit
  is the trial record and must stay reproducible.

**Verification note:** this repo has no test suite for skill prose, and
markdown doctrine cannot be driven by TDD. Every task below therefore
verifies with grep assertions that name exact commands and expected
output, plus the repo's real lint and test gates. Do not substitute
"confirm the text reads correctly" for these commands.

---

## Tasks

### Task 1: Stop rendering relationship archetypes as labels — VOID

**This task was implemented (6d09054) and reverted (c9c4f8c). Do not
execute it. It is retained for the record.**

The premise was wrong. `relationships.md:23` says archetypes do not
appear "in the final card", and `CONTEXT.md:29` reserves "card" for the
Export-phase artifact. Line 23 was always describing the exported card,
not the character blueprint. Archetypes are labelled in the blueprint by
design, so the format instruction, the worked example, the SKILL.md
checklist and the OKF template were all correct as written and there was
no contradiction to resolve.

The blind trial's relationship-label finding therefore stands on its
original footing: labels do ship in the blueprint, so their accuracy
matters, and the real defect is the bidirectional Authority definition
that Task 2 fixes.

Task 6 covers the archetype-variety wording that this task's review
raised.

The original task text follows, unchanged, for the record only.

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md:76`
- Modify: `skills/worldbuilder-character/relationships.md:79-81`
- Modify: `skills/worldbuilder-character/SKILL.md` (Relationships block
  of the Self-Check list)
- Modify: `defaults/templates/character.md:37`
- Regenerate: `defaults/okf.json` (via build script, never by hand)

**Interfaces:**
- Produces: the relationship bullet format used by Task 2's coverage
  wording and by every downstream character note — `- **Name:**`
  followed by behavioral prose, with no archetype token.

- [ ] **Step 1: Assert the current state, so the change is provable**

Run: `rg -n 'Archetype\(s\)' skills defaults`

Expected: three matches — `skills/worldbuilder-character/relationships.md:76`,
`skills/worldbuilder-character/SKILL.md` (Relationships checklist line),
`defaults/templates/character.md:37`.

- [ ] **Step 2: Change the format instruction in `relationships.md`**

Replace the Format line (currently at `relationships.md:76`):

```markdown
**Format:** Bullet list. One entry per relationship. Bold `**Name — Archetype(s):**` prefix inline on the bullet, followed by behavioral description as prose sentence(s).
```

with:

```markdown
**Format:** Bullet list. One entry per relationship. Bold `**Name:**` prefix inline on the bullet, followed by behavioral description as prose sentence(s). The archetype is not written into the entry — it is a planning tool for checking variety, and naming it in the note gives the LLM a label to repeat.
```

- [ ] **Step 3: Change the worked example in `relationships.md`**

Replace the example bullet (currently at `relationships.md:79-81`):

```markdown
- **Mira — Kin:** When Mira dismisses her ideas in front of others, she doesn't argue — she brings the idea back later, one-on-one, where Mira has room to change her mind without losing face.
```

with:

```markdown
- **Mira:** When Mira dismisses her ideas in front of others, she doesn't argue. She brings the idea back later, one-on-one, where Mira has room to change her mind without losing face.
```

Note the em-dash is also removed, per `skills/writing-style.md:91`
(*No em-dashes*), which the original example violated.

- [ ] **Step 4: Change the checklist line in `SKILL.md`**

In the **Relationships** block of `## Self-Check Before Marking
Complete`, replace:

```markdown
- [ ] Each entry in bullet format with `**Name — Archetype(s):**` prefix
```

with:

```markdown
- [ ] Each entry in bullet format with `**Name:**` prefix; no archetype named in the entry
```

- [ ] **Step 5: Change the OKF template**

In `defaults/templates/character.md`, replace line 37:

```markdown
_Named relationship dynamics. One bullet per relationship: **Name — Archetype(s):** [behavioral description]_
```

with:

```markdown
_Named relationship dynamics. One bullet per relationship: **Name:** [behavioral description]_
```

- [ ] **Step 6: Regenerate the preset**

Run: `python scripts/build-okf.py`

Expected: exits 0. `defaults/okf.json` is modified.

- [ ] **Step 7: Verify no rendered-label instruction survives**

Run: `rg -n 'Archetype\(s\)' skills defaults`

Expected: no matches, exit code 1.

Run: `rg -n 'Mira — Kin' skills`

Expected: no matches, exit code 1.

- [ ] **Step 8: Run the repo gates**

Run: `python -m pytest tests -q`

Expected: all 13 tests pass. If `tests/test_generate_templates.py`
fails, it asserts on the old template text — read the failing assertion
and update the fixture to the new format, then re-run.

Run: `doodle --strict skills`

Expected: exits 0, no findings.

- [ ] **Step 9: Commit**

```bash
git add skills/worldbuilder-character/relationships.md skills/worldbuilder-character/SKILL.md defaults/templates/character.md defaults/okf.json
git commit -m "Stop rendering relationship archetypes as visible labels

relationships.md:23 already stated archetypes are a blueprinting tool
that does not appear in the final note, but the format instruction, the
worked example, the SKILL.md checklist and the OKF character template
all mandated a '**Name — Archetype(s):**' prefix. The operative
instructions won: the 2026-07-23 blind trial found all six arms
rendering labels, and misapplying them.

Removing the archetype from the rendered format resolves the
contradiction in favour of the line-23 intent. Coverage and variety
checks still use archetypes; they now stay in the planning step.

The worked example also dropped an em-dash that violated
writing-style.md:91."
```

---

### Task 2: Split Authority and Charge by direction

`Authority` currently covers both directions, so the label carries no
direction, collides with `Charge` on the downward side, and blunts the
variety count that the repetition limit depends on.

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md:27` (Authority)
- Modify: `skills/worldbuilder-character/relationships.md:47` (Charge)
- Modify: `skills/worldbuilder-character/relationships.md:53-55`
  (Coverage Requirements)
- Modify: `skills/worldbuilder-character/SKILL.md` (Relationships block
  of the Self-Check list)

**Interfaces:**
- Consumes: the `- **Name:**` entry format established in Task 1.
- Produces: `Authority` = upward only; `Charge` = downward, including
  formal subordinates. Both remain valid power-asymmetry anchors.

- [ ] **Step 1: Narrow Authority to upward only**

Replace `relationships.md:27`:

```markdown
**2. Authority** — A structured power relationship: mentor, employer, elder, or superior upward; apprentice, subordinate, or ward downward. Behavioral signature: asymmetric obligation. Upward: deference, resentment, desire to prove oneself. Downward: responsibility, protectiveness, impatience, fear of failing them.
```

with:

```markdown
**2. Authority** — Someone who holds structured power over the character: a mentor, employer, elder, or superior. Behavioral signature: deference, resentment, and the desire to prove oneself. The label always points upward. For the downward direction, use Charge.
```

- [ ] **Step 2: Widen Charge to cover the downward direction**

Replace `relationships.md:47`:

```markdown
**12. Charge** — Someone the character feels self-appointed responsibility for who is not their kin and not a formal subordinate. Behavioral signature: worry and preemptive action. Produces unwanted intervention, sacrifice, and conflict when the charge resists protection.
```

with:

```markdown
**12. Charge** — Someone the character holds responsibility for, whether the role is formal (an apprentice, subordinate, or ward) or self-appointed. Behavioral signature: worry and preemptive action. Produces unwanted intervention, sacrifice, and conflict when the charge resists protection. Where the responsibility is formal, the duty is the setup and the behavior is what the character does beyond it.
```

- [ ] **Step 3: Update the Coverage Requirements**

In `## Coverage Requirements`, replace both anchor clauses. Major
characters:

```markdown
**Major characters:** target 8 named relationships. Anchor types that should be present: a family or family-equivalent tie (Kin or Ghost), at least one power-asymmetric relationship (Authority), at least one rivalry or friction relationship, at least one Confidant. Additional entries should include at least one genuine friction source beyond rivalry — Obligation, Unease, or Ideological Counterpart.
```

with:

```markdown
**Major characters:** target 8 named relationships. Anchor types that should be present: a family or family-equivalent tie (Kin or Ghost), at least one power-asymmetric relationship (Authority or Charge), at least one rivalry or friction relationship, at least one Confidant. Additional entries should include at least one genuine friction source beyond rivalry: Obligation, Unease, or Ideological Counterpart.
```

The supporting-character line already says "one power-asymmetric
relationship" without naming Authority, so it needs no change. Verify
that in Step 5 rather than assuming it.

- [ ] **Step 4: Update the checklist anchor list in `SKILL.md`**

In the **Relationships** block of the Self-Check list, replace:

```markdown
- [ ] Coverage requirements met: 8 named relationships for major characters, 5 for supporting; required anchor types present (family or Ghost, Authority, friction or rivalry, Confidant — see `relationships.md` for full requirements)
```

with:

```markdown
- [ ] Coverage requirements met: 8 named relationships for major characters, 5 for supporting; required anchor types present (family or Ghost, Authority or Charge, friction or rivalry, Confidant; see `relationships.md` for full requirements)
```

- [ ] **Step 5: Verify no stale Authority-as-anchor wording survives**

Run: `rg -n 'power-asymmetric' skills`

Expected: two matches in `relationships.md` (major line now reading
"Authority or Charge", supporting line unchanged and naming no
archetype). If the supporting line names Authority, update it the same
way and re-run.

Run: `rg -n 'ward downward|not a formal subordinate' skills`

Expected: no matches, exit code 1.

- [ ] **Step 6: Run the repo gates**

Run: `python -m pytest tests -q`

Expected: all 13 tests pass.

Run: `doodle --strict skills`

Expected: exits 0, no findings.

- [ ] **Step 7: Commit**

```bash
git add skills/worldbuilder-character/relationships.md skills/worldbuilder-character/SKILL.md
git commit -m "Split Authority and Charge by direction

Authority was defined to cover both directions, so the label carried no
direction at all: an upward and a downward relationship scored as a
repeat against the per-character repetition limit despite being
different behavioral engines, and downward Authority overlapped Charge.
The 2026-07-23 blind trial read this as the model misapplying labels;
the shipped definition produced it.

Authority is now upward only. Charge absorbs the downward direction and
drops its 'not a formal subordinate' exclusion, which widens the
archetype: a formal duty is now a valid Charge setup, with the
behavioral content being what the character does beyond the duty.
Adding a separate downward archetype was considered and rejected as
unnecessary.

Coverage requirements and the SKILL.md checklist now name 'Authority or
Charge' as the power-asymmetry anchor, so narrowing Authority does not
silently make the anchor harder to satisfy."
```

---

### Task 3: Add Cut Filler to the shared writing style

The stopslop arm differs from current by exactly one section. Adopting
it means adding that section, merged against the rule it overlaps
rather than appended whole.

**Files:**
- Modify: `skills/writing-style.md:58-65` (extend *No significance
  inflation*)
- Modify: `skills/writing-style.md` (new subsection under `## Word
  Choice`)

**Interfaces:**
- Produces: a `### Cut filler` subsection that every Wide-phase skill
  inherits by reference to `writing-style.md`.

- [ ] **Step 1: Fold the vague-declarative group into the existing rule**

Cut Filler's fifth group duplicates *No significance inflation*. Extend
the shipped rule instead of restating it. Replace
`skills/writing-style.md:65`:

```markdown
"Pivotal," "enduring," "testament," "underscores," "highlights," "reflects broader": cut them. They add length without adding information.
```

with:

```markdown
"Pivotal," "enduring," "testament," "underscores," "highlights," "reflects broader": cut them. They add length without adding information.

Vague declaratives are the same move in sentence form: "the stakes are high," "the reasons are structural," "the implications are significant." Each one announces that something matters without saying what it is. Cut the sentence and state the fact it was standing in for.
```

- [ ] **Step 2: Add the Cut filler subsection**

Insert a new subsection at the end of `## Word Choice`, immediately
after the extended *No significance inflation* rule and before the `---`
that closes the section:

```markdown
### Cut filler

Delete phrases that announce importance instead of carrying it, and strip adverbs that pad a claim instead of sharpening it.

- Wrong: "It's worth noting that she essentially runs the kitchen."
- Right: "She runs the kitchen."

Cut these groups outright:

- Throat-clearers: "here's the thing," "it's worth noting," "the truth is," "let me be clear."
- Emphasis crutches: "full stop," "make no mistake," "let that sink in," "I promise."
- Jargon standing in for a plain verb: "navigate," "unpack," "lean into," "deep dive," "circle back."
- Adverbs of degree: "really," "just," "genuinely," "truly," "deeply," "actually," "simply," "honestly."

- Wrong: "She genuinely just wants to help, honestly."
- Right: "She wants to help."
```

The vague-declaratives group is deliberately absent here: it lives in
*No significance inflation* per Step 1, because
`skills/writing-style.md:147` (*Single source of truth*) forbids stating
one rule in two places.

- [ ] **Step 3: Verify placement and non-duplication**

Run: `rg -n '^#{2,3} ' skills/writing-style.md`

Expected: `### Cut filler` appears inside `## Word Choice`, after
`### No significance inflation` and before `## Sentence Structure`.

Run: `rg -n 'the stakes are high' skills/writing-style.md`

Expected: exactly one match, inside the *No significance inflation*
rule.

- [ ] **Step 4: Run the repo gates**

Run: `doodle --strict skills`

Expected: exits 0. This step is the real check on Cut Filler's own
prose, since the section bans constructions the linter also flags.

Run: `python -m pytest tests -q`

Expected: all 13 tests pass.

- [ ] **Step 5: Commit**

```bash
git add skills/writing-style.md
git commit -m "Adopt the stopslop Cut Filler rules into writing-style

The 2026-07-23 blind trial's style axis reduced to one section: the
stopslop arms carried a Cut Filler block that the current arms did not.
The Style Model block absent from the stopslop source was
de-duplication, not a treatment, since the trial base carried the
action-line convention independently; ADR 0004 is untouched.

Four of the five banned groups are new. The fifth, vague declaratives,
is folded into the existing No significance inflation rule rather than
restated, per the single-source-of-truth rule at writing-style.md:147."
```

---

### Task 4: Add the additive doctrine principles to the character framework

Three principles are novel and two extend rules already shipped. This
task covers everything landing in `framework.md`.

**Files:**
- Modify: `skills/worldbuilder-character/framework.md:70-80` (extend the
  trait table rule)
- Modify: `skills/worldbuilder-character/framework.md:105-110` (extend
  Contradictions)
- Modify: `skills/worldbuilder-character/framework.md` (two new
  subsections in the Soul section)

**Interfaces:**
- Produces: Knowledge Boundaries, Unresolved States and A Life in Motion
  as named Soul rules that Task 5's checklist items refer to by name.

- [ ] **Step 1: Add the replacement formula to the trait rule**

`framework.md:70-80` shows label-vs-behavioral pairs but does not say
what to replace a trait word with. Append after the closing line
("Labels give the LLM one word to repeat..."):

```markdown
**Heavy trait adjectives are banned outright**, in every section: "intelligent," "analytical," "arrogant," "dominant," and words of that weight. One of them outvotes a page of behavioral description and pulls the character toward the stock type welded to that word. A softer adjective is not the fix. Replace the label with three things: the domain the character is competent in, the drive behind that competence, and a cost or flaw the competence produces.

- Wrong: "She is highly intelligent and analytical."
- Right: "She rereads every contract twice and catches the clause everyone else missed, because one bad signature cost her a job at 24. She cannot sign off on anything without checking it three times, which makes her slow under pressure."
```

- [ ] **Step 2: Add Knowledge Boundaries to the Soul section**

Insert a new `###` subsection in the Soul section, after the trait rule
from Step 1:

```markdown
### Knowledge boundaries

For every topic the character has expertise in, state where that expertise stops. Unbounded competence produces a character who somehow knows everything about everything, because nothing in the note says otherwise. Per-topic depth beats a global claim of intelligence.

- Wrong: "She's the smartest person in the room and can handle anything that comes up."
- Right: "She can price a shipment of grain to the coin and knows which merchants are lying about a bad harvest. She has never read a legal contract and hands those to someone else without embarrassment."
```

- [ ] **Step 3: Add A Life in Motion to the Soul section**

Insert immediately after the Knowledge boundaries subsection:

```markdown
### A life in motion

The character carries ongoing pressures of their own — money, family, obligations — that move on their own timeline whether or not the player is present. These give the character something to act on beyond reacting to the player.

- Wrong: a character whose only stated concerns are things the player raises first.
- Right: "Rent is due at the end of the month and she is short. Her brother has asked to borrow money again. Neither problem waits for anyone to ask about it."
```

- [ ] **Step 4: Extend Contradictions with Unresolved States**

The shipped Contradictions rule covers internal friction but not leaving
the character's direction open. Append to the Contradictions subsection,
after the existing two bullet questions:

```markdown
**Leave the direction unresolved.** The present must hold live competing pulls, not settled facts. A resolved fact is a shortcut around the work of finding out who the character is right now; an unresolved tension forces that discovery in every scene. Leave multiple futures open, none of them chosen.

- Wrong: "She has decided to leave the guild once the debt is paid."
- Right: "She keeps a half-packed bag under her bed and adds to the guild's ledger anyway. Some weeks she counts the debt down. Some weeks she pays more than she owes."
```

- [ ] **Step 5: Verify the new rules landed**

Run: `rg -n '^### ' skills/worldbuilder-character/framework.md`

Expected: `### Knowledge boundaries` and `### A life in motion` both
present, both inside the Soul section and before the Contradictions
subsection's closing.

Run: `rg -c 'half-packed bag|price a shipment of grain|rereads every contract' skills/worldbuilder-character/framework.md`

Expected: `3`.

- [ ] **Step 6: Run the repo gates**

Run: `doodle --strict skills`

Expected: exits 0.

Run: `python -m pytest tests -q`

Expected: all 13 tests pass.

- [ ] **Step 7: Commit**

```bash
git add skills/worldbuilder-character/framework.md
git commit -m "Fold the additive doctrine principles into the character framework

Adopts four of the five principles from the blind trial's additive
doctrine block: the banned-trait-word replacement formula (domain,
drive, cost) extending the existing label-vs-behavioral table;
knowledge boundaries and a life in motion as new Soul rules; and
unresolved states extending the Contradictions rule.

The trial did not earn this on measured evidence. Packet-2, stopslop
without additive, beat packet-1 on behavioral specificity and slop
density, and both additive arms scored 4 where the only two 5s were
non-additive. Adopted on the human qualitative read of note-1, ahead of
the data, because repeated human A/B runs are not worth their cost at
this stage. Tracked for revisit in .claude/inbox.md."
```

---

### Task 5: Add the specification boundary to the writing rules and update the checklist

The fifth principle belongs with the other cross-section writing rules,
not in the Soul framework, and every new rule needs a self-check item or
it will not be enforced.

**Files:**
- Modify: `skills/worldbuilder-character/SKILL.md:82-106` (Writing Rules)
- Modify: `skills/worldbuilder-character/SKILL.md` (Soul block of the
  Self-Check list)

**Interfaces:**
- Consumes: the rule names established in Task 4 — "knowledge
  boundaries", "a life in motion", "leave the direction unresolved".

- [ ] **Step 1: Add the specification boundary rule**

Insert into `## Writing Rules`, immediately after the **Make decisions,
don't hedge** rule (so the two sit adjacent and the distinction is
readable):

```markdown
**Decide what not to specify.** For each detail, ask whether it changes behavior. Specify the details that lock behavior and leave the rest unwritten. This is not the same as the hedging rule above: hedging governs what you commit to when you do write a fact, and this governs which facts you decline to write at all.

- Wrong: "The house was pale green with a red door on the third street past the mill, and the family kept a gray cart horse named Birch." None of it changes how she behaves.
- Right: "The house was cramped and the walls were thin." That fact alone explains why she can't sleep with a door closed.
```

- [ ] **Step 2: Add self-check items for the new rules**

In the **Soul** block of `## Self-Check Before Marking Complete`, add
after the existing "Plain language throughout" item:

```markdown
- [ ] No heavy trait adjectives anywhere in the note; each replaced by the behavior that earned it
- [ ] Where the blueprint states an expertise, it also states where that expertise stops
- [ ] At least one standing pressure of the character's own, shown through what they do about it
- [ ] The character's direction is left unresolved: competing pulls, no chosen future
- [ ] Details that do not change behavior are left unwritten
```

Then, in the same **Soul** block, replace the two coverage-minimum items so
the checklist mirrors the framework's three coverage areas rather than two:

```markdown
- [ ] 3–5 psychological behavioral entries minimum
- [ ] 2–3 general social behavior entries minimum
```

with:

```markdown
- [ ] 3–5 psychological behavioral entries minimum
- [ ] 2–3 general social behavior entries minimum
- [ ] 1 standing-pressure entry minimum, plus a boundary entry for each stated expertise
```

Task 4 added a third coverage area to `framework.md`. Leaving this
checklist at two means a blueprint can pass its own completion check
while missing the entire third group.

- [ ] **Step 3: Verify every new rule has an enforcement item**

Run: `rg -n 'states where that expertise stops' skills/worldbuilder-character/SKILL.md`

Expected: exactly one match, the checklist item added by Step 2. The
corresponding rule lives in `framework.md` under different wording, so
grep for the checklist item's own text rather than a shared phrase.

Run: `rg -c '^- \[ \]' skills/worldbuilder-character/SKILL.md`

Expected: `33`. The file has 27 checklist items before this task; the five new Soul rule checks plus the third coverage-minimum item make 33.

- [ ] **Step 4: Run the repo gates**

Run: `doodle --strict skills`

Expected: exits 0.

Run: `python -m pytest tests -q`

Expected: all 13 tests pass.

- [ ] **Step 5: Full-repo regression check**

Run: `python scripts/build-okf.py`

Expected: exits 0.

Run: `git status --porcelain`

Expected: `defaults/okf.json` is unchanged by this run. If it is
modified, Task 1's regeneration was skipped or the templates drifted;
stop and investigate before committing.

- [ ] **Step 6: Commit**

```bash
git add skills/worldbuilder-character/SKILL.md
git commit -m "Add the specification boundary rule and self-check items

Completes the additive-doctrine fold-in. The specification boundary
lands in Writing Rules rather than the Soul framework because it governs
every section, and sits next to the no-hedging rule with the distinction
stated inline: hedging is about what you commit to when you write a
fact, this is about which facts you decline to write.

Adds five self-check items so the four rules added to framework.md and
the one added here are actually enforced at completion time. A rule with
no checklist item does not survive contact with a real note."
```

---

### Task 6: State no repeats as the archetype-variety ideal

**Execution order: run this immediately after Task 2**, before Task 3.
Both edit `relationships.md`, and Task 2's changes should land first.

The distribution guidance currently sets its target as a ceiling ("no
more than once or twice", "at least 4–5 distinct archetypes"), which
reads as permission to repeat. The ideal is that every relationship
carries a different archetype. A major character has 8 relationships and
there are 12 archetypes, so a set with no repeats is achievable.

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md` (Archetype
  Distribution: the repetition-limit paragraph and the self-check
  paragraph)
- Modify: `skills/worldbuilder-character/relationships.md` (Coverage
  Validation, item 2)

**Interfaces:**
- Consumes: the `Authority` / `Charge` split from Task 2. Narrowing
  Authority to one direction increases the archetype pool available for
  a no-repeat set, so this task must not run before it.

- [ ] **Step 1: Rewrite the repetition limit as a no-repeat ideal**

Replace the **Per-character repetition limit** paragraph:

```markdown
**Per-character repetition limit:** No single archetype should appear more than once or twice across a character's full relationship list. If an archetype is applied more than twice, treat that as a signal to reconsider: is the framing too loose, or is there a more specific archetype that would better serve behavioral variety?
```

with:

```markdown
**The ideal is no repeats.** No archetype should appear twice across a character's full relationship list, counting every tag on every entry. There are 12 archetypes against 8 named relationships for a major character and 5 for a supporting one, so a set with no repeats has room to spare, though tagging an entry with more than one archetype uses that room up faster. Treat every repeat as a signal to reconsider before accepting it: is the framing too loose, or is there a more specific archetype that would better serve behavioral variety? Where a repeat survives that check, no archetype may appear more than twice.
```

- [ ] **Step 2: Align the self-check with the same ideal**

Replace the **Self-check before finalizing** paragraph:

```markdown
**Self-check before finalizing:** Scan the full relationship list and count how many times each archetype appears. If any archetype appears three or more times, revisit those entries. If Community Thread appears more than once, reconsider the weaker entry. Aim for at least 4–5 distinct archetypes across the full set.
```

with:

```markdown
**Self-check before finalizing:** Scan the full relationship list and count how many times each archetype appears, counting every tag on every entry. Every repeat is worth revisiting. An archetype appearing three or more times is wrong and must be fixed. If Community Thread appears more than once, reconsider the weaker entry. The ideal is that no archetype appears twice anywhere in the set, whether or not an entry carries more than one tag.
```

- [ ] **Step 3: Align the Coverage Validation scan**

In `## Coverage Validation`, replace item 2:

```markdown
2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list. Flag any archetype used three or more times for revision. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.
```

with:

```markdown
2. **Archetype distribution scan:** Count how many times each archetype appears across the full relationship list, counting every tag on every entry. The ideal is no repeats: flag every repeat for reconsideration, and treat any archetype used three or more times as wrong and fix it. Flag any Community Thread entry beyond the first — these are the lowest-value entries and should be replaced with something more specific when possible.
```

- [ ] **Step 4: Verify the ceiling framing is gone and the counting unit is stated**

Run: `rg -n 'once or twice|at least 4' skills/worldbuilder-character/relationships.md`

Expected: no matches, exit code 1.

Run: `rg -c 'no repeats' skills/worldbuilder-character/relationships.md`

Expected: `2`.

Run: `rg -c 'counting every tag on every entry' skills/worldbuilder-character/relationships.md`

Expected: `3` — all three passages must name the same counting unit, because
an entry may carry more than one archetype (`relationships.md:23`) and a
passage that counts entries instead of tags will disagree with the others.

- [ ] **Step 5: Run the repo gates**

Run: `python -m pytest tests -q`

Expected: all 13 tests pass.

Run: `doodle --strict skills`

Expected: exits 0, no findings.

- [ ] **Step 6: Commit**

```bash
git add skills/worldbuilder-character/relationships.md
git commit -m "State no repeats as the archetype-variety ideal

The distribution guidance expressed its target as a ceiling: 'no more
than once or twice' and 'at least 4-5 distinct archetypes' both read as
permission to repeat, when the intent is that every relationship carries
a different archetype. A major character has 8 relationships against 12
archetypes, so a no-repeat set is achievable rather than aspirational.

The two-occurrence ceiling is retained as the outer bound for a repeat
that survives reconsideration, and three or more is now stated as a
defect rather than a flag."
```

---

## Execution amendments

Review found defects in this plan's own step text, not only in how it was
applied. The step text above is what was planned; this section records
what actually shipped. Where the two differ, the commits are authoritative.

Task 6's step text was rewritten in place at `c95d6b9` because its brief
was still regenerable at the time and would have reintroduced a closed
defect. Tasks 2, 4 and 5 were already past that point, so their changes
are recorded here instead of retro-edited into the steps, which would
erase the fix history.

**Task 2 — `cdc2373`.** The Charge rewrite was over-wide: it covered
responsibility toward a peer, which carries no asymmetry, and silently
dropped the original exclusion of kin while the commit documented only
the formal-subordinate drop. Both hollowed out the "Authority or Charge"
coverage anchor. Charge now requires the stronger position, excludes kin,
and names itself the downward counterpart to Authority.

**Task 4 — `c44903d`, `38ac2cd`, `5b9f907`.** Four defects, all in the
planned text:

- The trait-word replacement was competence-shaped (domain, drive, cost)
  while the ban names "arrogant" and "dominant", which are not
  competences. Now general, with the three-part form as the competence
  case.
- "For every topic the character has expertise in" was unbounded and
  collided with the specification boundary added in Task 5. Now scoped to
  expertise the blueprint already states.
- "A life in motion" collided with the shipped no-forward-references
  rule, since a standing pressure and a scheduled event read alike. The
  boundary is now drawn at whether the thing has already happened.
- Neither new Soul rule had a slot or an entry budget in the Soul
  coverage list, and the Soul section opener still announced two coverage
  areas. Both rules now name where their output lands, the coverage list
  has a third group, and its minimum is conditional so a character with
  no stated expertise can still satisfy it.

The "a life in motion" Right example was also replaced: the planned one
stated the character's situation rather than showing behavior, which
contradicted the instruction above it and failed the file's staging test.

**Task 5 — `b327b25`.** The self-check item for the specification
boundary sat in the Soul block with no scope marker, so a rule
deliberately placed in Writing Rules for governing every section read as
Soul-only. It now opens with "Across every section".

Task 5's Step 3 check was also corrected at `2fd1c17`: it grepped for a
phrase from an earlier draft of the checklist item and could not be
satisfied by any faithful transcription. The executor stopped rather than
reword the item to force the grep to pass.

---

## Close-out

After Task 5:

- [ ] Flip this plan's status tag to `complete`.
- [ ] Flip
  [2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md](../research/2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md)
  to `complete` — its findings are now acted on.
- [ ] Delete the two 2026-07-24 inbox lines this plan closes (the
  relationship-label fix and the doctrine fold-in). Leave the
  2026-07-25 revisit line in place; it tracks work this plan
  deliberately does not do.
- [ ] The fold-in inbox line also carried the World-Forge audit patterns
  (scenario classes, cold-read author/grader separation, counterfactual
  probe, blind-line voice test). This plan does **not** cover them —
  they are trial-methodology improvements, not doctrine. Re-capture them
  as their own inbox line before deleting the original.
