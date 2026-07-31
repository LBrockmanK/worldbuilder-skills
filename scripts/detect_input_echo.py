"""Input-echo detection for the grader agent.

Compares output entries against source Design Notes to categorize
them as input-echo (phrasing too close to input) or clean (content
matches but phrasing diverges).

Standard library only — no external dependencies.
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
) -> dict:
    """Categorize an output entry as 'input_echo' or 'clean'.

    Splits input_notes into lines and checks the output against each.
    If any input line has n-gram overlap above the threshold with the
    output, the entry is input-echo.

    Returns:
        dict with keys:
        - category: "input_echo" | "clean"
        - matched_input: the input line that triggered echo, or None
        - overlap: the overlap score (actual best score for all categories)
    """
    input_lines = [
        line.strip().lstrip("- ")
        for line in input_notes.split("\n")
        if line.strip() and not line.strip().startswith("#")
    ]

    best_overlap = 0.0
    best_line = None

    for input_line in input_lines:
        if len(input_line) < 10:
            continue
        overlap = ngram_overlap(output_entry, input_line)
        if overlap > best_overlap:
            best_overlap = overlap
            best_line = input_line

    if best_overlap >= threshold:
        return {
            "category": "input_echo",
            "matched_input": best_line,
            "overlap": best_overlap,
        }

    return {"category": "clean", "matched_input": None, "overlap": best_overlap}


def compare_cross_model(
    entries_by_model: dict[str, list[str]],
    input_notes: str,
    echo_threshold: float = ECHO_THRESHOLD,
    convergence_threshold: float = 0.25,
    alignment: list[tuple[int, int]] | None = None,
) -> list[dict]:
    """Compare entries across models after filtering input-echo.

    Args:
        entries_by_model: {model_name: [entry_text, ...]} for the same section
        input_notes: source Design Notes for input-echo filtering
        echo_threshold: threshold for input-echo detection
        convergence_threshold: n-gram overlap threshold for cross-model convergence
        alignment: optional list of (index_model_a, index_model_b) pairs for
            entry matching. When None (default), uses all-pairs comparison.
            Future work: align entries by source fact or section position.

    Returns:
        List of findings, each with:
        - category: "input_echo" | "cross_model_convergence" | "clean" | "input_echo_only"
        - entry: the output text
        - model: which model produced it
        - match_model: which other model it converged with (if convergent)
        - overlap: the overlap score

    Note: When alignment is None, all-pairs comparison is used. This can
    trigger false convergence between unrelated entries. The alignment
    parameter exists for future use when source-fact metadata is available.

    When only one model is provided, entries are labeled 'input_echo' or
    'input_echo_only' (cannot verify cross-model divergence without a
    second model).
    """
    findings = []
    model_names = list(entries_by_model.keys())
    single_model = len(model_names) == 1

    for model_name, entries in entries_by_model.items():
        for entry in entries:
            # First check: is this input echo?
            cat_result = categorize(entry, input_notes, echo_threshold)
            if cat_result["category"] == "input_echo":
                findings.append({
                    "category": "input_echo",
                    "entry": entry,
                    "model": model_name,
                    "match_model": None,
                    "overlap": cat_result["overlap"],
                })
                continue

            # Single model: cannot assess cross-model convergence
            if single_model:
                findings.append({
                    "category": "input_echo_only",
                    "entry": entry,
                    "model": model_name,
                    "match_model": None,
                    "overlap": 0.0,
                })
                continue

            # Multi-model: check convergence with other models' entries
            best_match = None
            best_overlap = 0.0
            for other_model in model_names:
                if other_model == model_name:
                    continue
                for other_entry in entries_by_model[other_model]:
                    other_cat = categorize(other_entry, input_notes, echo_threshold)
                    if other_cat["category"] == "input_echo":
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
