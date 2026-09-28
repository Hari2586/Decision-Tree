"""Builds every monthly campaign in English and Hindi.

Usage: python3 build.py [month-key ...]    e.g. python3 build.py 01-jan
Writes monthly/<lang>/<key>/<panel>.html and prints the page names for render.js.
"""
import importlib
import sys

from framework import ROOT, SIZES, legal, page

MODULES = ["m01_jan", "m02_feb", "m03_mar", "m04_apr", "m05_may", "m06_jun",
           "m07_jul", "m08_aug", "m09_sep", "m10_oct", "m11_nov", "m12_dec"]


def build(mod):
    names = []
    for lang in ("en", "hi"):
        out = ROOT / lang / mod.KEY
        out.mkdir(parents=True, exist_ok=True)
        for panel, spec in mod.panels(lang, mod.T[lang]).items():
            w, h, fname = SIZES[panel]
            note = mod.NOTE[lang] if spec.get("note") else ""
            html = page(lang, f"MoneyHoney {mod.KEY} {panel} {lang}", w, h, spec["css"], spec["html"],
                        legal(lang, panel, spec["legal"], note), spec["bg"])
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
