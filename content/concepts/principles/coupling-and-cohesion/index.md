---
title: Coupling and Cohesion
slug: coupling-and-cohesion
order: 20
category: principles
kind: principle
summary: Coupling describes how strongly modules depend on each other. Cohesion describes how well the
  parts inside one module belong together. Low coupling often goes with high cohesion.
arc42:
- 5
- 8
step: s07-solution-strategy
related:
- maintainability-tactic
- ddd-building-blocks-tactical-patterns
- information-hiding
- component-design-principles
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
- url: https://quality.arc42.org/approaches/increase-cohesion
  title: Increase Cohesion | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-17/
  title: 'Tip 5-17: ‘Cohesion’ shall be the primary driver when creating architecture building blocks!
  | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/cohesion
  title: Cohesion | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/ramblings/coupling_facets.html
  title: The Many Facets of Coupling - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/ramblings/eventdriven_coupling.html
  title: Event-driven = Loosely coupled? Not so fast! - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Loose_coupling
  title: Loose coupling - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.aivosto.com/project/help/pm-oo-cohesion.html
  title: Project Metrics Help - Cohesion metrics
  site: aivosto.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/reduce-coupling
  title: Reduce Coupling | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://connascence.io/
  title: connascence.io
  site: connascence.io
  accessed: '2026-11-09'
- url: https://www.ndepend.com/docs/code-metrics
  title: 'Code Metrics for C# and .NET: 100+ Definitions'
  site: ndepend.com
  accessed: '2026-11-09'
- url: https://pdepend.org/documentation/handbook/reports/abstraction-instability-chart.html
  title: 'PHP Depend - Software Metrics for PHP: News'
  site: pdepend.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Software_package_metrics
  title: Software package metrics - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://odrotbohm.github.io/2024/09/the-instability-abstractness-relationsship-an-alternative-view/
  title: Oliver Drotbohm - The Instability-Abstractness-Relationship — An Alternative View
  site: odrotbohm.github.io
  accessed: '2026-11-09'
- url: https://daedtech.com/entering-zone-pain/
  title: Entering the Zone of Pain - DaedTech
  site: daedtech.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/loose-coupling
  title: "Loose Coupling | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Coupling and cohesion are two ways to judge how a system is split into parts. The ideas come from structured design, published by Stevens, Myers and Constantine in 1974 [src:1]. A module is one such part.

**Coupling** is about the links *between* modules. It can be low (also called loose or weak) or high (also called tight or strong). See *Loose Coupling*.

**Cohesion** is about the inside of one module. It is the degree to which the elements in a module belong together. See *High Cohesion*.

The two ideas often move together. Low coupling often goes with high cohesion, and the reverse also holds.

**Levels of cohesion.** Cohesion comes in types, from weak to strong:

- **Coincidental:** the weakest. Parts are grouped arbitrarily.
- **Sequential:** parts are grouped because the output of one is the input of the next.
- **Functional:** the best. All parts contribute to one well-defined task.

The article *Types of Cohesion* covers the range.

**Link to modifiability.** The SEI report on modifiability tactics bases its tactics on coupling, cohesion and cost motivations. It also ties the tactics to the parameters of quality attribute models. See *Maintainability Tactic*.

**More about coupling and cohesion.**

- **High Cohesion:** High cohesion means the parts of a module belong together and serve one focused responsibility. A change to that responsibility then stays inside one module. It works best together with low coupling.
- **Loose Coupling:** Loose coupling means building blocks depend on each other as little as possible, so a change in one rarely forces a change in another. The right level depends on how much control you have over both sides.
- **Types of Cohesion:** Cohesion describes how well the parts of a module belong together [src:2]. Seven types exist, from functional (strongest) to coincidental (weakest). Each type names the reason the parts were grouped.
- **Connect or Disconnect:** Connecting components creates dependencies between them. Good design keeps few, narrow, explicit dependencies, and the right amount depends on how much control you have.
- **Main Sequence (Balance of Abstractness and Instability):** The main sequence is an ideal line on a chart that plots how abstract a software component is against how unstable it is. Components are judged by their distance from that line.

**In the arc42 quality model.** It has quality pages on [Loose Coupling](https://quality.arc42.org/qualities/loose-coupling) and [Cohesion](https://quality.arc42.org/qualities/cohesion), and approach pages on [Reduce Coupling](https://quality.arc42.org/approaches/reduce-coupling) and [Increase Cohesion](https://quality.arc42.org/approaches/increase-cohesion).

## Example

A shop system has a module called "Utilities". It holds price rounding, email sending and image resizing. These parts have nothing in common, so its cohesion is coincidental. A second module, "Invoice Calculation", only computes invoice totals. Every part serves one task, so its cohesion is functional. The second module is easier to describe and to find your way around in.
