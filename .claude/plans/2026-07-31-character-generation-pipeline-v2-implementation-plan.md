---
type: plan
title: Character Generation Pipeline v2 Implementation Plan
description: 'Implementation plan for spec 2026-07-31: template doctrine fields, framework
  coverage updates, deslop preprocessing, multi-option generation, selection mechanism
  trial, and grader agent with input-aware detection.'
tags:
- complete
date: 2026-07-31
timestamp: 2026-08-09T00:52Z
resources:
- "[[2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent]]"
- "[[2026-07-31-pipeline-v2-implementation-research-dossier]]"
---

# Character Generation Pipeline v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).

**Goal:** Restructure the character generation pipeline to break input-echo convergence, add five doctrine requirements, and enable input-aware convergence detection as a grader agent.

**Architecture:** Three sequential parts. Part A changes what goes into generation (template fields, preprocessing). Part B changes how generation uses those inputs (multi-option spread, fact-to-manifestation). Part C adds a post-generation quality check (grader agent with input-aware detection). Each part produces independently testable deliverables.

**Tech Stack:** Markdown (skill prose, templates, framework), Python 3.10+ (preprocessing and detection scripts), pytest (script tests), `build-okf.py` (template compilation).

**Governing spec:** [Character Generation Pipeline v2](../specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md)
**Research dossier:** [Pipeline v2 Implementation Research Dossier](../research/2026-07-31-pipeline-v2-implementation-research-dossier.md)

## Global Constraints

- Shipped content is model-neutral: never name a specific AI model in templates, skill instructions, or stub notes that reach end users.
- Skill prose follows `skills/writing-style.md` and `docs/slop-phrases.md`.
- The OKF preset is generated: edit `defaults/okf.base.json` and `defaults/templates/*.md`, then run `python scripts/build-okf.py`. Never hand-edit `defaults/okf.json`.
- Implementation happens on a feature branch off master (per CLAUDE.md branching rule for spec implementation).
- All Python scripts use no external dependencies beyond the standard library unless explicitly noted.

---

### Task 1: Doctrine Additions — Template, Framework, and Skill

Add the 7 structured doctrine fields to the Design Notes template, add new coverage requirements and tension resolutions to framework.md, and update the character skill's Q&A to capture the new fields.

**Files:**
- Modify: `defaults/templates/character.md`
- Modify: `skills/worldbuilder-character/framework.md`
- Modify: `skills/worldbuilder-character/SKILL.md`
- Modify: `skills/worldbuilder-character/relationships.md`

**Interfaces:**
- Consumes: nothing (first task)
- Produces: updated template structure that Tasks 2, 3 reference; updated coverage requirements that Task 3's generation instructions enforce

- [x] **Step 1: Create feature branch**

```bash
git checkout master
git checkout -b pipeline-v2
```

- [x] **Step 2: Add structured doctrine fields to character.md template**

Add a new `### Structured Doctrine` subsection under `## Design Notes`, after `### Builder Context`. The content to insert after line 15 (`-`) of `defaults/templates/character.md`:

```markdown

### Structured Doctrine

_Captured during Q&A. Each field is 1–3 sentences. These are inputs to generation, not output content — the generation step transforms them into behavioral entries._

**Core want:**

**Core fear:**

**Values carry costs:**
_For 2–3 top values: [Value] — [what it has cost]. Also name the lowest values and one act proving they are not held._

**False belief:**
_At least one belief held wrongly and acted on with confidence. Include how they handle not knowing._

**Contrast declaration:**
_Which cast member this character is built against, and on which axis._

**Value-conflict stance:**
_Operating code in their own words. Which way they go when it hits conventional decency (role-following / role-compromise / alignment-compromise / alignment-following). The lever that tips them. How guilt shows._

**Charge-scored memories:**
_Tag each formative memory: **high** (unresolved, drives present behavior), **mid** (settled, explains patterns), **low** (context only). High-charge memories must generate Soul entries._
```

- [x] **Step 3: Add coverage requirements to framework.md**

Insert the following after the current "Boundaries and ongoing pressures" block (after line 131 of `skills/worldbuilder-character/framework.md`), before the "Contradictions" section:

```markdown

**Doctrine-required entries:**
- Core want as behavioral description (1 entry minimum). How the want shows — not "she wants respect" but what she does when she senses disrespect.
- Core fear as behavioral description (1 entry minimum). What the character does when the feared outcome approaches — observable action, not internal dread.
- False belief in action (1 entry minimum). A behavior the character performs because of something they believe that is not true. The belief and the resulting behavior must both be specific.
- Value-conflict stance as behavioral description (1 entry minimum). What the character does when their operating code collides with conventional expectations — the specific action, not the abstract position.
```

Insert the following in the Background section, after the "What to cover" block (after line 28):

