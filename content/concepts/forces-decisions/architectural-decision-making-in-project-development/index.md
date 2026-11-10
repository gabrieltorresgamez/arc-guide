---
title: Architectural Decision-Making Process
slug: architectural-decision-making-in-project-development
category: forces-decisions
kind: practice
summary: Architectural decision-making is an ongoing, team-based activity. One decision triggers others,
  so it is never finished at once. Teams compare real alternatives, weigh trade-offs, and revisit their
  choices.
arc42:
- 9
- 4
step: s09-decisions
related:
- architectural-decision
- architectural-decision-record
- decision-dependencies
- last-responsible-moment
- architecturally-significant-decision
- architectural-decision-management-cycle
- definition-of-done-for-architectural-decisions
- architecture-decision-rationale
checks:
- Each recorded decision shows at least two options that were compared.
- Each decision record states the problem and the trade-offs considered.
- Decisions state when they will be reviewed or which context changes trigger re-evaluation.
- Recorded decisions are the ones that are hard and costly to change.
- Follow-up decisions triggered by a decision are identified.
sources:
- url: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
  title: A Definition of Done for Architectural Decision Making
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
  title: Architecture Decision Record
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/scaling-architecture-conversationally.html
  title: Scaling the Practice of Architecture, Conversationally
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/1707.00107
  title: '[1707.00107] An Empirical Study on Collaborative Architecture Decision Making in Software Teams'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Teams do not make all architectural decisions in one session. Making one decision typically triggers further decisions, and decisions that were made age and may need attention later, so decision making is never entirely done.

**Which decisions matter most.** One way to describe architecture is as the set of decisions you would most like to get right early in a project. Teams should focus on the architecturally significant decisions, including those that are hard and costly to change, and not document everything. Cost, effort, and risk guide the prioritization of decisions.

**When to decide.** Teams aim for the most responsible moment. See Last Responsible Moment.

**Comparing options.** One criterion for a decision being done is that the team has compared at least two options, at least semi-systematically, though sometimes there is only one choice. Listing fake alternatives to fill a template has no value. The team weighs the trade-offs between options. The decision record should state the problem and those trade-offs.

**Who decides.** An empirical study found that most teams make architecture decisions collaboratively, and that a consultative style was preferred. In an advice process, anyone may decide but must consult affected people and experts. The goal is broad input, not consensus.

**Uncertainty and revisiting.** Teams decide under uncertainty. They record how confident they are and which context changes should trigger a new look. They also plan when to review and possibly revise a decision.

## Example

A team building an online shop must choose how to store orders. They compare two real options and write down the trade-offs. They pick one and note their confidence and a review date. The choice immediately raises new questions, such as how to back up the data and how other parts of the system read orders. Each of those becomes its own decision.

## Trade-offs

Consulting many people brings broader input, though how many people to consult is a concern that can be mitigated, for example with a checklist of who to speak to.
