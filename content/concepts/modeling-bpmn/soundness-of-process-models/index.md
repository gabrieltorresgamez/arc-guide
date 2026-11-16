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
- bpmn-gateway-semantics
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
- url: https://issues.omg.org/issues/BPMN21-249
  title: BPMN 2.1 RTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://schematex.js.org/research/bpmn-exclusive-vs-parallel-gateway
  title: 'BPMN exclusive vs parallel gateways: a token-by-token worked example | Schematex Research'
  site: schematex.js.org
  accessed: '2026-11-09'
- url: https://research.tue.nl/p/en/research-outputs/seven-process-modeling-guidelines-7pmg
  title: Seven process modeling guidelines (7PMG) — Eindhoven University of Technology Research Portal
  site: research.tue.nl
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://aisel.aisnet.org/icis2014/proceedings/GeneralIS/28/
  title: 'AIS Electronic Library (AISeL) - ICIS 2014 Proceedings: Testing the Impact of Wand and Weber’s
    Decomposition Model on Process Model Understandability'
  site: aisel.aisnet.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://research.tue.nl/p/en/research-outputs/understanding-business-process-models-the-costs-and-benefits-of-s
  title: Understanding business process models — Eindhoven University of Technology Research Portal
  site: research.tue.nl
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

**Deadlock.** A deadlock means a token stays blocked on one edge of the graph.

**Lack of synchronization.** This is the second flaw.

**Where the idea is used.** Workflow nets are a subclass of Petri nets. They model the workflow of process activities. Soundness is defined for such nets and for workflow graphs.

**Variants.** Weaker or broader forms exist:

**Checking it.** Tools can verify soundness. The check looks for the absence of deadlock and of lack of synchronization. These are handled as separate Petri net analysis tasks, for example in the tool LoLA. One recently introduced BPMN soundness-checking tool displays violations in the model, runs in under 500 ms, and suggests fixes.

**More about process model quality.**

- **BPMN Gateway Mismatch Antipatterns:** A gateway mismatch means a BPMN split and its join have incompatible types. The result is a deadlock, where the process cannot finish, or a lack of synchronization, where more than one token ends up on an edge.
- **Deadlock in Process Models:** A deadlock is a control-flow error in a process model. A parallel join waits for a token that never arrives, so the instance stalls and never finishes. Matching split and join gateway types prevents it.
- **Errors in Process Models:** Many real process models contain control-flow errors, such as deadlocks and lack of synchronization. A model counts as correct only if it has neither.
- **Lack of Synchronization:** A lack of synchronization happens when parallel branches are merged by an exclusive (XOR) join. Nothing waits for the other branches, so the work after the merge runs once per branch instead of once.
- **BPMN 2.0 Model Quality:** A BPMN process model is of high quality when it is free of control-flow errors such as deadlocks. Tools can check this in milliseconds, and guidelines such as 7PMG give advice on model quality.
- **Process Model Complexity:** Larger models are harder to understand. Splitting them into subprocesses, limiting data objects, and following guidelines help.

## Example

A team models an order process. After approval, two branches run side by side: packing and invoicing. A checker analyzes the model. If a token can stay blocked on an edge, the checker reports a deadlock. If the branches can end up unsynchronized, it reports a lack of synchronization. The team fixes the model before anyone builds the process.

## Trade-offs

