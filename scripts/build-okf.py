#!/usr/bin/env python3
"""Regenerate defaults/okf.json from okf.base.json + defaults/templates/*.md."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, 'defaults', 'okf.base.json')
TEMPLATES = os.path.join(ROOT, 'defaults', 'templates')
OUT = os.path.join(ROOT, 'defaults', 'okf.json')


def main():
    with io.open(BASE, encoding='utf-8') as f:
        config = json.load(f)
    for name, spec in config.get('types', {}).items():
        ref = spec.pop('template_file', None)
        if ref is None:
            continue
        path = os.path.join(TEMPLATES, ref)
        if not os.path.isfile(path):
            sys.exit(f'Missing template file: {path}')
        with io.open(path, encoding='utf-8') as f:
            spec['template'] = f.read()
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'Wrote {OUT}')


if __name__ == '__main__':
    main()
