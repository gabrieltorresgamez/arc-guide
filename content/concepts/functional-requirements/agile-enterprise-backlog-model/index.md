---
title: Agile Enterprise Backlog Model
slug: agile-enterprise-backlog-model
category: functional-requirements
kind: concept
summary: 'The Agile Enterprise Backlog Model arranges requirement work items in levels: themes, epics,
  features, stories and tasks. Tests show when items are done and whether the system meets its nonfunctional
  requirements.'
arc42:
- 1
- 4
step: s03-functional-requirements
related:
- epic
- user-story
- acceptance-criteria
- story-splitting
- traceability
- agile-architecture
checks:
- Stories are marked done only when an acceptance test passes.
- Features have one or more functional acceptance tests.
- System validation tests exist to verify the nonfunctional requirements.
- Architecture work is shown as enabler epics, separate from business epics.
sources:
- url: https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/982/A-Lean-and-Scalable-Requirements-Information-Model-for-the-Agile-Enterprise.aspx
  title: A Lean and Scalable Requirements Information Model for the Agile Enterprise > Business Analyst
    Community & Resources | Modern Analyst
  site: modernanalyst.com
  accessed: '2026-11-09'
- url: https://framework.scaledagile.com/epic
  title: Epic - Scaled Agile Framework
  site: framework.scaledagile.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Backlog levels and the tests that verify them
review:
  status: generated
  flags: []
---

## Explanation

The model describes how requirement work items relate when agile teams work at large scale. Each level sits below the one above it.

**The levels**

- **Themes** sit at the top. They live much longer than epics. A set of themes may stay largely unchanged for a year or more.
- **Epics** are the highest-level expression of a customer need. They are held in an epic backlog. (See the article *Epic*.)
- **Features** and **stories** come below epics. (See *User Story*.)
- **Tasks** sit below stories. Each team member estimates the tasks needed to achieve a story.

**Business and enabler epics**

SAFe separates business epics from enabler epics. Enabler epics improve the architectural runway. That runway supports future business or technical needs.

SAFe also manages epics at the portfolio level. It uses a Kanban system for this, which makes the epics easier to see and track.

**Verification**

Tests show when work is done.

- A story is not done until it passes an acceptance test. (See *Acceptance Criterion*.)
- Features usually need one or more functional acceptance tests too. These check that the feature meets the user's needs.
- A system is compliant when it passes system validation tests. These tests verify the nonfunctional requirements.

## Example

A company keeps a long-lived theme: "make ordering easier for customers". One epic under it is "support mobile payments". The epic holds features such as "save a card". Each feature holds stories, and each story holds tasks that team members estimate. A story is done when its acceptance test passes. The system as a whole is compliant when its system validation tests pass.

## Trade-offs

Teams should check how the model fits their own scale before adopting all the levels.