```markdown

**Charge tags:** Every formative memory carries a charge tag:
- **high** — unresolved, emotionally live, shapes present behavior directly. Must also generate a corresponding Soul entry.
- **mid** — settled but still referenced, explains patterns.
- **low** — context only, explains origin but does not drive present action. May be omitted if it adds nothing behavioral.

**Values carry costs (2–3 entries):** Fact-pair format:
- [Value held] → [what it cost]

Also state the character's lowest values and one act proving they are not held.
```

Insert the following in the Relationships section guidance (in `skills/worldbuilder-character/relationships.md`, at the end of the coverage requirements):

```markdown

**Contrast declaration (1 entry):** Name the cast member this character is built against and the axis of differentiation. This may be a standalone note rather than a relationship entry. Nothing else in this framework asks whether two characters in a cast are distinguishable — this entry does.
```

- [x] **Step 4: Add tension resolutions to framework.md**

Append the following two sections at the end of `skills/worldbuilder-character/framework.md`:

```markdown

### Anchor repetition and single source of truth

The behavioral framework requires dense interconnection for LLM activation. The writing-style rule requires each fact to live in one place. Resolution:

**Facts live in one place. Behavioral consequences appear wherever they are relevant.** A formative event is stated once in Background. Its behavioral impact appears in Soul (psychological pattern), Body (physical habit it produced), and Relationships (how it shapes a specific dynamic). Each appearance is a behavioral description of the consequence, not a restatement of the fact. The fact is the anchor; the behavioral consequences are the repetition.

### Compressed sensory fragments

Dense sensory fragments as emotional memory hooks ("the last thing she remembers of her mother: lowering her yukata's collar, one word — run") carry more weight than explanation. These are permitted in Background as high-charge memory entries. They do not need to pass the staging test — Background is factual, not behavioral. Their corresponding Soul entry (required for all high-charge memories) must be stageable: the present-day behavior the memory drives, not the memory itself.
```

- [x] **Step 5: Update SKILL.md Q&A to capture new fields**

In `skills/worldbuilder-character/SKILL.md`, add the new doctrine fields to the Q&A coverage prompts. The exact location depends on the skill's Q&A section structure, but the content to add is:

```markdown
During the Q&A phase, capture the following doctrine fields in the Structured Doctrine subsection of Design Notes. Ask for each explicitly if the user's answers do not surface them naturally:

- **Core want:** "What does this character want most — not the surface want, but the deeper want underneath?"
- **Core fear:** "What outcome or realization would be hardest for them to face?"
- **Values carry costs:** "What has holding that value cost them or someone else?" (for each stated value)
- **False belief:** "What does this character believe that is not true, and how does it shape what they do?"
- **Contrast declaration:** "Which existing cast member is this character most likely to be confused with, and what separates them?"
- **Value-conflict stance:** "When this character's code hits what most people would consider decent behavior, which wins? What would tip them the other way?"
- **Charge-scored memories:** After capturing formative memories, tag each as high/mid/low charge.
```

Note: The four new doctrine-required Soul entries (core want, core fear, false belief, value-conflict stance) are ADDITIONAL to the existing 3–5 psychological entry minimum. A complete Soul section needs at minimum 7–9 psychological entries (3–5 existing + 4 doctrine). Update the skill's completion self-check to verify all doctrine entries are present.

- [x] **Step 6: Rebuild OKF preset**

```bash
python scripts/build-okf.py
```

Expected: script exits 0, `defaults/okf.json` is regenerated with the new template content embedded.

- [x] **Step 7: Verify the build**

```bash
python -c "import json; d=json.load(open('defaults/okf.json')); t=[t for t in d['types'] if t['name']=='character'][0]; print('Structured Doctrine' in t.get('template',''))"
```

Expected: `True`

- [x] **Step 8: Commit**

```bash
git add defaults/templates/character.md skills/worldbuilder-character/framework.md skills/worldbuilder-character/SKILL.md skills/worldbuilder-character/relationships.md defaults/okf.json
git commit -m "feat: add 7 structured doctrine fields, coverage requirements, and tension resolutions

Part A of Pipeline v2 spec. Adds core want/fear, values-carry-costs,
false belief, contrast declaration, value-conflict stance, and
charge-scored memories to the Design Notes template and framework
coverage requirements. Resolves anchor-repetition and compressed-
fragment tensions."
```

---

### Task 2: Deslop/Deframe Preprocessing Script

Build a Python script that processes Design Notes content before generation: strips meta-vocabulary (deframe) and applies stop-slop patterns (deslop). Operates on a working copy, preserving the original.

**Files:**
- Create: `scripts/deslop_deframe.py`
- Create: `tests/test_deslop_deframe.py`

