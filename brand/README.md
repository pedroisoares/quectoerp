**English** | [Português (Brasil)](README.pt-BR.md)

# QuectoERP brand

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logo/quectoerp-logo-on-dark.svg">
  <img src="logo/quectoerp-logo.svg" alt="QuectoERP" height="64">
</picture>

This folder holds the QuectoERP logo, favicon and color tokens. The brand is meant to change as the project grows, so every asset here is **generated** from one file, [`brand.json`](brand.json). Change that file, run the build, and every logo, icon and token follows.

## The idea

**quecto** (symbol **q**, factor 10⁻³⁰) is the smallest prefix in the International System of Units. The symbol is that **q**, drawn as a single geometric stroke. The dot at its top right is the exponent, as in 10⁻³⁰: the notation of science and measurement. The wordmark is lowercase `quecto` in the ink color, with `ERP` in the accent color.

The teal palette reads as stable and calm, and keeps the brand away from the blue used by most ERPs and by the "Quec-" family of trademarks from Quectel. Do not use blue as the brand color.

## Files

| Path | Use |
| --- | --- |
| `logo/quectoerp-logo.svg` | Main logo (symbol + name) on light backgrounds |
| `logo/quectoerp-logo-on-dark.svg` | Main logo on dark backgrounds |
| `logo/quectoerp-logo-mono-black.svg`, `-mono-white.svg` | One-color logo (print, stamps, embossing, photos) |
| `logo/quectoerp-wordmark*.svg` | Name only, for places where the symbol already appears nearby |
| `logo/quectoerp-symbol*.svg` | Symbol only: avatars, app icons, social profiles |
| `favicon/favicon.svg`, `favicon.ico`, `favicon-*.png` | Browser tab icon |
| `favicon/apple-touch-icon.png`, `icon-*.png`, `site.webmanifest` | Home screen and PWA icons |
| `tokens/colors.css` | CSS custom properties for the UI, with light and dark themes |
| `tokens/colors.json` | The same tokens for code, design tools and other platforms |

### Favicon HTML

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

## Colors

| Role | Token | Value | Notes |
| --- | --- | --- | --- |
| Ink | `--q-color-fg` | `#0F2A2A` | Text, symbol tile, wordmark on light |
| Teal | `--q-color-accent` | `#0F766E` | Buttons, links, `ERP` in the logo. 5.5:1 on white (WCAG AA for text) |
| Mint | `--q-color-accent` (dark theme) | `#5EEAD4` | The exponent dot, and the accent on dark backgrounds. Too light for text on white |
| Mist | `--q-color-paper` | `#E6F4F1` | Soft background for marketing pages and highlighted areas |

`tokens/colors.css` also has the full 50–950 teal and neutral scales (`--q-brand-*`, `--q-neutral-*`) and status colors (`--q-status-success|warning|danger|info`). Semantic tokens (`--q-color-*`) switch to dark values with `prefers-color-scheme` or `data-theme="dark"`. Use semantic tokens in components and the raw scales only when no role fits.

## Typography

The logo does not depend on any font: it is drawn as vector strokes. For the UI and documents, use **Inter** for text and **JetBrains Mono** for code and numbers in tables. Both are free (SIL Open Font License). They are listed in `brand.json` and exposed as `--q-font-sans` and `--q-font-mono`.

## Using the logo

- Keep clear space around the logo equal to half the height of the symbol.
- Minimum size: symbol 16 px, full logo 96 px wide on screen.
- Use the provided files. Do not redraw, stretch, rotate, outline, add shadows or change the colors outside the options in `brand.json`.
- On photos or busy backgrounds, use the symbol tile or the one-color version.
- Write the name as **QuectoERP** in text and `quectoerp` in code, packages and domains.

## Changing the brand

Everything lives in [`brand.json`](brand.json):

- `symbol`: the shape of the q. `exponent` (dot at the top right, like the exponent of 10⁻³⁰, current), `particle` (dot in the middle of the q) or `limit` (the stem ends in a foot, the floor of the scale).
- `palette`: which palette in `palettes` to use. `teal` is current; `amber` and `indigo` are ready as alternatives. To add one, give it an `ink`, an `accent` and a `paper` color, and optionally a brighter `highlight` for the dot and dark backgrounds. The build derives the 11-step scales, picks accent shades that meet contrast rules, and adapts the symbol for dark backgrounds.
- `status`, `typography` and `radius` hold the rest.

Then rebuild:

```sh
python3 brand/scripts/build.py      # SVG logos, favicon.svg, manifest, tokens (Python 3.8+, no dependencies)
node brand/scripts/rasterize.mjs    # PNG icons and favicon.ico (Node 18+ and Playwright with Chromium)
```

Commit the generated files with the change to `brand.json`. Do not edit generated files by hand, because the next build overwrites them.

## License

The QuectoERP name and logo identify the project. The files in this folder are part of the repository and follow its license, but using the name or logo in a way that suggests endorsement by the project needs permission from the maintainers.
