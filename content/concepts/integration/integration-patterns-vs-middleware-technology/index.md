---
title: Integration Pattern vs. Middleware Technology
slug: integration-patterns-vs-middleware-technology
category: integration
kind: principle
summary: An integration pattern describes a solution without tying it to any product. Middleware is the
  concrete product or protocol that carries it out. Keeping the two apart lets you ask separate questions
  about each.
arc42:
- 4
- 8
- 9
step: s08-integration-data
related:
- integration-pattern
- messaging-pattern-language
- file-transfer
- shared-database
- remote-procedure-call
- messaging
- messaging-systems-and-protocols
checks:
- The integration style (file transfer, shared database, remote procedure invocation, or messaging) is
  named in product-neutral terms.
- Pattern names used in the document are neutral about technology and product.
- Platform and protocol constraints of a chosen messaging product, such as proprietary protocols, are
  stated.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Introduction.html
  title: Introduction - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

The Enterprise Integration Patterns book describes its patterns as vendor-independent. They apply to most messaging solutions. Its authors also chose pattern names that stay neutral about technology and product, yet still describe the idea and be easy to use conversationally.

The four integration styles show what "pattern level" means:

- **File Transfer:** each application produces files of shared data for others to read, and reads files that others produced.
- **Shared Database:** applications store the data they share in one common database.
- **Remote Procedure Invocation:** each application exposes some of its procedures so others can call them remotely.
- **Messaging:** applications connect to a common messaging system. They exchange data and trigger behavior through messages.

None of these four names a product. Each is a choice about how applications relate, made without naming a tool. The articles Integration Styles and Messaging cover them in more detail.

Technology choice brings its own concerns. Many messaging implementations rely on proprietary protocols. Proprietary protocols are tied to vendor lock-in, and many proprietary messaging systems are not available on all platforms. The source also lists integration technology as one criterion when choosing among styles, noting that specialized tools can be expensive and can lead to vendor lock-in.

## Example

A team must let an order system share data with a billing system. They first decide on the style: messaging, not a shared database. They record this in product-neutral terms. Then they compare messaging products. They check whether a candidate relies on a proprietary protocol and whether it fits their platforms.

## Trade-offs

The book chose pattern names that are neutral about technology and product. The technology question stays open for its own constraints, such as the proprietary protocols many messaging products rely on.