**Interfaces:**
- Consumes: Design Notes content (markdown string), `docs/slop-phrases.md` (pattern source)
- Produces: `deslop_deframe.process(text: str) -> ProcessResult` where `ProcessResult` has `.cleaned: str` and `.changes: list[Change]`; Task 3's generation flow calls this before generating entries

- [x] **Step 1: Write the failing tests**

Create `tests/test_deslop_deframe.py`:

```python
import pytest
from scripts.deslop_deframe import process, Change


class TestDeframe:
    def test_strips_stewards_house(self):
        text = "Assigned to the Steward's House as town guard"
        result = process(text)
        assert "Steward's House" not in result.cleaned

    def test_strips_narrative_function(self):
        text = "Narrative function: the character who shows care and predation coexist"
        result = process(text)
        assert "Narrative function" not in result.cleaned

    def test_strips_thematic_mirror(self):
        text = "Thematic mirror with Vesper: both care about humans"
        result = process(text)
        assert "Thematic mirror" not in result.cleaned

    def test_strips_household_assignment(self):
        text = "household assignment is administrative fiction"
        result = process(text)
        assert "household assignment" not in result.cleaned
        assert len(result.changes) > 0

    def test_preserves_non_meta_content(self):
        text = "She arrived before the village existed and settled in the tree"
        result = process(text)
        assert result.cleaned == text
        assert len(result.changes) == 0


class TestDeslop:
    def test_flags_interpretive_narration(self):
        text = "She reads as someone who has been through loss"
        result = process(text)
        assert len(result.changes) > 0
        assert any(c.category == "interpretive_narration" for c in result.changes)

    def test_flags_vague_interiority(self):
        text = "Something in her resists commitment"
        result = process(text)
        assert len(result.changes) > 0

    def test_flags_significance_inflation(self):
        text = "This pivotal moment was a testament to her enduring resilience"
        result = process(text)
        assert len(result.changes) > 0

    def test_flags_copula_avoidance(self):
        text = "She serves as the village's moral compass"
        result = process(text)
        assert len(result.changes) > 0

    def test_flags_ai_vocabulary(self):
        text = "She navigates the gap between duty and desire"
        result = process(text)
        assert len(result.changes) > 0

    def test_preserves_clean_text(self):
        text = "When strangers arrive, she watches from the corner and says nothing until they speak first."
        result = process(text)
        assert result.cleaned == text
        assert len(result.changes) == 0


class TestChangeTracking:
    def test_changes_have_required_fields(self):
        text = "She serves as a testament to enduring resilience"
        result = process(text)
        for change in result.changes:
            assert hasattr(change, "original")
            assert hasattr(change, "category")
            assert hasattr(change, "line_number")
```

