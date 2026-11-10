---
title: INVEST Applied to Architectural Work
slug: invest-applied-to-architectural-work
category: functional-requirements
kind: practice
summary: 'INVEST is a checklist for writing good user stories. Applied to architectural work, it fits
  unevenly: value and testability carry over well, while independence is doubtful because architectural
  goals and components depend on each other.'
arc42:
- 10
- 4
- 11
step: s04-quality-requirements
related:
- invest-criteria
- user-story
- quality-attribute-scenario
- architecturally-significant-requirement
- acceptance-criteria
- technical-debt
- story-splitting
- agile-enterprise-backlog-model
checks:
- Each architectural backlog item states its value to the business.
- Each architectural backlog item has a measurable criterion, such as a response measure.
- Dependencies between architectural items are made visible, not assumed away.
- Each architectural item is small enough to be specific and measurable.
sources:
- url: https://xp123.com/invest-in-good-stories-and-smart-tasks/
  title: INVEST in Good Stories, and SMART Tasks - XP123
  site: xp123.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/non-functional-requirements-as-user-stories
  title: Non-functional Requirements as User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://framework.scaledagile.com/enablers
  title: Enablers - Scaled Agile Framework
  site: framework.scaledagile.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/
  title: Quality Attribute Workshops (QAWs), Third Edition | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

INVEST is a checklist for good user stories (see INVEST Criteria and User Story). The letters stand for Independent, Negotiable, Valuable, Estimable, Small and Testable. 

**Independent.** The checklist asks that stories do not overlap in concept and can be scheduled and implemented in any order. The source notes that this independence cannot always be achieved.

**Negotiable.** A good story is not an explicit contract. Its details are co-created by the customer and programmer during development.

**Valuable.** The checklist means value to the customer. It advises slicing work vertically through the layers, not by technical layer. Developer concerns should be framed so that the customer sees them as important.

**Estimable.** Being estimable depends partly on how well the item has been negotiated, on its size, and on the team's experience.

**Small.** Stories are meant to represent at most a few person-weeks of work. Smaller stories tend to get more accurate estimates.

**Testable.** Non-functional requirements, such as performance, can be tested. A quality attribute scenario (see Quality Attribute Scenario) defines a response measure, the metric used to judge the system's response. The SEI Quality Attribute Workshop yields prioritized, refined scenarios.

**Constraints and enablers.** Constraints and non-functional requirements can be written as user stories. SAFe also defines enabler items, which extend the architectural runway of the solution and are managed like customer-facing items.

## Example

A team wants faster search. A vague item reads "Improve the search architecture." It has no stated value and no way to check it. The team rewrites it: "During peak load, search results appear within 2 seconds for 95% of requests." The business confirms that slow search loses customers, so the value is clear. The 2-second target makes the item measurable. The team then estimates and schedules it.

## Trade-offs

Measurable criteria make an item specific and checkable.
