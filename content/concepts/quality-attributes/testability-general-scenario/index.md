---
title: Testability General Scenario
slug: testability-general-scenario
category: quality-attributes
kind: concept
summary: The testability general scenario is a template for writing concrete testability requirements.
  It covers who tests, how the system is controlled and observed, and how easily the system reveals its
  faults.
arc42:
- 10
step: s04-quality-requirements
related:
- testability
- quality-attribute-scenario
- integrability-deployability-and-testability-tactics
- architectural-tactic
- arc42-quality-chapter
- availability-scenario
checks:
- Each testability scenario names whether the source is a human or an automated tester.
- The scenario states how the system is controlled to run tests and how results are observed.
- The scenario names the test harness or test environment where relevant.
- The scenario has a response measure, such as effort to test a given percentage of statements.
sources:
- url: https://hanfak.gitbook.io/workspace/general-paradigms/design-architecture-aims/quality-attributes/testability
  title: Testability | Learning
  site: hanfak.gitbook.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A testability scenario describes one concrete situation in which someone tests a system. The general scenario is the template behind it. For the wider ideas, see the articles Quality Attribute Scenario and Testability.

**Source.** The source of the test activity can be a human tester or an automated tester.

**Environment.** This is the setting in which testing happens. It can include the test harness or the test environments in use. A test harness is the tooling that runs tests and collects results.

**Response.** The system can be controlled so that the desired tests run. The results of those tests can be observed. This links to the tactic of controlling and observing system state. See Integrability, Deployability, Testability and Reliability Tactics.

**Response measure.** Measures show how easily the system under test gives up its faults. Two examples:

- The effort needed to test a given percentage of statements.
- The reduction in risk from remaining errors.

## Example

A team writes a scenario for a billing service. An automated tester runs tests against the service in a test environment with a harness. The team can put the service into the needed state and read the results. The measure is the effort needed to test a chosen percentage of statements. If that effort is too high, the team looks for ways to control and observe the service's state more easily.

## Trade-offs

Choose measures with care. Risk reduction needs a judgment about how serious each remaining fault could be, because faults are not all equal in impact.
