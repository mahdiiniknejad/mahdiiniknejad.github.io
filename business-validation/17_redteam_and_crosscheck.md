# 17 — Red-Team & AI-vs-AI Cross-Checker

Two adversarial reviews of the #1 pick ("Recover"), then the PM's reconciliation.

---

## PART A — Red-Team Memo (attack to kill)

**Mandate:** assume the idea is bad. Find the fatal flaws.

1. **Why won't customers buy?** Owners are busy, skeptical of "another AI tool," and afraid an AI will message *their* customers badly. Many believe their front desk "already does this." Latent pain = no urgency.
2. **Why is the pain weaker than it looks?** The dollar magnitudes are **vendor-sourced** (file 16). Real recoverable revenue per shop may be far lower than $1M-style figures — much "lost" revenue is genuinely dead (customers gone, declined for real reasons). **If recovery rates are low, contingency doesn't pay and the business has no engine.**
3. **Why will competitors win?** This is **a feature, not a moat.** Weave, Podium, RevenueWell, and especially the PMS/POS vendors (who own the data) can bolt on "AI recovery." Incumbents have distribution; the founder has none.
4. **Why is the market smaller than claimed?** TAM numbers are directional/inflated (file 16). The *serviceable* set (owners who'll adopt + integrate + pay) is much smaller, and fragmented across verticals each needing its own integration + playbook.
5. **Why is the MVP harder than expected?** Concierge is **labor-heavy** and doesn't scale; automating it well (per-PMS integration, message quality, deliverability, opt-out handling) is real engineering. Solo founder time is the bottleneck.
6. **Why is trust harder than expected?** Letting an AI text a business's customers is a high-trust ask. One bad/spammy message → owner churns + reputational damage. Human-in-the-loop slows scaling.
7. **Why is regulation dangerous?** **TCPA** (SMS consent) is a real liability in the US — texting lapsed customers without consent invites fines. **HIPAA** if dental. Consent provenance must be airtight.
8. **Why is acquisition too expensive?** Founder-led works for 10 accounts; scaling past that needs paid acquisition into fragmented SMB verticals with low LTV-per-account — CAC could swamp contribution.
9. **Why might AI add no real value?** If owners insist on approving every message anyway, the AI is just a drafting assist — thin. The hard part (which customers are recoverable, what to say) may need human judgement the AI can't reliably replace.
10. **Hidden assumption that could destroy it:** *That a contingency-priced concierge can be automated into a high-margin product without the recovery rate collapsing or the trust/compliance burden exploding.* If automation degrades recovery quality, the unit economics invert.

**Red-Team decision: REVISE (not kill).** The pain is real and the concierge test is nearly free, so it's worth testing — **but the plan must not assume success; it must measure recovery rate, attribution, and trust/compliance before any build.** Defensibility is genuinely weak; the founder is betting on a head-start + vertical depth, not a moat.

---

## PART B — AI-vs-AI Cross-Checker (independent review)

**Mandate:** don't trust the prior agents. Re-check.

1. **Does evidence support the conclusion?** *Partly.* Pain universality: yes. Recoverable-magnitude: **not primary-verified** (vendor sources). Conclusion should be "validate," not "build." ✔ matches file 13.
2. **Sources reliable?** Mixed — frequencies solid, magnitudes vendor-biased (file 16). ✔ flagged.
3. **Market-size realistic?** The TAM numbers are not reliable; the **SOM ($120–300k y1 solo)** is plausible and is the only number that should drive decisions. ✔
4. **Competitors fairly analysed?** Mostly, but the report **under-weights the PMS/POS-vendor threat** (they own the data and the customer). Raise this risk.
5. **WTP proven or guessed?** *Proven structure* (contingency/RCM/ISAs exist); *unproven rate* (will the math work?). Honest.
6. **Founder advantage real?** Yes for AI/speed; **the report is correctly honest that Solidity is unused.** Good — no over-claim.
7. **MVP buildable?** Concierge: trivially. Product: medium — don't underestimate per-PMS integration + deliverability.
8. **Revenue model realistic?** Yes, *if* recovery rates hold. That's the load-bearing if.
9. **Hallucination check?** No fabricated competitors/sources detected; the main flagged issue is **reliance on vendor magnitudes**, already disclosed.
10. **Final recommendation too optimistic?** The *ranking* is fine; the *readiness* must be **VALIDATION READY, not BUILD READY.**

**Cross-Checker revised scores vs. Judge:** lower "blue-ocean" (3→3), lower "defensibility" (keep 3), and **explicitly gate to validation-first.** Adds one risk the Judge under-weighted: **PMS/POS incumbents owning the data/customer.**

**Cross-Checker final recommendation:** **Agree with #1 pick; disagree with any "build now" framing.** Proceed to paid concierge pilots; let the data choose the beachhead and confirm the economics.

---

## PART C — PM reconciliation (required when Cross-Checker disagrees with Judge)

The Cross-Checker did **not** dispute the #1 *ranking*; it disputed *readiness* and flagged the PMS-vendor threat. The PM reconciles as follows:

- **Accept:** Final status is **VALIDATION READY, NOT BUILD READY** (file 20). The 30-day plan (file 15) is validation-only by design — already aligned.
- **Accept:** Add **"PMS/POS vendor bolts on AI recovery"** as a top-tier risk and assumption (file 18). Mitigation: go vertical + outcome-priced + relationship-led where incumbents are slow; consider *partnering with* a PMS as a channel rather than fighting it.
- **Accept:** Treat all recoverable-$ magnitudes as **hypotheses measured in pilots**, not facts.
- **No conflict on the pick.** #1 stands: **Recover**, with N7 (collections) as the designated pivot if attribution/recovery-rate fails.

**Reconciled outcome:** Proceed to validation. The reconciliation *strengthens* the plan by making the kill-thresholds (file 18) the real deliverable.
