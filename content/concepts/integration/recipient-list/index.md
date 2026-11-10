---
title: Recipient List
slug: recipient-list
category: integration
kind: pattern
summary: Recipient List is a routing pattern for sending one message to a list of recipients that is decided
  dynamically. Apache Camel offers it, and Scatter-Gather can use it to send requests.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- message-routing
- scatter-gather
- message-channel
- messaging-pattern-language
- publish-subscribe-channel
- content-based-router
checks:
- Where one message must reach a dynamically chosen set of receivers, the document names Recipient List
  as the routing approach.
- Where Scatter-Gather is used, the document states whether a Recipient List distributes the requests
  and so controls the recipients.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RecipientList.html
  title: Recipient List - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/recipientList-eip.html
  title: 'Recipient List :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html
  title: Scatter-Gather - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A router forwards the message to the channel of each recipient on the list.
review:
  status: generated
  flags: []
---

## Explanation

Sometimes one message must reach several receivers, and the set of receivers is not fixed in advance. The Recipient List pattern solves this. It routes a message to a list of dynamically specified recipients.

The pattern belongs to message routing. See the articles Message Routing and Enterprise Integration Patterns for the wider picture.

**In Apache Camel.** The Recipient List EIP (Enterprise Integration Pattern) inspects an incoming message, determines the list of desired recipients, and forwards the message to all channels associated with those recipients. See Message Channel.

**In Scatter-Gather.** Scatter-Gather sends a request out to several parties and then collects the answers. See Scatter/Gather. It can use a Recipient List to distribute those requests. This lets Scatter-Gather control which recipients get the request.

## Example

An order system must ask for price quotes. The list of suppliers to ask changes from order to order. The system builds a list of suppliers for each order. A router then forwards the quote request to the channel of every supplier on that list.
