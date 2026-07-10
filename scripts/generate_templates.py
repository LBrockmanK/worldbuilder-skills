#!/usr/bin/env python
"""Generate Obsidian Templater templates from an OKF registry.

Write-side sibling of generate_rules.py: one Templater template per
registry type (frontmatter skeleton + type body) in <out>/_templates/,
a suggester type-picker per mixed-type directory, and (--obsidian) the
folder_templates wiring in the vendored Templater data.json. Generic
over any okf.json — no worldbuilder knowledge; graduates verbatim to
okf-enforcement/scripts/.
"""
import argparse
import json
import os
import sys

MOMENT_TS = '<% moment.utc().format("YYYY-MM-DDTHH:mm[Z]") %>'
MOMENT_DATE = '<% moment.utc().format("YYYY-MM-DD") %>'
UNIVERSAL_ORDER = ('type', 'title', 'description', 'tags', 'date',
                   'timestamp', 'resources')


def empty_value(ftype):
    return {'list': '[]', 'tags': '[]', 'checkbox': 'false',
            'number': ''}.get(ftype, '""')


def type_template(config, tname):
    spec = config['types'][tname]
    status = config['tags']['status']['open'][0]
    lines = ['---',
             f'type: {tname}',
             'title: <% tp.file.title %>',
             'description: ""',
             'tags:',
             f'  - {status}',
             f'date: {MOMENT_DATE}',
             f'timestamp: {MOMENT_TS}',
             'resources: []']
    for fname, fspec in (spec.get('fields') or {}).items():
        if fname in UNIVERSAL_ORDER:
            continue
        lines.append(f'{fname}: {empty_value(fspec.get("type", "text"))}')
    lines.append('---')
    body = (spec.get('template') or '').strip()
    return '\n'.join(lines) + '\n' + (('\n' + body + '\n') if body else '')


def picker_template(types):
    choices = json.dumps(types)
    return ('<%*\n'
            f'const choices = {choices};\n'
            'const type = await tp.system.suggester(choices, choices);\n'
            'const tmpl = tp.file.find_tfile("_templates/type-" + type);\n'
            'tR += await tp.file.include(tmpl);\n'
            '%>')


def dir_slug(path):
    return path.strip('/').replace('/', '-') or 'note'


def parse_dirs(pairs, config):
    """[(path, [types])] from --dir path=a,b; validates type names."""
    out = []
    for pair in pairs:
        path, _, names = pair.partition('=')
        types = [t.strip() for t in names.split(',') if t.strip()]
        for t in types:
            if t not in config['types']:
                print(f'error: unknown type {t!r} in --dir {pair!r}',
                      file=sys.stderr)
                sys.exit(2)
        out.append((path, types))
    return out


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def update_obsidian_config(out_root, attachments):
    p = os.path.join(out_root, '.obsidian', 'plugins',
                     'templater-obsidian', 'data.json')
    data = {}
    if os.path.isfile(p):
        with open(p, encoding='utf-8') as f:
            data = json.load(f)
    data['templates_folder'] = '_templates'
    data['trigger_on_file_creation_mode'] = 'folder'
    data['folder_templates'] = [
        {'folder': folder.strip('/'), 'template': template}
        for folder, template in attachments]
    write(p, json.dumps(data, indent=2) + '\n')


def main():
    ap = argparse.ArgumentParser(description='Generate Templater templates '
                                             'from an OKF registry')
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--dir', action='append', default=[],
                    help='path=type[,type...] — types allowed in that dir')
    ap.add_argument('--obsidian', action='store_true',
                    help='wire folder_templates into the vendored '
                         'Templater data.json')
    args = ap.parse_args()

    with open(args.config, encoding='utf-8') as f:
        config = json.load(f)

    if args.dir:
        dirs = parse_dirs(args.dir, config)
    else:
        all_types = sorted(config['types'])
        dirs = [(p, all_types) for p in config.get('enforced_paths', {})] or [('', all_types)]

    emitted = set()
    attachments = []
    for path, types in dirs:
        for t in types:
            if t not in emitted:
                write(os.path.join(args.out, '_templates', f'type-{t}.md'),
                      type_template(config, t))
                emitted.add(t)
        if len(types) == 1:
            attachments.append((path, f'_templates/type-{types[0]}.md'))
        else:
            name = (f'new-{dir_slug(path)}.md' if args.dir
                    else 'new-note.md')
            write(os.path.join(args.out, '_templates', name),
                  picker_template(types))
            attachments.append((path, f'_templates/{name}'))

    if args.obsidian:
        update_obsidian_config(args.out, attachments)
    print(f'{len(emitted)} type template(s), '
          f'{len(attachments)} folder attachment(s).')


if __name__ == '__main__':
    main()
