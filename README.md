# Kaptweb

Official website for **Kapture**: a Chrome extension for capturing full webpages,
and **Kapture Pro for Mac**, which organises those captures.

Live domain: **kaptapp.com** (published with GitHub Pages from this repository).

## Stack

Plain HTML, CSS and a small amount of vanilla JavaScript. No build step, no framework,
no dependencies. Open `index.html` in a browser to preview locally, or just push and
review on the deployed URL.

## Files

```text
/
├── index.html            Landing page
├── privacy/index.html    Privacy policy, served at /privacy/
├── styles.css            All styles for both pages
├── script.js             Sticky header, scroll reveal, footer year
├── CNAME                 kaptapp.com
├── .nojekyll             Serve files as-is on GitHub Pages
├── robots.txt            Fully crawlable, names the sitemap
├── sitemap.xml           The two indexable URLs
├── llms.txt              Plain-text product summary for AI crawlers
├── site.webmanifest      Name, theme colour and icons
├── favicon.ico           16, 32 and 48px in one file
├── favicon-16x16.png
├── favicon-32x32.png
├── favicon-48x48.png
├── favicon-512x512.png   Large square for modern browsers and search
├── apple-touch-icon.png  180px, opaque, for iOS home screens
└── assets/
    ├── logo/             Supplied Kapture icon and wordmark (source of truth)
    ├── social/           1200×630 Open Graph image
    ├── demo/             Real panel renders, curated thumbnails, the captured page
    └── screenshots/      Real product captures
```

Every favicon is rendered from `assets/logo/kapture-icon.svg`, the supplied icon.
They are referenced with **relative** paths rather than root-relative ones, so
they resolve both on `kaptapp.com` and on the `github.io` project URL while the
custom domain is still being set up. Because both pages sit at the site root,
a relative `favicon.ico` resolves to `kaptapp.com/favicon.ico` in production,
which is also where browsers probe for it automatically.

## Brand

| Token      | Value                | Notes                                  |
| ---------- | -------------------- | -------------------------------------- |
| Background | `#1b1d1c` / `#171918`| Dark charcoal                          |
| Accent     | `#19d7c0`            | Solid teal, no gradients               |
| Text       | `#f1f4f2`            | Plus dimmed `#b6bfbb` / `#8b9490`      |

`assets/logo/kapture-icon.svg` is the icon exactly as supplied (copied from the
extension package). It is used in the header, footer, favicon and product mock.
Do not redraw it. `kapture-icon-512.png` and `assets/social/kapture-og.png` are
renders/compositions of that same file.

## Content rules

Every product claim on the site comes from the shipped extension: `manifest.json`,
the side panel and the bundled help page for version 0.4.7:

- Full page capture, split into 8,000px sections
- Select area capture (Freeform, 1:1, 16:9, 9:16)
- PNG, JPEG and PDF output
- Viewport presets: current window, Phone 390, Tablet 820, Desktop 1440, Desktop 1920
- Saves to a subfolder of Chrome's Downloads directory, named per capture
- Local capture history with open and delete
- Light and dark side panel themes
- No account, ads, analytics or data transmission
- Requires Chrome 120+

Kapture is presented as one product on two platforms. Alongside each "Add to
Chrome" action there is a teal "Add to Mac" action carrying a "Soon" pill, and
the supporting lines say the Mac app is coming. Both are deliberately worded as
plans with no dates.

`privacy/index.html` reproduces the supplied privacy-policy wording verbatim. Do not
reword its claims without a corresponding change to the extension.

## Chrome Web Store CTA

The extension is live. All three "Add to Chrome" buttons link to the listing:

```text
https://chromewebstore.google.com/detail/kapture/bpkhaglkdlkbjnlkbefmobiajidgoeap
```

They open in a new tab with `rel="noopener noreferrer"`, use the `.btn-white`
treatment with the official Chrome mark, and behave as ordinary links.

The Mac buttons sit beside them in the header, hero and final CTA. The Mac app
is **not** released, so they still carry `data-mac-pending`, which renders the
"Soon" pill and blocks the click. When a Mac build ships, give each a real href
and drop `data-mac-pending`.

