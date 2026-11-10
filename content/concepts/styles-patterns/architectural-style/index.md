---
title: Architecture Style
slug: architectural-style
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
- pipe-and-filter-pattern
- arc42-solution-strategy
- quality-attribute-prioritization
- big-ball-of-mud
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

Martin Fowler's point is that a style, like any other, has both costs and benefits.

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
