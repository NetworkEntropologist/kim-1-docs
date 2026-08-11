#!/usr/bin/env python3
"""
gen_memmap.py -- generate a memory-map SVG from a declarative region list.

Edit the DATA structure below (or point --data at a JSON file with the same
shape) and re-run. Intended to be invoked at docs build time so the diagram
never has to be drawn by hand.

Usage:
    python3 gen_memmap.py [-o kim1_memmap.svg] [--data map.json]
"""

import argparse
import json

# --------------------------------------------------------------------------
# 1. THE DATA -- this is the only part you normally touch
# --------------------------------------------------------------------------
# Regions are listed bottom -> top.  "w" is a layout weight (the map is not
# to scale, exactly like the original figure).  "detail" links a region to an
# expanded inset column.  "hatch" cross-hatches a box, "torn" draws the
# open-ended break used for expansion space.

DATA = {
    "title": "KIM-1 Memory Map",
    "subtitle": "after Figure 3.12, KIM-1 User Manual",
    "k_span": 0x0400,          # size of one "K" block (1 KB), bracket column
    "k_max": 0x2000,           # draw K brackets up to this address
    "page_span": 0x0100,       # size of one page (256 B), page-number column
    "page_max": 0x2000,        # draw page numbers up to this address
    "main": [
        {"lo": 0x0000, "hi": 0x01FF, "label": "PAGE 0 / STACK", "w": 1.1, "detail": "low"},
        {"lo": 0x0200, "hi": 0x03FF, "label": "RAM", "w": 0.9},
        {"lo": 0x0400, "hi": 0x13FF, "label": "DECODED FOR\n4K EXPANSION", "w": 3.4},
        {"lo": 0x1400, "hi": 0x16FF, "label": "", "w": 1.0},
        {"lo": 0x1700, "hi": 0x17FF, "label": "6530 I/O · RAM", "w": 1.0, "detail": "io"},
        {"lo": 0x1800, "hi": 0x1BFF, "label": "KIM ROM\n6530-003", "w": 1.3},
        {"lo": 0x1C00, "hi": 0x1FFF, "label": "KIM ROM\n6530-002", "w": 1.3},
        {"lo": 0x2000, "hi": 0xFFFF, "label": "AVAILABLE FOR\nEXPANSION", "w": 1.7, "torn": True},
    ],
    "details": {
        "low": [
            {"lo": 0x0000, "hi": 0x00EE, "label": "PAGE 0", "w": 1.4},
            {"lo": 0x00EF, "hi": 0x00FF, "label": "", "w": 0.6, "hatch": True,
             "note": "17 BYTES RESERVED FOR KIM"},
            {"lo": 0x0100, "hi": 0x01FF, "label": "STACK · PAGE 1", "w": 1.2,
             "note": "SP INITIALIZED TO 0x01FF"},
        ],
        "io": [
            {"lo": 0x1700, "hi": 0x173F, "label": "I/O + TIMER\n6530-003", "w": 1.2,
             "group": "APPLICATION I/O"},
            {"lo": 0x1740, "hi": 0x177F, "label": "I/O + TIMER\n6530-002", "w": 1.2,
             "group": "KIM I/O"},
            {"lo": 0x1780, "hi": 0x17BF, "label": "64-BYTE RAM\n6530-003", "w": 1.2,
             "group": "APPLICATION RAM"},
            {"lo": 0x17C0, "hi": 0x17E6, "label": "64-BYTE RAM\n6530-002", "w": 1.0,
             "group": "APPLICATION RAM"},
            {"lo": 0x17E7, "hi": 0x17FF, "label": "", "w": 0.7,
             "group": "KIM RAM"},
        ],
    },
}

# --------------------------------------------------------------------------
# 2. STYLE TOKENS
# --------------------------------------------------------------------------
UNIT        = 52          # px per weight unit
BOX_W       = 190         # main column width
DET_W       = 168         # detail column width
MAIN_X      = 172
DET_X       = 520
TOP_PAD     = 64
BOT_PAD     = 36
STROKE      = "#2b2b2b"
FILL        = "#ffffff"
FILL_ALT    = "#f2efe9"   # ROM / occupied regions
INK_DIM     = "#6b6b6b"
MONO        = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS        = "Avenir, 'Trebuchet MS', Verdana, sans-serif"


def hexs(v):
    return f"0x{v:04X}"


