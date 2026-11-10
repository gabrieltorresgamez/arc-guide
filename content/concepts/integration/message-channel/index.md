---
title: Message Channel
slug: message-channel
category: integration
kind: pattern
summary: A message channel is a pipe between applications. One application writes messages into it, and
  another reads them out. The sender does not need to know the receiver. Channel types cover delivery,
  message types, errors, and durability.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- point-to-point-channel
- publish-subscribe-channel
- datatype-channel
- dead-letter-channel
- invalid-message-channel
- messaging
- messaging-pattern-language
- message-routing
checks:
- The document states whether each channel is Point-to-Point (one receiver per message) or Publish-Subscribe
  (a copy per subscriber).
- Each channel carries one data type, so receivers can tell the message type from the channel.
- Non-messaging applications are connected through a Channel Adapter.
- The document describes how undeliverable messages are handled, such as with a Dead Letter Channel, and
  how this works in the chosen messaging system.
- Where messages must survive a messaging system crash, the document states that Guaranteed Delivery is
  used.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html
  title: Message Channel - Enterprise Integration Patterns
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
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DatatypeChannel.html
  title: Datatype Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html
  title: Channel Adapter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html
  title: Dead Letter Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedMessaging.html
  title: Guaranteed Delivery - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html
  title: Message Bus - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A publish-subscribe channel: one input channel splits into one output channel per subscriber.'
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A message channel is a pipe in a messaging system. One application writes information into the channel. Another application reads it from the channel. The sender does not need to know which application will pick the message up.

**Choosing who receives a message**

- A *Point-to-Point Channel* makes sure only one receiver gets each message. Because the channel ensures only one receiver succeeds with each message, receivers do not have to coordinate with each other. See Point-to-Point Channel.
- A *Publish-Subscribe Channel* delivers a copy of each event to every subscriber. Inside, it has one input channel that splits into one output channel per subscriber. See Publish/Subscribe Channel.

**Organizing messages by type**

A *Datatype Channel* uses one channel per data type. The receiver then knows the type of a message from the channel it arrived on. See Datatype Channel.

**Connecting applications**

A *Channel Adapter* connects an application to the messaging system. The adapter works through the application's API or data. It acts as a messaging client and publishes messages on a channel.

**Handling problems**

- A *Dead Letter Channel* takes messages the system cannot or should not deliver. Exactly how it works depends on the messaging system. See Dead Letter Channel.
- *Guaranteed Delivery* stores messages in a built-in data store. They then survive a crash of the messaging system. A send only completes once the message is safely stored in the sender's data store.

**Sharing channels across applications**

A *Message Bus* brings together a shared data model, a shared set of commands and a messaging infrastructure. Together they act as shared channel middleware between applications.

## Example

An online shop has an order application and several other systems. The order application writes each new order to a channel. If only one worker should process each order, the shop uses a point-to-point channel. If billing, shipping, and reporting all need to see the order, it uses a publish-subscribe channel. The order application does not know who reads its messages. A separate channel holds only invoices, so readers know what they receive.

## Trade-offs

Channels let the sender stay unaware of which application will receive its messages.

Some choices depend on the messaging system:

- Guaranteed Delivery protects messages from crashes. A send does not complete until the message is stored safely.
- A Dead Letter Channel behaves differently in each messaging system. Check what your system does.
