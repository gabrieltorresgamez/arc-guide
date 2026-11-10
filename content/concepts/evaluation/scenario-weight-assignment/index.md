---
title: Scenario Weight Assignment and Prioritization
slug: scenario-weight-assignment
category: evaluation
kind: method
summary: Stakeholders brainstorm many scenarios, then vote to rank them. In ATAM and the Quality Attribute
  Workshop, the voting involves the stakeholder group.
arc42:
- 10
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- voting
- quality-attribute-scenario
- quality-attribute-prioritization
- stakeholder
- software-architecture-evaluation
- atam-phase-1-and-2-activities
checks:
- The scenario set was brainstormed with the entire stakeholder group.
- The whole stakeholder group voted to prioritize the scenarios.
- Each architectural driver is covered by at least one scenario.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/quality-attribute-workshop-collection/
  title: Quality Attribute Workshop Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: From brainstorming to a ranked scenario list.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Scenarios are gathered from stakeholders and then prioritized through voting.

**Collecting scenarios.** In step 7 of the Architecture Tradeoff Analysis Method (ATAM), a larger set of scenarios is elicited from the entire stakeholder group. This is whole-group brainstorming. See the article "Architecture Tradeoff Analysis Method (ATAM)" for the full method.

**Prioritizing by voting.** ATAM then prioritizes the brainstormed set through a voting process. The entire stakeholder group takes part, not only a few people.

**The same idea in another method.** The Quality Attribute Workshop (QAW) works in a similar way. Stakeholders generate scenarios. Facilitators ensure that at least one scenario addresses each architectural driver. Stakeholders then prioritize the scenarios by voting.

This article covers brainstorming and voting only, not how votes are scored or combined.

## Example

A team building an online shop runs a workshop. Stakeholders from sales, operations, and support suggest scenarios. One says "the payment provider goes down during a sale." Another says "we add a new shipping partner." After brainstorming, everyone votes. The scenarios that receive the most votes are the ones the team looks at first.

## Trade-offs

The sources describe the whole stakeholder group taking part in the voting.
