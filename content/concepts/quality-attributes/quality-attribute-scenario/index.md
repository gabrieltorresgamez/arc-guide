---
title: Quality Attribute Scenario
slug: quality-attribute-scenario
order: 40
category: quality-attributes
kind: artifact
summary: A quality attribute scenario turns a vague quality wish into a specific, measurable statement.
  It lets a team decide whether the system meets the requirement.
arc42:
- 10
- 1
step: s04-quality-requirements
related:
- arc42-quality-requirements
- architecture-tradeoff-analysis-method-atam
- reliability
- interaction-capability
- smart-requirements
- quality-attribute
- performance-efficiency
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

Requirements such as "the system must be fast" or "easy to use" are hard to check. A quality scenario fixes this. It describes a concrete situation and the response the system should show [src:1]. It also states how to measure that response. The requirement becomes specific, and you can decide whether the system fulfills it.

**The long form.** The Software Engineering Institute (SEI) template has six elements, and the book by Bass et al. follows them. arc42 calls this the long form. arc42 also offers a short form, called Q42, for lighter use.

- **Source of stimulus:** the entity, such as a person, a system or another actor, that generates the stimulus.
- **Stimulus:** any condition or event that arrives at the system.
- **Artifact:** the part of the system that is affected by the stimulus.
- **Environment:** the conditions or context under which the stimulus occurs.
- **Response:** how the system should react to the stimulus.
- **Response measure:** the measurable criteria that show whether the response is good enough.

**Using scenarios.** Teams write them to make quality requirements concrete. They can also use them to analyze or evaluate an architecture systematically.

## Example

A team starts with the requirement "Customers can order quickly." They rewrite it as a scenario with all six elements:

| Element | Content |
|---|---|
| Source of stimulus | A customer in the web shop |
| Stimulus | Submits an order |
| Artifact | The order service |
| Environment | Normal operation, during the evening peak |
| Response | The order is stored and the customer sees a confirmation |
| Response measure | 95% of orders are confirmed within 3 seconds |

Now a test can show whether the requirement is met.

## Trade-offs

The full six-element template is slow to use when you document many scenarios. arc42's quality site suggests a pragmatic option: it merges the six elements into three focused sections. The short Q42 form is another lighter choice.
