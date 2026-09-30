# -*- coding: utf-8 -*-
"""Find English copy that survived translation, by comparing each built page
against the English source sentence by sentence.

The sentinel list only catches phrases someone thought to add. This catches any
sentence that is byte-identical to the English one, which is what a retired key
leaves behind. Brand names and the deliberately English app mock are excluded.
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from t_ld import LANGS

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGES = {'index': 'index.html', 'privacy': 'privacy/index.html', 'help': 'help/index.html'}

# Regions that are English on every locale by design.
DROP = [
    r'<div class="kp-demo.*?<ul class="pro-points" id="kpPoints">',   # Kapture Pro mock
    r'<div class="sm-demo.*?<ul class="pro-points" id="smPoints">',   # Smart mock
    r'<div class="lg reveal".*?</ul>\s*</div>',                       # Languages mock
    r'<div class="cap-panel".*?</div>\s*</div>\s*</div>',             # extension mock
    r'<span class="hero-panel.*?</span>\s*</span>',                   # hero panel mock
    r'<div class="kp-fit".*?</div>\s*</div>\s*</div>',                # hero Mac mock
    r'<script.*?</script>', r'<!--.*?-->', r'<svg.*?</svg>', r'<style.*?</style>',
]
ALLOW = {
    'Kapture', 'Kapture Pro', 'Chrome', 'Google Chrome', 'Mac', 'Windows', 'macOS',
    'PNG, JPEG or PDF', 'kaptapp.com', 'Kumo Studio', 'Smart', 'PDF', 'PNG', 'JPEG',
    # Interface text inside the rendered app mocks. Neither product's UI is
    # translated on this site, by the same decision that keeps the screenshots
    # of it in English, so these are expected in every locale.
    'Every screenshot and PDF in your Kapture folder.',
    'Search captures, projects or tags',
    'Captures that are not in a Project yet, from every source.',
    'Captures whose files are exactly the same, byte for byte.',
    'Captures worth a second look. Nothing here is removed for you.',
    'Where your captures came from.',
    'Tidying you asked Kapture to do for you.',
}


def sentences(html):
    for pat in DROP:
        html = re.sub(pat, ' ', html, flags=re.S)
    txt = re.sub(r'<[^>]+>', '\n', html)
    txt = (txt.replace('&middot;', '.').replace('&nbsp;', ' ').replace('&amp;', '&')
              .replace('&#8209;', '-').replace('&rarr;', '').replace('&ntilde;', 'n'))
    out = set()
    for line in txt.split('\n'):
        line = re.sub(r'\s+', ' ', line).strip()
        # Long enough to be prose, and containing a space, so labels are ignored.
        if len(line) >= 40 and ' ' in line and line not in ALLOW:
            out.add(line)
    return out


def main():
    en = {p: sentences((ROOT / f).read_text()) for p, f in PAGES.items()}
    bad = 0
    for lang in LANGS:
        if lang == 'en':
            continue
        for page, f in PAGES.items():
            got = sentences((ROOT / lang / f).read_text())
            leaks = sorted(got & en[page])
            for s in leaks:
                print('  %-6s %-8s %s' % (lang, page, s[:96]))
                bad += 1
    print('  English sentences still present in a translated page:', bad)
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
