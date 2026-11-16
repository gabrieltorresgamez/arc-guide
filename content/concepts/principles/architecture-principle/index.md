---
title: Architecture Principle
slug: architecture-principle
order: 10
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
- continuous-architecture-principles
- architectural-decision
- arc42-solution-strategy
- data-architecture-principle
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
- url: https://togaf.visual-paradigm.com/2025/01/21/comprehensive-guide-to-applying-architecture-principles-in-togaf-adm/
  title: Comprehensive Guide to Applying Architecture Principles in TOGAF ADM - Visual Paradigm
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://togaf.visual-paradigm.com/2023/10/12/crafting-effective-architecture-principles-a-guide/
  title: 'Crafting Effective Architecture Principles: A Guide - Visual Paradigm'
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://public.isaqb.org/glossary/glossary-en.html
  title: iSAQB® Glossary of Software Architecture Terminology
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/simplify
  title: Architecture strategies for designing for simplicity and efficiency - Microsoft Azure Well-Architected
    Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles
  title: Architectural principles - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/Yagni.html
  title: Yagni
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/architectural-design-principles/
  title: Harnessing the Power of Architectural Design Principles - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://cio-wiki.org/wiki/Architectural_Principles
  title: Architectural Principles - CIO Wiki
  site: cio-wiki.org
  accessed: '2026-11-09'
- url: https://docs.sunnycalc.griesser.com/architecture/05-principles-and-guidelines/
  title: Principles and Guidelines | Sunny Calculator Add-On
  site: docs.sunnycalc.griesser.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/loose-coupling
  title: "Loose Coupling | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/cohesion
  title: "Cohesion | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/modularity
  title: "Modularity | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/composability
  title: "Composability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
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

The rationale should support discussion.

**Exceptions and review.** Sometimes a team sets a principle aside for good reasons. If that happens repeatedly, the principle may need a review. For instance, setting a principle aside three times for valid reasons could trigger one.

**In arc42.** The solution strategy is a short summary and explanation of the fundamental decisions that shape the architecture. The explanation of these decisions should be kept short, and it should say what was decided and why. See Solution Strategy.

**More about working with principles.**

- **Architecture Principle Structure:** An architecture principle is written in four parts: a Name, a Statement, a Rationale and Implications. Together they show the rule, why it helps the business, and what it demands.
- **Working with Principles:** Working with principles means writing short rules that tie design decisions to requirements. A good principle has a name, a statement, a rationale and implications. Teams may break one only for a justified reason.

**In the arc42 quality model.** It has quality pages on related principles: [Loose Coupling](https://quality.arc42.org/qualities/loose-coupling), [Cohesion](https://quality.arc42.org/qualities/cohesion), [Modularity](https://quality.arc42.org/qualities/modularity), [Composability](https://quality.arc42.org/qualities/composability).

## Example

A company states this principle: "Prefer packaged products over custom code." The rationale says the business wants features quickly and has a small team. A consequence is that teams must justify any custom build. An exception covers a feature that gives the company a unique edge. When a team plans a new billing function, the principle removes "build from scratch" as the default option. The team then compares packaged products.

## Trade-offs

Principles involve trade-offs. For example, a principle that favors packaged solutions saves effort. But heavy customization of such packages raises maintenance costs. Recurring exceptions to a principle are a sign that it may need review.
