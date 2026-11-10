---
title: Content Filter
slug: content-filter
category: integration
kind: pattern
summary: A Content Filter removes unimportant data items from inside a message and keeps only the important
  ones. It helps when a message is large and the receiver needs just a few items.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-filter
- content-enricher
- content-based-router
- message-translator
- messaging-pattern-language
- pipes-and-filters
- claim-check
- message-structure
checks:
- Where a consumer needs only a few items from a large message, the document names a Content Filter that
  removes the other items.
- The document distinguishes removing data inside a message (Content Filter) from dropping whole messages
  (Message Filter).
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html
  title: Content Filter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html
  title: Message Filter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DataEnricher.html
  title: Content Enricher - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A Content Filter removes data items inside one message; the message still moves on.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A Content Filter is a pattern from Enterprise Integration Patterns (see the article of that name). It answers one question: how do you simplify handling a large message when you care about only a few data items?

The answer is to remove the unimportant data items from the message. Only the important items stay. The message itself is still delivered. It is just smaller and simpler.

**How it differs from related patterns**

- **Message Filter** works at the channel level. It removes whole messages that a component does not want to receive. A Content Filter removes data inside a message instead.
- **Content Enricher** is the opposite. It is a specialized transformer that adds missing information from an external source. A Content Filter takes information away.

A simple way to remember it: a Message Filter decides which messages pass. A Content Filter decides which parts of a message pass.

## Example

An order system sends a large order message with customer details, line items, notes and shipping data. A billing component needs only the order number and the total. A Content Filter sits in front of billing. It keeps those two items and removes the rest. Billing receives a smaller message.

## Trade-offs

The pattern works by discarding data items from a message. Once removed, they are no longer in that message. Decide carefully which items are truly unimportant for the receiver.
