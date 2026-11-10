---
title: BPMN Core Elements
slug: bpmn-core-elements
category: modeling-bpmn
kind: notation-element
summary: BPMN is a standard notation for drawing business processes. Its core elements are tasks, sequence
  flow, gateways, events, data objects and swim lanes. Together they show what happens, in which order.
arc42:
- 6
- 3
- 12
step: s10-document
related:
- bpmn-activity
- bpmn-gateway-semantics
- bpmn-event
- bpmn-connecting-object
- bpmn-data-element
- bpmn-swimlane-pool-and-lane
- bpmn-link-event
- event-based-gateway
checks:
- Every process diagram uses sequence flow to show the order of steps.
- 'Each gateway type matches its routing intent: exclusive picks one path, parallel takes all, inclusive
  takes all whose condition is true.'
- Parallel splits are closed by a parallel join that waits for all incoming flows.
- Data objects show which data activities need or produce.
- Pools and lanes organize activities by responsibility.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
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
- url: https://docs.camunda.io/docs/components/modeler/bpmn/timer-events/
  title: Timer events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/link-events/
  title: Link events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: A small order process showing a start event, tasks, an exclusive gateway, sequence flow and
    end events.
review:
  status: generated
  flags: []
---

## Explanation

BPMN (Business Process Model and Notation) is an OMG specification. It is also ratified as ISO 19510.

**Flow objects.** Events, activities and gateways are the main describing elements of BPMN.

- **Tasks** are the atomic units of work. Combined, they produce a meaningful result. See BPMN Activity for more.
- **Sequence flow** is the arrow that sets the order in which steps happen.
- **Events** are things that happen. A process can catch an event, meaning it reacts to it. It can also throw an event, meaning it emits it. A timer event fires from a defined timer. It can start a process or sit in the middle of one. A link event connects two parts of one diagram, matched by link name.
- **Gateways** route flow in patterns more complex than a plain arrow.

**Gateway types.**

- Exclusive (XOR): picks exactly one outgoing path, based on data. It can have a default path.
- Parallel: takes all outgoing paths when splitting. When joining, it waits for all incoming paths.
- Inclusive (OR): takes every outgoing path whose condition is true.
- Event-based: waits for the first of several catch events, such as a timer, message or signal. It follows only that event's path.

**Data and organization.** Data objects show which data an activity needs or produces. Swim lanes (pools and lanes) organize activities visually.

**Tokens.** A token is created when the process starts. It moves forward with each completed step. It is consumed at the end, which ends that process instance.

## Example

Picture a simple order process. A start event creates a token. The task "Check order" runs. An exclusive gateway then sends the token down one path: "Approve order" or "Reject order". The approve path continues to an end event. The token is consumed there, and the instance ends.

## Trade-offs

Pick the gateway type that matches the routing you mean. An exclusive gateway takes one path. A parallel gateway takes all paths. An inclusive gateway takes every path whose condition is true.
