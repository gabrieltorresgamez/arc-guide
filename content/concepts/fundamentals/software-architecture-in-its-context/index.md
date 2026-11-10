---
title: Software Architecture in Its Context
slug: software-architecture-in-its-context
category: fundamentals
kind: concept
summary: Software architecture is shaped by its surroundings. The organization, its constraints and its
  stakeholders all influence which designs are possible. Architects need to know where they are free and
  where they are bound.
arc42:
- 1
- 2
step: s05-constraints
related:
- arc42-constraints
- requirements-versus-constraints
- stakeholder
- stakeholder-concern
- requirements-and-means-influence-architecture
- architect-knowledge-and-tasks
- software-architecture
- arc42-introduction-and-goals
checks:
- Constraints that limit design and implementation freedom are listed, grouped as technical, organizational,
  political or conventions.
- The document notes which constraints come from the wider organization rather than from this system alone.
- The document shows which constraints are fixed and which may be negotiable.
- The quality goals of the most important stakeholders are stated.
- The level of detail of the document matches what the stakeholders need.
sources:
- url: https://www.melconway.com/Home/Committees_Paper.html
  title: Committees Paper
  site: melconway.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Organization, constraints and stakeholders all influence the architecture.
review:
  status: generated
  flags: []
---

## Explanation

A software architecture is not designed in a vacuum. Outside forces push on it.

**The organization shapes the design.** Melvin Conway argued that any organization that designs a system will produce a design whose structure copies the organization's communication structure. In military-style organizations, protocol restricts communication along lines of command, so the communication structure resembles the administrative structure. This is one reason such organizations design systems that look like their organization charts.

**Constraints limit the architect's freedom.** An architecture constraint is a requirement that restricts the architect's freedom in design and implementation decisions. Some constraints reach beyond one system. They can apply to a whole organization or company. One way to sort them is into technical constraints, organizational and political constraints, and conventions.

Architects must always deal with constraints. Some are negotiable. So architects need to know where they are free and where they are bound.

**Stakeholders steer the big decisions.** The quality goals of the most important stakeholders influence fundamental architectural decisions. Stakeholders also determine the extent and level of detail of the architect's work and results.

## Example

A company has three teams: one for the web shop, one for payments and one for shipping.  A company-wide rule requires one approved database product. That is a constraint, and the architect asks whether it is negotiable. The most important stakeholders care about fast checkout, and that goal weighs heavily on the main design decisions.

## Trade-offs

Constraints reduce the architect's freedom, but they must still be handled, and some can be negotiated. Likewise, stakeholders determine the extent and level of detail of the architect's work, so the effort has to match what they need.
