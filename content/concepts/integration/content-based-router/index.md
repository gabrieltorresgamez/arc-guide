---
title: Content-Based Router
slug: content-based-router
category: integration
kind: pattern
summary: A Content-Based Router reads each message and sends it to a channel chosen from data inside the
  message. It lets one logical function span several systems. Its fixed rules need careful upkeep.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- dynamic-router
- message-routing
- recipient-list
- message-filter
- message-channel
- messaging-pattern-language
- publish-subscribe-channel
- loose-coupling
checks:
- The routing rules are documented and kept easy to maintain.
- The document states what happens to a message that matches no rule.
- Where rules are checked in order, the order is documented, because the first match decides the branch.
- The document lists the destinations the router depends on, or explains how they are discovered, for
  example with a Dynamic Router.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html
  title: Content-Based Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/choice-eip.html
  title: 'Choice :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://docs.spring.io/spring-integration/reference/router/overview.html
  title: 'Overview :: Spring Integration'
  site: docs.spring.io
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html
  title: Dynamic Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A router reads the category in each order and picks the matching channel.
review:
  status: generated
  flags: []
---

## Explanation

A Content-Based Router looks at each message that arrives. It reads data in the message and picks the channel that fits. A channel is a path that carries messages to a receiver (see the article Message Channel). The router then puts the message on that channel.

The pattern solves a common problem. Sometimes one logical function is spread over several systems. The router sends each message to the right system, based on what the message contains.

**How it looks in tools**

- Apache Camel implements the pattern with its Choice feature. Choice routes on the contents of the message exchange.
- In Camel, the first `when` clause that matches decides the branch.
- An optional `otherwise` clause handles messages that match no `when`. Without it, no branch is selected.
- Spring Integration describes routers as components that read from one channel. They forward each message to other channels based on conditions.
- Spring Integration offers payload-type, header-value, recipient-list, XPath and generic routers. By default it throws an exception if no channel is resolved, unless a default output channel is set.

**Related pattern**

The Dynamic Router is a related pattern. It adds a control channel. Recipients announce themselves on that channel, so the router configures itself. See the article Dynamic Router.

## Example

An online shop receives orders on one channel. Each order carries a product category. The router reads the category. Book orders go to the channel of the book supplier. Electronics orders go to the channel of the electronics supplier.

## Trade-offs

- The routing logic is a maintenance concern. The pattern itself warns that it must be kept easy to maintain.
- The router can become a point of frequent maintenance.
- In Camel, the first matching `when` clause determines the branch.
- Messages that match no rule need a deliberate answer. Camel's `otherwise` clause is one option. Spring Integration throws an exception by default unless a default output channel is set.
- The Dynamic Router instead configures itself through a control channel.
