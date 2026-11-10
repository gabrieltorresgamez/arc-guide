---
title: Architectural Pattern
slug: architectural-pattern
category: styles-patterns
kind: pattern
summary: An architectural pattern is a proven, reusable solution to a problem that keeps recurring in
  systems. Its description covers context, problem, solution and consequences, so you can see the trade-offs
  before you choose.
arc42:
- 4
- 5
- 9
step: s07-solution-strategy
related:
- architectural-pattern-vs-design-pattern
- architectural-style
- architectural-tactic
- tactics-vs-architectural-styles-and-patterns
- pipes-and-filters
- layers-pattern
- broker-pattern
- model-view-controller-pattern
checks:
- Each pattern used is described with its context, the problem and the consequences.
- The document names the element types of each pattern and their responsibilities.
- The document states the topology constraints of each pattern, such as what elements may know about each
  other.
- The document states the conditions under which each chosen pattern works and does not work.
- The choice of pattern is justified by the quality goals it serves and its trade-offs.
sources:
- url: https://en.wikipedia.org/wiki/Architecture_pattern
  title: Software architecture - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters
  title: Pipes and Filters pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
  title: Architecture Styles - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/enterprisePatterns.html
  title: Patterns in Enterprise Software
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: 'Pipes and Filters: filters do one task each, and pipes only connect them.'
review:
  status: generated
  flags: []
---

## Explanation

An architectural pattern is a reusable solution that has worked before. It targets a recurring problem at the level of the whole system. It sits at a higher level of abstraction than a design pattern (see Architectural Pattern vs. Design Pattern).

**How a pattern is described**

Good pattern descriptions follow a fixed shape. The Pipes and Filters page from Azure shows it well.

- **Context and problem.** The problem there is a processing module built as one big block. That block is hard to reuse, reorder or scale.
- **Solution.** The pattern names the element types and what each does. Filters each do one task. Pipes only connect filters and contain no logic.
- **Topology and constraints.** Filters know only their input and output formats. They do not know each other. So you can arrange them in any order, as long as each output format matches the next input format.
- **Consequences.** The pipeline is usually still one unit and needs end-to-end testing. Spreading filters across servers adds complexity.
- **Fit.** The page also says when the pattern works poorly. Examples are request-response processing, or steps that are not independent and must run together in one transaction.

**Patterns and styles**

An architecture style is a family of architectures with shared traits. It limits which elements may appear and how they may relate. Those limits bring desirable properties (see Architecture Style). The N-tier style is one example. Each layer has one responsibility, and layers only call the layers beneath them. The same page notes that this layering can make change harder. One source says the line between style and pattern can be blurry.

**Where patterns come from and how to analyze them**

Fowler credits the Buschmann et al. POSA book with influential work on architectural patterns. He names layers and pipes and filters as foundations for later enterprise patterns. The SEI report on modifiability tactics describes standard patterns and their variants in terms of the tactics they use. A tactic is a design decision that affects how well an architecture addresses a particular quality attribute (see Architectural Tactic).

**Choosing**

Every style or pattern has trade-offs. Choose based on why it fits the quality goals that drive the business, not only on how to build it.

## Example

A team builds an order-import job. It reads a file, validates rows, converts currencies and writes to storage, all in one block of code. Changing the order of steps is risky, and nobody can reuse the validation. The team reads a pattern description. The context matches, and the steps are independent. They split the job into single-task filters joined by connectors that hold no logic. They also note the cost: the whole pipeline still needs end-to-end tests.

## Trade-offs

A pattern improves some qualities and weakens others. Pipes and Filters gains reuse and reordering. It pays with end-to-end testing effort and added complexity when distributed. It also fits poorly when steps depend on each other or share one transaction. Layering, in the N-tier style, gives clear responsibilities but can make change harder. Check the stated conditions before you adopt a pattern.
