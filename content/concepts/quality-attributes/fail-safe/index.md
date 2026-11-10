---
title: Fail Safe
slug: fail-safe
category: quality-attributes
kind: quality-attribute
summary: Fail safe means a system reacts to a failure by automatically moving into a safe mode or condition.
  It does not prevent failure. It limits the harm a failure can cause.
arc42:
- 10
- 8
- 11
step: s04-quality-requirements
related:
- safety
- safety-tactics
- fault-tolerance
- graceful-degradation
- iso-iec-25010-quality-model
- quality-attribute-scenario
- availability
- security
checks:
- The document states what the safe state is for each relevant failure.
- Fail-safe behavior is written as a quality scenario, such as a severe error leading to a shutdown into
  a safe state.
- Terms such as fail operational, fail degraded, fail safe and fail secure are defined, since usage varies.
- Conflicts between fail safe and fail secure are identified and resolved explicitly.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=9
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/fail-safe
  title: Fail safe | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-10'
- url: https://en.wikipedia.org/wiki/Fail-safe
  title: Fail-safe - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-10'
- url: https://arxiv.org/abs/2106.11042
  title: '[2106.11042] A Taxonomy to Unify Fault Tolerance Regimes for Automotive Systems: Defining Fail-Operational,
    Fail-Degraded, and Fail-Safe'
  site: arxiv.org
  accessed: '2026-11-10'
diagrams:
- file: diagram-1.mmd
  caption: On failure, the system moves by itself into a safe state.
review:
  status: generated
  flags: []
---

## Explanation

Fail safe is a sub-characteristic of Safety in the ISO/IEC 25010 quality model. Safety means avoiding states in which people, property or the environment are endangered (see the articles Safety and ISO/IEC 25010 Product Quality Model). Fail safe covers one part of that: what the product does when something breaks.

The definition has two parts. First, the product acts on its own. It places itself in a safe operating mode, or reverts to a safe condition. Second, the goal is to limit the harm that follows from the failure. In general, a fail-safe is a design feature or practice that responds to a failure so that harm to equipment, environment or people stays small.

Fail safe does not mean failure is impossible or unlikely. A fail-safe system can still fail. The design only limits the unsafe consequences.

One example is a traffic light controller. A conflict monitor unit detects faults and switches the intersection to all-flashing error signals.

Related terms are used in different ways:

- **Fail operational and fail degraded.** One taxonomy paper names three fault-tolerance regimes: fail-operational, fail-degraded and fail-safe. It also gives a concise definition of a safe state. It notes that such regimes are often used without definitions and can be ambiguous. See Fault Tolerance and Graceful Degradation.
- **Fail secure.** Fail secure (also called fail closed) puts security first, so that access or data does not reach the wrong people when something fails. This can conflict with fail safe. In a fire, doors that unlock may serve safety. Doors that stay locked serve security.

To make fail safe concrete, write it as a quality scenario (see Quality Attribute Scenario). arc42 gives an example: severe errors are detected and the system shuts down into a safe state.

## Example

A hypothetical machine that heats material has a monitor that checks the temperature sensor. If the sensor stops reporting, the monitor switches the heater off and shows an error. The machine is no longer useful, but nobody is endangered. The team writes this down as a scenario: sensor failure is detected, and the machine moves to its safe state.

## Trade-offs

Fail safe can conflict with fail secure, as the door example shows.
