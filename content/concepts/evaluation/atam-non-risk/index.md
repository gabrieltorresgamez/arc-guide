---
title: ATAM Non-Risk
slug: atam-non-risk
category: evaluation
kind: concept
summary: A non-risk is a decision that an ATAM evaluation team analyzed and found sound for a specific
  quality goal. The team records it with its reasoning, next to the risks it finds.
arc42:
- 9
- 10
- 11
step: s11-evaluate
related:
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- architecture-tradeoff-analysis-method-atam
- atam-results
- sensitivity-point
- trade-off-point
- quality-attribute-scenario
- architectural-decision
- arc42-quality-chapter
checks:
- Each documented non-risk names a quality attribute or scenario, a specific architectural decision, and
  a justification.
- Every non-risk traces to an area the evaluation team actually analyzed, not to an unexamined area.
- The evaluation report lists non-risks next to risks, sensitivity points and trade-off points, organized
  by quality attribute.
- Non-risks are judged against prioritized scenarios, for example those from the utility tree.
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
diagrams:
- file: diagram-1.mmd
  caption: Analysis of a decision against a scenario can yield a non-risk, documented with attribute,
    decision and justification.
review:
  status: generated
  flags: []
---

## Explanation

ATAM is the Architecture Tradeoff Analysis Method (see the article on it). The team checks quality scenarios against architectural decisions. This analysis produces four kinds of findings: risks, non-risks, sensitivity points and trade-off points.

A **non-risk** is the good-news finding. The team looked at a decision and judged it well-reasoned for the quality scenarios, given stakeholder priorities and constraints.

**Documentation.** A non-risk needs the same evidence as a risk. Write down three things:

- the quality attribute (or its scenario),
- the architectural decision,
- the justification that the decision is adequate.

**It needs real analysis.** If the team did not examine an area, that area is not a non-risk. It is simply unexamined.

**Where the scenarios come from.** The utility tree is a prioritized, layered model of the driving requirements. It refines quality factors down to scenarios with stimuli and responses. The analysis judges decisions against these scenarios and finds risks or non-risks.

**In the results.** The SEI lists non-risks among the ATAM outputs, next to risks. The final report's catalog lists all four finding types, organized by quality attribute. Risks are then grouped into risk themes. These show which business driver each risk threatens. In the SEI description, non-risks are not part of that grouping.

**Why record them.** Non-risks give stakeholders evidence that the architecture is sound in the areas examined. They also give a baseline for later change.

**Link to arc42.** arc42 advises using quality scenarios to analyze or evaluate an architecture, and it tags this advice with ATAM. That ties its quality requirements section to ATAM-style evaluation.

## Example

A team evaluates a web shop. One scenario says: during a sale, order requests triple and orders must still be accepted. The team examines the decision to queue incoming orders and process them in the background. It finds the reasoning sound for this scenario. It records a non-risk with three parts: the quality attribute (performance under load), the decision (queue orders), and the justification (the queue absorbs bursts, so order intake does not wait for processing). A different area, such as backups, was never examined. The team records nothing about it as a non-risk.

## Trade-offs

Writing non-risks takes effort, because each one needs a scenario, a decision and evidence. A non-risk holds only for the scenarios and priorities that were analyzed. Areas the team did not examine have no verdict at all, so a list of non-risks does not prove the whole architecture is sound.
