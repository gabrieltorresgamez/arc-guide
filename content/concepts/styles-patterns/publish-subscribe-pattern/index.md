---
title: Publish-Subscribe Pattern
slug: publish-subscribe-pattern
category: styles-patterns
kind: pattern
summary: Publish-subscribe lets a sender announce events without knowing who receives them. A broker or
  event bus copies each event to every interested subscriber. Senders and receivers stay independent,
  at the cost of latency, weaker ordering, and harder tracing.
arc42:
- 5
- 6
- 8
- 11
step: s08-integration-data
related:
- publish-subscribe-channel
- broker-pattern
- messaging
- correlation-identifier
- loose-coupling
- modifiability
- message-channel
- synchronous-vs-asynchronous-communication
checks:
- The document names the broker or event bus that sits between publishers and subscribers.
- The document states whether subscribers select messages by topic or by content filtering.
- Subscribers are designed to tolerate messages arriving in any order.
- Publishers and subscribers are authenticated and authorized per topic, and messages are encrypted.
- Correlation IDs or similar means exist to trace a message end to end.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber
  title: Publisher-Subscriber Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/articles/201701-event-driven.html
  title: What do you mean by “Event-Driven”?
  site: martinfowler.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: A publisher sends one event to the broker, which delivers a copy to each subscriber.
review:
  status: generated
  flags: []
---

## Explanation

In publish-subscribe (often called pub/sub), a sender publishes an event without knowing which consumers will receive it. A middle layer handles delivery. It is usually a message broker or an event bus.

**The elements**

- **Publisher:** the sender. It puts events on one input channel.
- **Subscribers:** the receivers. Each one has its own output channel.
- **Broker or event bus:** the intermediary. It copies each message from the input channel to the output channel of every subscriber that is interested in it.

The channel delivers a copy of each event to each subscriber. See Publish/Subscribe Channel for the messaging view of this idea.

**Why use it**

Without pub/sub, adding or removing a consumer forces a change to the sender. That limits how independently teams can develop and deploy their parts. Pub/sub decouples the sender from its consumers, so the sender can publish without knowing who receives the events.

**How subscribers choose what they get**

- **By topic:** each topic has its own channel, and subscribers pick the topics they want.
- **By content:** the broker inspects each message and delivers it based on what the subscriber asked for.

**Security**

Authenticate and authorize both publishers and subscribers for each topic. An unauthorized publisher that sends in messages can do as much harm as an unauthorized subscriber that reads them. Encrypt messages in transit, and encrypt them at rest in the broker if the content is sensitive.

## Example

An online shop publishes an "order placed" event. A billing service, a warehouse service, and an email service each subscribe to it. Each gets its own copy. Later, the team adds an analytics service as a new subscriber. The shop's ordering code does not change.

## Trade-offs

- **Latency:** the broker adds delay. Pub/sub is a poor fit when consumers need near real-time interaction.
- **Ordering:** subscribers may receive messages in a different order than the sender created them. Design subscribers to handle messages independently of arrival order.
- **Traceability:** decoupling makes the end-to-end flow of a message harder to follow. Correlation IDs help. See Correlation Identifier.

