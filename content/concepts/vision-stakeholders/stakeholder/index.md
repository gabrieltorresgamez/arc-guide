---
title: Stakeholder
slug: stakeholder
category: vision-stakeholders
kind: concept
summary: A stakeholder is a person, team, organization, or class of such parties with an interest in a
  system being built. Architects must balance their different needs and make sure each class is represented.
arc42:
- 1
step: s01-goals-stakeholders
related:
- stakeholder-concern
- stakeholder-identification
- stakeholder-power-grid
- concern
- arc42-introduction-and-goals
- arc42-documentation-template
- stakeholder-perspective-and-concern
- iso-iec-ieee-42010-architecture-description-standard
checks:
- The document has an explicit stakeholder overview, so no surprises arise later in development.
- The stakeholder overview lists roles, names, and their expectations about the architecture and its documentation.
- Every stakeholder class has a representative, so no class is ignored.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/stakeholders/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A stakeholder is an individual, a team, an organization, or a whole class of them. What they share is an interest in the realization of the system.

Typical projects involve representatives from many stakeholder classes. Each class has its own requirements, interests, and needs. These needs have to be balanced and prioritized.

**Classes need representatives.** The architect must make sure representation is adequate across the board. If a class is not considered, problems appear later.

**Stakeholders shape the architecture work.** They determine how extensive and detailed the architecture work and its results must be.

**Documenting stakeholders.** The arc42 template (see *arc42 Architecture Documentation Template*) has a section 1.3 for an explicit stakeholder overview. The goal is to avoid surprises later in development. You should know all parties involved in developing the system or affected by it. The overview is a table with these columns:

- the role,
- the person's name,
- their expectations about the architecture and its documentation.

## Example

A team builds an online booking system. Its stakeholder table might list "Customer (class)" with a named representative from a customer panel, "Operations lead" who expects simple monitoring, and "Product owner" who expects short, readable documentation. Each row states what that party expects from the architecture and its documentation. When the operations lead's needs clash with the customers' needs, the architect weighs both and sets priorities.

## Trade-offs

Stakeholder needs can conflict, so they must be balanced and prioritized. If a class is not considered, problems appear later.
