---
title: Responsibility Allocation
slug: responsibility-allocation
category: functional-requirements
kind: concept
summary: Responsibility allocation assigns tasks and knowledge to parts of a system. Functionality alone
  does not fix the design, so quality requirements steer which allocation the architect picks.
arc42:
- 4
- 5
step: s03-functional-requirements
related:
- goal-hierarchy-to-component-mapping
- architectural-tactic
- quality-attribute
- functional-suitability
- architecturally-significant-requirement
- component-view
- coupling-and-cohesion
- method-phase-working-with-functional-requirements
checks:
- Responsibilities are named explicitly, and public ones (offered as services) are distinguished from
  private ones.
- The decomposition is justified by quality attribute requirements, not only by the list of functions.
- Tactics or patterns used to shape the decomposition are named, with their trade-offs.
- The functions cover all specified tasks and user objectives.
sources:
- url: https://www.sei.cmu.edu/library/attribute-driven-design-add-version-20/
  title: Attribute-Driven Design (ADD), Version 2.0 | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Responsibility-driven_design
  title: Responsibility-driven design - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Attribute-driven_design
  title: Attribute-driven design - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A responsibility is an obligation to perform a task or to know some information. Allocating responsibilities means deciding which part of the system carries each one.

Some responsibilities are public: a part offers them as services to others. Others are private: they only support the public ones.

The Attribute-Driven Design (ADD) method defines the architecture based on quality attribute requirements (see Quality Attribute).

ADD is also recursive. It splits a system, or one element of it, by applying tactics and patterns that satisfy the main quality needs. Then it repeats the step on the resulting elements. Tactics and patterns shape the design so that it reflects the architecturally significant requirements. Several tactics can pull in different directions, so trade-offs arise. See Architectural Tactic and Architecturally Significant Requirement.

ISO 25010 treats functional suitability as a quality characteristic. It describes how well a system provides functions that meet stated and implied needs. One sub-characteristic is completeness: whether the functions cover all specified tasks and user objectives.

## Example

An online shop has these responsibilities: know the price of each item, take an order, and charge a card. The team first assigns each one to a part of the system. Each part publicly offers the services the others need. Then a quality need, such as handling many orders at once, leads the team to split or reshape one part. The team repeats this step on the new parts.

## Trade-offs

When designing for quality needs, the architect often has to make a trade-off between several tactics and requirements.
