---
title: Placing ATAM Evaluation in arc42
slug: placing-atam-evaluation-in-arc42
category: evaluation
kind: practice
summary: arc42 section 11 normally lists risks and technical debt. An ATAM-based variant replaces it with
  an evaluation section that records the risks, sensitivity points and trade-off points found during an
  ATAM evaluation.
arc42:
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- atam-results
- sensitivity-point
- trade-off-point
- atam-non-risk
- technical-debt
- arc42-quality-chapter
checks:
- Section 11 is titled as an ATAM evaluation, and its subsections separate risks, sensitivity points and
  trade-off points.
- Each risk finding is tied to a business driver or quality goal, for example through a risk theme.
- Findings name the stakeholders who were involved in identifying them.
- The document states where technical debt is recorded if section 11 no longer holds it.
sources:
- url: https://docs.arc42.org/section-11/
  title: 11 - Risks and technical debt | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

In the standard arc42 template, section 11 is called "Risks and technical debt". It holds a list of technical risks and debts, ordered by priority, with measures to reduce them.

This variant swaps that section for an evaluation section based on ATAM. ATAM is the Architecture Tradeoff Analysis Method. It is explained in the article "Architecture Tradeoff Analysis Method (ATAM)".

**Why the swap makes sense**

- ATAM exposes architectural risks that could stop an organization from reaching its business goals. A section that records risks is a natural home for its results.
- In one ATAM step, the team identifies risks, sensitivity points and trade-off points together. So the evaluation section can have one subsection for each: 11.1 for risks, 11.3 for sensitivity points and 11.4 for trade-off points.
- ATAM also groups individual risks into risk themes. Each theme shows how risks threaten one business driver. Recording the theme next to a finding shows which business driver the related risks threaten.

**Traceability to people**

The arc42 tips for section 11 say to look for problems and risks together with different stakeholders. In the evaluation section, you can note which stakeholders raised or care about each finding.

**What to decide before replacing**

Standard section 11 holds technical debt as well as risks. If you replace it, you must decide where the debt list goes. This article does not prescribe a place.

For definitions of the finding types, see the related article on ATAM findings.

## Example

A team documents an online shop. After an ATAM evaluation, section 11 is titled "Evaluation with ATAM". Subsection 11.1 lists a risk. It is grouped under a risk theme that names the business driver it threatens. A note beside it names the stakeholders who raised it. Subsection 11.3 lists a sensitivity point and 11.4 lists a trade-off point. The team keeps its list of technical debt in a separate place and says so in the section.

## Trade-offs

Replacing section 11 gives ATAM findings a clear home and keeps them together. The cost is that the standard risks and technical debt list no longer has a place in that section. You must then place the debt list elsewhere, or you risk losing it.
