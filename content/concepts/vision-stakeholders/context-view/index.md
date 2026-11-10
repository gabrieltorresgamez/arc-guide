---
title: Context View
slug: context-view
category: vision-stakeholders
kind: artifact
summary: A context view shows the system as a black box and the world around it. It focuses on what data
  the system exchanges with its environment, so everyone can see where the system starts and ends.
arc42:
- 3
step: s02-scope-context
related:
- arc42-context-and-scope
- business-and-technical-context
- c4-level-1-system-context-diagram
- context-view-antipatterns
- refining-complex-context-views
- contemporary-essential-views
- deployment-diagram
- software-architecture-in-its-context
checks:
- The system appears as a black box with its communication partners around it.
- The domain interfaces state which data are exchanged with the environment.
- Technical interfaces and channels to neighboring systems are documented.
- Risks are marked explicitly in the context.
- Many external systems are grouped by explicit criteria.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/context/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/system-context
  title: System context diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Generic context view: the system as one box, with data labeled on each arrow.'
review:
  status: generated
  flags: []
---

## Explanation

A context view shows how a system sits in its environment. The system itself is a black box. You do not show what is inside. You show the communication partners around it and the interfaces between them.

**Why it matters**

- Domain and technical interfaces to communication partners are among the most critical aspects of a system. The team must understand them fully.
- Context is often left implicit rather than being defined during project initiation or requirements capture. A context view makes it explicit.
- It shows how the system relates to its environment, what it depends on and how the two interact.

**Business and technical context**

The business context shows which data the system exchanges with its environment. All stakeholders should be able to understand it. Diagrams work well, and a table can replace or complement them. See Business and Technical Context for more.

The technical context shows the channels and technical interfaces to neighbors. Many stakeholders base architectural decisions on these interfaces. Infrastructure and hardware designers in particular decide these technical interfaces. A UML deployment diagram can show the channels to neighboring systems.

**Practical advice**

- Mark risks directly in the context.
- If many external systems are involved, group them by explicit criteria.
- Keep detail low. The C4 system context diagram is a zoomed-out picture of the system landscape. It suits technical and non-technical people, inside and outside the team.

For the arc42 chapter that holds this view, see arc42 Context and Scope. For the C4 version, see System Context Diagram.

## Example

A team builds an online booking system. The context view shows one box for the booking system. Around it sit customers, a payment provider and an email service. Each line is labeled with the data exchanged, such as booking requests or payment confirmations. A second view shows the technical channels to each partner. 

## Trade-offs

A context view keeps detail low on purpose. With many external systems, grouping partners by explicit criteria is one way to handle this.
