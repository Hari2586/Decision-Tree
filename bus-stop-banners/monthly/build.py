"""Builds every monthly campaign in Hindi: bus stop 1 (monthly theme) and bus stop 2 (product topic).

Usage: python3 build.py [month-key ...]    e.g. python3 build.py 01-jan
Writes monthly/<lang>/<key>/<panel>.html and prints the page names for render.js.
"""
import importlib
import sys

from framework import ROOT, SIZES, footer, page, products_band
import stop_b

MODULES = ["m01_jan", "m02_feb", "m03_mar", "m04_apr", "m05_may", "m06_jun",
           "m07_jul", "m08_aug", "m09_sep", "m10_oct", "m11_nov", "m12_dec"]


def build(mod):
    """Each month module gives panels(lang, t) -> {front, back} and side(lang, t); every panel spec carries
    its background, CSS, HTML and whether it shows a starred figure that needs the footnote."""
    names = []
    for lang in ("hi",):
        out = ROOT / lang / mod.KEY
        out.mkdir(parents=True, exist_ok=True)
        t = mod.T[lang]
        specs = mod.panels(lang, t)
        specs = {"front": specs["front"], "side": mod.side(lang, t), "back": specs["back"]}
        for panel, spec in specs.items():
            w, h, fname = SIZES[panel]
            note = (mod.SIDE_NOTE if panel == "side" else mod.NOTE) if spec.get("note") else ""
            html = page(lang, panel, f"MoneyHoney {mod.KEY} {panel} {lang}", w, h, spec["css"], spec["html"],
                        footer(panel, note), spec["bg"], products_band() if panel == "front" else "")
            (out / f"{fname}.html").write_text(html)
            names.append(f"monthly/{lang}/{mod.KEY}/{fname}")
    t = stop_b.TOPICS[mod.KEY]
    out = ROOT / "hi" / f"{mod.KEY}-b"
    out.mkdir(parents=True, exist_ok=True)
    for panel, spec in (("front", stop_b.front(t)), ("side", stop_b.side(t)), ("back", stop_b.back(t))):
        w, h, fname = SIZES[panel]
        html = page("hi", panel, f"MoneyHoney {mod.KEY} stop 2 {panel}", w, h, spec["css"], spec["html"],
                    footer(panel, t["note"] if spec["note"] else ""), spec["bg"], products_band() if panel == "front" else "")
        (out / f"{fname}.html").write_text(html)
        names.append(f"monthly/hi/{mod.KEY}-b/{fname}")
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
