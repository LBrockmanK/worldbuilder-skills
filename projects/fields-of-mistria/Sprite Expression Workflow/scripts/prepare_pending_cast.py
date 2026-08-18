from __future__ import annotations

import json
import re
import shutil
from collections import Counter
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PENDING = ROOT / "PENDING"

SPECIAL_SETS = {
    "Caldarus": [
        ("spring", "Spring Humanoid", "Caldarus_Portrait.png"),
        ("dragon", "Dragon Form", "Caldarus_Dragon_Form.png"),
        ("statue", "Statue Form", "Caldarus_statue.png"),
    ],
    "Seridia": [
        ("spring", "Spring Revealed Form", "Seridia_Spring.png"),
        ("dragon", "Dragon Form", "Seridia_Dragon_Form.png"),
        ("priestess", "Dragon Priestess Guise", "Priestess_Portrait.png"),
    ],
    "Dozy": [("agnostic", "Season-Agnostic", "Dozy.png")],
    "Henrietta": [("agnostic", "Season-Agnostic", "Henrietta_Portrait.png")],
}


def section(text: str, heading: str) -> str:
    match = re.search(rf"(?s)^## {re.escape(heading)}\s*(.*?)(?=\n## |\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def description(text: str) -> str:
    match = re.search(r'^description:\s*"?(.*?)"?\s*$', text, re.M)
    return match.group(1).strip() if match else ""


def palette(path: Path) -> tuple[str, str]:
    with Image.open(path).convert("RGBA") as image:
        image.thumbnail((160, 160))
        pixels = []
        for r, g, b, a in image.getdata():
            if a < 220 or (r > 242 and g > 242 and b > 242):
                continue
            if max(r, g, b) - min(r, g, b) < 10 and max(r, g, b) > 210:
                continue
            pixels.append((r // 24 * 24, g // 24 * 24, b // 24 * 24))
    counts = Counter(pixels)
    chromatic = [(rgb, count) for rgb, count in counts.items() if max(rgb) - min(rgb) >= 36]
    ranked = sorted(chromatic or counts.items(), key=lambda item: item[1], reverse=True)
    common = [rgb for rgb, _ in ranked[:30]] or [(96, 96, 128), (184, 152, 176)]
    top = common[0]
    bottom = max(common[1:] or common, key=lambda c: sum((a - b) ** 2 for a, b in zip(top, c)))
    def hx(rgb: tuple[int, int, int]) -> str:
        return "#" + "".join(f"{min(v + 12, 255):02X}" for v in rgb)
    return hx(top), hx(bottom)


def refresh_existing_palettes() -> None:
    for spec_path in sorted((ROOT / "characters").glob("*.json")):
        if spec_path.stem in {"adeline", "celine", "dell", "juniper", "valen"}:
            continue
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        for sprite_set in spec["sprite_sets"]:
            source = ROOT / sprite_set["references"][0]["path"]
            top, bottom = palette(source)
            sprite_set["background"] = {"mode": "character", "top": top, "bottom": bottom}
        spec_path.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def apply_review_corrections() -> None:
    replacements = {
        "eiland": [("Brown skin, dark eyes.", "Brown skin, violet-purple eyes.")],
        "vera": [("Dark brown skin, brown eyes.", "Dark brown skin, violet-purple eyes.")],
        "seridia": [
            ("small dark horns", "large dark organic dragon horns growing from her head"),
            ("Gold hoop earrings.", "Solid gold circular disk earrings, each bearing a narrow vertical slit-eye motif."),
        ],
        "louis": [
            (
                "Brown wavy hair swept up from the forehead. Warm olive skin. Glasses. He wears tailored seasonal outfits in rich colors: a blue coat with gold braid trim and a diamond-pattern vest in spring,",
                "Brown wavy hair swept up from the forehead. Warm olive skin. Glasses. A thin pencil mustache with a narrow gap at the center. He wears tailored seasonal outfits in rich colors: a blue coat with gold braid trim, a clean cream chest layer, and a golden-yellow tailor's measuring tape draped around his neck and shoulders in spring,",
            )
        ],
    }
    for char_id, pairs in replacements.items():
        path = ROOT / "characters" / f"{char_id}.json"
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")

    notes = {
        ("caldarus", "dragon"): "Caldarus is male; his dragon form should retain a mature masculine facial and body read without changing canonical anatomy or ornaments.",
        ("seridia", "dragon"): "Seridia is female; her dragon form should retain a powerful feminine facial and body read without becoming cute, juvenile, or humanoid.",
        ("seridia", "spring"): "Production intentionally departs from the canonical horn gradient: her horns remain uniformly deep charcoal-black to match her dragon form.",
        ("nora", "spring"): "Nora is a mature older adult. Preserve the faint small bun or gathered hair visible behind her short golden-blonde style.",
    }
    for (char_id, set_id), note in notes.items():
        path = ROOT / "characters" / f"{char_id}.json"
        spec = json.loads(path.read_text(encoding="utf-8"))
        sprite_set = next(s for s in spec["sprite_sets"] if s["id"] == set_id)
        if note not in sprite_set["set_notes"]:
            sprite_set["set_notes"] += " " + note
        path.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def set_plan(name: str) -> list[tuple[str, str, str]]:
    if name in SPECIAL_SETS:
        return SPECIAL_SETS[name]
    candidates = sorted(PENDING.glob(f"{name}_*.png"))
    if not candidates:
        raise FileNotFoundError(f"No source image for {name}")
    return [("spring", "Spring Outfit", candidates[0].name)]


def identity_for(name: str, body: str, set_id: str) -> str:
    if name in {"Caldarus", "Seridia"}:
        return (
            f"{name}, preserving the exact form-specific identity shown in the current sprite-set source reference, including apparent age, facial or draconic structure, "
            "body plan, skin or scale coloring, hair, horns, eyes, wings, and every distinctive feature; the humanoid, dragon, statue, and guise designs are alternate forms of one character and must not be blended together"
        )
    shared = (
        f"{name}, preserving the exact identity, apparent age, facial structure, body type, "
        "skin or surface coloring, hair or species anatomy, eyes, and distinctive features shown in the source reference"
    )
    if set_id == "dragon":
        return shared + "; a true quadrupedal dragon, not a humanoid or human-dragon hybrid"
    if set_id == "statue":
        return shared + "; an immobile carved stone dragon statue, not a living creature"
    if set_id == "agnostic" and name == "Dozy":
        return shared + "; a compact, fluffy golden retriever with natural canine anatomy"
    if set_id == "agnostic" and name == "Henrietta":
        return shared + "; a well-kept domestic chicken with natural avian anatomy"
    first = re.split(r"\n\s*-", body, maxsplit=1)[0].strip().replace("\n", " ")
    return shared + (f". Source description: {first}" if first else "")


def outfit_for(name: str, set_id: str, display: str, body: str) -> str:
    if set_id == "dragon":
        return (
            f"No clothing except the exact ornaments visibly belonging to {name}'s dragon design in the source; "
            "preserve every horn, crest, wing, scale, spine, tail, jewelry, and colored accent"
        )
    if set_id == "statue":
        return "Exact carved stone dragon statue design from the source, including horns, antlers, hanging ornaments, cracks, facets, and monochrome stone material; no clothing"
    if name == "Dozy":
        return "No clothing; clean fluffy brown-and-cream golden retriever coat exactly matching the source"
    if name == "Henrietta":
        return "No clothing; white plumage, brown tail, red comb and wattle exactly matching the source"
    return (
        f"The exact {display.lower()} clothing, jewelry, accessories, fasteners, layers, color blocking, and silhouette shown in the source reference. "
        f"Use this source description as supporting evidence: {re.split(r'\n\s*-', body, maxsplit=1)[0].strip().replace(chr(10), ' ')}"
    )


def neutral_instruction(name: str, set_id: str) -> str:
    if set_id == "statue":
        return "Show the inert stone statue exactly as carved, with no facial acting, movement, glow, breath, or living pose. Use a centered three-quarter portrait crop that clearly contains the head, neck, shoulders, and ornamental silhouette."
    if set_id == "dragon":
        return "Show calm, alert neutrality in the dragon's eyes and resting mouth. Use a readable three-quarter view with the head, neck, near shoulder, wing roots, and enough torso to establish true quadrupedal dragon anatomy; no humanoid pose or hands."
    if name == "Dozy":
        return "Show calm canine neutrality: awake, relaxed eyes, closed mouth, ears resting naturally, and an upright seated posture. Include the full head, chest, front legs, and paws with correct canine anatomy."
    if name == "Henrietta":
        return "Show calm avian neutrality: bright attentive eye, closed beak, and natural standing posture. Include her full head, body, wings, tail, and visible feet with correct chicken anatomy."
    return (
        "Show composed neutrality: level brows, relaxed jaw, softly closed mouth, and attentive forward eyes. "
        "Keep the character's habitual posture from the source but simplify the pose: both shoulders visible, arms separated, and any visible hands fully inside the canvas with natural anatomy."
    )


def main() -> None:
    character_files = sorted(PENDING.glob("*.md"))
    if not character_files:
        refresh_existing_palettes()
        apply_review_corrections()
        print("Refreshed pending-cast palettes from permanent references")
        return
    cast_plan = []
    for md_path in character_files:
        name = md_path.stem
        char_id = name.lower()
        text = md_path.read_text(encoding="utf-8")
        body = section(text, "Body")
        soul = section(text, "Soul")
        desc = description(text)
        dest_bio = ROOT / "references" / char_id / md_path.name
        dest_bio.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(md_path), str(dest_bio))

        sprite_sets = []
        for set_id, display, source_name in set_plan(name):
            source = PENDING / source_name
            dest_dir = ROOT / "references" / char_id / set_id
            dest_dir.mkdir(parents=True, exist_ok=True)
            source_dest = dest_dir / f"{char_id}_{set_id}_source_sprite.png"
            shutil.move(str(source), str(source_dest))
            top, bottom = palette(source_dest)
            ref_rel = source_dest.relative_to(ROOT).as_posix()
            sprite_sets.append(
                {
                    "id": set_id,
                    "display_name": display,
                    "asset_stem": f"{char_id}_{set_id}",
                    "style": "seiyo",
                    "expression_pack": "seiyo-26",
                    "outfit_anchor": outfit_for(name, set_id, display, body),
                    "set_notes": (
                        "Bootstrap specification. The source sprite is the provisional identity/outfit reference until the generated neutral is visually accepted. "
                        + ("This statue set intentionally supports neutral only." if set_id == "statue" else "Future expressions are mapped to Seiyo-26 and must be generated independently from the approved neutral.")
                    ),
                    "references": [
                        {
                            "path": ref_rel,
                            "role": "identity-base",
                            "notes": "Provisional bootstrap reference for identity, costume or form construction, colors, and distinctive landmarks; do not reproduce pixel rendering or the exact source pose.",
                        }
                    ],
                    "background": {"mode": "character", "top": top, "bottom": bottom},
                    "expression_overrides": {"neutral": {"instruction": neutral_instruction(name, set_id)}},
                }
            )
            cast_plan.append(
                {
                    "character": name,
                    "set": set_id,
                    "display": display,
                    "source": ref_rel,
                    "gradient": f"{top} to {bottom}",
                    "future_expressions": "neutral only" if set_id == "statue" else "Seiyo-26",
                }
            )

        spec = {
            "schema_version": 1,
            "id": char_id,
            "display_name": name,
            "identity_anchor": identity_for(name, body, sprite_sets[0]["id"]),
            "personality_notes": (desc + " " + soul).strip(),
            "physicality_notes": body,
            "sprite_sets": sprite_sets,
        }
        out = ROOT / "characters" / f"{char_id}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    plan_lines = [
        "# Full cast default portrait plan",
        "",
        "All non-statue sprite sets use the shared Seiyo-26 taxonomy for future independent expression generation. This pass generates only neutral. Caldarus's statue is permanently neutral-only.",
        "",
        "| Character | Sprite set | Source | Fixed gradient | Future expressions |",
        "|---|---|---|---|---|",
    ]
    for item in cast_plan:
        plan_lines.append(
            f"| {item['character']} | {item['set']} ({item['display']}) | `{item['source']}` | {item['gradient']} | {item['future_expressions']} |"
        )
    (ROOT / "compiled" / "full_cast_default_plan.md").write_text("\n".join(plan_lines) + "\n", encoding="utf-8")
    print(f"Prepared {len(character_files)} characters and {len(cast_plan)} sprite sets")


if __name__ == "__main__":
    main()
