---
title: Decision Dependencies
slug: decision-dependencies
category: forces-decisions
kind: concept
summary: Architectural decisions depend on each other. One decision can trigger or split into others.
  Recording these links helps teams see which decisions to make early and where follow-on work comes from.
arc42:
- 4
- 9
step: s09-decisions
related:
- architectural-decision
- levels-of-architectural-decisions
- architectural-decision-record
- arc42-architecture-decisions
- architectural-decision-management-practices
- formulation-of-decision-issues
- architecture-principle
- broker-pattern
checks:
- Decisions that trigger follow-on decisions (for example a principle leading to technology choices) are
  identified.
- Decisions with many or unclear outgoing dependencies are flagged as big or early decisions.
- A superseded decision points to its replacement.
- The decisions section refers to decisions already captured in the solution strategy section.
sources:
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/1807.02798
  title: '[1807.02798] Formal Semantics of Architectural Decision Models'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2025/07/17/ArchitectureDecisionGuidanceTool.html
  title: 'ADG: A Light Architectural Decision Guidance and Management Tool'
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One decision triggers and splits into follow-on decisions.
review:
  status: generated
  flags: []
---

## Explanation

Decisions rarely stand alone. Making one choice often creates the need for others. Decision models can capture these relations between decisions (see Architectural Decision).

**Abstract decisions cause detailed ones.** A high-level decision usually leads to follow-on decisions about design details, technology and product choices. Decisions can reach from the conceptual, pattern-like level all the way down to implementation and DevOps.

**Principles trigger decisions.** A strategic decision or a principle such as loose coupling immediately raises a question: how will the team promote that principle?

**One decision can split into several.** Composite patterns, such as an integration broker, require further decisions about topology, technologies and message delivery. Here one decision decomposes into several issues.

**Many outgoing links mark a big decision.** A decision with many or unclear outgoing dependencies is a "one thing leads to another" case. Such decisions are among those with an early most responsible moment.

**Models can check consistency.** Research on formal definitions of decision models aims at consistency checking. Earlier models supported such checks only to a very limited degree.

**In arc42.** A decision can be marked as superseded, ideally with a reference to its replacement.

## Example

A team adopts loose coupling as a principle. That raises a new question: how will services exchange data? They choose an integration broker. The broker in turn requires decisions on topology, technologies and message delivery. Later, they pick a specific product, which is a technology-level decision. Each step follows from the one before. The team can trace the product choice back to the principle.

## Trade-offs

Consistency checks with formal models are still a research goal, and earlier models offered little support.
