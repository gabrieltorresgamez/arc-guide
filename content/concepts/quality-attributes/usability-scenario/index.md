---
title: Usability Quality Attribute Scenario
slug: usability-scenario
category: quality-attributes
kind: concept
summary: A usability scenario describes a user action (the stimulus) and how the system should react (the
  response). Adding a number, such as a time limit, makes a usability requirement testable.
arc42:
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- usability
- usability-tactics
- arc42-quality-chapter
- iso-iec-25010-quality-model
- smart-requirements
- architectural-pattern
checks:
- Each usability requirement is written as a scenario with a stimulus (user action) and an expected system
  response.
- Usability scenarios carry a measurable value, such as a time limit in seconds.
- Where users must make very few or no errors, a scenario uses error rate as its measure.
- Learnability scenarios state the starting condition, such as first use without demo, tutorial, or training,
  and the reason behind it.
- Usability scenarios are linked to the architecture pattern or design that supports them.
sources:
- url: https://www.sei.cmu.edu/library/achieving-usability-through-software-architecture/
  title: Achieving Usability Through Software Architecture | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/1-12/
  title: 'Tip 1-12: Explain quality requirements through scenarios! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/ease-of-use
  title: Ease of Use | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/requirements/new-user-completes-core-tasks-without-training
  title: New user completes core tasks without prior training | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

"The system must be easy to use" is hard to test. A usability scenario fixes this. It describes one aspect of usability as a stimulus and a response. The stimulus is what the user does or what happens. The response is how the system reacts.

A scenario becomes testable when it carries a measure. The arc42 material shows these kinds:

- **Time until the system responds.** After switching on, a navigation system accepts input from its screen within 4 seconds.
- **Time to reach an action.** Users can tap Find within 3 seconds of opening the interface.

A scenario can also describe a situation. One example is a new user who logs into an enterprise system for the first time. That user has had no demo, tutorial, or instructor-led training. The scenario then asks whether the user can complete the core tasks. The reason is practical. The organisation cannot afford extended training programmes, so the software must be self-explanatory to users who know the domain.

For the wider idea, see the articles Quality Attribute Scenario and arc42 Quality Requirements.

A scenario can also connect to design. The SEI report on usability and architecture pairs each usability scenario with an architecture pattern that implements it. So a scenario says what to test. It also points toward a design that supports it.

## Example

A team builds a mobile app for field technicians. Their first draft says "the app must be user-friendly." They rewrite it as a scenario. A technician opens the app on a job site. The Search button must then be tappable within a fixed number of seconds. The team can now time this in a test and decide whether the requirement is met.
