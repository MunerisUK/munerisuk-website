# muneris.co.uk

Static marketing site for **Muneris Management Ltd**. No build step, no
dependencies, no JavaScript framework — plain HTML, CSS and ~60 lines of
progressive-enhancement JS. It will run on any static host.

```
index.html         Home
services.html      Four service practices (#board #interim #pe #ai)
about.html         Martin Carpenter — profile, career, credentials
contact.html       Enquiry form (mailto) + company details
404.html           Not-found page
assets/css/brand.css   ← brand tokens: colour, type, spacing
assets/css/site.css    Layout and components
assets/js/site.js      Mobile nav, footer year, scroll reveal
assets/img/            Official logo artwork
CLAUDE.md              Canonical brand reference
robots.txt, sitemap.xml
```

## Where the content came from

| Section | Source |
| --- | --- |
| Positioning, services, career, credentials | `Martin Carpenter Feb 2026 CV.docx` (OneDrive) |
| Logo artwork and the four brand colours | OneDrive brand drop, sampled from the source PNGs |
| Company number 09096411 | Companies House public register |

## Scope

The site presents Muneris as a consultancy practice only — advisory, interim
leadership and PE work. **Software products and ventures (WealthHorizon) are
deliberately out of scope for now.**

An earlier revision included a `ventures.html` page covering WealthHorizon and
the board-advisory portfolio. It was removed rather than hidden, so the nav,
sitemap and enquiry form carry no trace of it. To bring it back, recover the
file from git history:

```bash
git show a32206a:ventures.html > ventures.html
```

Then re-add the nav and footer links and the sitemap entry. Note that the page
deliberately excluded every commercial figure from the WealthHorizon deck
(TAM/SAM/SOM, ARPU, LTV:CAC, pricing, the raise), as that deck is marked
*Confidential — for discussion*.

The board, advisory and non-executive roles still appear — on the homepage and
in full on `about.html` — since those are consultancy credentials rather than
product.

## Brand

The site uses the official Muneris brand — real logo artwork and the four
colours sampled from it. **See [CLAUDE.md](CLAUDE.md) for the full brand
reference**, which is the canonical description of the identity.

The short version:

| | Hex | |
| --- | --- | --- |
| slate | `#576E7E` | wordmark, and a third of the symbol |
| cyan | `#51C8E8` | symbol |
| orange | `#FF8A3D` | symbol |
| tint | `#EEF2F5` | the light ground the brand sits on |

Cyan and orange are too light to carry text (1.95:1 and 2.35:1 on white), so
`brand.css` also defines derived tones — `--accent` `#17758F` and
`--accent-warm` `#A85310` — for links and typed accents. Every text/background
pairing on the site clears WCAG AA, and the ratios are noted per token in the
file. The primary button is brand orange with dark ink type, because white on
orange is only 2.35:1.

`assets/css/brand.css` is the single place to change the look. Nothing in
`site.css` hard-codes a brand colour except `.rule`, the three-segment device
that quotes the symbol.

### Logo files

Generated from the OneDrive brand drop, trimmed to content with transparent
backgrounds:

```
muneris-logo-horizontal.png          default lockup, light backgrounds
muneris-logo-horizontal-reverse.png  dark backgrounds (footer)
muneris-logo-stacked.png             symbol above wordmark
muneris-symbol.png                   symbol alone — favicon, hero watermark
```

In the reverse lockup the slate wordmark knocks out to white while the symbol
keeps its cyan and orange; the symbol's slate third also goes white, since at
`#576E7E` on the dark ground it would sit at 2.2:1 and read as a hole. If you
would rather it stayed slate, regenerate that one asset.

The wordmark is always lowercase and never letter-spaced.

## Running it locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploying

Any static host works. The repository root *is* the site root.

- **Cloudflare Pages / Netlify** — connect the repo, build command: none,
  output directory: `/`.
- **GitHub Pages** — Settings → Pages → deploy from branch, folder `/ (root)`,
  then point the `muneris.co.uk` DNS at Pages and add a `CNAME` file.

## Before it goes live

- [ ] Confirm you are happy naming clients publicly (Optum/UnitedHealth, EMIS,
      NHS Kent & Medway, Government of Jersey, Synomics, Calyx, ColorTokens)
      and quoting the associated figures.
- [ ] Decide whether to publish the mobile number — it is on the CV but is
      currently left off the site.
- [ ] Add the registered office address to `contact.html` if you want it shown.
- [ ] Add a LinkedIn URL to the footer/contact page.
- [ ] The enquiry form uses `mailto:`, which depends on the visitor having a
      mail client configured. If you would rather have a proper form, point the
      `<form action>` at Formspree, Netlify Forms or Cloudflare Workers.
