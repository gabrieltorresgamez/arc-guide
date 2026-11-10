---
title: 'ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-Off Points'
slug: atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
category: evaluation
kind: concept
summary: 'An ATAM review produces findings: risks, non-risks, sensitivity points and trade-off points.
  They come from analyzing architectural approaches against the highest-priority scenarios. Risks are
  then grouped into themes tied to business drivers.'
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-non-risk
- sensitivity-point
- trade-off-point
- atam-results
- advantages-and-drawbacks-of-atam
- lightweight-atam
- quality-attribute-scenario
checks:
- Risks found in an evaluation are listed in the risks section, ordered by priority, with suggested mitigation
  measures.
- Individual risks are grouped into risk themes, and each theme names the business driver it threatens.
- Findings trace back to high-priority, voted scenarios from the utility tree.
- The review output also lists non-risks, not only risks.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-11/
  title: 11 - Risks and technical debt | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/11-3/
  title: 'Tip 11-3: Identify problems or risks by qualitative evaluation! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How ATAM findings arise and where they go
review:
  status: generated
  flags: []
---

## Explanation

An ATAM (Architecture Tradeoff Analysis Method, see the article on it) is a structured review of an architecture. Its findings fall into a few named kinds.

**Where findings come from.** The review starts from business drivers. These are refined into scenarios, together with the architectural decisions that support each one. The review examines the architectural approaches linked to the high-priority factors from the utility tree. In that step, the team identifies risks, sensitivity points and trade-off points. Stakeholders then vote to prioritize a larger set of scenarios, and the analysis is repeated using the top-ranked ones.

**The kinds of findings.**
- **Risks** are concerns the review identifies in the architecture. They are listed as an output.
- **Non-risks** are also listed as an output (see ATAM Non-Risk).
- **Sensitivity points** and **trade-off points** are identified in the same analysis step. The articles Sensitivity Point and Trade-off Point define them.

**Risk themes.** At the end of the review, the team groups the individual risks into risk themes. Each theme shows how a set of risks threatens a business driver.

**Where findings go next.** arc42 section 11 holds a list of technical risks and debts, ordered by priority. Each entry can also suggest what to do: lower, mitigate or avoid the risk, or pay down the debt. arc42 also tags its tip on qualitative evaluation for finding risks with #atam. It recommends quality scenarios for that evaluation.

## Example

A team reviews an online shop. One top-rated scenario, chosen by stakeholder vote, concerns a sales peak. The review examines the approach chosen for that scenario. It records what it finds as risks, non-risks, sensitivity points or trade-off points. At the end, the team groups several risks into one theme, such as "peak sales may be lost". It links the theme to the business driver of revenue. 

## Trade-offs

See Advantages and Drawbacks of ATAM, and the article on lightweight ATAM, for how the method compares with lighter reviews.