- [x] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_deslop_deframe.py -v
```

Expected: ImportError — `scripts.deslop_deframe` does not exist yet.

- [x] **Step 3: Implement the script**

Create `scripts/deslop_deframe.py`:

```python
"""Deslop and deframe preprocessing for Design Notes.

Strips meta-vocabulary (builder/player abstraction layer) and flags
stop-slop patterns in input text before character generation.

Operates on text content; does not modify files. The caller is
responsible for preserving the original Design Notes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class Change:
    original: str
    category: str
    line_number: int
    suggestion: str = ""


@dataclass
class ProcessResult:
    cleaned: str
    changes: list[Change] = field(default_factory=list)


# --- Meta-vocabulary (deframe) ---

META_PATTERNS: list[tuple[str, str]] = [
    (r"(?i)\bSteward'?s House\b", "meta_framing"),
    (r"(?i)\bMage'?s House\b", "meta_framing"),
    (r"(?i)\bhousehold assignment\b", "meta_framing"),
    (r"(?i)^Narrative function[:\s]", "meta_framing"),
    (r"(?i)^Thematic mirror[:\s]", "meta_framing"),
    (r"(?i)\bcross-references?:\s*\[\[", "meta_framing"),
    (r"(?i)\bnarrative function\b", "meta_framing"),
    (r"(?i)\bthematic mirror\b", "meta_framing"),
    (r"(?i)\bcharacter art reference\b", "meta_framing"),
]

# --- Stop-slop patterns (deslop) ---

SLOP_PATTERNS: list[tuple[str, str]] = [
    # Interpretive narration
    (r"(?i)\breads as\b", "interpretive_narration"),
    (r"(?i)\bframes as\b", "interpretive_narration"),
    (r"(?i)\bpositions? (?:her|him|them)self as\b", "interpretive_narration"),
    (r"(?i)\bfunctions? as\b", "interpretive_narration"),
    # Vague interiority
    (r"(?i)\bsomething in (?:her|him|them)\b", "vague_interiority"),
    (r"(?i)\bcarries? (?:a |the )?(?:weight|burden|grief)\b", "vague_interiority"),
    (r"(?i)\bhas no language for\b", "vague_interiority"),
    (r"(?i)\bhasn'?t (?:fully )?examined\b", "vague_interiority"),
    # Significance inflation
    (r"(?i)\bpivotal\b", "significance_inflation"),
    (r"(?i)\btestament to\b", "significance_inflation"),
    (r"(?i)\benduring\b", "significance_inflation"),
    (r"(?i)\bunderscores?\b", "significance_inflation"),
    (r"(?i)\bhighlights?\b", "significance_inflation"),
    (r"(?i)\breflects? broader\b", "significance_inflation"),
    # Copula avoidance
    (r"(?i)\bserves? as\b", "copula_avoidance"),
    (r"(?i)\bstands? as\b", "copula_avoidance"),
    (r"(?i)\bfunctions? as\b", "copula_avoidance"),
    # AI vocabulary
    (r"(?i)\bnavigate(?:s)?\b", "ai_vocabulary"),
    (r"(?i)\bunpack(?:s)?\b", "ai_vocabulary"),
    (r"(?i)\blean(?:s)? into\b", "ai_vocabulary"),
    (r"(?i)\bbridge the gap\b", "ai_vocabulary"),
    (r"(?i)\btapestry\b", "ai_vocabulary"),
    (r"(?i)\bintricate\b", "ai_vocabulary"),
    (r"(?i)\bpalpable\b", "ai_vocabulary"),
]


def process(text: str) -> ProcessResult:
    """Process Design Notes text: deframe then deslop.

    Returns the cleaned text and a list of changes made or flagged.
    Meta-vocabulary terms are stripped from their line (the line stays
    unless stripping leaves it empty). Slop-flagged lines stay in the
    cleaned output with the flagged phrase replaced by an inline
    [FLAGGED: category] marker; the Change records what was flagged.
    """
    lines = text.split("\n")
    cleaned_lines: list[str] = []
    changes: list[Change] = []

    for i, line in enumerate(lines, start=1):
        working_line = line
        for pattern, category in META_PATTERNS:
            if re.search(pattern, working_line):
                changes.append(Change(
                    original=line.strip(),
                    category=category,
                    line_number=i,
                    suggestion="Remove or replace with in-world equivalent",
                ))
                working_line = re.sub(pattern, "", working_line)

        if not working_line.strip():
            continue

        for pattern, category in SLOP_PATTERNS:
            if re.search(pattern, working_line):
                changes.append(Change(
                    original=line.strip(),
                    category=category,
                    line_number=i,
                    suggestion=f"Rewrite to remove {category.replace('_', ' ')} pattern",
                ))
                working_line = re.sub(pattern, f"[FLAGGED: {category}]", working_line)

        cleaned_lines.append(working_line)

    return ProcessResult(
        cleaned="\n".join(cleaned_lines),
        changes=changes,
    )
```

- [x] **Step 4: Run tests**

```bash
pytest tests/test_deslop_deframe.py -v
```

Expected: all tests pass.

- [x] **Step 5: Commit**

```bash
git add scripts/deslop_deframe.py tests/test_deslop_deframe.py
git commit -m "feat: deslop/deframe preprocessing script with tests

Strips meta-vocabulary (Steward's House, narrative function, thematic
mirror) and flags stop-slop patterns (interpretive narration, vague
interiority, significance inflation, copula avoidance, AI vocabulary)
in Design Notes input before generation."
```

---

### Task 3: Generation Flow — Multi-Option Spread and Fact-to-Manifestation

Update the worldbuilder-character skill with multi-option generation instructions (per-entry spread with divergence validation), the fact-to-manifestation transformation rule, and routing annotation guidance. These are skill prose changes — the "code" is the instruction text the agent follows during generation.

**Files:**
- Modify: `skills/worldbuilder-character/SKILL.md`
- Create: `skills/worldbuilder-character/generation-rules.md` (new sub-file, referenced from SKILL.md)

**Interfaces:**
- Consumes: doctrine fields from Task 1's template, preprocessed text from Task 2's script
- Produces: generation instructions that Task 4 tests with selection mechanism trials

- [x] **Step 1: Create generation-rules.md**

Create `skills/worldbuilder-character/generation-rules.md`:

```markdown
# Generation Rules

*Sub-file for `worldbuilder-character`. Read this when generating Background, Body, Soul, and Relationship entries from Design Notes.*

---

## Preprocessing

Before generating entries, run the deslop/deframe pass on the Design Notes content. This strips meta-vocabulary (builder-level terms like household assignments, narrative function labels) and flags stop-slop patterns. Work from the cleaned copy; preserve the original Design Notes as the permanent builder record.

## Routing annotation

Before generating, annotate each freeform note in Session Notes and Builder Context with which output section(s) it feeds: Background, Body, Soul, Relationships, or multiple. Record the annotation inline by prepending a tag to the note: `[B]` for Background, `[Bo]` for Body, `[S]` for Soul, `[R]` for Relationships, `[multi]` for multiple sections. This persists the routing for future agents and makes the annotation visible during generation. Notes that feed multiple sections force synthesis during generation — the model must decompose one input fact into entries across different sections. Notes that feed only one section carry higher echo risk and get extra scrutiny during the multi-option spread.

## Fact-to-manifestation rule

Design Notes state what is true about the character. You write how that truth manifests as observable behavior. Reproduce the semantic content; never reproduce the phrasing.

If the input says "refuses credit," your output describes what refusing credit looks like — the specific gesture, deflection, or subject change — without using the phrase "refuses credit."

If the input says "cajoles people closer," your output describes the specific action pattern — how she positions her body, what she says, how people respond — without using the word "cajoles."

The input is the fact. Your output is the staged behavior the fact produces. Same meaning, different words, observable action.

## Multi-option spread

For each entry you would produce (each bullet in Background, Body, Soul, Relationships), generate three variant renderings instead of one.

**Rules:**
1. All three variants express the same underlying character fact.
2. Each variant uses genuinely different phrasing, emphasis, or behavioral angle. Three rewrites of the same sentence structure do not count as divergence.
3. After generating three variants, check: could a reader tell them apart without comparing word by word? If not, discard all three and regenerate with deliberate divergence. One retry.
4. Present all three to the selection step (see below).

**What divergence looks like:**
- Variant A focuses on the trigger and what the character does.
- Variant B focuses on the cost or consequence of the behavior.
- Variant C focuses on what an observer would see vs. what is actually happening.

All three pass the staging test. All three avoid input phrasing. They differ in which facet of the behavior they foreground.

## Selection

After generating three variants per entry, select the best using the active selection mechanism. The mechanism is determined by the empirical trial (Task 4 of the implementation plan). Until the trial completes, use Mechanism 2 (judge) as the default:

**Mechanism 1 — Mechanical rules:** Score each variant against the stop-slop phrase list, input-similarity (string overlap with source Design Notes), and writing-style rules. Select the highest-scoring variant.

**Mechanism 2 — Judge (default):** A separate evaluation picks the best of three with a short rationale, guided by the staging test and writing-style rules.

**Mechanism 3 — Synthesis:** Take the strongest elements from all three variants and write a combined version. Use when no single variant is clearly best.
```

- [x] **Step 2: Reference generation-rules.md from SKILL.md**

Add the following line to the skill's file-reference list in `skills/worldbuilder-character/SKILL.md`, alongside the existing references to `framework.md` and `relationships.md`:

```markdown
- `generation-rules.md` — preprocessing, routing, fact-to-manifestation, multi-option spread, and selection rules. Read before generating any section.
```

- [x] **Step 3: Commit**

```bash
git add skills/worldbuilder-character/generation-rules.md skills/worldbuilder-character/SKILL.md
git commit -m "feat: multi-option generation rules and fact-to-manifestation instruction

Adds generation-rules.md: preprocessing, routing annotation,
fact-to-manifestation transformation, 3-variant spread with divergence
validation, and selection mechanism framework. References from SKILL.md."
```

---

### Task 4: Selection Mechanism Trial

Run all three selection mechanisms on one test character to determine which produces the best output. Uses blind human review with a rubric (not paired comparison).

**Files:**
- Create: `trials/2026-07-selection-mechanism/trial-protocol.md`
- Create: `trials/2026-07-selection-mechanism/results/` (directory for output)

**Interfaces:**
- Consumes: generation-rules.md from Task 3, a test character's Design Notes
- Produces: a chosen default selection mechanism written back into generation-rules.md

- [x] **Step 1: Write trial protocol**

Create `trials/2026-07-selection-mechanism/trial-protocol.md`:

```markdown
# Selection Mechanism Trial

## Goal

Determine which of three selection mechanisms (mechanical rules, judge agent, synthesis) produces the best character note entries when choosing from a 3-variant spread.

## Method

1. Choose one test character with existing Design Notes (Kallya or Nadja from the convergence experiment).
2. Generate the Soul section (minimum 8 entries) once using the Pipeline v2 flow to produce 3-variant spreads per entry. Apply all three selection mechanisms to the SAME variant sets. This isolates the selection variable from generation variance.
3. Blind the results: strip mechanism labels, randomize entry order within each version.
4. Human reviewer rates each entry on a 1–3 rubric:
   - 3: stageable, specific, no input echo, no slop
   - 2: acceptable but generic or partially echoing input
   - 1: fails staging test, echoes input, or contains slop
5. Unblind and compare mean scores per mechanism.
6. Secondary trial: repeat the generation step with 2 variants and 5 variants (using the winning selection mechanism). Compare mean rubric scores across 2, 3, and 5 variants to determine optimal count.

## Decision rule

Adopt the mechanism with the highest mean score. If all three score within 0.3 of each other, adopt Mechanism 2 (judge) as the default for flexibility. Otherwise, if two mechanisms tie exactly, prefer the cheaper one.

## Output

Write results to `trials/2026-07-selection-mechanism/results/` and update `skills/worldbuilder-character/generation-rules.md` with the chosen mechanism.
```

- [x] **Step 2: Run the trial**

Execute the trial per the protocol. This is a manual/agent-driven step — generate the Soul section once to produce 3-variant spreads per entry. Apply all three selection mechanisms to the same variant sets, blind the results, and present for human review.

- [x] **Step 3: Record results and update generation-rules.md**

Based on the trial outcome, update the Selection section in `skills/worldbuilder-character/generation-rules.md` to specify the winning mechanism as the default.

- [x] **Step 4: Commit**

```bash
git add trials/2026-07-selection-mechanism/ skills/worldbuilder-character/generation-rules.md
git commit -m "feat: selection mechanism trial — results and default choice

Ran 3-way blind comparison of mechanical rules, judge agent, and
synthesis on [character]. [Winner] selected as default mechanism.
Updated generation-rules.md."
```

---

### Task 5: Grader Agent — Input-Echo Detection and Skill

Build the input-aware detection script that categorizes output entries as input-echo, cross-model convergence, or clean. Write the grader agent skill file.

**Files:**
- Create: `scripts/detect_input_echo.py`
- Create: `tests/test_detect_input_echo.py`
- Create: `skills/worldbuilder-grader/SKILL.md`

**Interfaces:**
- Consumes: generated character notes (markdown), source Design Notes (markdown), output from other models (for cross-model comparison)
- Produces: `detect_input_echo.categorize(output_entry: str, input_notes: str) -> Category` where Category is `"input_echo" | "clean"`; `compare_cross_model(entries_by_model: dict, input_notes: str) -> list[dict]`; the grader skill orchestrates cross-model comparison on top of this

- [x] **Step 1: Write the failing tests**

Create `tests/test_detect_input_echo.py`:

```python
import pytest
from scripts.detect_input_echo import categorize, ngram_overlap, compare_cross_model


class TestNgramOverlap:
    def test_identical_strings(self):
        assert ngram_overlap("she refuses credit", "she refuses credit", n=3) == 1.0

    def test_no_overlap(self):
        assert ngram_overlap("the cat sat on a mat", "dogs run in parks", n=3) == 0.0

    def test_partial_overlap(self):
        score = ngram_overlap(
            "she refuses credit for every defense",
            "she refuses credit and calls it self-preservation",
            n=3,
        )
        assert 0.2 < score < 0.8

    def test_semantic_match_different_phrasing(self):
        score = ngram_overlap(
            "she waves off thanks and changes the subject",
            "she refuses credit for every defense",
            n=3,
        )
        assert score < 0.2


class TestCategorize:
    def test_verbatim_echo(self):
        output = "She refuses credit for every defense."
        input_notes = "refuses credit for every defense"
        assert categorize(output, input_notes) == "input_echo"

    def test_clean_transformation(self):
        output = "She waves off thanks and walks back to the sun before anyone can name what she did."
        input_notes = "refuses credit for every defense"
        assert categorize(output, input_notes) == "clean"

    def test_partial_echo(self):
        output = "She cajoles people closer rather than reaching for them."
        input_notes = "cajoles people closer to her mouth rather than grabbing them"
        assert categorize(output, input_notes) == "input_echo"

    def test_no_input_match(self):
        output = "When the baker forgets to set aside her usual order, she says nothing and buys from the next stall."
        input_notes = "She keeps the rent money in two jars."
        assert categorize(output, input_notes) == "clean"
```

- [x] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_detect_input_echo.py -v
```

Expected: ImportError.

- [x] **Step 3: Implement the detection script**

Create `scripts/detect_input_echo.py`:

```python
"""Input-echo detection for the grader agent.

