# muneris.co.uk

Static marketing site for **Muneris Management Ltd**. No build step, no
dependencies, no JavaScript framework — plain HTML, CSS and ~60 lines of
progressive-enhancement JS. It will run on any static host.

```
index.html         Home — hero, services overview, selected engagements (#work)
services.html      Six service lines (#interim #ps #reviews #maturity #advisory #tools)
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
| Hero, stats, six service lines, selected engagements | Copy supplied from the live Netlify build, used verbatim |
| Service detail pages, About, Contact | `Martin Carpenter Feb 2026 CV.docx` (OneDrive) |
| Logo artwork and the four brand colours | OneDrive brand drop, sampled from the source PNGs |
| Company number 09096411 | Companies House public register |

The homepage copy is the supplied wording unchanged. The per-service detail on
`services.html` expands each of the six one-liners; that expansion is written,
not sourced, so read it before publishing.

## Scope

Muneris is positioned as **interim leadership and advisory**. Six service
lines, with engagements presented anonymously.

**WealthHorizon remains out of scope.** Note that the "Software & tools"
service line is a different thing — templates and assessment frameworks
distilled from client engagements, not a product venture.

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

## Two things to resolve

**1. The About page names clients the homepage anonymises.** The engagements
section states that client names are withheld, and the first case study —
"interim Global VP for a clinical-trials technology business" — maps directly
onto the Calyx.AI entry on `about.html`. Anyone reading both pages can
de-anonymise it. The same applies to Synomics and ColorTokens.

This was left as-is rather than decided unilaterally: your CV names these
publicly, and employment history is not the same as a client engagement. But
it is a live inconsistency, and the fix is yours to choose — either anonymise
those entries on the About page, or drop the confidentiality line from the
engagements section.

**2. The "available to buy" section is missing.** The supplied copy ends with
"Software & tools … available to buy below", but the products, descriptions and
prices below that point were not included, and the Netlify host is blocked from
this environment so the page could not be fetched. That service line currently
points at the contact page with "Ask what's available". Send me the product
list and prices and I will build the section properly.

## Before it goes live

- [ ] Resolve the two items above.
- [ ] Decide whether to publish the mobile number — it is on the CV but is
      currently left off the site.
- [ ] Add the registered office address to `contact.html` if you want it shown.
- [ ] Add a LinkedIn URL to the footer/contact page.
- [ ] The enquiry form uses `mailto:`, which depends on the visitor having a
      mail client configured. If you would rather have a proper form, point the
      `<form action>` at Formspree, Netlify Forms or Cloudflare Workers.
