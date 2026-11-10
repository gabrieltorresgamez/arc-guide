---
title: Types of Cohesion
slug: types-of-cohesion
category: principles
kind: concept
summary: Cohesion describes how well the parts of a module belong together. Seven types exist, from functional
  (strongest) to coincidental (weakest). Each type names the reason the parts were grouped.
arc42:
- 5
- 8
step: s10-document
related:
- coupling-and-cohesion
- high-cohesion
- increase-cohesion
- module
- loose-coupling
- reduce-coupling
- modularity
- split-module
checks:
- For each module, the document states why its parts are grouped (for example one task, same data, or
  same time).
- No module groups its parts arbitrarily, such as a catch-all utility module.
- Classes with more than one connected group of methods (LCOM4 above one) are reviewed for splitting.
sources:
- url: https://en.wikipedia.org/wiki/Cohesion_(computer_science)
  title: Cohesion (computer science) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.aivosto.com/project/help/pm-oo-cohesion.html
  title: Project Metrics Help - Cohesion metrics
  site: aivosto.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The seven types of cohesion, from strongest to weakest.
review:
  status: generated
  flags: []
---

## Explanation

Cohesion is the degree to which the elements inside a module belong together. A module is a unit of code that groups related parts (see the article Module). The types of cohesion describe *why* the parts were put together. They run from strongest to weakest.

1. **Functional (strongest).** Every part contributes to one well-defined task of the module.
2. **Sequential.** The output of one part is the input of the next part.
3. **Communicational.** The parts operate on the same data.
4. **Procedural.** The parts always follow a certain order of execution.
5. **Temporal.** The parts are grouped by the time at which they are processed.
6. **Logical.** The parts are grouped because they are categorized as doing the same kind of thing.
7. **Coincidental (weakest).** The parts are grouped arbitrarily.

The list works as a ruler. Ask why a module's parts sit together, then find the matching type. A reason near the top means a tighter module. A reason near the bottom is a warning sign.

Cohesion is often contrasted with coupling. High cohesion often goes with loose coupling, and the reverse also holds. See Coupling and Cohesion and High Cohesion.

A code metric can support the judgment. LCOM4 counts the connected groups of methods in a class. A cohesive class should have exactly one group. A higher count suggests the class holds parts that do not belong together.

## Example

An invented online shop has a module called `Helpers`. It holds a price formatter, an email sender and a date parser. Nobody can say why they sit together. This is coincidental cohesion.

Now take a module called `InvoiceCalculation`. It sums line items, adds tax and applies a discount. All parts serve one task: computing an invoice total. This is functional cohesion.

Moving the email sender into its own module, and keeping the invoice parts together, turns a weak grouping into stronger ones.

## Trade-offs

The seven types are a guide, not a score. They tell you the reason for a grouping, not whether the design is good overall. Cohesion is also only one side of the picture. Coupling matters too, although the two often move together.
