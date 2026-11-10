---
title: Dynamic Router
slug: dynamic-router
category: integration
kind: pattern
summary: A Dynamic Router sends messages to recipients using rules it learns at runtime. Recipients tell
  the router what they want over a control channel, so the router needs no fixed list of destinations.
arc42:
- 5
- 6
- 8
- 9
step: s08-integration-data
related:
- content-based-router
- recipient-list
- routing-slip
- message-routing
- publish-subscribe-channel
- message-channel
- loose-coupling
checks:
- The document states whether the design uses a control channel for recipients to register and unsubscribe.
- The document says how the router handles a message that matches several recipients, for example first
  match or all matches.
- The document states whether routing-table changes at runtime are applied incrementally or replaced as
  a whole, and how inconsistency is handled.
- The document says whether the core Dynamic Router or Camel's component is used, if Camel is the technology.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html
  title: Dynamic Router - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/next/dynamic-router-component.html
  title: 'Dynamic Router :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.18.x/eips/dynamicRouter-eip.html
  title: 'Dynamic Router :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://docs.spring.io/spring-integration/reference/router/dynamic-routers.html
  title: 'Dynamic Routers :: Spring Integration'
  site: docs.spring.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Recipients register rules over the control channel. The router uses its rule base to route
    input messages.
review:
  status: generated
  flags: []
---

## Explanation

A router decides where each message goes. A simple router knows every possible destination in advance. That creates a dependency: the router must change whenever destinations change. The Dynamic Router addresses this. It aims to remove the dependency while keeping routing efficient.

**How it works.** Besides the usual input and output channels, the pattern adds a control channel. Recipients use it to tell the router about themselves. The router stores each participant's preferences in a rule base, which is a collection of conditions. It routes a message to the recipient whose rules are fulfilled.

**In Apache Camel.** Camel offers a Dynamic Router component. It builds its rule base while the system runs. It updates that rule base as participants subscribe or unsubscribe through the control channel. A recipient can leave by sending an unsubscribe message.

The component keeps prioritized filters for each channel. A `recipientMode` option, either `firstMatch` or `allMatch`, decides what happens when several recipients match one message.

Camel also has a core Dynamic Router, which is a separate implementation with no control channel. It computes the route at runtime. It is similar to a Routing Slip (see the Routing Slip article), except that the slip is evaluated dynamically. For some use cases the core version fits better.

**In Spring Integration.** Its documentation describes the pattern as a way to change router configuration without bringing down the system. Mapping routers let you add, change and remove channel mappings at runtime. You can expose these operations through JMX or the control bus.

## Example

An order system sends messages to several handlers. A new "gift-card" handler starts up. It sends a registration message on the control channel, along with the conditions it accepts. The router adds these to its rule base. Later orders that match go to the new handler. Nobody edited the router's code. When the handler is retired, it sends an unsubscribe message and the router drops its rules.

## Trade-offs

**Benefit:** the router no longer depends on a fixed list of destinations. Recipients can join and leave while the system runs.

**Cost: consistency.** In Spring Integration, changing the routing table step by step is not atomic. Removing one route and adding another can leave the table briefly in an indeterminate state. Since version 4.0, you can replace the whole table atomically.

**Cost: choice of variant.** Camel's component adds a control channel, but the core pattern has none. Pick the one that matches your use case.

**Cost: overlapping rules.** When several recipients match, you must decide between first match and all matches, and set filter priorities.
