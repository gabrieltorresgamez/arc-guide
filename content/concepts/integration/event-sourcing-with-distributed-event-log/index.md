---
title: Event Sourcing with Distributed Event Log
slug: event-sourcing-with-distributed-event-log
category: integration
kind: pattern
summary: A distributed event log is a shared, append-only record of events that many applications use
  to exchange data. Writers add events. Readers pull them at their own pace and can replay older events
  until retention removes them.
arc42:
- 3
- 5
- 6
- 8
- 9
- 11
step: s08-integration-data
related:
- shared-database
- command-query-responsibility-segregation
- idempotent-receiver
- integration-pattern
- domain-event
- publish-subscribe-channel
- messaging
- stream
checks:
- The document states the retention period of the event log and what that means for replay.
- Consumers are described as idempotent, because delivery is typically at-least-once.
- Events that must stay in order share a partition key, and the document states where order is not guaranteed.
- How each consumer tracks its position (offset or checkpoint) is documented.
- If a broker is the system of record, the document explains how it covers per-entity queries and optimistic
  concurrency.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html
  title: Shared Database - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
  title: Event Sourcing Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-features
  title: Event Hubs features and terminology - Azure Event Hubs | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaDev/EventSourcing.html
  title: Event Sourcing
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/CQRS.html
  title: CQRS
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Writers append to one log; each consumer group pulls from its own position.
review:
  status: generated
  flags: []
---

## Explanation

The classic Shared Database style (see the article Shared Database) has applications store their data in one common database. This article looks at an event log as an integration medium.

**Event sourcing in brief.** Event sourcing stores every change to application state as a sequence of events. The log can rebuild the current state. Replaying it from a blank state up to a chosen time or event also reconstructs past states.

**How the log works as an integration medium.** The log is append-only. Writers add events and do not edit old ones. The code that produces events does not know which systems consume them.

In Azure Event Hubs, an event hub is an append-only log, equivalent to a Kafka topic, and consumers pull events rather than having them pushed to them. Each consumer group is an independent view of the stream and tracks its own position.

**Replay.** A consumer can start at a specific offset (a position in the log), at a timestamp, or at the beginning or end. If it saves its position (a checkpoint), it can resume after a failure. It can also replay historical events by choosing an earlier offset.

**Retention.** Retention is time-based and configurable up to a tier maximum. The platform then removes events automatically. Nobody can delete them explicitly.

**Ordering.** Order is guaranteed only within a partition, which is one ordered sequence of events inside the log. A partition key keeps related events together and in order. Demanding absolute order across all events limits how many partitions you can use.

**Relation to other patterns.** CQRS (see Command Query Responsibility Segregation) pairs naturally with event sourcing. If the write model emits events for every update, read models can be built from them. Fowler also describes event sourcing as the foundation for patterns such as Parallel Models and Retroactive Events.

## Example

An online shop writes "order placed", "order paid" and "order shipped" events to one log, using the order number as partition key. A billing service and a reporting service each read the log with their own position. Reporting breaks for a day. After the fix, it resumes from its saved position and catches up, as long as those events are still within retention.

## Trade-offs

- **Retention limits replay.** Events disappear after the retention period, and they cannot be deleted on demand.
- **Ordering is partial.** Order holds only within a partition. Demanding global order limits how many partitions you can use.
- **A broker is not a full event store.** A broker such as Kafka typically lacks per-entity stream queries and optimistic concurrency. It mainly distributes events.
- **Duplicates are possible.** Delivery is typically at-least-once, so consumers must be idempotent (see Idempotent Receiver).
- **Decoupling.** Producers do not depend on subscribers, which lets you add new readers without changing writers.
