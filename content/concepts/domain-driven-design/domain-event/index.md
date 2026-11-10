---
title: Domain Event
slug: domain-event
category: domain-driven-design
kind: concept
summary: A domain event records something that happened in the business and that other parts of the domain
  need to know about. It is named in the past tense, never changes, and can trigger reactions in other
  aggregates or bounded contexts.
arc42:
- 5
- 6
- 8
- 12
step: s06-domain
related:
- aggregate
- bounded-context
- domain-model
- event-sourcing-with-distributed-event-log
- entity-life-cycle
- ubiquitous-language
- domain-driven-design
- synchronous-vs-asynchronous-communication
checks:
- Domain events are named with past-tense verbs and are immutable.
- Domain events used inside one domain model are distinguished from integration events that cross bounded
  contexts.
- Integration events sent to other bounded contexts are asynchronous.
- Aggregates raise events, and dispatch is deferred until the transaction commits.
sources:
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation
  title: 'Domain events: Design and implementation - .NET | Microsoft Learn'
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaDev/DomainEvent.html
  title: Domain Event
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: An aggregate raises an event; handlers react in the same domain or forward an integration event
    to another bounded context.
review:
  status: generated
  flags: []
---

## Explanation

A domain event is a record of something that already happened in the business domain. Other parts of the same domain are meant to learn about it and react. It captures things that can trigger a change in the state of the application.

**Naming and immutability.** The event happened in the past, so its name uses a past-tense verb, such as "order shipped". The event must not change after it is created. Events can also carry time information and a type.

**Source data.** An event can hold the unchanging data of the outside trigger. This data stays separate from the changeable data used while processing it.

**Reacting inside one domain.** Domain events spread state changes and side effects across several aggregates in the same domain model.

**Raising events.** An aggregate adds an event to a list on itself when something happens. The events are dispatched later, either right before or right after the transaction commits. This keeps raising an event separate from handling it.

**Eventual consistency.** Vaughn Vernon's view is that an aggregate method publishes an event to asynchronous subscribers. Other aggregates then catch up over time instead of instantly.

**Crossing context boundaries.** Integration events are semantically the same as domain events, but their implementation differs. They carry committed changes to other microservices, bounded contexts, or external applications, and they must be asynchronous because they rely on communication between processes. A domain event handler can create an integration event and send it to an event bus. See the article Bounded Context.

**Link to event sourcing.** If all inputs are funneled into streams of events, they keep a record of all system inputs, and the event log supports audit. The domain event pattern is also necessary for event sourcing.

## Example

An online shop has an order aggregate. When the customer pays, the order raises an "order paid" event with the order number and the time. After the transaction commits, a handler in the stock area reacts and reserves items. Another handler turns the event into an integration event for a separate shipping service. The order code does not know about either handler.

## Trade-offs

Separating the raising of events from their dispatch keeps the raising code decoupled from its reactions. Dispatching after the commit means multiple transactions, so eventual consistency must be handled. Domain events and integration events need different implementations.
