---
title: Deadlock in Process Models
slug: deadlock-in-process-models
category: modeling-bpmn
kind: concept
summary: A deadlock is a control-flow error in a process model. A parallel join waits for a token that
  never arrives, so the instance stalls and never finishes. Matching split and join gateway types prevents
  it.
arc42:
- 6
- 8
step: s10-document
related:
- soundness-of-process-models
- lack-of-synchronization-in-process-models
- antipatterns-for-process-flows
- errors-in-process-models
- bpmn-gateway-semantics
- bpmn-2-0-model-quality
- bpmn-modeling-tips
- process-model-versus-process-instance
checks:
- Every parallel (AND) join in the process models is preceded by a parallel split, so no branch can fail
  to deliver a token.
- Every exclusive gateway has a default flow or conditions that cover all cases.
- Process models have been checked for soundness, including option to complete.
- Inclusive (OR) joins are used only where their completion conditions are understood.
sources:
- url: https://arxiv.org/html/2407.03965v1
  title: Instantaneous, Comprehensible, and Fixable Soundness Checking of Realistic BPMN Models
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/parallel-gateways/
  title: Parallel gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
  title: Exclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/inclusive-gateways/
  title: Inclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.bpmn
  caption: 'Deadlock: an exclusive split feeds a parallel join, which waits forever for the second token.'
review:
  status: generated
  flags: []
---

## Explanation

A process model is a diagram of steps and decisions. Each running case is a process instance. Gateways are the diamond shapes that split or join the flow. Many models contain control-flow errors. Deadlock is one of them, and lack of synchronization is another.

**How a deadlock happens.** A parallel (AND) join makes the instance wait until every incoming sequence flow has been taken. If one incoming branch never delivers, the instance waits forever.

One example is mismatched gateways. An exclusive (XOR) gateway selects only one outgoing flow. If a parallel join follows it, the other branches never fire. The join keeps waiting, and the work after it never runs.

**The opposite mismatch.** An exclusive join only passes flows through. It does not merge concurrent flows the way a parallel gateway does. Merging a parallel split with an exclusive join therefore causes lack of synchronization, not a deadlock. See the article "Lack of Synchronization".

**Other ways to get stuck.** An exclusive gateway with no matching condition and no default flow creates an incident, and the instance gets stuck. A default flow avoids this. An inclusive (OR) join completes only under defined conditions. Either all incoming flows were taken at least once, or no path from any active node can still deliver one.

**Link to soundness.** Soundness is a quality check for process models. It has three parts: option to complete, proper completion, and no dead activities. Option to complete guarantees that no deadlocks occur. Proper completion means each token ends in a different end event. A dead activity is one that no instance can ever execute. See "Soundness of Process Models".

**Detection.** Soundness comes from Petri nets and workflow nets, which are formal models of token flow. Translating BPMN into Petri nets is not always possible. A dedicated open-source BPMN soundness checker exists that is fast, makes violations comprehensible, and suggests fixes.

## Example

An order process starts with an exclusive gateway: "Pay by card" or "Pay by invoice". Both paths lead into a parallel join before "Ship order". Only one path ever runs. The join waits for a token from the other path, which never comes. The order never ships, and the process never reaches its end. The fix is to use an exclusive join where the two paths meet, so it passes on whichever token arrives.

## Trade-offs

Choosing a join type is a trade-off. A parallel join waits for every branch, which is right after a parallel split but blocks after an exclusive split. An exclusive join never blocks, but it does not synchronize concurrent branches. That leads to lack of synchronization.
