---
title: Routing Slip
slug: routing-slip
category: integration
kind: pattern
summary: A Routing Slip is a list attached to a message that names the processing steps it must visit,
  in order. Each step reads the slip and passes the message on, so every message can follow its own path.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- pipes-and-filters
- process-manager
- dynamic-router
- message-routing
- recipient-list
- content-based-router
- messaging-pattern-language
- composite-message-processor
checks:
- Messages that need varying sequences of steps carry a slip listing those steps, rather than relying
  on a fixed pipeline.
- The document states whether the slip is computed once up front or must be computed on the fly, and picks
  the matching pattern (Routing Slip or Dynamic Router).
- Where steps can be reversed, the document explains how compensation works for slip-based flows.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html
  title: Routing Slip - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html
  title: Process Manager - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://camel.apache.org/components/4.22.x/eips/routingSlip-eip.html
  title: 'Routing Slip :: Apache Camel'
  site: camel.apache.org
  accessed: '2026-11-09'
- url: https://masstransit.massient.com/concepts/routing-slips
  title: Routing Slips | MassTransit Documentation
  site: masstransit.massient.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A message carries a slip listing steps A and C. Each step's router reads the slip and forwards
    the message to the next listed step.
review:
  status: generated
  flags: []
---

## Explanation

Some messages must pass through several processing steps. The order of those steps may differ from message to message. You may not know the order when you design the system.

The Routing Slip pattern solves this. You attach a slip to each message. The slip lists the steps in order. Each step is wrapped with a small router, a component that decides where a message goes next. This router reads the slip and forwards the message to the next step.

**Where it comes from.** The starting point is Pipes and Filters (see the article of that name). It sends every message through the same fixed chain of steps. A Routing Slip builds on that idea for messages that need different chains.

**Comparison with Process Manager.** A Process Manager (see the article of that name) keeps central state. It picks the next step based on intermediate results. That central role can become a bottleneck, and it may be more than a simple case needs. A Routing Slip needs no such central controller.

**How tools use it.**
- Apache Camel computes the slip once, before the message starts its trip. A string slip is split into endpoint addresses at a delimiter, which is a comma by default. Camel can skip invalid endpoints instead of failing.
- MassTransit calls the steps activities. Together they form an itinerary. Each activity passes the slip on when it finishes.
- MassTransit also supports compensation. Activities store data about what they did, so reversible work can be undone. This links routing slips to distributed transactions.

## Example

An order system has three reusable steps: check fraud, apply discount, and reserve stock. A small domestic order gets a slip listing only "reserve stock". A large international order gets a slip listing all three, in a chosen order. The steps are the same components in both cases. Only the slip differs. After each step, the wrapping router reads the slip and forwards the order to the next listed step.

## Trade-offs

The slip is computed once, up front. In Apache Camel, this means the slip does not react to what happens along the way. If you must compute the route on the fly, Camel recommends the Dynamic Router instead (see the article of that name).

If the next step depends on intermediate results, a Process Manager fits better. It pays for that with central state and a possible bottleneck.
