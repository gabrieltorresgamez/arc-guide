---
title: Software Architect
slug: software-architect-role
category: fundamentals
kind: concept
summary: A software architect links business goals and technical work. They decide what matters, weigh
  trade-offs, talk with people at every level of the organization, and stay close to the building of the
  system.
arc42:
- 1
- 3
- 9
step: s01-goals-stakeholders
related:
- architect-knowledge-and-tasks
- software-architecture
- stakeholder
- architectural-trade-off-thinking
- architecture-view
- architectural-thinking
- common-architect-mistakes
- architectural-decision
checks:
- The document names who acts as architect and who is responsible for meeting requirements and the architecture
  design.
- The architecture is communicated to stakeholders through views and patterns.
- The consequences of key trade-offs are made visible to stakeholders at several organizational levels.
- The architect takes part in implementation and checks that code and architecture are consistent.
sources:
- url: https://martinfowler.com/articles/architect-elevator.html
  title: The Architect Elevator — Visiting the upper floors
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://www.isaqb.org/blog/the-profession-of-software-architecture/
  title: The Profession of “Software Architecture” - iSAQB® - Official Website
  site: isaqb.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A software architect is responsible for meeting requirements and for creating the architecture design of a solution. See *Software Architecture* for what the architecture itself is.

**Bridging two worlds.** One view says the architect's primary role is to ride the "elevator" between the executive penthouse and the engine room. Architects must engage with the upper floors of the organization, not only technical levels, for example to unblock or trigger organizational change. Finding the appropriate context also requires visiting many floors of the organization.

**Making trade-offs visible.** An architect's job includes making the ramifications of choices transparent. It also includes involving all levels of the organization in the trade-off. A trade-off means gaining one benefit by giving up another. See *Quality Attribute Trade-off*.

**Knowing what is important.** Architecture is about the important stuff, and the architect must recognize what is important. A developer who wants to become an architect needs to be able to recognize what is important.

**Experience.** One recommendation is to spend several years programming and working actively in software development. That gives the necessary instinct to recognize and navigate uncertainties and risks in design and architecture.

**Communication.** Architects deal with many stakeholder groups, meaning people with an interest in the system. The better an architect adapts to their languages and goals, the better the decisions will be. Architects communicate and document the architecture using views and patterns. See *Architecture View* and *Architectural Pattern*.

**Staying involved in building.** Architects get feedback by being directly involved in, and accountable for, delivery. They also accompany implementation and check that source code and architecture stay consistent.

## Example

A company wants a new customer portal. The manager talks about faster sign-up and lower support cost. The developers talk about databases and deadlines. The architect talks with both. They explain to the manager what each option costs in time and flexibility. They explain to the developers which goals matter most. Later, the architect joins the team during delivery and checks that the code still follows the agreed design.

