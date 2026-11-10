---
title: Modifiability Scenario
slug: modifiability-scenario
category: quality-attributes
kind: concept
summary: A modifiability scenario turns a vague wish like "easy to change" into one concrete change request
  with a measurable limit, such as effort in person-weeks. You can then check whether the architecture
  meets it.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- modifiability
- quality-attribute-scenario
- modifiability-tactics
- arc42-quality-chapter
- architecture-tradeoff-analysis-method-atam
- smart-requirements
- design-for-change
checks:
- Each modifiability scenario describes one specific change, not a general wish to be easy to change.
- Each scenario has a measurable response measure, such as person-weeks or person-hours of effort.
- Each scenario names the stimulus, the system affected and the response.
- Portability needs, such as supported databases, are written as testable change scenarios.
- The scenarios are collected in a quality tree that serves as a checklist.
sources:
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/tips/10-6/
  title: 'Tip 10-6: Consider change (quality) scenarios!! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://dmccreary.github.io/atam/chapters/06-quality-attribute-scenarios/
  title: Quality Attribute Scenarios - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-10-2/
  title: 'Question C-10-2: What is a ''quality scenario''? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Many teams write "the system must be easy to change." Nobody can test that. A modifiability scenario fixes this. It describes one concrete change and states how much effort that change may take.

**Why scenarios help.** Quality scenarios make quality requirements concrete, so you can decide whether they are fulfilled. They must be specific and measurable. A change scenario describes the desired effect of modifying or extending the system. Change scenarios cover goals such as maintainability, modifiability, changeability and flexibility. The articles Modifiability and Quality Attribute Scenario cover the wider ideas.

**What a scenario contains.** A quality scenario names a stimulus (what happens to the system), the stimulated system, and a response. The response must be measurable in some fashion. For modifiability, the stimulus is a change request and the response is the change being carried out.

**The response measure.** The response measure is the quantitative criterion that decides whether the response is good enough. Without it, a scenario is only a wish. For change scenarios, effort is a common measure. Two examples:

- Integrating a new external payment provider takes at most two person-weeks.
- Adapting the data format of a yearly booking report to legal requirements takes at most 80 person-hours.

Another example sets a scope limit. A team adds a new payment method to checkout, the changes stay inside the payment module, and the work takes at most 5 developer-days.

**Portability as a change scenario.** A change scenario can also state a platform need. For example, the system must work with the databases DB2, Oracle and MySQL without source code modifications. Here the measure is "no source code changes."

**Collecting scenarios.** The term Quality Attribute Utility Tree (a "quality tree") comes from Bass et al. arc42 recommends using the quality tree as a checklist. See arc42 Quality Requirements for where scenarios live in the documentation.

## Example

A shop runs an online store. The team writes this scenario: *A product owner asks for a new delivery option at checkout. The team makes the change in the delivery module only. The work takes at most four person-days.* Later, the team estimates a planned change against this sentence. If the estimate is ten person-days, the architecture misses the goal. The team now has a concrete problem to discuss instead of a feeling that the system is hard to change.

## Trade-offs

Scenarios make requirements testable. This article does not say how to pick the numbers. A limit such as two person-weeks is a judgment the team must make. A scenario without a measure is only a wish, so skipping the measure removes the value.
