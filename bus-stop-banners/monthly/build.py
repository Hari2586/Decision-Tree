"""Builds every monthly campaign in English and Hindi.

Usage: python3 build.py [month-key ...]    e.g. python3 build.py 01-jan
Writes monthly/<lang>/<key>/<panel>.html and prints the page names for render.js.
"""
import importlib
import sys

from framework import ROOT, SIZES, legal, page, products_band
from sides import side_panel

MODULES = ["m01_jan", "m02_feb", "m03_mar", "m04_apr", "m05_may", "m06_jun",
           "m07_jul", "m08_aug", "m09_sep", "m10_oct", "m11_nov", "m12_dec"]


def build(mod):
    names = []
    for lang in ("en", "hi"):
        out = ROOT / lang / mod.KEY
        out.mkdir(parents=True, exist_ok=True)
        specs = mod.panels(lang, mod.T[lang])
        specs = {"front": specs["front"], "side": side_panel(mod, lang), "back": specs["back"]}
        for old in ("side-left-4x4.html", "side-right-4x4.html"):
            (out / old).unlink(missing_ok=True)
        for panel, spec in specs.items():
            w, h, fname = SIZES[panel]
            note = mod.NOTE["en"] if spec.get("note") else ""
            html = page(lang, f"MoneyHoney {mod.KEY} {panel} {lang}", w, h, spec["css"], spec["html"],
                        legal(lang, panel, spec["legal"], note), spec["bg"],
                        products_band(lang) if panel == "front" else "")
            (out / f"{fname}.html").write_text(html)
            names.append(f"monthly/{lang}/{mod.KEY}/{fname}")
    return names


if __name__ == "__main__":
    wanted = sys.argv[1:]
    names = []
    for m in MODULES:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError:
            continue
        if wanted and mod.KEY not in wanted:
            continue
        names += build(mod)
    print(" ".join(names))
