# 07 — Solution Design Options

**Agent:** Solution Design. For the lead opportunity (C1, with the others as parallels), design solutions from simple→complex and recommend the **cheapest path to first paid validation.**

> Rule honored: prefer manual/concierge over platform; prefer paid validation over beautiful product; use AI only where it adds real value; do **not** force blockchain.

## Solution ladder for "Recover" (revenue-recovery agent)

| # | Solution | What it does | Who pays | Build difficulty | Sales difficulty | First paid test? |
|---|----------|--------------|----------|------------------|------------------|------------------|
| 1 | **Manual concierge** | Founder gets a CSV export of one shop's declined estimates / lapsed customers, manually writes & sends personalised recovery messages (with owner's sign-off), books returns | Owner, contingency (e.g., 15–25% of recovered revenue) | **Trivial** | Low (owner-led) | **Yes — week 1** |
| 2 | Landing page + manual backend | "We recover the revenue your front desk doesn't have time to chase. Pay only for what we recover." Form → founder does #1 by hand | Owner | Trivial | Low | Yes |
| 3 | No-code semi-automation | Zapier/Make + LLM API drafts messages from the export; founder reviews/sends | Owner | Low | Low | Yes |
| 4 | Lightweight AI assistant | Connect to one PMS via export/API; AI classifies lost-revenue events, drafts multi-touch sequences; human approves | Owner, low SaaS + success fee | Medium | Medium | Yes |
| 5 | SaaS dashboard | Self-serve: connect system-of-record, see "$X recoverable," approve campaigns, track recovered $ | Owner, SaaS + % | Medium-High | Medium | After 5–10 concierge wins |
| 6 | API/integration product | Deep PMS/POS integrations per vertical | Owner | High | Medium | Later |
| 7 | Autonomous agent | Fully automated recovery with guardrails | Owner | High | Medium-High | Later |
| 8 | Verification/trust layer | Tamper-evident log of customer consent/opt-out (compliance) | — | — | **Skip unless needed** |
| 9–10 | Full platform | Multi-vertical, marketplace | — | Very High | — | **Do NOT build yet** |

### Recommended path: **Start at #1 (manual concierge), graduate to #4.**

- **Why concierge first:** It validates the *only* thing that matters — *will owners pay for recovered revenue?* — with **zero build**. The founder learns the message templates, objection patterns, and per-vertical recovery rates that become the AI's training signal. This is the cheapest path to a paid "yes."
- **Pricing for the test:** **Contingency (15–25% of recovered revenue)** or a small pilot fee + success fee. Contingency makes the buyer's decision near-frictionless and proves WTP unambiguously.
- **AI's role:** Becomes the engine at #3–#4 (drafting, classification, sequencing, reconciliation). Genuinely additive — persistent, personalised, scalable follow-up no front desk delivers.
- **Blockchain's role:** **None.** Explicitly excluded. (The only place a verifiable record appears is the *optional* consent/opt-out log at #8, and even that is a normal database + audit trail, not a chain.)

## Parallel solution notes (other survivors)

- **N7 collections:** Same ladder — concierge dunning on contingency → vertical SaaS. Add lien-compliance checklist automation as the moat.
- **N6 quoting:** Concierge = founder turns the shop's RFQs into draft quotes overnight → AI drafting with human approval. Liability means *human always approves*.
- **C3 scope-creep:** Concierge = founder reviews an agency's week of project comms, flags out-of-scope, drafts the change-order email. **Reframe to overcome behavioral barrier:** the product must *send the diplomatic change order + keep the defensible record*, not just detect. This is where a tamper-evident approval log is a genuine thin feature.

## Why this is better than current alternatives (lead solution)

| Current alternative | Why "Recover" beats it |
|---|---|
| Front-desk works the list | It never does (first task dropped); AI is persistent & consistent |
| Generic recall/reminder blast | Personalised, event-specific, multi-touch — higher recovery |
| Hire an ISA/VA ($900–1,500/mo) | Contingency = pay only for results; no hiring/management |
| Reactivation point tools | Outcome-priced + cross-system; owner doesn't configure campaigns |

**Recommendation to founder:** The cheapest path to a paid "yes" is to **sell the concierge service to 3 owners this month on contingency**, before writing any product code. Passed to Willingness-to-Pay (Stage 8).
