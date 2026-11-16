---
title: Software Connector
slug: software-connector
category: fundamentals
kind: concept
summary: A connector is the element of an architecture description that stands for an interaction between
  components. It plugs into component ports, and its interface is a set of roles, one per participant.
arc42:
- 5
- 6
step: s10-document
related:
- uml-component-diagram
- component-view
- classification-of-integration-patterns
- connector-transparency
checks:
- Interactions between components are shown as explicit connectors in the architecture description.
- Each connector names its roles, so each participant in the interaction is identifiable.
- Each connector plugs into identified ports of the components it joins.
sources:
- url: https://arxiv.org/html/cs/0105009
  title: Using Dependence Analysis to Support Software Architecture Understanding
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://ar5iv.arxiv.org/html/1608.03324
  title: '[1608.03324] Architecture Diagrams: A Graphical Language for Architecture Style Specification'
  site: ar5iv.arxiv.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/handle-partial-failure
  title: Handling partial failure - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/distributed-objects-microservices.html
  title: Microservices and the First Law of Distributed Objects
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A connector joins the ports of two components. Each end of the connector is a role.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Software is built from parts called components. Components rarely work alone. They interact. An architecture description needs a way to show these interactions. That is the job of a **connector**.

A connector represents an interaction between components.

**Ports.** A component has ports. A port is a point where the component interacts with its environment. Connectors plug in at these points. The article *Port* covers ports in more detail.

**Roles.** A connector has an interface, just as a component does. The connector's interface is a set of roles. Each role is one participant in the interaction. A connector for an interaction between two parties therefore has a role for each side.

Putting the pieces together:

- Components own the ports.
- Connectors own the roles.
- Plugging a connector into a port ties a component into the interaction.

This keeps two questions apart. Components answer "what are the parts?" Connectors answer "how do the parts interact?"

**More about connectors.**

- **Connector Cardinality:** A point-to-point connector links two. A multicast connector delivers to several components through one shared channel.
- **Connectors and Distribution:** A monolith can only be copied and run as several identical instances. Splitting a system into separate processes adds a new risk: a call to another process may be slow or fail while the rest keeps running.

## Example

Imagine a small shop system with two components: an "Order Service" and a "Payment Service". The Order Service has a port where it asks for payments. The Payment Service has a port where it receives payment requests. A connector joins the two ports. It has two roles: one for the party that asks and one for the party that answers. In a diagram, you would draw this as a line between two boxes.
