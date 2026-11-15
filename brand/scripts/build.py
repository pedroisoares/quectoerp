#!/usr/bin/env python3
"""Generate the QuectoERP brand assets from brand/brand.json.

Standard library only. Writes:
  brand/logo/*.svg        logo, symbol and wordmark variants
  brand/favicon/favicon.svg and site.webmanifest
  brand/tokens/colors.json and colors.css

PNG and ICO files come from scripts/rasterize.mjs, which reads the SVGs written here.
"""
import json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYMBOLS = ("particle", "exponent", "limit")


# ---------------------------------------------------------------- color math (OKLCH)

def _hex_to_rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]

def _rgb_to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)

def _lin(c):   return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def _delin(c): return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055

def hex_to_oklch(h):
    r, g, b = (_lin(c) for c in _hex_to_rgb(h))
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360

def _oklch_to_rgb(L, C, H):
    a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return [r, g, bb]

def oklch_to_hex(L, C, H):
    while C > 0:  # reduce chroma until the color fits in sRGB
        rgb = _oklch_to_rgb(L, C, H)
        if all(-1e-4 <= c <= 1 + 1e-4 for c in rgb):
            break
        C -= 0.002
    return _rgb_to_hex([_delin(max(0, c)) for c in _oklch_to_rgb(L, max(C, 0), H)])

