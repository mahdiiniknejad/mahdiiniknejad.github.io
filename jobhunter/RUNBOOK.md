# RUNBOOK — how to actually run the pipeline

## What's here
A working job-application pipeline. Stages 2–4 (score, tailor, review queue) run
anywhere. Stage 1 (scrape) needs **outbound web access**.

```
jobhunter/
  pipeline/scrape.py     Stage 1 — Playwright scraper -> data/jobs.csv
  pipeline/sources.yml   which job boards + CSS selectors to read
  pipeline/score.py      Stage 2 — hard filters + 0-100 score -> data/shortlist.csv
  pipeline/tailor.py     Stage 3 — per-job CV/letter/answers -> apps/ + data/queue.json
  queue.html             Stage 4 — phone-friendly review page (reads data/queue.json)
  profile.md preferences.md templates/   your inputs (git-ignored: kept private)
```

## ⚠️ The network catch (read this)
The scrape stage was **built and tested, but could not be run** in the Claude Code
*web* environment where it was created: that session's network policy blocks every
job board (`403 policy denial` at the proxy — jobs.ac.uk, indeed, ucd.ie, even
google). Playwright/Chromium work fine; there's just nowhere to browse.

**Run Stage 1 where the network is open:**
- **Your phone/desktop Claude Code** (the original plan): `claude mcp add playwright`,
  then ask Claude to run `pipeline/scrape.py`. OR
- **Your own machine**: `pip install playwright pyyaml python-docx && playwright install chromium`,
  then `python pipeline/scrape.py`. OR
- A remote environment whose **network policy allows** those domains.

Stages 2–4 have no such restriction — they run in any session.

## Run it
```bash
cd jobhunter
pip install playwright pyyaml python-docx        # once
python pipeline/scrape.py --max 40               # Stage 1 (needs web) -> data/jobs.csv
python pipeline/score.py  --min-score 40         # Stage 2 -> data/shortlist.csv
python pipeline/tailor.py --batch 25 --offset 0  # Stage 3, first 25 -> apps/ + queue.json
#   next evenings: --offset 25, 50, 75  (25/day = 100 in 4 days)
```
Then open **queue.html** on your phone and tap through: each card has the posting
link, tailored Letter PDF, CV PDF, and copy-paste form answers.

## Hosting the queue on your site
`queue.html` is committed so it can live at `mahdiiniknejad.github.io/jobhunter/queue.html`
once this branch is merged to `main`. But `data/queue.json` (your real applications)
is **git-ignored on purpose** — this repo is public. Two safe ways to use it:
- Open `queue.html` and use the built-in **"Load queue.json" file picker** to load
  the file from your phone/device — nothing is published. *(recommended)*
- Or, if you accept that your queue would be publicly readable, un-ignore and commit
  `data/queue.json` yourself.

## The rules the tailoring obeys (from CLAUDE.md)
- Never auto-submits — every card needs your tap.
- Never invents facts. Research output is written exactly as "in preparation".
- Uses only what's in `profile.md` / `preferences.md`. Missing info → status BLOCKED.
- The scorer's hard filters auto-reject: completed ACCA/ACA required, 5+ yrs experience,
  work permission beyond your Stamp 2.

## Note on CV tailoring
`tailor.py` ships each app with your **base CV** (`cv.pdf` from templates) plus a
**per-job cover letter** and **form answers** that mirror the posting's language.
Deep per-job CV bullet-reordering is best done by Claude in-session on the shortlist
(a deterministic script shouldn't rewrite your CV) — ask: *"reorder the CV bullets in
apps/<folder>/ to match its meta.json posting."*
