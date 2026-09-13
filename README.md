# Kaptweb

Official website for **Kapture**, a Chrome extension for capturing full webpages.

Live domain: **kaptapp.com** (published with GitHub Pages from this repository).

## Stack

Plain HTML, CSS and a small amount of vanilla JavaScript. No build step, no framework,
no dependencies. Open `index.html` in a browser to preview locally, or just push and
review on the deployed URL.

## Files

```text
/
├── index.html            Landing page
├── privacy.html          Privacy policy
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
    ├── logo/             Supplied Kapture icon (source of truth)
    ├── social/           1200×630 Open Graph image
    └── screenshots/      Empty. Real extension screenshots go here
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
the side panel and the bundled help page for version 0.4.4:

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

`privacy.html` reproduces the supplied privacy-policy wording verbatim. Do not
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

## Cache busting

`styles.css` and `script.js` are referenced with a `?v=N` query in both pages.
GitHub Pages serves assets with `cache-control: max-age=600`, and local dev
servers often send no cache headers at all, so without this a browser can hold
a stale stylesheet against fresh HTML and render the page wrong in ways that
look like a broken deploy.

**Bump the number in both `index.html` and `privacy.html` whenever you change
`styles.css` or `script.js`.** Currently `v=3`.

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

## Still to supply

- **Real extension screenshots**: the hero currently uses a faithful HTML/CSS
  recreation of the side panel. Drop real PNGs into `assets/screenshots/` and swap
  the `.window` block in `index.html` for an `<img>` when they are available.

## Hero mock scaling

Kapture only runs on the desktop, so the hero mock never reflows into a phone
layout. It is laid out at a fixed design width (1040px, the shell's maximum
content width) inside `.product-scaler`, and `fitMock()` in `script.js` scales
it down as a single unit and sets the wrapper's height to match. The result is
the same desktop composition at every viewport, the way a real screenshot of a
desktop window behaves. Change `DESIGN_WIDTH` in `script.js` if the shell width
ever changes.
