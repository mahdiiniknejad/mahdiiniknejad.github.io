# 19 — CTO Handoff Pack (conditional)

**Status:** This pack is **conditional** — it is only to be acted on **after** the 30-day validation gate (file 20) returns BUILD READY (≥2 paid pilots with economics that work). Until then, **build nothing.** It is included so the founder/CTO can see the shape of the product the validation is pointing toward.

1. **Product thesis.** AI agent that connects to a service business's system-of-record, identifies recoverable revenue events (declined estimates, unscheduled treatment, no-shows, lapsed customers), and runs persistent, personalised, human-approved recovery outreach; priced on outcomes.
2. **Target customer.** Owner-led high-ticket service SMB (beachhead chosen in validation: auto repair / optometry / aesthetic).
3. **User problem.** Front desk never works the lost-revenue list → money leaks.
4. **Buyer problem.** Owner loses already-earned revenue and can't trust/justify hiring to fix it.
5. **MVP scope (post-validation).**
   - Ingest one vertical's lost-revenue data (CSV export first; one PMS API second).
   - Classify recoverable events; estimate recoverable $.
   - AI-draft personalised multi-touch sequences (SMS/email) in the owner's voice.
   - **Human-in-the-loop approval queue** (non-negotiable for trust).
   - Booking/reply handling; recovered-$ tracking & reporting; opt-out/consent management.
6. **Non-MVP (avoid).** Multi-vertical at once; voice calls; full PMS write-back; mobile app; marketplace; **anything blockchain.**
7. **Core user journey.** Connect/export → "you have $X recoverable" → review/approve AI sequences → AI sends & follows up → customer rebooks → recovered-$ dashboard → owner billed on success.
8. **Required features.** Data ingest; event classification; LLM drafting; approval queue; messaging + deliverability; opt-out/consent ledger; outcome attribution/reporting; billing.
9. **Optional features.** Auto-send (trusted accounts); A/B message testing; multi-location; PMS deep integration.
10. **Technical assumptions.** LLM API (use the latest, most capable models for drafting/classification); per-vertical data schemas; messaging provider with compliance features.
11. **Data requirements.** Customer contact + consent status; service/estimate history; appointment data. Minimise PII; encrypt; clear retention policy.
12. **AI requirements.** LLM for classification + personalised drafting + reply handling; guardrails (no spam, on-brand, opt-out aware); human-approval gate; eval harness on recovery quality.
13. **Blockchain / smart-contract requirements.** **NONE.** Explicitly not needed; do not add. (The founder's Solidity skill is not used in this product — confirmed across files 03/13/14/17.)
14. **Integrations.** Email/SMS (compliance-grade); per-vertical PMS/POS (Tekmetric, RevolutionEHR, etc.); calendar/booking; Stripe (billing).
15. **Security risks.** Customer PII; messaging on behalf of the business; credential storage for integrations. → encryption, least-privilege, audit log.
16. **Compliance risks.** **TCPA** (SMS consent) — top priority; **HIPAA** if dental (avoid first); CAN-SPAM; state privacy. → consent ledger, opt-out, human approval, BAAs where needed.
17. **Trust requirements.** Human-in-the-loop, "in your voice," opt-out, transparent recovered-$ reporting.
18. **Estimated build complexity.** MVP (one vertical, export-based, human-approved): **low-medium** (weeks for a capable founder). Productised (multi-PMS, auto-send, compliance): **medium**.
19. **Suggested tech stack options.** Lightweight: Next.js + a serverless backend + Postgres + an LLM API + a compliance-grade messaging API + Stripe. Keep it boring and shippable. (Supabase/Vercel-class tooling is fine.)
20. **First 30-day build plan (post-gate).** Wk1: ingest + classify one vertical's export. Wk2: LLM drafting + approval queue. Wk3: messaging + opt-out + reply handling. Wk4: recovered-$ tracking + billing; onboard the 2 pilot shops onto the tool.
21. **First validation experiment (post-build).** Migrate the 2 paid concierge pilots onto the software; confirm automated recovery rate ≥ manual rate.
22. **Success metrics.** Automated recovery rate ≥ manual; <X min owner approval time/week; recovered-$ ≥ contingency threshold; ≥1 pilot converts to SaaS+success.
23. **Kill metrics.** Automated recovery rate collapses vs. manual; compliance blocker in chosen vertical; owners won't approve/trust at acceptable effort.

**CTO note:** This is an **AI product with disciplined compliance**, not a blockchain product. If at any point someone proposes adding a chain "because the founder knows Solidity," the answer per this entire analysis is **no** — it adds cost and trust-friction without value here.
