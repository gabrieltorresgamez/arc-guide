---
title: BPMN Activity
slug: bpmn-activity
order: 20
category: modeling-bpmn
kind: notation-element
summary: A BPMN activity is a unit of work in a process. It can be a single task or a subprocess that
  groups further steps. Call activities reuse separate processes, and markers show repetition.
arc42:
- 6
step: s10-document
related:
- bpmn-event
- bpmn-core-elements
- purpose-of-process-analysis-and-modeling
- bpmn-2-0-notation-overview
checks:
- Reusable process logic is modeled as a call activity, not as a collapsed subprocess.
- Each embedded subprocess has exactly one none start event.
- Each event subprocess is marked clearly as interrupting or non-interrupting.
- 'Multi-instance activities show the correct marker: horizontal lines for sequential, vertical lines
  for parallel.'
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/call-activities/
  title: Call activities | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/multi-instance/
  title: Multi-instance | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/event-subprocesses/
  title: Event subprocess | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/embedded-subprocesses/
  title: Embedded subprocess | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/service-tasks/
  title: Service tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
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
- url: https://docs.camunda.org/manual/7.24/reference/bpmn20/tasks/task-markers/
  title: Task Markers | docs.camunda.org
  site: docs.camunda.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/script-tasks/
  title: Script tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/manual-tasks/
  title: Manual tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A process with a collapsed-style embedded subprocess, a call activity and a parallel multi-instance
    task.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

An activity is a piece of work in a process model. This article covers several kinds.

**Embedded subprocess.** It groups process elements inside the parent process. It must have exactly one none start event.

**Collapsed subprocess.** The diagram hides its inner steps to reduce complexity. This is for display only. It does not make the content reusable.

**Call activity.** It invokes another process that is stored as a separate BPMN file. Several processes can invoke that file. For reusable processes, call activities are the recommended choice.

**Event subprocess.** It sits inside its scope, much like a boundary event (see the article BPMN Event). A boundary event is attached to the edge of an activity. An event subprocess can be interrupting or non-interrupting. An interrupting one fires only once and ends the active instances of its containing scope. A non-interrupting one can fire many times.

**Multi-instance markers.** A multi-instance activity runs several times, either in sequence or in parallel. Three horizontal lines at the bottom mean sequential. Three vertical lines mean parallel. In the parallel case, all instances are created when the multi-instance body activates.

**Task types.** A service task is a work item with a specific type.

**More about activities.**
- **Task types and markers** refine a task. Examples of types are the service task (the engine creates a job for a worker), the script task and the manual task (a person does the work without tooling). The multi-instance marker repeats a step, sequentially (three horizontal lines) or in parallel (three vertical lines).
- **Ad hoc sub-process:** a container for work whose order is left open. Each inner activity can run several times, in any order, or not at all, and the order is decided at runtime.

## Example

An order process contains a step "Check customer". Its inner steps sit behind a collapsed subprocess, so the main diagram stays readable. "Calculate shipping" is a call activity, and other processes call the same stored shipping process. "Pack item" carries a parallel multi-instance marker, so all items in an order are packed at once. A non-interrupting event subprocess answers "customer asks for status" as often as needed.

## Trade-offs

A collapsed subprocess keeps a diagram simple, but it is for display only. It gives no reuse. A call activity gives reuse across processes, but the logic lives in a separate file. An interrupting event subprocess ends the active work in its scope and fires only once. A non-interrupting one can fire repeatedly.
