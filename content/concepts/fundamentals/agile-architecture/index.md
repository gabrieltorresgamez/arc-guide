---
title: Agile Architecture
slug: agile-architecture
category: fundamentals
kind: practice
summary: Agile architecture means doing just enough architecture, guided by the biggest risks, and revisiting
  it as the product changes. It avoids both big upfront design and no design at all.
arc42:
- 4
- 9
- 11
step: s12-evolve
related:
- risk-storming
- technical-debt
- architectural-thinking
- continuous-architecture-principles
- last-responsible-moment
- iterative-and-incremental-development
- architecture-viewpoint
- architecture-decay
checks:
- The document names the main project risks and ties architecture effort to them.
- Models or viewpoints are chosen to answer stated questions, such as a throughput model for a throughput
  concern.
- The document shows some deliberate design effort rather than only ad-hoc tactical decisions.
- The architectural runway or intentions are kept current as the product changes.
- The design describes a broad starting-point architecture, not a complete upfront design.
sources:
- url: https://framework.scaledagile.com/agile-architecture/
  title: Extended Guidance - Agile Architecture in SAFe - Scaled Agile Framework
  site: framework.scaledagile.com
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.methodsandtools.com/archive/agilearchi.html
  title: ''
  site: methodsandtools.com
  accessed: '2026-11-09'
- url: https://continuous-architecture.pages.dev/practices/architecture-runway/
  title: Architecture Runway – Aligning Intentional and Emerging Design
  site: continuous-architecture.pages.dev
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/fairbanks-jesa/
  title: 'Interview and Book Excerpt: George Fairbanks’ Just Enough Software Architecture - InfoQ'
  site: infoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A risk-driven cycle of just enough architecture
review:
  status: generated
  flags: []
---

## Explanation

Agile teams build in small steps. Architecture work has to fit that pace. Two extremes are best avoided: designing everything up front, and not designing at all.

**Why no design fails.** Evolutionary design means letting the design emerge as code grows. Fowler argues it fails without design effort. The design turns into a pile of ad-hoc, short-term decisions. He names a lack of will to design as a major cause of failure. He also links decaying design to a shrinking ability to change software effectively. Fairbanks says skipping design is impractical when the risk of failure is high.

**Why full upfront design is not the answer.** Fowler sees a role for a broad starting-point architecture. SAFe cites Coplien: design will partly emerge, yet a little planning avoids much waste.

**Just enough, driven by risk.** Fairbanks' risk-driven model ties architecture effort to the risk of failure. You do three things:

- Prioritize the risks.
- Apply techniques that reduce them.
- Check the outcome.

You design only the riskiest parts. This often takes hours or days, not months. The model works with waterfall or agile processes.

**Tailor the models.** Decide in advance which questions it must answer. If throughput is the main worry, build a throughput model.

**Runway and intentional architecture.** SAFe asks agile architects to keep just enough architectural runway in place for evolving business needs. The runway is not a one-time exercise. It is updated as the product changes.

## Example

A team starts a new online shop. In a short session they list their biggest risks. One risk is that checkout may be too slow during sales. They build a small throughput model, which answers one question: can checkout handle the expected load? They skip detailed design for low-risk parts, such as the help pages. As the product grows, they revisit the risk list and update their architectural intentions.

## Trade-offs

Avoiding over-design saves time, but just enough architecture needs discipline. If the team lacks the will to design, the design can degrade into ad-hoc decisions. If the team misjudges the risks, it may skip design that mattered.
