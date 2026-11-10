---
title: Boundary Event
slug: attached-boundary-intermediate-event
category: modeling-bpmn
kind: notation-element
summary: A boundary event is attached to the edge of an activity and reacts while that activity runs.
  It can stop the activity or run alongside it. Typical uses are timeouts, reminders, and error handling.
arc42:
- 6
- 8
step: s10-document
related:
- bpmn-event
- intermediate-event
- bpmn-activity
- bpmn-core-elements
- bpmn-compensation-event
- exception-handling
checks:
- Error boundary events in the model are interrupting.
- Timeouts are modeled with interrupting timer boundary events, and reminders with non-interrupting ones.
- Escalations are handled by a catch event in the nearest parent flow scope.
- Escalation is not modeled as an error, and any interrupting escalation boundary event is a deliberate
  choice.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/error-events/
  title: Error events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/timer-events/
  title: Timer events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/escalation-events/
  title: Escalation events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A review task with a non-interrupting reminder timer and an interrupting timeout timer.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A boundary event sits on the edge of a task or subprocess. It watches for something to happen while that activity runs. (See the articles "BPMN Activity" and "BPMN Event" for the basics.)

The event can be interrupting or non-interrupting. An interrupting event ends the activity when it fires. A non-interrupting event does not end the activity.

**Timer boundary events**

- An interrupting timer ends the activity when the timer fires. Modelers often use it for timeouts.
- A non-interrupting timer is often used for notifications, such as reminders. The timer starts when the activity is entered.

**Error boundary events**

An error boundary event is always interrupting. The task is terminated and the flow leaves the regular path.

**Escalation boundary events**

An escalation is not an error. It is non-critical, and execution continues where it was thrown. Only one catch event handles an escalation: the one in the nearest parent flow scope. That catch event can be a boundary event or an event subprocess. An escalation boundary event can optionally be interrupting. In that case it ends the scope it is attached to.

## Example

A "Review application" task has two timer boundary events. A non-interrupting timer sends a reminder to the reviewer when the task has been open for a while. The task keeps running. An interrupting timer fires later and cancels the review. The flow then follows a path that handles the timeout.

## Trade-offs

Interrupting or non-interrupting changes what happens to the running work. An interrupting event ends the activity. A non-interrupting event leaves it running. Escalations can be either, so the modeler must choose. Errors give no such choice: they always interrupt.
