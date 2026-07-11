---
type: plan
title: Writing-doctrine blind-trial kit build
description: 'Implementation plan for trials/2026-07-writing-doctrine/: source blocks,
  packet build script with baked shuffle and sealed key, brief procedure, rubric,
  runner README.'
tags:
- complete
date: 2026-07-11
timestamp: 2026-07-11T16:50Z
resources:
- '[[2026-07-11-writing-doctrine-blind-trial-kit]]'
- '[[2026-07-11-blind-trial-kit-implementation-research]]'
---

# Writing-doctrine blind-trial kit build

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).

**Goal:** Build the portable blind-trial kit `trials/2026-07-writing-doctrine/` defined by the [approved spec](../specs/2026-07-11-writing-doctrine-blind-trial-kit.md): six instruction packets (2 style rule sets x 3 doctrine levels), brief procedure, rubric, runner README, and a build script that assembles packets from shared source blocks and seals a base64 key.

**Architecture:** Packets are generated, not hand-written. Shared prose lives in `src/` blocks; `build.py` splices the style and doctrine blocks into two marker points in `src/base.md`, shuffles the six cells across packet numbers, and writes the sealed key. A unittest file locks the assembly properties (axis purity, no marker leaks, no model names, valid key permutation).

**Tech Stack:** Markdown deliverables; Python 3 stdlib-only build script (repo convention: python3 shebang, `newline='\n'` writes); plain `unittest` run directly.

**Implementation research:** [Blind-trial kit implementation research](../research/2026-07-11-blind-trial-kit-implementation-research.md) — read §1 (include/exclude heading maps), §2 (stop-slop rule inventory), §3 (additive/tension source passages) before the content tasks.

## Global Constraints

- Model-neutral (CLAUDE.md, verbatim): "never name a specific AI model in templates, stub notes, or skill instructions that reach end users — 'for future agents', never a product name." Applies to every file in `trials/`. "LLM" is allowed.
- Kit prose follows the plugin writing doctrine: plain, concrete, no filler (`skills/writing-style.md` spirit; check drafts against `docs/slop-phrases.md`).
- Packets are self-contained and portable: no references to this repo's paths, skill names, vault mechanics, or the trial's design rationale.
- Packets must not tell the writing agent to name its rules in the note; notes must not self-identify their arm.
- The six packets are byte-identical outside the two axis blocks — guaranteed by generation, never hand-edit `packet-*.md` or `key.md`.
- No OKF frontmatter on any file in `trials/` (outside `.claude/`, unenforced).
- The writing agent contract in every packet: no questions to the user; no invoking or opening any installed worldbuilding skill or style reference; where brief and vault are silent, decide per the packet and move on.
- Commit after every task.

---

### Task 1: `src/base.md` — shared instruction set

**Files:**
- Create: `trials/2026-07-writing-doctrine/src/base.md`

**Interfaces:**
- Produces: `base.md` containing exactly one `<!-- STYLE-BLOCK -->` line and one `<!-- DOCTRINE-BLOCK -->` line (Task 5's build script replaces them; Task 5's tests assert no markers survive assembly).

- [x] **Step 1: Write the frame and contract**

Open `base.md` with this structure (actual heading names; prose to be written in full, following the include/exclude map below):

```markdown
# Character Note Instructions

## Your Task
## What You Receive
## Rules of Engagement
## Note Structure
## Writing Rules
<!-- DOCTRINE-BLOCK -->
## Style Rules
<!-- STYLE-BLOCK -->
## Background
## Body
## Soul
## Relationships
## Intimate Dynamics (only if the brief flags it)
## Self-Check Before Finishing
```

`Your Task`: write one complete character note body (Background, Body, Soul, Relationships; Intimate Dynamics only if the brief flags it) for the character described in the brief, to the output path named in your dispatch instructions. `What You Receive`: the brief (a frozen Q&A transcript), read access to the project vault (seed, direction, existing notes) for relationships and world grounding. `Rules of Engagement` (all four, verbatim intent from the spec):

