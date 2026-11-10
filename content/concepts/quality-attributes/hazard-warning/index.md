---
title: Hazard Warning
slug: hazard-warning
category: quality-attributes
kind: quality-attribute
summary: Hazard warning is a Safety quality in ISO/IEC 25010. A product with it warns operations or internal
  controls about unacceptable risks, so they can react.
arc42:
- 10
- 8
- 11
step: s04-quality-requirements
related:
- safety
- safety-tactics
- operational-constraint
- risk-identification
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- quality-attribute-scenario
checks:
- 'The document states who receives risk warnings: operations, internal controls, or both.'
- Hazard warning is distinguished from operational constraint, risk identification, fail safe and safe
  integration.
- The design addresses alarm flood during upsets.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=9
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Alarm_management
  title: Alarm management - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Hazard warning is one of five Safety sub-characteristics in ISO/IEC 25010. The product provides warnings of unacceptable risks. The warnings concern risks to operations or to internal controls. Safety is one of the nine quality characteristics in the ISO/IEC 25010 product quality model. See the articles ISO/IEC 25010 Product Quality Model and Safety.

**The other four Safety sub-characteristics**

- **Operational constraint:** the product keeps its operation within safe parameters or states when it meets an operational hazard.
- **Risk identification:** the product can identify event sequences or operations that could expose life, property or the environment to unacceptable risk.
- **Fail safe:** after a failure, the product automatically enters a safe operating mode or returns to a safe condition.
- **Safe integration:** the product stays safe during and after integration with other components.

**Where hazard warning fits**

Hazard warning is about telling someone or something about a risk. The other four cover identifying risk, limiting operation, handling failure, and combining components safely.

**An alarm design problem**

Too many warnings can defeat the purpose. Alarm flood means too many alarms sound during a plant upset. Guidelines and standards on alarm management include EEMUA 191 and ISA 18.2.

## Example

A generic machine-monitoring system detects a risky condition. It sends one warning to the operator console. It also sends a signal to an automatic internal control. Either can then react. The team checks that a single upset does not trigger a flood of alarms.

## Trade-offs

Too many alarms at once, known as alarm flood, are a usability problem, and a poorly configured alarm system does not improve operator situation awareness. Alarm management guidelines such as EEMUA 191 and ISA 18.2 address alarm usability.
