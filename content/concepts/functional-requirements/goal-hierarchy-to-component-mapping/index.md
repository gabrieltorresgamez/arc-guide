---
title: Goal Hierarchy to Component Mapping
slug: goal-hierarchy-to-component-mapping
category: functional-requirements
kind: method
summary: A use case can carry a goal level, and its scope can range from a whole organization down to
  one component. Matching goals to components of similar size gives each building block a clear responsibility.
arc42:
- 5
- 3
step: s03-functional-requirements
related:
- use-case-goal-levels
- use-case-goal-hierarchy-with-include-relationships
- responsibility-allocation
- coupling-and-cohesion
- layers-and-components-decomposition
- use-case
- method-phase-working-with-functional-requirements
- modularity
checks:
- Use cases are annotated with a goal level so readers know the expected level of detail.
- Every important black box in the building block view has a described responsibility.
- Blocks that group similar business functions are formed with cohesion as the primary driver.
- The scope of each use case (system, sub-system or component) is stated and fits the building block it
  is assigned to.
sources:
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://github.com/socadk/design-practice-repository/blob/master/artifact-templates/DPR-UseCase.md
  title: design-practice-repository/artifact-templates/DPR-UseCase.md at master · socadk/design-practice-repository
    · GitHub
  site: github.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://examples.arc42.org/systems/mama/05-building-block-view/
  title: Building Block View · arc42 Examples
  site: examples.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Goals of different size are assigned to building blocks of matching size.
review:
  status: generated
  flags: []
---

## Explanation

A use case describes how a user reaches a goal with the help of a system. You can label each use case with a goal level. The preferred level is the user goal, informally called sea level.

A use case also has a subject. The subject can be a system, a sub-system or a single component. So the scope of a use case can range from a black-box view of a whole organization down to one component.



The arc42 building block view is a hierarchical collection of black boxes and white boxes. A white box shows the inner parts of a block. The hierarchy starts with the whole system at level 1 and goes deeper from there. Each important black box, which hides its inner parts, should have its responsibility described.

An arc42 practical tip says cohesion should be the primary driver when creating building blocks. See Coupling and Cohesion.

Functional decomposition is one way to shape the top level. One arc42 example bases its level-1 structure on it.

## Example

An online shop has the broad goal "Run the shop". The shop owner has a user goal, "Fulfill an order". That goal needs a smaller step, "Calculate shipping cost".

The architect assigns the broad goal to the system as a whole. The user goal goes to a block that groups order-related functions. The small step goes to a small component inside that block.

## Trade-offs

Grouping by function is only one way to form blocks. an arc42 practical tip names cohesion as the primary driver, so check each functional grouping against it. The arc42 example above bases its structure on both functional decomposition and a generated persistence concept.
