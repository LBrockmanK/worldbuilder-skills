---
type: plan
title: Additive-Doctrine Discriminator Trial Implementation
description: 'Implementation plan for the discriminator trial: prompt assembly, API-driven
  generation, detection and reporting. 3 tasks.'
tags:
- complete
date: 2026-08-09
timestamp: 2026-08-09T23:21Z
resources:
- "[[2026-08-09-additive-doctrine-discriminator-trial]]"
- "[[2026-08-09-additive-doctrine-discriminator-trial-implementation-research]]"
---

# Additive-Doctrine Discriminator Trial Implementation

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).

**Goal:** Build a trial runner that generates character notes under three doctrine arms, measures input-echo and within-model divergence, and reports whether additive doctrine measurably changes model behavior.

**Architecture:** A single Python script (`run_trial.py`) with two independent phases: generation (Claude API calls to produce 36 character notes) and detection (trigram-based metrics from the existing `scripts/detect_input_echo.py`). A `--detect-only` flag allows rerunning analysis over existing outputs without regenerating.

**Tech Stack:** Python 3.10+, `anthropic` SDK for generation, stdlib only for detection (imports from existing `scripts/detect_input_echo.py`).

**Research dossier:** [Implementation Research](../research/2026-08-09-additive-doctrine-discriminator-trial-implementation-research.md)

## Global Constraints

- Model IDs pinned: `claude-sonnet-5`, `claude-opus-4-6` — no aliases.
- Temperature and system prompt held constant across all cells (values pinned in Task 1).
- Entry extraction: split by `##` headings, exclude frontmatter and H1 title, drop empty sections.
- Aggregation: per-run entry means averaged equally to cell mean; within-model divergence uses full note text.
- Output naming: `{character}-{doctrine}-{model_short}-run{n}.md` where model_short strips the `claude-` prefix (e.g., `sonnet-5`, `opus-4-6`).
- No blinding — metrics are mechanical.

---

### Task 1: Trial directory, prompt assembly, and runner skeleton

**Files:**
- Create: `trials/2026-08-additive-discriminator/run_trial.py`
- Create: `trials/2026-08-additive-discriminator/README.md`
- Read: `trials/2026-07-writing-doctrine/src/base.md`
- Read: `trials/2026-07-writing-doctrine/src/doctrine-additive.md`
- Read: `trials/2026-07-writing-doctrine/src/style-stopslop.md`
- Read: `trials/2026-07-convergence-retest/nadja-cleaned.md`
- Read: `trials/2026-07-convergence-retest/kallya-cleaned.md`

**Interfaces:**
- Consumes: source markdown files listed above (read at runtime).
- Produces: `assemble_prompt(character: str, doctrine: str) -> str` — returns the full prompt string for one generation. `MATRIX: list[dict]` — the 12-cell trial matrix (character × doctrine × model). `parse_args() -> argparse.Namespace` — CLI with `--detect-only`, `--dry-run`, `--out-dir` flags.

- [ ] **Step 1: Create the trial directory**

```bash
mkdir -p trials/2026-08-additive-discriminator/out
```

Expected: directory `trials/2026-08-additive-discriminator/out/` created. Verify:

```bash
ls trials/2026-08-additive-discriminator/
```

Expected output includes `out/`.

- [ ] **Step 2: Write the test for prompt assembly**

Create `trials/2026-08-additive-discriminator/test_runner.py`:

