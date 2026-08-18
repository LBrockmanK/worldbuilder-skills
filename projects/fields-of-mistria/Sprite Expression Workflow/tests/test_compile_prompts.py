from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import compile_prompts as compiler


class CompilePromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.character = compiler.load_json(ROOT / "characters" / "celine.json")
        compiler.validate_character(cls.character)
        cls.sprite_set = compiler.select_sprite_set(cls.character, "spring")
        cls.style = compiler.load_style("seiyo")
        cls.seiyo = compiler.load_expression_pack("seiyo-26")

    def test_pack_sizes_are_stable(self) -> None:
        self.assertEqual(len(self.seiyo["expressions"]), 26)
        self.assertEqual(len(compiler.load_expression_pack("core-24")["expressions"]), 24)

    def test_identity_anchor_contains_no_mutable_expression_or_background(self) -> None:
        anchor = self.character["identity_anchor"].lower()
        for forbidden in ("grin", "smile", "expression", "background", "gradient"):
            self.assertNotIn(forbidden, anchor)

    def test_character_gradient_is_constant(self) -> None:
        chosen = {"neutral", "happy", "annoyed", "angry", "sad", "surprised"}
        document = compiler.compile_document(
            self.character, self.sprite_set, self.seiyo, self.style, chosen
        )
        self.assertEqual(document.count("Background gradient: soft aqua-teal at the top fading to warm pale cream"), 6)
        self.assertNotIn("Resolved gradient:", document)

    def test_non_character_background_mode_is_rejected(self) -> None:
        sprite_set = copy.deepcopy(self.sprite_set)
        sprite_set["background"]["mode"] = "emotion"
        with self.assertRaises(compiler.SpecError):
            compiler.validate_sprite_set(sprite_set, self.seiyo)

    def test_legacy_heading_is_followed_directly_by_prompt(self) -> None:
        document = compiler.compile_document(
            self.character, self.sprite_set, self.seiyo, self.style, {"annoyed"}
        )
        lines = document.splitlines()
        heading_index = lines.index("--- ANNOYED ---")
        self.assertTrue(lines[heading_index + 1].startswith(self.style["prefix"]))

    def test_core_24_compiles_with_character_palette(self) -> None:
        sprite_set = copy.deepcopy(self.sprite_set)
        sprite_set["expression_pack"] = "core-24"
        sprite_set["expression_overrides"] = {}
        pack = compiler.load_expression_pack("core-24")
        document = compiler.compile_document(
            self.character, sprite_set, pack, self.style, None
        )
        self.assertEqual(document.count("\n--- "), 24)

    def test_celine_has_a_complete_bespoke_seiyo_layer(self) -> None:
        celine = compiler.load_json(ROOT / "characters" / "celine.json")
        compiler.validate_character(celine)
        spring = compiler.select_sprite_set(celine, "spring")
        compiler.validate_sprite_set(spring, self.seiyo)
        self.assertEqual(set(spring["expression_overrides"]), {item["id"] for item in self.seiyo["expressions"]})
        notes = " ".join(item["instruction"].lower() for item in spring["expression_overrides"].values())
        self.assertNotIn("crack her knuckles", notes)
        self.assertNotIn("athletic swagger", notes)

    def test_celine_compiles_with_one_constant_background(self) -> None:
        celine = compiler.load_json(ROOT / "characters" / "celine.json")
        spring = compiler.select_sprite_set(celine, "spring")
        compiler.validate_sprite_set(spring, self.seiyo)
        character_document = compiler.compile_document(celine, spring, self.seiyo, self.style, None)
        self.assertEqual(character_document.count("\n--- "), 26)
        self.assertEqual(
            character_document.count("soft aqua-teal at the top fading to warm pale cream"), 26
        )
        self.assertNotIn("dusty mauve", character_document)

    def test_celine_asset_names_are_semantic(self) -> None:
        celine = compiler.load_json(ROOT / "characters" / "celine.json")
        spring = compiler.select_sprite_set(celine, "spring")
        self.assertEqual(spring["asset_stem"], "celine_spring")
        self.assertEqual(spring["references"][0]["path"], "sprites/celine/spring/celine_spring_neutral.png")
        self.assertEqual(f"{spring['asset_stem']}_happy.png", "celine_spring_happy.png")

    def test_celine_production_manifest_resolves_existing_files(self) -> None:
        manifest_path = ROOT / "sprites" / "celine" / "spring" / "manifest.json"
        manifest = compiler.load_json(manifest_path)
        self.assertEqual(manifest["base_expression"], "neutral")
        self.assertEqual(
            set(manifest["expressions"]),
            {item["id"] for item in self.seiyo["expressions"]},
        )
        for filename in manifest["expressions"].values():
            self.assertTrue((manifest_path.parent / filename).is_file(), filename)

    def test_juniper_has_a_complete_bespoke_seiyo_layer(self) -> None:
        juniper = compiler.load_json(ROOT / "characters" / "juniper.json")
        compiler.validate_character(juniper)
        spring = compiler.select_sprite_set(juniper, "spring")
        compiler.validate_sprite_set(spring, self.seiyo)
        self.assertEqual(
            set(spring["expression_overrides"]),
            {item["id"] for item in self.seiyo["expressions"]},
        )
        self.assertEqual(spring["references"][0]["path"], "sprites/juniper/spring/juniper_spring_neutral.png")
        self.assertEqual(spring["references"][0]["role"], "identity-base")

    def test_juniper_production_manifest_resolves_existing_files(self) -> None:
        manifest_path = ROOT / "sprites" / "juniper" / "spring" / "manifest.json"
        manifest = compiler.load_json(manifest_path)
        self.assertEqual(manifest["base_expression"], "neutral")
        self.assertEqual(
            set(manifest["expressions"]),
            {item["id"] for item in self.seiyo["expressions"]},
        )
        for filename in manifest["expressions"].values():
            self.assertTrue((manifest_path.parent / filename).is_file(), filename)


if __name__ == "__main__":
    unittest.main()
