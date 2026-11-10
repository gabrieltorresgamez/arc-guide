---
title: High Cohesion
slug: high-cohesion
category: principles
kind: principle
summary: High cohesion means the parts of a module belong together and serve one focused responsibility.
  A change to that responsibility then stays inside one module. It works best together with low coupling.
arc42:
- 5
- 8
- 4
step: s07-solution-strategy
related:
- coupling-and-cohesion
- types-of-cohesion
- increase-cohesion
- loose-coupling
- modifiability
- split-module
- module
- separation-of-concerns
checks:
- Each building block has a responsibility that can be stated in one sentence without 'and'.
- The same rules for what belongs together are applied consistently across the system.
- Splits of modules are checked so they do not create anemic modules with heavy coupling between them.
- Cohesion is described as high or low, not claimed as an exact number, and any LCOM value is read with
  its limits in mind.
sources:
- url: https://quality.arc42.org/approaches/increase-cohesion
  title: Increase Cohesion | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Cohesion_(computer_science)
  title: Cohesion (computer science) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/tips/5-17/
  title: 'Tip 5-17: ‘Cohesion’ shall be the primary driver when creating architecture building blocks!
    | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/cohesion
  title: Cohesion | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Cohesion describes how closely the parts of a module belong together. A highly cohesive module is single-minded: it has one responsibility. The idea applies to any building block of an architecture, such as a component, module, subsystem or package. It is a fundamental, classical design principle.

**Why it helps change.** If a responsibility sits in a single place, changing it affects one module and not several. Raising cohesion therefore localizes change and supports modifiability (see the article Modifiability).

**Cohesion and coupling.** Coupling is the dependency between modules. The two ideas are complementary levers: raise cohesion inside modules and lower coupling between them. High cohesion often goes with loose coupling, and the reverse also holds (see Loose Coupling and Coupling and Cohesion).

**How to judge it.** Cohesion is an ordinal measure. People call it "high" or "low" and do not measure it exactly. Two aids help:

- A one-sentence test. Describe the module's responsibility in one sentence without using "and". If that is hard, cohesion may be low.
- LCOM, a metric based on which methods use which fields inside a class. It captures only those links, so read it with care.

**Context matters.** What belongs together depends on the viewpoint and on the stakeholder. Different people may group things differently. Apply consistent rules for cohesion across the whole system.

Cohesion types can be ranked, but the ranks are ordinal. A higher rank does not mean steady improvement from one type to the next (see Types of Cohesion).

## Example

A shop system has one module for prices, discounts and tax rules. A second module handles shipping labels and carrier choice. Each module can be described in one sentence without "and" joining unrelated topics. When tax rules change, the team edits only the first module. Now imagine a single module that mixes tax rules with shipping labels. Its description needs "and", and a tax change risks touching shipping code too.

## Trade-offs

Do not push cohesion too far. Over-splitting a cohesive module creates anemic modules that do too little. The coupling between them can then exceed the cohesion gained. Cohesion must also be balanced against coupling and against the complexity of each unit. Because the judgment depends on viewpoint and stakeholder, there is no single exact answer.
