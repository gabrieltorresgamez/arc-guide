---
title: Canonical Data Model
slug: canonical-data-model
category: integration
kind: pattern
summary: A Canonical Data Model is one shared, application-independent data format that systems translate
  to and from. It cuts translation paths from n×n to n, but it is overkill for small integrations.
arc42:
- 8
- 9
- 3
step: s08-integration-data
related:
- normalizer
- message-translator
- messaging-pattern-language
- integration
- loose-coupling
- datatype-channel
checks:
- The document justifies the canonical model by the number of integrated applications, since it is overkill
  for only a few.
- The canonical model is independent of any specific application.
- The document states whether one enterprise-wide model or several canonical models with translation between
  overlaps are used.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html
  title: Canonical Data Model - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/MultipleCanonicalModels.html
  title: Multiple Canonical Models
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html
  title: Normalizer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each system translates only to and from the shared canonical model.
review:
  status: generated
  flags: []
---

## Explanation

Different applications often send data in different formats. If every system must talk to every other system, each pair needs its own translation. With n systems, that means n × n translation paths.

A Canonical Data Model removes most of that work. You design one data model that does not depend on any specific application. Each system then translates only to and from that shared model, which acts as a central hub. The result is n paths instead of n × n.

The goal is to minimize dependencies between applications that use different data formats. A system no longer needs to know the format of the systems it talks to. It only needs to know the shared format.

A related pattern is the Normalizer (see the article "Normalizer"). It routes each incoming message type through a matching Message Translator (see "Message Translator"). Every message then arrives in the shared format. One published example involves over 1,700 affiliates.

**Designing the shared model is hard.** A single model for a large enterprise tends to be very large, abstract, or both. That makes it hard to understand. One suggestion is to use several canonical models instead of one. You then translate between the parts where they overlap.

## Example

A retailer has an order system, a warehouse system, and an invoicing system. Each uses its own order format. Instead of building a translator for every pair, the team defines one shared "Order" format. Each system gets one translator to and from it.

## Trade-offs

- **Seems complicated for small setups.** With only a few applications, the approach can look complicated, but it pays off quickly as the number of applications grows.
- **Hard to design.** A model that covers a whole enterprise tends to become large or abstract, so people struggle to understand it.
- **Possible remedy.** Several canonical models, with translation between overlapping parts, can replace one big model.
