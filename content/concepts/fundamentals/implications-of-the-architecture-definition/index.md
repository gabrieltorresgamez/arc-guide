---
title: Software Architecture Definition
slug: implications-of-the-architecture-definition
category: fundamentals
kind: concept
summary: Definitions of software architecture differ. One says it is the design decisions about a system's
  overall structure and behavior. Another calls it the important stuff, or the expert developers' shared
  understanding of the design.
arc42:
- 1
- 4
step: null
related:
- software-architecture
- architecture-as-set-of-design-decisions
- software-architecture-basic-concepts
- iso-iec-ieee-42010-architecture-description-standard
- architectural-decision
- architecture-facts-and-challenges
checks:
- The document states which definition of architecture the team uses, such as design decisions about overall
  structure and behavior.
- The document describes the system's components, connectors, constraints and rationale.
- The document makes clear which parts of the system the team treats as important.
sources:
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/software-architecture/
  title: Software Architecture | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/the-software-architecture-renaissance/
  title: The Software Architecture Renaissance | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

There is no single definition of software architecture. The sources here describe it in three ways.

**Design decisions about structure and behavior.** The Software Engineering Institute (SEI) says a system's architecture represents the design decisions about its overall structure and behavior.

**The important stuff.** Martin Fowler, citing Ralph Johnson, says architecture is about the important stuff, whatever that is. Fowler says the heart of thinking architecturally is deciding what is important.

**Shared understanding.** Johnson also describes architecture as the expert developers' shared understanding of the system design.

**An older, looser SEI wording.** An early SEI article described architecture as the organizational structure of a software system. That structure includes components, connectors, constraints and rationale.

## Example

A team builds an online shop. One member lists the decisions made: split the system into a catalog part and an order part, and set how they exchange data. That matches the SEI view. Another member says the architecture is whatever the team agrees matters most, such as keeping orders safe. That matches the "important stuff" view. A third member says it is what the experienced developers all understand about how the shop is built. That matches the shared-understanding view.

## Trade-offs

- The early SEI wording is described as loose, and a more formal definition was being worked on.
