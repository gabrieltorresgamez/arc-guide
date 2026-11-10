---
title: Enterprise Integration Patterns
slug: messaging-pattern-language
category: integration
kind: framework
summary: Enterprise Integration Patterns are named designs for connecting applications through messaging.
  Messaging is asynchronous, program-to-program communication with reliable delivery. Apache Camel supports
  most of these patterns.
arc42:
- 3
- 5
- 6
- 8
step: s08-integration-data
related:
- messaging
- message-channel
- point-to-point-channel
- dead-letter-channel
- file-transfer
- shared-database
- synchronous-vs-asynchronous-communication
- integration-pattern
checks:
- The document states which integration style connects each pair of applications (messaging, file transfer
  or shared database).
- Channels where each message must reach only one receiver are identified as point-to-point.
- A dead letter queue or equivalent exists for messages that cannot be delivered.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Introduction.html
  title: Introduction - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/enterprise-integration-patterns.html
  title: 'EIPs :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html
  title: Dead Letter Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Basic messaging flow with a dead letter queue for undeliverable messages.
review:
  status: generated
  flags: []
---

## Explanation

Enterprise Integration Patterns describe common ways to connect separate applications using messaging. Messaging is asynchronous, program-to-program communication with reliable delivery. Asynchronous means the sender does not wait for the receiver. See the article Synchronous vs. Asynchronous Communication.

**The basic flow**

1. The sender creates a message and puts it on a channel.
2. The receiver reads the message from the channel.
3. The receiver then extracts the data from the message.

A channel is the path a message travels. See Message Channel.

**Other integration styles**

Messaging is one of several ways to integrate applications. Two others are:

- **File Transfer:** one application writes a file, and another application reads it later.
- **Shared Database:** several applications use the same schema in one physical database.

**Example patterns: channels**

- A Point-to-Point Channel delivers each message to exactly one receiver.
- Several receivers can read from such a channel at the same time. They consume different messages, and only one of them gets any given message.
- A Dead Letter Channel (Dead Letter Queue) collects messages that cannot be delivered.

**Tool support**

Apache Camel is a framework that supports most of the patterns from the Hohpe and Woolf book.

## Example

An online shop has an order application and a shipping application. The order application puts each new order on a point-to-point channel. Two shipping workers read from that channel. Each order goes to only one worker. If an order cannot be delivered, it lands in a dead letter queue, where staff can inspect it.

## Trade-offs

Messaging is asynchronous, so the sender does not wait for the receiver. Delivery is meant to be reliable. A messaging system may move a message it cannot deliver to a dead letter channel.
