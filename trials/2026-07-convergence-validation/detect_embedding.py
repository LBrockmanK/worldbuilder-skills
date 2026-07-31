"""Method 2: Embedding similarity detection.

Embeds sentences from two notes, computes pairwise cosine similarity,
flags pairs above threshold. Uses Voyage AI (voyage-3-large) to avoid
Claude/GPT family circularity.

Usage: python detect_embedding.py <note_a> <note_b> [--threshold 0.92]
       python detect_embedding.py --all-pairs <out_dir> <character> [--threshold 0.92]

Requires: VOYAGE_API_KEY environment variable.
"""
import sys
import json
import os
import numpy as np
from pathlib import Path
from itertools import combinations

MODELS = ['opus46', 'opus5', 'sol', 'terra']
DEFAULT_THRESHOLD = 0.92

def split_sentences(text):
    import re
    raw = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in raw if s.strip() and len(s.strip()) > 10]

def embed_sentences(sentences, api_key):
    """Embed via Voyage AI. Returns list of embedding vectors."""
    import requests
    resp = requests.post(
        'https://api.voyageai.com/v1/embeddings',
        headers={'Authorization': f'Bearer {api_key}'},
        json={'input': sentences, 'model': 'voyage-3-large'},
    )
    resp.raise_for_status()
    data = resp.json()['data']
    return [d['embedding'] for d in data]

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def find_similar_pairs(text_a, text_b, api_key, threshold):
    sents_a = split_sentences(text_a)
    sents_b = split_sentences(text_b)
    if not sents_a or not sents_b:
        return []

    all_sents = sents_a + sents_b
    embeddings = embed_sentences(all_sents, api_key)
    emb_a = embeddings[:len(sents_a)]
    emb_b = embeddings[len(sents_a):]

    pairs = []
    for i, (sa, ea) in enumerate(zip(sents_a, emb_a)):
        for j, (sb, eb) in enumerate(zip(sents_b, emb_b)):
            sim = cosine_similarity(ea, eb)
            if sim >= threshold:
                pairs.append({
                    'sentence_a': sa,
                    'sentence_b': sb,
                    'similarity': round(sim, 4),
                })
    return pairs

def run_all_pairs(out_dir, character, api_key, threshold):
    out_dir = Path(out_dir)
    results = []
    for ma, mb in combinations(MODELS, 2):
        file_a = out_dir / f'{character}-{ma}.md'
        file_b = out_dir / f'{character}-{mb}.md'
        pairs = find_similar_pairs(
            file_a.read_text(encoding='utf-8'),
            file_b.read_text(encoding='utf-8'),
            api_key, threshold,
        )
        results.append({
            'pair': f'{ma}-vs-{mb}',
            'character': character,
            'threshold': threshold,
            'flag_count': len(pairs),
            'flags': pairs,
        })
    return results

def run_four_way(out_dir, character, api_key, threshold):
    """Embed all sentences from all 4 models, cluster by similarity.
    Report sentences where 3+ models converge."""
    out_dir = Path(out_dir)
    all_sents = []
    sent_meta = []
    for model in MODELS:
        path = out_dir / f'{character}-{model}.md'
        for s in split_sentences(path.read_text(encoding='utf-8')):
            all_sents.append(s)
            sent_meta.append({'model': model, 'sentence': s})

    embeddings = embed_sentences(all_sents, api_key)
    clusters = []
    used = set()
    for i in range(len(all_sents)):
        if i in used:
            continue
        cluster = [i]
        for j in range(i + 1, len(all_sents)):
            if j in used:
                continue
            if cosine_similarity(embeddings[i], embeddings[j]) >= threshold:
                cluster.append(j)
        if len(set(sent_meta[k]['model'] for k in cluster)) >= 2:
            used.update(cluster)
            models = list(set(sent_meta[k]['model'] for k in cluster))
            clusters.append({
                'model_count': len(models),
                'models': models,
                'character': character,
                'threshold': threshold,
                'sentences': {sent_meta[k]['model']: sent_meta[k]['sentence'] for k in cluster},
            })
    clusters.sort(key=lambda x: -x['model_count'])
    return clusters

if __name__ == '__main__':
    api_key = os.environ['VOYAGE_API_KEY']
    threshold = DEFAULT_THRESHOLD
    if '--threshold' in sys.argv:
        idx = sys.argv.index('--threshold')
        threshold = float(sys.argv[idx + 1])
        sys.argv.pop(idx)
        sys.argv.pop(idx)

    if sys.argv[1] == '--all-pairs':
        out_dir, character = sys.argv[2], sys.argv[3]
        results = run_all_pairs(out_dir, character, api_key, threshold)
        print(json.dumps(results, indent=2))
    elif sys.argv[1] == '--four-way':
        out_dir, character = sys.argv[2], sys.argv[3]
        results = run_four_way(out_dir, character, api_key, threshold)
        print(json.dumps(results, indent=2))
    else:
        a, b = Path(sys.argv[1]), Path(sys.argv[2])
        pairs = find_similar_pairs(
            a.read_text(encoding='utf-8'),
            b.read_text(encoding='utf-8'),
            api_key, threshold,
        )
        print(json.dumps(pairs, indent=2))
        print(f'\nTotal: {len(pairs)} pairs above {threshold}')