```python
"""Tests for the discriminator trial runner."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from run_trial import assemble_prompt, MATRIX, ARMS


def test_assemble_prompt_current_arm():
    """Current arm: base instructions + design notes, no overlay."""
    prompt = assemble_prompt("nadja", "current")
    assert "Character Note Instructions" in prompt
    assert "Nadja" in prompt
    assert "Additional Construction Rules" not in prompt
    assert "Cut Filler" not in prompt


def test_assemble_prompt_additive_arm():
    """Additive arm: base + additive doctrine overlay + design notes."""
    prompt = assemble_prompt("nadja", "additive")
    assert "Character Note Instructions" in prompt
    assert "Nadja" in prompt
    assert "Additional Construction Rules" in prompt
    assert "Banned Trait Words" in prompt
    assert "Cut Filler" not in prompt


def test_assemble_prompt_stopslop_arm():
    """Stopslop arm: base + stopslop style overlay + design notes."""
    prompt = assemble_prompt("nadja", "stopslop")
    assert "Character Note Instructions" in prompt
    assert "Nadja" in prompt
    assert "Cut Filler" in prompt
    assert "Additional Construction Rules" not in prompt


def test_assemble_prompt_kallya():
    """Kallya character gets Kallya design notes."""
    prompt = assemble_prompt("kallya", "current")
    assert "Kallya" in prompt


def test_matrix_has_12_cells():
    """3 arms × 2 characters × 2 models = 12 cells."""
    assert len(MATRIX) == 12


def test_matrix_cell_keys():
    """Every cell has the required keys."""
    for cell in MATRIX:
        assert "character" in cell
        assert "doctrine" in cell
        assert "model" in cell


def test_arms_are_three():
    """Three doctrine arms defined."""
    assert set(ARMS) == {"current", "additive", "stopslop"}
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py -v
```

Expected: FAIL — `run_trial` module not found.

- [ ] **Step 4: Write the runner skeleton with prompt assembly**

Create `trials/2026-08-additive-discriminator/run_trial.py`:

```python
"""Additive-doctrine discriminator trial runner.

Two phases:
1. Generation: Claude API calls to produce character notes.
2. Detection: input-echo and within-model divergence metrics.

Usage:
    python run_trial.py                  # full run (generate + detect)
    python run_trial.py --detect-only    # rerun detection on existing outputs
    python run_trial.py --dry-run        # print prompts, no API calls
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

TRIAL_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(TRIAL_DIR, "..", ".."))
OUT_DIR = os.path.join(TRIAL_DIR, "out")

sys.path.insert(0, PROJECT_ROOT)
from scripts.detect_input_echo import categorize, ngram_overlap

# --- Constants ---

CHARACTERS = ["nadja", "kallya"]
ARMS = ["current", "additive", "stopslop"]
MODELS = ["claude-sonnet-5", "claude-opus-4-6"]
RUNS_PER_CELL = 3
TEMPERATURE = 1.0
MAX_TOKENS = 4096

# --- Source paths ---

SRC_DIR = os.path.join(PROJECT_ROOT, "trials", "2026-07-writing-doctrine", "src")
RETEST_DIR = os.path.join(PROJECT_ROOT, "trials", "2026-07-convergence-retest")

DESIGN_NOTES = {
    "nadja": os.path.join(RETEST_DIR, "nadja-cleaned.md"),
    "kallya": os.path.join(RETEST_DIR, "kallya-cleaned.md"),
}
BASE_PATH = os.path.join(SRC_DIR, "base.md")
OVERLAY_PATHS = {
    "current": None,
    "additive": os.path.join(SRC_DIR, "doctrine-additive.md"),
    "stopslop": os.path.join(SRC_DIR, "style-stopslop.md"),
}

# --- Trial matrix ---

MATRIX = [
    {"character": char, "doctrine": arm, "model": model}
    for char in CHARACTERS
    for arm in ARMS
    for model in MODELS
]


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def assemble_prompt(character: str, doctrine: str) -> str:
    """Assemble the full prompt for one generation.

    Structure: base instructions + doctrine/style overlay + design notes.
    """
    parts = [_read(BASE_PATH)]

    overlay_path = OVERLAY_PATHS[doctrine]
    if overlay_path is not None:
        parts.append(_read(overlay_path))

    parts.append("# Design Notes\n\n" + _read(DESIGN_NOTES[character]))

    return "\n\n".join(parts)


def output_path(character: str, doctrine: str, model: str, run: int) -> str:
    """Return the output file path for one generation."""
    model_short = model.replace("claude-", "")
    return os.path.join(OUT_DIR, f"{character}-{doctrine}-{model_short}-run{run}.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Additive-doctrine discriminator trial")
    parser.add_argument("--detect-only", action="store_true",
                        help="Skip generation, run detection on existing outputs")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print prompts and exit, no API calls")
    parser.add_argument("--out-dir", default=OUT_DIR,
                        help="Output directory for generated notes")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.dry_run:
        for cell in MATRIX:
            prompt = assemble_prompt(cell["character"], cell["doctrine"])
            print(f"--- {cell['character']}/{cell['doctrine']}/{cell['model']} ---")
            print(f"Prompt length: {len(prompt)} chars")
            print(prompt[:200] + "...\n")
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py -v
```

