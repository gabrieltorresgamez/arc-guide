---
title: Architectural Pattern vs. Design Pattern
slug: architectural-pattern-vs-design-pattern
category: styles-patterns
kind: concept
summary: An architectural pattern shapes the structure of a whole system. A design pattern solves a narrower
  problem in one subsystem. Architectural choices are costly to change later, so they deserve more upfront
  effort.
arc42:
- 4
- 5
- 9
step: s07-solution-strategy
related:
- architectural-pattern
- architectural-style
- microservices-architecture
- layered-architecture
- circuit-breaker
- retry
- architectural-trade-off-thinking
- arc42-solution-strategy
checks:
- The document names the architecture style or patterns chosen for the whole system.
- The reasons for the chosen style are recorded, given that late changes are costly.
- The trade-offs of the chosen style or patterns are stated.
- Where several patterns are combined, the document says which problem each one solves.
sources:
- url: https://www.modernescpp.com/index.php/architectural-patterns/
  title: Architectural Patterns – MC++ BLOG
  site: modernescpp.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
  title: Architecture Styles - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/
  title: Cloud Design Patterns - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Patterns exist at different levels of detail. Three levels are commonly named: architectural patterns, design patterns and idioms. Each level covers a different scope.

**Architectural patterns** describe the fundamental structure of the whole software system. They focus on the system as a whole.

**Design patterns** work at the level of subsystems. They define how components interact.

**Idioms** are the most concrete level. An idiom is a pattern realized in one specific programming language.

The Pattern-Oriented Software Architecture series (POSA) is a rich source of architectural patterns.

**Pattern versus style.** An architecture style is a family of architectures that share characteristics. N-tier and microservices are examples. A style limits which elements may appear in a design and how they may relate. When a team follows those limits, desirable properties emerge. Styles do not require specific technologies, although some technologies fit certain styles better. See the article Architecture Style for more.

**Why the level matters.** Changing architectural direction late is costly. Effort spent on choosing a style early often pays off. A good architecture also decides how expensive future change will be. With a poor one, adding new capabilities gets slower and more expensive.

**Patterns work together.** One pattern addresses one problem. A real workload faces several problems at once, so teams combine patterns. Retry combined with Circuit Breaker is one example.

## Example

Imagine an online shop. The team chooses microservices, meaning the shop is split into several services. That choice shapes the whole system, so it is architectural. Later, the team adds Retry and Circuit Breaker to handle failing calls between services. These patterns address specific problems and are combined within the larger structure.

## Trade-offs

Every architecture style has trade-offs. Microservices bring autonomy and faster releases. They also add complexity in service discovery, data consistency and distributed management.

Cloud design patterns work the same way. Each supports certain quality goals, possibly at the expense of others. Late changes to the architecture cost more, so choose a style deliberately and early.
