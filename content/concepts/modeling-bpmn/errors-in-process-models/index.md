---
title: Errors in Process Models
slug: errors-in-process-models
category: modeling-bpmn
kind: concept
summary: Many real process models contain control-flow errors, such as deadlocks and lack of synchronization.
  A model counts as correct only if it has neither. A typical cause is merging parallel branches with
  the wrong gateway type.
arc42:
- 6
- 8
step: s10-document
related:
- deadlock-in-process-models
- lack-of-synchronization-in-process-models
- soundness-of-process-models
- antipatterns-for-process-flows
- bpmn-gateway-semantics
- bpmn-2-0-model-quality
checks:
- Each process model in the document contains neither a deadlock nor a lack of synchronization.
- No exclusive gateway merges the outgoing flows of a parallel gateway.
sources:
- url: https://issues.omg.org/issues/BPMN21-249
  title: BPMN 2.1 RTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2407.03965v1
  title: Instantaneous, Comprehensible, and Fixable Soundness Checking of Realistic BPMN Models
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'A parallel split merged by an exclusive gateway: the final task can run once per branch.'
review:
  status: generated
  flags: []
---

## Explanation

A process model can look fine and still have a structural flaw in how work flows through it. These flaws are control-flow errors. Research reports that many real process models suffer from them.

Two examples of such errors are:

- **Deadlock.** The process gets stuck. See *Deadlock in Process Models*.
- **Lack of synchronization.** The BPMN specification's chapter on mapping to WS-BPEL describes it as a reachable state where some sequence flow carries more than one token. See *Lack of Synchronization*.

See *Soundness of Process Models* for more.

**Gateway mismatch is one example.** (See *BPMN Gateway*.) Suppose a parallel gateway splits the flow into several branches. An exclusive gateway then merges those branches. That combination breaks safeness, meaning multiple tokens can appear. *BPMN Gateway Mismatch Antipatterns* covers more of these patterns.

## Example

A loan team models two checks that run side by side: a credit check and a property appraisal. A parallel gateway starts both. An exclusive gateway then merges them before the final decision task. Both branches now reach the decision step separately, so a sequence flow can carry more than one token. Changing the merge to a parallel gateway is one possible fix, aimed at matching the gateways.
