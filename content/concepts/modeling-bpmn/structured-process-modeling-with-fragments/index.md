---
title: Structured Process Modeling with Fragments
slug: structured-process-modeling-with-fragments
category: modeling-bpmn
kind: method
summary: Structured process modeling builds a model from a simple sequence of steps and inserts parallel
  or alternative blocks. In BPMN, these blocks use parallel gateways (AND) and exclusive gateways (XOR)
  as splits and joins.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-gateway-semantics
- antipatterns-for-process-flows
- soundness-of-process-models
- deadlock-in-process-models
- lack-of-synchronization-in-process-models
- errors-in-process-models
- bpmn-modeling-tips
- process-model-complexity
checks:
- Each parallel (AND) split in a process model has a parallel (AND) join that waits for all its branches.
- Exclusive (XOR) splits are used where exactly one path should be taken, such as alternative branches
  or loop exits.
- Exclusive joins are used only where paths are alternatives, since they do not wait for other paths.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/parallel-gateways/
  title: Parallel gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
  title: Exclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://research.tue.nl/p/en/research-outputs/seven-process-modeling-guidelines-7pmg
  title: Seven process modeling guidelines (7PMG) — Eindhoven University of Technology Research Portal
  site: research.tue.nl
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A plain sequence refined with a parallel block that contains alternative branches.
review:
  status: generated
  flags: []
---

## Explanation

A process model shows the steps of a business process and the order between them.

**Parallel gateway (AND).** As a split, it starts all outgoing paths at once. As a join, it waits until every incoming path has arrived.

**Exclusive gateway (XOR).** As a split, it picks exactly one outgoing path, based on data such as process variables. As a join, it lets arriving paths pass through. It does not wait for other paths.

These gateways can be combined into two patterns:

- **Parallel block:** an AND split, several paths, then an AND join. All paths run, and the process continues only when all are done.
- **Alternative branches:** an XOR split, several paths, then an XOR join. Exactly one path runs.

An AND join waits for all paths. An XOR join does not wait.

## Example

An order process starts as a sequence: "Receive order", then "Ship order". The modeler refines it in two steps.

1. Between the two activities, insert a parallel block. "Check stock" and "Check payment" both start after an AND split. An AND join waits for both.
2. In the "Check payment" path, insert alternative branches. An XOR split chooses "Charge card" or "Send invoice". An XOR join merges the chosen path.

The second block sits fully inside one path of the first block.

## Trade-offs

An XOR join has pass-through semantics and does not merge concurrent flows the way an AND join does.

Guidelines such as 7PMG come from research on how model structure affects errors and comprehension. They are meant to be intuitive to practitioners.
