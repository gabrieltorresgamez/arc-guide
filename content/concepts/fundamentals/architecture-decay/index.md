---
title: Architecture Decay
slug: architecture-decay
category: fundamentals
kind: concept
summary: Architecture decay is the slow divergence of a built system from its intended design. Small,
  unplanned changes pile up and erode the structure. Refactoring and conformance checks counter it.
arc42:
- 11
- 4
step: s12-evolve
related:
- big-ball-of-mud
- refactoring
- technical-debt
- layered-architecture
- design-for-change
- iterative-and-incremental-development
- keep-it-working
- maintainability
checks:
- The document states how divergence between the intended and implemented architecture is detected, for
  example through conformance checking.
- Known technical debt that may erode the architecture is listed.
- The document names refactoring as the way the team counters structural decay.
sources:
- url: https://ar5iv.arxiv.org/html/2103.11392
  title: '[2103.11392] Understanding Architecture Erosion:The Practitioners’ Perceptive'
  site: ar5iv.arxiv.org
  accessed: '2026-11-09'
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A system can have an intended architecture: the structure its designers decided on. Over time, the code that actually gets built can differ from that plan. This gap is called architecture erosion. It is the divergence between the intended and the implemented architecture.

Even systems that start with a well-defined architecture are prone to structural erosion. The paper on the Big Ball of Mud (see Big Ball of Mud) describes this: changing requirements can gradually undermine even a well-defined structure.

**Why it happens**

- Piecemeal growth can gradually let elements of the system sprawl in an uncontrolled fashion, which undermines its structure.
- Technical debt is a major cause. Technical debt is a short-term solution that may speed up development but can violate architectural principles (see Technical Debt).
- Software tends toward disorder, which the source calls entropy. Fighting it takes invested effort.

**How to counter it**

- Refactoring is the way to arrest entropy in software (see Refactoring).
- Throwing the system away and starting over (reconstruction) is a drastic but frequently necessary alternative.

**How to detect it**

Developers usually identify erosion through a number of symptoms, using a range of practices and tools. One practice is conformance checking, which compares the implemented architecture against the intended one by identifying architectural violations in the implementation.

## Example

A team designs a system in three layers. Over two years, developers add quick fixes. Some of them reach around a layer to save time. Each shortcut works, but the code now differs from the design. A conformance check finds these violations. The team then refactors them away in small steps.

## Trade-offs

Refactoring costs effort, because countering entropy needs invested energy. Starting over is drastic, though sometimes necessary.
