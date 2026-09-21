# -*- coding: utf-8 -*-
"""
Generates the localised pages from the English sources.

English index.html and privacy/index.html are the single source of truth for markup.
This script only swaps copy, rewrites relative paths for the subfolder, and
injects the hreflang set, the language selector and localised JSON-LD. Re-run
it after any change to the English pages.

    python3 tools/build_i18n.py
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))

from t_home import HOME
from t_home2 import HOME2
from t_home3 import HOME3
from t_eco1 import ECO1
from t_eco2 import ECO2
from t_eco3 import ECO3
from t_fix import FIX
from t_privacy import PRIV
from t_ld import (APP_DESC, FEATURES, PRO_DESC, PRO_FEATURES, SELECTOR_LABEL, NATIVE_NAME, SHORT_NAME,
                  LANGS, HTMLLANG, BASE, home_url, privacy_url)

ROOT = pathlib.Path(__file__).resolve().parent.parent
# ECO* are the ecosystem pass and win over any older entry with the same key.
# FIX is the correction pass and wins over every earlier entry.
HOME_ALL = {**HOME, **HOME2, **HOME3, **ECO1, **ECO2, **ECO3, **FIX}


# ---------------------------------------------------------------- selector
def selector(lang, page):
    """A <details> disclosure: native keyboard support, no JavaScript."""
    url = (lambda l: home_url(l) if page == 'index' else privacy_url(l))
    items = []
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ''
        items.append(
            f'        <li><a href="{url(l)}" hreflang="{HTMLLANG[l]}" lang="{HTMLLANG[l]}"{cur}>'
            f'{NATIVE_NAME[l]}</a></li>')
    return (
'    <details class="langpick">\n'
f'      <summary aria-label="{SELECTOR_LABEL[lang]}">\n'
'        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/>'
'<path d="M3.2 9.5h17.6M3.2 14.5h17.6"/><path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18"/></svg>\n'
f'        <span>{SHORT_NAME[lang]}</span>\n'
'      </summary>\n'
'      <ul>\n' + '\n'.join(items) + '\n      </ul>\n'
'    </details>\n')


def hreflang(page):
    url = (lambda l: home_url(l) if page == 'index' else privacy_url(l))
    rows = [f'<link rel="alternate" hreflang="{HTMLLANG[l]}" href="{url(l)}">' for l in LANGS]
    rows.append(f'<link rel="alternate" hreflang="x-default" href="{url("en")}">')
    return '\n'.join(rows)


# ---------------------------------------------------------------- JSON-LD
def localise_ld(raw, lang, page, title, desc):
    data = json.loads(raw)
    h, p = home_url(lang), (home_url(lang) if page == 'index' else privacy_url(lang))
    for node in data['@graph']:
        t = node['@type']
        if t == 'WebSite':
            node['@id'] = h + '#website'
            node['url'] = h
            node['description'] = desc
            node['inLanguage'] = HTMLLANG[lang]
        elif t == 'SoftwareApplication':
            # Two apps share this type, so key off the existing id suffix rather
            # than overwriting both with the same one.
            suffix = node['@id'].rsplit('#', 1)[1]
            node['@id'] = f'{h}#{suffix}'
            if suffix == 'kapture-pro':
                node['url'] = h + '#pro'
                node['description'] = PRO_DESC[lang]
                node['featureList'] = PRO_FEATURES[lang]
            else:
                node['url'] = h
                node['description'] = APP_DESC[lang]
                node['featureList'] = FEATURES[lang]
        elif t == 'WebPage':
            node['@id'] = p + '#webpage'
            node['url'] = p
            node['name'] = title
            node['description'] = desc
            node['inLanguage'] = HTMLLANG[lang]
            for k in ('isPartOf', 'about'):
                if k in node:
                    node[k]['@id'] = h + ('#website' if k == 'isPartOf' else '#kapture')
            if 'breadcrumb' in node:
                node['breadcrumb']['@id'] = p + '#breadcrumb'
        elif t == 'BreadcrumbList':
            node['@id'] = p + '#breadcrumb'
            node['itemListElement'][0]['item'] = h
        # Organization is identical in every language and keeps its shared @id
    return json.dumps(data, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- build
def strip_i18n(src):
    """Remove any previously injected hreflang set and selector, so the build
    is idempotent whether or not the English source has already been patched."""
    src = re.sub(r'\n<link rel="alternate"[^>]*>', '', src)
    src = re.sub(r'\n    <details class="langpick">.*?</details>\n', '\n', src, flags=re.S)
    return src


# Where each page lives. English privacy sits at privacy/index.html so it is
# served at the clean /privacy/ URL, which makes it one level deep already.
SOURCE = {'index': 'index.html', 'privacy': 'privacy/index.html'}


def build(lang, page):
    src = strip_i18n((ROOT / SOURCE[page]).read_text())
    table = HOME_ALL if page == 'index' else PRIV

    # 1. copy, longest key first so no key is a prefix of another. Keys that no
    #    longer appear are retired copy, not an error, so they are only reported.
    retired = []
    for key in sorted(table, key=len, reverse=True):
        if key in src:
            src = src.replace(key, table[key][lang])
        else:
            retired.append(key)
    build.retired = retired

    # 2. assets sit one more level up for every translated page. The English
    #    homepage is at the root, everything else is already one deep.
    if page == 'index':
        for a, b in [('href="styles.css', 'href="../styles.css'),
                     ('src="script.js', 'src="../script.js'),
                     ('href="favicon', 'href="../favicon'),
                     ('href="apple-touch-icon', 'href="../apple-touch-icon'),
                     ('href="site.webmanifest', 'href="../site.webmanifest'),
                     ('src="assets/', 'src="../assets/'),
                     ('href="assets/', 'href="../assets/')]:
            src = src.replace(a, b)
    else:
        # privacy/index.html already uses ../, and {lang}/privacy/ is two deep
        src = src.replace('href="../', 'href="../../').replace('src="../', 'src="../../')

    # 3. language attribute, then every root-relative internal link moves into
    #    this language: href="/" , href="/#how" and href="/privacy/" all shift.
    src = src.replace('<html lang="en">', f'<html lang="{HTMLLANG[lang]}">', 1)
    src = src.replace('href="/', f'href="/{lang}/')
    page_url = home_url(lang) if page == 'index' else privacy_url(lang)
    src = re.sub(r'<link rel="canonical" href="[^"]+">',
                 f'<link rel="canonical" href="{page_url}">', src, count=1)
    src = re.sub(r'<meta property="og:url" content="[^"]+">',
                 f'<meta property="og:url" content="{page_url}">', src, count=1)

    # 4. hreflang set, immediately after the canonical
    src = src.replace(f'<link rel="canonical" href="{page_url}">',
                      f'<link rel="canonical" href="{page_url}">\n' + hreflang(page), 1)

    # 5. language selector at the start of the header actions
    if page == 'index':
        anchor = '    <div class="header-ctas">\n'
        src = src.replace(anchor, anchor + selector(lang, page), 1)
    else:
        anchor = '    <a class="btn btn-ghost btn-sm store-cta"'
        src = src.replace(anchor, selector(lang, page) + anchor, 1)

    # 6. localised JSON-LD
    title = re.search(r'<title>(.*?)</title>', src, re.S).group(1)
    desc = re.search(r'<meta name="description" content="([^"]+)">', src).group(1)
    block = re.search(r'<script type="application/ld\+json">\n(.*?)\n</script>', src, re.S)
    src = src.replace(block.group(0),
                      '<script type="application/ld+json">\n'
                      + localise_ld(block.group(1), lang, page, title, desc) + '\n</script>')

    out = ROOT / lang / ('index.html' if page == 'index' else 'privacy/index.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(src)
    return out


def patch_english():
    """English pages need the same hreflang set and the selector."""
    for page in ('index', 'privacy'):
        p = ROOT / SOURCE[page]
        src = strip_i18n(p.read_text())
        url = home_url('en') if page == 'index' else privacy_url('en')
        # Derive rather than assume, so a URL change cannot silently skip the
        # hreflang injection the way a stale canonical once did.
        src = re.sub(r'<link rel="canonical" href="[^"]+">',
                     f'<link rel="canonical" href="{url}">', src, count=1)
        src = re.sub(r'<meta property="og:url" content="[^"]+">',
                     f'<meta property="og:url" content="{url}">', src, count=1)
        src = src.replace(f'<link rel="canonical" href="{url}">',
                          f'<link rel="canonical" href="{url}">\n' + hreflang(page), 1)
        if page == 'index':
            anchor = '    <div class="header-ctas">\n'
            src = src.replace(anchor, anchor + selector('en', page), 1)
        else:
            anchor = '    <a class="btn btn-ghost btn-sm store-cta"'
            src = src.replace(anchor, selector('en', page) + anchor, 1)
        p.write_text(src)
        print(f'  patched  {SOURCE[page]} (hreflang + selector)')


SENTINELS = [
    'Capture in Chrome', 'Organise on Mac', 'Your screenshots,', 'finally organised',
    'Local by default', 'Two products',
    'One workflow', 'Project folders', 'History previews', 'Local only',
    'Visual library', 'Tags and notes', 'One-time purchase', 'Free</p>',
    'Privacy</a>', 'Add to Chrome', 'In the extension',
]


def audit(lang):
    """Fail loudly if recognisable English marketing copy survived translation."""
    out = (ROOT / lang / 'index.html').read_text()
    body = out[out.index('<body>'):]
    body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
    leftovers = [s for s in SENTINELS if s in body]
    return leftovers


if __name__ == '__main__':
    patch_english()
    retired = None
    for lang in [l for l in LANGS if l != 'en']:
        for page in ('index', 'privacy'):
            print(f'  built    {build(lang, page).relative_to(ROOT)}')
            if page == 'index':
                retired = build.retired
        bad = audit(lang)
        if bad:
            raise SystemExit(f'  !! {lang}: untranslated English still present: {bad}')
    if retired:
        print(f'\n  {len(retired)} retired key(s) no longer in the English source:')
        for k in retired:
            print(f'    - {k[:78]!r}')
