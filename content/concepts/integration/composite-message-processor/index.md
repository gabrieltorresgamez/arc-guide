---
title: Composed Message Processor
slug: composite-message-processor
category: integration
kind: pattern
summary: A Composed Message Processor keeps the overall message flow intact when one message holds several
  elements that may need different processing. An Aggregator gathers the results and decides when the
  combined answer is ready.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- scatter-gather
- content-based-router
- correlation-identifier
- process-manager
- message-routing
- messaging-pattern-language
checks:
- The document states the completeness condition that tells the Aggregator when to publish the combined
  result.
- The document says what happens when one reply is missing or delayed, since that blocks the whole aggregate.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DistributionAggregate.html
  title: Composed Message Processor - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
  title: Aggregator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html
  title: Scatter-Gather - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Some messages carry several elements, and those elements may need different handling. The Composed Message Processor pattern addresses this problem: how to keep the overall message flow intact while the elements are processed.

The gathering step relies on the Aggregator pattern. An Aggregator is a special kind of filter. It receives a stream of messages and works out which ones belong together.

The Aggregator needs a completeness condition. This rule decides when enough replies have arrived to publish the combined result.

A related pattern is Scatter-Gather. It broadcasts a message to several recipients and merges their responses back into one message. The pattern catalog lists Composed Message Processor as related to it. See also the articles on Scatter/Gather, Content-based Router and Correlation Identifier.

## Example

An order contains several items. Each item needs a different check before the order can be confirmed. The system collects the individual results and publishes one combined answer. It does this once its completeness rule says all results are in.

## Trade-offs

Waiting for all parts has a cost. A single missing or delayed reply blocks the whole aggregate, so further processing stops. Plan for this partial-failure risk when you define the completeness condition.
