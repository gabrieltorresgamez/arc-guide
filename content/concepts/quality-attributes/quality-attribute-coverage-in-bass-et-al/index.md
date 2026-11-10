---
title: Quality Attribute Coverage in Bass et al.
slug: quality-attribute-coverage-in-bass-et-al
category: quality-attributes
kind: concept
summary: The Bass et al. model of quality attributes is much smaller than ISO 25010, with 10 top-level
  areas. It covers topics the 2011 ISO standard lacks, such as deployability and safety, and it has no
  chapter on compatibility.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- quality-attribute
- quality-attribute-scenario
- iso-iec-25010-quality-model
- standard-quality-attribute-checklist
- safety
- energy-efficiency-tactics
- performance-efficiency
- tactic-sources-by-iso-25010-quality-category
checks:
- Quality goals were checked against both a short attribute list and the larger ISO 25010 list, so topics
  such as compatibility are not missed.
- Deployability is considered, or its omission is justified, for the type of system (e.g., embedded systems
  deploy less often).
- Safety is considered as a quality goal where physical harm is possible.
- Key quality requirements are written as scenarios with source, stimulus, artifact, environment, response
  and metric.
sources:
- url: https://quality.arc42.org/articles/sei-quality-model
  title: SEI Quality Model | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/articles/iso-25010-shortcomings
  title: Shortcomings of ISO 25010 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/specify-quality-requirements
  title: How to specify quality requirements | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The SEI model is a short list of quality attributes. The arc42 quality model site counts only 10 top-level areas. ISO 25010 has almost 40 terms. The arc42 author calls the SEI model a great simplification of the somewhat bloated ISO model.

**Where the two models differ**

- **Deployability.** ISO 25010 (2011) lacks operational or DevOps qualities. The fourth edition of Bass et al. presents deployability as a concept.
- **Safety.** The 2011 ISO overview left out safety (safety of life and health, physical integrity). The 2022 draft adds it.
- **Energy efficiency.** ISO 25010 groups time behavior, resource utilization and capacity under performance efficiency. Energy use would fit there as a resource concern.
- **Compatibility.** ISO 25010 lists compatibility (co-existence and interoperability) as a characteristic.

**Scenarios**

Bass et al. coined "quality attribute scenarios." A scenario is a structured way to write a quality requirement. It has six elements: source, stimulus, artifact, environment, response and metric. See the article Quality Attribute Scenario.

## Example

A team builds an online ordering service and wants quality goals. They start from the short list and pick performance and deployability, because they release often. Then they scan the ISO list. They notice the service must work with partner systems. They add that need as a compatibility goal, which ISO 25010 lists as a characteristic.

## Trade-offs

**Benefits.** The short list is a great simplification compared with the ISO model. It also includes deployability, which ISO 25010 (2011) lacked.

**Limits.**
- Critics say deployability suits highly automated online and mobile systems. It suits embedded and real-time systems less, since they are deployed less often and with less automation. They propose "operable" as a top-level attribute, with deployable as a sub-goal.
- The arc42 site lists poor fit for agile work as a drawback of the full six-part scenario template, because the comprehensive approach does not align well with fast-paced, iterative development. It also lists redundancy and time-consuming effort as separate drawbacks.
