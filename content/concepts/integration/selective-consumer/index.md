---
title: Selective Consumer
slug: selective-consumer
category: integration
kind: pattern
summary: A Selective Consumer tells its channel which messages it wants. The channel delivers only matching
  messages, so the consumer does not have to sort through the rest itself.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-channel
- point-to-point-channel
- publish-subscribe-channel
- message-filter
- content-based-router
- datatype-channel
- messaging-pattern-language
- message-routing
checks:
- The selection criteria of all consumers on a channel together cover every valid selection value.
- The document states which message headers or properties consumers select on, because selectors cannot
  use the message body.
- The document states that the broker or messaging provider, not the consumer, performs the filtering.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSelector.html
  title: Selective Consumer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://docs.oracle.com/cd/E19798-01/821-1841/bncer/index.html
  title: JMS Message Selectors (The Java EE 6 Tutorial)
  site: docs.oracle.com
  accessed: '2026-11-09'
- url: https://www.rabbitmq.com/tutorials/amqp-concepts
  title: AMQP 0-9-1 Model Explained | RabbitMQ
  site: rabbitmq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A channel delivers each message only to the consumer whose criteria match.
review:
  status: generated
  flags: []
---

## Explanation

Sometimes a consumer wants only some of the messages on a channel. It needs a way to choose which ones it receives. (A channel is the path that carries messages between systems. See Message Channel.)

The Selective Consumer pattern solves this. The consumer states its criteria, and only matching messages reach it.

**Concrete forms**

- **JMS message selectors.** JMS is the Java messaging API. A selector lets a consumer say which messages it is interested in. Its syntax is based on a subset of SQL92 conditional expressions. The JMS provider, not the application, does the filtering.
- **RabbitMQ and AMQP bindings.** Bindings are rules that tell an exchange how to route messages to queues. The broker does the matching. A headers exchange can route on several header attributes. The `x-match` setting controls whether any or all of them must match.

**Limits of matching**

JMS selectors look only at message headers and properties. They cannot look at the message body.

**Several consumers on one channel**

On a Point-to-Point Channel, several Selective Consumers behave as selective Competing Consumers. They compete for messages, but each one only competes for messages that match.

**Cover every value**

If no consumer matches a message's selection value, nobody consumes that message. It clutters the channel until it expires. The criteria of all consumers together must therefore cover every valid value.

## Example

An order channel carries messages with a header called `region`. The EU billing service asks for `region = 'EU'`. The US billing service asks for `region = 'US'`. Each service receives only its own orders. If a message arrives with `region = 'APAC'`, no service selects it. It stays on the channel until it expires. The team must add a consumer for that value or change the criteria.

## Trade-offs

**Benefits**

- The consumer does not filter messages itself. The channel or broker does that work.
- One channel can serve consumers with different interests.

**Costs and risks**

- Unmatched messages clutter the channel until they expire. Criteria must cover all valid values.
- Selectors cannot see the message body, so body content cannot drive the choice.
