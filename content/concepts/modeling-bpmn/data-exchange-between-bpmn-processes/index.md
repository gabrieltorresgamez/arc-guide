---
title: Data Exchange between BPMN Processes
slug: data-exchange-between-bpmn-processes
category: modeling-bpmn
kind: notation-element
summary: 'Separate BPMN processes sit in separate pools. They exchange data in two ways: messages sent
  across pools, or a shared data store that one process writes and another reads. The store keeps writer
  and reader independent.'
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- bpmn-collaboration-diagram
- bpmn-swimlane-pool-and-lane
- bpmn-data-element
- shared-database
- bpmn-event
- polling-consumer
- bpmn-connecting-object
- integration-pattern
checks:
- Processes run by different participants are modeled in separate pools, and message flows (not links
  inside one pool) connect them.
- Each message has a single sender and a single recipient.
- A reader process that polls a shared store has a timer start event with a date or cycle definition.
- The shared schema of a data store used by several processes is designed and documented.
- Where Camunda is used, the document states that data stores and data objects are modeling-only and not
  executed.
sources:
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html
  title: Shared Database - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/timer-events/
  title: Timer events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-coverage/
  title: BPMN coverage | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'Two pools: the writer saves data to a store, and a timer-started reader process reads it.'
review:
  status: generated
  flags: []
---

## Explanation

A BPMN collaboration diagram shows how two or more business entities interact (see the article BPMN Collaboration Diagram). A pool stands for a major participant, often a separate organization (see BPMN Swimlane (Pool and Lane)).

**Message flows connect pools.** A message flow can never link elements inside the same pool. That makes it the connector between pools.

**Events carry the signal.** A process can have one or more message start events. Deploying the process creates a message subscription for each one. An intermediate message catch event also creates a subscription when the process reaches it, so the instance waits there until the message arrives.

**Data stores hold shared data.** A data object shows the reader which data an activity needs or produces.

**A timer can start the reader.** A timer start event creates a new process instance each time the timer fires. It needs a date or a cycle definition, and deployment schedules it.

**Tool support varies.** Camunda supports data stores and data objects for modeling only, not for execution. A diagram can show the store, but the engine will not read or write it for you.

## Example

An online shop has two pools. The "Order intake" pool saves each new order to an orders store. A separate "Reporting" pool starts every night from a timer start event. It reads the orders store and builds a sales summary. Intake never calls Reporting. If Intake needs to tell Reporting something directly, it sends a message across the pools.

## Trade-offs

The Shared Database style, where applications keep their data in one database, has a difficult design problem: a unified schema that meets the needs of multiple applications. Messages are different: a message event has a single sender and a single recipient, while signal events reach multiple listeners. Because Camunda treats stores as modeling-only, the diagram documents the data exchange but does not run it.
