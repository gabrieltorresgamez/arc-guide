---
title: BPMN 2.0 Notation
slug: bpmn-2-0-notation-overview
category: modeling-bpmn
kind: standard
summary: BPMN 2.0 is an industry standard notation for modeling and running business processes. Its core
  elements are tasks, events, gateways, and sequence flow, which together show the order of work.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-core-elements
- bpmn-event
- bpmn-gateway-semantics
- event-based-gateway
- attached-boundary-intermediate-event
- bpmn-activity
- bpmn-swimlane-pool-and-lane
- runtime-view
checks:
- Each process model uses sequence flow to show the order of steps.
- Every outgoing flow of an event-based gateway leads to an intermediate catch event.
- Boundary events are modeled as intermediate catch events, and each is marked as interrupting or not
  on purpose.
- Inclusive gateways have conditions on their outgoing flows and a default flow.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/events/
  title: Overview | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-based-gateways/
  title: Event-based gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/inclusive-gateways/
  title: Inclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0/
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: Order process with an inclusive gateway and an interrupting boundary event.
review:
  status: generated
  flags: []
---

## Explanation

BPMN stands for Business Process Model and Notation. Version 2.0 is an industry standard for both modeling and executing processes. OMG, the standards body behind it, calls it a de-facto standard notation. Stakeholders can use it directly, and it does not depend on any implementation environment.

**Sequence flow.** Sequence flow is a core concept of BPMN. A sequence flow defines the order in which the steps of a process happen.

**Tasks.** Tasks are the basic elements. Each is an atomic unit of work, meaning one step that is not split further. Tasks combine to produce a meaningful result.

**Events.** A process can react to events. These are catching events. It can also emit events. These are throwing events.

**Boundary events.** A boundary event models what should happen if something occurs while an activity is running. It must be an intermediate catch event. If it is interrupting, it ends the activity it is attached to once it triggers. See the article Boundary Event.

**Gateways.** A gateway routes tokens in more complex patterns than plain sequence flow. A token marks the current position of a running process.
- The event-based gateway waits until one of its events fires. It then follows that event's flow, and the other events cannot fire afterward. Its outgoing flows must lead to intermediate catch events. In Camunda, these are timer, message, or signal events.
- The inclusive (OR) gateway follows every outgoing flow whose condition is true. If none is true, it uses the default flow.

## Example

An order process starts when an order arrives. A task checks stock. An inclusive gateway then looks at the order. If the customer wants gift wrapping and express delivery, both tasks start. If neither applies, the default flow goes straight to shipping. While the stock check runs, an interrupting boundary event for a cancellation message can stop it.

## Trade-offs

This article covers only the basic elements, not every BPMN element or variant. The event-based gateway limits its outgoing flows to intermediate catch events. An interrupting boundary event ends the running activity, so any work in progress there stops.
