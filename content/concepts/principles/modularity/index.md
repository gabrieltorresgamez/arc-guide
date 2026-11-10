---
title: Modularity
slug: modularity
category: principles
kind: principle
summary: Modularity means dividing a system into self-contained building blocks. The quality of the split
  depends on the criteria used to divide the system, so modularity is a design issue.
arc42:
- 5
- 4
- 8
step: s07-solution-strategy
related:
- module
- information-hiding
- high-cohesion
- coupling-and-cohesion
- separation-of-concerns
- big-ball-of-mud
- architecture-decay
- bounded-context
checks:
- Building blocks are formed mainly by cohesion.
- Building blocks map to the modularization constructs of the programming language.
- Module interfaces reveal as little as possible about their inner workings.
- The criteria used to divide the system into modules are stated.
sources:
- url: https://blog.acolyer.org/2016/09/05/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/
  title: On the criteria to be used in decomposing systems into modules – the morning paper
  site: blog.acolyer.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A module is a building block of a system. Modularity is the practice of dividing a system into such blocks. The arc42 building block view shows this static decomposition. See the article Module for the definition.

**The criteria matter.** How effective a split is depends on the criteria used to divide the system.

**Start from decisions likely to change.** One proposed approach is to begin with a list of difficult design decisions, or decisions likely to change. This replaces starting from a flowchart of processing steps.

**Hide the inner workings.** A module's interface should reveal as little as possible about what happens inside. This idea is called information hiding. See the article Information Hiding.

**Cohesion first.** arc42 advises that cohesion should be the main driver when forming building blocks. See High Cohesion.

**Use your language's constructs.** arc42 also advises mapping building blocks to the modularization constructs of your programming language.

**Structure erodes.** A Big Ball of Mud is a system with a casual, haphazard structure, organized by expediency rather than design. Even systems with well-defined architectures are prone to structural erosion. Left unchecked, the structure can degrade until the system must be abandoned. See Big Ball of Mud and Architecture Decay.

**Domain-oriented splits.** Domain-Driven Design divides a large system into Bounded Contexts. Each context can have a unified model. This is a domain-oriented way to decompose a system. See Bounded Context.

## Example

A shop system lists the decisions most likely to change: how prices are calculated and how payments are made. The team gives each decision its own module. Each module offers a small interface and keeps its inner workings private. When the pricing rules change, the change is more likely to be confined to the pricing module.

## Trade-offs

The criteria you pick decide the result, and a poor choice gives a poor split. Structure also erodes over time, even in well-designed systems, so the split needs ongoing attention.
