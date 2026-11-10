---
title: Scatter/Gather
slug: scatter-gather
category: integration
kind: pattern
summary: Scatter-Gather sends one request to several recipients, then combines their replies into a single
  answer. The caller sees one response instead of many.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- publish-subscribe-channel
- recipient-list
- messaging-pattern-language
- message-routing
- request-reply
- timeout-based-delivery
- scalability
- load-balancer
checks:
- The document states how long the aggregator waits for replies, such as a timeout, and what happens when
  it expires.
- The document says whether a missing or delayed reply can block the combined result.
- The document states whether recipients are chosen through a Publish/Subscribe Channel or through a Recipient
  List.
- The document names the component that combines the replies into one response.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html
  title: Scatter-Gather - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
  title: Aggregator - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.spring.io/spring-integration/reference/7.0/scatter-gather.html
  title: 'Scatter-Gather :: Spring Integration'
  site: docs.spring.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A request is scattered to several recipients. An aggregator gathers the replies into one response.
review:
  status: generated
  flags: []
---

## Explanation

Scatter-Gather is an integration pattern. It broadcasts a request to several recipients. It then merges their replies into one message.

**Two parts.** The "scatter" part sends the request out. The "gather" part uses an Aggregator. An Aggregator is a component that collects the replies and distills them into one response message.

**Two ways to reach recipients.**
- A Publish/Subscribe Channel (see the article of that name) lets the pattern use a single channel. The cost is that it gives up control over who receives the request.
- A Recipient List (see the article of that name) lets the pattern control which recipients are addressed.

**When to stop waiting.** The aggregator needs a rule for when it is done.
- Wait for all: every reply must arrive. One missing or late reply blocks the whole result.
- Timeout: wait a set time, then decide using the replies received.
- First best: take the fastest reply and ignore the rest.

**In practice.** Spring Integration offers this as one combined endpoint. It pairs a publish/subscribe channel or a recipient list router with an aggregator. It waits a bounded time for the aggregated reply. If time runs out, it returns null. A finite timeout therefore avoids waiting forever.

## Example

A travel site asks three hotel booking systems for a price on the same dates. Each system answers on its own schedule. The site waits two seconds. It then combines whatever arrived into one answer for the visitor. A system that did not answer in time is left out.

## Trade-offs

- Waiting for all replies gives the best basis for a decision, but it is the slowest and most brittle option, because one slow or missing reply blocks everything.
- A timeout keeps the caller moving, but the result may rest on fewer replies than hoped.
- Taking only the fastest reply is quick, but it ignores all other replies.
- A publish/subscribe channel needs only one channel, but you lose control over the recipients. A recipient list keeps that control.
