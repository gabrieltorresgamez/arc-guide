---
title: Software Architecture Basic Concepts
slug: software-architecture-basic-concepts
category: fundamentals
kind: concept
summary: Software architecture is the set of design decisions about a system's overall structure and behavior.
  Business needs and quality goals drive it. A system has a boundary, and its building blocks are organized
  in levels.
arc42:
- 1
- 3
- 5
- 12
step: s01-goals-stakeholders
related:
- software-architecture
- architecture-as-set-of-design-decisions
- arc42-introduction-and-goals
- arc42-context-and-scope
- arc42-quality-chapter
- stakeholder
- architecture-view
- layers-pattern
checks:
- The document states the requirements and driving forces the architecture must consider.
- Quality goals are few, tied to major stakeholders, and kept separate from project goals.
- The system is explicitly demarcated from its environment.
- The building block view shows the decomposition as a hierarchy of black boxes and white boxes.
sources:
- url: https://www.sei.cmu.edu/software-architecture/
  title: Software Architecture | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Needs drive the architecture; the system boundary separates the building blocks from the environment.
review:
  status: generated
  flags: []
---

## Explanation

**Architecture as decisions and structure.** A system's software architecture captures the design decisions about how the system as a whole is structured and how it behaves. It helps stakeholders (people with an interest in the system) understand and analyze how the system will reach its essential qualities. Documenting architecture also means describing its elements and how they relate to each other, aimed at key qualities. That is the structural side. See *Software Architecture* and *Architecture as Set of Design Decisions*.

**Requirements drive architecture.** A system is created or changed to support a business activity. The requirements and driving forces that architects must consider belong in the introduction and goals section of an arc42 document (see *arc42 Introduction and Goals*).

**Quality goals.** Quality goals for the architecture are the few that matter most to major stakeholders. They shape fundamental decisions. They are not necessarily identical to project goals, so do not confuse the two.

**System and boundary.** A system sits in an environment. arc42 advises you to demarcate the system explicitly from that environment. The line you draw is the system boundary. See *arc42 Context and Scope*.

**Building blocks.** Inside the boundary, the system is split into building blocks. The arc42 building block view shows this static decomposition. The blocks form a hierarchy of black boxes and white boxes. Each level zooms into the blocks of the level above.

## Example

A company builds an online shop to sell more products. That business need drives the architecture. The team names two quality goals that matter most to the major stakeholders. They draw a boundary around the shop and show payment providers and customers as its environment. Inside the boundary, they split the shop into a few blocks. They then zoom into one block to show its parts.

## Trade-offs

This article covers only the basic terms. Other sources may use these terms differently, and this article does not compare them.
