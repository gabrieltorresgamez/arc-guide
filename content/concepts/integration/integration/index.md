---
title: Integration
slug: integration
category: integration
kind: concept
summary: Integration makes separate applications work together to deliver one unified set of functionality.
  Teams choose a style, keep dependencies low, and often add a translation layer where systems differ.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- integration-pattern
- file-transfer
- shared-database
- remote-procedure-call
- messaging
- loose-coupling
- synchronous-vs-asynchronous-communication
- interoperability
checks:
- The document names the integration style used between each pair of systems (file transfer, shared database,
  remote procedure call or messaging).
- Where a legacy or external system is integrated, the document says how its semantics are kept out of
  the new design, for example with an anti-corruption layer.
- The document states whether each interaction is synchronous or asynchronous.
- The document records the added latency, extra operations effort and consistency monitoring of any anti-corruption
  layer.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer
  title: Anti-Corruption Layer Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A translation layer sits between a new system and a legacy or external system.
review:
  status: generated
  flags: []
---

## Explanation

Integration is the task of making separate applications work together. The goal is a unified set of functionality that no single application delivers alone.

**Four common styles**

- **File transfer:** each application writes files of shared data. Others read them.
- **Shared database:** applications keep the data they share in one common database.
- **Remote procedure call:** an application exposes some of its procedures. Other applications call them remotely.
- **Messaging:** each application connects to a common messaging system.

The articles *File Transfer*, *Shared Database*, *Remote Procedure Call*, *Messaging* and *Integration Styles* cover these in more depth.

**Keep coupling low**

Coupling describes how much applications assume about each other. Tightly coupled applications make many assumptions about how the others work. Integrated applications should keep their mutual dependencies to a minimum. See *Loose Coupling*.

**Synchronous and asynchronous**

Applications may not want to wait for a remote call to finish. A source application can make data available or log a request, then go on to other work. An anti-corruption layer can also use an asynchronous, event-driven approach with message services, which decouples the modern system from the legacy system's throughput constraints. See *Synchronous vs. Asynchronous Communication*.

**Legacy and external systems**

The features and technologies of legacy systems can vary widely from those of modern systems. If a new system integrates with one directly, it may have to adopt some of the legacy system's APIs or other semantics. When those legacy features have quality problems, this corrupts the new system's design. Similar problems arise with any external system your team does not control.

An anti-corruption layer addresses this. It is a facade or adapter between subsystems that do not share the same semantics. It translates the requests one subsystem makes to the other. Outside dependencies then do not constrain the design of your application. One system can stay unchanged without compromising the design of the other.

## Example

A new online shop must show stock levels held in an old warehouse system. The warehouse system uses its own codes and data layout. The shop team adds a translation layer between the two. The layer converts warehouse codes into the shop's own terms. The warehouse system stays unchanged, and the shop keeps its own design. The team can call the layer directly and wait for an answer. Or they can have the warehouse publish stock changes as events that the layer picks up later.

## Trade-offs

Each style and each choice has a price.

- Tight coupling makes applications depend on assumptions about each other. Reducing those assumptions is the aim of good integration.
- An anti-corruption layer protects design, but it adds latency to calls between the two systems. It is also an extra service to operate.
- Synchronous request-response and asynchronous event-driven communication suit different needs.
