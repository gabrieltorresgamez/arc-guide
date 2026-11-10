---
title: Format Indicator
slug: format-identifier
category: integration
kind: pattern
summary: A Format Indicator is a tag on each message that names its data format. It helps a message format
  cope with future change, and it is an alternative to giving every data type its own channel.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- datatype-channel
- content-based-router
- invalid-message-channel
- message-translator
- canonical-data-model
- message-channel
- envelope-wrapper
- dead-letter-channel
checks:
- The document states where the format identifier is carried (for example, payload prefix or header) and
  why.
- A router or other mechanism that reads the format identifier and sends messages to the right recipient
  is described.
- Messages with unknown or unprocessable formats have a defined destination, such as an invalid message
  channel.
- The choice between a format indicator and one channel per data type is explained.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/FormatIndicator.html
  title: Format Indicator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DatatypeChannel.html
  title: Datatype Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html
  title: Content-Based Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/InvalidMessageChannel.html
  title: Invalid Message Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.confluent.io/fr-fr/blog/schema-id-kafka-headers-data-governance/
  title: Introducing Schema IDs in Kafka Headers for Smarter Data Governance | FR
  site: confluent.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A router reads the format tag and sends each message to the matching receiver.
review:
  status: generated
  flags: []
---

## Explanation

Senders and receivers must agree on how data looks. The Format Indicator pattern asks how a message's data format can be designed so it can accommodate future changes. The approach is to mark each message with its format.

**The alternative: one channel per type.** A Datatype Channel (see the article of that name) gives each data type its own channel. Receivers infer the type from the channel they read. Datatype Channel is aimed at receivers knowing how to process different types of data, and it lists Format Indicator as a related pattern.

**Routing on content.** A Content-Based Router (see Content-based Router) inspects message content and sends each message to the right recipient.

**Unknown formats.** Some messages make no sense to a receiver. These go to an Invalid Message Channel (see Invalid Message Channel). That channel is a special one for messages that receivers could not process.

**Where to put the tag: a Kafka case.** In Kafka with Schema Registry, a numeric schema ID has traditionally been placed as a prefix in the payload. Adding such a prefix to existing topics can break legacy consumers that do not expect the extra bytes.

The alternative is to carry the schema ID in Kafka headers. The payload stays unchanged. Consumers that look in the headers first let producers and consumers avoid upgrading in lockstep during migration.

## Example

An order system sends order messages. Version 1 of the format has no discount field. Version 2 adds one. Each message carries a tag such as "order, v1" or "order, v2". A receiver that expects several formats uses the tag to know which one a message uses and how to interpret it.
