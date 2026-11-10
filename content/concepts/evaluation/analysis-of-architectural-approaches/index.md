---
title: Analysis of Architectural Approaches
slug: analysis-of-architectural-approaches
category: evaluation
kind: method
summary: Analysis of architectural approaches is the ATAM step where evaluators examine how design decisions
  handle important scenarios. It produces risks, non-risks, sensitivity points and tradeoff points. A
  second pass repeats it with stakeholder-ranked scenarios.
arc42:
- 10
- 11
- 9
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- sensitivity-point
- trade-off-point
- atam-non-risk
- utility-tree
- atam-phase-1-architecture-centric-analysis
- voting
checks:
- 'Evaluation findings are recorded in four categories: risks, non-risks, sensitivity points and tradeoff
  points.'
- Each documented risk names a specific architectural decision and its possible negative consequences.
- Each sensitivity point names a design decision and the quality-attribute scenario it affects.
- The stakeholder-ranked scenarios are used as test cases to confirm the earlier analysis.
- Additional approaches and findings uncovered during the analysis are documented.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2506.00150
  title: Supporting architecture evaluation for ATAM scenarios with LLMs
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Where the analysis of approaches is applied and repeated.
review:
  status: generated
  flags: []
---

## Explanation

ATAM is the Architecture Tradeoff Analysis Method. See *Architecture Tradeoff Analysis Method (ATAM)* for the full picture. Step 6, "Analyze Architectural Approaches," is where evaluators look closely at the architecture. They identify architectural risks, sensitivity points and tradeoff points.

**What the step produces**

The analysis of scenarios and design decisions yields four kinds of findings:

- **Risks.** A risk is a problematic architectural decision that can lead to negative consequences.
- **Non-risks.** See *ATAM Non-Risk*.
- **Sensitivity points.** A sensitivity point is a design decision that affects how well a particular quality-attribute scenario is achieved. See *Sensitivity Point*.
- **Tradeoff points.** See *Trade-off Point*.

*ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points* covers these four in more detail.

**The second pass**

Step 8 repeats the work of Step 6. This time it uses the highly ranked scenarios from Step 7, which stakeholders prioritized. These scenarios serve as test cases. They confirm the analysis done so far.

**New discoveries**

The analysis can reveal further architectural approaches. It can also reveal more risks, sensitivity points and tradeoff points. The team documents all of them.

## Example

A team takes one high-priority scenario and traces how the design handles it. They find one decision that could lead to negative consequences and record it as a risk. They find another decision that affects how well the scenario is met and record it as a sensitivity point. Later, stakeholders rank a set of scenarios. The team runs the same analysis on the top-ranked ones, using them as test cases for the earlier findings.
