"""Tests for the discriminator trial runner."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from unittest.mock import patch, MagicMock
from run_trial import assemble_prompt, MATRIX, ARMS, RUNS_PER_CELL


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
