---
title: Performance Efficiency Scenario
slug: performance-scenario
category: quality-attributes
kind: artifact
summary: A performance efficiency scenario turns a vague goal like "be fast" into a testable statement.
  Something triggers the system, the system reacts, and a measurable criterion says whether the reaction
  was good enough.
arc42:
- 10
- 1
step: s04-quality-requirements
related:
- quality-attribute-scenario
- performance-efficiency
- performance-tactics
- arc42-quality-chapter
- acceptance-criteria
- iso-iec-25010-quality-model
- architecture-tradeoff-analysis-method-atam
- availability-scenario
checks:
- Each performance requirement is written as a scenario with a stimulus, an affected artifact, and an
  environment.
- Each performance scenario has a measurable response measure, such as a time limit or a percentile.
- Performance scenarios are usable as acceptance criteria that decide whether the requirement is fulfilled.
- Performance scenarios are listed in the quality requirements section and used to evaluate the architecture.
sources:
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/specify-quality-requirements
  title: How to specify quality requirements | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Teams often write performance goals such as "the system must be fast". Nobody can test that. A quality scenario fixes this. arc42 says quality scenarios make quality requirements concrete and let you decide whether they are fulfilled. They can serve as acceptance criteria.

arc42 says usage scenarios describe how the running system reacts to a stimulus, and that they include scenarios describing efficiency or performance. A stimulus is an event that hits the system, such as a user request.

Parts of a scenario include:

- **Artifact:** the part of the system that the stimulus affects.
- **Environment:** the conditions under which the stimulus occurs.
- **Response measure:** a measurable criterion that lets you judge objectively whether the requirement is met.

The response measure makes the scenario testable. A percentile is one example. One example from the Q42 site, for search results, is a criterion saying the 95th percentile response time remains under 800 milliseconds.

The simplest form is short. arc42 gives this example: the system reacts to a user's request within one second.

Performance efficiency is also a standard quality category. ISO 25010 defines it as performing functions within a specified time, with efficient use of resources. Its subcharacteristics are time behaviour, resource utilization, and capacity. They give you ideas for what to measure. See ISO/IEC 25010 Product Quality Model.

See Quality Attribute Scenario for the general template.

## Example

An online shop team starts with the vague goal "search should be quick".

They rewrite it as a scenario. A visitor sends a search request (the stimulus). The search component is the artifact. The environment is normal daily operation. The response measure says the 95th percentile response time stays under a chosen limit.

Now a load test can show a clear pass or fail.

## Trade-offs

One point follows from the definitions: a scenario only helps if its response measure is measurable. A goal without a measurable criterion cannot be judged objectively.
