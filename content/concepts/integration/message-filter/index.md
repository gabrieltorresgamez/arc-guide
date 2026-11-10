---
title: Message Filter
slug: message-filter
category: integration
kind: pattern
summary: A Message Filter checks each message against a condition on its content. Matching messages move
  on and the rest are discarded, so a component avoids receiving messages it does not care about.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-routing
- content-based-router
- content-filter
- message-channel
- dead-letter-channel
- invalid-message-channel
- selective-consumer
- pipes-and-filters
checks:
- Each filter in the design states the content criteria that decide whether a message passes.
- 'The design states what happens to messages that do not match: dropped, sent to a discard channel, or
  raised as an error.'
- Each filter has a single output channel.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html
  title: Message Filter - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/filter-eip.html
  title: 'Filter :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://docs.spring.io/spring-integration/reference/filter.html
  title: 'Filter :: Spring Integration'
  site: docs.spring.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A Message Filter passes matching messages to its single output channel and discards the rest.
review:
  status: generated
  flags: []
---

## Explanation

A component sometimes receives messages it has no interest in. The Message Filter addresses this problem. It is a small processing step placed in front of that component.

**How it works**

The filter reads the content of each incoming message and compares it with a set of criteria. If the message matches, the filter passes it on. If not, the filter discards it.

The filter is a special kind of router, and it has only one output channel. A router sends messages onward to a destination. See Message Routing for the wider family. A channel is the path messages travel along. See Message Channel.

**In common frameworks**

- In Apache Camel, the filter uses a predicate. A predicate is a test that answers true or false. Only messages with a true result continue. Messages with a false result are not routed further.
- In Spring Integration, the filter decides whether to pass or drop a message. It can look at a header value or at the message content.

**What happens to rejected messages**

Spring Integration offers choices beyond a silent drop:

- Send rejected messages to a dedicated discard channel.
- Raise an error when a message is rejected.

## Example

An order system publishes every order event to one channel. A shipping component only cares about orders marked "ready to ship". A filter in front of shipping checks each event. Ready orders pass through. All other events are discarded, or sent to a discard channel for review. The shipping component never sees the other events.

## Trade-offs

A message that fails the condition is gone unless the design routes it to a discard channel or raises an error.
