---
title: BPMN Event
slug: bpmn-event
order: 10
category: modeling-bpmn
kind: notation-element
summary: A BPMN event is something that happens in a process and affects its flow. Events either wait
  for something from outside (catch) or are raised by the process itself (throw).
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-gateway
- bpmn-core-elements
- bpmn-activity
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
- url: https://www.flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs
  title: BPMN 2.0 Constructs · Flowable Open Source Documentation
  site: flowable.com
  accessed: '2026-11-09'
- url: https://camunda.com/bpmn/reference/
  title: BPMN 2.0 Symbols - A complete guide with examples. | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-based-gateways/
  title: Event-based gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://camunda.com/blog/2018/08/bpmn-for-microservices-orchestration-a-primer-part-1/
  title: BPMN and Microservices Orchestration, Part 1 of 2 | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://docs.axelor.com/studio/3.3/bpm-docs/BPMN/events/link_event.html
  title: 'Link Event :: Axelor Documentation'
  site: docs.axelor.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/compensation-events/
  title: Compensation events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.org/manual/7.6/reference/bpmn20/events/cancel-and-compensation-events/
  title: Cancel and Compensation Events | docs.camunda.org
  site: docs.camunda.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/error-events/
  title: Error events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/timer-events/
  title: Timer events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/escalation-events/
  title: Escalation events | Camunda 8 Docs
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

A boundary event must be an intermediate catch event.

**Link events**

Link events come in pairs. One throws and marks an exit point. The other catches and marks a re-entry point. A shared link name matches them.

A pair works like two plain intermediate events joined by a sequence flow. Modelers use links to build loops or to skip sections.

**Terminate end events**

A terminate end event stops every element instance in its flow scope. On the process scope, the process instance then completes. Inside a subprocess, it only affects that subprocess, and the subprocess completes.

**Event subprocesses**

An event subprocess can be interrupting or non-interrupting.

- An interrupting one can trigger only once.
- A non-interrupting one can trigger many times.

**Signals**

Broadcasting a signal triggers every signal event with a matching name. So one signal can reach many subscribers.

**More about events.**
- **Intermediate events** sit in the middle of a process. A throwing event has a black-filled icon and fires a trigger when execution reaches it. A catching event has a white icon and makes the process wait until the trigger occurs.
- **Boundary events** sit on the edge of a task or subprocess and watch for something while it runs. An interrupting boundary event ends the activity when it fires, and a non-interrupting one does not. An error boundary event is always interrupting.
- **Link events** work as a jump: a throwing link event is the exit point and the catching link event with the same name is the re-entrance point. They carry no business meaning and only make diagrams easier to read.
- **Compensation events** model the undo of work that finished successfully. A compensation boundary event marks an activity as one that may need to be reverted, and a throwing compensation event starts the undo.

## Example

An order process starts when a customer order arrives. That arrival is a catch event, because it comes from outside.

The process then checks stock. A link throw event sends the flow to a matching link catch event further on, which skips a section. The process ends with a terminate end event, which stops everything still running in that scope.

If a warehouse system broadcasts a signal, every signal event with that name reacts.

## Trade-offs

Signals reach many subscribers at once, because every matching signal event is triggered. That is useful when you want to communicate with multiple listeners.

An interrupting event subprocess fires once. A non-interrupting one can fire repeatedly. Pick based on whether the trigger may happen again.
