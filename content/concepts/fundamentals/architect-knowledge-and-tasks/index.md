---
title: Role of the Software Architect
slug: architect-knowledge-and-tasks
category: fundamentals
kind: concept
summary: A software architect makes the big design decisions for a system and leads the teams that build
  it. The role needs technical skill, communication skill, and hands-on involvement in delivery.
arc42:
- 1
- 4
- 9
step: s09-decisions
related:
- software-architect-role
- architectural-decision
- architecture-view
- quality-attribute
- stakeholder
- accountability
- common-architect-mistakes
- software-architecture
checks:
- Architectural decisions are documented together with their justification.
- The architect's scope of decision authority is defined.
- The architecture is described in views that address stakeholder concerns.
- Cross-cutting concerns such as persistence, communication and GUI have an explicit decision.
- Architectural activities trace back to specific qualities to achieve or improve.
sources:
- url: https://learn.microsoft.com/en-us/archive/blogs/dave_langer/architecture-as-leadership
  title: Architecture as Leadership | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/architect-elevator.html
  title: The Architect Elevator — Visiting the upper floors
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A software architect is responsible for meeting the requirements and creating the architecture design of a solution. Depending on the approach or process model, they must align this responsibility with the overall project responsibility of project management or other roles.

**What the architect decides**

Architecture means the "big decisions": how the software is structured, which frameworks and technologies it uses, and which patterns it follows. It also covers how functional and non-functional requirements are met. Architects decide how to split the system into building blocks. They also decide on cross-cutting concerns, such as persistence, communication and the user interface.

The need to reach or improve specific qualities should guide architectural work. See the article Quality Attribute.

**Making decisions visible**

Architects make, justify, communicate and document their decisions in a systematic way. They coordinate refinements of requirements with stakeholders. They also describe the architecture through views that address stakeholder concerns. See Architectural Decision and Architecture View.

**Leadership**

One author argues that the most basic responsibility is technical leadership of the teams the architect works with. Within their defined scope, the architect is the final arbiter of architectural decisions, and developers are bound by them. Even so, architects should keep solo decrees to a minimum and rely on consensus.

Technical expertise is necessary but not enough. Nobody can be an expert in everything. Architects therefore also need interpersonal communication and consensus-building skills.

**Hands-on, not ivory tower**

Good architects keep their coding and delivery skills sharp. They mentor the team and listen to developers. The industry still often sees architects as "ivory tower" figures who offer little practical value or act as roadblocks. Hohpe describes the setup where architects sit in a penthouse and define how developers build, without developing software themselves, as a well-known anti-pattern, because it gives the architects no feedback on the effectiveness or cost of their decisions. Hohpe calls being directly involved in, and accountable for, delivery a great way for architects to get feedback.

**Role versus title**

One view holds that most of what architects traditionally did should be done by developers, by tools, or not at all.

## Example

A team builds an online booking system. The architect splits it into building blocks and picks how they communicate. They write down why, and show the decisions to stakeholders in simple views. They sit with developers, write some code themselves, and listen to concerns. When the team disagrees, they seek consensus first. They make the final call only inside their agreed scope.

## Trade-offs

Being involved in and accountable for delivery gives architects feedback on their decisions. Tools and developers can take over much traditional architect work, and many companies drop the separate job title.
