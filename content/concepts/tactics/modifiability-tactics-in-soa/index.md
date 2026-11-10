---
title: Modifiability Tactics in SOA
slug: modifiability-tactics-in-soa
category: tactics
kind: tactic
summary: In service-based systems, intermediaries such as message buses, publish-subscribe channels, and
  registries sit between providers and consumers. Each side can then change without breaking the other,
  at some cost to performance and security.
arc42:
- 4
- 5
- 8
- 9
step: s08-integration-data
related:
- service-oriented-architecture
- modifiability-tactics
- reduce-coupling
- publish-subscribe-channel
- messaging
- loose-coupling
- architectural-trade-off-thinking
- modifiability
checks:
- Applications that exchange messages connect through a shared set of interfaces, so applications can
  be added or removed without affecting others.
- Event senders publish to a channel and do not need to know their subscribers.
- The document states who provides service discovery, versioning and access control, and whether the registry
  is custom-built or a product.
- The document records the trade-off of performance and security accepted in exchange for interoperability
  and modifiability.
- Consumers read only the data they need from a service, so providers can evolve it.
sources:
- url: https://www.sei.cmu.edu/blog/architecting-service-oriented-systems/
  title: Architecting Service-Oriented Systems | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html
  title: Message Bus - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/bliki/TolerantReader.html
  title: Tolerant Reader
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A publisher reaches several subscribers through a channel, without knowing them.
review:
  status: generated
  flags: []
---

## Explanation

In a service-oriented architecture (see Service-Oriented Architecture), applications offer services to other applications. Consumers call services. Providers offer them.

An SOA infrastructure is a piece of infrastructure that connects service consumers to services. This follows the general idea in Reduce Coupling.

**Mediating infrastructure.** An SOA infrastructure can hide differences between consumers and service interfaces. One example is different versions of a standard, such as SOAP 1.1 and SOAP 1.2.

**Message bus.** A message bus connects applications through a shared set of interfaces. It works like a universal adapter across platforms and languages. Applications can be added or removed without affecting the others. See Messaging.

**Publish-subscribe.** A sender publishes an event on a publish-subscribe channel. The channel delivers a copy to each receiver. See Publish/Subscribe Channel.

**Service registry.** A service registry and repository typically offers functionality such as discovery, versioning, and access control, among others. It can be custom-built or, more commonly, provided by a product in the SOA infrastructure. An ESB (enterprise service bus) is an example of an SOA infrastructure product, but buying one covers only one piece of the service-oriented system.

**Tolerant consumers.** A consumer can also help. A tolerant reader takes only the data it needs from a service. This aims to let providers make changes that ought not to break the consumer's code.

## Example

A shop publishes an "order placed" event. Billing and shipping both subscribe. Later, the team adds a loyalty-points service as a third subscriber. The shop's order code does not change, because it never knew who was listening.

## Trade-offs

Service-oriented systems generally favor interoperability and modifiability over optimal performance and strict security. See Quality Attribute Trade-off.
