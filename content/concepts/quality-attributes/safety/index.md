---
title: Safety
slug: safety
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
- operational-constraint
- hazard-warning
- risk-identification
- heartbeat
- iso-iec-25010-quality-model
- fault-tolerance
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
diagrams:
- file: diagram-1.mmd
  caption: Generic paths from normal operation to a safe state.
review:
  status: generated
  flags: []
---

## Explanation

Safety means the system avoids states in which human life, health, property or the environment is endangered. ISO/IEC 25010 breaks this into five sub-characteristics. The article ISO/IEC 25010 Product Quality Model covers the wider model.

**The five sub-characteristics**

- **Operational constraint:** when the system meets an operational hazard, it keeps its operation within safe parameters or states. See the article Operational Constraint.
- **Risk identification:** the system can recognize sequences of events or operations that expose life, property or the environment to unacceptable risk.
- **Fail safe:** after a failure, the system automatically enters a safe operating mode or returns to a safe condition.
- **Hazard warning:** the system warns of unacceptable risks early enough for operators or internal controls to react and keep operations safe. See the article Hazard Warning.
- **Safe integration:** the system stays safe during and after integration with other components.

**Related design ideas**

A fail-safe default makes the system fall into a known-safe state when something unexpected happens. It does not fall into an open, permissive or undefined state.

Watchdog supervision is one safety tactic. A component sends a periodic heartbeat. If the heartbeat stops, the system moves to a safe state. See the articles Heartbeat and Safety Tactic.

**Lessons from the Therac-25 analysis**

Safety is a property of the whole system, not of the software alone. Safety must be built into the software. It must also be assured at the system level, even when the software has errors.

Reusing software does not guarantee safety in a new system. In the older Therac-20, hardware interlocks limited the harm.

## Example

A hypothetical machine controller sends a heartbeat every 100 ms to a separate supervisor. If the heartbeat stops, the supervisor moves the machine to a known-safe state. The machine does not stay in whatever state it was in. This is a watchdog with a fail-safe default. The team also lists the event sequences that could harm an operator, which is risk identification.

## Trade-offs

One point follows from the Therac-25 lessons. Software-level safety alone is not enough. Safety must also be assured at the system level.
