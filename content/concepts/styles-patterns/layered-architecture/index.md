---
title: Layered Architecture
slug: layered-architecture
category: styles-patterns
kind: style
summary: Layered architecture splits a system into layers with separate responsibilities. A higher layer
  may use a lower one, never the reverse. This keeps dependencies orderly and makes parts easier to change,
  test and reuse.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- layers-pattern
- domain-layer
- separation-of-concerns
- coupling-and-cohesion
- domain-driven-design
- modifiability
- architectural-style
- layers-and-components-decomposition
checks:
- The document states that each layer has a defined responsibility and that dependencies run only from
  higher to lower layers.
- The document says whether layering is strict or relaxed, and names the latency or coupling consequences.
- Any upward communication from a lower layer is handled through callbacks, observers or events, and is
  documented.
- The domain layer is isolated from user interface and persistence code.
- If layers run on separate tiers, the document notes the added network latency.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier
  title: N-tier Architecture Style - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/bliki/PresentationDomainDataLayering.html
  title: Presentation Domain Data Layering
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://herbertograca.com/2015/09/18/domain-driven-design-by-eric-evans-chap-4-isolationg-the-domain/
  title: DDD.4 – Isolating the domain – @hgraca
  site: herbertograca.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/THE_multiprogramming_system
  title: THE multiprogramming system - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Layers where each one uses only the layer beneath it.
review:
  status: generated
  flags: []
---

## Explanation

A layered architecture divides a system into layers. Each layer has a specific responsibility. The key rule is about direction: a higher layer may use the services of a lower layer, but a lower layer may not use a higher one.

**Typical layers.** A common split has three parts:

- a presentation layer (what users see),
- a domain layer, also called business logic (the rules of the business),
- a data access layer (reading and writing data).

Dependencies run from top to bottom through this stack.

**Why it helps.** The domain logic sits in its own layer, so several presentations can share it. A web site and a mobile app, for example, can use the same logic without copying it. Layer boundaries also give natural seams for testing parts separately.

**Early use.** Dijkstra's THE operating system imposed the rule that higher layers depend only on lower layers. The designers imposed this constraint to make reasoning about the system more tractable and to let them build and test it step by step.

**Closed and open layers.** In a closed layer architecture, a layer can only call the next layer immediately down. In an open layer architecture, a layer can call any layer under it.

**Strict and relaxed tiers.** Tiers can use a strict or a relaxed communication model. In the strict model, a request must pass through adjacent tiers one by one and can't skip any. In the relaxed model, requests may skip some tiers. The strict model adds delay and overhead. The relaxed approach has more couplings, which makes changes harder.

**Layers and tiers.** Logical layers can be hosted on separate physical tiers. The physical separation of tiers improves scalability and resiliency. It also adds network latency.

**Layers in Domain-Driven Design.** In DDD (see Domain-Driven Design), each layer depends only on the layer below it. Isolating the domain layer from user interface and persistence code is central. Sometimes a lower layer must notify an upper one. Callbacks, observers or events can handle this. Use them with restraint.

**N-tier.** An n-tier style suits evolving requirements. It also suits moving existing on-premises applications with minimal changes and relatively low cost. It is portable and has a smaller learning curve for most developers.

## Example

An online shop has three layers. The presentation layer shows product pages on the web and in a mobile app. The domain layer calculates prices and discounts. The data access layer reads and writes orders. The web page asks the domain layer for a price. The domain layer never calls the web page directly. Because the web page and the mobile app share the domain layer, they use the same discount logic without copying it.

## Trade-offs

- **Strict vs. relaxed tiers:** the strict model has more latency and overhead. The relaxed model has more couplings, so changes get harder.
- **Pass-through traffic:** closed layers limit dependencies. They can cause needless network traffic when a layer only forwards requests.
- **Separate tiers:** hosting layers on different tiers improves scalability and resiliency. It adds latency from extra network communication.
- **Upward calls:** the "never upward" rule needs callbacks, observers or events when a lower layer must notify a higher one. Use them with restraint.
