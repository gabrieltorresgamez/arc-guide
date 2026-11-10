---
title: Aggregate Tactic
slug: aggregate-tactic
category: tactics
kind: tactic
summary: 'The aggregate tactic follows the bulk idea: handle many items in one operation instead of one
  by one. At service level, the same idea appears as a request bundle. It is unrelated to the DDD aggregate
  and the Aggregator pattern.'
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- usability-tactics
- usability
- architectural-tactic
- aggregate
- patterns-for-api-design
- messaging-pattern-language
- performance-tactics
checks:
- Where a service offers bulk operations, the API bundles several independent requests into one message
  to reduce round trips.
- Long-running bulk operations offer a Cancel option that is easy to find and quick to use.
- Bulk operations have an undo or other way to correct mistakes.
- The document does not confuse the user-facing aggregate tactic with the DDD aggregate or the Aggregator
  integration pattern.
sources:
- url: https://microservice-api-patterns.org/patterns/quality/dataTransferParsimony/RequestBundle.html
  title: Request Bundle
  site: microservice-api-patterns.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/DDD_Aggregate.html
  title: D D D_ Aggregate
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
  title: Aggregator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.nngroup.com/articles/user-control-and-freedom/
  title: 'User Control and Freedom (Usability Heuristic #3) - NN/G'
  site: nngroup.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

**Request Bundle.** The Request Bundle pattern packs several independent requests into one message. The goal is fewer requests and responses, which makes communication more efficient.

**Link to the Command pattern.** Request Bundle can be seen as an extension of the Command pattern: each item in a bundle is a command in the sense of that pattern.

**Two similar names.**
- A DDD aggregate is a cluster of domain objects treated as one unit. See the article "Aggregate".
- The Aggregator is an integration pattern. It is a stateful filter that collects related messages until a complete set has arrived, then publishes a single message.

## Example

A support team wants to close 200 resolved tickets. The interface lets them select all 200 and apply one "close" action. The backend accepts one message that holds 200 close requests instead of 200 separate messages.

## Trade-offs

The goal of bundling is to reduce the number of requests and responses, which aims to make communication more efficient.
