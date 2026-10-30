"""Browser tests for the Kapture Pro connect mode of /account/, in Chromium, Chrome, WebKit and Firefox.
Usage: python3 tools/test_account_connect.py [site root] [screenshot dir]   (needs Playwright)
The local Kaptweb files are served at the real https://kaptapp.com origin through request
interception, Supabase is mocked, and a stand-in Kapture Pro listens on 127.0.0.1. Fake tokens only."""
import http.server, json, mimetypes, pathlib, socketserver, sys, threading, time, urllib.parse
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent)
SB = "https://sokcwfqvutnjzzbsuhqm.supabase.co"
STATE = "A" * 20 + "b-_" + "Z" * 20  # 43 chars
TOK = {"access_token": "fake-access-NEW", "refresh_token": "fake-refresh-NEW", "expires_at": "1900000000"}
HASH = "#" + urllib.parse.urlencode({**TOK, "expires_in": "3600", "token_type": "bearer", "type": "magiclink"})
WEB = {"access_token": "web-access-OLD", "refresh_token": "web-refresh-OLD"}

got = []
class App(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        got.append({"path": self.path, "origin": self.headers.get("Origin"), "ctype": self.headers.get("Content-Type"),
                    "fields": {k: v[0] for k, v in urllib.parse.parse_qs(self.rfile.read(n).decode()).items()}})
        page = b"<!doctype html><title>Kapture Pro</title><p id=ok>Kapture Pro is signed in. You can close this tab.</p>"
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", str(len(page))); self.end_headers(); self.wfile.write(page)
srv = socketserver.TCPServer(("127.0.0.1", 0), App); PORT = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
# A port with nothing listening, for the "app no longer waiting" case.
s2 = socketserver.TCPServer(("127.0.0.1", 0), App); DEAD = s2.server_address[1]; s2.server_close()

def setup(ctx, calls, user_status=200):
    def site(route):
        path = urllib.parse.urlparse(route.request.url).path
        f = ROOT / path.lstrip("/")
        if f.is_dir(): f = f / "index.html"
        if not f.exists(): return route.fulfill(status=404, body="")
        route.fulfill(status=200, body=f.read_bytes(), content_type=mimetypes.guess_type(str(f))[0] or "application/octet-stream")
    def supa(route):
        r = route.request; u = urllib.parse.urlparse(r.url)
        calls.append({"m": r.method, "path": u.path, "q": u.query, "auth": r.headers.get("authorization"), "body": r.post_data})
        cors = {"access-control-allow-origin": "*", "access-control-allow-headers": "*", "access-control-allow-methods": "*"}
        if r.method == "OPTIONS": return route.fulfill(status=204, headers=cors)
        if u.path == "/auth/v1/user":
            return route.fulfill(status=user_status, headers=cors, json={"id": "u1", "email": "me@example.test"} if user_status == 200 else {"msg": "bad"})
        if u.path.startswith("/auth/v1/logout"): return route.fulfill(status=204, headers=cors)
        if u.path == "/auth/v1/otp": return route.fulfill(status=200, headers=cors, json={})
        if u.path.endswith("get_my_access"): return route.fulfill(status=200, headers=cors, json=[{"pro": False, "state": "none"}])
        return route.fulfill(status=200, headers=cors, json=[])
    ctx.route("https://kaptapp.com/**", site)
    ctx.route(SB + "/**", supa)
    ctx.route("https://fonts.googleapis.com/**", lambda r: r.fulfill(status=200, body="", content_type="text/css"))

ACC = "https://kaptapp.com/account/"
def store(pg): return pg.evaluate("() => ({c: localStorage.getItem('kapture.app_connect'), s: localStorage.getItem('kapture.session')})")
def st(pg): return pg.get_attribute("main.ac", "data-state")
def visible(pg, sel): return pg.is_visible(sel)

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

def run(engine_name, bt, opts):
    br = bt.launch(headless=True, **opts)
    def fresh(**kw):
        ctx = br.new_context(); calls = []; setup(ctx, calls, **kw); pg = ctx.new_page()
        logs = []; pg.on("console", lambda m: logs.append(m.text))
        return ctx, pg, calls, logs
    E = engine_name

    # 1. Normal page untouched.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC); pg.wait_for_function("document.querySelector('main.ac').dataset.state !== 'loading'")
    check(f"{E}: plain visit shows sign-in, no connect note, nothing stored", st(pg) == "signed-out" and not visible(pg, "#acConnectNote") and store(pg)["c"] is None)
    ctx.close()

    # 2. Normal link return still signs in to the website.
    ctx, pg, calls, logs = fresh(); pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'signed-in'")
    s = json.loads(store(pg)["s"] or "{}")
    check(f"{E}: normal link signs in to the website and strips the fragment", s.get("refresh_token") == TOK["refresh_token"] and "#" not in pg.url and "fake" not in pg.url)
    ctx.close()

    # 3. Invalid requests are refused and not stored.
    for bad in [f"port=80&state={STATE}&platform=macos", f"port={PORT}&state=short&platform=macos", f"port={PORT}&state={STATE}&platform=linux",
                f"port=70000&state={STATE}&platform=windows", f"port=1e4&state={STATE}&platform=macos", f"port={PORT}&state={STATE}%3Cx&platform=macos"]:
        ctx, pg, calls, logs = fresh(); pg.goto(ACC + "?app=connect&" + bad)
        check(f"{E}: invalid request refused ({bad.split('&')[0] if 'port=' + str(PORT) not in bad else bad.split('&')[1 if 'state=' + STATE not in bad else 2]})",
              st(pg) == "error" and store(pg)["c"] is None and "?" not in pg.url, pg.text_content("#acErrorText"))
        ctx.close()

    # 4-5. Full connect: request stored, email sent unchanged, consent, POST to loopback; web session untouched.
    ctx, pg, calls, logs = fresh()
    pg.goto(ACC); pg.evaluate("s => localStorage.setItem('kapture.session', JSON.stringify(s))", WEB)
    pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos")
    c = json.loads(store(pg)["c"] or "{}")
    check(f"{E}: valid request stored for 15 min and query removed", c.get("state") == STATE and c.get("port") == PORT and 890e3 < c["expires"] - time.time() * 1000 <= 900e3 and pg.url == ACC)
    check(f"{E}: sign-in form shown with the connect note", st(pg) == "signed-out" and visible(pg, "#acConnectNote"))
    pg.fill("#acEmail", "me@example.test"); pg.click("#acSend"); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'link-sent'")
    otp = [x for x in calls if x["path"] == "/auth/v1/otp"][0]
    check(f"{E}: email sent exactly as today (redirect_to unchanged)", urllib.parse.parse_qs(otp["q"])["redirect_to"] == [ACC] and json.loads(otp["body"]) == {"email": "me@example.test", "create_user": True})
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'connect'")
    check(f"{E}: fragment removed, consent shows the account", "#" not in pg.url and pg.text_content("#acConnectEmail") == "me@example.test" and visible(pg, "#acConnectYes"))
    u = [x for x in calls if x["path"] == "/auth/v1/user"]
    check(f"{E}: account checked with the new token", u and u[-1]["auth"] == "Bearer " + TOK["access_token"])
    check(f"{E}: website session not replaced", json.loads(store(pg)["s"]) == WEB)
    got.clear(); pg.click("#acConnectYes"); pg.wait_for_url(f"http://127.0.0.1:{PORT}/**", timeout=10000); pg.wait_for_selector("#ok")
    post = got[0] if got else {}
    check(f"{E}: one POST to 127.0.0.1 with exactly state and tokens", len(got) == 1 and post["path"] == "/kapture-auth/callback" and post["fields"] == {"state": STATE, **TOK}
          and post["ctype"].startswith("application/x-www-form-urlencoded"), f"origin={post.get('origin')}")
    check(f"{E}: no token in the app's URL", "fake" not in pg.url)
    pg.goto(ACC); pg.wait_for_function("document.querySelector('main.ac').dataset.state !== 'loading'")
    check(f"{E}: request single use (gone after Connect); website session still the old one", store(pg)["c"] is None and json.loads(store(pg)["s"]) == WEB)
    check(f"{E}: no tokens in console", not any("fake" in l or "web-" in l for l in logs))
    ctx.close()

    # 6. Cancel ends that session and sends nothing.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=windows")
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'connect'")
    got.clear(); pg.click("#acConnectNo"); pg.wait_for_timeout(300)
    lo = [x for x in calls if x["path"] == "/auth/v1/logout"]
    check(f"{E}: Cancel logs that session out, sends nothing, drops the request",
          lo and lo[-1]["auth"] == "Bearer " + TOK["access_token"] and "scope=local" in lo[-1]["q"] and not got and store(pg)["c"] is None
          and store(pg)["s"] is None and pg.text_content("#acConnectTitle") == "Not connected" and not visible(pg, "#acConnectYes"))
    ctx.close()

    # 6b. Consent asks people who did not start it from the app to cancel.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos")
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'connect'")
    check(f"{E}: consent tells people to cancel if they did not start it", "otherwise choose Cancel" in pg.text_content("#acConnectHint"))
    ctx.close()

    # 6c. A request and a sign-in in the same address: the sign-in is ended, not kept or handed over.
    ctx, pg, calls, logs = fresh(); got.clear()
    pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos" + HASH); pg.wait_for_timeout(300)
    lo = [x for x in calls if x["path"] == "/auth/v1/logout"]
    check(f"{E}: request plus fragment ends that sign-in", lo and lo[-1]["auth"] == "Bearer " + TOK["access_token"] and store(pg)["s"] is None
          and not got and "#" not in pg.url and "?" not in pg.url and st(pg) == "signed-out")
    ctx.close()

    # 7. An expired request is ignored: the link signs in to the website as usual.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC)
    pg.evaluate("r => localStorage.setItem('kapture.app_connect', JSON.stringify(r))", {"port": PORT, "state": STATE, "platform": "macos", "expires": int(time.time() * 1000) - 1})
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'signed-in'")
    check(f"{E}: expired request discarded, normal sign-in", store(pg)["c"] is None and store(pg)["s"] is not None)
    ctx.close()

    # 8. Request expires while the question is on screen.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos")
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'connect'")
    pg.evaluate("() => { const r = JSON.parse(localStorage.getItem('kapture.app_connect')); r.expires = Date.now() - 1; localStorage.setItem('kapture.app_connect', JSON.stringify(r)); }")
    got.clear(); pg.click("#acConnectYes"); pg.wait_for_timeout(300)
    check(f"{E}: expiry before Connect sends nothing and logs out", not got and pg.url == ACC and pg.text_content("#acConnectTitle") == "Not connected"
          and any(x["path"] == "/auth/v1/logout" for x in calls))
    ctx.close()

    # 9. Tampered stored request (port changed to a non-loopback-looking value) is rejected.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC)
    pg.evaluate("r => localStorage.setItem('kapture.app_connect', JSON.stringify(r))", {"port": "8080/evil", "state": STATE, "platform": "macos", "expires": int(time.time() * 1000) + 60000})
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'signed-in'")
    check(f"{E}: malformed stored request ignored", store(pg)["c"] is None)
    ctx.close()

    # 10. Bad token: /user fails -> error, session ended, nothing posted.
    ctx, pg, calls, logs = fresh(user_status=401); pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos")
    got.clear(); pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'error'")
    check(f"{E}: unverifiable sign-in fails safely", not got and any(x["path"] == "/auth/v1/logout" for x in calls))
    ctx.close()

    # 11. Storage blocked: clear message, nothing else happens.
    ctx, pg, calls, logs = fresh(); pg.add_init_script("Storage.prototype.setItem = function () { throw new Error('blocked'); }")
    pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos")
    check(f"{E}: blocked storage fails with a clear message", st(pg) == "error" and "remember the request" in pg.text_content("#acErrorText"))
    ctx.close()

    # 12. App no longer listening: request already consumed, browser shows its own error, tokens not in URL.
    ctx, pg, calls, logs = fresh(); pg.goto(ACC + f"?app=connect&port={DEAD}&state={STATE}&platform=macos")
    pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'connect'")
    try:
        pg.click("#acConnectYes"); pg.wait_for_timeout(1500)
    except Exception: pass
    check(f"{E}: dead listener: no token in URL, request consumed", "fake" not in pg.url, pg.url[:60])
    ctx.close()

    # 13. Responsive: consent panel at three widths, no horizontal overflow.
    for w in (360, 768, 1280):
        ctx = br.new_context(viewport={"width": w, "height": 800}); calls = []; setup(ctx, calls); pg = ctx.new_page()
        pg.goto(ACC + f"?app=connect&port={PORT}&state={STATE}&platform=macos")
        if w == 360: pg.screenshot(path=str(OUT / f"{E.split()[0]}-{w}-signin.png"), full_page=True)
        pg.goto("about:blank"); pg.goto(ACC + HASH); pg.wait_for_function("document.querySelector('main.ac').dataset.state === 'connect'")
        over = pg.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        pg.screenshot(path=str(OUT / f"{E.split()[0]}-{w}.png"), full_page=True)
        check(f"{E}: {w}px no horizontal overflow", over <= 0, f"overflow {over}")
        ctx.close()
    br.close()

OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/kapture-connect-shots"); OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
    for name, bt, opts in [("Chromium", p.chromium, {}), ("Chrome", p.chromium, {"channel": "chrome"}), ("WebKit", p.webkit, {}), ("Firefox", p.firefox, {})]:
        try: run(name, bt, opts)
        except Exception as e: results.append((f"{name}: run crashed", False, str(e).splitlines()[0][:200]))
srv.shutdown()
for n, ok, d in results: print(("PASS " if ok else "FAIL ") + n + (f"  [{d}]" if d and not ok else (f"  [{d}]" if "origin=" in d else "")))
print(f"\n{sum(ok for _, ok, _ in results)}/{len(results)} passed")
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