In the header the two actions shed detail as the viewport narrows: the status
pills go at 1040px, the nav at 900px, and the Mac action at 460px, where there
is no longer room for both. The hero and final CTA keep both actions at every
width.

## Languages

Five static language versions, each with real crawlable HTML. English is the
default and stays at the root.

| Language | Home | Privacy |
| -------- | ---- | ------- |
| English  | `/` | `/privacy/` |
| Spanish  | `/es/` | `/es/privacy/` |
| Chinese (Simplified) | `/zh/` | `/zh/privacy/` |
| Korean   | `/ko/` | `/ko/privacy/` |
| Japanese | `/ja/` | `/ja/privacy/` |

**The translated pages are generated, not hand-edited.** `index.html` and
`privacy/index.html` are the source of truth for markup; the copy lives in
`tools/t_*.py`, where later tables override earlier ones (`t_fix.py` last). After changing either English page, or any translation, run:

```sh
python3 tools/build_i18n.py
```

That rewrites all eight translated pages and re-injects the hreflang set and the
language selector into the English pages too. It is idempotent, so it is safe to
run repeatedly. Editing `es/index.html` by hand will be overwritten.

Each page self-canonicalises, carries the full reciprocal hreflang set (five
languages plus `x-default`), sets the right `<html lang>`, and ships localised
metadata and JSON-LD prose. Factual fields in the structured data (name,
version, category, `installUrl`, `browserRequirements`) are identical in every
language.

The language selector is a native `<details>` disclosure: keyboard accessible,
no JavaScript. It keeps you on the same kind of page, so switching language from
a privacy page lands on that language's privacy page. There is **no** automatic
redirect based on browser language.

The Kapture side panel shown in the hero mock stays in English on every page. It
reproduces the real extension interface, which is not localised, so translating
it would show a product that does not exist. The badge, caption and the
descriptive `aria-label` around it are translated.

Fonts are system-only. The stack gains PingFang SC, Hiragino Sans, Yu Gothic UI,
Apple SD Gothic Neo, Malgun Gothic and the Noto CJK fallbacks, so nothing is
downloaded for CJK or Hangul.

Privacy pages use directory URLs (`/privacy/`, `/es/privacy/`) rather than
`.html`, so each is an `index.html` inside a `privacy/` folder. Internal links
to them are root-relative; the build rewrites `href="/..."` into the current
language when it generates a translated page.

## Product assets

`assets/logo/kapture_wordmark.svg` is the supplied final wordmark, used as-is in the
header and footer on every page. It is an outlined vector with no font dependency, so
it stays sharp at any pixel ratio. The icon (`kapture-icon.svg`) is still the favicon,
app icon and Open Graph mark.

Every product visual comes from the shipped products. Nothing on the page is a
mock-up, an illustration or an approximation.

| File | Shows |
| ---- | ----- |
| `screenshots/kapture-pro-curated.png` | The Kapture Pro window, hero layer |
| `screenshots/kapture-chrome-0-4-7.png` | Kapture 0.4.7 in Chrome (structured data only) |
| `demo/panel-light-full.png`, `panel-dark-full.png` | The 0.4.7 side panel, Full page, both themes |
| `demo/panel-light-area.png`, `panel-dark-area.png` | The same panel switched to Select area |
| `demo/page-dotto.jpg` | A real Kapture capture of a real webpage |
| `demo/thumb-1…7.png` | The seven curated captures |

The seven curated captures are the set in
`KapturePro/Assets/kapture_screenshots`. **Do not use the full library from
`~/Downloads/Kapture`**: it is personal and it makes the product look cluttered.

`kapture-pro-curated.png` is a render of the `.kp` component described below,
not a photograph of a window. Regenerate it by rendering that markup at
1024×514 with `--force-device-scale-factor=2`. If its size changes, update the
`width`/`height` on the hero `<img>` and rerun `python3 tools/build_i18n.py`.

## Cache busting

