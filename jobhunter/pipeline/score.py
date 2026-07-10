#!/usr/bin/env python3
"""
Stage 2 — SCORE.

Reads data/jobs.csv, applies hard filters (fast reject), scores each
surviving posting 0-100 against profile.md + preferences.md, and writes
data/shortlist.csv sorted by score desc with a 1-line "why fit" and
1-line "risk/gap".

Scoring is deterministic and transparent (keyword + rule based) so it's
auditable. It is a *ranking* aid, not a judgement — the human approves.

Usage: python pipeline/score.py [--min-score 40]
"""
import argparse, csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# --- from preferences.md: hard filters (auto-reject) ---
HARD_REJECT = [
    (r"\b(aca|acca|cpa)\b.{0,40}\b(qualified|fully qualified|required)\b",
     "requires completed accounting qualification"),
    (r"\b(5|6|7|8|9|10)\+?\s*years'?\s*(post[- ]qualification|industry|relevant)\s*experience",
     "requires 5+ years experience"),
    (r"\b(stamp\s*4\s*required|eu passport required|must have.*work permit|full work authorization required)\b",
     "requires work permission beyond Stamp 2"),
]

# roles ranked by preferences.md priority -> base points
ROLE_TIERS = [
    (["research assistant", "research fellow", "postdoctoral", "research officer",
      "research associate"], 30),
    (["quantitative analyst", "quant", "data analyst", "data scientist"], 26),
    (["fintech", "crypto", "digital asset", "blockchain", "web3"], 24),
    (["economist", "research economist", "policy analyst"], 22),
    (["lecturer", "assistant lecturer", "teaching assistant", "tutor", "grader"], 18),
]

# boost keywords (from preferences.md fit hints + profile.md skills)
BOOST = {
    "python": 6, "econometric": 6, "research": 5, "nlp": 5, "textual analysis": 5,
    "blockchain": 5, "digital asset": 5, "mica": 6, "tokeni": 5, "teaching": 4,
    "sme": 4, "risk": 4, "finance": 4, "stata": 3, "panel data": 4, "phd": 5,
    "smart contract": 4, "solidity": 4, "credit": 3, "valuation": 3, "defi": 4,
}
PENALIZE = {
    "software engineer": -10, "full stack": -8, "devops": -8, "sales": -12,
    "business development": -10, "head of": -8, "director": -8, "vp ": -8,
    "senior manager": -8, "account executive": -10,
}
VISA_FRIENDLY = ["university", "college", "ucd", "trinity", "dcu", "esri",
                 "central bank", "public", "institute", "smurfit", "maynooth"]


def hard_reject(text):
    for pat, reason in HARD_REJECT:
        if re.search(pat, text, re.I):
            return reason
    return None


def score_row(r):
    text = f"{r.get('title','')} {r.get('description','')} {r.get('employer','')}".lower()
    title = r.get("title", "").lower()

    reject = hard_reject(text)
    if reject:
        return None, None, reject

    score, hits = 0, []

    tier_pts = 0
    for kws, pts in ROLE_TIERS:
        if any(k in title or k in text for k in kws):
            tier_pts = max(tier_pts, pts)
            matched = next(k for k in kws if k in title or k in text)
            hits.append(matched)
    score += tier_pts

    for kw, pts in BOOST.items():
        if kw in text:
            score += pts
            if kw not in hits:
                hits.append(kw)
    for kw, pts in PENALIZE.items():
        if kw in text:
            score += pts
    if any(v in text for v in VISA_FRIENDLY):
        score += 6
        hits.append("visa-friendly employer")

    # deadline urgency nudge
    if re.search(r"\b(2026|closing|deadline)\b", text):
        score += 2

    score = max(0, min(100, score))

    gap = "review pay & hours vs Stamp 2 (max 20h/wk term-time)"
    if "phd" in text and "required" in text:
        gap = "may require completed PhD — Mahdi's is in progress"
    elif "€" not in text and "salary" not in text:
        gap = "salary not stated — confirm ≥ €20/hr before applying"
    elif re.search(r"full[- ]time|40 hours|37\.5", text):
        gap = "full-time hours may exceed Stamp 2 term-time cap (20h/wk)"

    why = "matches: " + ", ".join(dict.fromkeys(hits[:5])) if hits else "weak keyword match"
    return score, why, gap


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-score", type=int, default=40)
    args = ap.parse_args()

    src = DATA / "jobs.csv"
    if not src.exists():
        raise SystemExit(f"{src} not found — run pipeline/scrape.py first.")

    with open(src) as f:
        jobs = list(csv.DictReader(f))

    scored, rejected = [], 0
    for r in jobs:
        s, why, gap = score_row(r)
        if s is None:
            rejected += 1
            continue
        r["score"], r["why_fit"], r["risk_gap"] = s, why, gap
        scored.append(r)

    scored.sort(key=lambda r: r["score"], reverse=True)
    shortlist = [r for r in scored if r["score"] >= args.min_score]

    out = DATA / "shortlist.csv"
    cols = ["score", "title", "employer", "location", "salary", "deadline",
            "why_fit", "risk_gap", "url", "source", "description"]
    for r in shortlist:  # keep description so Stage 3 can mirror the posting's language
        r["description"] = (r.get("description", "") or "")[:4000]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(shortlist)

    print(f"Scored {len(jobs)} | hard-rejected {rejected} | "
          f"shortlisted {len(shortlist)} (score ≥ {args.min_score}) -> {out}")
    for r in shortlist[:10]:
        print(f"  {r['score']:>3}  {r['title'][:48]:48}  {r['employer'][:24]}")


if __name__ == "__main__":
    main()
