"""Composes each month's four panels into one shelter-style overview image per language.

Usage: python3 mockup.py [month-key ...]   (reads ../preview/monthly/<lang>/<key>/*.png)
"""
import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).parent
PREV = HERE.parent / "preview" / "monthly"
S = 0.5  # previews are 2x; draw at 1 css px


def compose(lang, key):
    d = PREV / lang / key
    im = {p: Image.open(d / f"{p}.png") for p in ("front-15x4", "side-4x4", "backdrop-12x4")}
    im = {k: v.resize((int(v.width * S), int(v.height * S))) for k, v in im.items()}
    gap, pad = 24, 30
    W = 400 + 1200 + gap + 2 * pad
    H = 400 + 400 + gap + 2 * pad + 20
    sheet = Image.new("RGB", (W, H), "#7d7d7d")
    ImageDraw.Draw(sheet).text((pad, 12), f"{key.upper()}  |  {lang.upper()}  |  front, side, backdrop", fill="white")
    sheet.paste(im["front-15x4"], ((W - 1500) // 2, pad + 20))
    y = pad + 20 + 400 + gap
    sheet.paste(im["side-4x4"], (pad, y))
    sheet.paste(im["backdrop-12x4"], (pad + 400 + gap, y))
    out = HERE.parent / "preview" / "monthly" / "mockups"
    out.mkdir(parents=True, exist_ok=True)
    sheet.save(out / f"{key}-{lang}.png")


if __name__ == "__main__":
    keys = sys.argv[1:] or sorted(p.name for p in (PREV / "hi").iterdir() if p.is_dir() and p.name != "mockups")
    for k in keys:
        for lang in ("hi",):
            compose(lang, k)
            print("mockup", k, lang)
