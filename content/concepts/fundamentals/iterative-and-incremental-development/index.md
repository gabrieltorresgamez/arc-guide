---
title: Iterative and Incremental Development
slug: iterative-and-incremental-development
category: fundamentals
kind: practice
summary: Iterative and incremental development builds a system in complete pieces and refines it over
  repeated cycles. Teams deliver value early, get feedback, and adapt. Continual refactoring keeps the
  growing system orderly.
arc42:
- 4
- 11
step: s12-evolve
related:
- incrementality
- refactoring
- big-ball-of-mud
- agile-architecture
- evolutionary-domain-modeling
- technical-debt
- design-for-change
- architecture-decay
checks:
- The document or team process describes delivering features as complete pieces and gathering feedback
  after each one.
- Refactoring and consolidation are planned as ongoing work, not left for later.
- The team relies on self-testing code so refactoring stays safe and the code stays malleable.
sources:
- url: https://www.mountaingoatsoftware.com/agile/agile-needs-to-be-both-iterative-and-incremental
  title: 'Iterative vs. Incremental Development: Why Agile Teams Need Both - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.laputan.org/mud/mud.html
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/Yagni.html
  title: Yagni
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each cycle delivers a complete piece, gathers feedback, and consolidates before the next.
review:
  status: generated
  flags: []
---

## Explanation

Incremental development builds and delivers a product in complete pieces. The team finishes one piece before moving to the next. The sculpting analogy shows this: an incremental sculptor picks one element of the sculpture and works on it until it is finished.

Combining iterative and incremental work lets teams deliver value early, get feedback, and adapt. The feedback arrives while the work is still going on, not at the end.

**Keeping order while growing**

Growth without care can erode a system into a Big Ball of Mud (see the article of that name). A sustained commitment to refactoring can keep a system from becoming mud.

**YAGNI and evolutionary design**

YAGNI is the rule of not building what you do not need yet. Evolutionary design lets the design grow with the system. The two enable each other. Refactoring does not violate YAGNI, because it keeps the code malleable. Self-testing code is one practice that makes this work.

## Example

A team builds an online booking tool. In the first cycle, it delivers one complete, tested feature: search and book. Customers try it and ask for an easier date picker. The next cycle improves the date picker and adds a second complete feature, cancel booking. Between cycles, the team cleans up the code so the new feature fits the existing structure instead of being bolted on.

## Trade-offs

Growing in small steps gives early feedback, but it needs discipline. Without a sustained commitment to refactoring, the system can erode into a Big Ball of Mud. Refactoring does not violate YAGNI, because it keeps the code malleable.
