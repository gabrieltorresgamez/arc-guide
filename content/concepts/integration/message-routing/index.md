---
title: Message Routing
slug: message-routing
category: integration
kind: pattern
summary: Message routing patterns decide where each message goes, so a sender does not need to know the
  final recipient. Examples are the Content-Based Router, Recipient List, Aggregator, Scatter-Gather and
  Routing Slip.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- content-based-router
- recipient-list
- scatter-gather
- routing-slip
- message-filter
- dynamic-router
- process-manager
- composite-message-processor
checks:
- Where a message must reach a different system depending on its content, a Content-Based Router is used
  instead of the sender choosing the target.
- Every Aggregator that waits for replies defines a time-out strategy, so one missing message cannot block
  processing.
- Where one message must go to several recipients, a Recipient List sends a copy to each.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageRoutingIntro.html
  title: Introduction to Message Routing - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html
  title: Content-Based Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RecipientList.html
  title: Recipient List - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html
  title: Scatter-Gather - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html
  title: Routing Slip - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
  title: Aggregator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A router sends each message to a system based on its content, so the sender knows no addresses.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Message routing is a family of patterns that decouple a message source from the message's final destination. The sender hands over a message. The routing logic decides who receives it.

**Content-Based Router.** It sends each message to the right recipient based on what the message contains. This helps when one logical function is spread over several systems. See the article Content-based Router.

**Recipient List.** It computes a list of recipients. Then it sends a copy of the message to each one. Like the Content-Based Router, it normally leaves the message contents unchanged. See the article Recipient List.

**Aggregator.** It collects several messages into one. An Aggregator that waits for all replies has a weakness: one missing or delayed message can block the whole result. A time-out strategy avoids this. The Aggregator waits a set time, then decides with what has arrived.

**Scatter-Gather.** It uses an Aggregator to collect the responses into a single response message. See the article Scatter/Gather.

**Routing Slip.** It attaches the sequence of processing steps to each message. See the article Routing Slip.

## Example

An online shop receives orders. A router reads the product type in each order. It sends book orders to one system and electronics orders to another. The sender of the order knows neither system.

For a price check, the shop sends a copy of one request to three supplier systems. It then combines the answers into one reply. If one supplier is slow, the shop waits a set time and uses the answers it already has.

## Trade-offs

The main benefit: senders no longer need to know destinations.

One cost shows up in the Aggregator. If it waits for every reply, a single missing message blocks the result.
