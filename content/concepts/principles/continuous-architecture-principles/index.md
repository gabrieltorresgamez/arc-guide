---
title: Continuous Architecture Principles
slug: continuous-architecture-principles
category: principles
kind: principle
summary: 'Continuous Architecture rests on principles that guide design reasoning. This article covers
  four: focus on quality attributes, delay decisions until facts exist, architect for change with small
  elements, and organize teams after the system design.'
arc42:
- 4
- 9
- 10
step: s07-solution-strategy
related:
- architecture-principle
- working-with-principles
- last-responsible-moment
- quality-attribute
- loose-coupling
- coupling-and-cohesion
- architectural-decision-record
- design-for-change
checks:
- Quality attribute requirements, not only functional ones, are named as drivers of the architecture.
- Decisions are based on facts rather than guesses, so unused capabilities are not built.
- The design favors small, loosely coupled elements over big, tightly coupled components.
- Team organization matches the system design.
- Decisions are captured in lightweight decision records.
sources:
- url: https://continuousarchitecture.com/2025/11/04/a-decade-of-ca/
  title: 'Continuous Architecture: A decade of designing for change – Continuous Architecture in Practice'
  site: continuousarchitecture.com
  accessed: '2026-11-09'
- url: https://cio-wiki.org/wiki/Continuous_Architecture
  title: Continuous Architecture - CIO Wiki
  site: cio-wiki.org
  accessed: '2026-11-09'
- url: https://continuousarchitecture.com/2025/11/15/why-principles-and-decisions-are-the-core-of-modern-software-architecture/
  title: Why Principles and Decisions Are the Core of Modern Software Architecture – Continuous Architecture
    in Practice
  site: continuousarchitecture.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Continuous Architecture authors describe principles as capturing priorities and beliefs that guide a team's reasoning. See Architecture Principle and Working with Principles for the general idea.

This article covers four of these principles.

**Principle 2: Focus on quality attributes.** Quality attribute requirements, not functional ones, are the main drivers of the architecture. Resilience, scalability and security are examples of quality attributes. See Quality Attribute.

**Principle 3: Delay design decisions until they are needed.** Teams decide based on facts, not guesses. That way they do not build capabilities nobody uses. See Last Responsible Moment.

**Principle 4: Architect for change.** This principle leverages the "power of small" elements. Big, monolithic, tightly coupled components are hard to change. So the principle favors small, loosely coupled services. See Loose Coupling and Coupling and Cohesion.

**Principle 6: Model your teams after the system design.** This follows Conway's Law. The way teams are organized drives the architecture and design of the systems they work on. The authors say the law is now widely accepted.

The authors also recommend lightweight decision records (ADRs) to capture decisions. See Architectural Decision Record.

## Example

A team plans an online shop. Speed at peak sales and ease of change matter most to the business, so the team makes these qualities the main drivers of the design. It postpones choosing a recommendation feature until real usage shows it is needed. It builds the shop from small, loosely coupled services. It then organizes its teams to match those services. It records each decision in a short decision record.

## Trade-offs

Teams should weigh the principles against their own context.
