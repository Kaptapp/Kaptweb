"""Browser tests for redeeming an access code (friends and family) on /account/, in Chromium, Chrome, WebKit and Firefox.
Usage: python3 tools/test_account_code.py [site root] [screenshot dir]   (needs Playwright)
The local Kaptweb files are served at the real https://kaptapp.com origin through request
interception and Supabase is mocked. Fake tokens only."""
import json, mimetypes, pathlib, sys, urllib.parse
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent)
SB = "https://sokcwfqvutnjzzbsuhqm.supabase.co"
TOK = {"access_token": "fake-access-CODE", "refresh_token": "fake-refresh-CODE", "expires_at": "1900000000"}
HASH = "#" + urllib.parse.urlencode({**TOK, "expires_in": "3600", "token_type": "bearer", "type": "magiclink"})
NONE = {"pro": False, "plan": "none", "state": "none"}
TRIAL = {"pro": True, "plan": "trial", "state": "trialing", "trial_started_at": "2026-11-01T00:00:00Z", "trial_ends_at": "2026-11-15T00:00:00Z", "seats_max": 2}
PAID = {"pro": True, "plan": "monthly", "state": "active", "access_until": "2026-12-01T00:00:00Z", "seats_max": 2}
MANUAL = {"pro": True, "plan": "manual", "state": "active", "access_until": None, "seats_max": 2}

def setup(ctx, calls, world):
    def site(route):
        path = urllib.parse.urlparse(route.request.url).path
        f = ROOT / path.lstrip("/")
        if f.is_dir(): f = f / "index.html"
        if not f.exists(): return route.fulfill(status=404, body="")
        route.fulfill(status=200, body=f.read_bytes(), content_type=mimetypes.guess_type(str(f))[0] or "application/octet-stream")
    def supa(route):
        r = route.request; u = urllib.parse.urlparse(r.url)
        calls.append({"m": r.method, "path": u.path, "auth": r.headers.get("authorization"), "body": r.post_data})
        cors = {"access-control-allow-origin": "*", "access-control-allow-headers": "*", "access-control-allow-methods": "*"}
        if r.method == "OPTIONS": return route.fulfill(status=204, headers=cors)
        if u.path == "/auth/v1/user": return route.fulfill(status=200, headers=cors, json={"id": "u1", "email": "friend@example.test"})
        if u.path == "/auth/v1/otp": return route.fulfill(status=200, headers=cors, json={})
        if u.path.endswith("get_my_access"): return route.fulfill(status=200, headers=cors, json=[world["access"]])
        if u.path.endswith("redeem_access_code"):
            if world["answer"] == "error": return route.fulfill(status=500, headers=cors, json={"message": "boom"})
            if world["answer"] == "granted": world["access"] = MANUAL
            return route.fulfill(status=200, headers=cors, json=world["answer"])
        return route.fulfill(status=200, headers=cors, json=[])
    ctx.route("https://kaptapp.com/**", site)
    ctx.route(SB + "/**", supa)
    ctx.route("https://fonts.googleapis.com/**", lambda r: r.fulfill(status=200, body="", content_type="text/css"))

ACC = "https://kaptapp.com/account/"
def st(pg): return pg.get_attribute("main.ac", "data-state")
def stored(pg): return pg.evaluate("() => localStorage.getItem('kapture.access_code')")
def signed_in(pg): pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'signed-in'")
def redeem_calls(calls): return [x for x in calls if x["path"].endswith("redeem_access_code") and x["m"] == "POST"]

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

