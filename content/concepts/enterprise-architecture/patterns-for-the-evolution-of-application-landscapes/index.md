---
title: Application Landscape Evolution Drivers
slug: patterns-for-the-evolution-of-application-landscapes
category: enterprise-architecture
kind: concept
summary: Application landscape evolution drivers are the business and IT goals that push a company to
  change its applications. Typical drivers are cost, agility, resilience and AI. They guide choices such
  as retire, replace, rehost or refactor.
arc42:
- 1
- 4
- 11
step: s12-evolve
related:
- enterprise-architecture-strategy
- technical-debt
- application-lifecycle-diagram
- business-capability-map
- architecture-principle
- conflicting-architecture-principles
- enterprise-architecture-management
- refactoring
checks:
- Each planned landscape change is tied to a documented business goal or driver.
- The chosen strategy per application (retire, replace, rehost, refactor, retain) is stated with its reason.
- A target stack per area is defined, with justified exceptions.
- Rehosted workloads with known problems have a modernization plan.
- Strategy decisions are reviewed on a regular cycle against current goals.
sources:
- url: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/select-cloud-migration-strategy
  title: Select your cloud migration strategies - Cloud Adoption Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://cosh.de/en/2-application-harmonization/
  title: 2. Application Harmonization - CosH Information Technology
  site: cosh.de
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html
  title: About the migration strategies - AWS Prescriptive Guidance
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/blog/gartner-time-invest
  title: 'Gartner® TIME Framework For App Rationalization: Invest'
  site: leanix.net
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A driver guides the choice of strategy.
review:
  status: generated
  flags: []
---

## Explanation

An application landscape is the set of applications a company runs. Drivers are the reasons that landscape changes.

**Where drivers come from.** A driver arises from a gap between a workload's current state and the state the business wants. It is a specific, actionable reason for change. Typical high-level goals behind cloud-driven change are adopting AI, agility, innovation, cost reduction and resilience.

**Standardization and consolidation.** Companies often run duplicate or similar applications. Harmonization merges them. It uses capability mapping, which groups applications by function or value-added. Standardization reduces versions and variants. It phases out legacy systems in a targeted way. It also defines a target stack per area, with justified exceptions.

**Cost.** Landscape optimization aims to cut cost. Quick wins often sit in licenses, operations and support.

**How drivers become evolution patterns.** The driver guides which migration strategy fits.

- **Retire:** decommission redundant, obsolete or low-value applications. This shrinks the landscape. It also removes cost and the security risk of unsupported components.
- **Replace (repurchase):** switch to SaaS or AI solutions. The aims are simpler operations, freed development resources and lower maintenance, infrastructure and licensing cost.
- **Refactor:** rework the application. Business demand for scale, faster releases and lower cost drives it.
- **Retain:** keep the application in place, for example for compliance, data residency, risk or dependencies.

**Portfolio view.** The TIME model, as described by LeanIX, rates applications on technical and functional fit. It supports rationalizing the portfolio: Tolerate, Invest, Migrate, Eliminate. Strategy choices should be tied to documented goals and reviewed regularly, because business priorities change.

## Example

A company runs three order-entry tools after mergers. Cost reduction and standardization are the drivers. The team maps each tool to the capability it supports and picks one target tool. It retires the other two. It replaces a custom reporting tool with a SaaS product. One tool that holds regulated data stays in place. It stays for data residency reasons. The team reviews these choices each year against the company's goals.

## Trade-offs

Drivers can conflict. Rehosting is fast and low-risk, but it carries technical debt forward. Problematic workloads should be modernized instead. Refactoring serves scale, speed and cost goals, yet it is the most complex strategy, and it is hard to manage across many applications in large migrations. Security and compliance needs, such as data residency, can also block moving an application to the cloud. Make the priorities explicit and review them as goals change.
