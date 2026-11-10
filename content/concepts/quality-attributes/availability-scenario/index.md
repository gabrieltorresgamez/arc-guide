---
title: Availability Scenario
slug: availability-scenario
category: quality-attributes
kind: artifact
summary: 'An availability scenario describes one concrete failure and how the system should react, in
  six parts: source, stimulus, artifact, environment, response, and response measure. The measure makes
  the requirement testable.'
arc42:
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- availability
- availability-tactic
- fault
- arc42-quality-chapter
- architecture-tradeoff-analysis-method-atam
- heartbeat
- availability-tactics-fault-detection
checks:
- Each availability scenario names a source, stimulus, artifact, environment, response, and response measure.
- Each scenario states a response measure that can be checked, not only a vague percentage.
- Availability targets such as 99% state a measurement window and an SLO boundary.
- Each scenario names the affected part of the system and the operating condition when the failure occurs.
sources:
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/specify-quality-requirements
  title: How to specify quality requirements | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A detailed quality scenario has six parts: source, stimulus, environment, artifact, response, and response measure. An availability scenario uses this layout to describe one failure and the expected reaction. The general idea is covered in Quality Attribute Scenario.

The parts, in plain words:

- **Source:** the entity that starts the scenario. It can be a user, a system, or an event.
- **Stimulus:** the event that hits the system. For availability, this is a failure.
- **Artifact:** the part of the system that the stimulus affects. This can be a building block or another element.
- **Environment:** the operating condition when the stimulus occurs.
- **Response:** what the system does when the stimulus arrives.
- **Response measure:** the metric used to judge whether the response is good enough.

The response measure is what makes the scenario checkable. A vague statement such as "the user registration service must be available 7x24h 99%" leaves gaps. It should be made precise with a measurement window and an SLO boundary.

**Connection to tactics.** A scenario says what should happen. Availability tactics describe design choices that make it happen. The SEI takes its tactics from the fourth edition of Software Architecture in Practice. Fault detection tactics come first, because the system must detect or anticipate a fault before it can act on it. Recovery tactics split into preparation and repair tactics, and reintroduction tactics.

## Example

A team writes a scenario for an online shop. The source is a hardware fault. The stimulus is a server failure. The artifact is the order service. The environment is normal operation. The response is that the system keeps running. The response measure is no downtime. This follows a scenario on arc42's availability page: a server fails and the system continues without downtime.
