---
title: Technical Debt
slug: technical-debt
category: evaluation
kind: concept
summary: Technical debt means shortcuts in design or code that help in the short term but make later change
  more costly. A little deliberate debt can speed work if the team repays it promptly.
arc42:
- 11
step: s12-evolve
related:
- refactoring
- risk-storming
- architecture-decay
- maintainability
- code-smell
- big-ball-of-mud
- software-architecture
- modifiability
checks:
- Known technical debts are listed in the risks and technical debts section, ordered by priority.
- Each deliberate debt is marked as knowingly accepted, with a plan to repay it (for example by refactoring).
- Debt in architecture and design is covered, not only code-level debt.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3128836&seqNum=4
  title: Technical Debt | Why Software Architecture is Important and Essential Activities | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/TechnicalDebt.html
  title: Technical Debt
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
  title: Technical Debt Quadrant
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/ATDM
  title: About the Automated Technical Debt Measure Specification Version 1.0
  site: omg.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-11/
  title: 11 - Risks and technical debt | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://sei.cmu.edu/blog/10-years-of-research-in-technical-debt-and-an-agenda-for-the-future/
  title: 10 Years of Research in Technical Debt and an Agenda for the Future | CMU Software Engineering
    Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/blog/enabling-agility-by-strategically-managing-architectural-technical-debt/
  title: Enabling Agility by Strategically Managing Architectural Technical Debt | CMU Software Engineering
    Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A shortcut gives speed now and creates interest that grows until the debt is repaid.
review:
  status: generated
  flags: []
---

## Explanation

Technical debt is a metaphor. A team takes a shortcut, finishes sooner, and pays for it later. Fowler credits Ward Cunningham with introducing the metaphor in 1992.

Kruchten, Nord and Ozkaya define technical debt as design or implementation constructs that are expedient in the short term. "Expedient" means quick and convenient now.

**Interest.** In the metaphor, the extra effort needed to add new features is the interest paid on the debt. The more debt a system carries, the slower future change becomes.

**Where debt lives.** Debt is not only a code problem. SEI researchers hold that it is rooted in architecture and design issues. See Software Architecture for what architecture means.

**Measuring it.** Tools can measure some debt. The OMG Automated Technical Debt Measure standardizes a measure that source-code analysis tools can compute from quality characteristic measures. Architecture debt is hard to measure with tools.

**Prudent or reckless.** Fowler argues the useful question is not whether something is debt. It is whether the debt is prudent or reckless. Deliberate debt can be prudent when the team knowingly accepts it.

**Repayment.** In Cunningham's view, a little debt speeds development, but only if the team pays it back promptly. SEI describes repayment through refactoring or rewriting. The Refactoring article explains refactoring.

**Documenting it.** arc42 section 11 holds the identified technical risks and technical debts, ordered by priority.

## Example

A team must release a booking feature before a trade fair. It copies an existing payment module instead of building a shared one. The team writes this down as a known debt in the risks and debts section and plans to merge the two modules after the fair. Because the team chose this knowingly and recorded it, the debt is deliberate and tracked.

## Trade-offs

Deliberate debt buys speed now. The price is extra effort whenever the indebted area has to be changed, and the benefit holds only if the team repays the debt promptly. Teams that accept debt knowingly (prudent) are in a different position from teams that take it recklessly. Architecture debt has deep roots but is hard to measure with tools, so tool numbers alone give an incomplete picture.
