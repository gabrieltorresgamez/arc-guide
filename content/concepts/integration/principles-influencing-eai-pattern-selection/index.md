---
title: Principles Influencing EAI Pattern Selection
slug: principles-influencing-eai-pattern-selection
category: integration
kind: principle
summary: Pick an integration style by asking how tightly it ties applications together. Prefer styles
  that keep mutual dependencies low, so one application can change without breaking the others.
arc42:
- 4
- 8
- 9
step: s08-integration-data
related:
- loose-coupling
- coupling-and-cohesion
- design-for-change
- shared-database
- messaging
- message-translator
- integration-pattern
- file-transfer
checks:
- The document names which integration style (file transfer, shared database, remote procedure invocation
  or messaging) connects each pair of applications.
- The document states how much each integration choice makes applications depend on each other.
- Any shared database between applications is justified, including the risk it adds when applications
  change.
- Where messaging is used, the document says how it removes dependence on time and data format.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html
  title: Shared Database - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html
  title: Messaging - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/IntegrationDatabase.html
  title: Integration Database
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Enterprise application integration (EAI) offers four integration styles: file transfer, shared database, remote procedure invocation and messaging. See the articles on Integration Styles and Enterprise Integration Patterns for the full picture.

Coupling is a main criterion for choosing among them. Even integrated applications should depend on each other as little as possible. Tightly coupled applications make many assumptions about how the other applications work. The more assumptions, the harder it is to change one application alone. See Loose Coupling and Coupling and Cohesion.

Two styles show the difference clearly.

**Shared database.** Several applications use one common schema (the structure of the stored data). Designing one schema that meets the needs of many applications is very difficult. It is also awkward for developers. Martin Fowler describes an integration database as a point of deep coupling. It raises the risk of changing any application that uses it. This works against Design for Change.

**Messaging.** Applications connect to a common messaging system. They exchange data and invoke behavior through messages. This loosens two kinds of coupling:

- *Time.* Sender and receiver do not need to be up at the same moment.
- *Data format.* Messages can be translated in transit, and neither side needs to know.

Use the principles as a filter. For each style, ask which assumptions it forces on the applications. Then choose the pattern that keeps those assumptions few.

## Example

A shop's order system and warehouse system must share order data.

Option A: both read and write one common database. A change to the order table can break the warehouse system. The team must agree on one schema for both.

Option B: the order system sends messages through a messaging system. The warehouse system reads them when it is running. If the formats differ, a translator converts them on the way, and neither system knows.

Option B leaves each system freer to change.

## Trade-offs

Loose coupling gains independent change, no need for both systems to be up, and no need to share one format. Weigh the gains above against your own needs before choosing.
