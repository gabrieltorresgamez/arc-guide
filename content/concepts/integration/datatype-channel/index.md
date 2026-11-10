---
title: Datatype Channel
slug: datatype-channel
category: integration
kind: pattern
summary: A Datatype Channel gives each type of data its own message channel. The sender picks the channel
  that matches the data. The receiver knows the type from the channel it reads.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-channel
- selective-consumer
- format-identifier
- canonical-data-model
- messaging
- point-to-point-channel
- publish-subscribe-channel
- content-based-router
checks:
- Each data type that the system sends has its own channel, so all messages on one channel share one type.
- Senders have a documented rule for choosing the channel that matches the data type.
- Receivers take the data type from the channel they read, not from the message content.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DatatypeChannel.html
  title: Datatype Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSelector.html
  title: Selective Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html
  title: Message Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each data type travels on its own channel, so each receiver knows what it reads.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

An application that uses messaging often sends different kinds of data. The receiver must know how to process each item it gets (see Messaging).

The Datatype Channel pattern solves this with one channel per data type. Every message on a given channel then has the same type. A channel is a path that carries messages from sender to receiver (see Message Channel). In the Message Channel pattern, the messaging system already uses different channels for different kinds of information. Each channel has a specific purpose. This pattern applies that idea to data types.

Two roles follow from this:

- **The sender** knows the type of its data. It must pick the channel that matches that type.
- **The receiver** knows which channel a message arrived on. From the channel, it knows the type.

**Other ways to handle mixed data.** A Selective Consumer works differently. It reads a shared channel and filters out messages that do not match its criteria. With a Datatype Channel, the sender instead picks the channel that matches the data type.

The catalog also lists these related patterns: Canonical Data Model, Format Indicator, Message Dispatcher, Command Message, Selective Consumer and Message Channel.

## Example

An online shop sends orders and payment confirmations. The team creates one channel named "orders" and another named "payment-confirmations". The checkout service sends each order to "orders". The payment service sends each confirmation to "payment-confirmations". The shipping service reads only "orders". It treats every message there as an order.

## Trade-offs

The sender takes on the job of choosing the right channel for each message. The receiver knows the type of a message from the channel it arrived on. The source pages do not cover other costs or benefits.
