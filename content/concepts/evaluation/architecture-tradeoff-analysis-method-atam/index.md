---
title: Architecture Tradeoff Analysis Method (ATAM)
slug: architecture-tradeoff-analysis-method-atam
category: evaluation
kind: method
summary: ATAM is a method for checking a software architecture against its quality goals. It shows how
  those goals pull against each other and exposes risks that could block business goals.
arc42:
- 10
- 11
step: s11-evaluate
related:
- advantages-and-drawbacks-of-atam
- lightweight-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- atam-application-phases
- software-architecture-evaluation
- sensitivity-point
- trade-off-point
- software-architecture-analysis-method-saam
checks:
- The architecture documentation records an evaluation of the architecture against its quality attribute
  goals.
- The documented evaluation lists the architectural risks found and states which business goals they could
  threaten.
- Sensitivity points and trade-off points found during the analysis are recorded.
- A utility tree of the driving architectural requirements is included or referenced.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8838159/
  title: 'Lightweight Software Architecture Evaluation for Industry: A Comprehensive Review - PMC'
  site: pmc.ncbi.nlm.nih.gov
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Architecture Tradeoff Analysis Method (ATAM) was developed at the Software Engineering Institute at Carnegie Mellon University. It evaluates a software architecture against its quality attribute goals. These are goals such as performance or security (see the article Quality Attribute). The method also shows how those goals interact.

The aim is to expose architectural risks. These are weaknesses that could keep an organization from reaching its business goals.

**How it runs**

ATAM formally has nine steps. Phase 1 covers steps 1 to 6. Phase 2 covers steps 7 to 9 and finishes the evaluation. Step 5 builds a utility tree. This is a hierarchic model of the requirements that drive the architecture.

**What it produces**

- Risks and non-risks.
- Sensitivity points and trade-off points, found while the team analyzes the architectural approaches. See the articles Sensitivity Point and Trade-off Point.
- Risk themes. ATAM groups individual risks into themes. Each theme shows how it threatens a business driver.
- The utility tree itself.

For details on these findings, see ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points.

**When it pays off**

ATAM is most valuable early in the life cycle. The cost of changing the architecture is minimal at that stage.

## Example

A team plans an online ticket shop. Fast checkout and strong data protection are both top goals. During the evaluation, the group finds that encrypting every request slows checkout. That is a trade-off point. The group also finds that checkout depends on one payment service with no fallback. That is a risk. The team records both and links the risk to the business goal of steady sales.

## Trade-offs

ATAM is costly. A 2022 review says comprehensive methods, ATAM in particular, need a great deal of cost and effort. The method is scenario-based and involves many stakeholders. Its prioritization uses cumulative voting.

Lightweight variants reduce cost by minimizing documentation, formality and the number of stakeholders involved. See Lightweight ATAM and Advantages and Drawbacks of ATAM.