Expected: all 7 tests PASS.

- [ ] **Step 6: Write README.md**

Create `trials/2026-08-additive-discriminator/README.md`:

```markdown
# Additive-Doctrine Discriminator Trial

Measures whether the additive doctrine measurably changes model
behavior using two graduated detection components: input-echo
detection and within-model divergence.

## Trial design

- **Arms:** current (baseline), additive (doctrine overlay), stopslop
  (style overlay as reference delta)
- **Characters:** Nadja, Kallya
- **Models:** claude-sonnet-5, claude-opus-4-6
- **Runs:** 3 per cell
- **Total generations:** 36

## Usage

Full run (generate + detect):

    python run_trial.py

Detection only (rerun on existing outputs):

    python run_trial.py --detect-only

Dry run (print prompts, no API calls):

    python run_trial.py --dry-run

## Requirements

    pip install anthropic

Set `ANTHROPIC_API_KEY` in environment.

## Outputs

- `out/` — 36 generated character notes
- `report.json` — structured metrics
- `summary.md` — human-readable comparison report

## Spec

See `.claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md`.
```

- [ ] **Step 7: Verify dry-run works end to end**

```bash
cd trials/2026-08-additive-discriminator && python run_trial.py --dry-run
```

Expected: prints 12 prompt previews (one per cell) with character/doctrine/model labels and prompt lengths. No API calls.

- [ ] **Step 8: Commit**

```bash
git add trials/2026-08-additive-discriminator/run_trial.py \
       trials/2026-08-additive-discriminator/test_runner.py \
       trials/2026-08-additive-discriminator/README.md
git commit -m "feat: add discriminator trial skeleton with prompt assembly"
```

Expected: commit created with the listed files. Verify with `git log -1 --stat`.

---

### Task 2: Generation phase (Claude API)

**Files:**
- Modify: `trials/2026-08-additive-discriminator/run_trial.py`
- Modify: `trials/2026-08-additive-discriminator/test_runner.py`

**Interfaces:**
- Consumes: `assemble_prompt()`, `output_path()`, `MATRIX`, `RUNS_PER_CELL`, `TEMPERATURE`, `MAX_TOKENS` from Task 1.
- Produces: `generate_all(matrix, runs, out_dir, dry_run) -> dict[str, str]` — runs all generations and saves outputs, returns `{output_path: content}`. 36 markdown files in `out/`.

- [ ] **Step 1: Write the test for the generation function**

Add to `test_runner.py`:

```python
from unittest.mock import patch, MagicMock
from run_trial import generate_one, generate_all, MATRIX, RUNS_PER_CELL


def test_generate_one_calls_api():
    """generate_one calls anthropic with correct model and prompt."""
    mock_client = MagicMock()
    mock_client.messages.create.return_value = MagicMock(
        content=[MagicMock(text="# Generated Note\n\nContent here.")]
    )

    result = generate_one(
        mock_client, "claude-sonnet-5",
        "test prompt", max_tokens=4096, temperature=1.0,
    )

    mock_client.messages.create.assert_called_once()
    call_kwargs = mock_client.messages.create.call_args[1]
    assert call_kwargs["model"] == "claude-sonnet-5"
    assert call_kwargs["max_tokens"] == 4096
    assert call_kwargs["temperature"] == 1.0
    assert result == "# Generated Note\n\nContent here."


def test_generate_all_creates_files(tmp_path):
    """generate_all creates one file per cell × run."""
    mock_client = MagicMock()
    mock_client.messages.create.return_value = MagicMock(
        content=[MagicMock(text="# Note\n\n## Section\n\nBody.")]
    )

    out_dir = str(tmp_path)
    with patch("run_trial.anthropic") as mock_anthropic:
        mock_anthropic.Anthropic.return_value = mock_client
        results = generate_all(MATRIX, RUNS_PER_CELL, out_dir, dry_run=False)

    assert len(results) == 36
    for path in results:
        assert os.path.exists(path)
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py::test_generate_one_calls_api -v
```

