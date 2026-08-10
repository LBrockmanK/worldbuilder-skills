"""Tests for the discriminator trial runner."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from unittest.mock import patch, MagicMock
from run_trial import (
    assemble_prompt, MATRIX, ARMS, MODELS, CHARACTERS, RUNS_PER_CELL,
    extract_entries, run_detection, write_summary,
)


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
    """3 arms x 2 characters x 2 models = 12 cells."""
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


def test_generate_one_calls_api():
    """generate_one calls anthropic with correct model and prompt."""
    from run_trial import generate_one

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
    """generate_all creates one file per cell x run."""
    from run_trial import generate_all

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


def test_run_detection_structure(tmp_path):
    """Detection report has the expected structure."""
    # Create synthetic outputs: 3 runs x 12 cells = 36 files
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
                "echo_delta": -0.05, "pairwise_overlap_delta": -0.05,
                "echo_consistent_wins": "1/1",
                "pairwise_overlap_consistent_wins": "1/1",
            },
            "stopslop_vs_current": {"echo_delta": 0.0, "pairwise_overlap_delta": 0.0},
            "arm_means": {
                "current": {"echo": 0.2, "pairwise_overlap": 0.3},
                "additive": {"echo": 0.15, "pairwise_overlap": 0.25},
                "stopslop": {"echo": 0.2, "pairwise_overlap": 0.3},
            },
            "per_model": {
                "sonnet-5": {
                    "current": {"echo": 0.2, "pairwise_overlap": 0.3},
                    "additive": {"echo": 0.15, "pairwise_overlap": 0.25},
                    "stopslop": {"echo": 0.2, "pairwise_overlap": 0.3},
                },
            },
            "per_character": {
                "nadja": {
                    "current": {"echo": 0.2, "pairwise_overlap": 0.3},
                    "additive": {"echo": 0.15, "pairwise_overlap": 0.25},
                    "stopslop": {"echo": 0.2, "pairwise_overlap": 0.3},
                },
            },
        },
    }
    out = str(tmp_path / "summary.md")
    write_summary(report, out)
    assert os.path.exists(out)
    content = open(out, encoding="utf-8").read()
    assert "Arm means" in content
    assert "Cross-arm deltas" in content
    assert "Consistency" in content
    assert "Per-model breakdown" in content
    assert "Per-character breakdown" in content
    assert "Per-cell detail" in content