`styles.css` and `script.js` are referenced with a `?v=N` query in both pages.
GitHub Pages serves assets with `cache-control: max-age=600`, and local dev
servers often send no cache headers at all, so without this a browser can hold
a stale stylesheet against fresh HTML and render the page wrong in ways that
look like a broken deploy.

**Bump the number in both `index.html` and `privacy/index.html` whenever you change
`styles.css` or `script.js`.** Currently `v=10`.

## SEO and discoverability

Both pages carry a unique title, a factual meta description, a self-referencing
canonical on `https://kaptapp.com`, `robots` set to `index, follow,
max-image-preview:large`, full Open Graph and Twitter card tags pointing at
`assets/social/kapture-og.png`, and JSON-LD.

Structured data:

| Page | Types |
| ---- | ----- |
| Home | `WebSite`, `Organization`, `SoftwareApplication`, `WebPage` |
| Privacy | `WebPage`, `BreadcrumbList` |

`SoftwareApplication` uses `applicationCategory: BrowserApplication` and
`browserRequirements: Requires Google Chrome 120 or later`. It deliberately
carries **no** `operatingSystem` (a browser extension has no OS requirement of
its own, so the property would be semantically wrong) and no `offers`,
`aggregateRating` or `review`, since the site states no price, rating or review
count. Only facts taken from the shipped extension appear in `featureList`.

`robots.txt` disallows nothing. It repeats `Allow: /` for named search and
answer-engine crawlers, `OAI-SearchBot` included, because a named user-agent
group replaces the `*` group for that bot.

## Search Console

The verification tag is **not** in the repository. To add it:

1. In Google Search Console add the property `https://kaptapp.com`
2. Choose the **HTML tag** verification method and copy the tag it gives you
3. Open `index.html` and find the comment `GOOGLE SEARCH CONSOLE VERIFICATION`
   near the top of the `<head>`, around line 10
4. Paste the tag on the empty line directly below that comment
5. Commit, push, wait for Pages to deploy, then click Verify

Then submit `https://kaptapp.com/sitemap.xml` under **Sitemaps**.

## Deployment

GitHub Pages, published from the `main` branch root.

1. Repository **Settings → Pages**
2. Source: *Deploy from a branch* → `main` / `/ (root)`
3. Save, then confirm the generated URL loads

### Custom domain

DNS is managed at Hostinger. Set the custom domain in **Settings → Pages** first, then
point DNS at GitHub:

Apex `kaptapp.com`, A records:

```text
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

`www.kaptapp.com`: CNAME to `kaptapp.github.io`.

Enable **Enforce HTTPS** once GitHub offers it. DNS propagation can take a while.
Cloudflare is not needed.

## The two animated compositions

Both are driven by one attribute that JavaScript steps through, so every state
is expressible in CSS alone and the page still reads with scripting off.

**`#capDemo` (`data-phase`)** replays the real Chrome workflow across six
phases: `full`, `scan`, `kept`, `area`, `draw`, `crop`. The left half is a real
capture of a real page; the right half is the shipped 0.4.7 side panel, swapped
between its Full page and Select area screenshots. Everything drawn on top (the
sweep, the region, the cursor, the two control rings) is annotation over real
pixels. `.cap-hit-go` and `.cap-hit-mode` are positioned in percentages over the
panel screenshot, so they move if the panel render is ever replaced.

**`#kpDemo` (`data-state`)** is Kapture Pro rebuilt in HTML from the app's own
`Brand.swift` tokens, real Phosphor icons out of `KapturePro/Assets/Icons`, and
the real New Project sheet from `ProjectEditorView.swift`. The six controls in
`#kpPoints` switch it between `library`, `search`, `projects`, `inspector`,
`tags` and `storage`.

**The window must never change size between states.** `.kp-body` has a fixed
height and the three panes clip, so searching down to three results cannot make
the page jump. Keep it that way: if you add a state, check the height rather
than trusting it.

Under `prefers-reduced-motion: reduce` neither composition cycles. `#capDemo`
holds its finished `crop` state and `#kpDemo` stays on `library`.

The Kapture Pro interface and the side-panel screenshots stay in English on
every language version. Neither product is localised, so translating their
interface would show software that does not exist.
