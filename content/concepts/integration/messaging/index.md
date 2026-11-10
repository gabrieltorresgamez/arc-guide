---
title: Messaging
slug: messaging
category: integration
kind: pattern
summary: Messaging connects applications through a shared messaging system. Applications exchange small
  messages instead of calling each other directly, and sender and receiver need not be running at the
  same time.
arc42:
- 3
- 5
- 6
- 8
step: s08-integration-data
related:
- message-channel
- point-to-point-channel
- publish-subscribe-channel
- content-based-router
- idempotent-receiver
- file-transfer
- integration-pattern
- messaging-pattern-language
checks:
- The document states which channels are point-to-point (one consumer per message) and which are publish-subscribe
  (a copy to each receiver).
- The document states the delivery guarantee in use and whether messages are persisted until acknowledged.
- Consumers that can see duplicate messages say how they ignore them, for example with a stable deduplication
  key.
- Where message order matters, the document names the mechanism, such as sessions or sequence/version
  data.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html
  title: Messaging - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedMessaging.html
  title: Guaranteed Delivery - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html
  title: Content-Based Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer
  title: Idempotent Consumer Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A sender hands a message to the messaging system, which stores it until the receiver acknowledges
    it.
review:
  status: generated
  flags: []
---

## Explanation

Messaging is an integration style: applications connect to a common messaging system. They exchange data and invoke behavior by sending messages through it. It is a pragmatic reaction to the problems of distributed systems (see Integration Style).

**Decoupling in time.** The two systems do not both have to be running and ready when a message is sent.

**Looser links.** Messaging keeps much of the decoupling that file transfer offers. The messaging system can also change a message in transit. Neither sender nor receiver needs to know about that change.

**Channels.** Messages travel over channels (see Message Channel). Two kinds of channel are:

- A point-to-point channel makes sure only one receiver consumes each message (see Point-to-Point Channel).
- A publish-subscribe channel announces an event by delivering a copy to every receiver (see Publish/Subscribe Channel).

**Routing.** A content-based router looks at each message and sends it to the right recipient channel based on its content (see Content-based Router).

**Delivery guarantees.** Guaranteed Delivery stores messages on disk until the receiver acknowledges them. They then survive a crash of the messaging system. Most brokers offer at-least-once delivery, so duplicates can occur. Exactly-once delivery across a distributed system is impractical.

**Duplicates and order.** A producer may send a message, miss the acknowledgment because of a network fault or timeout, and send it again. The broker then holds two copies. A consumer that ignores duplicates, using a stable deduplication key, achieves effectively-once processing (see Idempotent Receiver). Deduplication does not guarantee order. Ordering needs sessions or sequence/version data so the consumer can reject stale messages.

## Example

An online shop sends an "order placed" message. The messaging system stores it. The invoicing system is down for maintenance, so it reads the message later when it is back. The shop never waited for it. If the shop resends the message because an acknowledgment was lost, invoicing checks the order number and ignores the second copy.

## Trade-offs

Messaging gives decoupling in time and lets messages be transformed in transit without the sender or receiver knowing.

The guarantees have limits. At-least-once delivery means duplicates, so consumers must handle them. Exactly-once is impractical across a distributed system. Removing duplicates does not restore order, so ordering needs extra data or sessions.
