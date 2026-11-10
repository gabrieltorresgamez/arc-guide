---
title: Split Module
slug: split-module
category: tactics
kind: tactic
summary: Split Module breaks a module that mixes unrelated responsibilities into smaller modules, so each
  part changes for its own reason. The split must follow expected change, and it adds interfaces, so weigh
  it against joining.
arc42:
- 4
- 5
- 9
step: s07-solution-strategy
related:
- modifiability-tactics
- coupling-and-cohesion
- increase-cohesion
- high-cohesion
- information-hiding
- module
- separation-of-concerns
- modifiability
checks:
- Each module split is justified by responsibilities that change for different reasons.
- Cohesive code that changes as one unit has not been split.
- The decision to split or join is based on overall complexity, not size.
- The added interfaces from a split are acknowledged.
sources:
- url: https://quality.arc42.org/approaches/increase-cohesion
  title: Increase Cohesion | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://yingang.github.io/aposd-zh/en/ch09.html
  title: Chapter 9 Better Together Or Better Apart? | A Philosophy of Software Design, 1st Edition
  site: yingang.github.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A module is a unit of code with a defined job. Some modules carry several jobs that change for different reasons. Such a module is pulled in several directions at once. A change to one job risks the others.

Split Module addresses this. You break the module into smaller modules, so each one has a single reason to change. A change then touches only the part it concerns. (The article Coupling and Cohesion explains these terms.)

**When to split**

Split when a module's responsibilities change for different reasons. The deciding question is what changes, and why. Do not split just to make pieces smaller.

Code that is already cohesive and changes as one unit gains nothing from a split. The split only adds boundaries. So the split must follow change.

**How to judge the split**

The decision to split or join should be based on overall complexity. Choose the structure with the best information hiding, the fewest dependencies, and the deepest interfaces.

Signs that pieces belong together:

- They are closely related.
- They share information, for example both depend on the syntax of one document type.
- They are used together, but only if the relationship runs both ways.

Unrelated pieces are better apart.

## Example

A "Reports" module both formats invoices and calculates tax. Tax rules change each year. Invoice layout changes when the brand changes. The two jobs change for different reasons.

The team splits it into "Tax Calculation" and "Invoice Layout". A new tax rule now touches only the first module.

Suppose both parts also had to read the same document format. That shared information would be a reason to keep them together.

## Trade-offs

Subdividing usually creates more components and more interfaces, and every new interface adds complexity. Splitting code that is already cohesive and changes as one unit only adds boundaries. Joining closely related pieces can lower complexity. So compare the complexity of both structures before you decide.
