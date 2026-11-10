---
title: Shearing Layers
slug: shearing-layers
category: principles
kind: principle
summary: Shearing Layers means grouping parts of a system that change at similar rates and keeping them
  apart from faster or slower parts. The boundaries between layers help lasting abstractions emerge.
arc42:
- 4
- 8
- 9
step: s07-solution-strategy
related:
- design-for-change
- adaptability
- modifiability
- separation-of-concerns
- layers-pattern
- big-ball-of-mud
- architecture-decay
- architectural-forces
checks:
- The document states which parts of the system change at similar rates and groups them together.
- Elements that change most quickly are kept in data, not hard-wired into code.
- Widely deployed, hard-to-change elements, such as enterprise database schemas, are identified, with
  the cost of changing them noted.
- The balance between adaptability and stability is addressed explicitly where layers are chosen.
sources:
- url: https://www.laputan.org/mud/mud.html
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Shearing Layers is a pattern. Systems and their parts evolve at different rates, and things that change quickly tend to become distinct from things that change more slowly.

**Fault lines.** Where change rates differ, the layers act like fault lines. These boundaries help enduring abstractions emerge.

## Example

An online shop has prices and promotions that change daily. Its checkout rules change a few times a year. Its customer database layout rarely changes, because many systems depend on it.

The team keeps prices and promotions as data that staff can edit. Checkout rules live in their own part of the code. The database layout stays untouched. Each group changes at its own pace without forcing changes in the others.
