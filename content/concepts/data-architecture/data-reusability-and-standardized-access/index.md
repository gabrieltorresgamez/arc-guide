---
title: Data Reusability and Standardized Access
slug: data-reusability-and-standardized-access
category: data-architecture
kind: principle
summary: Systems should expose their data in a shared, standardized form so other teams can reuse it without
  heavy cleanup. Common tools are data products, agreed identifiers, and a canonical data model.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- canonical-data-model
- message-translator
- data-architecture
- interoperability
- data-architecture-principle
- normalizer
- reusability
- integration
checks:
- Analytical data that domains provide is treated as a product with a standardized interface.
- Shared identity concepts, such as how to identify a customer or listener, are agreed across domains.
- Where applications use different formats, a common data model independent of any one application is
  defined.
- Applications produce and consume the canonical format, with translation done at the edges.
- The document states how local domain autonomy is balanced against enterprise-wide standards.
sources:
- url: https://martinfowler.com/articles/data-mesh-principles.html
  title: Data Mesh Principles and Logical Architecture
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html
  title: Canonical Data Model - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Applications translate to a common model at their edges; consumers reuse the data through a
    standard interface.
review:
  status: generated
  flags: []
---

## Explanation

Different applications often describe the same data in different formats.

**Treat data as a product.** Data mesh is an approach where business domains supply data for analysis. It holds that this analytical data must be treated as a product. Data products can also expose standardized interfaces, so consumers reach data in a uniform way.

**Agree on shared identity.** Some concepts cross domain borders. One example is how to identify a podcast listener. That decision is a global concern, so domains need to agree on it. A unified identification lets users be correlated across domains.

**Set global standards for a purpose.** Global decisions in data mesh have one purpose: creating interoperability and a compounding network effect through the discovery and composition of data products.

**Use a canonical data model.** The Canonical Data Model pattern asks how to integrate applications that use different data formats while keeping dependencies minimal. The answer is a common data model that does not depend on any one application. Every application produces and consumes messages in that format. See the article Canonical Data Model for details.

**Balance local and global.** Federated computational governance accepts change and multiple interpretive contexts. It balances local domain autonomy against global standards.

## Example

An order system and a shipping system both store customers, each with its own customer key. An analyst who wants shipping delays per customer must first match the keys by hand. Instead, the two teams agree on one customer identifier. Each team then publishes its data as a product with a standard interface. The analyst can combine both without manual matching.

## Trade-offs

Global standards create interoperability, while domain data models stay local to each domain. Federated computational governance tries to balance the two. It keeps local autonomy while applying global rules that the platform automates, and it accepts that change and different interpretations will occur.

A canonical data model keeps dependencies low. It can seem complicated when only a few applications take part, but it quickly pays off as the number of applications grows.