Expected: FAIL — `generate_one` not defined.

- [ ] **Step 3: Implement the generation functions**

Add to `run_trial.py`, after the existing imports:

```python
try:
    import anthropic
except ImportError:
    anthropic = None

SYSTEM_PROMPT = (
    "You are a character designer for an LLM-powered game. "
    "Write a complete character note following the instructions provided. "
    "Output only the character note in markdown, no commentary."
)
```

Add the generation functions after `parse_args()`:

```python
def generate_one(
    client,
    model: str,
    prompt: str,
    max_tokens: int = MAX_TOKENS,
    temperature: float = TEMPERATURE,
) -> str:
    """Generate one character note via the Claude API."""
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def generate_all(
    matrix: list[dict],
    runs: int,
    out_dir: str,
    dry_run: bool = False,
) -> dict[str, str]:
    """Run all generations and save outputs.

    Returns {output_file_path: generated_content}.
    """
    if anthropic is None:
        raise ImportError("pip install anthropic")

    os.makedirs(out_dir, exist_ok=True)
    client = anthropic.Anthropic()
    results = {}
    total = len(matrix) * runs
    done = 0

    for cell in matrix:
        prompt = assemble_prompt(cell["character"], cell["doctrine"])
        for run in range(1, runs + 1):
            done += 1
            path = output_path(cell["character"], cell["doctrine"],
                               cell["model"], run)
            # Use out_dir override if provided
            if out_dir != OUT_DIR:
                fname = os.path.basename(path)
                path = os.path.join(out_dir, fname)

            if dry_run:
                content = f"# Dry Run\n\n{cell}"
            else:
                print(f"[{done}/{total}] {cell['character']}/{cell['doctrine']}"
                      f"/{cell['model']} run {run}...")
                content = generate_one(client, cell["model"], prompt)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            results[path] = content

    return results
```

Update the `__main__` block:

```python
if __name__ == "__main__":
    args = parse_args()
    out_dir = args.out_dir or OUT_DIR

    if args.dry_run:
        for cell in MATRIX:
            prompt = assemble_prompt(cell["character"], cell["doctrine"])
            print(f"--- {cell['character']}/{cell['doctrine']}/{cell['model']} ---")
            print(f"Prompt length: {len(prompt)} chars")
            print(prompt[:200] + "...\n")
        sys.exit(0)

    if not args.detect_only:
        print(f"Generating {len(MATRIX) * RUNS_PER_CELL} notes...")
        generate_all(MATRIX, RUNS_PER_CELL, out_dir)
        print("Generation complete.\n")
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py -v
```

Expected: all tests PASS (9 total — 7 from Task 1 + 2 new).

- [ ] **Step 5: Commit**

```bash
git add trials/2026-08-additive-discriminator/run_trial.py \
       trials/2026-08-additive-discriminator/test_runner.py
git commit -m "feat: add generation phase with Claude API calls"
```

Expected: commit created with the listed files. Verify with `git log -1 --stat`.

---

### Task 3: Detection, aggregation, and reporting

**Files:**
- Modify: `trials/2026-08-additive-discriminator/run_trial.py`
- Modify: `trials/2026-08-additive-discriminator/test_runner.py`

**Interfaces:**
- Consumes: `categorize()` and `ngram_overlap()` from `scripts/detect_input_echo.py`. `output_path()` and `MATRIX` from Task 1. Generated note files from Task 2 (or pre-existing files for `--detect-only`).
- Produces: `extract_entries(note_text: str) -> list[str]` — splits note by ## headings. `run_detection(out_dir: str) -> dict` — computes all metrics and returns the structured report. `write_summary(report: dict, path: str) -> None` — writes the human-readable summary. Files: `report.json`, `summary.md`.

- [ ] **Step 1: Write the test for entry extraction**

Add to `test_runner.py`:

