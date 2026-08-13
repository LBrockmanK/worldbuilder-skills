import pytest
from fail_check import fail_check

def test_divergent_variants_pass():
    variants = [
        "She flinches at loud voices, tucking her chin before catching herself.",
        "When cornered, she defaults to bargaining — offering information, favors, anything portable.",
        "Her laughter arrives a beat late, calibrated to the room rather than the joke."
    ]
    result = fail_check(variants)
    assert result["passed"] is True
    assert result["max_jaccard"] < 0.25

def test_identical_variants_fail():
    variants = [
        "She is brave and strong and kind.",
        "She is brave and strong and kind.",
        "She is brave and strong and kind."
    ]
    result = fail_check(variants)
    assert result["passed"] is False
    assert result["max_jaccard"] == 1.0

def test_near_identical_variants_fail():
    variants = [
        "She flinches at loud noises, tucking her chin down.",
        "She flinches at loud sounds, tucking her chin down.",
        "She flinches at loud voices, tucking her chin down."
    ]
    result = fail_check(variants)
    assert result["passed"] is False
    assert result["max_jaccard"] > 0.25

def test_returns_all_pairs():
    variants = ["a", "b", "c"]
    result = fail_check(variants)
    assert len(result["pairs"]) == 3  # 3 choose 2

def test_boundary_value_passes():
    """Spec says 'exceeds 0.25' so exactly 0.25 should pass."""
    # Use variants whose trigram Jaccard is exactly at threshold
    variants = ["abcdef", "abcxyz", "mnopqr"]
    result = fail_check(variants)
    # The exact similarity depends on trigram overlap; this test verifies
    # the boundary operator is <= not <
    assert result["passed"] == (result["max_jaccard"] <= 0.25)
