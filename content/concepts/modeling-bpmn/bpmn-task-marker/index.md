---
title: BPMN Task Marker and Task Type
slug: bpmn-task-marker
category: modeling-bpmn
kind: notation-element
summary: 'Task types say what kind of work a BPMN step is, such as service, script, or manual. Markers
  add repetition or compensation behavior. Tool support differs: Camunda 7 does not natively support the
  loop marker.'
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-activity
- bpmn-compensation-event
- bpmn-gateway-semantics
- bpmn-ad-hoc-sub-process
- bpmn-core-elements
- bpmn-2-0-notation-overview
checks:
- Each loop in a model targeting Camunda 7 is modeled explicitly (for example with gateways), not with
  the loop marker.
- Each multi-instance activity is clearly drawn as parallel (vertical lines) or sequential (horizontal
  lines).
- Each compensation handler is linked by association and triggered by a compensation event, not reached
  by sequence flow.
- Manual tasks are used only for work that needs no external tooling or UI, since the engine passes through
  them.
sources:
- url: https://docs.camunda.org/manual/7.24/reference/bpmn20/tasks/task-markers/
  title: Task Markers | docs.camunda.org
  site: docs.camunda.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/script-tasks/
  title: Script tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/service-tasks/
  title: Service tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/manual-tasks/
  title: Manual tasks | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/multi-instance/
  title: Multi-instance | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A parallel multi-instance service task followed by a script task and a manual task.
review:
  status: generated
  flags: []
---

## Explanation

A BPMN task is one step in a process model. Two kinds of small symbols refine it: **types** and **markers**. The BPMN Activity article covers the wider idea of tasks and activities.

**Task types**

- **Service task:** a work item with a specific type. When the process reaches it, the engine creates a job for a worker to pick up.
- **Script task:** models the evaluation of a script. By default the engine evaluates a FEEL expression; other implementations need a job worker.
- **Manual task:** a person does the work without external tooling or a user interface. The engine simply passes through it.

**Multi-instance marker**

Multi-instance repeats a step. It comes in two forms:

- **Sequential:** drawn with three horizontal lines at the bottom of the activity.
- **Parallel:** drawn with three vertical lines. All instances are created when the activity starts. They run at the same time, independently of each other.

In Camunda 8, parallel is the default.

**Loop marker**

Camunda 7 does not natively support the loop marker. If you use that engine, model the loop explicitly in your BPMN process.

**Compensation marker**

Compensation handlers sit outside the regular flow. They run only when a compensation event is thrown. An association links them, not a sequence flow. The BPMN Compensation Event article covers the event side.

## Example

An order process has a parallel multi-instance service task named "Reserve item". Each order line gets its own instance. All instances start together and run independently. A script task then totals the prices. A manual task, "Pack parcel", follows. A person does it, and the engine passes straight through.

## Trade-offs

Check the target engine before you use a marker. Camunda 7 lacks native loop support, so a loop there needs explicit modeling. Parallel multi-instance runs all instances at once and independently. Sequential multi-instance is the other choice when you want repetition one instance at a time.
