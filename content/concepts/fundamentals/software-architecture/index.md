---
title: Software Architecture
slug: software-architecture
category: fundamentals
kind: concept
summary: 'Software architecture is the set of fundamental choices about a system: its parts, how they
  relate, and the reasoning behind them. Definitions differ, but most stress structure, important decisions,
  and the cost of changing them later.'
arc42:
- 1
- 4
- 5
- 9
step: s07-solution-strategy
related:
- implications-of-the-architecture-definition
- software-architecture-basic-concepts
- iso-iec-ieee-42010-architecture-description-standard
- architecture-as-set-of-design-decisions
- architectural-decision
- architecture-decision-rationale
- software-architect-role
- technical-debt
checks:
- The document states the rationale behind the architecture, not only its structure.
- The document separates the architecture itself from the description that documents it.
- The document names the main building blocks, their interfaces and relationships.
- The document states where architectural design ends and detailed design begins.
sources:
- url: https://ics.uci.edu/~arcadia/arcadia_papers/arch/found_abstract.html
  title: 'Arcadia Collected Papers: ABSTRACT'
  site: ics.uci.edu
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/standards/iso-42010
  title: ISO/IEC/IEEE 42010 - Architecture Description | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Software_architecture
  title: Software architecture - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

There is no single agreed definition of software architecture. Several sources describe it from different angles.

**Elements, form and rationale.** An early model splits architecture into three parts: elements, form and rationale. Elements are processing, data or connecting elements. The rationale explains why the architecture looks the way it does. It rests on system constraints, which usually come from requirements. So the "why" is part of the architecture, not only the structure.

**The standard view.** The standard ISO/IEC/IEEE 42010 separates two things. The architecture is the fundamental concepts or properties of the thing being described. The architecture description is a work product made of artifacts that document it. The thing being described is called the "entity of interest". It can be a system, software, an enterprise or something else. See the article ISO/IEC/IEEE 42010 Architecture Description Standard.

**The important stuff.** One well-known view says architecture is about what is important, whatever that turns out to be. The same source also describes it as the shared understanding that expert developers have of the system design.

**Building blocks and decisions.** A software architecture curriculum describes architecture through building blocks, their interfaces and relationships, and through decisions with system-wide consequences. It makes architects responsible for meeting requirements and creating the architecture design.

**Architecture and design.** Architecture is design, but not all design is architectural. The architect decides where architectural design ends and detailed design begins.

**Why it matters.** Architectural choices are costly to change. A poor architecture contributes to the growth of cruft, meaning messy leftovers that make software harder to modify.

## Example

Imagine a small online shop. The team decides that ordering, payment and stock are separate parts. They also decide how those parts exchange data, and they write down why. These choices are architectural, because they are costly to change once implemented. The color of a button is detailed design. The architect decides where that line falls.

## Trade-offs

Definitions differ: one person means structure, another means key decisions, another means shared understanding. The line between architecture and detailed design is a judgment call, so it can move from project to project.
