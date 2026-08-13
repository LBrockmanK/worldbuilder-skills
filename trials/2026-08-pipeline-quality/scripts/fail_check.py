from itertools import combinations

THRESHOLD = 0.25

def char_trigrams(text: str) -> set[str]:
    t = text.lower()
    return {t[i:i+3] for i in range(len(t) - 2)} if len(t) >= 3 else set()

def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)

def fail_check(variants: list[str], threshold: float = THRESHOLD) -> dict:
    trigrams = [char_trigrams(v) for v in variants]
    pairs = []
    max_sim = 0.0
    for i, j in combinations(range(len(variants)), 2):
        sim = jaccard(trigrams[i], trigrams[j])
        pairs.append({"i": i, "j": j, "similarity": sim})
        max_sim = max(max_sim, sim)
    return {
        "passed": max_sim <= threshold,
        "max_jaccard": max_sim,
        "pairs": pairs
    }
