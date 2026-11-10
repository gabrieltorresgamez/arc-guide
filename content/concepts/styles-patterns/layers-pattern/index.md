---
title: Layers Pattern
slug: layers-pattern
category: styles-patterns
kind: pattern
summary: The Layers pattern splits software into layers with separate responsibilities. A higher layer
  may use a lower layer, never the reverse. This keeps dependencies under control, at the cost of some
  latency and pass-through work.
arc42:
- 4
- 5
- 8
- 9
step: s07-solution-strategy
related:
- layered-architecture
- architectural-pattern
- coupling-and-cohesion
- separation-of-concerns
- modifiability
- layers-and-components-decomposition
- shearing-layers
- domain-layer
checks:
- Each layer has a stated responsibility, and the document says which layers may use which.
- No lower layer uses a higher layer.
- The document states whether layering is strict, relaxed or mixed.
- Any layer that only forwards requests has been justified against its latency cost.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier
  title: N-tier Architecture Style - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/THE_multiprogramming_system
  title: THE multiprogramming system - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.martinfowler.com/bliki/PresentationDomainDataLayering.html
  title: Presentation Domain Data Layering
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Layer_(object-oriented_design)
  title: Layer (object-oriented design) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Usage flows downward only. The dotted arrow shows relaxed layering.
review:
  status: generated
  flags: []
---

## Explanation

The Layers pattern is an architectural pattern (see Architectural Pattern). It divides a system into layers. Each layer has one specific responsibility. Layers also manage the dependencies between parts of the system.

**The core rule.** A higher layer may use the services of a lower layer. A lower layer may never use the services of a higher layer. This is a one-way "allowed-to-use" relation: there is no upward usage.

**Strict and relaxed layering.** Two styles exist:

- In a closed (strict) layer architecture, a layer calls only the layer directly below it.
- In an open (relaxed) layer architecture, a layer may call any layer below it.


**What you gain.**

- Developers can narrow their focus to one piece at a time.
- Module boundaries create seams. You can substitute an implementation or test a piece at those seams.
- Because higher layers depend only on lower ones, it is easier to reason about the system and to build and test it step by step.

**Organizing teams.** Fowler calls organizing development teams by layer an antipattern. Team boundaries add friction to work that crosses layers.

**Background.** In object-oriented design, a layer is a group of classes that share the same link-time dependencies. Layers are often arranged as a hierarchy. The pattern is described in several well-known books. In the T.H.E. operating system, layers were built bottom-up. Layer 0 handled scheduling and context switching.

## Example

A web shop has three layers: presentation, business rules and data storage. The presentation layer calls the business rules. The business rules call data storage. Data storage never calls the business rules. In strict mode, presentation never touches data storage directly. In relaxed mode, it may.

## Trade-offs

- **Unnecessary traffic.** A closed layer that only forwards requests can create unnecessary traffic.
- **Team structure.** Splitting teams along layers adds friction to cross-layer work.
