---
title: Relationships between Architecture Principles
slug: relationships-between-architecture-principles
category: principles
kind: concept
summary: 'Architecture principles support one another. For example, high cohesion tends
  to bring low coupling, and low coupling signals a well-structured system that avoids rigidity.'
arc42:
- 4
- 8
step: s07-solution-strategy
related:
- coupling-and-cohesion
- high-cohesion
- loose-coupling
- separation-of-concerns
- design-for-change
- architecture-principle
- conflicting-architecture-principles
- working-with-principles
checks:
- The documentation states that coupling between building blocks is loose but still functionally sufficient.
- Each element has clear responsibilities and does not mix in unrelated ones.
- Elements are cohesive, and the document links this to low coupling.
sources:
- url: https://public.isaqb.org/glossary/glossary-en.html
  title: iSAQB® Glossary of Software Architecture Terminology
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Architecture principles are rules of thumb for good design. They do not stand alone. Some support others. This article covers only some of these links.

**Cohesion and coupling.** Cohesion describes how well the parts inside one element belong together. Coupling describes how strongly elements depend on each other. The two are linked. The glossary recommends aiming for high cohesion, since it often brings reuse, low coupling and code that is easier to understand. See *Coupling and Cohesion* and *High Cohesion* for the basics.

**Why low coupling matters.** Low coupling is often a sign of a well-structured system. The iSAQB foundation curriculum lists "loose, but functionally sufficient, coupling" of building blocks as a design principle.

**Separation of concerns.** The glossary lists separation of concerns, along with low coupling and high cohesion, as an aim of design principles.

**What the principles protect against.** Design principles aim to avoid rigidity. A rigid system is hard to change, because every change potentially affects many other elements.

**Reading the links.** You can picture the principles as a network. One principle supports another, and together they push the design toward the same goals. See the related articles for each principle.

## Example

A team builds an online shop. The orders part holds only order logic. The payments part holds only payment logic. Each part has one clear job, so each part is cohesive. The two parts need little knowledge of each other, so coupling stays low. When the team changes how payments work, few other parts are affected.

## Trade-offs

Coupling must be loose but still functionally sufficient. Apply the principles together and check each against the real needs of the system.
