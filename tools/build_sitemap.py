# -*- coding: utf-8 -*-
"""Generate sitemap.xml from the same locale list the site is built from.

Hand-editing it was fine for five languages and three pages. With nine it is
fifteen URLs per page type and an hreflang cluster on every one, so it is
derived instead: add a language to t_ld.LANGS and the sitemap follows.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from t_ld import LANGS, HTMLLANG, page_url

ROOT = pathlib.Path(__file__).resolve().parents[1]

# page key -> (lastmod, changefreq, priority)
PAGES = {
    'index':   ('2026-09-30', 'monthly', '1.0'),
    'help':    ('2026-09-30', 'monthly', '0.6'),
    'privacy': ('2026-09-30', 'yearly',  '0.5'),
}
# English-only pages: no alternates, so no hreflang cluster is claimed.
SOLO = {
    'https://kaptapp.com/screenshot-organizer/': ('2026-09-30', 'monthly', '0.7'),
}


def cluster(page):
    rows = ['      <xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
            % (HTMLLANG[l], page_url(l, page)) for l in LANGS]
    rows.append('      <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                % page_url('en', page))
    return '\n'.join(rows)


def main():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for page, (mod, freq, pri) in PAGES.items():
        for lang in LANGS:
            out += ['  <url>',
                    '    <loc>%s</loc>' % page_url(lang, page),
                    cluster(page),
                    '    <lastmod>%s</lastmod>' % mod,
                    '    <changefreq>%s</changefreq>' % freq,
                    '    <priority>%s</priority>' % pri,
                    '  </url>']
    for loc, (mod, freq, pri) in SOLO.items():
        out += ['  <url>',
                '    <loc>%s</loc>' % loc,
                '    <lastmod>%s</lastmod>' % mod,
                '    <changefreq>%s</changefreq>' % freq,
                '    <priority>%s</priority>' % pri,
                '  </url>']
    out.append('</urlset>')
    (ROOT / 'sitemap.xml').write_text('\n'.join(out) + '\n')
    n = len(PAGES) * len(LANGS) + len(SOLO)
    print('  wrote sitemap.xml with %d urls (%d locales x %d pages + %d solo)'
          % (n, len(LANGS), len(PAGES), len(SOLO)))


if __name__ == '__main__':
    main()
