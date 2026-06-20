# 16 — Source Verification Agent

**Agent:** Source Verification. Classify the load-bearing factual claims in the pipeline. **Rule: Unsupported claims must not enter the final business plan (files 13/14).**

## Verification status legend
Verified by source · Partly supported · Unsupported · Contradicted · Needs human check

## Verification table (load-bearing claims)

| # | Claim | Appears in | Source(s) | Source quality | Status | Risk if wrong | Keep/Revise/Delete |
|---|-------|-----------|-----------|----------------|--------|---------------|--------------------|
| 1 | Late/unpaid payment is endemic across services (agencies 97%, construction 82% >30d / $64B, freelancers 85%) | 01,03,13 | Ignition 2025; BD+C/Rabbet; Freelancers Union; agiled | Medium-high (some vendor) | **Partly supported** (frequencies corroborated; magnitudes vendor-soft) | Over-claim magnitude | **Keep, hedged** |
| 2 | Voice-receptionist/lead-gen is a funded red ocean (Beside $32M; ElevenLabs/Vapi/Retell) | 01,02,04,13 | Fortune/Yahoo (Beside raise); market roundups | High (named funding) | **Verified** | Mis-call crowding | **Keep** |
| 3 | Blockchain trade/supply consortia failed (TradeLens, We.Trade, Marco Polo, Contour, Everledger dead) | 00,03,13 | GTR; Ledger Insights; Maersk; CoinDesk; Computerworld | High (news) | **Verified** | Wrongly dismiss blockchain | **Keep** |
| 4 | Dental leaves $1M–1.5M unscheduled treatment/provider; 15–20% attrition | 02,03,10 | clerri.com; dentalbilling.com | Low-med (vendor) | **Partly supported** | Over-state recoverable $ | **Keep as directional; verify in pilots** |
| 5 | Dental offices spend 6+ hrs/wk on insurance verification (55%) | 02,03 | Weave (via daydream.dental); Daily Dot | Low-med (vendor + anecdote) | **Partly supported** | Over-state C4 pain | **Keep, hedged** |
| 6 | Optometry ~25% no-show; manual recall 3–5% at 4.5 hrs/100 | 03,10 | ICO study (rate); irismed/revolutionEHR (recall) | Med (rate) / low (recall) | **Partly supported** | Over-state leakage | **Keep, hedged** |
| 7 | Job shops: ~4% RFQ-bucket win; 78% buy from first responder; Excel+eyeball top-2 methods | 03,04,05,10 | practicalmachinist; mmsonline; simplyask.ai | Med (trade press + vendor) | **Partly supported** | Over-state N6 | **Keep, hedged** |
| 8 | Self-storage: 10–15 hrs/mgr/mo collections at 3–4% delinquency; 90–120-day lien process | 03,05,10 | ai-lean; storagepug; insideselfstorage | Low-med (vendor) + legal | **Partly supported** (lien timelines verifiable; hours vendor) | Over-state N7 | **Keep, hedged** |
| 9 | Contingency/outcome pricing is accepted (RCM cuts 5–30%; ISAs $900–1,500/mo) | 08,11,12 | vendor pricing; RCM norms | Medium | **Verified (directionally)** | WTP structure wrong | **Keep** |
| 10 | Market-size $ (TAM/SAM/SOM) | 10 | analyst/vendor estimates (divergent) | Low | **Unsupported as precise** (explicitly labelled directional) | False precision | **Keep ONLY as labelled-directional** |
| 11 | "Blockchain adds no value to revenue recovery" | 03,13,14 | reasoning + adjacent-market failure evidence | High (logical + #3) | **Verified (reasoned)** | — | **Keep** |
| 12 | AI is genuinely suited to personalised persistent follow-up | all | LLM capability (assistant domain knowledge) | High | **Verified** | — | **Keep** |

## Claims downgraded out of the final plan
- Any precise market-size $ → **kept only as explicitly-labelled directional**, never as fact.
- All per-business dollar magnitudes (dental $1M+, storage hours, etc.) → **reclassified as hypotheses to be measured in the concierge pilots** (see file 18), not as proven facts the plan depends on.

## Overall data-quality statement
The pipeline's **directions and frequencies are well-supported**; its **magnitudes are largely vendor-sourced and inflation-prone**, because research agents could not fetch primary sources (Reddit/G2/Capterra 403-blocked) and relied on search snippets. **No claim that the business *depends on* is left as "Unsupported" in files 13/14** — the dependence has been shifted to *testable assumptions* (file 18). The single biggest residual risk: the recoverable-revenue magnitudes that justify contingency pricing are not yet primary-verified — **which is exactly what the 30-day paid pilot measures.**
