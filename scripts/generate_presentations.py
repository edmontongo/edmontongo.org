#!/usr/bin/env python3
"""Generate data/presentations.json for the /presentations/ index page.

Scans content/meetup/*.md for links to the edmontongo/presentations repo
(both the {{< preslink >}} shortcode and literal GitHub links), and records
the nearest preceding Markdown heading as the talk title.

Usage:
    python3 scripts/generate_presentations.py
"""
from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parents[1]
CONTENT = SITE_ROOT / "content" / "meetup"
OUT = SITE_ROOT / "data" / "presentations.json"

REPO = "https://github.com/edmontongo/presentations"

PRESLINK_RE = re.compile(r'\{\{<\s*preslink\s+pres="([^"]+)"\s*>\}\}')
MD_LINK_RE = re.compile(
    r'\[([^\]]*)\]\((https?://github\.com/edmontongo/presentations/[^)\s]+)\)'
)
BARE_LINK_RE = re.compile(
    r'(?<![("\'])(https?://github\.com/edmontongo/presentations/[^\s)>"\']+)'
)
HEADING_RE = re.compile(r'^#{2,4}\s+(.*)$')


def front_matter(text: str) -> dict:
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    fm: dict = {}
    if not m:
        return fm
    for line in m.group(1).splitlines():
        key, _, val = line.partition(":")
        if _:
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def nearest_heading(headings: list[str]) -> str:
    for h in reversed(headings):
        if h:
            return re.sub(r'[`*_]', '', h).strip()
    return ""


def clean_title(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r'[`*_]', '', raw)
    return raw or "Presentation"


def collect_meetups() -> list[dict]:
    meetups = []
    for page in sorted(CONTENT.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        fm = front_matter(text)
        body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S)
        headings: list[str] = []
        talks: list[dict] = []
        seen: set[str] = set()
        seen_titles: set[str] = set()

        for line in body.splitlines():
            hm = HEADING_RE.match(line)
            if hm:
                headings.append(hm.group(1))
                continue

            found: list[tuple[str, str]] = []
            for pres in PRESLINK_RE.findall(line):
                found.append((f"{REPO}/tree/main/{pres}", nearest_heading(headings)))
            for anchor, url in MD_LINK_RE.findall(line):
                if "/issues" in url:
                    continue
                found.append((url, nearest_heading(headings) or clean_title(anchor)))
            for url in BARE_LINK_RE.findall(line):
                if "/issues" in url:
                    continue
                found.append((url, nearest_heading(headings)))

            for url, title in found:
                url = url.rstrip('.,;')
                title = title or "Presentation"
                if url in seen or title in seen_titles:
                    continue
                seen.add(url)
                seen_titles.add(title)
                talks.append({"title": title, "url": url})

        if not talks:
            continue
        date = fm.get("date", "")
        meetups.append({
            "title": fm.get("title", page.stem),
            "date": date,
            "url": f"/meetup/{page.stem}/",
            "talks": talks,
        })
    return meetups


def main() -> None:
    meetups = collect_meetups()

    years: list[dict] = []
    by_year: dict[str, list[dict]] = {}
    for m in meetups:
        year = (m["date"] or "0000")[:4]
        by_year.setdefault(year, []).append(m)

    for year in sorted(by_year, reverse=True):
        ms = sorted(by_year[year], key=lambda m: m["date"], reverse=True)
        years.append({"year": year, "meetups": ms})

    data = {
        "generated": _dt.date.today().isoformat(),
        "years": years,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n_talks = sum(len(m["talks"]) for m in meetups)
    print(f"wrote {OUT}  meetups={len(meetups)} talks={n_talks} years={len(years)}")


if __name__ == "__main__":
    main()