```python
from run_trial import extract_entries


def test_extract_entries_splits_by_h2():
    """Entries are the body text of ## sections."""
    note = (
        "---\ntype: note\n---\n\n"
        "# Character Name\n\n"
        "## Background\n\nShe grew up in a village.\n\n"
        "## Personality\n\nQuiet but fierce.\n\n"
        "## Relationships\n\nHates her brother.\n"
    )
    entries = extract_entries(note)
    assert len(entries) == 3
    assert "grew up" in entries[0]
    assert "Quiet" in entries[1]
    assert "Hates" in entries[2]


def test_extract_entries_skips_empty_sections():
    """Empty sections are dropped."""
    note = "# Title\n\n## Empty\n\n## Content\n\nSome text.\n"
    entries = extract_entries(note)
    assert len(entries) == 1
    assert "Some text" in entries[0]


def test_extract_entries_strips_subheadings():
    """Subheadings (### and below) are stripped from entry text."""
    note = (
        "# Title\n\n"
        "## Section\n\n"
        "### Sub\n\nParagraph one.\n\nParagraph two.\n"
    )
    entries = extract_entries(note)
    assert len(entries) == 1
    assert "Sub" not in entries[0]
    assert "Paragraph one" in entries[0]
    assert "Paragraph two" in entries[0]
```

- [ ] **Step 2: Write the test for detection and aggregation**

Add to `test_runner.py`:

```python
from run_trial import run_detection, write_summary, CHARACTERS, ARMS, MODELS


def test_run_detection_structure(tmp_path):
    """Detection report has the expected structure."""
    # Create synthetic outputs: 3 runs × 12 cells = 36 files
    for char in CHARACTERS:
        for arm in ARMS:
            for model in MODELS:
                model_short = model.replace("claude-", "")
                for run in range(1, 4):
                    fname = f"{char}-{arm}-{model_short}-run{run}.md"
                    path = tmp_path / fname
                    path.write_text(
                        f"# {char.title()}\n\n"
                        f"## Background\n\nUnique content for {arm} "
                        f"run {run} model {model_short}.\n\n"
                        f"## Personality\n\nDifferent text here {run}.\n",
                        encoding="utf-8",
                    )

    report = run_detection(str(tmp_path))

    # Top-level structure
    assert "cells" in report
    assert "summary" in report

    # Should have 12 cells
    assert len(report["cells"]) == 12

    # Each cell has required fields
    for cell_key, cell_data in report["cells"].items():
        assert "echo_mean" in cell_data
        assert "echo_rate" in cell_data
        assert "pairwise_overlap_mean" in cell_data

    # Summary has cross-arm deltas
    summary = report["summary"]
    assert "additive_vs_current" in summary
    assert "stopslop_vs_current" in summary


def test_write_summary_creates_file(tmp_path):
    """write_summary creates a markdown file with required sections."""
    # Minimal report structure
    report = {
        "cells": {
            "nadja/current/sonnet-5": {
                "character": "nadja", "doctrine": "current",
                "model": "sonnet-5", "echo_mean": 0.2,
                "echo_rate": 0.0, "pairwise_overlap_mean": 0.3,
                "runs": [], "pairwise_overlaps": [],
            },
            "nadja/additive/sonnet-5": {
                "character": "nadja", "doctrine": "additive",
                "model": "sonnet-5", "echo_mean": 0.15,
                "echo_rate": 0.0, "pairwise_overlap_mean": 0.25,
                "runs": [], "pairwise_overlaps": [],
            },
        },
        "summary": {
            "additive_vs_current": {
                "echo_delta": -0.05, "divergence_delta": -0.05,
                "echo_consistent_wins": "1/1",
                "pairwise_overlap_consistent_wins": "1/1",
            },
            "stopslop_vs_current": {"echo_delta": 0.0, "divergence_delta": 0.0},
            "arm_means": {
                "current": {"echo": 0.2, "pairwise_overlap": 0.3},
                "additive": {"echo": 0.15, "pairwise_overlap": 0.25},
                "stopslop": {"echo": 0.2, "pairwise_overlap": 0.3},
            },
            "per_model": {},
            "per_character": {},
        },
    }
    out = str(tmp_path / "summary.md")
    write_summary(report, out)
    assert os.path.exists(out)
    content = open(out).read()
    assert "Arm means" in content
    assert "Cross-arm deltas" in content
    assert "Consistency" in content
    assert "Per-cell detail" in content
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py::test_extract_entries_splits_by_h2 -v
```

