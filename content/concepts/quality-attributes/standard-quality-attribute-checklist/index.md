---
title: Standard Quality Attribute List
slug: standard-quality-attribute-checklist
category: quality-attributes
kind: practice
summary: A standard quality attribute list is a ready-made checklist and shared vocabulary for quality
  needs. No list is complete, and names alone are ambiguous, so teams adapt the list and add scenarios.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- iso-iec-25010-quality-model
- quality-attribute
- quality-attribute-scenario
- arc42-quality-chapter
- scalability
- iso-25010-2023-revision
- quality-attribute-prioritization
- arc42-glossary
checks:
- Quality attribute names in the document are backed by scenarios that are specific and measurable.
- The number of quality scenarios is kept manageable, around ten for most systems.
- Qualities missing from the standard list, such as deployability, were considered where relevant.
sources:
- url: https://quality.arc42.org/articles/iso-25010-shortcomings
  title: Shortcomings of ISO 25010 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=3128836&seqNum=3
  title: Quality Attributes | Why Software Architecture is Important and Essential Activities | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A standard quality attribute list names the qualities a system may need, such as the ones in ISO 25010 (see ISO/IEC 25010 Product Quality Model).

**Shared vocabulary.** The words people use for qualities vary with the author's perspective. A standard list aims to let all stakeholders recognize their goals and requirements in it, though a critic argues ISO 25010 does not achieve this.

**Known weaknesses.** Critics of ISO 25010 point out several problems:

- It builds a generic taxonomy (a structured set of terms) of almost 40 terms. The critic argues fewer terms would have been better.
- Some terms overlap. Maintainability and flexibility have definitions that are too similar.
- Placement is inconsistent. Adaptability also relates to maintainability, but the standard files it only under portability.
- Any strict hierarchy of qualities can be disputed.

**Gaps.** Scalability was missing from the 2011 version. The 2022 draft added it under flexibility. Operational or DevOps qualities such as deployability are also missing.

**Names are not requirements.** Words like "availability," "security," and "usability" are still ambiguous. A quality attribute scenario makes a requirement concrete. It lets you decide whether the requirement is fulfilled, and it should be specific and measurable (see Quality Attribute Scenario). About ten scenarios are manageable for most systems.

## Example

A team building an online shop reads through a standard list during requirements gathering. They notice nobody has talked about handling many visitors at once. They write one scenario that states what load the shop must handle and how that is judged. The list prompted the question. The scenario made it precise.

## Trade-offs

A standard list is a starting point, not a finished answer. It can be incomplete, it can overlap with itself, and it can lead to arguments about where a term belongs. Those arguments cost effort without improving the system. Scenarios and deeper analysis must supply the precision.
