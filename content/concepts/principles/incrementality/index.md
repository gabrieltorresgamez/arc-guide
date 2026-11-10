---
title: Incrementality
slug: incrementality
category: principles
kind: principle
summary: Incrementality means building and changing an architecture in small steps, with feedback after
  each step. It replaces designing everything at once, because requirements keep moving and not every
  issue can be foreseen.
arc42:
- 4
- 9
- 11
step: s12-evolve
related:
- design-for-change
- iterative-and-incremental-development
- agile-architecture
- evolutionary-domain-modeling
- keep-it-working
- last-responsible-moment
- architecture-decay
- separation-of-concerns
checks:
- The document describes how first versions are released early and how functionality is added step by
  step.
- The document shows how user and stakeholder feedback is collected and fed back into the design.
- Prototypes, if used, are labeled as learning tools and not treated as final designs.
- The document states what keeps the overall structure from eroding as small changes accumulate.
- Capabilities are built only when they are needed, not in advance.
sources:
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/SpreadingIncrementalism.html
  title: Spreading Incrementalism
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Incremental loop: build a small step, release it, gather feedback, adjust, repeat.'
review:
  status: generated
  flags: []
---

## Explanation

Instead of one complete plan, the team builds in small steps and learns from each one.

**Why not design everything at once?**

- Requirements keep changing. Fowler says changing requirements are a major headache for planned design, and that building in flexibility only helps with changes you foresaw.
- Nobody can think through every issue before implementation starts.

**What this approach asks for**

- Let the design grow as the system is built. Fowler calls this evolutionary design.
- Favor an early first release. In discussing story ordering, Fowler says complexity the first release does not need is worth doing afterwards, and that releasing sooner is better even if adding something later takes more effort.
- Do not build capability before it is needed. Early work on the wrong solution wastes effort.
- Use prototypes to explore the problem. A prototype helps you learn, but it is not a good design and should not be mistaken for one.

**Not purely emergent**

Incremental does not mean unplanned. Fowler says incremental design needs something that makes the design converge into order.

## Example

A team builds an online booking system. It ships a first version with only the basic booking flow. Real users try it and give feedback. The team then adds the next feature, and the next, adjusting the design each time. It builds no feature before it is needed.

## Trade-offs

Small steps bring early feedback. Done in an uncontrolled way, incremental design is likely to end up as a mess. Teams need some mechanism that keeps the design converging to counter these risks.
