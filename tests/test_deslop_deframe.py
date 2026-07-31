import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import pytest
from scripts.deslop_deframe import process, Change


class TestDeframe:
    def test_marks_stewards_house(self):
        text = "Assigned to the Steward's House as town guard"
        result = process(text)
        assert "[DEFRAME: meta_framing]" in result.cleaned
        assert "Steward's House" in result.cleaned
        assert "town guard" in result.cleaned
        assert len(result.changes) > 0

    def test_marks_narrative_function(self):
        text = "Narrative function: the character who shows care and predation coexist"
        result = process(text)
        assert "[DEFRAME: meta_framing]" in result.cleaned
        assert "care and predation coexist" in result.cleaned

    def test_marks_thematic_mirror(self):
        text = "Thematic mirror with Vesper: both care about humans"
        result = process(text)
        assert "[DEFRAME: meta_framing]" in result.cleaned
        assert "both care about humans" in result.cleaned

    def test_marks_household_assignment(self):
        text = "household assignment is administrative fiction"
        result = process(text)
        assert "[DEFRAME: meta_framing]" in result.cleaned
        assert "household assignment" in result.cleaned
        assert len(result.changes) > 0

    def test_marks_standalone_household(self):
        text = "She belongs to a household on the east ridge"
        result = process(text)
        assert "[DEFRAME: meta_framing]" in result.cleaned
        assert "east ridge" in result.cleaned

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

    def test_flags_soul_section_hedging(self):
        text = "She hasn't examined this tendency closely"
        result = process(text)
        assert len(result.changes) > 0
        assert any(c.category == "soul_section_hedging" for c in result.changes)

    def test_flags_vague_declaratives(self):
        text = "The stakes are high for her family"
        result = process(text)
        assert len(result.changes) > 0
        assert any(c.category == "vague_declaratives" for c in result.changes)

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


class TestSlopFileLoading:
    def test_all_file_categories_loaded(self):
        """Every category from docs/slop-phrases.md should be detectable."""
        from scripts.deslop_deframe import _load_slop_patterns
        patterns = _load_slop_patterns()
        categories = {cat for _, cat in patterns}
        expected = {
            "interpretive_narration",
            "soul_section_hedging",
            "vague_interiority",
            "significance_inflation",
            "vague_declaratives",
            "copula_avoidance",
            "ai_vocabulary",
        }
        assert expected == categories
