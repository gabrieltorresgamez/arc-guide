---
title: BPMN Focus on Connected Businesses
slug: bpmn-focus-on-connected-businesses
category: modeling-bpmn
kind: concept
summary: BPMN can model processes that cross company borders. Each organization gets its own pool, and
  message flows show the messages passing between them. Business and technical people can both read the
  result.
arc42:
- 3
- 5
- 6
step: s02-scope-context
related:
- bpmn-collaboration-diagram
- bpmn-swimlane-pool-and-lane
- bpmn-conversation-diagram
- bpmn-diagram-types
- data-exchange-between-bpmn-processes
- bpmn-event
- messaging
- bpmn-motivation
checks:
- Each participating organization in a cross-company process appears as its own pool.
- Messages that cross organizational boundaries are drawn as message flows between pools, not inside one
  pool.
- Each message has exactly one sender and one recipient.
- Steps where a process waits for a partner's answer use message events.
sources:
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0/
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A customer and a webshop exchange messages across pool boundaries.
review:
  status: generated
  flags: []
---

## Explanation

BPMN is a flowchart-like notation. Stakeholders can use it directly, and it does not depend on any implementation environment. That makes it a shared language for business and IT people (see BPMN Motivation).

**Pools for each organization.** A pool stands for a main participant in a process. Pools typically separate different organizations (see BPMN Swimlane (Pool and Lane)).

**Message flows between pools.** A message flow shows which messages cross an organizational boundary. It connects one pool to another.

**Message events.** A message event makes a process instance wait until the right message arrives from a secondary process or an external system.

**Process types.** BPMN distinguishes three kinds of process:

- *Private processes* are internal to one organization.
- *Public (abstract) processes* show the interactions between a private process and another process or participant.
- *Collaboration (global) processes* depict the interactions between two or more business entities.

A collaboration process may be shown as two or more abstract processes that interact through message flow (see BPMN Collaboration Diagram).

## Example

A customer orders from a webshop. The webshop asks a payment provider to charge the customer. It then asks a delivery service to ship the goods. Each of the four parties is a pool. Message flows carry the order, the payment request, the payment confirmation and the shipping request between the pools. The webshop's process waits at a message event until the payment confirmation arrives. Each party's own private process stays internal to that organization.


