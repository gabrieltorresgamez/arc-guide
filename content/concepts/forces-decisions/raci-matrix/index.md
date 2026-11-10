---
title: RACI Matrix
slug: raci-matrix
category: forces-decisions
kind: artifact
summary: A RACI matrix lists, for each task or decision, who is Responsible, Accountable, Consulted and
  Informed. It shows who does the work, who answers for it, who gives input and who is told.
arc42:
- 9
- 1
step: s09-decisions
related:
- definition-of-ready-for-architectural-decisions
- stakeholder-identification
- architectural-decision-record
- accountability
- stakeholder
- architectural-decision-making-in-project-development
- architectural-decision
checks:
- Each architectural decision names its decision makers, consulted stakeholders and affected people.
- The people involved in a decision are grouped in a RACI matrix.
- Each task or decision has exactly one Accountable party.
- R and A for architectural decisions may be assigned to a role, not only to a named person.
sources:
- url: https://en.wikipedia.org/wiki/Responsibility_assignment_matrix
  title: Responsibility assignment matrix - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A RACI matrix is a table. Rows are tasks or decisions. Columns are people or roles. Each cell holds one of four letters, or stays empty.

**The four letters**

- **Responsible (R):** the people who do the work.
- **Accountable (A):** the one person ultimately answerable for the task being completed correctly. This differs from doing the work. The doers are the Responsible ones.
- **Consulted (C):** people whose opinions are sought, such as subject-matter experts.
- **Informed (I):** people who are kept up to date on progress.

**One accountable per task**

Some project management theories require exactly one Accountable stakeholder for each task or deliverable.

**RACI and architectural decisions**

The Architectural Decision Definition of Ready says a decision should be made only when certain people are known and able to take part. These are the decision makers, the consulted stakeholders and the people affected by the outcome. It suggests grouping them in a RACI matrix.

**Roles, not only individuals**

The architect is a role. It is not necessarily one person.

## Example

A team must choose a messaging product. The matrix has one row: "Select messaging product."

- The architect role is Accountable.
- Two developers are Responsible. They compare the options.
- An operations expert is Consulted, because their opinion is needed.
- The support team is Informed once the choice is made.

## Trade-offs

The one-Accountable rule comes from some project management theories, not from all of them. A matrix shows who takes part. It does not show how the decision is reached.
