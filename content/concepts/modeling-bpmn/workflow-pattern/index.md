---
title: Workflow Pattern
slug: workflow-pattern
category: modeling-bpmn
kind: pattern
summary: Workflow patterns are named, recurring ways a process controls its flow, such as sequence, parallel
  split, and simple merge. They help describe process models and compare process languages such as BPMN.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-gateway-semantics
- antipatterns-for-process-flows
- lack-of-synchronization-in-process-models
- deadlock-in-process-models
- event-based-gateway
- process-notations-comparison
- soundness-of-process-models
- bpmn-2-0-notation-overview
checks:
- Where a process runs branches in parallel, a parallel gateway splits the flow and a parallel gateway
  joins it again.
- Exclusive gateways are used as merges only where the incoming branches are alternatives, since they
  do not synchronize concurrent flows.
- Each exclusive split has conditions on its outgoing flows, because the gateway takes the first flow
  whose condition is fulfilled.
sources:
- url: https://docs.tibco.com/pub/amx-bpm/4.3.1/doc/html/bpmhelp/GUID-781A0624-4DF4-4E64-A8C1-668BAEC2F808.html
  title: Workflow Process Patterns Support
  site: docs.tibco.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Workflow_pattern
  title: Workflow pattern - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/parallel-gateways/
  title: Parallel gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
  title: Exclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: A sequence, then a parallel split and a synchronizing join.
review:
  status: generated
  flags: []
---

## Explanation

A workflow pattern is a named control-flow structure that recurs in process models. Control flow means the order in which steps run, and how the path splits or joins.

**Patterns from the verified set**

- **Sequence.** A step becomes enabled once the step before it in the same process completes.
- **Parallel split.** One branch diverges into two or more branches that run at the same time.
- **Simple merge.** Whenever any incoming branch is enabled, control passes to the next branch. Nothing waits for the other branches.
- **Arbitrary cycles.** Loops in a process model may have more than one entry or exit point.
- **Deferred choice.** The environment decides which of several branches runs, as a race between them.

**How the patterns map to BPMN**

BPMN is a process notation. Its gateways split and join the flow. See the article *BPMN Gateway*.

- A parallel gateway used as a split takes all outgoing flows, and the paths run concurrently and independently.
- A parallel gateway used as a join makes the process instance wait until every incoming flow has arrived.
- An exclusive gateway used as a split takes the first flow whose condition is fulfilled.
- An exclusive gateway used as a merge only passes control through. It does not merge concurrent flows the way a parallel gateway does.

**What the patterns are used for**

The patterns served as initial requirements for designing the workflow language and system YAWL (Yet Another Workflow Language). They have also been used to evaluate proposed standards: BPEL, BPMN, UML Activity diagrams and XPDL.

The same research groups that developed these patterns also proposed further pattern sets beyond control flow. These cover data, resources, exception handling and service interaction.

## Example

A support team handles a refund request. A clerk registers the request, then a second step checks the order. That is a sequence. After the check, two branches start together: one prepares the payment and one notifies the customer. That is a parallel split. A join then waits until both branches finish. Another place in the process lets either of two alternative review paths continue immediately. That is a simple merge, and it does not wait.

## Trade-offs

One practical caution follows from the BPMN gateways: an exclusive gateway used as a merge only passes control through, while a parallel gateway used as a join waits for every incoming flow.
