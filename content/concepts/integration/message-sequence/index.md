---
title: Message Sequence
slug: message-sequence
category: integration
kind: pattern
summary: Message Sequence splits data that is too big for one message into several smaller messages. Each
  message carries a position, so the receiver can put the parts back in order and rebuild the whole.
arc42:
- 5
- 6
- 8
- 9
step: s08-integration-data
related:
- claim-check
- correlation-identifier
- message-channel
- messaging
- composite-message-processor
- idempotent-receiver
- message-structure
- messaging-pattern-language
checks:
- The document names the message size limit that makes splitting necessary.
- Each message in a sequence carries a position identifier that orders it.
- The design states how out-of-order arrivals are buffered and reordered before processing.
- The design states what happens when parts are missing, such as waiting for all parts or a timeout.
- The design explains why Message Sequence was chosen over Claim Check, including duplicate handling and
  reassembly effort.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSequence.html
  title: Message Sequence - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html
  title: Resequencer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
  title: Aggregator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check
  title: Claim Check pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A large payload is split into numbered parts, sent through a channel and rebuilt by the receiver.
review:
  status: generated
  flags: []
---

## Explanation

Sometimes an application must send more data than fits in a single message. Messaging systems often limit message size, and large messages can also slow the system down. Message Sequence is one way to handle this.

The idea is simple. The sender cuts the data into parts and sends each part as its own message. Every message carries a position identifier. That identifier uniquely identifies the message and fixes its place in the order.

**Putting the parts back together**

Two related patterns help the receiver:

- The Aggregator receives a stream of messages, finds the ones that belong together (see Correlation Identifier) and combines them.
- The Resequencer receives a stream that may arrive out of order. It holds early arrivals in an internal buffer. When a complete sequence is available, it publishes the messages in order.

**Missing parts**

A part may never arrive. One completeness strategy is to wait for all parts. If they do not all arrive within a time-out period, the Aggregator raises an error.

**Alternative: Claim Check**

The Claim Check pattern stores the full payload in an external data store. Only a reference travels through the messaging system.

## Example

An export job produces a very large report, and the channel accepts only small messages. The sender cuts the report into numbered chunks and sends them all. The receiver buffers the chunks, joins them in order and hands over the complete report. If a chunk does not arrive before the timeout, the receiver raises an error.

## Trade-offs

Splitting keeps the data inside the messaging system. The price is extra design work: sequencing, correlation, duplicate handling and reassembly.

Claim Check has its own costs. It adds extra network trips compared with sending the data inline. It also makes the system depend on an external store.
