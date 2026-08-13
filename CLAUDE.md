# Muneris — house brand

**This is the canonical Muneris brand. Use it as the default for anything
Muneris-branded — this site, decks, documents, diagrams — without asking.**

Do not invent, guess at, or substitute Muneris colours. The values below are
sampled directly from the official logo artwork in `assets/img/`.

## Logo

The mark is a six-segment pinwheel in cyan, orange and slate. The wordmark is
**lowercase "muneris"** in a rounded geometric sans, slate. Never set the
wordmark in capitals, and never letter-space it.

| File | Use |
| --- | --- |
| `assets/img/muneris-logo-horizontal.png` | Default lockup, light backgrounds |
| `assets/img/muneris-logo-horizontal-reverse.png` | Dark backgrounds — wordmark knocks out to white, symbol keeps cyan and orange |
| `assets/img/muneris-logo-stacked.png` | Stacked lockup, symbol above wordmark |
| `assets/img/muneris-symbol.png` | Symbol alone — favicon, avatars, watermarks |

All four are trimmed to their content and have transparent backgrounds. They
were generated from the source art in the OneDrive brand drop; regenerate from
that source rather than editing these.

## Colour

Four official colours, exact:

| Token | Hex | Role |
| --- | --- | --- |
| slate | `#576E7E` | The wordmark, and a third of the symbol |
| cyan | `#51C8E8` | Symbol |
| orange | `#FF8A3D` | Symbol |
| tint | `#EEF2F5` | The light ground the brand sits on |

Cyan and orange are **too light to carry text** — 1.95:1 and 2.35:1 on white,
both far below the 4.5:1 needed. They are for graphic use: fills, rules,
watermarks, and backgrounds behind dark type. Where an accent must be *typed*,
use the derived tones:

| Token | Hex | Contrast |
| --- | --- | --- |
| `--accent` (from cyan) | `#17758F` | 5.28:1 on white · 4.69:1 on tint |
| `--accent-warm` (from orange) | `#A85310` | 5.37:1 on white · 4.77:1 on tint |
| `--ink` | `#25333C` | 12.98:1 on white |
| `--text-muted` | `#536876` | 5.82:1 on white · 5.17:1 on tint |

On the dark slate ground `#2E3F4A`, the pure brand colours *are* safe and
should be used directly: cyan 5.60:1, orange 4.65:1, white 10.90:1.

The primary button is brand orange with **ink-coloured type** (5.54:1). White
type on orange is 2.35:1 and must not be used.

Every token lives in `assets/css/brand.css`. Change colour there, nowhere else.

## Character

Light and warm, not dark and corporate. The brand's own ground is the pale
`#EEF2F5`, so pages lead light and use the deep slate sparingly — one band
mid-page, plus the footer. The three-colour rule (`.rule`) quotes the symbol
and is the site's signature device; it appears above hero and CTA headings and
along the top edge of the footer.

## Site conventions

Static HTML, no build step, no dependencies. Repository root is the site root.
`assets/css/brand.css` holds tokens; `assets/css/site.css` holds everything
else and hard-codes no brand colour except in `.rule`, which quotes the symbol
deliberately.

Verify visual changes by serving the site and screenshotting it — check both
1280px and 390px, and confirm no console errors and no horizontal overflow.

```bash
python3 -m http.server 8000
```
