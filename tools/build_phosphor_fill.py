#!/usr/bin/env python3
"""Build the site's Phosphor Fill icon font from the official package.

Kaptweb uses Phosphor Icons, Fill weight only, from @phosphor-icons/web.
GitHub Pages serves the site and its CSP allows fonts and styles from
'self' only, so the icons are self-hosted. To keep them small, only the
icons listed in assets/icons/phosphor-fill/icons.txt are kept: the font is
subset to those glyphs and the stylesheet to their class rules.

Usage:
    npm pack @phosphor-icons/web@2.1.2 && tar -xzf phosphor-icons-web-2.1.2.tgz
    pip install fonttools brotli
    python3 tools/build_phosphor_fill.py path/to/package

Then use an icon as <i class="ph-fill ph-NAME" aria-hidden="true"></i>.
"""
import pathlib
import re
import sys

from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'icons' / 'phosphor-fill'


def main(package):
    src = pathlib.Path(package) / 'src' / 'fill'
    css = (src / 'style.css').read_text()
    version = re.search(r'"version":\s*"([^"]+)"', (pathlib.Path(package) / 'package.json').read_text()).group(1)
    wanted = [l.strip() for l in (OUT / 'icons.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]

    rules, codepoints = [], []
    for name in wanted:
        m = re.search(r'\.ph-fill\.ph-%s:before \{\s*content: "\\([0-9a-f]+)";\s*\}' % re.escape(name), css)
        if not m:
            sys.exit('not in Phosphor Fill %s: %s' % (version, name))
        codepoints.append(int(m.group(1), 16))
        rules.append('.ph-fill.ph-%s:before { content: "\\%s"; }' % (name, m.group(1)))

    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = []
    opts.name_IDs = ['*']
    opts.notdef_outline = True
    font = subset.load_font(str(src / 'Phosphor-Fill.ttf'), opts)
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=codepoints)
    sub.subset(font)
    subset.save_font(font, str(OUT / 'phosphor-fill.woff2'), opts)

    head = css[css.index('.ph-fill {'):css.index('}', css.index('.ph-fill {')) + 1]
    (OUT / 'phosphor-fill.css').write_text(
        '/* Phosphor Icons %s, Fill weight (MIT, Copyright (c) 2023 Phosphor Icons).\n'
        '   Subset of @phosphor-icons/web to the icons in icons.txt; built by\n'
        '   tools/build_phosphor_fill.py. Do not edit by hand. */\n'
        '@font-face {\n  font-family: "Phosphor-Fill";\n'
        '  src: url("phosphor-fill.woff2?v=%s") format("woff2");\n'
        '  font-weight: normal;\n  font-style: normal;\n  font-display: block;\n}\n\n'
        % (version, version) + head + '\n\n' + '\n'.join(rules) + '\n')
    (OUT / 'LICENSE.txt').write_text((pathlib.Path(package) / 'LICENSE').read_text())
    print('%d icons, %d bytes of font' % (len(wanted), (OUT / 'phosphor-fill.woff2').stat().st_size))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'package')
