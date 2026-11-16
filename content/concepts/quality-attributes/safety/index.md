---
title: Safety
slug: safety
order: 90
category: quality-attributes
kind: quality-attribute
summary: Safety is a system's ability to avoid states that endanger people, property or the environment.
  ISO/IEC 25010 splits it into five parts, from limiting operation to staying safe after integration.
arc42:
- 1
- 8
- 10
- 11
step: s04-quality-requirements
related:
- safety-tactics
- iso-iec-25010-quality-model
- reliability
- quality-attribute-scenario
checks:
- The document states which operational hazards exist and how the system limits its operation to safe
  parameters or states when they occur.
- The document describes the safe state the system enters or returns to after a failure.
- The document says how operators or controls get warned of unacceptable risks early enough to react.
- The document explains how safety is kept when components are integrated, including reused software.
- Safety is assured at system level, not only in software, for example with hardware safeguards.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=9
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/fail-safe-defaults
  title: Fail-Safe Defaults | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_5.html
  title: Therac-25 - V
  site: web.mit.edu
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: "ISO 25010"
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://www.itemis.com/en/glossary/functional-safety/
  title: "What is Functional Safety? | itemis AG"
  site: itemis.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/operational-constraint
  title: "Operational constraint | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/risk-identification
  title: "Risk identification | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Fail-safe
  title: "Fail-safe - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-10'
- url: https://arxiv.org/abs/2106.11042
  title: "[2106.11042] A Taxonomy to Unify Fault Tolerance Regimes for Automotive Systems: Defining Fail-Operational, Fail-Degraded, and Fail-Safe"
  site: arxiv.org
  accessed: '2026-11-10'
- url: https://quality.arc42.org/qualities/fail-safe
  title: "Fail safe | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Alarm_management
  title: "Alarm management - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/hazard-warning
  title: "Hazard warning | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/safe-integration
  title: "Safe integration | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/shutdown-to-safe-state
  title: "Severe errors are detected and the system shuts down into safe state"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/provable-insulin-dosage-safety
  title: "Provable Insulin Dosage Safety"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/calibrated-medical-triage-confidence
  title: "Medical triage model confidence is calibrated"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/safety
  title: "Safety | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: Generic paths from normal operation to a safe state.
review:
  status: generated
  flags: []
---

## Explanation

Safety means the system avoids states in which human life, health, property or the environment is endangered. ISO/IEC 25010 breaks this into sub-characteristics. The article ISO/IEC 25010 Product Quality Model covers the wider model.

**Related design ideas**

A fail-safe default makes the system fall into a known-safe state when something unexpected happens. It does not fall into an open, permissive or undefined state.

In the arc42 quality model, watchdog supervision is a tactic related to fail-safe defaults. A component sends a periodic heartbeat. If the heartbeat stops, the system moves to a safe state. See the article Safety Tactic.

**Lessons from the Therac-25 analysis**

Safety is a property of the whole system, not of the software alone. Safety must be built into the software. It must also be assured at the system level, even when the software has errors.

Reusing software does not guarantee safety in a new system. In the Therac-20, hardware interlocks limited the harm.

**Tactics.** See the article Safety Tactic.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Operational constraint** means the product keeps its operation within safe parameters or states when it meets an operational hazard. More: [arc42 quality model](https://quality.arc42.org/qualities/operational-constraint), [What is Functional Safety? | itemis AG](https://www.itemis.com/en/glossary/functional-safety/).
- **Risk identification** is a product's ability to spot events or operations that could put people, property or the environment at unacceptable risk. More: [arc42 quality model](https://quality.arc42.org/qualities/risk-identification).
- **Fail safe** means a system reacts to a failure by automatically moving into a safe mode or condition. It does not mean that failure is impossible or harmless. More: [arc42 quality model](https://quality.arc42.org/qualities/fail-safe), [Fail-safe - Wikipedia](https://en.wikipedia.org/wiki/Fail-safe), [2106.11042 A Taxonomy to Unify Fault Tolerance Regimes for Automotive Systems: Defining Fail-Operational, Fail-Degraded, and Fail-Safe](https://arxiv.org/abs/2106.11042).
- **Hazard warning** means the product warns operations or internal controls about unacceptable risks, so they can react. More: [arc42 quality model](https://quality.arc42.org/qualities/hazard-warning), [Alarm management - Wikipedia](https://en.wikipedia.org/wiki/Alarm_management).
- **Safe integration** means that the product keeps safety intact during and after its integration with one or more other components. More: [arc42 quality model](https://quality.arc42.org/qualities/safe-integration).

**In the arc42 quality model.** The arc42 quality model has its own page on [Safety](https://quality.arc42.org/qualities/safety).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [Severe errors are detected and the system shuts down into safe state](https://quality.arc42.org/requirements/shutdown-to-safe-state), [Provable Insulin Dosage Safety](https://quality.arc42.org/requirements/provable-insulin-dosage-safety), [Medical triage model confidence is calibrated](https://quality.arc42.org/requirements/calibrated-medical-triage-confidence).

## Example

A hypothetical machine controller sends a heartbeat every 100 ms to a separate supervisor. If the heartbeat stops, the supervisor moves the machine to a known-safe state. The machine does not stay in whatever state it was in. This is a watchdog with a fail-safe default. The team also lists the event sequences that could harm an operator, which is risk identification.

## Trade-offs

One point follows from the Therac-25 lessons. Safety must be built into the software and also assured at the system level, despite software errors.
