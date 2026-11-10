---
title: AS-IS and TO-BE View
slug: as-is-and-to-be-view
category: documentation
kind: practice
summary: An AS-IS view shows the legacy system as it is. A TO-BE view shows the target. Temporary transition
  states between them may differ from both.
arc42:
- 5
- 9
step: s12-evolve
related:
- arc42-architecture-decisions
- architecture-view
- technical-debt
- togaf
- design-for-change
- architectural-decision-record
checks:
- The document states which building blocks belong to the existing system and which belong to the target.
- Temporary transition components are identified, and a plan exists to remove them once the target is
  reached.
- Planned decisions are marked as proposed or accepted, and replaced decisions as deprecated or superseded.
sources:
- url: https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html
  title: Transitional Architecture
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: From the existing system to the target, with temporary transition parts in between.
review:
  status: generated
  flags: []
---

## Explanation

When a legacy system is displaced step by step, the intermediate configurations may need integrations that have no place in the target architecture.

Such transitional parts work like scaffolding on a building. They ease the move from the legacy system to the target. They are not needed once the target architecture is reached, and must be removed.

In an arc42 document:

- The building block view is the static decomposition of a system into building blocks.
- Decisions can carry a status: proposed, accepted, deprecated or superseded. A proposed decision can mark something planned. A superseded one can mark something replaced. The arc42 page does not present this as a technique for transitions, so treat it as a possible convention, not a rule.

## Example

A team runs an old billing system and plans to replace it. The AS-IS view shows the old system. The TO-BE view shows the new one. The team sees that during the move, a small adapter must connect old and new parts. That adapter appears in neither view. They document it as a transition state and plan to remove it once the new system runs alone.

## Trade-offs

Building transitional parts costs effort, and they will be thrown away. The benefits are faster delivery and lower risk in the displacement. Teams should also remove these parts when they are no longer needed, because leftover components can complicate future maintenance.
