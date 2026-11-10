---
title: Tactic Coverage of ISO 25010 Quality Categories
slug: tactic-sources-by-iso-25010-quality-category
category: tactics
kind: concept
summary: Tactic catalogs and ISO 25010 use different vocabularies. Catalogs cover terms the 2011 standard
  lacks, such as deployability and energy efficiency, so you must map one to the other before judging
  coverage.
arc42:
- 4
- 10
step: s04-quality-requirements
related:
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- quality-attribute-coverage-in-bass-et-al
- architectural-tactic
- functional-suitability
- installability
- testability
- energy-efficiency-tactics
checks:
- The document states which ISO 25010 edition (2011 or 2023) its quality terms come from.
- Where a tactic term has no ISO 25010 (2011) equivalent, such as deployability, the document names the
  stand-in term used, for example installability.
- The document says where testability is placed (maintainability, reliability or both).
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

ISO 25010 is a standard list of product quality characteristics. Tactic catalogs and ISO 25010 do not line up one to one.

**The two vocabularies differ in size.** The quality model from Bass et al. has about 10 attributes. ISO 25010 has roughly 40 terms. Because of this gap, you need a mapping before you can say which ISO characteristic a catalog covers.

**Some catalog terms are missing from ISO 25010 (2011).** Scalability, deployability, energy efficiency and safety are missing from the 2011 standard. Operational topics such as deployability are absent altogether. The arc42 quality model treats deployable as a sub-goal of operable.

**Testability's place depends on the edition.** The 2011 standard files testability under maintainability, while the 2023 edition lists it under Flexibility. The arc42 quality model's author argues it should also appear under reliability. When you map a testability tactic, state which parent you mean.

**Bass et al. split attributes into two groups.** They define a quality attribute as a measurable or testable property of a system. They sort attributes into runtime and development categories.

**Functional suitability has its own shape.** It means the degree to which functions meet stated and implied needs. Its sub-characteristics are completeness, appropriateness and correctness.

**The 2023 edition adds terms.** The 2023 edition, as shown by iso25000.com, lists nine characteristics. It includes Interaction Capability and keeps functional suitability with completeness, correctness and appropriateness. Check which edition a document refers to before mapping.

## Example

A team reads a tactic catalog with a chapter on deployability. They look for "deployability" in ISO 25010 (2011) and find nothing. They note the gap and write it down. They do the same for testability and record that the 2011 edition puts it under maintainability.

## Trade-offs

A mapping makes catalogs usable with ISO terms, but every stand-in is a judgment call. Testability could sit under maintainability or reliability. Different teams may map the same term differently, so write the mapping down. Check which ISO characteristics each catalog covers against the catalogs themselves.
