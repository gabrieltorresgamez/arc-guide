---
title: BPMN Gateway
slug: bpmn-gateway-semantics
category: modeling-bpmn
kind: notation-element
summary: A BPMN gateway controls where a process path splits or joins. Splits send the flow down one,
  all, or some branches. Joins either pass flow on or wait for other branches.
arc42:
- 6
- 8
step: s10-document
related:
- event-based-gateway
- antipatterns-for-process-flows
- deadlock-in-process-models
- lack-of-synchronization-in-process-models
- bpmn-core-elements
- soundness-of-process-models
- bpmn-event
- bpmn-modeling-tips
checks:
- Every exclusive split that has a branch without a condition declares that branch as the default flow.
- Joins that must wait for concurrent branches use a parallel gateway, not an exclusive join.
- Each branch of an event-based gateway leads to an intermediate catch event of type timer, message, or
  signal.
- Inclusive splits have conditions on their outgoing flows, and the matching join is an inclusive gateway.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
  title: Exclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/parallel-gateways/
  title: Parallel gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/inclusive-gateways/
  title: Inclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-based-gateways/
  title: Event-based gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: A parallel split and join, followed by an exclusive split with a default flow.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Process execution can be pictured as tokens moving through a process model. A token marks where a process instance currently is. Plain sequence flow just moves a token along. Gateways route tokens in more complex patterns, and parallel gateways create new tokens.

**Exclusive gateway (XOR).** As a split, it picks one outgoing flow based on data, such as process variables. One flow can have no condition. The gateway must then name it as the default flow. As a join, it only passes tokens through. It does not synchronize concurrent flows the way a parallel gateway does.

**Parallel gateway (AND).** As a split, it takes all outgoing flows. As a join, it waits until every incoming flow has been taken.

**Inclusive gateway (OR).** As a split, it takes every outgoing flow whose condition is fulfilled. The join is finished when all incoming flows were taken. It is also finished when no path remains from any active node to it.

**Event-based gateway.** It waits for events and follows the flow of the first one that is triggered. The other events are then no longer possible. In Camunda, each target must be an intermediate catch event of type timer, message, or signal.

## Example

An online shop receives an order. A parallel split starts "pack goods" and "prepare invoice" at the same time. A parallel join waits for both before the next step. Then an exclusive split checks payment data. Paid orders go on to shipping. Other orders take the default flow to a reminder step.

## Trade-offs

Each gateway type fits one routing intent: exactly one path, all paths, or the paths whose conditions hold. An exclusive join does not wait for concurrent branches. A parallel join waits for every incoming flow.
