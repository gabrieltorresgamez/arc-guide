---
title: Coupling and Cohesion
slug: coupling-and-cohesion
category: principles
kind: principle
summary: Coupling describes how strongly modules depend on each other. Cohesion describes how well the
  parts inside one module belong together. Low coupling often goes with high cohesion.
arc42:
- 5
- 8
step: s07-solution-strategy
related:
- loose-coupling
- high-cohesion
- types-of-cohesion
- reduce-coupling
- increase-cohesion
- modifiability-tactics
- module
- information-hiding
checks:
- Modules are described by one well-defined task each, rather than grouped arbitrarily.
- Where modules depend on each other, the document shows how strong that coupling is (loose or tight).
sources:
- url: https://en.wikipedia.org/wiki/Coupling_(computer_programming)
  title: Coupling (computer programming) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Cohesion_(computer_science)
  title: Cohesion (computer science) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Coupling and cohesion are two ways to judge how a system is split into parts. The ideas come from structured design, published by Stevens, Myers and Constantine in 1974. A module is one such part (see the article *Module*).

**Coupling** is about the links *between* modules. It can be low (also called loose or weak) or high (also called tight or strong). See *Loose Coupling* and *Reduce Coupling*.

**Cohesion** is about the inside of one module. It is the degree to which the elements in a module belong together. See *High Cohesion* and *Increase Cohesion*.

The two ideas often move together. Low coupling often goes with high cohesion, and the reverse also holds.

**Levels of cohesion.** Cohesion comes in types, from weak to strong:

- **Coincidental:** the weakest. Parts are grouped arbitrarily.
- **Sequential:** parts are grouped because the output of one is the input of the next.
- **Functional:** the best. All parts contribute to one well-defined task.

The article *Types of Cohesion* covers the range.

**Link to modifiability.** The SEI report on modifiability tactics bases its tactics on coupling, cohesion and cost motivations. It also ties the tactics to the parameters of quality attribute models. See *Modifiability Tactic*.

## Example

A shop system has a module called "Utilities". It holds price rounding, email sending and image resizing. These parts have nothing in common, so its cohesion is coincidental. A second module, "Invoice Calculation", only computes invoice totals. Every part serves one task, so its cohesion is functional. The second module is easier to describe and to find your way around in.