Expected: FAIL — `extract_entries` not defined.

- [ ] **Step 4: Implement entry extraction**

Add to `run_trial.py`:

```python
def extract_entries(note_text: str) -> list[str]:
    """Split a character note into entries by ## headings.

    Excludes frontmatter, H1 title, and subheadings (### and below).
    Returns body text of each ## section. Empty sections are dropped.
    """
    # Strip frontmatter
    text = note_text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:].strip()

    # Split on ## headings
    sections = re.split(r"^## .+$", text, flags=re.MULTILINE)

    entries = []
    for section in sections[1:]:  # skip everything before first ##
        # Strip subheadings
        body = re.sub(r"^###+ .+$", "", section, flags=re.MULTILINE)
        body = body.strip()
        if body:
            entries.append(body)

    return entries
```

- [ ] **Step 5: Implement detection and aggregation**

Add to `run_trial.py`:

```python
def _cell_key(character: str, doctrine: str, model: str) -> str:
    model_short = model.replace("claude-", "")
    return f"{character}/{doctrine}/{model_short}"


def run_detection(out_dir: str) -> dict:
    """Run input-echo and within-model divergence over all outputs.

    Returns structured report with per-cell metrics and summary.
    """
    cells = {}

    # Validate: all 36 output files must exist
    expected = len(CHARACTERS) * len(ARMS) * len(MODELS) * RUNS_PER_CELL
    found = 0
    for char in CHARACTERS:
        for arm in ARMS:
            for model in MODELS:
                model_short = model.replace("claude-", "")
                for run in range(1, RUNS_PER_CELL + 1):
                    fname = f"{char}-{arm}-{model_short}-run{run}.md"
                    if os.path.exists(os.path.join(out_dir, fname)):
                        found += 1
    if found < expected:
        raise FileNotFoundError(
            f"Expected {expected} output files, found {found}. "
            f"Run generation first or check --out-dir."
        )

    for char in CHARACTERS:
        input_notes = _read(DESIGN_NOTES[char])

        for arm in ARMS:
            for model in MODELS:
                model_short = model.replace("claude-", "")
                key = _cell_key(char, arm, model)

                # Collect runs
                run_texts = []
                run_entry_overlaps = []

                for run in range(1, RUNS_PER_CELL + 1):
                    fname = f"{char}-{arm}-{model_short}-run{run}.md"
                    fpath = os.path.join(out_dir, fname)

                    text = _read(fpath)
                    run_texts.append(text)

                    # Input-echo per entry
                    entries = extract_entries(text)
                    if not entries:
                        raise ValueError(
                            f"No entries extracted from {fpath}. "
                            f"Check note format (needs ## headings)."
                        )
                    overlaps = []
                    for entry in entries:
                        result = categorize(entry, input_notes)
                        overlaps.append(result["overlap"])

                    run_mean = sum(overlaps) / len(overlaps) if overlaps else 0.0
                    run_entry_overlaps.append({
                        "run": run,
                        "mean_overlap": run_mean,
                        "echo_count": sum(
                            1 for o in overlaps if o >= 0.35
                        ),
                        "total_entries": len(entries),
                    })

                # Cell-level echo aggregation
                run_means = [r["mean_overlap"] for r in run_entry_overlaps]
                cell_echo_mean = (
                    sum(run_means) / len(run_means) if run_means else 0.0
                )
                total_entries = sum(r["total_entries"] for r in run_entry_overlaps)
                total_echo = sum(r["echo_count"] for r in run_entry_overlaps)
                cell_echo_rate = (
                    total_echo / total_entries if total_entries > 0 else 0.0
                )

                # Within-model divergence: pairwise on full note text
                pairwise_overlaps = []
                for i in range(len(run_texts)):
                    for j in range(i + 1, len(run_texts)):
                        pairwise_overlaps.append(
                            ngram_overlap(run_texts[i], run_texts[j])
                        )
                divergence_mean = (
                    sum(pairwise_overlaps) / len(pairwise_overlaps)
                    if pairwise_overlaps else 0.0
                )

                cells[key] = {
                    "character": char,
                    "doctrine": arm,
                    "model": model_short,
                    "echo_mean": cell_echo_mean,
                    "echo_rate": cell_echo_rate,
                    "pairwise_overlap_mean": divergence_mean,
                    "runs": run_entry_overlaps,
                    "pairwise_overlaps": [
                        round(o, 4) for o in pairwise_overlaps
                    ],
                }

    # Summary: cross-arm deltas
    summary = _compute_summary(cells)

    return {"cells": cells, "summary": summary}


def _compute_summary(cells: dict) -> dict:
    """Compute cross-arm deltas and per-dimension breakdowns."""

    def arm_means(arm: str, metric: str) -> list[float]:
        return [
            v[metric] for v in cells.values() if v["doctrine"] == arm
        ]

    def mean(values: list[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    current_echo = mean(arm_means("current", "echo_mean"))
    additive_echo = mean(arm_means("additive", "echo_mean"))
    stopslop_echo = mean(arm_means("stopslop", "echo_mean"))

    current_div = mean(arm_means("current", "pairwise_overlap_mean"))
    additive_div = mean(arm_means("additive", "pairwise_overlap_mean"))
    stopslop_div = mean(arm_means("stopslop", "pairwise_overlap_mean"))

    # Per character×model consistency check
    add_echo_wins = 0
    add_div_wins = 0
    combos = 0
    for char in CHARACTERS:
        for model in MODELS:
            model_short = model.replace("claude-", "")
            ck = _cell_key(char, "current", model)
            ak = _cell_key(char, "additive", model)
            if ck in cells and ak in cells:
                combos += 1
                if cells[ak]["echo_mean"] < cells[ck]["echo_mean"]:
                    add_echo_wins += 1
                if cells[ak]["pairwise_overlap_mean"] < cells[ck]["pairwise_overlap_mean"]:
                    add_div_wins += 1

    # Per-model breakdown
    per_model = {}
    for model in MODELS:
        model_short = model.replace("claude-", "")
        per_model[model_short] = {}
        for arm in ARMS:
            vals_echo = [v["echo_mean"] for v in cells.values()
                         if v["doctrine"] == arm and v["model"] == model_short]
            vals_div = [v["pairwise_overlap_mean"] for v in cells.values()
                        if v["doctrine"] == arm and v["model"] == model_short]
            per_model[model_short][arm] = {
                "echo": mean(vals_echo),
                "pairwise_overlap": mean(vals_div),
            }

    # Per-character breakdown
    per_character = {}
    for char in CHARACTERS:
        per_character[char] = {}
        for arm in ARMS:
            vals_echo = [v["echo_mean"] for v in cells.values()
                         if v["doctrine"] == arm and v["character"] == char]
            vals_div = [v["pairwise_overlap_mean"] for v in cells.values()
                        if v["doctrine"] == arm and v["character"] == char]
            per_character[char][arm] = {
                "echo": mean(vals_echo),
                "pairwise_overlap": mean(vals_div),
            }

    return {
        "additive_vs_current": {
            "echo_delta": additive_echo - current_echo,
            "divergence_delta": additive_div - current_div,
            "echo_consistent_wins": f"{add_echo_wins}/{combos}",
            "pairwise_overlap_consistent_wins": f"{add_div_wins}/{combos}",
        },
        "stopslop_vs_current": {
            "echo_delta": stopslop_echo - current_echo,
            "divergence_delta": stopslop_div - current_div,
        },
        "arm_means": {
            "current": {"echo": current_echo, "pairwise_overlap": current_div},
            "additive": {"echo": additive_echo, "pairwise_overlap": additive_div},
            "stopslop": {"echo": stopslop_echo, "pairwise_overlap": stopslop_div},
        },
        "per_model": per_model,
        "per_character": per_character,
    }
```

