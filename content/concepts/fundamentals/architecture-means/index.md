---
title: Architecture Means
slug: architecture-means
category: fundamentals
kind: concept
summary: 'Architecture means are the architect''s toolbox: styles, patterns, tactics, reference architectures
  and modelling notations. More concrete means give more structure and reuse, but they also limit the
  architect''s freedom.'
arc42:
- 4
- 8
- 9
step: s07-solution-strategy
related:
- architectural-style
- architectural-pattern
- architectural-tactic
- architecture-principle
- layered-architecture
- arc42-solution-strategy
- tactics-vs-architectural-styles-and-patterns
- microservices-architecture
checks:
- The solution strategy records the fundamental decisions, including which styles, patterns or tactics
  were chosen.
- Each tactic named in the document is tied to the single quality attribute it addresses.
- For each chosen style, the document states the constraints it imposes and the trade-offs accepted.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
  title: Architecture Styles - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Reference_architecture
  title: Reference architecture - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=2738304&seqNum=5
  title: '2.5 Design Concepts: The Building Blocks for Creating Structures | Architectural Design | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_description_language
  title: Architecture description language - Wikipedia
  site: en.wikipedia.org
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

Architects do not start from a blank page. They draw on a toolbox of means. These means help them describe, shape and change a system.

**Styles.** An architecture style is a family of architectures that share characteristics. N-tier and microservices are examples. A style limits which elements and relationships are allowed. Those limits make desirable properties emerge. Styles do not require specific technologies, but some technologies fit certain styles better (see Architecture Style).

**Tactics.** A tactic is a design decision that influences how a system responds for one quality attribute, such as availability or performance. Quality attributes therefore guide the choice of tactics. Tactics are simpler and more primitive than patterns (see Architectural Tactic).

**Patterns.** A pattern usually balances several quality goals at once. A tactic does not. Tactics are put into practice through combinations of patterns, frameworks and code (see Architectural Pattern).

**Basic architectures.** N-tier is one example. It structures a whole application into logical layers and physical tiers. Each layer may only call the layers below it (see Layered Architecture).

**Reference architectures.** A reference architecture is a template generalized from a set of solutions.

**Modelling means.** Notations describe architectures. ISO/IEC/IEEE 42010 defines an architecture description language broadly as any form of expression used in architecture descriptions. So these languages count as modelling means.

**Why it matters.** The fundamental decisions and solution strategies shape the system's architecture. Those decisions are the basis for many detailed ones. They are recorded in the solution strategy (see Solution Strategy).

## Example

A team must build an online shop that stays responsive under load. They pick a style: N-tier, with a web layer, a business layer and a data layer. For fast responses, they apply a tactic. Then they implement it with a pattern and a framework. They draw the result in a standard notation. They write all these choices into the solution strategy.

## Trade-offs

A reference architecture brings reuse of an effective solution. It also adds a set of issues that the architect must address during design.

Constraints from a style bring benefits but also challenges. It can be better to relax a constraint than to chase purity. Changing direction later is costly, so weigh the choice early.