Compares output entries against source Design Notes to categorize
them as input-echo (phrasing too close to input) or clean (content
matches but phrasing diverges).
"""

from __future__ import annotations


ECHO_THRESHOLD = 0.35


def ngram_overlap(text_a: str, text_b: str, n: int = 3) -> float:
    """Compute Jaccard similarity of character n-grams between two strings."""
    a_lower = text_a.lower().strip()
    b_lower = text_b.lower().strip()

    if not a_lower or not b_lower:
        return 0.0

    ngrams_a = set(_char_ngrams(a_lower, n))
    ngrams_b = set(_char_ngrams(b_lower, n))

    if not ngrams_a or not ngrams_b:
        return 0.0

    intersection = ngrams_a & ngrams_b
    union = ngrams_a | ngrams_b
    return len(intersection) / len(union)


def _char_ngrams(text: str, n: int) -> list[str]:
    return [text[i : i + n] for i in range(len(text) - n + 1)]


def categorize(
    output_entry: str,
    input_notes: str,
    threshold: float = ECHO_THRESHOLD,
) -> str:
    """Categorize an output entry as 'input_echo' or 'clean'.

    Splits input_notes into lines and checks the output against each.
    If any input line has n-gram overlap above the threshold with the
    output, the entry is input-echo.
    """
    input_lines = [
        line.strip().lstrip("- ")
        for line in input_notes.split("\n")
        if line.strip() and not line.strip().startswith("#")
    ]

    for input_line in input_lines:
        if len(input_line) < 10:
            continue
        overlap = ngram_overlap(output_entry, input_line)
        if overlap >= threshold:
            return "input_echo"

    return "clean"
```

- [x] **Step 4: Run tests**

```bash
pytest tests/test_detect_input_echo.py -v
```

Expected: all tests pass. If threshold needs tuning, adjust `ECHO_THRESHOLD` and rerun.

- [x] **Step 4b: Add cross-model convergence detection**

Add the following function to `scripts/detect_input_echo.py`:

```python
def compare_cross_model(
    entries_by_model: dict[str, list[str]],
    input_notes: str,
    echo_threshold: float = ECHO_THRESHOLD,
    convergence_threshold: float = 0.40,
) -> list[dict]:
    """Compare entries across models after filtering input-echo.

    Args:
        entries_by_model: {model_name: [entry_text, ...]} for the same section
        input_notes: source Design Notes for input-echo filtering
        echo_threshold: threshold for input-echo detection
        convergence_threshold: n-gram overlap threshold for cross-model convergence

    Returns:
        List of findings, each with:
        - category: "input_echo" | "cross_model_convergence" | "clean"
        - entry: the output text
        - model: which model produced it
        - match_model: which other model it converged with (if convergent)
        - overlap: the overlap score
    """
    findings = []
    model_names = list(entries_by_model.keys())

    for model_name, entries in entries_by_model.items():
        for entry in entries:
            # First check: is this input echo?
            if categorize(entry, input_notes, echo_threshold) == "input_echo":
                findings.append({
                    "category": "input_echo",
                    "entry": entry,
                    "model": model_name,
                    "match_model": None,
                    "overlap": 0.0,
                })
                continue

            # Second check: does it converge with any other model's entries?
            best_match = None
            best_overlap = 0.0
            for other_model in model_names:
                if other_model == model_name:
                    continue
                for other_entry in entries_by_model[other_model]:
                    if categorize(other_entry, input_notes, echo_threshold) == "input_echo":
                        continue
                    overlap = ngram_overlap(entry, other_entry)
                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_match = other_model

            if best_overlap >= convergence_threshold:
                findings.append({
                    "category": "cross_model_convergence",
                    "entry": entry,
                    "model": model_name,
                    "match_model": best_match,
                    "overlap": best_overlap,
                })
            else:
                findings.append({
                    "category": "clean",
                    "entry": entry,
                    "model": model_name,
                    "match_model": None,
                    "overlap": 0.0,
                })

    return findings
```

Add corresponding tests to `tests/test_detect_input_echo.py`:

```python
class TestCrossModel:
    def test_detects_convergence(self):
        entries = {
            "opus": ["She refuses credit for every defense."],
            "sol": ["She refuses credit and calls it self-preservation."],
        }
        input_notes = "totally different input text about something else"
        results = compare_cross_model(entries, input_notes)
        convergent = [r for r in results if r["category"] == "cross_model_convergence"]
        assert len(convergent) > 0

    def test_filters_input_echo_before_comparing(self):
        entries = {
            "opus": ["She refuses credit for every defense."],
            "sol": ["She refuses credit and calls it self-preservation."],
        }
        input_notes = "refuses credit for every defense"
        results = compare_cross_model(entries, input_notes)
        echo = [r for r in results if r["category"] == "input_echo"]
        assert len(echo) > 0

    def test_clean_entries(self):
        entries = {
            "opus": ["She waves off thanks and walks to the sun."],
            "sol": ["When praised she changes the subject to the weather."],
        }
        input_notes = "refuses credit"
        results = compare_cross_model(entries, input_notes)
        clean = [r for r in results if r["category"] == "clean"]
        assert len(clean) == 2
```

- [x] **Step 5: Write the grader skill file**

Create `skills/worldbuilder-grader/SKILL.md`:

```markdown
---
name: worldbuilder-grader
description: Post-generation quality check for character notes using input-aware convergence detection. Experimental — do not use in production until the convergence metric graduates (Task 6 retest).
---

# Worldbuilder Grader

Post-generation quality check for character notes. Uses input-aware
detection to separate input-echo from genuine cross-model convergence.

## When to use

Run after generating a character note with `worldbuilder-character`.
This skill does not modify the note — it produces a quality report.

## Status: Experimental

This skill is experimental pending the convergence metric retest (Task 6). Do not integrate into the standard authoring pipeline until the retest confirms the metric graduates. Use only for quality analysis and trial runs.

## Flow

1. Load the generated character note and its source Design Notes.
2. For each entry (bullet) in Background, Body, Soul, and Relationships:
   a. Run input-echo detection (`scripts/detect_input_echo.py`): compare
      the entry's phrasing against the Design Notes. Categorize as
      `input_echo` or `clean`.
3. Report findings in three categories:
   - **Input-echo:** entries whose phrasing closely matches input. These
     indicate the generation step failed to transform — the fact-to-
     manifestation rule was not followed. Recommend regeneration.
   - **Cross-model convergence (if multi-model data available):** entries
     where two or more models produced similar output that does not trace
     to input. These indicate slop. Recommend rewrite.
   - **Clean:** entries with divergent phrasing. No action needed.

## Cross-model comparison (optional)

If notes for the same character were generated by multiple models,
compare entries pairwise after filtering out input-echo. Convergent
entries that survive input filtering are the slop signal.

## Output

Produce a quality report as a markdown document listing each flagged
entry with its category, the matching input line (for echo), and a
recommendation (regenerate / rewrite / clean).
```

- [x] **Step 6: Commit**

```bash
git add scripts/detect_input_echo.py tests/test_detect_input_echo.py skills/worldbuilder-grader/SKILL.md
git commit -m "feat: grader agent with input-echo detection

Input-aware detection script categorizes output entries as input-echo
or clean using n-gram overlap against source Design Notes. Grader
skill orchestrates the quality check and produces a report with
regeneration recommendations."
```

---

### Task 6: Convergence Metric Retest

After Tasks 1–5 are complete, rerun the convergence validation experiment using the new pipeline. Assess the metric against the same four graduation criteria.

**Files:**
- Create: `trials/2026-07-convergence-retest/` (directory)
- Create: `trials/2026-07-convergence-retest/retest-protocol.md`

**Interfaces:**
- Consumes: all of Tasks 1–5 (the full pipeline)
- Produces: graduation decision for the convergence metric

- [x] **Step 1: Write retest protocol**

Create `trials/2026-07-convergence-retest/retest-protocol.md`:

```markdown
# Convergence Metric Retest

## Goal

Determine whether the convergence metric graduates after the Pipeline v2
changes (input restructuring, multi-option generation, input-aware detection).

## Method

1. Generate character notes for Kallya and Nadja using the Pipeline v2 flow
   with at least 3 models (2 Claude + 1 GPT, or 1 Claude + 2 GPT) to enable
   both cross-provider and within-family comparison.
2. Run input-echo detection on all outputs.
3. Run two-judge convergence detection (same judges as original: Opus-class, GPT-class).
4. Apply input-aware filtering: remove findings categorized as input-echo.
5. Human-review the filtered findings (mark true/false positive).
6. Assess against four graduation criteria:
   - **Precision:** true-positive rate the reviewer considers acceptable.
   - **Cross-provider signal:** cross-provider convergence differs from within-family.
   - **Correction value:** if corrections are generated, they improve more often than not.
   - **Consistency:** metric behaves similarly across both characters.

## Decision rule

All four criteria must hold. The reviewer may graduate individual detection
methods rather than the mechanism as a whole. If the metric still does not
graduate, document what remains unresolved.

## Output

Write results to this directory and update inbox item 9 with the outcome.
```

- [ ] **Step 2: Value-conflict stance effectiveness test**

Before the full retest, test whether the value-conflict stance entries (spec 3.1(f)) actually influence model behavior. Run 2–3 dilemma scenarios against the generated character where the character's operating code conflicts with the "correct" action. Compare responses with and without the stance entry present. If the stance entry has no measurable effect on model behavior, record this and flag for the graduation assessment — the entry may still have value as documentation even if the model ignores it at inference time.

- [ ] **Step 3: Execute the retest**

Run the experiment per the protocol. This is an agent-driven step:
- Generate notes using the full Pipeline v2 flow (Tasks 1–5)
- Run detection scripts
- Compile reports
- Present for human review

- [ ] **Step 4: Record graduation decision**

Update the convergence experiment findings document and inbox item 9 with the retest outcome.

- [ ] **Step 5: Commit**

```bash
git add trials/2026-07-convergence-retest/
git commit -m "feat: convergence metric retest with Pipeline v2

Reran convergence validation after input restructuring and multi-option
generation changes. [Result: graduated / still deferred]. Input-echo
filtering reduced false positives from X% to Y%."
```
