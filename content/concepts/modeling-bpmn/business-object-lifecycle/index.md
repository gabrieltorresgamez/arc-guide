---
title: Business Object Lifecycle
slug: business-object-lifecycle
category: modeling-bpmn
kind: concept
summary: A business object lifecycle describes the states an object passes through, drawn as a state machine.
  Processes change those states. This data-centric view is an alternative to modeling only the activities
  of a process.
arc42:
- 6
- 8
step: s06-domain
related:
- state-machine-diagram
- state-and-event
- entity-life-cycle
- process-notations-comparison
- bpmn-data-element
- bpmn-event
- process-model-complexity
- aris-process-views
checks:
- Important business objects have their lifecycle drawn as a state machine diagram or statechart.
- Constraints on how processes may change each business object are stated.
- Process events are described as business-relevant states of information objects.
- Where many object instances interact in parallel, the model goes beyond a single activity flow.
sources:
- url: https://ar5iv.labs.arxiv.org/html/1408.5094
  title: '[1408.5094] Verifiable UML Artifact-Centric Business Process Models'
  site: ar5iv.labs.arxiv.org
  accessed: '2026-11-09'
- url: https://ar5iv.labs.arxiv.org/html/1303.2554
  title: '[1303.2554] Artifact Lifecycle Discovery'
  site: ar5iv.labs.arxiv.org
  accessed: '2026-11-09'
- url: https://ariscommunity.com/help/aris-express/35908
  title: Event | ARIS BPM Community
  site: ariscommunity.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A process that moves an invoice from one state to another.
review:
  status: generated
  flags: []
---

## Explanation

Most process models center on activities: what people or systems do, in which order. The artifact-centric (or data-centric) approach is an alternative. It centers on the business objects (artifacts) themselves.

**Lifecycle as a state machine.** Each object has a lifecycle: the states it can be in and how it moves between them. You can draw a lifecycle as a statechart or a UML-style state machine diagram. See the articles State Machine Diagram and State and Event.

**Processes change states.** In the BALSA framework, services are atomic units of work that change artifacts. Associations set limits on how services may change them.

**Events are states.** In ARIS business process models, an event is a commercially relevant state. It controls how one or more processes continue. State changes show up as changes in the status of an information object.

**Why not only activities?** For a large number of processes, the flow of activities is closely tied to the data flow. A prime example is a build-to-order process, where customer orders and material orders are in n-to-m relations. Such complex dynamics cannot be represented in a classical activity-flow model in such cases. Artifact-centric systems also allow a high level of parallelism and complex relationships between multiple artifact instances.

See Process Notations Comparison for how EPC, BPMN and UML activity diagrams compare.

## Example

Take a rental car. Its lifecycle might have the states "available", "rented" and "in maintenance". A "return car" process moves it from "rented" to "available". The state "available" can act as an event that lets the next booking proceed. Each car has its own state, even when many cars are handled at the same time.

## Trade-offs

The sources describe advantages of this approach, such as combining data and process aspects and handling n-to-m relations between objects. They do not describe costs of the approach, so weigh it against your own modeling needs.