- [ ] **Step 6: Implement summary writer**

Add to `run_trial.py`:

```python
def write_summary(report: dict, path: str) -> None:
    """Write the human-readable summary report."""
    s = report["summary"]
    lines = [
        "# Additive-Doctrine Discriminator Trial — Results\n",
        "## Arm means\n",
        "| Arm | Echo mean | Pairwise overlap mean |",
        "|---|---|---|",
    ]
    for arm in ["current", "additive", "stopslop"]:
        m = s["arm_means"][arm]
        lines.append(f"| {arm} | {m['echo']:.4f} | {m['pairwise_overlap']:.4f} |")

    avsc = s["additive_vs_current"]
    svsc = s["stopslop_vs_current"]
    lines += [
        "",
        "## Cross-arm deltas (vs current)\n",
        "| Comparison | Echo delta | Divergence delta |",
        "|---|---|---|",
        f"| additive | {avsc['echo_delta']:+.4f} | {avsc['divergence_delta']:+.4f} |",
        f"| stopslop | {svsc['echo_delta']:+.4f} | {svsc['divergence_delta']:+.4f} |",
        "",
        "## Consistency (additive vs current)\n",
        f"- Echo: additive lower in {avsc['echo_consistent_wins']} "
        f"character×model combinations",
        f"- Pairwise overlap: additive lower in {avsc['pairwise_overlap_consistent_wins']} "
        f"character×model combinations",
    ]

    lines += [
        "",
        "## Per-model breakdown\n",
    ]
    for model_short, arms in s["per_model"].items():
        lines.append(f"### {model_short}\n")
        lines.append("| Arm | Echo mean | Pairwise overlap mean |")
        lines.append("|---|---|---|")
        for arm in ["current", "additive", "stopslop"]:
            m = arms[arm]
            lines.append(f"| {arm} | {m['echo']:.4f} | {m['pairwise_overlap']:.4f} |")
        lines.append("")

    lines += [
        "## Per-character breakdown\n",
    ]
    for char, arms in s["per_character"].items():
        lines.append(f"### {char}\n")
        lines.append("| Arm | Echo mean | Pairwise overlap mean |")
        lines.append("|---|---|---|")
        for arm in ["current", "additive", "stopslop"]:
            m = arms[arm]
            lines.append(f"| {arm} | {m['echo']:.4f} | {m['pairwise_overlap']:.4f} |")
        lines.append("")

    lines += [
        "## Per-cell detail\n",
        "| Cell | Echo mean | Echo rate | Pairwise overlap mean |",
        "|---|---|---|---|",
    ]
    for key in sorted(report["cells"].keys()):
        c = report["cells"][key]
        lines.append(
            f"| {key} | {c['echo_mean']:.4f} | {c['echo_rate']:.4f} "
            f"| {c['pairwise_overlap_mean']:.4f} |"
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
```

