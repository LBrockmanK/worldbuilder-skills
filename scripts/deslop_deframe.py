"""Deslop and deframe preprocessing for Design Notes.

Strips meta-vocabulary (builder/player abstraction layer) and flags
stop-slop patterns in input text before character generation.

Operates on text content; does not modify files. The caller is
responsible for preserving the original Design Notes.
"""

from __future__ import annotations

import os
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
    (r"(?i)\bhousehold\b", "meta_framing"),
    (r"(?i)\bnarrative function\b", "meta_framing"),
    (r"(?i)\bthematic mirror\b", "meta_framing"),
    (r"(?i)\bcross-references?:\s*\[\[", "meta_framing"),
    (r"(?i)\bcharacter art reference\b", "meta_framing"),
]


# --- Stop-slop pattern loading ---

def _load_slop_patterns() -> list[tuple[str, str]]:
    """Parse docs/slop-phrases.md and return (regex, category) pairs."""
    slop_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "docs", "slop-phrases.md",
    )
    with open(slop_file, encoding="utf-8") as f:
        content = f.read()

    patterns: list[tuple[str, str]] = []
    current_category = None

    for line in content.split("\n"):
        # Category header
        header = re.match(r"^## (.+)$", line)
        if header:
            # Convert "Soul section hedging" -> "soul_section_hedging"
            current_category = re.sub(r"\s+", "_", header.group(1).strip().lower())
            continue

        if current_category is None:
            continue

        # Bullet with quoted phrases: - "phrase" / "variant" / ...
        if not line.startswith("- "):
            continue

        # Extract all quoted strings from the line
        phrases = re.findall(r'"([^"]+)"', line)
        for phrase in phrases:
            # Skip phrases that are purely descriptive placeholders
            if phrase in ("same register", "the register she runs with"):
                # These are examples within the "register" entry; keep as-is
                pass

            # Clean up bracket placeholders: [X] -> optional content
            regex = phrase
            # Replace " [X] " with a single placeholder token before escaping
            regex = re.sub(r" ?\[([A-Za-z/ ]+)\] ?", "\x00", regex)
            # Escape the literal parts
            parts = regex.split("\x00")
            escaped = []
            for j, part in enumerate(parts):
                escaped.append(re.escape(part))
                if j < len(parts) - 1:
                    escaped.append(r"(?:\s+\S+){0,3}\s+")
            regex = "".join(escaped)
            # Word boundaries
            regex = r"(?i)\b" + regex + r"\b"
            patterns.append((regex, current_category))

    return patterns


SLOP_PATTERNS = _load_slop_patterns()


def process(text: str) -> ProcessResult:
    """Process Design Notes text: deframe then deslop.

    Returns the cleaned text and a list of changes made or flagged.
    Lines with meta-vocabulary get a [DEFRAME: category] marker prepended
    and the full original content is preserved. Slop-flagged lines get
    inline [FLAGGED: category] markers replacing the flagged phrase.
    """
    lines = text.split("\n")
    cleaned_lines: list[str] = []
    changes: list[Change] = []

    for i, line in enumerate(lines, start=1):
        working_line = line
        deframed = False

        # Deframe: mark lines containing meta-vocabulary
        matched_meta_spans: list[tuple[int, int]] = []
        for pattern, category in META_PATTERNS:
            m = re.search(pattern, line)
            if not m:
                continue
            # Skip if this match is fully contained within an earlier match
            # (e.g. skip \bhousehold\b when \bhousehold assignment\b hit)
            ms, me = m.start(), m.end()
            if any(ps <= ms and me <= pe for ps, pe in matched_meta_spans):
                continue
            matched_meta_spans.append((ms, me))
            if not deframed:
                changes.append(Change(
                    original=line.strip(),
                    category=category,
                    line_number=i,
                    suggestion="Remove or replace with in-world equivalent",
                ))
                working_line = f"[DEFRAME: {category}] {line}"
                deframed = True
            else:
                # Already marked this line; just record additional match
                changes.append(Change(
                    original=line.strip(),
                    category=category,
                    line_number=i,
                    suggestion="Remove or replace with in-world equivalent",
                ))

        # Deslop: flag slop patterns
        for pattern, category in SLOP_PATTERNS:
            if re.search(pattern, working_line):
                changes.append(Change(
                    original=line.strip(),
                    category=category,
                    line_number=i,
                    suggestion=f"Rewrite to remove {category.replace('_', ' ')} pattern",
                ))
                working_line = re.sub(
                    pattern, f"[FLAGGED: {category}]", working_line
                )

        cleaned_lines.append(working_line)

    return ProcessResult(
        cleaned="\n".join(cleaned_lines),
        changes=changes,
    )
