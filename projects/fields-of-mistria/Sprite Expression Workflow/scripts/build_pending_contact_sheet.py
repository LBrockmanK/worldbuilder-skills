from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
pending = sorted((root / "PENDING").glob("*.png"))
files = pending or sorted((root / "diagnostics").glob("*/*/*_neutral_candidate_v1.png"))
thumb_w, thumb_h = 240, 240
label_h = 42
cols = 5
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "#ece7df")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=14)

for i, path in enumerate(files):
    with Image.open(path).convert("RGBA") as src:
        src.thumbnail((thumb_w - 20, thumb_h - 20), Image.Resampling.NEAREST)
        x = (i % cols) * thumb_w + (thumb_w - src.width) // 2
        y = (i // cols) * (thumb_h + label_h) + (thumb_h - src.height) // 2
        bg = Image.new("RGBA", src.size, "white")
        bg.alpha_composite(src)
        sheet.paste(bg.convert("RGB"), (x, y))
    label = path.stem.replace("_", " ")
    tx = (i % cols) * thumb_w + 8
    ty = (i // cols) * (thumb_h + label_h) + thumb_h + 8
    draw.text((tx, ty), label, fill="#252525", font=font)

output = root / "diagnostics" / ("pending-cast-contact-sheet.png" if pending else "full-cast-neutral-v1-contact-sheet.png")
output.parent.mkdir(parents=True, exist_ok=True)
sheet.save(output)
print(output)
