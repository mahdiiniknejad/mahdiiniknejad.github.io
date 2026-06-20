# 00 — Pipeline Architecture & Operating Memo

**Role:** Main Project Manager (PM) Agent
**Founder profile:** Solo technical founder. Strong in Solidity, smart contracts, blockchain, AI, and business/research thinking. Possible access to a smart-contract developer. Wants a *real* business, not a cool toy.
**Prime directive:** Find the single strongest opportunity where AI and/or blockchain/smart contracts solve a painful, expensive, repeated problem with reachable, paying customers — and be rewarded for *killing weak ideas*, not validating assumptions.

---

## 1. How the multi-agent pipeline is wired

The pipeline is a **funnel with verification gates**. Each agent produces a short structured memo that becomes the *input* to the next. No agent invents facts; every factual claim must carry evidence and a source, and three adversarial agents (Source Verification, Red-Team, AI Cross-Checker) sit across the flow to stop hallucination and over-claiming from reaching the final plan.

```
                         ┌──────────────────────────────────────────────┐
                         │            MAIN PM AGENT (this doc)            │
                         │  - sets scope, passes memos, enforces gates    │
                         │  - kills weak ideas, prevents looping          │
                         └──────────────────────────────────────────────┘
                                            │ broad → narrow
   DISCOVERY FUNNEL                         ▼
   1. Industry Scanner ............ 18 longlist → top 5            [01]
   2. Painpoint Discovery ......... precise pain statements        [02]
   3. Data Collection ............. real evidence tables           [03]  ← web research subagents
   4. Market Evidence ............. scorecards + GREEN/YELLOW/RED   [04]
   5. Competitor Intelligence ..... gap analysis + the wedge       [05]
   6. Customer Segment ............ first beachhead customer        [06]
   7. Solution Design ............. cheapest path to paid test      [07]
   8. Willingness-to-Pay .......... proxy-based WTP                 [08]
   9. Psychology & Positioning .... why they buy, how to say it     [09]
   10. Market Research ............ full reports for top 2–3        [10]
   11. Business Model ............. how it makes money              [11]
   12. Financial Feasibility ...... does the math work             [12]
   13. Final Validation Judge ..... hard ranking + #1 pick         [13]

   VERIFICATION LAYER (runs across the funnel, not after it)
   14. Source Verification ........ every claim classified         [in 03/13]
   15. Red-Team ................... attack to kill                 [in 13]
   16. AI-vs-AI Cross-Checker ..... independent re-score           [in 13]
   17. Assumption Register ........ what must be true + tests       [in 14/15]
   18. CTO Handoff ................ only if Build-Readiness passes  [CTO pack]

   FINAL: Build-Readiness Gate → BUILD READY / VALIDATION READY / REFRAME / KILL
```

## 2. What every agent receives (anti-hallucination contract)

Per the founder's add-on, **no agent may write from imagination**. Each handoff packet contains:

1. Previous agent's memo
2. Evidence table (claim → source → strength)
3. Source list (URLs / named reports)
4. Uncertainty list (what we don't know)
5. Open assumptions (what we're betting on)

**Hard rule:** An *Unsupported* claim cannot enter the final business plan (file 13/14). It is either downgraded to an explicit assumption (file 17, with a test) or deleted.

## 3. Evidence-strength legend (used in every table)

| Tag | Meaning |
|---|---|
| **STRONG** | Multiple independent reputable sources, or directly observable (public pricing pages, regulator text, real review volume). |
| **MEDIUM** | One credible source, or several weak ones agreeing; directionally trustworthy. |
| **WEAK** | Vendor marketing, single forum post, or PM-Agent inference. Treated as a hypothesis, not a fact. |
| **ASSUMPTION** | No source yet; must be listed in the Assumption Register (file 17) with a kill-threshold test. |

> **Transparency note from the PM Agent.** This pipeline was run by an AI with web-search sub-agents, not by a human analyst with paid database access (CB Insights, PitchBook, Gartner). Market-size numbers from "research firms" are frequently inflated press-release figures — they are tagged accordingly. **Treat this report as a rigorously-structured hypothesis engine that tells the founder exactly what to go and verify with 20 real customer conversations — not as a substitute for that primary research.** The most valuable output is not the #1 pick; it is the Assumption Register and the 30-day test plan.

## 4. PM operating rules (enforced throughout)

- Do **not** force blockchain. Use it only where trust, verification, settlement, ownership, escrow, audit-trail, or automated-obligation logic creates *advantage a normal database cannot*. Where plain software wins, say so.
- Use AI only where extraction, classification, reasoning, prediction, or personalisation creates real advantage.
- Prefer a manual/concierge MVP over a platform. Prefer paid validation over a beautiful product.
- Kill fast. Maximum two reframes per idea. No infinite loops.
- If evidence is weak, say *weak*. If a market is crowded, say *crowded*. If regulation is dangerous, say *dangerous*.
- The final recommendation must be commercially realistic for a solo technical founder, not a VC fantasy.

## 5. Reading order

Files `01` → `15` follow the funnel. If you only read three: **13** (the decision), **14** (the one-page thesis), **15** (what to do for 30 days). File **17 (Assumption Register)** is embedded in 13/14 and is where the real risk lives.
