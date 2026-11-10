---
title: ATAM Phase 0 (Setup and Documentation Improvement)
slug: atam-phase-0
category: evaluation
kind: method
summary: ATAM Phase 0 is the preparation before an architecture evaluation. The team checks whether the
  architecture is documented well enough to evaluate, and it requests missing information through targeted
  questions.
arc42:
- 1
- 3
- 10
step: s11-evaluate
related:
- atam-application-phases
- architecture-tradeoff-analysis-method-atam
- atam-phase-1-architecture-centric-analysis
- atam-evaluation-team-and-stakeholder-selection
- battlefield-control-system-atam-case-study
- quality-attribute-scenario
- atam-roles
- software-architecture-evaluation
checks:
- The documentation shows how the architecture maps to software constructs and names the architectural
  styles used.
- Initial quality attribute requirements and scenarios are recorded.
- Open documentation gaps are written as targeted questions, for example on dependencies, database and
  data volume.
- The architecture describes facilities for self-testing and monitoring of components.
sources:
- url: https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf
  title: 'ATAM: Method for Architecture Evaluation'
  site: sei.cmu.edu
  accessed: '2026-11-10'
diagrams:
- file: diagram-1.mmd
  caption: 'Preparation loop: gather, check documentation, ask questions until it is sufficient.'
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

See ATAM Application Phases for how the phases are numbered.

A scenario is a brief description of how a stakeholder interacts with the system.

## Example

A team plans to evaluate an order system. The first documents show only boxes labeled "Orders", "Payments" and "Shipping" with arrows between them. Nobody can tell which code or modules sit behind the boxes. The evaluation team decides the documentation is too vague to analyze. It sends questions: how is the order-handling software structured, how large is the database, and how much data flows between the boxes? It also adds a database expert to the team. Analysis starts only after the answers arrive.
