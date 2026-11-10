---
title: Service-Oriented Architecture
slug: service-oriented-architecture
category: styles-patterns
kind: style
summary: Service-Oriented Architecture (SOA) organizes software as services that consumers reach through
  defined interfaces. Providers and consumers may belong to different organizations. The term is loose,
  and a central hub can become a bottleneck.
arc42:
- 4
- 5
- 8
- 11
step: s08-integration-data
related:
- broker-pattern
- microservices-architecture
- architectural-style
- loose-coupling
- modifiability-tactics-in-soa
- integration-pattern
- messaging
checks:
- Each service has a documented interface that is separate from its implementation.
- Each service has a description with the information needed to use it.
- The document states how consumers discover services, for example through a registry.
- If a central broker is used, the document addresses the bottleneck risk.
- The document states which meaning of SOA it uses.
sources:
- url: https://docs.oasis-open.org/soa-rm/v1.0/soa-rm.html
  title: Reference Model for Service Oriented Architecture v1.0
  site: docs.oasis-open.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html
  title: Message Broker - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/bliki/ServiceOrientedAmbiguity.html
  title: Service Oriented Ambiguity
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A consumer finds a service through a registry, then calls it through its interface.
review:
  status: generated
  flags: []
---

## Explanation

Service-Oriented Architecture (SOA) is a paradigm, or way of thinking, for organizing and using distributed capabilities. The capabilities may be under the control of different ownership domains.

**Services.** A service is the mechanism that brings together what a consumer needs and what a provider can do.

**Interface and contract.** The service interface is the way to reach a service's underlying capabilities. The implementation behind it is typically hidden from callers, apart from what the interface exposes. A contract is what consumer and provider agree on regarding constraints and policies.

**Description and discovery.** A service description holds the information needed to use a service, or to decide whether to use it. Consumers usually become aware of services through discovery mechanisms such as registries.

**Different owners.** SOA is motivated by ownership boundaries. A provider and its consumers may belong to different organizations.

**Central hubs.** Separately from SOA, the Message Broker pattern routes all messages through one central broker, sometimes called the hub-and-spoke style.

**A loose term.** Martin Fowler notes that SOA means many different things. For some people it means exposing software through web services. For others it means asynchronous document messaging. In their microservices article, James Lewis and Martin Fowler say that the SOA they usually came across centered on ESBs used to integrate monolithic applications. So check which meaning a document intends.

**Contrast with microservices.** The microservice community prefers smart endpoints and dumb pipes. ESB products, by contrast, often include sophisticated facilities for routing, choreography, transformation and business rules.

## Example

A city's permit office offers a "check application status" service. Other organizations, such as a bank or a law firm, call it through a published interface. The description says how to call it. A registry lists it. The office can replace its internal systems, and callers notice nothing as long as the interface stays the same.

## Trade-offs

Routing all messages through a single central broker has the advantage of central maintenance, but it can turn that broker into a serious bottleneck.