```markdown
- Use only this document, the brief, and the project vault. Do not invoke
  or open any installed worldbuilding skill or style reference.
- Asking the user is not available. Where the brief and vault are silent,
  decide and move on.
- Do not name or quote these instructions in the note. The note contains
  only the character.
- Do not read any other packet or any other agent's output.
```

- [x] **Step 2: Port the note structure and writing rules**

From `skills/worldbuilder-character/SKILL.md`, per the dossier §1 map:

- Include: `## Overview` paragraph 1 (behavioral-specification framing) into `Your Task`; the section table from `## Character Note Structure` minus the Design Notes row and the frontmatter/rename paragraph; all five bolded rules from `## Writing Rules` plus the asymmetry note.
- Rewire every "ask the user" phrasing to the no-questions rule (e.g. the hedging rule's "If you don't know, ask the user." becomes "If the brief doesn't say, decide and keep it consistent.").
- Exclude: `## Design Notes`, `### Session Notes`, `### Builder Context`, `## Session Flow`, `## Story Notes`, `## Post-Group Sync Pass`, all sub-file pointers, all `new_doc.py`/frontmatter/status-tag mechanics.

- [x] **Step 3: Port the section construction rules**

- `## Background`, `## Body`, `## Soul` from `skills/worldbuilder-character/framework.md`: include essentially all — the When/Behavior/Because formula, the label-vs-behavioral table, coverage minimums (3–5 psychological + 2–3 social entries, required contradiction and irrational-behavior-with-root), the Because-clause section with its Design-Notes/Q&A dependency redirected to "the Because clause must trace to wants, fears, or experiences stated in the brief; if the brief gives none, choose one consistent with the brief and use it consistently."
- `## Relationships` from `relationships.md`: the 12 archetypes, coverage requirements (major: 8 named, anchors Kin-or-Ghost / Authority / rivalry-or-friction / Confidant plus one more friction source; supporting: 5), archetype distribution, entry format (`**Name — Archetype(s):**` bullets), generativity hierarchy, per-entry internal-state check — minus all `project/plan.md` capture mechanics.
- `## Intimate Dynamics` from `intimate.md`: overview paragraph 1, format, coverage including the required friction point; conditional stated as "only if the brief flags this character for intimate dynamics."
- `## Self-Check Before Finishing`: only the Background / Body / Soul / Relationships / Intimate blocks from SKILL.md's self-check, minus Frontmatter, Design Notes, Story Notes, Pre-Handoff Scan, and Description items.

- [x] **Step 4: Verify self-containment and neutrality**

Run: `grep -inE "claude|anthropic|gpt|openai|gemini" trials/2026-07-writing-doctrine/src/base.md`
Expected: no output.
Run: `grep -inE "new_doc|frontmatter|Design Notes|Session Notes|worldbuilder|scraibe|framework\.md|relationships\.md|writing-style" trials/2026-07-writing-doctrine/src/base.md`
Expected: no output.
Run: `grep -c "STYLE-BLOCK" trials/2026-07-writing-doctrine/src/base.md` and same for `DOCTRINE-BLOCK`
Expected: `1` each.

- [x] **Step 5: Commit**

```bash
git add trials/2026-07-writing-doctrine/src/base.md
git commit -m "trial-kit: shared instruction set (base block)"
```

---

### Task 2: `src/style-current.md` — current style block

**Files:**
- Create: `trials/2026-07-writing-doctrine/src/style-current.md`

**Interfaces:**
- Produces: a block of H3-and-below content (no H1/H2 — it lands under base.md's `## Style Rules`). Contains the sentinel heading `### Four Failure Modes` (Task 5's tests key on it).

- [x] **Step 1: Port writing-style.md, demoted one heading level**

Copy `skills/writing-style.md` content with H2→H3, H3→H4. Include everything: Style Model (staging test), Word Choice (3 subsections, full 12-row table), Sentence Structure (5 subsections including no em-dashes), Content Standards (6 subsections), Structure, Four Failure Modes. Exclude: the header paragraphs naming Wide/Export phases and the export-skill pointer; the closing `docs/slop-phrases.md` pointer (that file is the rubric's slop-density checklist — shipping it in a packet coaches the arm). Replace "spec documents" framing with "the character note" where it appears.

- [x] **Step 2: Verify**

Run: `grep -inE "export|wide phase|slop-phrases" trials/2026-07-writing-doctrine/src/style-current.md`
Expected: no output.
Run: `grep -c "^### Four Failure Modes" trials/2026-07-writing-doctrine/src/style-current.md`
Expected: `1`.
Run: `grep -nE "^## |^# " trials/2026-07-writing-doctrine/src/style-current.md`
Expected: no output (block starts at H3).

- [x] **Step 3: Commit**

```bash
git add trials/2026-07-writing-doctrine/src/style-current.md
git commit -m "trial-kit: current style block"
```

---

### Task 3: `src/style-stopslop.md` — stop-slop style block

**Files:**
- Create: `trials/2026-07-writing-doctrine/src/style-stopslop.md`

**Interfaces:**
- Produces: a block of H3-and-below content in the same format as Task 2 (rule + wrong/right example pairs). Contains the sentinel heading `### Vary Rhythm` (Task 5's tests key on it).

- [x] **Step 1: Write the eight rules in current-block format**

Source: dossier §2 (stop-slop is MIT-licensed; derivation is fine). One H3 per rule, each with at least one wrong/right pair **written fresh in the character-note domain** — do not copy stop-slop's own examples (its examples.md is internally inconsistent: an em-dash appears in an "after" example). The eight rules, with required adaptations:

1. `### Cut Filler` — throat-clearing phrases, emphasis crutches, adverbs. Fold in the phrase-ban groups from stop-slop's phrases.md as a compact ban list.
2. `### Break Formulaic Structures` — binary contrasts ("not X but Y"), negative listing, dramatic fragmentation, rhetorical setups, false agency.
3. `### Active Voice, Human Subject` — no passive constructions.
4. `### Be Specific` — no lazy extremes. **Adaptation:** exempt behavioral frequency statements the note needs ("always counts the till twice" is a behavior, not a lazy extreme; ban vague intensity, keep true routines).
5. `### Vary Rhythm` — mix sentence lengths; two items beat three; no em-dashes.
6. `### Trust the Reader` — no softening, no justifying, no meta-commentary.
7. `### Cut Quotables` — no lines written to be admired.
8. `### Sentence Openers` — no What/Why/So/Look openers. **Adaptation (required carve-out):** "When [trigger], [behavior], because [reason]" sentences are the note's core formula and are exempt; the ban covers rhetorical openers, not the formula. Without this carve-out the style axis contaminates the doctrine axis.

Drop stop-slop's reader-in-the-room/direct-address rule entirely (targets essay prose; the note is third-person). Scrub any vendor or product names from derived text. Example of the required pair format:

```markdown
### Cut Filler

Delete phrases that announce importance instead of carrying it.

- Wrong: "It's worth noting that she essentially runs the kitchen."
- Right: "She runs the kitchen."
```

- [x] **Step 2: Verify**

Run: `grep -inE "claude|anthropic|gpt|openai|stop-slop|stopslop" trials/2026-07-writing-doctrine/src/style-stopslop.md`
Expected: no output.
Run: `grep -c "^### Vary Rhythm" trials/2026-07-writing-doctrine/src/style-stopslop.md`
Expected: `1`.
Run: `grep -n "—" trials/2026-07-writing-doctrine/src/style-stopslop.md | grep -v "Wrong:"`
Expected: no output (em-dashes only inside Wrong examples, if anywhere).

- [x] **Step 3: Commit**

```bash
git add trials/2026-07-writing-doctrine/src/style-stopslop.md
git commit -m "trial-kit: stop-slop style block"
```

---

### Task 4: doctrine blocks — `src/doctrine-additive.md` and `src/doctrine-tensions.md`

**Files:**
- Create: `trials/2026-07-writing-doctrine/src/doctrine-additive.md`
- Create: `trials/2026-07-writing-doctrine/src/doctrine-tensions.md`

**Interfaces:**
- Produces: `doctrine-additive.md` opens with `## Additional Construction Rules` and contains the sentinel heading `### Knowledge Boundaries`. `doctrine-tensions.md` contains only H3s (it concatenates under additive's H2) and the sentinel heading `### Anchor Repetition`. (Task 5's tests key on both sentinels; level-3 packets receive additive + tensions concatenated.)

- [x] **Step 1: Write `doctrine-additive.md`**

Five H3 principles under `## Additional Construction Rules`, each an instruction (not a finding) with one wrong/right pair, sourced from dossier §3 quotes:

1. `### Banned Trait Words` — heavy trait adjectives (intelligent, analytical, arrogant, dominant, and their class) may not appear anywhere in the note; they outvote every behavioral description. Replace with domain of competence, the drive behind it, and a cost or flaw it produces.
2. `### Knowledge Boundaries` — state what the character knows per topic and where their insight stops; per-topic depth beats a global trait.
3. `### Unresolved States` — the present must contain live, competing pulls; multiple supported futures, none chosen. Resolved facts are shortcuts; unresolved tensions force the character's position to be found in each scene.
4. `### The Specification Boundary` — for each detail, decide: does it change behavior, or can it stay open? Specify what locks behavior; deliberately leave the rest open. This governs what you deliberately don't write; the no-hedging rule still governs what you do write.
5. `### A Life in Motion` — the character carries independent ongoing pressures (money, family, obligations) that move without the player.

- [x] **Step 2: Write `doctrine-tensions.md`**

Two H3 exemptions, phrased as explicit overrides layered onto the base rules (so level-3 packets differ from level-2 only by these paragraphs):

1. `### Emotional Memory Hooks` — exemption to the plain-style rule: up to a handful of compressed, specific, unresolved sensory fragments are allowed where they carry more behavioral weight than explanation. A hook is still concrete and observable; it is dense, not decorative.
2. `### Anchor Repetition` — exemption to section discipline: a key anchor (a person, object, or loss) may be referenced from multiple sections to give it multiple activation routes. Reference, don't duplicate: the anchor's description lives once; other sections name it.

- [x] **Step 3: Verify**

Run: `grep -inE "claude|anthropic|gpt|openai|reference doc|dossier|trial" trials/2026-07-writing-doctrine/src/doctrine-additive.md trials/2026-07-writing-doctrine/src/doctrine-tensions.md`
Expected: no output.
Run: `grep -c "^### Knowledge Boundaries" trials/2026-07-writing-doctrine/src/doctrine-additive.md`
Expected: `1`.
Run: `grep -c "^### Anchor Repetition" trials/2026-07-writing-doctrine/src/doctrine-tensions.md`
Expected: `1`.
Run: `grep -nE "^## " trials/2026-07-writing-doctrine/src/doctrine-tensions.md`
Expected: no output.

- [x] **Step 4: Commit**

```bash
git add trials/2026-07-writing-doctrine/src/doctrine-additive.md trials/2026-07-writing-doctrine/src/doctrine-tensions.md
git commit -m "trial-kit: doctrine blocks (additive + tensions)"
```

---

### Task 5: `build.py` + tests — assembly, shuffle, sealed key

**Files:**
- Create: `trials/2026-07-writing-doctrine/build.py`
- Test: `tests/test_build_trial_kit.py`

**Interfaces:**
- Consumes: the five `src/` files and their markers/sentinels from Tasks 1–4.
- Produces: `build.py` writing `packet-1.md` … `packet-6.md` and `key.md` into its own directory by default, or into `sys.argv[1]` when given (tests build into a temp dir so the committed shuffle is not churned). Key format: markdown warning header, then a fenced block holding base64-encoded JSON `{"packet-N": {"style": "current"|"stopslop", "doctrine": "current"|"additive"|"tensions"}}`.

- [x] **Step 1: Write the failing test**

```python
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "trials", "2026-07-writing-doctrine")

SENTINELS = {
    "style": {"current": "### Four Failure Modes", "stopslop": "### Vary Rhythm"},
    "doctrine": {"additive": "### Knowledge Boundaries", "tensions": "### Anchor Repetition"},
}


class TestTrialKitBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = tempfile.mkdtemp()
        subprocess.run(
            [sys.executable, os.path.join(KIT, "build.py"), cls.out], check=True
        )
        cls.packets = {}
        for i in range(1, 7):
            with open(os.path.join(cls.out, f"packet-{i}.md"), encoding="utf-8") as f:
                cls.packets[i] = f.read()
        with open(os.path.join(cls.out, "key.md"), encoding="utf-8") as f:
            key_raw = f.read()
        payload = re.search(r"```\n(.+?)\n```", key_raw, re.S).group(1)
        cls.key = json.loads(base64.b64decode(payload))

    def test_key_is_a_permutation_of_all_six_cells(self):
        cells = {(v["style"], v["doctrine"]) for v in self.key.values()}
        self.assertEqual(len(self.key), 6)
        self.assertEqual(
            cells,
            {(s, d) for s in ("current", "stopslop")
             for d in ("current", "additive", "tensions")},
        )

    def test_no_markers_or_comments_leak(self):
        for text in self.packets.values():
            self.assertNotIn("<!--", text)

    def test_packets_share_identical_frame(self):
        first_headings = {text.splitlines()[0] for text in self.packets.values()}
        self.assertEqual(first_headings, {"# Character Note Instructions"})

    def test_axis_content_matches_key(self):
        for name, cell in self.key.items():
            text = self.packets[int(name.split("-")[1])]
            for style, sentinel in SENTINELS["style"].items():
                if cell["style"] == style:
                    self.assertIn(sentinel, text, name)
                else:
                    self.assertNotIn(sentinel, text, name)
            self.assertEqual(
                SENTINELS["doctrine"]["additive"] in text,
                cell["doctrine"] in ("additive", "tensions"), name)
            self.assertEqual(
                SENTINELS["doctrine"]["tensions"] in text,
                cell["doctrine"] == "tensions", name)

    def test_model_neutrality(self):
        for text in self.packets.values():
            for banned in ("claude", "anthropic", "gpt", "openai", "gemini"):
                self.assertNotIn(banned, text.lower())


if __name__ == "__main__":
    unittest.main()
```

- [x] **Step 2: Run test to verify it fails**

Run: `python tests/test_build_trial_kit.py -v`
Expected: setUpClass error — `build.py` not found / CalledProcessError.

- [x] **Step 3: Write `build.py`**

```python
#!/usr/bin/env python3
"""Assemble the six trial packets from src/ blocks and seal the key.

Every run reshuffles the packet-to-cell assignment. Rebuild only for a
fresh trial (never after outputs exist for the current packets).
Packets and key.md are generated; never hand-edit them.
"""
import base64
import json
import os
import random
import re
import sys

KIT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(KIT, "src")

STYLES = {"current": "style-current.md", "stopslop": "style-stopslop.md"}
DOCTRINES = {
    "current": [],
    "additive": ["doctrine-additive.md"],
    "tensions": ["doctrine-additive.md", "doctrine-tensions.md"],
}

KEY_HEADER = """# Trial key — DO NOT OPEN

Decode only after every score and the preference ranking are recorded
on the rubric sheet. The fenced block is base64; it decodes to the
packet-to-cell map.
"""


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read().strip()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text if text.endswith("\n") else text + "\n")


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else KIT
    base = read("base.md")
    cells = [(s, d) for s in STYLES for d in DOCTRINES]
    random.shuffle(cells)
    key = {}
    for i, (style, doctrine) in enumerate(cells, start=1):
        doctrine_text = "\n\n".join(read(n) for n in DOCTRINES[doctrine])
        packet = base.replace("<!-- STYLE-BLOCK -->", read(STYLES[style]))
        packet = packet.replace("<!-- DOCTRINE-BLOCK -->", doctrine_text)
        packet = re.sub(r"\n{3,}", "\n\n", packet)
        write(os.path.join(out_dir, "packet-%d.md" % i), packet)
        key["packet-%d" % i] = {"style": style, "doctrine": doctrine}
    payload = base64.b64encode(
        json.dumps(key, indent=2).encode("utf-8")).decode("ascii")
    write(os.path.join(out_dir, "key.md"),
          KEY_HEADER + "\n```\n" + payload + "\n```")


if __name__ == "__main__":
    main()
```

- [x] **Step 4: Run tests to verify they pass**

Run: `python tests/test_build_trial_kit.py -v`
Expected: 5 tests, `OK`.

- [x] **Step 5: Commit**

```bash
git add trials/2026-07-writing-doctrine/build.py tests/test_build_trial_kit.py
git commit -m "trial-kit: packet build script with shuffle and sealed key"
```

---

### Task 6: `brief-procedure.md`

**Files:**
- Create: `trials/2026-07-writing-doctrine/brief-procedure.md`

**Interfaces:**
- Produces: the procedure the downstream orchestrator follows before dispatch; names `brief.md` as its output (README, Task 8, references both).

- [x] **Step 1: Write the procedure**

Content, in order:

1. Pick one pending character from the project's cast plan; note whether it carries the intimate-dynamics flag (the flag rides into `brief.md` as a single line).
2. Run the project's normal character Q&A session with the user, exactly as its installed skill prescribes, through Session Notes capture. Stop there: no note sections are written for this character.
3. Freeze the captured Session Notes transcript verbatim as `brief.md` in the kit folder, prefixed by two lines: the character's name and the intimate flag state.
4. After freezing, the brief is read-only for the rest of the trial; if the user volunteers more character detail later, it is out of scope for this run.

The installed-skill ban applies to the six writing agents, not to this pre-trial Q&A — state that explicitly so the orchestrator doesn't over-apply it.

- [x] **Step 2: Verify neutrality**

Run: `grep -inE "claude|anthropic|gpt|openai" trials/2026-07-writing-doctrine/brief-procedure.md`
Expected: no output.

- [x] **Step 3: Commit**

```bash
git add trials/2026-07-writing-doctrine/brief-procedure.md
git commit -m "trial-kit: brief-freezing procedure"
```

---

### Task 7: `rubric.md` — scoring sheet and results record

**Files:**
- Create: `trials/2026-07-writing-doctrine/rubric.md`

**Interfaces:**
- Produces: the sheet the user fills in; README (Task 8) hands it over as the final runner step.

- [x] **Step 1: Write the rubric**

Structure:

1. **How to score** — read all six notes blind, in packet-number order; fill the table; rank last; decode `key.md` only after every cell is filled. One line stating what each 1–5 scale anchors to (1 = fails the criterion throughout, 5 = no violations found on a full read).
2. **Scoring table** — rows: packet-1 … packet-6; columns:
   - Behavioral specificity (1–5): entries describe enactable behavior, not labels.
   - Stageability (1–5): a director could stage the sentences.
   - Liveliness (1–5): the present state contains live, competing pulls a scene could pick up.
   - Trait-word leakage (count): heavy trait adjectives of the poisoning class (intelligent, analytical, arrogant, dominant, and kin).
   - Slop density (count): hits against the project's slop-phrase checklist (`docs/slop-phrases.md` in the plugin repo — the checklist is applied by the scorer, never shipped to the arms).
   - Coverage (n/4): contradiction present; irrational behavior with root; self-image gap; relationship anchors met.
   - Length (words; recorded, not scored).
   - Preference rank (1–6, forced, no ties).
3. **Results record** — empty sections to fill after decoding: the decoded map pasted in; three decision blocks matching the spec's decision mapping (style axis: arms 1–3 vs 4–6; additive step: cells {current} vs {additive}; tensions step: cells {additive} vs {tensions}); an interactions note ("suggestive, not conclusive — one character per cell").

- [x] **Step 2: Verify**

Run: `grep -inE "claude|anthropic|gpt|openai" trials/2026-07-writing-doctrine/rubric.md`
Expected: no output.
Run: `grep -c "packet-6" trials/2026-07-writing-doctrine/rubric.md`
Expected: at least `1`.

- [x] **Step 3: Commit**

```bash
git add trials/2026-07-writing-doctrine/rubric.md
git commit -m "trial-kit: scoring rubric and results record"
```

---

### Task 8: `README.md`, first build, kit review

**Files:**
- Create: `trials/2026-07-writing-doctrine/README.md`
- Create (generated): `trials/2026-07-writing-doctrine/packet-1.md` … `packet-6.md`, `key.md`

**Interfaces:**
- Consumes: everything from Tasks 1–7.

- [x] **Step 1: Write the runner README**

Addressed to the downstream project's orchestrating agent ("for future agents" voice, model-neutral). Contents, in order:

1. **What this is** — a blind writing trial: six sealed instruction packets, one character, six independent agents; the human scores results blind. One sentence; no doctrine rationale, no arm descriptions (the orchestrator stays blind too).
2. **Setup** — copy this folder into the project (scratch location fine); run `brief-procedure.md` to produce `brief.md`; create an empty `out/` directory.
3. **Dispatch** — for each packet 1–6, dispatch one fresh agent with exactly: its packet file, `brief.md`, read access to the project vault, and the instruction to write its note to `out/note-<packet number>.md`. Agents run independently: no shared context, no visibility of other packets or outputs, no user questions, no installed worldbuilding skills.
4. **Collect and hand off** — confirm six output files exist; give the human `rubric.md` and the `out/` folder; do not open `key.md` yourself; the human decodes it only after the rubric is fully scored.
5. **Regeneration note** — packets and `key.md` are generated by `build.py` in the source repo; never hand-edit; a rebuild reshuffles the key, so never rebuild once outputs exist for the current packets.

- [x] **Step 2: Run the first real build**

Run: `python trials/2026-07-writing-doctrine/build.py`
Expected: silent exit 0.
Run: `ls trials/2026-07-writing-doctrine/`
Expected: `README.md`, `brief-procedure.md`, `rubric.md`, `build.py`, `key.md`, `packet-1.md` … `packet-6.md`, `src/`.
Run: `python tests/test_build_trial_kit.py -v`
Expected: 5 tests, `OK` (tests build into a temp dir; the committed shuffle is untouched).

- [x] **Step 3: Kit prose review**

Read each non-generated kit file once against `docs/slop-phrases.md` and the plugin writing doctrine; fix hits in `src/` blocks, then re-run `python trials/2026-07-writing-doctrine/build.py` if any src file changed (a re-run reshuffles — acceptable before release; note it happened).
Run: `grep -rinE "claude|anthropic|gpt|openai|gemini" trials/2026-07-writing-doctrine/ --include="*.md" --exclude=key.md`
Expected: no output. (`key.md` is excluded: its base64 payload can contain any letter run by chance; the decoded map is covered by the unittest.)

- [x] **Step 4: Commit the complete kit**

```bash
git add trials/2026-07-writing-doctrine/
git commit -m "trial-kit: runner README and first sealed build"
```

---

## Out of Scope (this plan)

- Running the trial (downstream project's work, per README).
- The results reflection document and doctrine fold-in edits (follow-up work after the trial; results doc is `--type reflection` per the registry).
- Any edit to shipped skills, `defaults/`, or `docs/`.

## Execution Record (2026-07-11)

All 8 tasks complete over commits `d1e0f5b..c799821`; per-task reviews plus a final whole-branch review, verdict: ready to merge. Deviations from the plan as written:

- The identical-frame test was strengthened beyond the plan's code: it now checks all three static base.md segments in order, not just the first line (`df7e807`); a committed-kit consistency test (6th test) was added by the final-review fix wave, closing the src-drift gap the plan's test spec missed.
- Two rebuild/reshuffles beyond the planned first build: a per-task reviewer disclosed part of the shuffle, forcing a reshuffle (`ead4afa`); the final fix wave rebuilt again (`c799821`).
- Final-review fixes the plan did not anticipate: an em-dash carve-out added identically to both style blocks plus de-dashed base.md example prose (the plan missed the entry-format/style-rule collision while catching the analogous When-formula one); a style-rules scope line in base.md; the README rerun-after-decode caveat; a rubric decode-timing reword.
- Trial-run discipline recorded here for the scorer: before scoring, do not read the packet files, key.md, or any review artifacts containing packet contents — the mapping is derivable from packet content plus the design.
