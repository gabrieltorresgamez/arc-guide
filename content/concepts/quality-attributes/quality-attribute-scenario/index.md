---
title: Quality Attribute Scenario
slug: quality-attribute-scenario
category: quality-attributes
kind: artifact
summary: A quality attribute scenario turns a vague quality wish into a specific, measurable statement.
  It lets a team decide whether the system meets the requirement.
arc42:
- 10
- 1
step: s04-quality-requirements
related:
- arc42-quality-chapter
- architecture-tradeoff-analysis-method-atam
- availability-scenario
- usability-scenario
- smart-requirements
- quality-attribute
- performance-scenario
checks:
- Each quality requirement is written as a scenario that is specific and measurable.
- Every scenario names a response measure, meaning a metric or criteria to judge the response objectively.
- Scenarios state the stimulus event, the stimulated system and the expected response.
- The document uses a clear scenario form (short or long) and applies it consistently.
sources:
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/specify-quality-requirements
  title: How to specify quality requirements | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://faq.arc42.org/questions/C-10-2/
  title: 'Question C-10-2: What is a ''quality scenario''? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/10-8/
  title: 'Tip 10-8: Use (quality) scenarios for architecture analysis or evaluation! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Requirements such as "the system must be fast" or "easy to use" are hard to check. A quality scenario fixes this. It describes a concrete situation and the response the system should show. It also states how to measure that response. The requirement becomes specific, and you can decide whether the system fulfills it.

**The long form.** The Software Engineering Institute (SEI) uses six elements, and the book by Bass et al. follows them. arc42 calls this the long form. It adds fields such as artifact, environment and response. arc42 also offers a short form, called Q42, for lighter use.

Across the sources, the parts fall into these ideas:

- **Stimulus:** the event that hits the system.
- **Stimulated system:** the part of the system that receives the event (the artifact).
- **Environment:** the conditions under which the event happens.
- **Response:** what the system does.
- **Response measure:** the criteria or metric used to judge that response.

**Why the measure matters.** The measure gives you criteria to assess objectively whether the requirement is met. Without it, a scenario stays a matter of opinion.

**Using scenarios.** Teams write them to make quality requirements concrete. They can also use them to analyze or evaluate an architecture systematically. arc42 points to the Architecture Tradeoff Analysis Method (ATAM) for this. arc42 also notes that Bass et al. (2021) use the term Quality Attribute Utility Tree for the tree that structures quality requirements.

## Example

A team starts with the requirement "New users learn the tool quickly." They rewrite it as a scenario. A user who does not know the system (source) starts to use it (stimulus). The response is that the user can operate it. The response measure is that this works after 10 minutes of instruction. Now a test can show whether the requirement is met.

## Trade-offs

The full six-element template is slow to use when you document many scenarios. arc42's quality site suggests a pragmatic option: it merges the six elements into three focused sections. The short Q42 form is another lighter choice. The long form is more detailed, so pick the form that fits how many scenarios you must write.
