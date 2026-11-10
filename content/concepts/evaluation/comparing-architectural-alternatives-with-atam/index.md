---
title: Comparing Architectural Alternatives with ATAM
slug: comparing-architectural-alternatives-with-atam
category: evaluation
kind: method
summary: To compare candidate architectures with ATAM, judge each against the same requirements and scenarios.
  Tally the risks, sensitivity points and trade-off points per draft. Then weigh them by business impact,
  not by count alone.
arc42:
- 4
- 9
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- advantages-and-drawbacks-of-atam
- lightweight-atam
- scenario-weight-assignment
- quality-attribute-scenario
- sensitivity-point
- trade-off-point
checks:
- Every candidate architecture is evaluated against the same utility tree.
- Risks, sensitivity points and trade-off points are listed separately for each alternative.
- Risks are summarized as themes that name the business driver they threaten.
- Quality scenarios are documented in a table with quality goal, scenario, solution approach and risk.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/10-8/
  title: 'Tip 10-8: Use (quality) scenarios for architecture analysis or evaluation! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ATAM is a method for evaluating a software architecture against quality goals (see Architecture Tradeoff Analysis Method (ATAM)).

**Keep the basis identical.** Build one utility tree. This is a hierarchic model of the driving architectural requirements.

**Tally the findings per draft.** When ATAM analyzes the architectural approaches, it identifies risks, sensitivity points and trade-off points. See ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points. Record these per alternative, so you can set the lists side by side.

**Judge severity, not only counts.** ATAM combines risks into risk themes. Each theme shows how risks threaten a business driver. Use the themes to judge by business impact.

**Record scenarios in a table.** arc42 recommends using quality scenarios to evaluate an architecture, and it names ATAM. It suggests a table with quality goal, scenario, solution approach and risk. Such a table can support qualitative evaluation.

## Example

A team weighs two drafts for an online ordering system. Both are checked against the same utility tree and the same scenarios.

Draft A shows two risks and one trade-off point. Draft B shows one risk and three trade-off points. The team does not just count. It checks which risk themes touch the business drivers. If Draft B's single risk threatens the most important driver, Draft A may still be the better choice.

## Trade-offs

Risk themes tied to business drivers show how the risks threaten what the business needs.
