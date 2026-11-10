---
title: BPMN Ad Hoc Sub-Process
slug: bpmn-ad-hoc-sub-process
category: modeling-bpmn
kind: notation-element
summary: An ad hoc sub-process groups activities that have no fixed order. Each activity can run several
  times, in any order, or be skipped. The choice happens at runtime, not at design time.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-activity
- bpmn-2-0-notation-overview
- bpmn-core-elements
- bpmn-event
- process-model-versus-process-instance
- bpmn-gateway-semantics
- adaptability
checks:
- Ad hoc sub-processes in the model contain no start or end events.
- 'The model states who chooses the inner activities at runtime: the engine via an expression, or a job
  worker.'
- Where no completion condition is defined, the team knows the sub-process ends once all activated elements
  are done.
- Free-form work is modeled with an ad hoc sub-process only where order is truly decided at runtime, not
  at design time.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/ad-hoc-subprocesses/
  title: Ad-hoc sub-processes | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/building-flexibility-into-bpmn-models/
  title: Building flexibility into BPMN models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://www.omg.org/cmmn/
  title: Case Management Model and Notation™ (CMMN™) | Object Management Group
  site: omg.org
  accessed: '2026-11-09'
- url: https://camunda.com/blog/2025/12/orchestrating-messy-middle-case-work/
  title: 'Orchestrating the Messy Middle of Case Work: Highlights From Our New Whitepaper | Camunda'
  site: camunda.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: An ad hoc sub-process with three activities and no sequence flows between them.
review:
  status: generated
  flags: []
---

## Explanation

Most process models fix the order of steps in advance. Some work does not fit that mold. A BPMN ad hoc sub-process (see BPMN Activity) is a container for such work. It holds a set of activities, and the order is left open.

**What "open" means**

- Each inner element can run several times, in any order, or not at all.
- By default, no sequence flows connect the inner activities.
- Which activities run, in what order, and how often is decided at runtime, not at design time.
- The inner elements are not connected to a start or end event. An ad hoc sub-process must not contain them.

**Who decides**

Open sequencing does not mean no control. In Camunda's BPMN, the engine can decide, based on an expression in the model. A job worker, which is code that handles work on behalf of the engine, can also decide. Camunda can run an ad hoc sub-process internally in its engine Zeebe, or through a job worker.

**When it ends**

If the model defines no completion condition, the sub-process finishes after all activated elements are done.

**Alternative for free-form work**

CMMN is an OMG standard for cases whose activities may happen in an unpredictable order. OMG states that combining BPMN and CMMN covers a much broader range of work methods. That supports using CMMN next to BPMN for free-form work.

**Typical use**

Camunda proposes ad hoc sub-processes for agent-driven or flexible work. In that work, people add or remove tasks as circumstances change.

## Example

A support team handles a complaint. The ad hoc sub-process holds "call the customer", "check the order history", "request a refund" and "escalate to a manager". The case worker picks what the situation needs. They may call the customer twice and skip the refund. When all activated tasks are done, the sub-process ends.

## Trade-offs

**Benefits:** the model fits work where the steps cannot be known in advance. People or software can add or remove tasks as circumstances change.

**Costs:** the order of work is not fixed at design time, because it is decided at runtime, although related inner elements can still be connected by sequence flow. Control moves to an engine expression or a job worker. OMG describes BPMN and CMMN as complementary, and combining them covers a broader range of work methods.
