---
title: Insufficient ATAM Application
slug: insufficient-atam-application
category: evaluation
kind: concept
summary: An ATAM review is weak when its findings are not tied to specific architectural decisions, quality
  attributes and scenarios. Vague risks and unproven non-risks cannot be acted on or trusted.
arc42:
- 9
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- atam-non-risk
- sensitivity-point
- trade-off-point
- architectural-decision-records-as-evaluation-prerequisite
- quality-attribute-scenario
- advantages-and-drawbacks-of-atam
checks:
- Each risk names a specific architectural decision and a specific scenario it could make fail.
- Each non-risk names a scenario, a decision and evidence that the decision is adequate.
- Each sensitivity point names the decision and the quality attribute that reacts strongly to a small
  change.
- Each trade-off point names the quality attribute it helps and the one it harms.
- Quality requirements are written as specific, measurable scenarios.
sources:
- url: https://dmccreary.github.io/atam/chapters/10-risk-analysis-atam-reporting/
  title: Sensitivity, Tradeoffs, Risk Analysis, and ATAM Reporting - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Architecture Tradeoff Analysis Method (ATAM) exists to expose architectural risks. These are risks that may stop an organization from reaching its business goals. Individual risks are grouped into risk themes, and each theme shows which business driver it threatens.

The method builds a utility tree, a hierarchical model of the driving architectural requirements. In step 6, the team analyzes the highest-priority scenarios against the architecture. During this step it identifies risks, sensitivity points and trade-off points. The top-ranked scenarios then serve as test cases that confirm the analysis done so far.

**What goes wrong in an insufficient application**

Decisions are not linked to quality attributes and scenarios. The findings then float free of the architecture. Typical symptoms:

- **Vague risks.** A statement like "the architecture might have availability problems" names no decision and no scenario. Nobody can act on it.
- **Unproven non-risks.** A non-risk needs the same evidence as a risk: a scenario, a decision and evidence that the decision is adequate. Finding nothing wrong does not make a non-risk.
- **Weak sensitivity points.** A sensitivity point is a decision where a small change causes a disproportionately large change in a quality attribute. Without a named decision and a named quality, the claim cannot be shown.
- **Unnamed trade-offs.** A trade-off point is a decision that helps one quality attribute while harming another. It needs both qualities named.

**What a good application looks like**

A good risk is grounded in a specific scenario and a specific architectural decision. It has a credible chance of making that scenario fail. Non-risks get the same grounding, plus evidence of adequacy.

**Where this shows up in arc42**

arc42 asks for quality requirements written as specific, measurable scenarios. It recommends such scenarios for ATAM evaluation. Section 10 also introduces the quality (utility) tree. Section 9 asks that all consequences of a decision be listed.

## Example

Weak finding: "Risk: the system may be slow." No decision, no scenario.

Better finding: "Risk: decision ADR-7 (synchronous calls to the payment service) may make the scenario 'checkout completes within 2 seconds at peak load' fail. Quality attribute: performance."

Better non-risk: "Decision ADR-4 (replicated database) is adequate for the scenario 'a node fails and orders keep working'. Evidence: failover was tested and finished in time."

## Trade-offs

Tying every finding to a decision, a quality and a scenario takes effort. It needs scenarios that are specific. The payoff is that findings are credible and can be acted on, while vague findings cannot be acted on.
