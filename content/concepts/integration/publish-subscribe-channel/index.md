---
title: Publish/Subscribe Channel
slug: publish-subscribe-channel
category: integration
kind: pattern
summary: A publish-subscribe channel gives every interested subscriber its own copy of each message. The
  sender does not know who the receivers are, so senders and receivers stay decoupled.
arc42:
- 3
- 5
- 6
- 8
step: s08-integration-data
related:
- point-to-point-channel
- publish-subscribe-pattern
- message-channel
- messaging
- idempotent-receiver
- event-driven-consumer
- broker-pattern
- loose-coupling
checks:
- The document states which subscribers need durable subscriptions so they do not lose messages while
  disconnected.
- The document explains how subscribers handle duplicate messages, for example by being idempotent.
- The document states whether any consumer relies on the order of messages across subscribers.
- The document describes how topics are divided and how subscribers filter messages.
- The document distinguishes channels where every subscriber gets a copy from channels where only one
  receiver consumes each message.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber
  title: Publisher-Subscriber Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DurableSubscription.html
  title: Durable Subscriber - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.oracle.com/javaee/7/tutorial/jms-concepts003.htm
  title: '45.3 The JMS API Programming Model - Java Platform, Enterprise Edition: The Java EE Tutorial
    (Release 7)'
  site: docs.oracle.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A publisher writes once to a topic. Each subscriber receives its own copy.
review:
  status: generated
  flags: []
---

## Explanation

A sender often needs to broadcast an event to all interested receivers. A publish-subscribe channel solves this problem.

**How it works.** The sender publishes an event without knowing which consumers will receive it. A broker (a middleware component that moves messages between systems) copies each message from the input channel to the output channel of every interested subscriber.

**Contrast with a queue.** In a point-to-point channel (see the article Point-to-Point Channel), only one receiver consumes a given message. This holds even when several receivers listen. With plain queues, serving many consumers means creating one queue per consumer. That adds routing complexity and does not scale well. Pub/sub avoids this by copying messages.

**Topics in JMS.** In JMS (the Java messaging API), pub/sub destinations are called topics. Each subscription receives a copy of every message sent to the topic after the subscription is created. A message selector can filter messages out.

**Subscribers that are offline.** A nondurable JMS subscription exists only while an active consumer is attached. A subscriber that is disconnected misses messages. A durable subscriber changes this. The messaging system saves messages published while the subscriber is disconnected, so nothing is lost. JMS persists durable subscriptions and lets them collect messages until they are deleted. It recommends them when an application must receive every message.

**Fault isolation.** If a subscriber fails, the publisher and the other subscribers are not affected. The broker keeps the messages until the subscriber recovers and is ready to process them.

## Example

An online shop publishes an "order placed" event to a topic. A billing service, a warehouse service, and an email service each subscribe. Each one gets its own copy of every event. The shop later adds a fourth subscriber. The publisher does not change, because it never knew who was listening. If the email service goes down, the broker holds its messages until it returns. Billing and warehouse keep working.

## Trade-offs

- **Ordering.** The order in which subscribers receive messages is not guaranteed. It may differ from the order in which the sender created them. Ordered delivery within a partition or session limits scalability.
- **Duplicates.** At-least-once delivery guarantees arrival but can produce duplicates. If the broker does not remove duplicates, subscribers should tolerate them (see Idempotent Receiver).
- **Filtering.** Subscribers can filter through topics or content filtering. Broad topics are easier to manage but force subscribers to discard unwanted messages. Narrow topics reduce that work but increase the number of topics to manage. Some brokers also support wildcard subscriptions.
- **Missed messages.** Nondurable subscribers lose messages sent while they are inactive. Durable subscriptions prevent this.
