---
title: Conflicting Architecture Principles
slug: conflicting-architecture-principles
category: principles
kind: concept
summary: Architecture principles such as simplicity, separation of concerns and low coupling each favor
  some qualities and cost others. They are guidelines, not absolute rules, so architects weigh them against
  business context and record the trade-offs.
arc42:
- 4
- 8
- 9
- 10
- 11
step: s09-decisions
related:
- architecture-principle
- relationships-between-architecture-principles
- working-with-principles
- coupling-and-cohesion
- separation-of-concerns
- architectural-trade-off-thinking
- trade-off-point
- architectural-decision-record
checks:
- Design decisions are justified by a business requirement, not by a principle alone.
- Decisions where principles conflict are recorded with their rationale, trade-offs and consequences.
- Choices such as microservices are justified by fit to context, not by trend.
- Added abstraction (interfaces, extra layers) is tied to a need such as pluggability or testability.
sources:
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Design principles can pull in different directions, as the tradeoffs below show.

**Where principles pull apart**

- **Separation of concerns** (see Separation of Concerns) leads to layers and separate projects. Business logic becomes easy to test.
- **Loose coupling** often uses interfaces, so different implementations can be plugged in.
- **Single responsibility**, taken to its logical endpoint, gives microservices. Microservices bring complexity, overhead and dependency issues.
- **Simplicity** pulls the other way. A complex solution offers more flexibility, but it needs more coordination between components, which can hurt reliability. A simple one may hurt scalability and extensibility.
- **DRY** (don't repeat yourself) can clash with low coupling. Merging code that only looks alike creates a wrong shared piece. Here, duplication can be the better choice.
- **YAGNI** (you aren't gonna need it) warns against building flexibility before it is needed. Early flexibility adds complexity now and pays off only later.

**Over-applying a principle**

Azure guidance warns against both over-engineering and under-engineering. Splitting code into many small functions, for example, makes it harder to understand, test and maintain.

**Principles need context**

Principles are not universal rules. Every design decision should be justified by a business requirement. Teams should not follow trends that may not fit their context.

Constraints are also negotiated. Reaching reliability targets may require compromise between technology and business teams.

**Making the trade-off explicit**

The Architecture Tradeoff Analysis Method (ATAM) shows how quality goals interact and trade off. It identifies risks, sensitivity points and trade-off points. An Architectural Decision Record (ADR) documents a chosen decision with its rationale, trade-offs and consequences.

## Example

A team builds an internal tool for 50 users. One member wants every feature split into its own service, with interfaces everywhere, to keep parts independent. Another wants one simple application. The team notes that the user base is small and the business needs a release in two months. They choose a single application with clear internal layers. They write an ADR that records this choice, the reasons, and the condition under which they would split it later.

## Trade-offs

Following one principle strictly buys one quality and spends another. More separation gives testability. More simplicity gives easier understanding but may limit scalability and extensibility. The team has to choose, justify the choice with business needs, and write it down. Writing takes effort, but it keeps the reasoning available later.
