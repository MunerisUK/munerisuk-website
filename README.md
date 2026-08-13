# muneris.co.uk

Static marketing site for **Muneris Management Ltd**. No build step, no
dependencies, no JavaScript framework — plain HTML, CSS and ~60 lines of
progressive-enhancement JS. It will run on any static host.

```
netlify.toml       Netlify publish settings, security and caching headers
index.html         Home — hero, services overview, selected engagements (#work)
services.html      Five service lines (#interim #ps #reviews #maturity #advisory)
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
| Hero, stats, service lines, selected engagements | Copy supplied from the live Netlify build, used verbatim |
| Service detail pages, About, Contact | `Martin Carpenter Feb 2026 CV.docx` (OneDrive) |
| Logo artwork and the four brand colours | OneDrive brand drop, sampled from the source PNGs |
| Company number 09096411 | Companies House public register |

The homepage copy is the supplied wording unchanged. The per-service detail on
`services.html` expands each one-liner; that expansion is written, not sourced,
so read it before publishing.

## Scope

Muneris is positioned as **interim leadership and advisory**. Five service
lines, with engagements presented anonymously.

Anything software-as-a-product is out of scope: WealthHorizon, and the
"Software & tools" line that offered templates and assessment frameworks for
sale. The latter was removed along with the "available to buy" section it
pointed at. Both are recoverable from git history if that changes.

### Client confidentiality

Engagements are presented without client names. To keep the About page from
undoing that, three career entries are anonymised by descriptor — the
clinical-trials technology business, the genomics analytics business and the
US cybersecurity vendor — since each was matchable against a case study.

Salaried public-sector and corporate roles are still named: Government of
Jersey, NHS Kent & Medway ICB, Optum UK and Reporting Online LLP. So are the
two health-tech board advisory positions further down that page. Say the word
if you want either group anonymised too.

### Recovering removed work

An earlier revision had a `ventures.html` page covering WealthHorizon, and a
later one had the "Software & tools" service line. Both were removed rather
than hidden, so no nav, sitemap or form entry references either. To recover:

```bash
git show a32206a:ventures.html > ventures.html   # WealthHorizon page
git show eaf602e:services.html                   # includes the #tools section
```

Then re-add the nav, footer and sitemap entries. The ventures page deliberately
excluded every commercial figure from the WealthHorizon deck (TAM/SAM/SOM,
ARPU, LTV:CAC, pricing, the raise), as that deck is marked *Confidential — for
discussion*.

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

Any static host works. The repository root *is* the site root, and there is no
build step.

### Netlify (from GitHub)

`netlify.toml` carries the configuration, so connect the repo and accept the
defaults — leave the build command empty and the publish directory as `.`;
Netlify reads both from the file. Deploys happen on push to `main`.

The file also sets:

- **Security headers**, including a strict Content-Security-Policy. The site
  uses no inline script or style, so the policy needs neither `unsafe-inline`
  nor `unsafe-eval`. If you ever add an inline `<script>`, an inline `<style>`,
  a `style="..."` attribute, or an external font/analytics/embed, the policy
  must be widened or the page will silently break — check the browser console.
- **Caching.** Asset filenames are not content-hashed, so assets get a one-hour
  window and revalidate by ETag after that, and HTML always revalidates. If you
  later fingerprint filenames, `/assets/*` can move to
  `max-age=31536000, immutable`.
- **`skip_processing`**, so Netlify serves the files as committed. Without it
  Netlify's Pretty URLs would redirect `/about.html` to `/about`, disagreeing
  with the canonical URLs in each page's `<head>`.

`404.html` at the publish root is picked up automatically for unmatched paths —
no redirect rule needed.

For the custom domain: add `muneris.co.uk` in Netlify under Domain management,
point the DNS there, and let Netlify issue the certificate. Handle the
apex/`www` redirect in Netlify's domain settings rather than in this file.

### Other hosts

- **Cloudflare Pages** — connect the repo, build command: none, output
  directory: `/`. Headers would need porting to a `_headers` file.
- **GitHub Pages** — Settings → Pages → deploy from branch, folder `/ (root)`,
  then point DNS at Pages and add a `CNAME` file. Note that GitHub Pages cannot
  set custom response headers, so the CSP above would not apply.

## Before it goes live

- [ ] Decide whether to publish the mobile number — it is on the CV but is
      currently left off the site.
- [ ] Add the registered office address to `contact.html` if you want it shown.
- [ ] Add a LinkedIn URL to the footer/contact page.
- [ ] The enquiry form uses `mailto:`, which depends on the visitor having a
      mail client configured. If you would rather have a proper form, point the
      `<form action>` at Formspree, Netlify Forms or Cloudflare Workers.
