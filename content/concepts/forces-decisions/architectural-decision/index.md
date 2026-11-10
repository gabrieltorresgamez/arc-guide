---
title: Architectural Decision
slug: architectural-decision
category: forces-decisions
kind: concept
summary: An architectural decision is a choice of one option from several, made against stated criteria.
  Writing down the reasons lets others understand and retrace the choice later.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- architecture-decision-rationale
- arc42-architecture-decisions
- architecturally-significant-decision
- architecture-as-set-of-design-decisions
- architectural-forces
- decision-dependencies
- levels-of-architectural-decisions
checks:
- Each decision states the alternatives considered and the criteria used to choose among them.
- Each decision records its rationale, answering why this option was chosen.
- The context of each decision covers technical, political, social, and project aspects.
- All consequences are listed, including negative ones.
- Stakeholders can comprehend and retrace the decisions.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architectural decision means selecting one alternative from several, based on given criteria.

**Record the why.** Answers to "why?" questions about a design are as important as any other part of that design. Important decisions should be documented together with their reasons.

**Describe the situation.** The context of a decision includes technical, political, social, and project aspects. These forces can pull in different directions. A good record names them, so a reader sees what the team was balancing.

**List all consequences.** A record should not only list the benefits. Every consequence belongs in it, including the unwelcome ones.

**Make it retraceable.** Stakeholders (people with an interest in the system) should be able to understand and retrace the decisions.

For the record format, see the articles Architectural Decision Record and Architecture Decision Rationale.

## Example

A team must pick how two systems exchange data. They consider a shared database and messaging. Their criteria are ease of change and team skills. The project is under time pressure, and one department prefers the database. The team picks messaging. The record names both options, the criteria, and these pressures. It also lists the downsides, such as extra operating effort. A new colleague reads it a year later and sees why the team chose as it did.

## Trade-offs

Documentation takes maintenance effort, so only the key decisions justify it. A record that lists only the positive consequences is incomplete, since all consequences should be listed.
