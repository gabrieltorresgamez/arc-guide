---
title: Quality Attributes in Use Case Descriptions
slug: quality-attributes-in-use-case-descriptions
category: quality-attributes
kind: practice
summary: Most quality requirements belong to one specific use case. Write them in that use case, then
  refine them into measurable quality attribute scenarios. This also shows which conditions the use case
  left unstated.
arc42:
- 10
- 1
step: s04-quality-requirements
related:
- quality-attribute-scenario
- use-case-template
- use-case
- smart-requirements
- arc42-quality-chapter
- architecturally-significant-requirement
- story-splitting
- use-case-completeness-check
checks:
- System-wide quality requirements are stated separately from the use cases.
- Each use-case-specific quality requirement names the functional requirement it applies to.
- Each quality requirement for a use case states which environment applies, such as normal operation,
  peak load or error.
- Quality requirements from use cases are refined into specific, measurable scenarios.
sources:
- url: https://www.infoq.com/podcasts/use-case-2/
  title: Ivar Jacobson on Use Case 2.0 - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://github.com/socadk/design-practice-repository/blob/master/activities/DPR-SMART-NFR-Elicitation.md
  title: design-practice-repository/activities/DPR-SMART-NFR-Elicitation.md at master · socadk/design-practice-repository
    · GitHub
  site: github.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/11/19/ExtraExtraReadAllboutIt.html
  title: Do Software Architectures Meet Extra-Functional or Non-Functional Requirements?
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
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

Some quality requirements apply to the whole system. Others apply to one use case only. System-wide requirements need their own place, separate from the use cases. Use-case-specific requirements can sit in the use case text itself. Most non-functional requirements in a system are of this second kind.

**Linking function to quality.** A quality requirement is easier to act on when it names the feature it applies to. A useful question is: which functional requirement needs this quality property? Use-Case 2.0 builds this link in. Each slice of a use case inherits the non-functional requirements of its parent use case.

**Refining into scenarios.** A line such as "must be fast" is vague. A quality attribute scenario makes it concrete and measurable (see Quality Attribute Scenario). arc42 says such scenarios let you decide whether a requirement is fulfilled. They should be specific and measurable.

The use case supplies raw material for the scenario:
- Its functional context gives the sources and stimuli. Splitting a story into smaller pieces gives the same kind of input.
- Operating conditions go under "environment".
- The behavior goes under "response".

**Finding gaps.** Writing the scenario forces you to ask which environment applies. Is it normal operation, peak load, or an error situation?

**Traceability.** arc42 section 10 describes quality scenarios. It also mentions the quality tree (also called utility tree).

## Example

A use case "Place order" has a field for its own non-functional requirements. It says only "must be fast". The team asks which environment this applies to and writes a scenario: a customer submits an order (stimulus) during peak load (environment). The system confirms the order (response) in under a set time (response measure). While writing it, the team notices the use case never said what should happen when the payment service fails. That is a gap to close.

## Trade-offs

Scenarios make requirements measurable, but they are also a bit repetitive. Keeping requirements inside each use case is convenient, but system-wide requirements must still be written down separately.
