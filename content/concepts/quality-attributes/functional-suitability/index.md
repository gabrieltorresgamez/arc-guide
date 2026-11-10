---
title: Functional Suitability
slug: functional-suitability
category: quality-attributes
kind: quality-attribute
summary: 'Functional suitability is the degree to which a product provides functions that meet stated
  and implied needs under specified conditions. It has three parts: completeness, correctness and appropriateness.'
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- quality-attribute
- fitness-for-purpose
- acceptance-criteria
- usability
- security
- quality-models-and-their-target-entities
checks:
- The document states which tasks and user objectives the functions must cover (functional completeness).
- The document says who the intended users are and under which conditions the functions must give accurate
  results.
- Functional suitability is treated as one product quality characteristic next to others such as security.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/qualities/functional-suitability
  title: Functional suitability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://www.sonarsource.com/resources/library/iso-iec-25010-explained/
  title: 'ISO/IEC 25010 Explained: 9 Software Quality Characteristics That Matter | Sonar'
  site: sonarsource.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Functional suitability is a product quality characteristic in ISO/IEC 25010 (see ISO/IEC 25010 Product Quality Model). It asks whether the product provides functions that meet stated and implied needs under specified conditions.

The 2023 edition, as quoted by the arc42 quality model, words this around the needs of intended users when the product is used under specified conditions. Sonar summarizes it as performing the right functions correctly.

The standard splits the characteristic into three sub-characteristics:

- **Functional completeness.** The set of functions covers all specified tasks and the objectives of intended users.
- **Functional correctness.** The product gives accurate results when intended users use it.
- **Functional appropriateness.** The functions help users accomplish their specified tasks and objectives.

**Where it sits in the quality model.** Functional suitability is one of several product quality characteristics. Security is another. Product quality is distinguished from quality in use. Functional suitability concerns the functions a product provides. It is not the same as the separate "suitability" quality from ISO/IEC 25019.

**The 2023 revision.** The product quality model grew from eight to nine characteristics. Safety was added, and Usability was replaced by Interaction capability, which covers a broader scope. The sources reviewed did not list changes to the definition of functional suitability itself. See ISO/IEC 25010:2023 Product Quality Model Revision.

## Example

A team builds an online booking tool for a clinic. Patients must book, move and cancel appointments.

- Completeness: if patients cannot cancel, a specified task has no function.
- Correctness: if the tool shows the wrong appointment time, the results are not accurate.
- Appropriateness: the functions should help patients finish these tasks, not get in their way.
