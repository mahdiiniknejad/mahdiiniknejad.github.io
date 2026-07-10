#!/usr/bin/env python3
"""
Stage 1 — SCRAPE.

Reads job postings from the sources listed in sources.yml and writes
data/jobs.csv (title, employer, location, salary, deadline, url, description).
Dedupes by employer+title.

REQUIRES OUTBOUND WEB ACCESS. In a network-restricted session (e.g. the
managed Claude Code web environment whose proxy denies job boards) this
script cannot reach the sites and will report each source as blocked.
Run it in a session/machine with open network, or where the Playwright MCP
`claude mcp add playwright` was added.

Usage:
    python pipeline/scrape.py                 # all enabled sources
    python pipeline/scrape.py --source jobs_ac # one source
    python pipeline/scrape.py --max 50        # cap per source
"""
import argparse, csv, json, os, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

# Pre-installed Chromium in the managed environment (bundled build may be a
# version behind the pip package). Falls back to Playwright's own resolution.
_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
]
CHROME = next((p for p in _CANDIDATES if os.path.exists(p)), None)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def load_sources():
    import yaml
    with open(ROOT / "pipeline" / "sources.yml") as f:
        return yaml.safe_load(f)["sources"]


def scrape_source(page, src, cap):
    """Generic search-page -> result-cards parser driven by CSS selectors."""
    rows = []
    for url in src["search_urls"]:
        try:
            page.goto(url, timeout=45000, wait_until="domcontentloaded")
            page.wait_for_timeout(1500)
        except Exception as e:
            print(f"  ! {src['name']}: {url} -> {type(e).__name__}: {str(e)[:120]}")
            continue
        cards = page.locator(src["card_selector"])
        n = min(cards.count(), cap)
        for i in range(n):
            c = cards.nth(i)
            def txt(sel):
                try:
                    el = c.locator(sel)
                    return el.first.inner_text().strip() if el.count() else ""
                except Exception:
                    return ""
            def href(sel):
                try:
                    el = c.locator(sel)
                    return el.first.get_attribute("href") or "" if el.count() else ""
                except Exception:
                    return ""
            link = href(src["link_selector"])
            if link and link.startswith("/"):
                link = src["base"].rstrip("/") + link
            rows.append({
                "title": txt(src["title_selector"]),
                "employer": txt(src.get("employer_selector", "")) or src.get("default_employer", ""),
                "location": txt(src.get("location_selector", "")),
                "salary": txt(src.get("salary_selector", "")),
                "deadline": txt(src.get("deadline_selector", "")),
                "url": link,
                "description": "",
                "source": src["name"],
            })
    # follow detail pages for full description
    for r in rows:
        if not r["url"]:
            continue
        try:
            page.goto(r["url"], timeout=45000, wait_until="domcontentloaded")
            page.wait_for_timeout(800)
            sel = src.get("detail_selector", "body")
            el = page.locator(sel)
            r["description"] = (el.first.inner_text().strip()[:6000] if el.count() else "")
        except Exception as e:
            print(f"  ! detail {r['url']} -> {type(e).__name__}")
    return rows


def dedupe(rows):
    seen, out = set(), []
    for r in rows:
        key = (r["employer"].lower().strip(), r["title"].lower().strip())
        if key in seen or not r["title"]:
            continue
        seen.add(key)
        out.append(r)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source")
    ap.add_argument("--max", type=int, default=40)
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("playwright not installed. Run: pip install playwright pyyaml")

    sources = [s for s in load_sources() if s.get("enabled", True)]
    if args.source:
        sources = [s for s in sources if s["name"] == args.source]

    all_rows, launch_kw = [], {"headless": True, "args": ["--no-sandbox"]}
    if CHROME:
        launch_kw["executable_path"] = CHROME

    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kw)
        ctx = browser.new_context(user_agent=UA)
        page = ctx.new_page()
        for src in sources:
            print(f"» {src['name']} ...")
            got = scrape_source(page, src, args.max)
            print(f"  {len(got)} rows")
            all_rows += got
        browser.close()

    rows = dedupe(all_rows)
    if not rows:
        print("\nNo rows scraped. If every source printed a 403/tunnel error, "
              "this session has no outbound web access — run where the network "
              "is open (see README).")
    out = DATA / "jobs.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "employer", "location", "salary",
                                          "deadline", "url", "description", "source"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nWrote {len(rows)} deduped postings -> {out}")


if __name__ == "__main__":
    main()
