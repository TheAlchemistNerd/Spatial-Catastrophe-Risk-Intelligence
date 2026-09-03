"""Create contact sheets and extract text for PDF quality assurance."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output" / "pdf" / "SCRI_Positive_Product_Narrative_Edition.pdf"
RENDER = ROOT / "tmp" / "pdfs" / "source-url-render"
CONTACT = ROOT / "tmp" / "pdfs" / "source-url-contact-sheets"
CONTACT.mkdir(parents=True, exist_ok=True)


def get_font(size: int):
    path = Path("C:/Windows/Fonts/arial.ttf")
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()


reader = PdfReader(str(PDF))
text = "\n\n".join((page.extract_text() or "") for page in reader.pages)
(ROOT / "tmp" / "pdfs" / "SCRI_Positive_Product_Narrative_Edition.txt").write_text(text, encoding="utf-8")

pages = sorted(RENDER.glob("page-*.png"))
per_sheet, cols = 12, 3
thumb_w, thumb_h = 330, 427
margin, label_h = 30, 34
rows = math.ceil(per_sheet / cols)

for sheet_idx in range(math.ceil(len(pages) / per_sheet)):
    subset = pages[sheet_idx * per_sheet:(sheet_idx + 1) * per_sheet]
    canvas = Image.new(
        "RGB",
        (cols * (thumb_w + margin) + margin, rows * (thumb_h + label_h + margin) + margin),
        "#DDE4E7",
    )
    draw = ImageDraw.Draw(canvas)
    for idx, path in enumerate(subset):
        page_no = sheet_idx * per_sheet + idx + 1
        with Image.open(path) as source:
            thumb = source.convert("RGB")
            thumb.thumbnail((thumb_w, thumb_h))
            col, row = idx % cols, idx // cols
            x = margin + col * (thumb_w + margin)
            y = margin + row * (thumb_h + label_h + margin)
            canvas.paste(thumb, (x, y))
            draw.rectangle((x - 1, y - 1, x + thumb.width, y + thumb.height), outline="#52636B", width=2)
            draw.text((x, y + thumb_h + 6), f"Page {page_no}", fill="#1C2C34", font=get_font(19))
    canvas.save(CONTACT / f"contact-{sheet_idx + 1:02d}.jpg", quality=88)

print(f"pages={len(reader.pages)} rendered={len(pages)} sheets={math.ceil(len(pages) / per_sheet)}")
