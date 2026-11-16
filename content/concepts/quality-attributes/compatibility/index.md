---
title: Compatibility
slug: compatibility
order: 30
category: quality-attributes
kind: quality-attribute
summary: Compatibility is how well a product exchanges information with other products and does its job
  while sharing an environment and resources with them. Version numbers and tolerant reading help keep
  interfaces working as products change.
arc42:
- 3
- 4
- 8
- 10
step: s08-integration-data
related:
- iso-iec-25010-product-quality-model
- maintainability
- patterns-for-api-design
- architectural-tactic
- quality-attribute-scenario
- coupling-and-cohesion
checks:
- The document states which other products a component exchanges information with, and what it shares
  with them.
- Public APIs use a versioning scheme in which a major bump signals incompatible changes.
- Consumers read provider data tolerantly, taking only the elements they need.
- Providers run consumer-supplied reader tests in their build to catch breaking changes.
sources:
- url: https://quality.arc42.org/qualities/compatibility
  title: Compatibility | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://semver.org/
  title: Semantic Versioning 2.0.0 | Semantic Versioning
  site: semver.org
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/bliki/TolerantReader.html
  title: Tolerant Reader
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: "ISO 25010"
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/co-existence
  title: "Co-existence | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Interoperability
  title: "Interoperability - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html
  title: "Message Translator - Enterprise Integration Patterns"
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/interoperability
  title: "Interoperability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/interoperable-with-java-12
  title: "Interoperable with Java 12"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/low-effort-deployment
  title: "Low effort deployment"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/compatible-with-5-battery-providers
  title: "Compatible with 5 different battery providers"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Compatibility is a quality of a product defined in ISO 25010 (see the article ISO/IEC 25010 Product Quality Model). It has two parts. A product should exchange information with other products. It should also perform its required functions while sharing the same environment and resources with them.

**Where it matters**

Compatibility shows up where two products meet. If one side changes, the other side may stop working.

**Versioning as a signal**

Semantic versioning is a numbering scheme that writes compatibility into the version number of a public API:

- A major bump means the API changed in a backward incompatible way.
- A minor bump means new, backward compatible functionality was added.
- A patch bump means only backward compatible bug fixes were made.

A consumer can read the number and judge the risk of an upgrade.

**Reading data tolerantly**

The Tolerant Reader tactic puts some of the effort on the consumer. The consumer reads service data tolerantly, so the provider can evolve without breaking it. In practice, the consumer takes only the elements it needs and ignores the rest. Then the provider can add new elements without breaking that consumer.

**Contract tests**

A consumer can also send its reader and the reader's tests to the provider. The provider can use them in its own build to detect potential breakages. The source describes this as a step toward Consumer-Driven Contracts.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Co-existence** means that the product performs its required functions efficiently while sharing an environment and resources with other products, without harming them. More: [arc42 quality model](https://quality.arc42.org/qualities/co-existence).
- **Interoperability** is how well separate systems can exchange information and then use it. More: [arc42 quality model](https://quality.arc42.org/qualities/interoperability), [Interoperability - Wikipedia](https://en.wikipedia.org/wiki/Interoperability), [Message Translator - Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html).

**In the arc42 quality model.** The arc42 quality model has its own page on [Compatibility](https://quality.arc42.org/qualities/compatibility).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [Interoperable with Java 12](https://quality.arc42.org/requirements/interoperable-with-java-12), [Low effort deployment](https://quality.arc42.org/requirements/low-effort-deployment), [Compatible with 5 different battery providers](https://quality.arc42.org/requirements/compatible-with-5-battery-providers).

## Example

A shop's order service sends order data to a shipping service. The order team adds a new gift-message field. The shipping service reads only the address and item list, so it ignores the new field and keeps working. The order team publishes the change as a minor version, because it only adds something. Later, the order team removes the address field. That change is backward incompatible, so it needs a major version.

## Trade-offs

This article covers mainly versioning and data reading. Each technique has a cost.

- Tolerant reading protects the consumer from additions. It does not protect against removing or changing something the consumer needs.
- Semantic versioning only helps if the provider follows its rules for the public API.
- Shared reader tests need the consumer and provider to cooperate, with the provider using the tests in its build.
