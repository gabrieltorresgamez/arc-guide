---
title: BPMN Compensation Event
slug: bpmn-compensation-event
category: modeling-bpmn
kind: notation-element
summary: A compensation event lets a process undo work that already finished. You mark an activity as
  undoable, link it to an undo task, and trigger compensation later. Only successfully completed activities
  get undone.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-event
- attached-boundary-intermediate-event
- intermediate-event
- bpmn-activity
- bpmn-connecting-object
- bpmn-2-0-notation-overview
checks:
- Each activity that may need undoing has a compensation boundary event attached to it.
- Each compensation boundary event links to exactly one handler through a directed association, not a
  sequence flow.
- The model triggers compensation with a throwing compensation event inside the process scope that holds
  the completed activities.
- Undo of a whole subprocess uses a compensation event subprocess as its handler.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/compensation-events/
  title: Compensation events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.org/manual/7.6/reference/bpmn20/events/cancel-and-compensation-events/
  title: Cancel and Compensation Events | docs.camunda.org
  site: docs.camunda.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/error-events/
  title: Error events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A reservation task can be undone by an associated handler. A payment failure triggers compensation.
review:
  status: generated
  flags: []
---

## Explanation

Some processes run several steps in a row, and a later step can fail. The earlier steps may then need to be undone. A compensation event is the BPMN way to model that undo.

**Marking an activity as undoable.** You attach a compensation boundary event to an activity. It marks the activity as one that may need to be reverted. It also ties the activity to a compensation handler, which is the task that does the undoing. (The article on Boundary Event explains attached events in general.)

**Only completed work is undone.** Compensation applies only to activities that finished successfully. Handlers of activities that are still running, or that were terminated, are not invoked.

**Triggering compensation.** A throwing compensation event starts the undo. It can be an intermediate throw event or an end event. It acts inside its own process scope. There it triggers the handlers of the completed activities.

**Related interrupting events.** An error boundary event is always interrupting. The failing task is terminated and the regular flow stops.

## Example

A travel process reserves a rental car, then charges the customer. The car reservation has a compensation boundary event. The event is associated with a task called "Cancel car reservation". If the payment task fails, an error boundary event stops it. The flow then reaches a throwing compensation end event. The reservation had completed, so its cancel task runs. If the reservation had never finished, its cancel task would not run.

## Trade-offs

The model does not need to name each activity to undo. It relies on completed activities having handlers. Compensation also covers only completed activities. Handlers of running or terminated ones are not invoked.
