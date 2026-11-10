---
title: Connector Cardinality
slug: connector-cardinality
category: fundamentals
kind: concept
summary: Connector cardinality is the number of components a connector links. A point-to-point connector
  links two. A multicast connector delivers to several components through one shared channel.
arc42:
- 5
- 6
step: s08-integration-data
related:
- software-connector
- point-to-point-channel
- publish-subscribe-channel
- publish-subscribe-pattern
- message-channel
- component-port
- classification-of-integration-patterns
- scalability
checks:
- Each channel is documented as point-to-point (one receiver per message) or publish-subscribe (a copy
  to every subscriber).
- Where a channel has several competing receivers, the document states that only one receiver consumes
  each message.
- For publish-subscribe channels, the subscribers are listed, since each one receives a copy.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html
  title: Point-to-Point Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://ar5iv.arxiv.org/html/1608.03324
  title: '[1608.03324] Architecture Diagrams: A Graphical Language for Architecture Style Specification'
  site: ar5iv.arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Top: one message goes to one of the competing receivers. Bottom: each subscriber gets a copy.'
review:
  status: generated
  flags: []
---

## Explanation

A connector is the link through which components interact (see the article Software Connector). Cardinality, in the architecture-diagram paper, is the number of instances of a component type.

**Point-to-point.** A point-to-point channel delivers each message to exactly one receiver. Several receivers may listen on the same channel. If several receivers try to consume a message, only one of them succeeds. Multiple receivers can consume multiple messages concurrently, but each message is consumed by a single receiver.

**Publish-subscribe.** A publish-subscribe channel delivers a copy of each event to every subscriber.

**Inside a publish-subscribe channel.** A publish-subscribe channel takes one input and splits it into one output channel per subscriber. So an intermediate structure sits between the publisher and the subscribers.

**Arity in general.** Connectors can be modeled as sets of ports that must interact together. A port is a point where a component connects. With this model, one connector can have any number of ports. One research paper shows a single quaternary connector (four ports) and contrasts it with three binary connectors.

## Example

An online shop emits an "order placed" event. If the event goes to a point-to-point channel with several workers, only one worker handles each order. If billing, shipping, and analytics must each see every order, the shop publishes to a publish-subscribe channel. Each of the three gets its own copy.

## Trade-offs

Point-to-point gives one handler per message. Multiple receivers can consume multiple messages concurrently.

Publish-subscribe gives every subscriber its own copy. 

Choose the form by asking whether each message should be handled once or seen by everyone.
