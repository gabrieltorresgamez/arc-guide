---
title: Process Analysis
slug: process-analysis
category: modeling-bpmn
kind: method
summary: 'Process analysis turns a business process into a BPMN model by working through ordered questions:
  where it starts and ends, what steps occur, which paths exist, who takes part, and what is exchanged.'
arc42:
- 6
- 3
step: s03-functional-requirements
related:
- bpmn-swimlane-pool-and-lane
- bpmn-event
- bpmn-gateway-semantics
- bpmn-layout-guideline
- bpmn-modeling-tips
- purpose-of-process-analysis-and-modeling
- levels-of-process-modeling
- runtime-view
checks:
- Each process has a start event and end events that show its trigger and outcomes.
- Tasks are named with an object and an infinitive verb.
- Exclusive gateways are labeled as questions and their outgoing flows as answers.
- The happy path is drawn on a straight line in the center, left to right, with few crossing flows.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/none-events/
  title: None events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/naming-bpmn-elements/
  title: Naming BPMN elements | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/modeling-beyond-the-happy-path/
  title: Modeling beyond the happy path | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
  title: Exclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/BPMN/2.0/About-BPMN
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'Order process: start event, tasks, a question gateway and two outcomes.'
review:
  status: generated
  flags: []
---

## Explanation

Process analysis builds a BPMN model step by step. BPMN is a de-facto standard notation for business processes, and it is independent of any particular implementation environment. Work through the questions in order.

**Boundaries: where does the process start and end?**
A none start event is where a process instance starts when the process is activated. It is also required to trigger a process via a form. A none end event ends one execution path. The process completes when no active paths remain, so end events define the outcomes. Name events after a business state that is reached or awaited. Use an object plus a verb that expresses a state, such as "invoice received."

**Activities: what happens?**
Name each task with an object plus a verb in the infinitive, such as "check invoice." This is verb-object style.

**Paths: what can differ or go wrong?**
Model the happy path first. Then collect exceptions, prioritize them, and add them step by step. An exclusive gateway picks exactly one outgoing path based on data. A default flow covers the case where no condition holds. Label the gateway as a question. Label each outgoing flow as an answer.

**Participants and exchanges**
Message events refer to a message and are used to wait until a proper message is received. A single process instance waiting for a message has a one-to-one relationship with its sender. For the notation of participants, see the article BPMN Swimlane (Pool and Lane).

**Keeping the diagram readable**
Model the diagram from left to right and avoid flows crossing each other. You may want to place the happy path on a straight line in the center. Consider avoiding lanes in most models. In collaboration diagrams, rearrange the order of pools to avoid message flows crossing pools.

## Example

A company models how it handles a customer order.

1. Boundaries: the process starts with "order received." It ends with "order shipped" or "order rejected."
2. Activities: "check order" and "ship goods."
3. Paths: the happy path runs from receipt to shipment. A gateway asks "Order valid?" The answers "yes" and "no" lead to different paths. The team adds further exceptions later.
4. Participants: the customer sends the order as a message to the company.

## Trade-offs

Lanes can hurt readability and make models harder to change, which increases maintenance effort.
