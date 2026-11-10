---
title: Concern
slug: concern
category: forces-decisions
kind: concept
summary: A concern is something a stakeholder cares about in a system, such as performance, security or
  maintainability. Concerns shape architecture, can conflict, and must be explicitly addressed in the
  architecture description.
arc42:
- 1
- 4
- 9
- 10
step: s01-goals-stakeholders
related:
- stakeholder
- stakeholder-concern
- architecture-viewpoint
- architecture-view
- separation-of-concerns
- iso-iec-ieee-42010-architecture-description-standard
- architectural-decision-record
- arc42-introduction-and-goals
checks:
- Stakeholder concerns are explicitly addressed in the architecture description.
- Conflicting concerns, such as time-to-market versus maintainability, are named, and the chosen trade-off
  is explicit.
- The reasoning behind resolving concern conflicts is recorded in Architecture Decision Records.
- The quality goals of the most important stakeholders are known and documented.
sources:
- url: https://quality.arc42.org/standards/iso-42010
  title: ISO/IEC/IEEE 42010 - Architecture Description | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://archman.dev/docs/foundational-concepts/what-is-software-architecture/stakeholders-and-concerns
  title: Stakeholders & Concerns | ArchMan
  site: archman.dev
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Concern_(computer_science)
  title: Concern (computer science) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/stakeholders/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How concerns relate to stakeholders, viewpoints and views.
review:
  status: generated
  flags: []
---

## Explanation

A concern is an interest that a stakeholder has in the system. Stakeholders are the people or groups with a stake in it. Typical concerns are performance, security and maintainability.

**Concerns in the architecture description**

The ISO/IEC/IEEE 42010 standard asks that stakeholder concerns be explicitly addressed in the architecture description. See the article ISO/IEC/IEEE 42010 Architecture Description Standard.

Concerns also connect to views. A viewpoint defines which stakeholders, concerns and modeling techniques are used to build a view. A view then shows the architecture from that viewpoint.

**Concerns drive decisions**

arc42 says the quality goals of the most important stakeholders influence fundamental architectural decisions. Knowing these goals early therefore matters.

Rozanski and Woods classify stakeholders by their roles and concerns. They also say the architect must ensure adequate stakeholder representation.

**Where the word comes from**

Dijkstra coined the term separation of concerns. There, a concern is any aspect of software that can be defined separately from other aspects. See the article Separation of Concerns.

**Conflicting concerns**

Concerns can conflict. Time-to-market can pull against long-term maintainability. The architect should then facilitate explicit trade-off choices. One way is a time-boxed workshop. The reasoning is then recorded in Architecture Decision Records.

## Example

A team builds an online ticket shop. The operations manager worries about the site staying fast during sales. The product owner wants a launch in three months. The developers want code that stays easy to change.

The launch date and easy-to-change code pull in different directions. The architect brings these people together in a short workshop. They agree on a choice and write down why. Each concern is then addressed in the architecture description.

## Trade-offs

Favoring one concern, such as time-to-market, can cost another, such as long-term maintainability. Making the trade-off explicit, in a workshop and a written decision record, takes time. It avoids hidden choices.
