---
title: Fitness for Purpose
slug: fitness-for-purpose
category: evaluation
kind: principle
summary: An architecture is rarely good or bad on its own. It is fit or unfit for a purpose, and that
  purpose comes mostly from the context where the system will live.
arc42:
- 1
- 4
- 9
- 10
step: s11-evaluate
related:
- software-architecture-evaluation
- architectural-style
- quality-attribute
- architectural-trade-off-thinking
- big-ball-of-mud
- quality-attribute-prioritization
- software-architecture-in-its-context
- arc42-solution-strategy
checks:
- The document names the business drivers and prioritized quality requirements that the chosen architecture
  style is meant to serve.
- The document explains why the style was chosen and what trade-offs it accepts.
- The document judges the style's benefits against its challenges for the specific context.
- The document describes how the fit will be measured and validated over time.
sources:
- url: https://martinfowler.com/articles/architect-elevator.html
  title: The Architect Elevator — Visiting the upper floors
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
  title: Architecture Styles - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Architecture is rarely good or bad in absolute terms. It is either fit or unfit for its purpose. So "Is this a good architecture?" is an incomplete question. Ask instead: "Fit for what?"

**Where the purpose comes from**

The purpose depends mainly on the context in which the system will live, rather than on specific user requirements.

Guidance on choosing an architecture style (see Architecture Style) says to start from the problem. Then name the key business drivers and the matching quality needs, also called nonfunctional requirements (see Quality Attribute). Finally, rank them by priority.

Different priorities point to different choices:

- If time to market is the driver, favor maintainability, testability and reliability.
- If the budget is tight, favor simplicity.

**Trade-offs and context**

Every style has trade-offs. You should understand why a style was chosen. Sometimes relaxing one of its constraints is better than keeping the style pure.

Whether a style's benefits outweigh its challenges must be judged for the specific context. The complexity of the architecture must also match the domain. If it is too simple for the domain, the result can become a Big Ball of Mud.

**Fitness changes over time**

Choosing a style is not a one-time task. It needs ongoing measurement, validation and refinement. Changing the style later is costly, so early checks pay off.

## Example

A team builds an internal tool that must reach users within weeks. Its stated drivers are time to market and a small budget. The team ranks maintainability, testability and simplicity first. It picks a simple structure and records why.

A different team builds a system for a complex domain. For that team, the same simple structure may be too simple. Its benefits and challenges must be weighed again for that context.

## Trade-offs

Relaxing a style's constraint can serve the purpose better than purity, but the team must understand why it does so. Ongoing measurement and validation take effort, yet changing style late is costly.
