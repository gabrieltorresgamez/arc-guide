---
title: ATAM Results
slug: atam-results
category: evaluation
kind: artifact
summary: 'ATAM results are what an evaluation team hands to stakeholders at the end: documented architecture
  risks, plus risk themes showing which business goals those risks threaten.'
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- sensitivity-point
- trade-off-point
- atam-phase-1-and-2-activities
- software-architecture-evaluation
- architectural-approach-identification
- advantages-and-drawbacks-of-atam
checks:
- Identified risks are grouped into risk themes, and each theme names the business driver it threatens.
- The results record risks, sensitivity points and tradeoff points found during approach analysis.
- The business drivers are documented alongside the architecture presentation.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How ATAM findings lead to the presented results.
review:
  status: generated
  flags: []
---

## Explanation

An ATAM evaluation (see Architecture Tradeoff Analysis Method (ATAM)) looks for architectural risks that could stand in the way of business goals. Its results are the documented outcome of that search.

**Where the results come from**

The evaluation starts by collecting the business drivers and the architecture from project decision-makers. The architect then presents the architecture and explains how it meets those drivers. The architect also names the architectural approaches. At this point they are only named, not analyzed.

**What the analysis produces**

When the approaches are analyzed, the team identifies three kinds of findings:

- risks,
- sensitivity points,
- tradeoff points.

ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points explains these.

**Risk themes**

The team then groups the risks into risk themes. Each theme shows which business driver the risks behind it threaten. This ties technical findings back to business goals.

**Presenting the results**

The last step, step 9, presents the results. All documentation goes to the stakeholders. The steps fall into two phases. Phase 2 covers steps 7 to 9 and ends the evaluation.

One source adds that the analysis can be turned into risk themes and their impacts. The process can then be repeated.

## Example

A team evaluates an online shop. The business drivers are fast checkout and low downtime. The architect presents the design and names a few approaches. During analysis the team records a risk: one shared payment component could slow checkout under load. It groups this with similar findings into a theme, "checkout speed is at risk." In the last step, the team gives stakeholders all the documentation, including that theme and the driver it threatens.
