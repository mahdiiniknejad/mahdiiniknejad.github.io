# 01 — Industry Scanner Agent: Longlist (18 candidates) → Top 5

**Agent:** Industry Scanner
**Input:** Founder profile (Solidity/smart-contracts/blockchain/AI; solo; wants fast, real revenue), PM operating rules.
**Output:** A longlist of 18 pain areas across industries, scored, with the top 5 passed to Painpoint Discovery. Cluster-level web evidence (files 03) is already informing the scoring where available; un-researched rows are scored on PM-Agent priors and flagged.

> Scoring is 1–5 (5 = best for *this founder*). "Founder adv." rewards where Solidity/smart-contract/AI skill is a *real* edge. "Blue-ocean" penalises crowded red oceans. The composite is a weighted judgement, not a sum — speed-to-revenue and MVP feasibility are weighted up because the founder wants real revenue, not a moonshot.

## The longlist

| # | Industry | Customer | Core pain | Why it exists | Today's workaround | Why workaround is bad | Tech that helps | Why now |
|---|----------|----------|-----------|---------------|--------------------|-----------------------|-----------------|---------|
| 1 | SME finance | Small biz owner | Late payment / AR chasing | Debtors deprioritise small suppliers | Manual chasing, agencies | Slow, awkward, doesn't change behaviour | AI drafting/escalation | Cash-flow squeeze |
| 2 | SME finance | Finance teams | AP / invoice reconciliation | Unstructured invoices, many vendors | Manual entry, BILL/Ramp | Crowded; Ramp free | AI extraction/matching | E-invoicing mandates |
| 3 | Cross-border work | Small firms hiring abroad | Contractor compliance & FX | 100+ tax regimes | Deel/Rippling/Wise | Regulatory moat = incumbents | AI compliance copilot | Remote work |
| 4 | Compliance/B2B | Mid-market procurement | Vendor onboarding / KYB | Fragmented business data | Manual checks, Middesk | Slow, repeated per buyer | AI + verifiable record | Fraud + sanctions pressure |
| 5 | Recruitment/HR | Employers, gig platforms | Credential/reference/employment verification | No portable trusted record | Manual calls, background-check vendors | Slow, repeated, fakeable | AI + verifiable credentials | Resume fraud, AI-faked CVs |
| 6 | Records/certs | Cert issuers, professionals | Document authenticity / tamper-proof proof | Easy to forge PDFs | Notaries, PDF, manual checks | Forgeable, no instant verify | Hash-anchoring + AI | AI-generated fakes exploding |
| 7 | Legal ops | SMEs, prof-services | Contract review & risk flagging | Lawyers expensive | Manual review, Ironclad | Costly, crowded top-end | AI extraction/reasoning | LLM contract tooling |
| 8 | Freelance/agency | Freelancers, agencies | Non-payment / scope disputes / escrow | Trust gap, weak enforcement | Upwork escrow, Escrow.com | Fees, money-transmitter law | Smart-contract escrow (maybe) | Creator economy |
| 9 | Construction | Subcontractors | Slow pay-apps, lien waivers, retention | Long payment chains | Email/PDF, Siteline | Crowded vertical SaaS | Workflow + audit trail | Construction digitising |
| 10 | Supply chain | Brands, suppliers | Provenance / chain-of-custody / cert | Multi-party, no shared truth | Paper certs, ERP | Consortia failed (TradeLens) | Blockchain (risky) | ESG regulation |
| 11 | Trade/SME | Importers/exporters | Trade docs (B/L, LC, customs) | Paper-heavy, multi-party | Freight forwarders, paper | Coordination problem | Smart contracts (risky) | Digital trade laws |
| 12 | ESG/carbon | Corporates, auditors | Sustainability-claim verification / greenwashing | Self-reported, unaudited data | Consultants, spreadsheets | Costly, untrusted, fraud-prone | AI + verifiable audit trail | CSRD / SEC climate rules |
| 13 | Healthcare admin | Clinics, billers | Prior authorisation / claims paperwork | Payer-provider friction | Fax (!), manual staff | Insanely slow, US-specific | AI extraction/automation | AI in healthcare admin |
| 14 | Real estate | Agents, buyers | Transaction docs / title / deposits | Many parties, fraud risk | Lawyers, escrow, paper | Slow, fraud (wire fraud) | Verification + escrow | Title fraud rising |
| 15 | Education | Universities, learners | Diploma/credential verification | Paper diplomas, slow registrars | Manual letters, fees | Slow, forgeable, costly | Verifiable credentials | Global mobility, fraud |
| 16 | Insurance | Insurers, SMEs | Claims doc processing / fraud | Manual claims review | Adjusters, manual | Slow, fraud leakage | AI + audit trail | Insurtech, AI claims |
| 17 | Creator economy | Creators, sponsors | Brand-deal contracts & payment proof | Informal deals, ghosting | DMs, invoices, manual | Disputes, non-payment | Contract + escrow + proof | Creator monetisation |
| 18 | Procurement/gov | Suppliers to gov/large orgs | Bid/tender compliance & audit trail | Heavy documentation | Manual, consultants | Slow, opaque, dispute-prone | AI + audit trail | Procurement digitisation |

