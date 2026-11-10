---
title: Main Sequence (Balance of Abstractness and Instability)
slug: main-sequence
category: principles
kind: concept
summary: The main sequence is an ideal line on a chart that plots how abstract a software component is
  against how unstable it is. Components are judged by their distance from that line.
arc42:
- 5
- 10
- 11
step: s12-evolve
related:
- coupling-and-cohesion
- component-design-principles
- architecture-decay
- technical-debt
- loose-coupling
- modularity
checks:
- The document states how instability and abstractness are computed for each component, using the same
  definitions throughout.
- Components with a high distance from the main sequence are listed, with a stated threshold such as 0.7.
- Components in the zone of pain (low I and low A) are named, and their position is explained or accepted.
- Interfaces added to improve the score have a real purpose and are not empty additions that game the
  metric.
sources:
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
diagrams:
- file: diagram-1.mmd
  caption: 'The A-I chart: the main sequence runs from the abstract-and-stable corner to the concrete-and-unstable
    corner. Low-low is the zone of pain, high-high the zone of uselessness.'
review:
  status: generated
  flags: []
---

## Explanation

The main sequence rates a software component, such as a package or assembly, with two numbers.

**Instability (I)** compares the outgoing dependencies of a component (efferent coupling, Ce) with its total dependencies. The formula is I = Ce / (Ce + Ca), where Ca counts the incoming dependencies. I = 0 means fully stable. I = 1 means fully unstable.

**Abstractness (A)** is the share of abstract types, meaning abstract classes and interfaces, among the internal types of the component. A = 0 means fully concrete. A = 1 means fully abstract.

Plot I on one axis and A on the other. The ideal components lie on the line A + I = 1. This line is called the main sequence. It balances abstraction and instability.

**Distance from the line.** Tools measure how far a component sits from the line. NDepend uses the perpendicular, normalized distance. A value of 0 means the component is on the line. A value of 1 means as far as possible. NDepend suggests that values above 0.7 might be problematic.

**Two problem zones.**
- *Zone of pain:* both I and A are near 0. These are stable components that are not abstract. The idea behind this zone is that the more stable a package is, the more abstract it should be.
- *Zone of uselessness:* both I and A are near 1.

The ideal corners are fully abstract and stable (I=0, A=1), or fully concrete and unstable (I=1, A=0).

For related ideas, see the articles Coupling and Cohesion and Component Design Principles.

## Example

A team plots its components on the chart. One component, "Reports", has low I and low A, so it sits in the lower-left corner, the zone of pain. A second component has high I and high A, so it sits in the upper-right corner, the zone of uselessness. The team looks first at the components with the largest distance from the line.

## Trade-offs

The metric is a guide, not a verdict. Some components in the red zone may be fine.

Counting abstract and concrete types can mislead. One critique says the metric equates abstractness with real abstraction. It can push people to add interfaces only to satisfy the score. Adding empty interfaces games the metric and misses the point.

The logic does hold in some cases. In a collection library, clients depend on an interface such as List, and adding a new implementation is easy.

Reaching the zone of pain takes both low abstractness and high stability. A component that scores high on one and very low on the other need not be there.
