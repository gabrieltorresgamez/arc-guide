---
title: Functional Suitability
slug: functional-suitability
order: 10
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
- quality-attribute
- fitness-for-purpose
- acceptance-criteria
- interaction-capability
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
- url: https://quality.arc42.org/qualities/functional-completeness
  title: "Functional completeness | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/functional-correctness
  title: "Functional correctness | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/functional-appropriateness
  title: "Functional appropriateness | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/user-tries-primary-function
  title: "User tries to achieve primary function"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/display-data-based-on-context
  title: "Display Data Based on Context"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/restore-filter-after-log-in
  title: "Restore Filter after Log In"
  site: quality.arc42.org
  accessed: '2026-11-16'
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

**In ISO/IEC 25010:2023.** The product quality model has nine characteristics, including Safety and Interaction capability.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Functional completeness** means that the set of functions covers all the specified tasks and the objectives of the intended users. More: [arc42 quality model](https://quality.arc42.org/qualities/functional-completeness).
- **Functional correctness** means that the product gives accurate results when the intended users use it. More: [arc42 quality model](https://quality.arc42.org/qualities/functional-correctness).
- **Functional appropriateness** means that the functions help users accomplish their specified tasks and objectives. More: [arc42 quality model](https://quality.arc42.org/qualities/functional-appropriateness).

**In the arc42 quality model.** The arc42 quality model has its own page on [Functional suitability](https://quality.arc42.org/qualities/functional-suitability).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [User tries to achieve primary function](https://quality.arc42.org/requirements/user-tries-primary-function), [Display Data Based on Context](https://quality.arc42.org/requirements/display-data-based-on-context), [Restore Filter after Log In](https://quality.arc42.org/requirements/restore-filter-after-log-in).

## Example

A team builds an online booking tool for a clinic. Patients must book, move and cancel appointments.

- Completeness: if patients cannot cancel, a specified task has no function.
- Correctness: if the tool shows the wrong appointment time, the results are not accurate.
- Appropriateness: the functions should help patients finish these tasks, not get in their way.
