---
title: Event-Based Gateway
slug: event-based-gateway
category: modeling-bpmn
kind: notation-element
summary: An event-based gateway sends a process down one path depending on which event happens first,
  not on data. The first event wins, and the other events can no longer trigger.
arc42:
- 6
step: s10-document
related:
- bpmn-gateway-semantics
- intermediate-event
- bpmn-event
- antipatterns-for-process-flows
- bpmn-2-0-notation-overview
- timeout-based-delivery
checks:
- Each outgoing flow of an event-based gateway leads to an event or receive task, not to a decision based
  on data.
- If the target is Camunda 8, every outgoing flow of the event-based gateway ends at a timer, message
  or signal intermediate catch event.
- Decisions based on data use a data-based exclusive gateway, not an event-based gateway.
sources:
- url: https://camunda.com/bpmn/reference/
  title: BPMN 2.0 Symbols - A complete guide with examples. | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-based-gateways/
  title: Event-based gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: After ordering, the process waits for either the delivery message or a 60-minute timer. The
    first event decides the path.
review:
  status: generated
  flags: []
---

## Explanation

An event-based gateway is a decision point in a process model (see BPMN Gateway). It does not look at data. It routes by which event takes place next.

Compare it with the data-based exclusive gateway. That gateway decides from available data, such as a chosen recipe, and follows only one path. The event-based gateway decides from events.

**How it works**

- The process waits at the gateway.
- Each outgoing flow leads to an event or a receive task.
- The first event that is triggered selects its outgoing flow.
- No other event of that gateway can be triggered afterward.

**Which elements may follow**

Not every intermediate event can follow an event-based gateway (see Intermediate Event). In Camunda 8, each outgoing flow must lead to an intermediate catch event of type timer, message or signal. Receive tasks can also be combined with the gateway.

A timer is a typical way to handle a reply that never comes. One branch waits for the expected message. Another branch fires when time runs out.

## Example

A customer orders a pizza and waits. Two branches follow the gateway. One catches a "pizza delivered" message, and the customer eats. The other is a 60-minute timer, after which the customer makes an anxious phone call.

If the pizza arrives first, the timer can no longer fire. If the timer fires first, the delivery branch can no longer be taken.

## Trade-offs

Only certain elements may follow the gateway, so some intermediate events cannot be modeled directly after it. Camunda 8, for example, lists only timer, message and signal catch events.

Because the first event wins, the other events are ignored once one has fired.
