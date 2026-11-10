---
title: Command Query Responsibility Segregation
slug: command-query-responsibility-segregation
category: data-architecture
kind: pattern
summary: CQRS splits a system into a write side (commands) and a read side (queries), each with its own
  model. Teams can tune and scale each side separately, at the cost of extra complexity and possibly stale
  reads.
arc42:
- 4
- 5
- 8
- 9
- 11
step: s08-integration-data
related:
- event-sourcing-with-distributed-event-log
- bounded-context
- domain-event
- shared-database
- scalability
- domain-driven-design
- publish-subscribe-pattern
- technical-debt
checks:
- The document states which bounded contexts use CQRS rather than applying it to the whole system.
- The document explains how the read store is kept in sync with the write store, such as through events.
- The document accepts that the read side may show stale data and says where this is tolerable.
- The document justifies CQRS with a concrete benefit, such as read volume far above write volume, that
  outweighs the added complexity.
- Write permissions are restricted to the appropriate entities or operations.
sources:
- url: https://martinfowler.com/bliki/CQRS.html
  title: CQRS
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
  title: CQRS Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Commands go to the write side. Events update the read store. Queries use only the read side.
review:
  status: generated
  flags: []
---

## Explanation

Many systems treat information as one CRUD datastore. CRUD stands for create, read, update, and delete. One shared data model serves both reads and writes. This is simple and suits basic cases.

CQRS (Command Query Responsibility Segregation) takes a different path. It splits the model into an update model and a display model. The argument is that one shared model for both jobs grows more complex and serves neither well.

**Commands and queries**

- A command changes data. It should express a business task.
- A query never changes data. It returns data transfer objects (DTOs). These carry the needed data in a convenient shape and hold no domain logic.

**Separate stores**

The read and write sides can use separate data stores. Each store scales on its own. Each can also use a different storage technology. For example, a document database could serve reads while a relational database handles writes.

**Keeping the sides in sync**

A common approach is for the write side to publish an event whenever it updates its database. The read side consumes these events and refreshes its own data. A transactional outbox is recommended to avoid consistency problems.

Because the databases are separate, the read side can lag. Users may briefly see stale data. This is called eventual consistency.

**Link to event sourcing**

CQRS fits well with event-based programming models, so it can readily use event sourcing. In that combination, the event store acts as the write side and holds the one authoritative copy of the data. The read model builds materialized views from the events. Replaying the events can rebuild those views.

**When it helps**

- Reads greatly outnumber writes. The read model scales horizontally, and the write model can run on fewer instances.
- Security matters. Separating reads from writes lets you restrict write permissions to the appropriate domain entities or operations.

**Where to apply it**

Apply CQRS only to specific parts of a system, such as a bounded context (see the Bounded Context article), not to the whole system.

## Example

An online shop has a catalog with many visitors and few edits. Staff changes to products go through commands on a relational write store. Each change publishes an event. A read store, built for fast browsing, consumes the events and updates itself. Visitors query only the read store. After a price change, a visitor may briefly see the old price until the read store catches up.

## Trade-offs

- **Complexity.** The core idea is simple, but it can add significant complexity to the design. This is most true when combined with event sourcing.
- **Stale reads.** With separate databases, the read side may lag behind the write side.
- **Big mental shift.** Everyone involved must change how they think about the system. Adopt CQRS only when the benefit justifies the jump.
- **Poor fit for simple cases.** Simple domains and plain CRUD interfaces do not need it.
