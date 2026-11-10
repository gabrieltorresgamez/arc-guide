---
title: Requirements and Means Influence Architecture
slug: requirements-and-means-influence-architecture
category: fundamentals
kind: concept
summary: Requirements shape architecture, and constraints limit the architect's choices. Architects need
  to know which decisions are free and which are bound, and they need to learn key stakeholders' quality
  goals early.
arc42:
- 1
- 2
- 4
- 10
step: s05-constraints
related:
- architecturally-significant-requirement
- requirements-versus-constraints
- arc42-constraints
- architecture-means
- twin-peaks-model
- quality-attribute
- arc42-introduction-and-goals
- stakeholder
checks:
- The document names the quality goals of the most important stakeholders.
- The document lists constraints and shows where the architect is free to decide.
- Each constraint is marked as fixed or negotiable.
- Organization-wide constraints are identified separately from system-specific ones.
- Key architectural decisions are justified by architecturally significant requirements.
sources:
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecturally_significant_requirements
  title: Architecturally significant requirements - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Two things shape a system's architecture: what the system must achieve, and what limits the architect's choices.

**Requirements as a driver.** Some requirements affect the architecture more than others. An *architecturally significant requirement* has a measurable effect on a system's architecture. Architects use these requirements to drive their decisions and to justify them later. See the article Architecturally Significant Requirement.

Quality goals matter especially. These are goals such as speed or reliability. The quality goals of the most important stakeholders (people with a stake in the system) influence the most fundamental architectural decisions. So architects should learn these goals early.

**Constraints as a limit.** A constraint narrows what the architect may do. Architects should know exactly where they are free to decide and where they must follow a constraint. Three points apply:

- The team must always deal with constraints.
- Some constraints are negotiable, so a constraint is not automatically final.
- Some constraints reach beyond a single system. They can apply to a whole organization or company.

**In practice.** Early in a project, the architect can do two things:

1. Find the requirements with the most weight, especially the quality goals of key stakeholders.
2. Sort the constraints into fixed ones and negotiable ones.

The architectural decisions then sit inside the space that remains.

## Example

A team plans an online booking system. The operations manager, a key stakeholder, says the system must stay usable during busy sales. That quality goal pushes the team toward basic design choices. The company also requires one approved database product for all systems. This constraint covers the whole organization. The team notes it as fixed. A second rule, a preferred hosting provider, might be negotiable, so the team asks whether it can be changed. Now the team knows where it can decide freely and where it cannot.

## Trade-offs

Quality goals of important stakeholders influence fundamental decisions, and stakeholders who are not known early can cause unpleasant surprises later in development.
