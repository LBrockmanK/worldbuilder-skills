#!/usr/bin/env python3
"""Compile modular portrait specifications into platform-ready prompt text."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SpecError(ValueError):
    pass


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SpecError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SpecError(f"Invalid JSON in {path}: {exc}") from exc


def require(mapping: dict, key: str, context: str):
    value = mapping.get(key)
    if value is None or value == "" or value == []:
        raise SpecError(f"Missing required field '{key}' in {context}")
    return value


def validate_character(character: dict) -> None:
    if character.get("schema_version") != 1:
        raise SpecError("Character schema_version must be 1")
    for key in ("id", "display_name", "identity_anchor", "sprite_sets"):
        require(character, key, "character")
    ids = [item.get("id") for item in character["sprite_sets"]]
    if len(ids) != len(set(ids)):
        raise SpecError("Sprite-set IDs must be unique")


def select_sprite_set(character: dict, sprite_set_id: str | None) -> dict:
    sets = character["sprite_sets"]
    if sprite_set_id is None:
        if len(sets) != 1:
            raise SpecError("Character has multiple sprite sets; pass --sprite-set")
        return sets[0]
    for sprite_set in sets:
        if sprite_set.get("id") == sprite_set_id:
            return sprite_set
    raise SpecError(f"Unknown sprite set '{sprite_set_id}'")


def load_style(style_id: str) -> dict:
    style = load_json(ROOT / "presets" / "styles" / f"{style_id}.json")
    if style.get("id") != style_id:
        raise SpecError(f"Style ID mismatch for '{style_id}'")
    return style


def load_expression_pack(pack_id: str) -> dict:
    pack = load_json(ROOT / "presets" / "expressions" / f"{pack_id}.json")
    if pack.get("id") != pack_id:
        raise SpecError(f"Expression-pack ID mismatch for '{pack_id}'")
    expressions = require(pack, "expressions", f"expression pack '{pack_id}'")
    ids = [item.get("id") for item in expressions]
    if None in ids or len(ids) != len(set(ids)):
        raise SpecError(f"Expression IDs in '{pack_id}' must exist and be unique")
    return pack


def validate_sprite_set(sprite_set: dict, pack: dict) -> None:
    context = f"sprite set '{sprite_set.get('id', '?')}'"
    for key in ("asset_stem", "style", "expression_pack", "outfit_anchor", "background"):
        require(sprite_set, key, context)
    if "references" not in sprite_set or not isinstance(sprite_set["references"], list):
        raise SpecError(f"Missing required list 'references' in {context}")

    background = sprite_set["background"]
    mode = require(background, "mode", f"{context} background")
    if mode != "character":
        raise SpecError(f"{context} background mode must be 'character'")
    require(background, "top", f"{context} character background")
    require(background, "bottom", f"{context} character background")

    references = sprite_set["references"]
    if references:
        if references[0].get("role") != "identity-base":
            raise SpecError(f"The first reference in {context} must have role 'identity-base'")
        for reference in references:
            path_text = require(reference, "path", f"reference in {context}")
            path = Path(path_text)
            resolved = path if path.is_absolute() else ROOT / path
            if not resolved.is_file():
                raise SpecError(f"Reference file not found for {context}: {path_text}")

    expression_ids = {item["id"] for item in pack["expressions"]}
    unknown_overrides = set(sprite_set.get("expression_overrides", {})) - expression_ids
    if unknown_overrides:
        raise SpecError(
            f"Unknown expression override(s) in {context}: " + ", ".join(sorted(unknown_overrides))
        )

def resolve_background(sprite_set: dict) -> tuple[str, str]:
    configured = sprite_set["background"]
    return require(configured, "top", "character background"), require(configured, "bottom", "character background")


def normalize_sentence(text: str) -> str:
    text = " ".join(text.strip().split())
    return text if text.endswith((".", "!", "?")) else text + "."


def compile_prompt(character: dict, sprite_set: dict, expression: dict, style: dict) -> tuple[str, str, str]:
    override = sprite_set.get("expression_overrides", {}).get(expression["id"], {})
    instruction = override.get("instruction", expression.get("instruction"))
    if not instruction:
        raise SpecError(f"Expression '{expression['id']}' has no instruction")
    top, bottom = resolve_background(sprite_set)

    identity = normalize_sentence(character["identity_anchor"])
    outfit = normalize_sentence(sprite_set["outfit_anchor"])
    acting = normalize_sentence(instruction)
    gradient = normalize_sentence(f"Background gradient: {top} at the top fading to {bottom} at the bottom")
    parts = [
        style["prefix"] + identity[0].lower() + identity[1:],
        outfit,
        acting,
        gradient,
        normalize_sentence(style["framing"]),
        normalize_sentence(style["style_direction"]),
        normalize_sentence(style["background_constraints"]),
        normalize_sentence(style["identity_constraints"]),
        normalize_sentence(style["negative_constraints"]),
    ]
    return " ".join(parts), top, bottom


def compile_document(character: dict, sprite_set: dict, pack: dict, style: dict, only: set[str] | None) -> str:
    selected = [item for item in pack["expressions"] if only is None or item["id"] in only]
    if only is not None:
        missing = only - {item["id"] for item in selected}
        if missing:
            raise SpecError("Unknown expression(s): " + ", ".join(sorted(missing)))
    if not selected:
        raise SpecError("No expressions selected")

    base = f"{character['identity_anchor'].rstrip('.')}. {sprite_set['outfit_anchor'].rstrip('.')}"
    lines = [
        f"Expression Sprite Prompts for: {character['display_name']}",
        "=" * 50,
        "",
        f"Base appearance: {base}.",
        "",
        f"Art style prefix: {style['prefix']}",
        "Art style suffix: " + " ".join([
            style["framing"], style["style_direction"], style["background_constraints"],
            style["identity_constraints"], style["negative_constraints"]
        ]),
        "",
    ]
    for expression in selected:
        prompt, _, _ = compile_prompt(character, sprite_set, expression, style)
        lines.extend([
            f"--- {expression['label'].upper()} ---",
            prompt,
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("character", type=Path)
    parser.add_argument("--sprite-set")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--only", help="Comma-separated expression IDs")
    parser.add_argument("--check", action="store_true", help="Validate and compile without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        character = load_json(args.character.resolve())
        validate_character(character)
        sprite_set = select_sprite_set(character, args.sprite_set)
        style = load_style(sprite_set["style"])
        pack = load_expression_pack(sprite_set["expression_pack"])
        validate_sprite_set(sprite_set, pack)
        only = {item.strip() for item in args.only.split(",") if item.strip()} if args.only else None
        document = compile_document(character, sprite_set, pack, style, only)
        if args.check:
            print(f"OK: {character['display_name']} / {sprite_set['id']} / {pack['id']} / character palette")
        elif args.output:
            output = args.output.resolve()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(document, encoding="utf-8")
            print(output)
        else:
            sys.stdout.write(document)
        return 0
    except SpecError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
