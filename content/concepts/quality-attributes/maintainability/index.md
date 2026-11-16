---
title: Maintainability
slug: maintainability
order: 70
category: quality-attributes
kind: quality-attribute
summary: Maintainability is how effectively and efficiently people can modify a product to improve it,
  correct it, or adapt it to a new environment or new requirements.
arc42:
- 1
- 4
- 10
- 11
step: s04-quality-requirements
related:
- modularity
- technical-debt
- maintainability-tactics
- iso-iec-25010-quality-model
checks:
- The document states how the system is split into discrete components so that a change to one has minimal
  impact on others.
- The document explains how the impact of a planned change can be assessed and how failure causes can
  be diagnosed.
- Test criteria are defined, and tests can show whether they are met.
- Known technical debt, meaning internal quality deficiencies that make changes harder, is listed.
- The plan covers legacy parts that are hard to modify but still needed.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Software_maintenance
  title: Software maintenance - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://martinfowler.com/bliki/TechnicalDebt.html
  title: Technical Debt
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: "ISO 25010"
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/modularity
  title: "Modularity | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://arxiv.org/html/2409.04830v1
  title: "Beyond Dependencies: The Role of Copy-Based Reuse in Open Source Software Development"
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/reusability
  title: "Reusability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/ISO/IEC_9126
  title: "ISO/IEC 9126 - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: "10 - Quality | arc42 Documentation"
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/qualities/analysability
  title: "Analysability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://www.tmap.net/wiki/quality-characteristics-iso25010/
  title: "Quality characteristics ISO25010 - TMAP"
  site: tmap.net
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/modifiability
  title: "Modifiability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://arxiv.org/abs/1801.02201
  title: "[1801.02201] A survey on software testability"
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Software_testability
  title: "Software testability - Wikipedia"
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/testability
  title: "Testability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/shared-library-adoption-by-product-teams
  title: "Shared library adoption by product teams"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/monolith-loose-coupling-change-blast-radius
  title: "Monolith loose coupling: change blast radius"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/test-coverage-for-critical-business-logic
  title: "Test Coverage for Critical Business Logic"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/maintainability
  title: "Maintainability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: The five aspects of maintainability in ISO/IEC 25010.
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 (see ISO/IEC 25010 Product Quality Model) defines maintainability as how effectively and efficiently a product can be modified. A change can improve the product, correct it, or adapt it to a new environment or new requirements.

**Types of maintenance**

ISO/IEC 14764 sorts software maintenance into four types. Corrective maintenance fixes a bug or other failure to meet requirements, typically one reported by an end user. Adaptive maintenance modifies software after delivery so it stays usable in a changed or changing environment.

**Tactics**

An architectural tactic is a design decision that affects how well an architecture serves a quality attribute. See Architectural Tactic. For modifiability, a Software Engineering Institute report justifies tactics through coupling, cohesion, and cost. It describes each tactic by how well it controls these parameters.

**Technical debt and legacy systems**

Technical debt means internal quality deficiencies, sometimes called cruft. They make a system harder to modify and extend. The extra effort needed to add features is the interest paid on that debt. See Technical Debt.

Software is eventually withdrawn from the market, but it may stay in use. Legacy systems are old and hard to modify, yet still needed.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Modularity** means that the system is built from discrete components, so a change to one component has minimal impact on the others. More: [arc42 quality model](https://quality.arc42.org/qualities/modularity).
- **Reusability** is how well something you built, such as code or a design, can serve in more than one system. You can reuse by copying or by depending on shared code. Each way has costs and risks. More: [arc42 quality model](https://quality.arc42.org/qualities/reusability), [Beyond Dependencies: The Role of Copy-Based Reuse in Open Source Software Development](https://arxiv.org/html/2409.04830v1).
- **Analysability** is how easily people can judge the effect of a change, diagnose a failure, and find the parts to modify. More: [arc42 quality model](https://quality.arc42.org/qualities/analysability), [ISO/IEC 9126 - Wikipedia](https://en.wikipedia.org/wiki/ISO/IEC_9126), [10 - Quality | arc42 Documentation](https://docs.arc42.org/section-10/).
- **Modifiability** describes how well a system can be changed. Architects steer it by adjusting coupling, cohesion, and cost, using architectural tactics. More: [arc42 quality model](https://quality.arc42.org/qualities/modifiability), [Modifiability Tactics | CMU Software Engineering Institute](https://www.sei.cmu.edu/library/modifiability-tactics/), [Quality characteristics ISO25010 - TMAP](https://www.tmap.net/wiki/quality-characteristics-iso25010/).
- **Testability** is how well a system supports its own testing. High testability makes faults easier to find by testing. Low testability means more test effort. More: [arc42 quality model](https://quality.arc42.org/qualities/testability), [1801.02201 A survey on software testability](https://arxiv.org/abs/1801.02201), [Software testability - Wikipedia](https://en.wikipedia.org/wiki/Software_testability).

**In the arc42 quality model.** The arc42 quality model has its own page on [Maintainability](https://quality.arc42.org/qualities/maintainability).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [Shared library adoption by product teams](https://quality.arc42.org/requirements/shared-library-adoption-by-product-teams), [Monolith loose coupling: change blast radius](https://quality.arc42.org/requirements/monolith-loose-coupling-change-blast-radius), [Test Coverage for Critical Business Logic](https://quality.arc42.org/requirements/test-coverage-for-critical-business-logic).

## Example

A team runs an online shop. Orders, payments, and shipping are separate components. A change to the shipping rules touches only the shipping component, so the team can estimate the impact quickly. A user reports a wrong total, and the team fixes it. That is corrective maintenance. Later the payment provider changes its interface, and the team updates the shop so it keeps working. That is adaptive maintenance. Each change comes with tests that show whether the shop still behaves as expected.

## Trade-offs

One cost is clear: when internal quality deficiencies pile up as technical debt, adding features takes extra effort in the areas where that cruft sits.
