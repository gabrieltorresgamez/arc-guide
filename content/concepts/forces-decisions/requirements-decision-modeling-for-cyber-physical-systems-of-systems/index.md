---
title: Requirements-Decision Modeling for Cyber-Physical Systems of Systems
slug: requirements-decision-modeling-for-cyber-physical-systems-of-systems
category: forces-decisions
kind: method
summary: ReDeMo is a formal model that links non-functional requirements (qualities such as sustainability)
  to architectural decisions for cyber-physical systems. It comes from the TaSSAreCt research project
  and is built into a SysML v2-based toolchain for architects.
arc42:
- 9
- 10
- 4
step: s09-decisions
related:
- architectural-decision
- quality-attribute
- architecturally-significant-requirement
- architectural-trade-off-thinking
- traceability
- architecture-decision-rationale
- energy-efficiency-tactics
- decision-documentation-and-requirements-management
checks:
- Non-functional requirements are explicitly linked to the architectural decisions that address them.
- Sustainability is considered as a requirement category for resource-constrained cyber-physical systems.
- Architectural decisions and requirements are collected in a shared knowledge base.
sources:
- url: https://tassarect.github.io
  title: TaSSAreCt – Towards Sustainable Software Architectures for CPSoS
  site: tassarect.github.io
  accessed: '2026-11-09'
- url: https://www.zhaw.ch/en/research/project/76245
  title: Towards Sustainable Software Architectures for Cyber-physical Systems of Systems (TaSSAreCt)
    | ZHAW Zurich University of Applied Sciences
  site: zhaw.ch
  accessed: '2026-11-09'
- url: https://alexandria.unisg.ch/entities/funding/4c47be0e-9009-407c-a004-6c9062022a38
  title: Towards Sustainable Software Architectures for Cyber-physical Systems of Systems
  site: alexandria.unisg.ch
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Requirements linked to decisions, supported by a knowledge base and a toolchain.
review:
  status: generated
  flags: []
---

## Explanation

Cyber-physical systems (CPS) combine software with physical devices. A cyber-physical system of systems (CPSoS) joins several such systems. The research project TaSSAreCt studies how software architecture can support the sustainability, quality, and long-term evolution of these systems. The Swiss National Science Foundation funds it, and it runs from 2025 to 2028.

One project goal is to find out how CPS influence traditional non-functional properties and new ones. Non-functional requirements (NFRs) describe how the software should work. See the articles Quality Attribute and Architectural Decision for background.

ReDeMo is a formal model that links NFRs with architectural decisions. A formal model states these links in a precise, structured way.

The project also builds a knowledge base of architectural decisions and requirements in CPS. The model is implemented in a toolchain based on SysML v2, a modeling language, to support architects.

Sustainability is a key NFR category in this work. It matters most for resource-constrained CPS, which have limited resources to work with.

The project has two principal investigators, one at the University of St. Gallen (HSG) and one at ZHAW.

## Example

A team builds a network of battery-powered field sensors. One requirement says the sensors must run for years without a battery change. Another says they must report readings quickly. With a requirements-to-decisions model, the team records both requirements. It then links each decision, such as how often a sensor transmits, to the requirements it affects. Later, anyone who questions a decision can see which requirements it serves.

## Trade-offs

The project runs until 2028, so the model and toolchain are research work in progress. Treat them as an approach to watch, not a settled standard.
