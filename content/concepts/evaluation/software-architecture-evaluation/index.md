---
title: Software Architecture Evaluation
slug: software-architecture-evaluation
category: evaluation
kind: practice
summary: Architecture evaluation examines a design for problems and risks before teams build on it. Its
  findings are qualitative, and it works best when done early.
arc42:
- 11
- 10
- 9
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- lightweight-atam
- advantages-and-drawbacks-of-atam
- sensitivity-point
- trade-off-point
- quality-attribute-scenario
- software-architecture-analysis-method-saam
- risk-identification
checks:
- The document states when the architecture was evaluated and whether the evaluation worked from models
  or from code.
- The evaluation records identified risks, sensitivity points and trade-off points.
- The evaluation does not rely on metrics alone to judge whether quality goals are met.
sources:
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8838159/
  title: 'Lightweight Software Architecture Evaluation for Industry: A Comprehensive Review - PMC'
  site: pmc.ncbi.nlm.nih.gov
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/softwarearch-assessment/
  title: Trust is good, Control is better - Software Architecture Assessment - InfoQ
  site: infoq.com
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

Architecture evaluation means examining a software design to find problems and risks. The aim is to find them before development starts (see Software Architecture).

**What it finds**

Methods such as the Architecture Tradeoff Analysis Method (ATAM) expose risks that could keep an organization from reaching its business goals. ATAM also names sensitivity points and trade-off points. A sensitivity point is a place in the architecture that affects one quality attribute. A trade-off point affects more than one quality attribute. See the articles on ATAM, Sensitivity Point and Trade-off Point.

**Early and late evaluation**

- Methods differ in the development stage where they fit best, early or late. Some metrics-based approaches compare the actual architecture with the planned one.

Teams often start reviews too late. Then finding problems and refactoring gets harder.

**Techniques**

- Experience-based evaluation is the technique most practiced in industry.
- Scenario-based evaluation builds on scenarios. A scenario is a short description of how a stakeholder interacts with the system.
- Mathematical-model methods, such as Software Performance Engineering, and simulation are tied to performance, and the two can be mixed.

**Qualitative and metrics-based assessment**

Qualitative methods involve many stakeholders. They work breadth-first, which means they cover the key aspects of the architecture first. Quantitative assessments, such as prototypes, simulations and code quality tools, cover only partial aspects of a system. For example, a metrics tool can find dependency cycles. It cannot show how an architecture decision affects a quality attribute.

**Cost and adoption**

Full-scale methods, ATAM in particular, are heavyweight. They need a lot of effort and cost. Evaluation is beneficial, yet industry does not apply it widely. See Lightweight ATAM for a lighter option.

## Example

A team plans an online ticket shop. Before coding, they gather stakeholders and walk through scenarios, such as a sales rush for a popular event. They review the design against each scenario. They note risks and the places where two quality goals compete. They change the design on paper, which is cheaper than changing finished code.

## Trade-offs

Full-scale methods such as ATAM cost a lot of effort. This may explain why evaluation is not widely used in industry. Quantitative assessments cover only partial aspects of a system, and a code quality tool cannot show a decision's effect on quality attributes. Waiting until late makes problems harder to detect and fix.
