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
└── assets/
    ├── logo/             Supplied Kapture icon (source of truth)
    ├── social/           1200×630 Open Graph image
    └── screenshots/      Empty. Real extension screenshots go here
```

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

The store listing does not exist yet, so the site deliberately ships **no store URL**.
The three "Add to Chrome" buttons carry `data-store-pending`, which renders them as an
"In review" state and blocks navigation.

To go live, in `index.html`:

1. Replace `href="#cta"` with the real Chrome Web Store URL on all three buttons
   (each is marked with a `TODO` comment).
2. Delete the `data-store-pending` attribute from all three.
3. Remove the `<p class="cta-note" data-store-note>` paragraph in the final CTA section.

No other change is needed. The pending styling and the click handler both key off
that one attribute.

All three Chrome buttons use the `.btn-white` treatment with the official Chrome
mark (`.chrome-mark`, inline SVG in `index.html`).

The Mac buttons sit beside them in the header, hero and final CTA. They carry
`data-mac-pending`, which renders the "Soon" pill and blocks the click, and use
`.btn-primary` (teal) with `.apple-mark`. When a Mac build ships, give each a
real href and drop `data-mac-pending`; the same three-step swap as Chrome.

In the header the two actions shed detail as the viewport narrows: the status
pills go at 1040px, the nav at 900px, and the Mac action at 460px, where there
is no longer room for both. The hero and final CTA keep both actions and both
pills at every width.

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

- **Chrome Web Store listing URL**: see the CTA section above.
- **Real extension screenshots**: the hero currently uses a faithful HTML/CSS
  recreation of the side panel. Drop real PNGs into `assets/screenshots/` and swap
  the `.window` block in `index.html` for an `<img>` when they are available.
