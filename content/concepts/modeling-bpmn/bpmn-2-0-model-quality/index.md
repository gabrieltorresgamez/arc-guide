---
title: BPMN 2.0 Model Quality
slug: bpmn-2-0-model-quality
category: modeling-bpmn
kind: concept
summary: A BPMN process model is of high quality when it is free of control-flow errors such as deadlocks.
  Tools can check this in milliseconds, and guidelines such as 7PMG give advice on model quality.
arc42:
- 6
- 8
step: s10-document
related:
- soundness-of-process-models
- deadlock-in-process-models
- lack-of-synchronization-in-process-models
- errors-in-process-models
- bpmn-modeling-tips
- structured-process-modeling-with-fragments
- bpmn-2-0-notation-overview
- antipatterns-for-process-flows
checks:
- Process models in the documentation have been checked for deadlock and lack of synchronization (soundness).
- The team uses an automated tool to check soundness, for example by translating models to Petri nets.
- The team names the modeling guidelines it follows for model quality, such as 7PMG.
sources:
- url: https://issues.omg.org/issues/BPMN21-249
  title: BPMN 2.1 RTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://theo.informatik.uni-rostock.de/theo-forschung/tools/uml2owfn/fahlandfjkfvw-2009-bpm/
  title: fahlandfjkfvw_2009_bpm - Theoretische Informatik - Universität Rostock
  site: theo.informatik.uni-rostock.de
  accessed: '2026-11-09'
- url: https://research.tue.nl/p/en/research-outputs/seven-process-modeling-guidelines-7pmg
  title: Seven process modeling guidelines (7PMG) — Eindhoven University of Technology Research Portal
  site: research.tue.nl
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
  title: Business Process Model and Notation - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://arxiv.org/abs/2407.03965
  title: '[2407.03965] Instantaneous, Comprehensible, and Fixable Soundness Checking of Realistic BPMN
    Models'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'A sound process: the exclusive split and the exclusive join match, so each token passes through
    once.'
review:
  status: generated
  flags: []
---

## Explanation

BPMN is a notation for drawing business processes. It is an OMG specification and also an ISO standard (ISO 19510). See "BPMN 2.0 Notation" for the notation itself.

**Control-flow errors.** Many process models contain errors that keep them from running properly. The BPMN specification describes a process run as tokens moving along arrows (sequence flows). It defines two key errors in these terms:

- **Deadlock:** a reachable state where a token sits on an arrow and can never be removed. The process gets stuck. See "Deadlock in Process Models".
- **Lack of synchronization:** a reachable state where more than one token sits on the same arrow. See "Lack of Synchronization".

**Soundness.** Checking a model for soundness means checking that neither error can occur. See "Soundness of Process Models".

**Automatic checking.** Researchers checked 735 models derived from industrial practice, using three approaches. These were the tool Woflan, the Petri net model checker LoLA, and a recently developed technique based on SESE decomposition. The models were first translated into Petri nets, a formal notation that tools can analyze. The result: industrial models can be checked in a few milliseconds. Modeling can therefore be tightly combined with control-flow analysis. A more recent open-source tool checks soundness within 500 ms and suggests fixes.

**Guidelines.** The seven process modeling guidelines (7PMG) were proposed to give practitioners advice on model quality that rests on empirical evidence. For practical advice, see "BPMN Modeling Guidelines".

## Example

A team models an order process. After "Receive order", an exclusive gateway (a decision point) sends the flow to either "Ship from stock" or "Order from supplier". The two paths then meet at a second exclusive gateway before "Close order". Each token that enters leaves once, so the model has no deadlock and no extra tokens.

## Trade-offs

Checking soundness covers control flow only. Naming, layout and other style questions need separate guidelines such as 7PMG.
