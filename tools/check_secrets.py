# -*- coding: utf-8 -*-
"""Refuse to ship a Supabase secret.

This repository is public and GitHub Pages serves the branch root verbatim, so
anything committed here is readable twice over: on github.com and at
https://kaptapp.com/<path>. Dotfiles and the tools directory are served too,
which was measured, not assumed. A service_role key committed by accident is
therefore public the moment it is pushed.

The publishable (anon) key is deliberately not an error. It is meant to ship
inside client software and grants nothing on its own; Row Level Security is what
protects the data. It is reported so that its presence is always a visible,
deliberate fact rather than a surprise.
"""
import base64, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP_DIRS = {'.git', '__pycache__', 'node_modules'}
SELF = pathlib.Path(__file__).name

# A JWT: three base64url segments. Decoded, a Supabase key names its own role.
JWT = re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}')
NEW_SECRET = re.compile(r'\bsb_secret_[A-Za-z0-9_-]{8,}')
NEW_PUBLIC = re.compile(r'\bsb_publishable_[A-Za-z0-9_-]{8,}')

# An assignment with something actually after the "=", on the same line. The
# horizontal-only whitespace class matters: \s* would step over the newline and
# read the next variable's name as this one's value.
ASSIGNED = lambda name: re.compile(rf'{name}[ \t]*[:=][ \t]*["\']?[^\s"\'#]+')

SECRET_VARS = [
    'SUPABASE_SERVICE_ROLE_KEY', 'SUPABASE_SECRET_KEY', 'SUPABASE_JWT_SECRET',
    'SUPABASE_DB_PASSWORD', 'SUPABASE_ACCESS_TOKEN',
]


def jwt_role(token):
    """The role a Supabase JWT claims, or None if it is not one."""
    try:
        payload = token.split('.')[1]
        payload += '=' * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload)).get('role')
    except Exception:
        return None


def files():
    """Every file git is carrying: tracked plus staged. That is the set that can
    actually be committed, which is the thing being guarded. A .env sitting
    untracked and ignored on a developer machine is correct and is skipped."""
    out = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z', '--cached'],
                         capture_output=True, text=True)
    for name in out.stdout.split('\0'):
        if not name:
            continue
        p = ROOT / name
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.name == SELF:
            continue
        yield p


def main():
    problems, notes = [], []

    for p in files():
        rel = p.relative_to(ROOT)

        # A real .env must never be tracked. .env.example is the shape only.
        if (p.name == '.env' or p.suffix == '.env') and p.name != '.env.example':
            problems.append(f'{rel}: a real environment file is in the tree')
            continue

        try:
            text = p.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue

        for m in NEW_SECRET.finditer(text):
            problems.append(f'{rel}: Supabase secret key ({m.group(0)[:20]}...)')

        for m in JWT.finditer(text):
            role = jwt_role(m.group(0))
            if role == 'service_role':
                problems.append(f'{rel}: service_role JWT')
            elif role == 'anon':
                notes.append(f'{rel}: anon key (public by design)')

        for m in NEW_PUBLIC.finditer(text):
            notes.append(f'{rel}: publishable key (public by design)')

        for var in SECRET_VARS:
            if ASSIGNED(var).search(text):
                problems.append(f'{rel}: {var} has a value')

    print('  Supabase secret scan')
    for n in sorted(set(notes)):
        print(f'    note: {n}')
    if problems:
        print(f'    {len(problems)} problem(s):')
        for x in sorted(set(problems)):
            print(f'    !! {x}')
        return 1
    print('    no secrets found in the published tree')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
