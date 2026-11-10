---
title: BPMN Gateway Mismatch Antipatterns
slug: antipatterns-for-process-flows
category: modeling-bpmn
kind: pattern
summary: A gateway mismatch means a BPMN split and its join have incompatible types. The result is a deadlock,
  where the process cannot finish, or a lack of synchronization, where an end event is reached more than
  once.
arc42:
- 6
- 8
step: s10-document
related:
- deadlock-in-process-models
- lack-of-synchronization-in-process-models
- soundness-of-process-models
- bpmn-gateway-semantics
- errors-in-process-models
- bpmn-2-0-model-quality
checks:
- Every inclusive (OR) split is closed by an inclusive join, not by a parallel join.
- The model is checked for deadlocks and lack of synchronization, for example with a BPMN model checker.
- Each process run reaches any end event at most once (proper completion).
sources:
- url: https://arxiv.org/html/2105.06016v1
  title: Automated Discovery of Process Models with True Concurrency and Inclusive Choices
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://tynerblain.com/2006/09/20/bpmn-deadlock/
  title: BPMN Deadlock – Tyner Blain
  site: tynerblain.com
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2408.06028
  title: 'BPMN Analyzer 2.0: Instantaneous, Comprehensible, and Fixable Control Flow Analysis for Realistic
    BPMN Models'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'Antipattern: an inclusive split joined by a parallel gateway can deadlock. Replace the join
    with an inclusive gateway.'
review:
  status: generated
  flags: []
---

## Explanation

A mismatch means the join type does not fit the split before it.

**Deadlock.** A parallel (AND) join waits until every incoming path has arrived. Suppose the split before it started only some of those paths. The join then waits forever, and the process cannot complete.

**Typical fix.** An inclusive (OR) split may start a varying number of paths. Join those paths with an inclusive (OR) join. This join waits only for the paths that were actually activated. A parallel join in that place causes the deadlock.

**Finding these errors.** You do not have to spot them by eye. BPMN Analyzer is a model checker. It explores the possible states of a model. It reports deadlocks, livelocks, starvation, dead activities, and lack of synchronization. It also suggests quick fixes for the most common control-flow errors, including those that lead to deadlock and lack of synchronization.

For the wider ideas, see the articles Soundness of Process Models, Deadlock in Process Models, and Lack of Synchronization.

## Example

A support process receives a ticket. An inclusive split starts "Notify customer" and "Update billing", each only when it applies. Often only one applies. A parallel join then waits for both, so the ticket never closes. The fix is to replace the parallel join with an inclusive join. It waits only for the tasks that actually started.

## Trade-offs

This article covers only the inclusive-split case and the tool support. Automated checks catch common control-flow errors, but this article does not claim they catch every mismatch.
