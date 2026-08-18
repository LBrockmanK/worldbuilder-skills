"""
Crop Fields of Mistria portrait sprite sheets into individual square images.

Source images are 592x180 (two portraits side-by-side: left=mouth closed,
right=mouth open). This script takes the left half (mouth closed) and crops
to a 180x180 square centered on the actual content.

Output: source/portraits-cropped/<Character>/<season>/<filename>.png

Skips: Great Bird (no portrait needed), all Children/baby portraits,
all 296x180 single-frame files.
"""

import os
import sys
import json
from pathlib import Path
from PIL import Image

PORTRAITS_DIR = Path(__file__).parent / "portraits"
OUTPUT_DIR = Path(__file__).parent / "portraits-cropped"
SQUARE_SIZE = 180

SKIP_CHARACTERS = {"Great Bird"}


def content_center_x(img):
    bbox = img.getbbox()
    if bbox is None:
        return img.width // 2
    return (bbox[0] + bbox[2]) // 2


def crop_square(img, size=SQUARE_SIZE, scale_to_fit=False):
    bbox = img.getbbox()
    if bbox and scale_to_fit and (bbox[2] - bbox[0]) > size:
        content_w = bbox[2] - bbox[0]
        scale = size / content_w
        new_w = round(img.width * scale)
        new_h = round(img.height * scale)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        canvas = Image.new("RGBA", (img.width, size), (0, 0, 0, 0))
        canvas.paste(img, (0, size - new_h))
        img = canvas

    cx = content_center_x(img)
    half = size // 2
    left = cx - half
    right = cx + half

    if left < 0:
        left = 0
        right = size
    if right > img.width:
        right = img.width
        left = img.width - size

    left = max(0, left)
    right = min(img.width, right)

    return img.crop((left, 0, right, size))


def relative_output_path(src_path, portraits_dir):
    rel = src_path.relative_to(portraits_dir)
    parts = list(rel.parts)
    character = parts[0]
    remaining = [p for p in parts[1:] if p != "Portraits"]
    return Path(character, *remaining)


def should_skip(src_path, portraits_dir):
    rel = src_path.relative_to(portraits_dir)
    parts = list(rel.parts)
    character = parts[0]

    if character in SKIP_CHARACTERS:
        return True
    if "Children" in parts:
        return True
    return False


def process_file(src_path, portraits_dir, output_dir, flags):
    if should_skip(src_path, portraits_dir):
        return 0

    img = Image.open(src_path)
    w, h = img.size

    if w != 592 or h != 180:
        return 0

    stem = src_path.stem
    rel_out = relative_output_path(src_path, portraits_dir)
    out_dir = output_dir / rel_out.parent

    left_half = img.crop((0, 0, 296, 180))

    left_bbox = left_half.getbbox()
    needs_scale = False
    if left_bbox:
        cw = left_bbox[2] - left_bbox[0]
        if cw > SQUARE_SIZE:
            needs_scale = True

    cropped = crop_square(left_half, scale_to_fit=needs_scale)
    out_dir.mkdir(parents=True, exist_ok=True)
    cropped.save(out_dir / f"{stem}.png")
    return 1


def main():
    if not PORTRAITS_DIR.is_dir():
        print(f"Error: portraits directory not found: {PORTRAITS_DIR}")
        sys.exit(1)

    # Collect all PNGs
    png_files = sorted(PORTRAITS_DIR.rglob("*.png"))
    print(f"Found {len(png_files)} portrait files")

    flags = []
    total_output = 0

    for i, src in enumerate(png_files):
        count = process_file(src, PORTRAITS_DIR, OUTPUT_DIR, flags)
        total_output += count
        if (i + 1) % 200 == 0:
            print(f"  Processed {i + 1}/{len(png_files)}...")

    print(f"\nDone: {total_output} cropped images written to {OUTPUT_DIR}")

    if flags:
        print(f"\n{len(flags)} special cases flagged for review:")
        for f in flags:
            print(f"  [{f['reason']}] {f.get('content_size', f.get('size', '?'))} — {f['file']}")

        flags_file = OUTPUT_DIR / "_flagged_for_review.json"
        with open(flags_file, "w") as fh:
            json.dump(flags, fh, indent=2, default=str)
        print(f"\nFlags saved to {flags_file}")


if __name__ == "__main__":
    main()
