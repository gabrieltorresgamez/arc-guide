---
title: BPMN Event
slug: bpmn-event
category: modeling-bpmn
kind: notation-element
summary: A BPMN event is something that happens in a process and affects its flow. Events either wait
  for something from outside (catch) or are raised by the process itself (throw).
arc42:
- 6
- 8
step: s10-document
related:
- intermediate-event
- attached-boundary-intermediate-event
- bpmn-link-event
- bpmn-compensation-event
- event-based-gateway
- bpmn-core-elements
- bpmn-activity
- bpmn-gateway-semantics
checks:
- Boundary events in the process models are intermediate catch events.
- Every throwing link event has a catching link event with the same link name.
- Terminate end events inside a subprocess are understood to stop only that subprocess.
- Event subprocesses that must react repeatedly are modeled as non-interrupting.
- Each start event names an external trigger that begins the process or subprocess.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/events/
  title: Overview | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/link-events/
  title: Link events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/terminate-events/
  title: Terminate events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-subprocesses/
  title: Event subprocess | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/signal-events/
  title: Signal events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A start event, a link throw and catch pair that skips a section, and a terminate end event.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A BPMN event marks a point where something happens during a process. See BPMN Core Elements for the full set of diagram elements.

**Catch and throw**

Events fall into two groups.

- A catch event comes from outside the process. The process passively waits for it.
- A throw event is something the process does itself, as part of its own execution.

**Start events**

A start event reacts to something external. That trigger begins the process or a subprocess. A subprocess is a smaller process nested inside a larger one.

**Boundary events**

A boundary event must be an intermediate catch event. The articles Boundary Event and Intermediate Event cover this in detail.

**Link events**

Link events come in pairs. One throws and marks an exit point. The other catches and marks a re-entry point. A shared link name matches them.

A pair works like two plain intermediate events joined by a sequence flow. Modelers use links to build loops or to skip sections. The article Link Event covers this.

**Terminate end events**

A terminate end event stops every element instance in its flow scope. On the process scope, the process instance then completes. Inside a subprocess, it only affects that subprocess, and the subprocess completes.

**Event subprocesses**

An event subprocess can be interrupting or non-interrupting.

- An interrupting one can trigger only once.
- A non-interrupting one can trigger many times.

**Signals**

Broadcasting a signal triggers every signal event with a matching name. So one signal can reach many subscribers.

## Example

An order process starts when a customer order arrives. That arrival is a catch event, because it comes from outside.

The process then checks stock. A link throw event sends the flow to a matching link catch event further on, which skips a section. The process ends with a terminate end event, which stops everything still running in that scope.

If a warehouse system broadcasts a signal, every signal event with that name reacts.

## Trade-offs

Signals reach many subscribers at once, because every matching signal event is triggered. That is useful when you want to communicate with multiple listeners.

An interrupting event subprocess fires once. A non-interrupting one can fire repeatedly. Pick based on whether the trigger may happen again.
