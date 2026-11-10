---
title: View Creation Method
slug: view-creation-method
category: documentation
kind: method
summary: Every architecture diagram should say which notation it uses, who it is for and why it exists.
  The arc42 building block view and runtime view are two views where this applies.
arc42:
- 5
- 6
step: s10-document
related:
- architecture-view
- architecture-viewpoint
- purpose-of-views
- characteristics-of-a-good-view
- runtime-view
- arc42-documentation-template
- matching-diagram-type-to-system-aspect
- stakeholder-questions-addressed-in-views
checks:
- Each diagram states its notation, its target audience and its purpose.
- The documentation contains a building block view showing the static decomposition of the system.
- The runtime view covers scenarios chosen for their architectural relevance.
sources:
- url: https://socadk.github.io/design-practice-repository/activities/DPR-ArchitectureModeling
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A view is a diagram or description of a system made for a specific reader. When you create one, three details should travel with it:

- the **notation**, meaning the drawing language you used;
- the **target audience**, meaning who the view is for;
- the **purpose**, meaning what the view should help that audience do.

Two views from the arc42 template (see *arc42 Architecture Documentation Template*) show how purpose shapes content:

- **Building block view.** It documents the static decomposition of the system, meaning how it is split into parts. It is mandatory in every architecture documentation.
- **Runtime view.** It shows concrete behavior and the interactions between building blocks. You pick its scenarios by how relevant they are to the architecture.

The two views answer different questions. One shows what the parts are. The other shows what they do together.

## Example

A team draws a diagram of an online shop. Under the diagram they add a short note: "Notation: simple boxes and arrows. Audience: new developers. Purpose: show the main parts of the shop." A second diagram shows how those parts talk to each other while a customer places an order.

## Trade-offs

This article covers only the labeling of diagrams and two arc42 views, not the full process of creating and refining a view.