class SVG:
    def __init__(self):
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def line(self, x1, y1, x2, y2, dash=None, color=STROKE, w=1.4):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{color}" stroke-width="{w}"{d}/>')

    def rect(self, x, y, w, h, fill=FILL, hatch=False):
        f = "url(#hatch)" if hatch else fill
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                 f'fill="{f}" stroke="{STROKE}" stroke-width="1.6"/>')

    def text(self, x, y, s, size=12, anchor="middle", mono=False,
             color=STROKE, weight="normal", spacing=None):
        fam = MONO if mono else SANS
        sp = f' letter-spacing="{spacing}"' if spacing else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" '
                 f'text-anchor="{anchor}" fill="{color}" font-weight="{weight}"{sp}>{s}</text>')

    def multiline(self, x, y_center, s, size=12, **kw):
        lines = s.split("\n")
        lh = size * 1.25
        y0 = y_center - lh * (len(lines) - 1) / 2 + size * 0.35
        for i, ln in enumerate(lines):
            self.text(x, y0 + i * lh, ln, size=size, **kw)


def wavy(x0, x1, y, amp=4, n=7):
    """A hand-torn horizontal edge as an SVG path fragment."""
    step = (x1 - x0) / n
    d = f"M {x0:.1f} {y:.1f} "
    for i in range(n):
        cx = x0 + step * (i + 0.5)
        ex = x0 + step * (i + 1)
        a = amp if i % 2 == 0 else -amp
        d += f"Q {cx:.1f} {y + a:.1f} {ex:.1f} {y:.1f} "
    return d


