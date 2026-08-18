"""Generate a contact sheet of cropped portrait samples for visual review."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = Path(__file__).parent / "portraits-cropped"
REVIEW_FILE = Path(__file__).parent / "crop_review_contact_sheet.png"

# Pick one neutral (or first available) closed portrait per character
CHARACTERS = [
    "Adeline", "Balor", "Caldarus", "Celine", "Darcy", "Darren", "Dell",
    "Dozy", "Eiland", "Elsie", "Errol", "Great Bird", "Hayden", "Hemlock",
    "Henrietta", "Holt", "Josephine", "Juniper", "Landen", "Linnet",
    "Louis", "Luc", "Maple", "March", "Merri", "Nora", "Olric", "Reina",
    "Ryis", "Seridia", "Stillwell", "Taliferro", "Terithia", "Valen",
    "Vera", "Wheedle", "Wiscar", "Wynne", "Zorel",
]


def find_sample(char_dir):
    """Find a representative closed portrait — prefer neutral spring."""
    if not char_dir.is_dir():
        return None

    all_files = sorted(char_dir.rglob("*.png"))
    for f in all_files:
        if "neutral" in f.stem:
            return f
    return all_files[0] if all_files else None


def main():
    samples = []
    for char in CHARACTERS:
        if char == "Great Bird":
            continue
        char_dir = OUTPUT_DIR / char
        f = find_sample(char_dir)
        if f:
            samples.append((char, f))

    cols = 8
    rows = (len(samples) + cols - 1) // cols
    thumb = 180
    label_h = 20
    cell = thumb + label_h
    margin = 4

    sheet_w = cols * (thumb + margin) + margin
    sheet_h = rows * (cell + margin) + margin
    sheet = Image.new("RGBA", (sheet_w, sheet_h), (236, 231, 223, 255))
    draw = ImageDraw.Draw(sheet)

    for i, (name, path) in enumerate(samples):
        col = i % cols
        row = i // cols
        x = margin + col * (thumb + margin)
        y = margin + row * (cell + margin)

        img = Image.open(path)
        sheet.paste(img, (x, y), img)
        draw.text((x + 2, y + thumb + 2), name, fill=(60, 50, 40))

    sheet.save(REVIEW_FILE)
    print(f"Contact sheet saved: {REVIEW_FILE}")
    print(f"{len(samples)} characters shown")


if __name__ == "__main__":
    main()
