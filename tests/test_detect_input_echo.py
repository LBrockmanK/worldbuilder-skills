import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import pytest
from scripts.detect_input_echo import categorize, ngram_overlap, compare_cross_model, ECHO_THRESHOLD


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
        assert 0.15 < score < 0.8

    def test_semantic_match_different_phrasing(self):
        score = ngram_overlap(
            "she waves off thanks and changes the subject",
            "she refuses credit for every defense",
            n=3,
        )
        assert score < 0.2


class TestCategorize:
    """categorize returns a dict with category, matched_input, overlap."""

    def test_verbatim_echo(self):
        output = "She refuses credit for every defense."
        input_notes = "refuses credit for every defense"
        result = categorize(output, input_notes)
        assert result["category"] == "input_echo"
        assert result["matched_input"] is not None
        assert result["overlap"] > 0

    def test_clean_transformation(self):
        output = "She waves off thanks and walks back to the sun before anyone can name what she did."
        input_notes = "refuses credit for every defense"
        result = categorize(output, input_notes)
        assert result["category"] == "clean"
        assert result["matched_input"] is None
        assert result["overlap"] < ECHO_THRESHOLD

    def test_partial_echo(self):
        output = "She cajoles people closer rather than reaching for them."
        input_notes = "cajoles people closer to her mouth rather than grabbing them"
        result = categorize(output, input_notes)
        assert result["category"] == "input_echo"

    def test_no_input_match(self):
        output = "When the baker forgets to set aside her usual order, she says nothing and buys from the next stall."
        input_notes = "She keeps the rent money in two jars."
        result = categorize(output, input_notes)
        assert result["category"] == "clean"


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

    def test_single_model_no_clean_label(self):
        """Concern 5: single model entries must not be labeled 'clean'."""
        entries = {
            "opus": [
                "She waves off thanks and walks to the sun.",
                "She refuses credit for every defense.",
            ],
        }
        input_notes = "refuses credit for every defense"
        results = compare_cross_model(entries, input_notes)
        for r in results:
            assert r["category"] != "clean", (
                "Single-model entries must not be labeled 'clean'"
            )
        # non-echo entries should be input_echo_only
        non_echo = [r for r in results if r["category"] == "input_echo_only"]
        assert len(non_echo) > 0

    def test_alignment_parameter_accepted(self):
        """Concern 4: optional alignment parameter exists."""
        entries = {
            "opus": ["She waves off thanks."],
            "sol": ["She changes the subject."],
        }
        # Should not raise
        results = compare_cross_model(
            entries, "unrelated input", alignment=None
        )
        assert isinstance(results, list)
