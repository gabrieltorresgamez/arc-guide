---
title: Architecture Principle
slug: architecture-principle
category: principles
kind: principle
summary: An architecture principle is a short statement of what an organization values. It narrows the
  options for design decisions without dictating the answer, so teams decide faster and more consistently.
arc42:
- 4
- 2
- 9
step: s07-solution-strategy
related:
- structure-of-an-architecture-principle
- working-with-principles
- conflicting-architecture-principles
- continuous-architecture-principles
- architectural-decision
- arc42-solution-strategy
- data-architecture-principle
- relationships-between-architecture-principles
checks:
- Each principle has a statement, a rationale tied to stakeholder goals, consequences, exceptions and
  relations.
- The principles reflect what the organization values when it must compromise, not generic statements.
- Principles narrow the options instead of dictating a single answer.
- Repeated justified exceptions to a principle trigger a review of it.
sources:
- url: https://continuousarchitecture.com/2025/11/15/why-principles-and-decisions-are-the-core-of-modern-software-architecture/
  title: Why Principles and Decisions Are the Core of Modern Software Architecture – Continuous Architecture
    in Practice
  site: continuousarchitecture.com
  accessed: '2026-11-09'
- url: https://labs.sogeti.com/fundamentals-for-architecture-principles-part1/
  title: Fundamentals for architecture principles (part1) - Sogeti Labs
  site: labs.sogeti.com
  accessed: '2026-11-09'
- url: https://www.itarch.info/2020/01/it-architecture-principles.html
  title: IT Architecture Principles
  site: itarch.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-4/
  title: 4 - Solution strategy | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architecture principle is a guideline for a whole class of problems. It is cohesive, prescriptive and supports decisions. A good principle does not provide the answer. It narrows the range of options, like a guardrail rather than a gate. That narrowing helps teams decide faster.

**Principles and decisions.** Principles record the priorities and beliefs that guide reasoning. Decisions are the actual unit of architectural work (see Architectural Decision).

**Reflect real values.** A good principle shows what the organization values most when it must compromise. It only works when it is grounded in the organization's context.

**How to write one.** In one author's practice, an effective formulation has at least these parts:

- the statement itself;
- the rationale, which should tie to stakeholders and their goals;
- the consequences;
- the exceptions, meaning situations where deviation is acceptable;
- the relations, for example to other principles, or to mission, vision, goals or legal restrictions.

The rationale should support discussion. See Architecture Principle Structure for details.

**Exceptions and review.** Sometimes a team sets a principle aside for good reasons. If that happens repeatedly, the principle may need a review. For instance, setting a principle aside three times for valid reasons could trigger one.

**In arc42.** The solution strategy is a short summary and explanation of the fundamental decisions that shape the architecture. The explanation of these decisions should be kept short, and it should say what was decided and why. See Solution Strategy.

## Example

A company states this principle: "Prefer packaged products over custom code." The rationale says the business wants features quickly and has a small team. A consequence is that teams must justify any custom build. An exception covers a feature that gives the company a unique edge. When a team plans a new billing function, the principle removes "build from scratch" as the default option. The team then compares packaged products.

## Trade-offs

Principles involve trade-offs. For example, a principle that favors packaged solutions saves effort. But heavy customization of such packages raises maintenance costs. Recurring exceptions to a principle are a sign that it may need review.
