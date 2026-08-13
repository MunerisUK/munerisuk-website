# muneris.co.uk

Static marketing site for **Muneris Management Ltd**. No build step, no
dependencies, no JavaScript framework — plain HTML, CSS and ~60 lines of
progressive-enhancement JS. It will run on any static host.

```
index.html         Home
services.html      Four service practices (#board #interim #pe #ai)
ventures.html      WealthHorizon + advisory/board roles
about.html         Martin Carpenter — profile, career, credentials
contact.html       Enquiry form (mailto) + company details
404.html           Not-found page
assets/css/brand.css   ← brand tokens: colour, type, spacing
assets/css/site.css    Layout and components
assets/js/site.js      Mobile nav, footer year, scroll reveal
assets/img/            Logo assets
robots.txt, sitemap.xml
```

## Where the content came from

| Section | Source |
| --- | --- |
| Positioning, services, career, credentials | `Martin Carpenter Feb 2026 CV.docx` (OneDrive) |
| WealthHorizon | `WealthHorizon_Pitch_Deck.pptx` (OneDrive) |
| Letter-spaced capital section labels | Muneris/WealthHorizon deck styling |
| Company number 09096411 | Companies House public register |

**Deliberately excluded:** every commercial figure from the WealthHorizon deck
(TAM/SAM/SOM, ARPU, LTV:CAC, pricing, the raise). That deck is marked
*Confidential — for discussion*, so the public page describes the product only.

## Brand

`assets/css/brand.css` is the single place to change the look. Every colour,
font and spacing value on the site is a token in that file.

Two things need your confirmation before this goes live:

1. **Exact brand colours.** The official pack lives at
   `Documents/Dev/Complete_MultiBrand_Pack_V2_2_1/brands/muneris/`, but its
   `guidelines/` and `figma/` folders are empty and the logo files (SVG/PNG/JPG)
   could not be read through the Microsoft 365 connector. The palette in
   `brand.css` follows the pack's own naming — deep slate (`mono-slate`), a
   reverse-white treatment, and a teal accent. Drop the real hex values into the
   `--ink` / `--slate` / `--accent` tokens and the whole site follows.

2. **The logo.** `assets/img/muneris-mark.svg` is a stand-in. To use the real
   artwork, copy these out of the brand pack:

   ```
   brands/muneris/logos/svg/muneris-logo-horizontal-fullcolour.svg
   brands/muneris/logos/svg/muneris-logo-reverse-white.svg
   ```

   into `assets/img/`, then in each page swap the `.brand` block for:

   ```html
   <a class="brand" href="index.html" aria-label="Muneris — home">
     <img src="assets/img/muneris-logo-horizontal-fullcolour.svg" alt="Muneris" width="150" height="32">
   </a>
   ```

   (The footer sits on a dark background — use `muneris-logo-reverse-white.svg`
   there.) Also point the `<link rel="icon">` at the symbol asset.

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

- [ ] Confirm the brand hex values and swap in the official logo files.
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
