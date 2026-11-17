---
title: Tactic Coverage of ISO 25010 Quality Characteristics
slug: tactic-coverage-of-iso-25010-quality-characteristics
order: 80
category: tactics
kind: concept
summary: Tactic catalogs and ISO 25010 use different vocabularies. Catalogs cover terms the standard lacks,
  such as deployability, so you must map one to the other before judging coverage.
arc42:
- 4
- 10
step: s04-quality-requirements
related:
- iso-iec-25010-product-quality-model
- architectural-tactic
- functional-suitability
- flexibility
- maintainability
checks:
- The document uses the quality terms of ISO/IEC 25010:2023.
- Where a tactic term has no ISO 25010 equivalent, such as deployability, the document names the
  stand-in term used, for example installability.
- The document says where testability is placed in the mapping.
sources:
- url: https://quality.arc42.org/articles/iso-25010-shortcomings
  title: Shortcomings of ISO 25010 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/articles/sei-quality-model
  title: SEI Quality Model | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/standards/iso-25010
  title: ISO/IEC 25010 - Systems and Software Quality | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO 25010 is a standard list of product quality characteristics.

**The two vocabularies differ in size.** The quality model from Bass et al. has about 10 attributes. ISO/IEC 25010:2023 has nine characteristics, each with subcharacteristics [src:4].

**Some catalog terms are missing from ISO 25010.** Operational topics such as deployability are not among the nine characteristics. The arc42 quality model treats deployable as a sub-goal of operable.

**Bass et al. split attributes into two groups.** They define a quality attribute as a measurable or testable property of a system. They sort attributes into runtime and development categories.

**Functional suitability has its own shape.** It means the degree to which functions meet stated and implied needs. Its sub-characteristics are completeness, appropriateness and correctness.

## Example

A team reads a tactic catalog with a chapter on deployability. They look for "deployability" in ISO 25010 and find nothing. They note the gap and write it down. They do the same for testability and record that ISO 25010 puts it under maintainability.

## Trade-offs

A mapping makes catalogs usable with ISO terms, but every stand-in is a judgment call. Testability could sit under maintainability or reliability. Different teams may map the same term differently, so write the mapping down. Check which ISO characteristics each catalog covers against the catalogs themselves.
