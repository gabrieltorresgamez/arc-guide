---
title: Complexity Reduction
slug: complexity-reduction
category: principles
kind: principle
summary: Complexity reduction means keeping a system as simple as its problem allows. Needless complexity
  makes software harder to understand, change and debug, so architects avoid whatever the problem does
  not require.
arc42:
- 4
- 5
- 8
- 9
step: s07-solution-strategy
related:
- modularity
- separation-of-concerns
- information-hiding
- coupling-and-cohesion
- big-ball-of-mud
- technical-debt
- architecture-principle
- design-for-change
checks:
- The document separates complexity that comes from the problem from complexity the team introduced.
- Speculative features or abstractions that make current requirements harder to understand are absent
  or justified.
- Each module hides one design decision behind a minimal interface.
- The criteria used to divide the system into modules are stated.
sources:
- url: https://www.martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.ufried.com/blog/simplify_3_essential_and_accidental_complexity/
  title: Simplify! - Part 3
  site: ufried.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/No_Silver_Bullet
  title: No Silver Bullet - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/Yagni.html
  title: Yagni
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://blog.acolyer.org/2016/09/05/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/
  title: On the criteria to be used in decomposing systems into modules – the morning paper
  site: blog.acolyer.org
  accessed: '2026-11-09'
- url: https://arc42.org/resources/
  title: Resources - arc42
  site: arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Some complexity cannot be avoided. Other complexity is self-inflicted. Telling the two apart is the first step in reducing it.

**Two kinds of complexity**

- *Essential complexity* comes from the problem itself: its requirements and constraints. A solution cannot be less complex than the problem it solves.
- *Accidental complexity* comes from choices engineers make. Engineers created it, so they can fix it.

Brooks argued that removing all accidental complexity would not give an order-of-magnitude improvement, because essential complexity dominates. So the realistic goal is to avoid adding complexity the problem does not demand.

**Why it matters**

A complex design is harder to understand than a simple one. Unneeded complexity also makes a system harder to change in all directions, not only the one you expected.

**Ways to reduce it**

- *Avoid speculative features.* Features added "just in case" make software harder to modify and debug. This idea is called YAGNI ("you aren't gonna need it"). Many small YAGNI decisions add up to a large reduction in complexity.
- *Question abstractions.* An abstraction that makes today's requirements harder to understand is presumed guilty.
- *Divide the system with care.* How well a split into modules works depends on the criteria used to divide it. See Modularity and Separation of Concerns.
- *Hide design decisions.* Each module hides one design decision behind a minimal interface, so a change stays inside one module. See Information Hiding.
- *Keep coupling low.* Modularity, complexity, KISS ("keep it simple") and coupling are listed together as software engineering basics. See Coupling and Cohesion.

## Example

A team builds an order system. The requirements call for one payment provider. A developer proposes a plug-in framework for many future providers. The team asks whether the framework makes today's requirement harder to understand. It does, so they skip it. They put payment handling behind one small interface in one module. If a second provider is ever needed, the change stays in that module.

## Trade-offs

Simplicity has limits. Essential complexity stays, so a simple-looking design that ignores real requirements fails. Skipping speculative features also means accepting that some future needs will require work later. Judge each abstraction by whether it makes the current requirements easier or harder to understand.
