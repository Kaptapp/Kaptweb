"""Set the privacy policy's Effective date in all nine languages, then rebuild
the localised privacy pages. Terms keep their own date.

    python3 tools/set_privacy_date.py . YYYY-MM-DD   # on publication day
"""
import datetime, os, re, sys
R, iso = sys.argv[1], sys.argv[2]
d = datetime.date.fromisoformat(iso)
EN_M = "January February March April May June July August September October November December".split()
ES_M = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
DE_M = "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split()
FR_M = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()
PT_M = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()
IT_M = "gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split()
y, m, n = d.year, d.month, d.day
P = lambda t: f'<p class="legal-date">{t}</p>'
en = P(f"Effective {n} {EN_M[m-1]} {y}")
vals = {
 "es": P(f"En vigor desde el {n} de {ES_M[m-1]} de {y}"),
 "zh": P(f"自 {y} 年 {m} 月 {n} 日起生效"),
 "ko": P(f"{y}년 {m}월 {n}일 시행"),
 "ja": P(f"{y} 年 {m} 月 {n} 日発効"),
 "de": P(f"Gültig ab {n}. {DE_M[m-1]} {y}"),
 "fr": P(f"En vigueur depuis le {'1er' if n == 1 else n} {FR_M[m-1]} {y}"),
 "pt-br": P(f"Em vigor desde {'1º' if n == 1 else n} de {PT_M[m-1]} de {y}"),
 "it": P(f"In vigore dal {'1°' if n == 1 else n} {IT_M[m-1]} {y}"),
}
# English source
p = os.path.join(R, "privacy/index.html"); s = open(p, encoding="utf-8").read()
old = re.findall(r'<p class="legal-date">Effective [^<]+</p>', s); assert len(old) == 1, old
s = s.replace(old[0], en); open(p, "w", encoding="utf-8").write(s)
# translation pass: one entry for the current date, replacing any earlier one
tp = os.path.join(R, "tools/t_stats.py"); t = open(tp, encoding="utf-8").read()
t = re.sub(r"'<p class=\"legal-date\">Effective [^']+</p>': \{\n(?: '[^']+': '[^\n]*',?\}?,?\n)+", "", t)
entry = f"{en!r}: {{\n" + ",\n".join(f" {l!r}: {v!r}" for l, v in vals.items()) + "},\n"
assert t.count("STATS_PRIV = {\n") == 1
t = t.replace("STATS_PRIV = {\n", "STATS_PRIV = {\n" + entry, 1)
open(tp, "w", encoding="utf-8").write(t)
# rebuild localised privacy pages only
sys.path.insert(0, os.path.join(R, "tools")); os.chdir(os.path.join(R, "tools"))
import build_i18n as b
for lang in [l for l in b.LANGS if l != "en"]:
    out = b.build(lang, "privacy")
    assert vals[lang] in out.read_text(encoding="utf-8"), lang
print("privacy Effective date set to", iso, "in 9 languages")
