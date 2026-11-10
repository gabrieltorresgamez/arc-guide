---
title: 'Context View Antipattern: Forgetting Bidirectional Data Flows'
slug: context-view-antipattern-forgetting-bidirectional-data-flows
category: vision-stakeholders
kind: concept
summary: A context diagram goes wrong when it draws one-way arrows for exchanges that run both ways. The
  missing direction hides what data the system must send, receive and handle, so interfaces end up under-specified.
arc42:
- 3
step: s02-scope-context
related:
- context-view
- context-view-antipatterns
- business-and-technical-context
- arc42-context-and-scope
- refining-complex-context-views
- c4-level-1-system-context-diagram
- provided-and-required-interface
checks:
- Every external neighbor with two-way exchange shows both directions, as two arrows or one annotated
  arrow.
- Each flow is labeled with the data exchanged, and a legend states what arrows mean.
- The business context shows data flows, not dependencies.
- Each domain interface is linked to its technical channel in the technical context.
- All external neighbors appear, individually or as a documented group.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/3-11/
  title: 'Tip 3-11: In the business context, show data flows (instead of dependencies)! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/3-5/
  title: 'Tip 3-5: Restrict the context to an overview, avoid too many details! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams
  title: Create architecture design diagrams - Microsoft Azure Well-Architected Framework | Microsoft
    Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Two labeled flows show both directions of the exchange with an external payment service.
review:
  status: generated
  flags: []
---

## Explanation

A context diagram shows your system as a black box surrounded by users and external systems.

**Why arrows cause trouble.** Many people read an arrow between systems as data flow. Directed UML relationships such as dependency or association can confuse non-technical readers. For this reason, arc42 suggests showing data flows rather than dependencies in the business context, mainly for information systems. It notes that this advice is controversial in some teams.

**What gets hidden.** Section 3 of arc42 wants all stakeholders to understand which data the system exchanges with its environment. Domain and technical interfaces to communication partners are among the most critical aspects of a system.

**Business and technical context.** The business context shows what data is exchanged. The technical context shows the channels and transmission media that link the system to its environment. arc42 advises relating each domain interface to its technical realization.

**How to draw it.** Azure guidance offers two options for two-way communication:
- Show two separate arrows, one per direction. This is the preferred option.
- Annotate a single arrow with request and response notes.

Label lines when their meaning is not obvious, and add a legend if you introduce line semantics.

The same guidance warns against double-headed arrows. They imply bidirectional dependencies, and it suggests arrows from the initiating component to the dependency. Be consistent in how relationships are represented.

Keep detail low. arc42 asks you to document all external neighbors, but grouping them is fine.

## Example

An online shop draws one arrow from "Shop" to "Payment Service", labeled "payment request". The diagram looks complete.

In reality, the payment service also returns a result: approved, declined or failed. The shop must handle each outcome. The diagram shows no return flow.

The fix is a second arrow back to the shop, labeled "payment result". Now the interface shows two separate data flows, which is the preferred way to show two-way communication.

## Trade-offs

arc42 allows grouping neighbors to keep the view readable.

Double-headed arrows look tidy but can wrongly suggest two-way dependencies. If you introduce your own arrow or line semantics, explain them in a legend.
