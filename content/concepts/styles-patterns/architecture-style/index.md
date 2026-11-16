---
title: Architecture Style
slug: architecture-style
order: 10
category: styles-patterns
kind: style
summary: 'An architecture style is a set of design constraints: which elements may appear and how they
  may relate. Following the constraints gives a system certain desirable properties. Every style also
  has costs.'
arc42:
- 4
- 9
- 2
- 10
step: s07-solution-strategy
related:
- architectural-pattern
- microservices-architecture
- layered-architecture
- service-oriented-architecture
- pipes-and-filters
- arc42-solution-strategy
- quality-attribute-prioritization
- big-ball-of-mud
- blackboard-pattern
- lambda-architecture
checks:
- The document names the chosen architecture style and states the constraints it imposes on elements and
  their relationships.
- The style choice is traced to business drivers and prioritized architecture characteristics, with stakeholder
  input.
- The costs of the chosen style are stated next to its benefits, such as operational complexity or network
  latency.
- If layers and physical tiers are used, the document shows how layers map to tiers and whether layers
  are open or closed.
- The document says how the style choice will be validated over time, since changing it later is costly.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
  title: Architecture Styles - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier
  title: N-tier Architecture Style - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/approaches/microservice-architecture
  title: "Microservice Architecture | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/event-driven-architecture
  title: "Event-Driven Architecture | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/hexagonal-architecture
  title: "Hexagonal Architecture | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/plugin-architecture
  title: "Plugin Architecture | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/self-contained-systems
  title: "Self-Contained Systems | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/cqrs
  title: "CQRS | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/event-sourcing
  title: "Event Sourcing | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/saga-pattern
  title: "Saga Pattern | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/transactional-outbox
  title: "Transactional Outbox | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/api-gateway
  title: "API Gateway | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/backends-for-frontends
  title: "Backends for Frontends | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/sidecar
  title: "Sidecar | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: Two logical layers deployed as separate physical tiers. A higher layer uses only the layer
    below it.
review:
  status: generated
  flags: []
---

## Explanation

An architecture style limits your design choices on purpose. It says which kinds of elements can appear in a system. It also says how those elements may relate to each other. A design that follows these limits gets certain desirable properties.

**Microservices as a style.** This style constrains each service to a single responsibility. Services stay independent. Each service keeps its data private, and services do not share data. These constraints produce independent deployment, fault isolation, frequent updates and an easier path to new technology.

**N-tier as a style.** This style separates logical layers from physical tiers. Layers follow a dependency rule: a higher layer uses a lower one. Tiers are physically separate and run on separate machines. Layers do not have to map one-to-one onto tiers. Tiers can talk directly or through asynchronous messaging patterns that use a message queue.

**Event-driven as a style.** Producers and consumers stay decoupled. They communicate through event channels or brokers.

**Layering rules are style constraints too.** A closed layer limits the dependencies between layers. An open layer relaxes that limit.

**How to choose a style.** Start from the problem, not the style. Define the key business drivers. Name the matching architecture characteristics, also called nonfunctional requirements. Prioritize them, and ask stakeholders for input. Keep validating the choice, because changing a style later is costly.

A style, like any other, has both costs and benefits.

**More styles in the arc42 quality model.** The arc42 quality model has approach pages on related architecture styles and patterns: [Microservice Architecture](https://quality.arc42.org/approaches/microservice-architecture), [Event-Driven Architecture](https://quality.arc42.org/approaches/event-driven-architecture), [Hexagonal Architecture](https://quality.arc42.org/approaches/hexagonal-architecture), [Plugin Architecture](https://quality.arc42.org/approaches/plugin-architecture), [Self-Contained Systems](https://quality.arc42.org/approaches/self-contained-systems), [CQRS](https://quality.arc42.org/approaches/cqrs), [Event Sourcing](https://quality.arc42.org/approaches/event-sourcing). Microsoft's Azure Architecture Center also has a guide to [architecture styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/).

**Further approaches in the arc42 quality model.** The arc42 quality model has more approach pages on related ideas: [Saga Pattern](https://quality.arc42.org/approaches/saga-pattern), [Transactional Outbox](https://quality.arc42.org/approaches/transactional-outbox), [API Gateway](https://quality.arc42.org/approaches/api-gateway), [Backends for Frontends](https://quality.arc42.org/approaches/backends-for-frontends), [Sidecar](https://quality.arc42.org/approaches/sidecar).

## Example

A team builds an online shop. Their top priorities are frequent releases and isolating failures. They pick microservices. Orders, payments and catalog become separate services, and each owns its own data. The payments service can be released without touching the catalog. If it fails, the catalog can keep running. In return, the team must handle communication between services and keep data consistent across them.

## Trade-offs

Every style trades benefits for costs.

- **Microservices** give team autonomy and release velocity. They add complexity in service discovery, data consistency and distributed operations. They need mature DevOps practices, so they suit organizations with advanced technical capabilities.
- **Event-driven** designs give scalability and fault isolation. They raise challenges with delivery, ordering and eventual consistency.
- **Physical tiers** improve scalability and resiliency. They add network latency.
- **Closed layers** limit dependencies. They can cause needless network traffic when a layer only passes requests along.
- **Splitting into services** can increase communication overhead, which may lead to latency or network congestion.
- **Fit to the domain matters.** If the style is too simple for the domain, the system can become a big ball of mud. Manageability is also a challenge.
