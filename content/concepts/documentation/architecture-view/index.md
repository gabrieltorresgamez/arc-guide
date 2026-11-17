---
title: Architecture View
slug: architecture-view
order: 30
category: documentation
kind: concept
summary: An architecture view shows one side of a system's design. It shows how the architecture addresses
  the concerns of specific stakeholders, the people with an interest in the system.
arc42:
- 5
step: s10-document
related:
- architecture-viewpoint
- stakeholder-concern
- concern
- stakeholder
- essential-architecture-views
- architecture-view-model
- iso-iec-ieee-42010-architecture-description-standard
checks:
- The documentation includes a building block view of the system's static structure.
- Each view states which stakeholder concerns it addresses.
- Each view is built with the patterns, templates and conventions of a named viewpoint.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1766161&seqNum=4
  title: 'The Benefits of Using Viewpoints and Views | Software Systems Architecture: Viewpoints and Views
    | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How stakeholders, concerns, viewpoints and views relate.
review:
  status: generated
  flags: []
---

## Explanation

The architecture description is split into several views. Each view shows how the architecture deals with one or more concerns.

A view follows a viewpoint. A viewpoint is a set of patterns, templates and conventions for building one type of view. It also names the stakeholders whose concerns it reflects. The viewpoint is the recipe. The view is the result of following it.

Rozanski and Woods offer a catalog of viewpoints for information systems. It includes six core viewpoints:

- Functional
- Information
- Concurrency
- Development
- Deployment
- Operational

The arc42 template includes a view as well. Its building block view shows the static structure of the system. arc42 compares it to the floor plan of a house. arc42 also requires it in every architecture documentation.

See the articles "Architecture Viewpoint", "Stakeholder Concern" and "Essential Architecture Views" for more detail.

**More about views.**

- **Architectural View:** An architectural view addresses one or more concerns of one or more stakeholders. Splitting the description into views keeps each part understandable and lets each reader find what matters to them.

## Example

Imagine an online shop. The operations team asks where the system runs. A new developer asks which parts exist and how they connect. Each group gets a view that answers its own questions. Both views describe the same shop.
