---
title: Broker Pattern
slug: broker-pattern
category: styles-patterns
kind: pattern
summary: The broker pattern organizes a distributed system around one central component. Decoupled parts
  interact through remote calls, and the broker coordinates them. It forwards requests and returns results
  and errors. The whole system depends on it.
arc42:
- 4
- 5
- 8
- 11
step: s08-integration-data
related:
- publish-subscribe-pattern
- message-routing
- messaging
- remote-procedure-call
- loose-coupling
- architectural-pattern
- messaging-pattern-language
- connectors-and-distribution
checks:
- The document names the broker component and states that it coordinates communication, forwards requests,
  and returns results and exceptions.
- The document explains how the broker's robustness and efficiency are ensured, since the system depends
  on it.
- The document assesses whether routing all messages through one broker creates a bottleneck.
- The document distinguishes the broker pattern from publish-subscribe where both are mentioned.
sources:
- url: https://en.wikipedia.org/wiki/Broker_pattern
  title: Broker pattern - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html
  title: Message Broker - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingBridge.html
  title: Messaging Bridge - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: A broker forwards a request and returns the result or exception.
review:
  status: generated
  flags: []
---

## Explanation

A distributed system runs its parts on different machines or in different processes. In the broker pattern, these parts are decoupled. They do not talk to each other directly. They interact through remote calls, and a central component called the broker coordinates the communication.

The broker has a clear job. It forwards requests from one part to another. It transmits the results back. It also passes on exceptions (error reports) when a call fails.

A closely related idea exists in enterprise messaging. A Message Broker answers this question: how can you separate a message's destination from its sender, yet keep central control over the flow of messages? The broker receives each message, determines the correct destination, and routes the message to the right channel. The articles on Message Routing and Messaging give background.

A Messaging Bridge is a neighboring idea. It connects separate messaging systems by replicating messages between them.

Some people confuse the broker pattern with the Publish-Subscribe Pattern. The two have similarities, but they are represented differently. Treat them as separate patterns.

## Example

An order service needs a price from a pricing service. It does not know where the pricing service runs. It sends the request to the broker. The broker forwards the request and returns the price to the order service. If the call fails, the broker passes the error back instead.

## Trade-offs

- **Single point of dependence.** All communication runs through one central component. The source lists as a disadvantage that this one central component needs to be robust and efficiently written.
- **Bottleneck risk.** Routing all messages through a single broker can turn it into a serious bottleneck.
- **Benefit.** Senders do not need to know destinations, and the broker keeps central control over message flow.
