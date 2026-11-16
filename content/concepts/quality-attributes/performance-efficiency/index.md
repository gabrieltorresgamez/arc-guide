---
title: Performance Efficiency
slug: performance-efficiency
order: 20
category: quality-attributes
kind: quality-attribute
summary: Performance efficiency is a workload's ability to handle rising load without hurting user experience,
  and to use fewer resources when demand is low. Teams should consider it from the start and verify it
  by measuring.
arc42:
- 10
- 4
- 1
step: s04-quality-requirements
related:
- flexibility
- performance-efficiency-tactic
- iso-iec-25010-product-quality-model
- quality-attribute
- quality-attribute-trade-off
- arc42-quality-requirements
checks:
- Performance targets for key flows are stated as acceptable user-experience effects and agreed with business
  stakeholders.
- The document says how performance is measured and how the acceptable threshold was agreed.
- Production monitoring covers business transactions and technical metrics such as CPU, latency and requests
  per second, with real and synthetic transactions.
- Capacity limits are stated and checked against requirements.
- Performance work is planned from the start and refined during development.
sources:
- url: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/principles
  title: Performance Efficiency design principles - Microsoft Azure Well-Architected Framework | Microsoft
    Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/qualities/time-behaviour
  title: "Time behaviour | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/resource-utilization
  title: "Resource utilization | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/capacity
  title: "Capacity | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/efficient-generation-of-test-data
  title: "Efficient generation of test data"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/query-execution-management
  title: "Low-overhead query execution measurement"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/fast-shutdown-time
  title: "Fast shutdown time (less than 10 sec)"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/performance-efficiency
  title: "Performance efficiency | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Performance efficiency describes how well a workload adapts to changing demand. When load rises, it scales up so users do not notice a slowdown. When demand drops, it scales down to save resources.

**Capacity is one part of it.** Capacity is how well the maximum limits of a product or system parameter meet the requirements. In plain terms: do the system's upper limits cover what the business needs?

**Start early, even without numbers.** Performance should be a core concern from the beginning, not an afterthought. This holds even when no strict targets exist yet. Teams then test and refine throughout development.

**Set targets with the business.** Targets should not be purely technical. Agree with business stakeholders what user-experience effect is acceptable for the key flows.

**Targets and measurements depend on each other.** You cannot measure what you have not defined, and you cannot define a target without measuring. So teams measure the workload until the group agrees on an acceptable threshold.

**Keep watching in production.** Track end-to-end business transactions and technical metrics such as CPU, latency and requests per second. Use both real and synthetic transactions.

Related articles: Flexibility, Performance Efficiency Tactic and ISO/IEC 25010 Product Quality Model.

**Tactics.** See the article Performance Efficiency Tactic.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Time behaviour** means that response times and throughput rates, while the product performs its functions, meet the requirements. More: [arc42 quality model](https://quality.arc42.org/qualities/time-behaviour).
- **Resource utilization** means that the amounts and types of resources the product uses while performing its functions meet the requirements. More: [arc42 quality model](https://quality.arc42.org/qualities/resource-utilization).
- **Capacity** means that the maximum limits of a product or system parameter meet the requirements. More: [arc42 quality model](https://quality.arc42.org/qualities/capacity).

**In the arc42 quality model.** The arc42 quality model has its own page on [Performance efficiency](https://quality.arc42.org/qualities/performance-efficiency).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [Efficient generation of test data](https://quality.arc42.org/requirements/efficient-generation-of-test-data), [Low-overhead query execution measurement](https://quality.arc42.org/requirements/query-execution-management), [Fast shutdown time (less than 10 sec)](https://quality.arc42.org/requirements/fast-shutdown-time).

## Example

An online shop names "checkout" as a key flow. Together with the business, the team agrees how long a customer may wait before the delay becomes unacceptable. No measurements exist yet, so the team runs checkout under test load, records the results and adjusts the target until everyone accepts it. After launch, a synthetic purchase runs regularly. Dashboards show CPU use, latency and requests per second next to real orders.

## Trade-offs

Fine-grained performance tuning has costs in other qualities. Early work should therefore look at the whole system instead of fine-tuning single components. Defining targets also takes iteration, because targets and measurements depend on each other.
