---
title: Sweeping It Under the Rug
slug: sweeping-it-under-the-rug
category: fundamentals
kind: pattern
summary: Sweeping It Under the Rug is a pattern for tangled code you cannot remove. You fence the mess
  off from the rest of the system and put a clean interface in front of it.
arc42:
- 5
- 11
step: s12-evolve
related:
- big-ball-of-mud
- refactoring
- technical-debt
- coupling-and-cohesion
- shearing-layers
- architecture-decay
- information-hiding
checks:
- Disordered parts of the system are identified and isolated from the rest of it.
- Boundaries around the messy code start where coupling is lowest.
- Global data is split into distinct data structures.
- A façade fronts the quarantined code.
sources:
- url: https://www.laputan.org/mud/mud.html
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A façade fences off the tangled code from the rest of the system.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Some code is overgrown and tangled. People call it spaghetti code. It is hard to understand, fix or extend (see Big Ball of Mud).

**How it works**

A simple way to begin to control decline is to cordon off the blighted areas and put an attractive façade around them.

## Example

A company has an old billing module with tangled code. The team cordons it off and puts a façade in front of it. The mess stays inside the boundary.
