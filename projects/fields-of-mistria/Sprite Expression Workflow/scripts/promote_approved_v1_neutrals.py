from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def approved_notes(character_name: str, set_name: str, neutral_only: bool) -> str:
    base = (
        f"The approved generated neutral is authoritative for {character_name}'s "
        f"{set_name} identity, outfit or form construction, fixed gradient, framing, "
        "and Seiyo rendering."
    )
    if neutral_only:
        return base + " This sprite set intentionally supports neutral only."
    return (
        base
        + " Future expressions are mapped to Seiyo-26 and must be generated "
        "independently from this approved neutral."
    )


def main() -> None:
    promoted: list[str] = []
    skipped: list[str] = []
    missing: list[str] = []

    for character_path in sorted((ROOT / "characters").glob("*.json")):
        data = json.loads(character_path.read_text(encoding="utf-8"))
        changed = False

        for sprite_set in data.get("sprite_sets", []):
            character_id = data["id"]
            set_id = sprite_set["id"]
            asset_stem = sprite_set["asset_stem"]
            candidate = (
                ROOT
                / "diagnostics"
                / character_id
                / set_id
                / f"{asset_stem}_neutral_candidate_v1.png"
            )
            production_dir = ROOT / "sprites" / character_id / set_id
            production = production_dir / f"{asset_stem}_neutral.png"

            if production.exists():
                skipped.append(f"{character_id}/{set_id}: existing production")
                continue
            if not candidate.exists():
                missing.append(f"{character_id}/{set_id}: no V1 candidate")
                continue

            production_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(candidate, production)

            production_ref = production.relative_to(ROOT).as_posix()
            existing_refs = []
            for reference in sprite_set.get("references", []):
                if reference.get("path") == production_ref:
                    continue
                updated = dict(reference)
                if updated.get("role") == "identity-base":
                    updated["role"] = "outfit-reference"
                    updated["notes"] = (
                        "Canonical source for outfit or form construction, colors, and "
                        "distinctive landmarks; do not reproduce pixel rendering or the "
                        "exact source pose."
                    )
                existing_refs.append(updated)

            sprite_set["references"] = [
                {
                    "path": production_ref,
                    "role": "identity-base",
                    "notes": (
                        "Approved generated neutral. Preserve its identity, outfit or form "
                        "construction, gradient, framing, and Seiyo rendering."
                    ),
                },
                *existing_refs,
            ]

            neutral_only = character_id == "caldarus" and set_id == "statue"
            sprite_set["set_notes"] = approved_notes(
                data["display_name"], sprite_set["display_name"], neutral_only
            )

            background = sprite_set["background"]
            manifest = {
                "schema_version": 1,
                "character": character_id,
                "sprite_set": set_id,
                "asset_stem": asset_stem,
                "style": sprite_set["style"],
                "background": {
                    "top": background["top"],
                    "bottom": background["bottom"],
                },
                "base_expression": "neutral",
                "expressions": {"neutral": production.name},
            }
            (production_dir / "manifest.json").write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            promoted.append(f"{character_id}/{set_id}")
            changed = True

        if changed:
            character_path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

    print(f"Promoted {len(promoted)} V1 neutrals")
    for item in promoted:
        print(f"  + {item}")
    print(f"Skipped {len(skipped)} existing production sets")
    print(f"Missing {len(missing)} V1 candidates")
    for item in missing:
        print(f"  ! {item}")


if __name__ == "__main__":
    main()
