---
title: Compatibility
slug: compatibility
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
- interoperability
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- modifiability
- patterns-for-api-design
- architectural-tactic
- quality-attribute-scenario
- loose-coupling
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

## Example

A shop's order service sends order data to a shipping service. The order team adds a new gift-message field. The shipping service reads only the address and item list, so it ignores the new field and keeps working. The order team publishes the change as a minor version, because it only adds something. Later, the order team removes the address field. That change is backward incompatible, so it needs a major version.

## Trade-offs

This article covers mainly versioning and data reading. Each technique has a cost.

- Tolerant reading protects the consumer from additions. It does not protect against removing or changing something the consumer needs.
- Semantic versioning only helps if the provider follows its rules for the public API.
- Shared reader tests need the consumer and provider to cooperate, with the provider using the tests in its build.
