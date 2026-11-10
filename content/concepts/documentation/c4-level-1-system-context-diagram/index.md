---
title: System Context Diagram
slug: c4-level-1-system-context-diagram
category: documentation
kind: artifact
summary: A system context diagram shows one software system as a single box. Around it sit the people
  and other systems it works with. Technical and non-technical readers can both follow it, so it makes
  a good first diagram.
arc42:
- 3
step: s02-scope-context
related:
- context-view
- business-and-technical-context
- arc42-context-and-scope
- c4-model
- c4-container-diagram
- context-view-antipatterns
- context-view-antipattern-forgetting-bidirectional-data-flows
- refining-complex-context-views
checks:
- The diagram shows the system as one box surrounded by its users and the external systems it interacts
  with.
- The diagram focuses on people and software systems, not technologies.
- Neighbouring systems are drawn outside the system boundary, so the scope is clear.
- Stakeholders can see which data is exchanged with the environment.
sources:
- url: https://c4model.com/diagrams/system-context
  title: System context diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/context/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.c4.puml
  caption: 'Generic context diagram: one system, one user, one external system.'
review:
  status: generated
  flags: []
---

## Explanation

A system context diagram shows your system as one box in the centre. Around the box you draw its users and the other systems it interacts with.

**Scope.** The diagram covers a single software system. Neighbouring systems usually sit outside its boundary.

**Focus on people and systems.** Show people, such as actors, roles and personas, and show software systems. Do not focus on technologies. Keep the detail low.

**Audience.** Everyone can read it: technical and non-technical people, inside and outside the development team.

**Relationship to other ideas.**
- In the C4 model, this diagram is a good starting point for documenting a system. C4 recommends it for all software development teams.
- arc42 section 3 (Context and Scope) separates the system's scope from all its communication partners and specifies its external interfaces. In arc42, the *business context* aims for all stakeholders to understand which data the system exchanges with its environment. arc42 accepts any kind of diagram that treats the system as a black box and specify the domain interfaces to its communication partners. The *technical context* covers the technical interfaces, meaning the channels and transmission media that link the system to its environment.
- The Context viewpoint also covers the relationships, dependencies and interactions between the system and its environment. Among its concerns are the external entities, the data used, and the system's impact on its environment.

## Example

An online library lending system is drawn as one box in the middle. Readers and librarians are people placed around it. A payment service and a book catalog provider are external systems placed around it too. Each line carries a short label, such as "pays fines" or "looks up book details". Nothing inside the box is shown.

## Trade-offs

The diagram keeps detail low on purpose. It shows who and what the system talks to, but not technologies or internals.