## Scoring (1–5; higher = better for this founder)

| # | Pain | WTP | Mkt size | Founder adv. | Low compet. | MVP feas. | Speed-to-rev | Low reg. risk | Low trust barrier | Blue-ocean | **Composite** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 Late pay | 5 | 4 | 5 | 2 | 1 | 4 | 3 | 4 | 4 | 1 | **2.9** |
| 2 AP recon | 4 | 4 | 5 | 2 | 1 | 3 | 3 | 4 | 4 | 1 | **2.8** |
| 3 X-border compliance | 4 | 4 | 5 | 2 | 1 | 2 | 2 | 1 | 3 | 1 | **2.4** |
| 4 KYB/vendor onboard | 4 | 5 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 2 | **3.3** |
| 5 Credential verify | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | **3.5** |
| 6 Doc authenticity | 4 | 3 | 4 | 5 | 3 | 5 | 4 | 4 | 3 | 4 | **3.9** |
| 7 Contract review | 4 | 4 | 4 | 3 | 1 | 3 | 3 | 4 | 4 | 1 | **3.0** |
| 8 Freelance escrow | 4 | 3 | 3 | 4 | 2 | 2 | 2 | 1 | 2 | 2 | **2.5** |
| 9 Construction pay | 5 | 4 | 4 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | **3.1** |
| 10 Supply provenance | 3 | 3 | 4 | 3 | 3 | 2 | 1 | 2 | 2 | 2 | **2.5** |
| 11 Trade docs | 3 | 3 | 4 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | **2.3** |
| 12 ESG verification | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 3 | 3 | 4 | **3.5** |
| 13 Healthcare prior-auth | 5 | 5 | 4 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | **3.0** |
| 14 Real estate docs | 4 | 4 | 4 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | **2.7** |
| 15 Diploma verify | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | **3.4** |
| 16 Insurance claims | 4 | 4 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **2.6** |
| 17 Creator brand-deals | 3 | 2 | 3 | 4 | 3 | 3 | 2 | 2 | 2 | 3 | **2.7** |
| 18 Gov/procurement | 4 | 4 | 4 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | **2.8** |

### Why these scores (key reasoning)

- **SME finance (1, 2, 3)** scored *down* despite strong pain: Cluster A evidence (file 03) shows brutally crowded markets, incumbents (Ramp, Wise, Xero) giving the feature away or absorbing it natively, and **blockchain adding zero**. Strong pain ≠ good business when the wedge is gone.
- **Doc authenticity (6)** scores highest: it is the **purest fit for the founder's skills** (hash-anchoring/proof-of-existence is genuinely a blockchain-shaped problem), has the **smallest possible MVP** (hash a file, anchor it, verify it), low regulatory risk, and a **"why now" that is accelerating fast** — AI-generated fake documents/certificates are exploding. Trust barrier is the open question.
- **Verification cluster (4, 5, 6, 12, 15)** dominates the top because verification/audit-trail problems are where blockchain *and* AI both add real value, and where the founder's skills are a true edge — not a forced fit.
- **Smart-contract escrow (8), trade/supply (10, 11)** scored *down*: money-transmitter regulation (escrow) and multi-party coordination failure (the TradeLens/We.Trade graveyard) are structural killers for a solo founder, regardless of pain.
- **Healthcare prior-auth (13)** has monster pain and WTP but is US-centric, slow-selling, and regulation-heavy — wrong shape for a solo first venture.

## Top 5 passed to Painpoint Discovery (Stage 2)

Ranked by composite, biased toward founder-fit and speed-to-revenue:

1. **#6 — Document authenticity / tamper-proof proof-of-existence & verification** (composite 3.9) — *the standout for this founder.*
2. **#5 — Credential / reference / employment verification** (3.5) — adjacent, larger buyers, AI + verifiable-credential fit.
3. **#12 — ESG / sustainability-claim verification & anti-greenwashing audit trail** (3.5) — strong "why now" (CSRD), blue-ocean, real audit-trail value.
4. **#4 — Vendor onboarding / KYB & supplier compliance** (3.3) — highest WTP, clear budget owners, but more crowded.
5. **#15 — Academic/professional credential (diploma) verification** (3.4) — narrow, founder-fit, but slower institutional sales.

> Candidates #5, #6, #15 cluster tightly — they are variations of one meta-opportunity: **"trusted, instantly-verifiable records in a world where AI makes forgery trivial."** Stage 2 will sharpen each into a precise pain statement and test whether they collapse into one beachhead. The losing 13 are parked (not deleted) in case Stage 4 forces a pivot.
