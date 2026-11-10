---
title: Operational Constraint
slug: operational-constraint
category: quality-attributes
kind: quality-attribute
summary: Operational constraint is a safety quality in ISO/IEC 25010. It describes a product that keeps
  its operation within safe parameters or states when it meets an operational hazard.
arc42:
- 1
- 10
- 11
step: s04-quality-requirements
related:
- safety
- safety-tactics
- hazard-warning
- risk-identification
- iso-25010-2023-revision
- iso-iec-25010-quality-model
- fault-tolerance
- quality-attribute-scenario
checks:
- The document names the safe parameters or safe states within which the product must keep operating.
- Each operational hazard the product may meet is linked to a limit or constraint that applies to it.
- Operational constraint is described separately from fail safe, hazard warning, risk identification and
  safe integration.
- Where functional safety standards apply, the document names them, such as IEC 61508 or ISO 26262.
sources:
- url: https://quality.arc42.org/qualities/operational-constraint
  title: Operational constraint | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=9
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://www.itemis.com/en/glossary/functional-safety/
  title: What is Functional Safety? | itemis AG
  site: itemis.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Operational constraint is one sub-characteristic of Safety in ISO/IEC 25010. Safety means the product avoids states that endanger life, health, property or the environment. See the articles on Safety and on the ISO/IEC 25010 Product Quality Model.

Operational constraint is the product's ability to keep its operation inside safe parameters or safe states when it meets an operational hazard. A hazard is a situation that could lead to harm. The product limits what it does, so the hazard does not turn into damage.

Two typical examples show the idea:

- A product prevents an aircraft from entering a stall.
- A radiology device limits the radiation it releases to a safe threshold.

In both cases the product itself sets the limit.

**Sibling sub-characteristics.** Safety has other sub-characteristics. Each covers a different part of the safety problem:

- Risk identification: the product can identify events or operations that expose life, property or the environment to unacceptable risk. See Risk Identification and Safe Integration.
- Fail safe: on failure, the product automatically places itself in a safe operating mode.
- Hazard warning: the product warns of unacceptable risks. See Hazard Warning.
- Safe integration: the product stays safe during and after integration with other components.

Operational constraint is the one about limiting operation itself. Fail safe is about the safe mode a product enters on failure.

**Link to functional safety.** Functional safety commonly reduces risk by detecting faults and moving the system into a safe state. IEC 61508 is the basic standard for this. ISO 26262 applies in the automotive domain. The standards use integrity levels: SIL 1-4 and ASIL A-D.

## Example

A hypothetical infusion pump delivers medicine at a set rate. A nurse mistypes a dose far above the safe maximum. The pump does not accept the value. It stays within its safe limit and tells the nurse why. The safe limit is the operational constraint.
