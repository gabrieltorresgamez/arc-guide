---
title: Architectural Overview Diagram
slug: architectural-overview-diagram
category: documentation
kind: artifact
summary: An architectural overview diagram shows the inside of a system at a high level, together with
  the users and other systems it talks to. It records the early, big solution decisions and gives a base
  that other diagrams refine.
arc42:
- 3
- 4
- 5
step: s10-document
related:
- c4-container-diagram
- context-view
- arc42-context-and-scope
- arc42-solution-strategy
- architectural-overview-antipatterns
- c4-model
- component-view
checks:
- The overview diagram includes all external interfaces to human users and other systems.
- The diagram shows building blocks inside the system, not only its external dependencies.
- The diagram stays abstract and does not disclose implementation details.
- All communication partners (users, IT systems) are specified in the context section the overview draws
  on.
sources:
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-OverviewDiagram.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/activities/DPR-ArchitectureModeling.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/container
  title: Container diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://leanpub.com/read/arc42byexample/chapter-v
  title: V - DokChess — arc42 by Example
  site: leanpub.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.c4.puml
  caption: 'Generic overview: internal parts plus external users and systems.'
review:
  status: generated
  flags: []
---

## Explanation

An architectural overview diagram is a high-level picture of a system. It shows the main building blocks inside the system. It also shows the people and other systems outside it. Zimmermann's Design Practice Repository calls it a container diagram. It records the outcome of the early, big solution-strategy decisions (see the article Solution Strategy).

**How it differs from a context diagram.** A context diagram shows only the outside: external dependencies, used for scope control and risk management. In the repository, it comes first. The overview diagram goes further. It looks inside the system. It still includes all external interfaces with human users and other systems. So it combines internal structure with context.

**What it shows.**

- Logical and physical building blocks, at a high level. Other diagrams then refine them.
- Every external interface to users and other systems.
- Client-server splits, such as a Remote User Interface or Distributed Presentation.

**Relation to other models.** The C4 container diagram is a simple, high-level, technology-focused view of the shape of the architecture and major technology choices. It corresponds to the overview diagram (see Container Diagram (C4 Level 2)).

**Relation to arc42.** Section 3 delimits the system from all its communication partners. It also asks you to specify those partners, both users and IT systems. Section 5 includes an overview diagram of the whole system at level 1. It stresses abstraction without disclosing implementation details. The DokChess example chapter gives an architectural overview so readers can understand its important design decisions.

## Example

A small online shop might draw a box for the system. Inside the box sit a web front end and a backend service. Outside the box sit customers, a payment provider and a shipping provider. Arrows connect customers to the front end, and the backend to the two providers. The diagram stays at this coarse level. It leaves out code and server details.

## Trade-offs

The diagram should use a single, consistent level of abstraction and refinement, and should explain which elements it includes and why.