def luminance(h):
    r, g, b = (_lin(c) for c in _hex_to_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

# Position of each step between the base color (0) and the light/dark end (1).
LIGHT_END, DARK_END = 0.975, 0.25
STEPS = {50: (1, .93), 100: (1, .82), 200: (1, .62), 300: (1, .42), 400: (1, .2), 500: (0, 0),
         600: (-1, .16), 700: (-1, .33), 800: (-1, .52), 900: (-1, .72), 950: (-1, .88)}

def scale(base):
    """11-step scale around a base color. Step 500 is the base itself, lightness is monotonic."""
    L0, C0, H = hex_to_oklch(base)
    out = {}
    for step, (side, t) in STEPS.items():
        if side == 0:
            out[step] = base.upper(); continue
        L = L0 + (LIGHT_END - L0) * t if side > 0 else L0 - (L0 - DARK_END) * t
        # keep the hue, taper chroma toward the ends of the scale
        out[step] = oklch_to_hex(L, C0 * (1 - 0.6 * t ** 2), H)
    return out

def neutral_scale(ink):
    """Neutral greys tinted with the hue of the ink color."""
    _, C, H = hex_to_oklch(ink)
    C = min(C, 0.012)
    Ls = {0: 1.0, 50: .985, 100: .965, 200: .925, 300: .87, 400: .72, 500: .58,
          600: .47, 700: .38, 800: .30, 900: None, 950: .17}
    return {k: (ink.upper() if v is None else oklch_to_hex(v, C if v < 1 else 0, H)) for k, v in Ls.items()}

def first_step(sc, bg, ratio, order=(500, 600, 700, 800, 900)):
    for s in order:
        if contrast(sc[s], bg) >= ratio:
            return s
    return order[-1]


# ---------------------------------------------------------------- geometry

SW = 6  # wordmark stroke, in units of an x-height of 36

def n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")

def arc(cx, cy, r, a0, a1, large, sweep, move=True):
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    return (f"M{n(p0[0])} {n(p0[1])}" if move else "") + f"A{r} {r} 0 {large} {sweep} {n(p1[0])} {n(p1[1])}"

# Each glyph: (role, draw(x) -> svg, advance, extra space before)
GLYPHS = [
    ("ink", lambda x: f'<circle cx="{x+18}" cy="18" r="15"/><path d="M{x+33} 3V50"/>', 36, 0),            # q
    ("ink", lambda x: f'<path d="M{x+3} 3V18A15 15 0 0 0 {x+33} 18V3M{x+33} 18V33"/>', 36, 0),              # u
    ("ink", lambda x: f'<path d="M{x+3.5} 18H{x+33}' + arc(x+18, 18, 15, 0, 50, 1, 0, False) + '"/>', 36, 0),  # e
    ("ink", lambda x: '<path d="' + arc(x+18, 18, 15, -50, 50, 1, 0) + '"/>', 33, 0),                     # c
    ("ink", lambda x: f'<path d="M{x+9} -9V24A9 9 0 0 0 {x+18} 33H{x+21}M{x+2} 3H{x+19}"/>', 22, 0),     # t
    ("ink", lambda x: f'<circle cx="{x+18}" cy="18" r="15"/>', 36, 0),                                     # o
    ("accent", lambda x: f'<path d="M{x+21} 3H{x+3}V33H{x+21}M{x+3} 18H{x+17}"/>', 24, 6),                # E
    ("accent", lambda x: f'<path d="M{x+3} 33V3H{x+13}A7.5 7.5 0 0 1 {x+13} 18H{x+3}M{x+12} 18L{x+22} 33"/>', 25, 0),  # R
    ("accent", lambda x: f'<path d="M{x+3} 33V3H{x+13}A7.5 7.5 0 0 1 {x+13} 18H{x+3}"/>', 22, 0),        # P
]
GAP = 7

def wordmark_body(ink, accent):
    x, parts = 0, {"ink": "", "accent": ""}
    for role, draw, adv, before in GLYPHS:
        x += before
        parts[role] += draw(x)
        x += adv + GAP
    width = x - GAP
    body = (f'<g fill="none" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">'
            f'<g stroke="{ink}">{parts["ink"]}</g><g stroke="{accent}">{parts["accent"]}</g></g>')
    return width, body

def q_parts(symbol, dot):
    """The q of the symbol in local units. Returns (stroke elements, filled extras, bbox, stroke width)."""
    sw = 7.5
    strokes = ['<circle cx="18" cy="18" r="15"/>']
    if symbol == "limit":
        strokes.append('<path d="M33 3V47H42"/>'); bbox = [3 - sw/2, 3 - sw/2, 42 + sw/2, 47 + sw/2]
    else:
        strokes.append('<path d="M33 3V49"/>'); bbox = [3 - sw/2, 3 - sw/2, 33 + sw/2, 49 + sw/2]
    extra = []
    if symbol == "exponent":
        extra.append(("dot", '<circle cx="44" cy="-5" r="5.5"/>')); bbox = [bbox[0], -10.5, 49.5, bbox[3]]
    if symbol == "particle":
        extra.append(("dot", '<circle cx="18" cy="18" r="5.5"/>'))
    return strokes, extra, bbox, sw

def symbol_inner(symbol, bg, fg, dot, pad=0.2, rx=14, mono=None):
    """Contents of a 64x64 symbol. mono=color draws a single-color knockout version."""
    strokes, extra, bb, sw = q_parts(symbol, dot)
    gw, gh = bb[2] - bb[0], bb[3] - bb[1]
    s = 64 * (1 - 2 * pad) / max(gw, gh)
    tx, ty = 32 - (bb[0] + gw / 2) * s, 32 - (bb[1] + gh / 2) * s
    tr = f'translate({n(tx)} {n(ty)}) scale({n(s)})'
    if mono:
        holes = (f'<g transform="{tr}"><g fill="none" stroke="#000" stroke-width="{sw}" stroke-linecap="round" '
                 f'stroke-linejoin="round">{"".join(strokes)}</g>' +
                 "".join(e.replace("<circle", '<circle fill="#000"') for _, e in extra) + "</g>")
        mid = f"q-knockout-{symbol}"
        return (f'<defs><mask id="{mid}"><rect width="64" height="64" fill="#fff"/>{holes}</mask></defs>'
                f'<rect width="64" height="64" rx="{rx}" fill="{mono}" mask="url(#{mid})"/>')
    out = f'<rect width="64" height="64" rx="{rx}" fill="{bg}"/>' if bg else ""
    out += (f'<g transform="{tr}"><g fill="none" stroke="{fg}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round">{"".join(strokes)}</g>' +
            "".join(e.replace("<circle", f'<circle fill="{dot}"') for _, e in extra) + "</g>")
    return out

def svg(view_box, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{body}</svg>\n")

def symbol_svg(*a, title="QuectoERP", **k):
    return svg("0 0 64 64", symbol_inner(*a, **k), title)

def wordmark_svg(ink, accent, title="QuectoERP"):
    w, body = wordmark_body(ink, accent)
    return svg(f"-4 -13 {n(w + 8)} 70", body, title)

def lockup_svg(symbol, sym_colors, ink, accent, title="QuectoERP", mono=None):
    w, body = wordmark_body(ink, accent)
    inner = symbol_inner(symbol, *sym_colors, mono=mono)
    return svg(f"-2 -14 {n(64 + 22 + w + 6)} 68",
               f'<g transform="translate(0 -12)">{inner}</g><g transform="translate(86 0)">{body}</g>', title)


# ---------------------------------------------------------------- build

def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", rel)

def main():
    cfg = json.load(open(os.path.join(ROOT, "brand.json"), encoding="utf-8"))
    sym = cfg["symbol"]
    if sym not in SYMBOLS:
        sys.exit(f"brand.json: symbol must be one of {SYMBOLS}")
    pal = cfg["palettes"][cfg["palette"]]
    ink, accent, paper = pal["ink"].upper(), pal["accent"].upper(), pal["paper"].upper()
    brand, neutral = scale(accent), neutral_scale(ink)
    white = "#FFFFFF"

    # Accent variants that stay legible: >= 3:1 for graphics (logo), >= 4.5:1 for text.
    accent_on_light = brand[first_step(brand, white, 3.0)]
    text_on_light = brand[first_step(brand, white, 4.5)]
    accent_on_dark = brand[first_step(brand, ink, 3.0, order=(500, 400, 300, 200))]
    # Optional brighter companion of the accent, for the dot and for dark backgrounds.
    highlight = pal.get("highlight", "").upper() or None
    if highlight and contrast(highlight, ink) >= 3:
        accent_on_dark = highlight
    light_ink = neutral[50]
    # The symbol tile is dark ink with a white q; on a dark background the tile switches to the accent.
    dot_on_ink = accent if contrast(accent, ink) >= 3 else accent_on_dark
    tile_light = (ink, white, dot_on_ink)
    tile_dark = (accent if contrast(accent, ink) >= 3 else accent_on_dark, ink, ink)

    # logos
    write("logo/quectoerp-logo.svg", lockup_svg(sym, tile_light, ink, accent_on_light))
    write("logo/quectoerp-logo-on-dark.svg", lockup_svg(sym, tile_dark, light_ink, accent_on_dark))
    write("logo/quectoerp-logo-mono-black.svg", lockup_svg(sym, (None, None, None), "#000000", "#000000", mono="#000000"))
    write("logo/quectoerp-logo-mono-white.svg", lockup_svg(sym, (None, None, None), "#FFFFFF", "#FFFFFF", mono="#FFFFFF"))
    write("logo/quectoerp-wordmark.svg", wordmark_svg(ink, accent_on_light))
    write("logo/quectoerp-wordmark-on-dark.svg", wordmark_svg(light_ink, accent_on_dark))
    write("logo/quectoerp-symbol.svg", symbol_svg(sym, *tile_light))
    write("logo/quectoerp-symbol-on-dark.svg", symbol_svg(sym, *tile_dark))
    write("logo/quectoerp-symbol-mono.svg", symbol_svg(sym, None, None, None, mono="#000000"))

    # favicon: tighter padding so the q stays readable at 16 px
    write("favicon/favicon.svg", symbol_svg(sym, *tile_light, pad=0.12, rx=12))
    # sources for raster icons (not committed as deliverables, read by rasterize.mjs)
    write("favicon/src/apple-touch-icon.svg", symbol_svg(sym, *tile_light, pad=0.2, rx=0))
    write("favicon/src/maskable.svg", symbol_svg(sym, *tile_light, pad=0.28, rx=0))
    manifest = {
        "name": cfg["name"], "short_name": cfg["name"],
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
        "theme_color": ink, "background_color": white, "display": "standalone",
    }
    write("favicon/site.webmanifest", json.dumps(manifest, indent=2) + "\n")

    # tokens
    tokens = {
        "$comment": "Generated by brand/scripts/build.py from brand/brand.json. Do not edit by hand.",
        "palette": cfg["palette"], "symbol": sym,
        "color": {
            "brand": brand, "neutral": neutral, "status": cfg["status"],
            "role": {
                "light": {"bg": white, "surface": neutral[50], "fg": ink, "fg-muted": neutral[600],
                          "border": neutral[200], "accent": accent, "accent-graphic": accent_on_light,
                          "accent-text": text_on_light, "on-accent": ink if contrast(accent, ink) >= 4.5 else white,
                          "paper": paper},
                "dark": {"bg": neutral[950], "surface": ink, "fg": light_ink, "fg-muted": neutral[400],
                         "border": neutral[800], "accent": accent_on_dark, "accent-graphic": accent_on_dark,
                         "accent-text": accent_on_dark if contrast(accent_on_dark, neutral[950]) >= 4.5
                                        else brand[first_step(brand, neutral[950], 4.5, order=(500, 400, 300, 200))],
                         "on-accent": ink, "paper": neutral[900]},
            },
        },
        "font": {k: ", ".join(f'"{f}"' if " " in f else f for f in v) for k, v in cfg["typography"].items()},
    }
    write("tokens/colors.json", json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")

    css = ["/* Generated by brand/scripts/build.py from brand/brand.json. Do not edit by hand. */", ":root {"]
    for k, v in brand.items():   css.append(f"  --q-brand-{k}: {v};")
    for k, v in neutral.items(): css.append(f"  --q-neutral-{k}: {v};")
    for k, v in cfg["status"].items(): css.append(f"  --q-status-{k}: {v};")
    for k, v in tokens["font"].items(): css.append(f"  --q-font-{k}: {v};")
    roles = tokens["color"]["role"]
    for k, v in roles["light"].items(): css.append(f"  --q-color-{k}: {v};")
    css += ["}", "", "@media (prefers-color-scheme: dark) {", '  :root:not([data-theme="light"]) {']
    css += [f"    --q-color-{k}: {v};" for k, v in roles["dark"].items()]
    css += ["  }", "}", "", ':root[data-theme="dark"] {']
    css += [f"  --q-color-{k}: {v};" for k, v in roles["dark"].items()]
    css += ["}", ""]
    write("tokens/colors.css", "\n".join(css))

    print(f"\nsymbol={sym} palette={cfg['palette']}")
    print(f"accent {accent} on white {contrast(accent, white):.2f}:1, on ink {contrast(accent, ink):.2f}:1")
    print(f"accent-graphic {accent_on_light} ({contrast(accent_on_light, white):.2f}:1), "
          f"accent-text {text_on_light} ({contrast(text_on_light, white):.2f}:1)")

if __name__ == "__main__":
    main()
