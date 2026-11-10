---
title: Architecture Principle Structure
slug: structure-of-an-architecture-principle
category: principles
kind: artifact
summary: 'An architecture principle is written in four parts: a Name, a Statement, a Rationale and Implications.
  Together they show the rule, why it helps the business, and what it demands.'
arc42:
- 1
- 4
- 8
step: s07-solution-strategy
related:
- architecture-principle
- working-with-principles
- togaf
- relationships-between-architecture-principles
- conflicting-architecture-principles
- data-architecture-principle
- continuous-architecture-principles
- architecture-decision-rationale
checks:
- Each principle has a Name, a Statement, a Rationale and Implications.
- The Statement is short and states one fundamental rule without ambiguity.
- The Rationale gives business benefits and relates to stakeholders and their goals.
- The Implications list requirements, resources, costs and tasks for carrying out the principle.
sources:
- url: https://togaf.visual-paradigm.com/2025/01/21/comprehensive-guide-to-applying-architecture-principles-in-togaf-adm/
  title: Comprehensive Guide to Applying Architecture Principles in TOGAF ADM - Visual Paradigm
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://labs.sogeti.com/fundamentals-for-architecture-principles-part1/
  title: Fundamentals for architecture principles (part1) - Sogeti Labs
  site: labs.sogeti.com
  accessed: '2026-11-09'
- url: https://togaf.visual-paradigm.com/2023/10/12/crafting-effective-architecture-principles-a-guide/
  title: 'Crafting Effective Architecture Principles: A Guide - Visual Paradigm'
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A Visual Paradigm guide on TOGAF architecture principles lists four components that each principle should include. Each part has its own job. (The article on TOGAF covers the framework itself.)

**Name.** The name is a clear, memorable label for the rule. One example principle is Technology Independence.

**Statement.** The statement gives the fundamental rule. It is a succinct and unambiguous communication of that rule. For example: applications are independent of specific technology choices and can operate on a variety of technology platforms.

**Rationale.** The rationale explains the business benefits of following the principle.

**Implications.** The implications list what it takes to carry out the principle. That means requirements, resources, costs and activities or tasks.

**Why the structure matters.** Principles are meant to be enduring and seldom amended. They reflect consensus, guide future IT decisions and align with business objectives.

**Qualities of a good principle.** A separate Visual Paradigm guide on crafting effective principles lists five criteria: understandable, robust, complete, consistent and stable. Stable means the principle withstands the test of time and stays relevant.

For the general idea of a principle, see Architecture Principle.

## Example

A team writes a principle for a retail company.

- **Name:** Technology Independence.
- **Statement:** Applications are independent of specific technology choices and can operate on a variety of technology platforms.
- **Rationale:** Independence from the underlying technology allows applications to be developed, upgraded and operated in a cost-effective and timely way.
- **Implications:** The team lists the requirements, resources, costs and tasks needed to keep applications free of platform dependence.

## Trade-offs

A Visual Paradigm guide on crafting principles also lists name, statement, rationale and implication, while the Sogeti page lists a partly overlapping set (statement, rationale, consequences, plus others).
