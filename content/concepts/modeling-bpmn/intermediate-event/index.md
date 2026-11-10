---
title: Intermediate Event
slug: intermediate-event
category: modeling-bpmn
kind: notation-element
summary: An intermediate event sits inside a process flow, between start and end. Throwing events (filled
  icon) fire a trigger. Catching events (white icon) make the process wait until a trigger occurs.
arc42:
- 6
step: s10-document
related:
- bpmn-event
- attached-boundary-intermediate-event
- bpmn-link-event
- event-based-gateway
- bpmn-gateway-semantics
- bpmn-core-elements
checks:
- Catching events use an unfilled icon and throwing events use a filled icon, consistently across the
  diagrams.
- Boundary events are modeled only as catching events.
- Timer and conditional events are modeled as catching events only.
- Waiting for several messages uses receive tasks combined with a parallel gateway.
sources:
- url: https://www.flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs
  title: BPMN 2.0 Constructs · Flowable Open Source Documentation
  site: flowable.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/events/
  title: Overview | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
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
diagrams:
- file: diagram-1.bpmn
  caption: A process throws a message, then waits at a catching message event.
review:
  status: generated
  flags: []
---

## Explanation

An intermediate event is an event placed in the middle of a process, not at its start or end. For the general idea of events, see the article BPMN Event.

**Throwing and catching**

The inner icon shows the direction. A throwing event has an icon filled with black. A catching event has a white, unfilled icon.

- A throwing event fires a trigger when execution reaches it.
- A catching event waits for a trigger when execution reaches it.

Message events follow the same rule. The message catch icon is white to show that it catches.

**What waiting means**

A catching event stops the token until the awaited event occurs. For a message, the engine creates a subscription. The instance then waits until the message is correlated, meaning matched to it.

**Waiting for several messages**

To wait for several messages and merge them, combine receive tasks with a parallel gateway. A receive task is a task that waits for a message.

**Where an event sits**

An intermediate event can sit in the normal sequence flow. It can also sit on the edge of an activity that it may interrupt. Then it is a boundary event. Boundary events always catch and never throw. See the article Boundary Event.

**Which types can catch or throw**

Some types are restricted:
- Timer and conditional events can only catch.
- Link events are used only as intermediate events. See the article Link Event.
- A catching error event must be attached to an activity.

**Waiting for one of several events**

An event-based gateway routes by which event happens next, not by data. The instance waits at the gateway until one event triggers. Then the others can no longer fire. See the article Event-Based Gateway.

## Example

A process sends an order confirmation, then waits for the customer's payment message. The send step is a throwing message event with a filled envelope. The wait step is a catching message event with a white envelope. The token stays at the white envelope until the payment message arrives. Then the process continues.