def build(data):
    svg = SVG()
    main = data["main"]

    # geometry: y position of each main region (top edge), bottom -> top order
    total_h = sum(r["w"] for r in main) * UNIT
    height = TOP_PAD + total_h + BOT_PAD
    y = TOP_PAD + total_h
    for r in main:
        h = r["w"] * UNIT
        r["y_bot"], r["y_top"] = y, y - h
        y -= h

    def addr_to_y(a):
        for r in main:
            if r["lo"] <= a <= r["hi"] + 1:
                span = r["hi"] + 1 - r["lo"]
                frac = (a - r["lo"]) / span if span else 0
                return r["y_bot"] - frac * (r["y_bot"] - r["y_top"])
        return None

    # ---- title -----------------------------------------------------------
    svg.text(MAIN_X + BOX_W / 2, 26, data["title"].upper(), size=15,
             weight="bold", spacing="2px")
    if data.get("subtitle"):
        svg.text(MAIN_X + BOX_W / 2, 44, data["subtitle"], size=10.5,
                 color=INK_DIM)

    # ---- main column boxes ----------------------------------------------
    for r in main:
        x, w = MAIN_X, BOX_W
        yt, yb = r["y_top"], r["y_bot"]
        occupied = ("ROM" in r["label"]) or r.get("detail") == "io"
        if r.get("torn"):
            gap_top, gap_bot = yt + (yb - yt) * .58, yt + (yb - yt) * .70
            # upper fragment (open top edge suggests it continues)
            svg.add(f'<path d="M {x} {gap_top:.1f} L {x} {yt} L {x+w} {yt} '
                    f'L {x+w} {gap_top:.1f}" fill="none" stroke="{STROKE}" stroke-width="1.6"/>')
            svg.add(f'<path d="{wavy(x, x+w, gap_top)}" fill="none" '
                    f'stroke="{STROKE}" stroke-width="1.4"/>')
            svg.add(f'<path d="M {x} {gap_bot:.1f} L {x} {yb} L {x+w} {yb} '
                    f'L {x+w} {gap_bot:.1f}" fill="none" stroke="{STROKE}" stroke-width="1.6"/>')
            svg.add(f'<path d="{wavy(x, x+w, gap_bot)}" fill="none" '
                    f'stroke="{STROKE}" stroke-width="1.4"/>')
            svg.multiline(x + w / 2, yt + (gap_top - yt) / 2, r["label"],
                          size=11.5, spacing="1px")
        else:
            svg.rect(x, yt, w, yb - yt, fill=FILL_ALT if occupied else FILL)
            if r["label"]:
                svg.multiline(x + w / 2, (yt + yb) / 2, r["label"],
                              size=11.5, spacing="1px")

        # hex labels on the right edge: start below-line, end above-line
        lx = x + w + 8
        svg.text(lx, yb - 3, hexs(r["lo"]), size=11, anchor="start", mono=True)
        svg.text(lx, yt + 11, hexs(r["hi"]), size=11, anchor="start", mono=True)

    # ---- page-number column (256-byte pages) ----------------------------
    pspan, pmax = data.get("page_span", 0x0100), data.get("page_max", 0)
    px = MAIN_X - 10
    for p in range(pmax // pspan):
        yc = addr_to_y(p * pspan + pspan // 2)
        svg.text(px, yc + 3.5, str(p), size=10, anchor="end",
                 mono=True, color=INK_DIM)
    if pmax:
        svg.text(px, addr_to_y(pmax) - 8, "PAGE", size=9, anchor="end",
                 color=INK_DIM, spacing="1px")

    # ---- K brackets on the left -----------------------------------------
    span, kmax = data["k_span"], data["k_max"]
    bx = MAIN_X - 48
    svg.text(bx - 8, addr_to_y(kmax) - 8, "\u201cK\u201d", size=9,
             anchor="end", color=INK_DIM, spacing="1px")
    for k in range(kmax // span):
        y0, y1 = addr_to_y(k * span), addr_to_y((k + 1) * span)
        svg.line(bx, y0 - 2, bx, y1 + 2, color=INK_DIM, w=1.2)
        svg.line(bx, y0 - 2, bx + 6, y0 - 2, color=INK_DIM, w=1.2)
        svg.line(bx, y1 + 2, bx + 6, y1 + 2, color=INK_DIM, w=1.2)
        svg.text(bx - 8, (y0 + y1) / 2 + 4, f"K{k}", size=11, anchor="end",
                 mono=True, color=INK_DIM)

    # ---- detail insets ---------------------------------------------------
    for r in main:
        key = r.get("detail")
        if not key:
            continue
        boxes = data["details"][key]
        dh = sum(b["w"] for b in boxes) * UNIT * 0.82
        pc = (r["y_top"] + r["y_bot"]) / 2
        d_bot = min(pc + dh / 2, height - BOT_PAD)
        d_top = d_bot - dh

        # dashed connectors parent -> inset
        svg.line(MAIN_X + BOX_W + 60, r["y_top"], DET_X, d_top,
                 dash="5 4", color=INK_DIM, w=1.1)
        svg.line(MAIN_X + BOX_W + 60, r["y_bot"], DET_X, d_bot,
                 dash="5 4", color=INK_DIM, w=1.1)

        yy = d_bot
        for b in boxes:
            h = b["w"] * UNIT * 0.82
            yt = yy - h
            svg.rect(DET_X, yt, DET_W, h, hatch=b.get("hatch", False))
            if b["label"]:
                svg.multiline(DET_X + DET_W / 2, (yt + yy) / 2, b["label"],
                              size=10.5)
            # addresses left of the inset
            svg.text(DET_X - 7, yy - 2, hexs(b["lo"]), size=10, anchor="end", mono=True)
            svg.text(DET_X - 7, yt + 9.5, hexs(b["hi"]), size=10, anchor="end", mono=True)
            b["y_top"], b["y_bot"] = yt, yy
            yy = yt

        # group brackets / notes on the right of the inset
        gx = DET_X + DET_W + 8
        i = 0
        while i < len(boxes):
            b = boxes[i]
            grp = b.get("group")
            if grp:
                j = i
                while j + 1 < len(boxes) and boxes[j + 1].get("group") == grp:
                    j += 1
                y0, y1 = boxes[i]["y_bot"], boxes[j]["y_top"]
                svg.line(gx, y0 - 1, gx, y1 + 1, color=INK_DIM, w=1.2)
                svg.line(gx, y0 - 1, gx - 4, y0 - 1, color=INK_DIM, w=1.2)
                svg.line(gx, y1 + 1, gx - 4, y1 + 1, color=INK_DIM, w=1.2)
                svg.text(gx + 6, (y0 + y1) / 2 + 3.5, grp, size=9.5,
                         anchor="start", color=INK_DIM, spacing="0.5px")
                i = j + 1
            else:
                if b.get("note"):
                    svg.text(gx + 6, (b["y_top"] + b["y_bot"]) / 2 + 3.5,
                             b["note"], size=9.5, anchor="start",
                             color=INK_DIM, spacing="0.5px")
                    svg.line(gx, (b["y_top"] + b["y_bot"]) / 2,
                             gx + 3, (b["y_top"] + b["y_bot"]) / 2,
                             color=INK_DIM, w=1.2)
                i += 1

    width = DET_X + DET_W + 200
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width} {height:.0f}" width="{width}" '
            f'height="{height:.0f}" role="img" aria-label="{data["title"]}">'
            f'<defs><pattern id="hatch" width="7" height="7" '
            f'patternTransform="rotate(45)" patternUnits="userSpaceOnUse">'
            f'<rect width="7" height="7" fill="{FILL}"/>'
            f'<line x1="0" y1="0" x2="0" y2="7" stroke="{STROKE}" stroke-width="1.4"/>'
            f'</pattern></defs>'
            f'<rect width="{width}" height="{height:.0f}" fill="#fbfaf7"/>')
    return head + "".join(svg.parts) + "</svg>"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default="kim1_memmap.svg")
    ap.add_argument("--data", help="optional JSON file with the map definition")
    args = ap.parse_args()
    data = DATA
    if args.data:
        with open(args.data) as f:
            data = json.load(f)
    with open(args.out, "w") as f:
        f.write(build(data))
    print(f"wrote {args.out}")
