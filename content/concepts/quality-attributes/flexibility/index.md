---
title: Flexibility
slug: flexibility
order: 80
category: quality-attributes
kind: quality-attribute
summary: Flexibility is a product's ability to adapt to changed requirements and contexts of use. ISO
  25010:2023 splits it into adaptability, scalability, installability and replaceability.
arc42:
- 1
- 4
- 10
step: s04-quality-requirements
related:
- maintainability
- microservices-architecture
- design-for-change
checks:
- The document states which Flexibility sub-characteristics (adaptability, scalability, installability,
  replaceability) matter for the system.
- Scalability requirements say whether the workload is expected to grow, shrink, or both.
- Replaceability targets are stated, and accepted lock-in is named as a conscious choice.
- 'The document says who performs adaptation: support staff, operations staff or end users.'
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=8
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/articles/q42-for-iso-users/
  title: Q42 for ISO-25010 Users | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/replaceability
  title: Replaceability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/scalability
  title: Scalability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/adaptability
  title: Adaptability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: "ISO 25010"
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/scale-partition
  title: "Architecture strategies for optimizing scaling and partitioning - Microsoft Azure Well-Architected Framework | Microsoft Learn"
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/installability
  title: "Installability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/compatible-with-5-battery-providers
  title: "Compatible with 5 different battery providers"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/luggage-routing
  title: "Efficient change of business rules"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/display-data-based-on-context
  title: "Display Data Based on Context"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/flexibility
  title: "Flexibility | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Flexibility describes how well a product can be adapted when requirements or contexts of use change [src:1]. Flexibility is one of the nine characteristics of ISO/IEC 25010:2023 [src:7].

The standard lists four sub-characteristics:

- **Adaptability:** adapting a product to, or moving it to, different hardware, software or other environments. Support staff, operations staff or end users can do this work. When end users do it, adaptability equals suitability for individualization.
- **Scalability:** handling growing or shrinking workloads. Elasticity is a related quality.
- **Installability:** the third child of Flexibility in the standard's tree.
- **Replaceability:** the ability to use other software products in place of the present one. This lowers lock-in risk, meaning the risk of being tied to one product.

Some constructs make change easier. Microservices are one example (see Microservices Architecture). Each microservice is a component that can be replaced and upgraded on its own. After a change to a single service, often only that service needs redeploying. Moving code across service boundaries is hard.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Adaptability** is how well a product can be changed to fit new requirements, new contexts of use, or a new system environment. More: [arc42 quality model](https://quality.arc42.org/qualities/adaptability).
- **Scalability** is how well a system copes with growing workload by adding resources. Every resource has an upper scale limit. More: [arc42 quality model](https://quality.arc42.org/qualities/scalability), [Architecture strategies for optimizing scaling and partitioning - Microsoft Azure Well-Architected Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/scale-partition).
- **Installability** describes how well a product can be installed and removed in a specific environment. More: [arc42 quality model](https://quality.arc42.org/qualities/installability).
- **Replaceability** is how well one product can take over from another specified product for the same purpose in the same environment. More: [arc42 quality model](https://quality.arc42.org/qualities/replaceability).

**In the arc42 quality model.** The arc42 quality model has its own page on [Flexibility](https://quality.arc42.org/qualities/flexibility).

**Example quality requirements.** The arc42 quality model has example quality requirements for flexibility and its subcharacteristics, such as adaptability: [Compatible with 5 different battery providers](https://quality.arc42.org/requirements/compatible-with-5-battery-providers), [Efficient change of business rules](https://quality.arc42.org/requirements/luggage-routing), [Display Data Based on Context](https://quality.arc42.org/requirements/display-data-based-on-context).

## Example

A company runs an online shop as several small services. Holiday traffic grows, so the team adds capacity for the checkout service (scalability). The payment service needs a new provider. The team swaps that one service and redeploys only it (replaceability). The rest of the shop stays untouched.

## Trade-offs

Replaceability is not free and is rarely worth maximizing. Lock-in is the price of low replaceability, so a team should decide where it accepts lock-in. Microservices ease change, but moving code across service boundaries is hard.
