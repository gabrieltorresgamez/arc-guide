---
title: Insufficient Quality as Driver of Change
slug: insufficient-quality-as-driver-of-change
category: quality-attributes
kind: concept
summary: Quality goals shape a system as much as features do. Changing one quality goal can force a different
  solution, so architects should state quality goals concretely and early.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- acceptance-criteria
- arc42-quality-chapter
- quality-attribute
- technical-debt
- architecture-decay
- modifiability
- quality-attribute-prioritization
checks:
- Quality goals are stated concretely, without buzzwords.
- Quality requirements are written as quality scenarios that can serve as acceptance criteria.
- Change scenarios describe the desired effect of modifying or extending the system or its environment.
sources:
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.innoq.com/en/blog/2021/08/quality-driven-software-architecture-revised/
  title: Quality Driven Software Architecture - Revised — Getting your product quality right – INNOQ
  site: innoq.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Many projects put functionality, meaning what the system does, at the center of attention. Quality is different. It describes how well the system does its work, and it is the architect's core concern.

Quality does not come for free. Clean code alone does not make a system fast, secure, reliable or maintainable. Each of these needs systematic design.

Quality can also drive the whole solution. Adjusting a single quality attribute, with no new functionality, can force a completely different solution approach. A small change in a requirement can therefore have a large effect on the design.

For this reason, quality requirements need the same care as features. Three practices from arc42 help:

- **Concrete quality goals.** State them in specific terms and avoid buzzwords.
- **Quality scenarios.** A scenario makes a quality requirement concrete. It lets you decide whether the requirement is fulfilled, so it works like an acceptance criterion. See *Quality Attribute Scenario* and *Acceptance Criterion*.
- **Change scenarios.** These describe the desired effect of modifying or extending the system or its environment. They make changeability something you can measure.

## Example

A team writes "the shop must be fast" as a quality goal. Nobody can check that. They rewrite it as a scenario: "On a normal day, a customer opens a product page and sees it within two seconds." Now the team can test it. They also see that this goal may call for a different design than they first planned.

They add a change scenario too: "A developer adds a new payment method, and the change stays within one part of the system." Now changeability is something they can check.

## Trade-offs

The source describes the payoff of investing in quality goals as long term. Teams that look only at near-term features may not see that benefit early on.