def run(E, bt, opts):
    br = bt.launch(headless=True, **opts)
    def fresh(access=NONE, answer="granted", **kw):
        ctx = br.new_context(**kw); calls = []; world = {"access": access, "answer": answer}; setup(ctx, calls, world); pg = ctx.new_page()
        logs = []; pg.on("console", lambda m: logs.append(m.text))
        return ctx, pg, calls, logs
    def sign_in(pg):
        pg.goto("about:blank"); pg.goto(ACC + HASH); signed_in(pg)

    # 1-2. The link fills the code in through the emailed sign-in; one click redeems it.
    ctx, pg, calls, logs = fresh()
    pg.goto(ACC + "?code=rayfam"); pg.wait_for_function("document.querySelector('main.ac').dataset.state !== 'loading'")
    c = json.loads(stored(pg) or "{}")
    check(f"{E}: the code link is stripped from the address bar and kept", pg.url == ACC and c.get("code") == "RAYFAM")
    check(f"{E}: signed out, the page says to sign in to redeem", st(pg) == "signed-out" and pg.is_visible("#acCodeNote"))
    sign_in(pg)
    check(f"{E}: after the emailed link the code is filled in and nothing is redeemed yet",
          pg.is_visible("#acRedeem") and pg.input_value("#acCode") == "RAYFAM" and not redeem_calls(calls))
    pg.click("#acRedeemBtn"); pg.wait_for_function("document.getElementById('acRedeem').hidden === true")
    rc = redeem_calls(calls)
    check(f"{E}: one redemption, with the session in a header and only the code in the body",
          len(rc) == 1 and rc[0]["auth"] == "Bearer " + TOK["access_token"] and json.loads(rc[0]["body"]) == {"p_code": "RAYFAM"})
    facts = pg.text_content("#acFacts")
    check(f"{E}: the licence shows as granted by Kapture with no end date", "Licence granted by Kapture" in facts and "No end date" in facts, facts)
    check(f"{E}: the note confirms it and says how to use it", "Code redeemed" in pg.text_content("#acLicenceNote"))
    check(f"{E}: the kept code is cleared", stored(pg) is None)
    check(f"{E}: no checkout, payment or billing call", not any("billing" in x["path"] or "checkout" in x["path"] for x in calls))
    check(f"{E}: no token or code in the console", not any("fake" in l or "RAYFAM" in l for l in logs))
    ctx.close()

    # 3. Refusals keep the form and say why.
    for answer, words in [("invalid", "not valid"), ("has_subscription", "Cancel the renewal"), ("rate_limited", "Too many attempts"),
                          ("already_has_access", "already has a Kapture Pro licence"), ("already_redeemed", "already redeemed"), ("error", "could not redeem")]:
        ctx, pg, calls, logs = fresh(answer=answer); sign_in(pg)
        pg.fill("#acCode", "rayfam"); pg.click("#acRedeemBtn"); pg.wait_for_selector("#acCodeError:not([hidden])")
        check(f"{E}: {answer} is explained and the form stays", words in pg.text_content("#acCodeError") and pg.is_visible("#acRedeem")
              and pg.is_enabled("#acRedeemBtn"), pg.text_content("#acCodeError"))
        ctx.close()

    # 4. Typed codes are checked before anything is sent.
    ctx, pg, calls, logs = fresh(); sign_in(pg)
    for bad in ["ab", "ray-fam", ""]:
        pg.fill("#acCode", bad); pg.click("#acRedeemBtn")
        check(f"{E}: '{bad}' is refused in the page", pg.is_visible("#acCodeError") and not redeem_calls(calls))
    pg.fill("#acCode", " ray fam "); pg.click("#acRedeemBtn"); pg.wait_for_function("document.getElementById('acRedeem').hidden === true")
    check(f"{E}: spaces and case do not matter", json.loads(redeem_calls(calls)[0]["body"]) == {"p_code": "RAYFAM"})
    ctx.close()

    # 5. Offered only where a code can help.
    for access, shown in [(NONE, True), (TRIAL, True), ({**PAID, "state": "canceling"}, True), (PAID, False), (MANUAL, False)]:
        ctx, pg, calls, logs = fresh(access=access); sign_in(pg)
        check(f"{E}: card {'shown' if shown else 'hidden'} for {access['plan']}/{access['state']}", pg.is_visible("#acRedeem") == shown)
        ctx.close()

    # 6. A plain visit stores nothing; a bad code in the link is dropped.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC); pg.wait_for_function("document.querySelector('main.ac').dataset.state !== 'loading'")
    check(f"{E}: plain visit: no code kept, no note", stored(pg) is None and not pg.is_visible("#acCodeNote"))
    pg.goto(ACC + "?code=%3Cscript%3E"); pg.wait_for_function("document.querySelector('main.ac').dataset.state !== 'loading'")
    check(f"{E}: an invalid code in the link is removed and not kept", pg.url == ACC and stored(pg) is None)
    ctx.close()

    # 7. Responsive.
    for w in (360, 1280):
        ctx, pg, calls, logs = fresh(viewport={"width": w, "height": 900}); sign_in(pg)
        pg.fill("#acCode", "x"); pg.click("#acRedeemBtn")
        over = pg.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        pg.screenshot(path=str(OUT / f"{E.split()[0]}-code-{w}.png"), full_page=True)
        check(f"{E}: {w}px no horizontal overflow", over <= 0, f"overflow {over}")
        ctx.close()
    br.close()

OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/kapture-code-shots"); OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
    for name, bt, opts in [("Chromium", p.chromium, {}), ("Chrome", p.chromium, {"channel": "chrome"}), ("WebKit", p.webkit, {}), ("Firefox", p.firefox, {})]:
        try: run(name, bt, opts)
        except Exception as e: results.append((f"{name}: run crashed", False, str(e).splitlines()[0][:200]))
for n, ok, d in results: print(("PASS " if ok else "FAIL ") + n + (f"  [{d}]" if d and not ok else ""))
print(f"\n{sum(ok for _, ok, _ in results)}/{len(results)} passed")
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
