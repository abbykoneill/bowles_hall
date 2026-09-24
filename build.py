"""Assemble the site: wrap each src/pages/*.html in src/layout.html and write it to the repo root.

Each page starts with a header comment:
    <!-- title: Page title | description: One sentence | nav: about -->
`nav` names the top-level menu item to mark as current (home, about, life, apply, giving, media).
Run `python3 build.py` after editing anything in src/.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
layout = (ROOT / "src/layout.html").read_text()

for page in sorted((ROOT / "src/pages").glob("*.html")):
    text = page.read_text()
    meta_match = re.match(r"\s*<!--(.*?)-->", text, re.S)
    meta = dict(
        (k.strip(), v.strip())
        for k, v in (part.split(":", 1) for part in meta_match.group(1).split("|"))
    )
    body = text[meta_match.end():]
    html = layout
    for key in ("title", "description"):
        html = html.replace("{{" + key + "}}", meta.get(key, ""))
    html = html.replace("{{content}}", body.strip("\n"))
    nav = meta.get("nav", "")
    html = html.replace(f'data-nav="{nav}"', f'data-nav="{nav}" aria-current="page"')
    (ROOT / page.name).write_text(html)
    print("built", page.name)
