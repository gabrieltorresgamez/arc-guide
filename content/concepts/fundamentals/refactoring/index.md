---
title: Refactoring
slug: refactoring
category: fundamentals
kind: practice
summary: Refactoring changes the inside of software in small steps without changing what it does. It keeps
  the design easy to change and slows the decay that sets in when teams skip it.
arc42:
- 4
- 8
- 11
step: s12-evolve
related:
- code-smell
- technical-debt
- big-ball-of-mud
- architecture-decay
- maintainability
- testability
- design-for-change
- keep-it-working
checks:
- The document states that refactoring must not change observable behavior.
- Tests exist that protect refactoring work as a safety net.
- Refactoring is done continuously to prevent design decay.
- Known design weaknesses are tracked as technical debt and paid down gradually.
sources:
- url: https://martinfowler.com/bliki/DefinitionOfRefactoring.html
  title: Definition Of Refactoring
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/books/refactoring.html
  title: Refactoring
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/CodeSmell.html
  title: Code Smell
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/TechnicalDebt.html
  title: Technical Debt
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'The refactoring loop: small steps, each checked by tests.'
review:
  status: generated
  flags: []
---

## Explanation

Refactoring is a change to the internal structure of software. The goal is to make the software easier to understand and cheaper to modify. Observable behavior stays the same. Users notice nothing, while developers find the code easier to work with.

**Small steps.** A refactoring is usually one of a series of small changes, not a big rewrite. Small steps reduce the risk of introducing errors. The website of the book *Refactoring* offers a catalog that summarizes every refactoring in the book, so teams can follow known recipes.

**Where to start.** A code smell is a surface sign of a deeper problem in the system. Smells guide developers to where refactoring is worth the effort. See the article Code Smell.

**Safety net.** Testing protects refactoring. In Extreme Programming (XP), testing is the safety net that the other practices depend on, refactoring included. Continuous integration, which keeps the team in sync, also supports this style of evolving design.

**Design done later.** When change gets cheaper, a team can do more of its design later, as refactoring, instead of all upfront.

**Why it matters.** Without refactoring, design decays over time. As the design gets worse, so does the ability to change the software. The way to arrest that entropy is to refactor. A sustained commitment to it can keep a system from sinking into a Big Ball of Mud (see the article Big Ball of Mud).

**Link to technical debt.** Technical debt works like a financial debt. The extra effort for each new feature is the interest. The usual advice is to pay the principal down gradually. See the article Technical Debt.

## Example

A team keeps adding special cases to a price calculation. Each new case is harder to add than the last. Before the next feature, the team runs its tests and then makes small changes. They rename unclear variables, split one long routine into smaller ones, and remove duplicated rules. After each step they run the tests again. Prices come out the same as before. The next feature is now easier to add.

## Trade-offs

Refactoring takes time but does not add function. Cleaning up cruft can also cost extra days, and if it is done for only one feature it is no gain. There is one dependency too: refactoring relies on testing as its safety net. Skipping refactoring has a price as well. Design decays and change gets harder.
