---
title: Process Manager
slug: process-manager
category: integration
kind: pattern
summary: A Process Manager is a central component that tracks the state of a process and decides the next
  processing step. It fits cases where the needed steps are not known in advance.
arc42:
- 5
- 6
- 8
- 9
step: s08-integration-data
related:
- routing-slip
- content-based-router
- pipes-and-filters
- dynamic-router
- composite-message-processor
- messaging-pattern-language
- message-routing
- workflow-pattern
checks:
- The document states why a fixed sequence of steps does not work before it introduces a Process Manager.
- The document names the central unit that keeps the state of the sequence and decides the next step.
- The document addresses the risk that the central manager becomes a performance bottleneck or a point
  of failure.
- The document explains why a Process Manager was chosen over choreography, or the reverse.
- The document limits the Process Manager to cases that need it, not every flow.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html
  title: Process Manager - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
  title: Saga Design Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A Process Manager sends work to steps and picks the next step from each result.
review:
  status: generated
  flags: []
---

## Explanation

Sometimes a message must pass through several processing steps, but the design cannot say in advance which steps are needed. The route may depend on results from earlier steps. The Process Manager pattern handles this case.

The solution is one central unit, the Process Manager. It keeps track of the state of the sequence. After each step, it decides what happens next.

**Compared with Routing Slip.** A Routing Slip (see the article "Routing Slip") assumes two things. The steps are fixed up front, and they run in a line. If routing depends on intermediate results, those assumptions fail. A Process Manager is meant for that situation.

**Compared with saga orchestration.** A saga splits a long operation into steps across several participants. In the orchestrated form, a central orchestrator tells each participant what to do. It stores and interprets the state of each task. It also handles failure recovery with compensating transactions, which are steps that undo earlier work.

## Example

An order arrives. The Process Manager first asks for a credit check. If the check passes, it asks for stock reservation. If the check fails, it asks for a manual review instead. The route is chosen from the earlier result, not fixed in advance. The manager remembers where the order stands after each step.

## Trade-offs

The central control element has downsides.

- **Bottleneck.** All routing decisions pass through one unit. It can become a performance bottleneck.
- **Overkill.** Using a Process Manager for every situation may be too much. It can add performance overhead.

The other saga approach is choreography. Services exchange events without a centralized controller, so it does not introduce a single point of failure. The responsibilities are spread across the participants. The price is that the flow is harder to track and test.

Orchestration suits complex workflows. Because the orchestrator manages the flow, it also avoids cyclic dependencies.
