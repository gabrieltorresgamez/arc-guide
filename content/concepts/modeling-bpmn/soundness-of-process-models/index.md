---
title: Soundness of Process Models
slug: soundness-of-process-models
category: modeling-bpmn
kind: quality-attribute
summary: A process model is sound when it has no deadlock and no lack of synchronization. Soundness is
  a basic correctness check, and tools can verify it automatically.
arc42:
- 6
- 8
- 10
step: s10-document
related:
- deadlock-in-process-models
- lack-of-synchronization-in-process-models
- antipatterns-for-process-flows
- errors-in-process-models
- bpmn-gateway-semantics
- bpmn-2-0-model-quality
- process-model-versus-process-instance
- workflow-pattern
checks:
- Process models in the documentation have been checked for both deadlock and lack of synchronization.
- The check was done with a tool, and any reported violations were fixed or explained.
- If the documentation claims only relaxed soundness, it says so and does not call the model sound.
sources:
- url: https://patents.google.com/patent/US9477937B2/en
  title: US9477937B2 - Computer-implemented method, computer program product and system for analyzing
    a control-flow in a business process model - Google Patents
  site: patents.google.com
  accessed: '2026-11-09'
- url: https://theo.informatik.uni-rostock.de/theo-forschung/tools/uml2owfn/fahlandfjkfvw-2009-bpm/
  title: fahlandfjkfvw_2009_bpm - Theoretische Informatik - Universität Rostock
  site: theo.informatik.uni-rostock.de
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Petri_net
  title: Petri net - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2407.03965
  title: '[2407.03965] Instantaneous, Comprehensible, and Fixable Soundness Checking of Realistic BPMN
    Models'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A small process where parallel branches split and join with matching gateways.
review:
  status: generated
  flags: []
---

## Explanation

Soundness is a correctness property of process models. A workflow graph is sound exactly when it contains neither a deadlock nor a lack of synchronization.

**Deadlock.** A deadlock means a token stays blocked on one edge of the graph. See *Deadlock in Process Models*.

**Lack of synchronization.** This is the second flaw. See *Lack of Synchronization* for details.

**Where the idea is used.** Workflow nets are a subclass of Petri nets. They model the workflow of process activities. Soundness is defined for such nets and for workflow graphs.

**Variants.** Weaker or broader forms exist:

- *Relaxed soundness* is weaker than soundness. Every edge must be marked by at least one sound execution. A sound execution reaches neither a deadlock nor a lack of synchronization.
- *Generalized soundness* asks that a workflow net works for every number of initial tokens, not just one. Acyclic well-handled workflow nets meet this.

**Checking it.** Tools can verify soundness. The check looks for the absence of deadlock and of lack of synchronization. These are handled as separate Petri net analysis tasks, for example in the tool LoLA. One recently introduced BPMN soundness-checking tool displays violations in the model, runs in under 500 ms, and suggests fixes.

## Example

A team models an order process. After approval, two branches run side by side: packing and invoicing. A checker analyzes the model. If a token can stay blocked on an edge, the checker reports a deadlock. If the branches can end up unsynchronized, it reports a lack of synchronization. The team fixes the model before anyone builds the process.

## Trade-offs

Soundness covers only the two flaws named above.
