---
title: Lack of Synchronization
slug: lack-of-synchronization-in-process-models
category: modeling-bpmn
kind: concept
summary: A lack of synchronization happens when parallel branches are merged by an exclusive (XOR) join.
  Nothing waits for the other branches, so the work after the merge runs once per branch instead of once.
arc42:
- 6
- 8
step: s10-document
related:
- deadlock-in-process-models
- antipatterns-for-process-flows
- bpmn-gateway-semantics
- errors-in-process-models
- soundness-of-process-models
- bpmn-modeling-tips
checks:
- Every place where parallel branches from an AND split come back together uses a parallel (AND) join,
  not an exclusive (XOR) join.
- No exclusive gateway merges flows that were started concurrently by a parallel gateway.
- Tasks after a merge of parallel branches run only once per process instance.
sources:
- url: https://schematex.js.org/research/bpmn-exclusive-vs-parallel-gateway
  title: 'BPMN exclusive vs parallel gateways: a token-by-token worked example | Schematex Research'
  site: schematex.js.org
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
  caption: 'Faulty model: an AND split merged by an XOR join, so ''Send confirmation'' runs twice.'
review:
  status: generated
  flags: []
---

## Explanation

A process model can split work into parallel branches. A parallel (AND) gateway does this: it takes all outgoing flows at once. Each branch carries its own token, a marker that shows where the process instance currently is.

A lack of synchronization is a modeling error. It appears when those parallel branches come back together at an exclusive (XOR) gateway instead of a parallel one.

An exclusive join does not synchronize. Each token that arrives simply continues on its own. Camunda describes this as pass-through behavior: the gateway does not merge concurrent flows the way a parallel gateway does.

The result is that tasks after the merge can run once for each arriving token, because each arrival can continue independently.

**The fix** is to join the branches with a parallel (AND) gateway. It waits until all required incoming flows have delivered their tokens. It then consumes those arrivals and releases one continuation. The downstream tasks then run once.

To spot the error, look at each place where parallel branches merge. Check which type of gateway does the merging.

For related gateway-mismatch patterns, see BPMN Gateway Mismatch Antipatterns. For the gateways themselves, see BPMN Gateway.

## Example

An order process splits after payment approval. One branch reserves stock. The other branch prepares the invoice. Both branches then merge at an exclusive gateway, and the next task is "Send confirmation to customer."

The reserve-stock branch finishes and sends a token through the merge. The confirmation goes out. The invoice branch finishes later and sends its own token. The confirmation goes out again.

Replacing the exclusive merge with a parallel merge fixes this. The process waits for both branches, then sends one confirmation.
