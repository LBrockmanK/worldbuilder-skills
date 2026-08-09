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