- [ ] **Step 7: Wire detection and reporting into the main block**

Update the `__main__` block in `run_trial.py`:

```python
if __name__ == "__main__":
    args = parse_args()
    out_dir = args.out_dir or OUT_DIR

    if args.dry_run:
        for cell in MATRIX:
            prompt = assemble_prompt(cell["character"], cell["doctrine"])
            print(f"--- {cell['character']}/{cell['doctrine']}/{cell['model']} ---")
            print(f"Prompt length: {len(prompt)} chars")
            print(prompt[:200] + "...\n")
        sys.exit(0)

    if not args.detect_only:
        print(f"Generating {len(MATRIX) * RUNS_PER_CELL} notes...")
        generate_all(MATRIX, RUNS_PER_CELL, out_dir)
        print("Generation complete.\n")

    print("Running detection...")
    report = run_detection(out_dir)

    report_path = os.path.join(TRIAL_DIR, "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"Report saved to {report_path}")

    summary_path = os.path.join(TRIAL_DIR, "summary.md")
    write_summary(report, summary_path)
    print(f"Summary saved to {summary_path}")
```

- [ ] **Step 8: Run all tests**

```bash
cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py -v
```

Expected: all tests PASS (14 total).

- [ ] **Step 9: Commit**

```bash
git add trials/2026-08-additive-discriminator/run_trial.py \
       trials/2026-08-additive-discriminator/test_runner.py
git commit -m "feat: add detection, aggregation, and reporting phase"
```

Expected: commit created with the listed files. Verify with `git log -1 --stat`.
