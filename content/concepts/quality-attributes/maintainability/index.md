---
title: Maintainability
slug: maintainability
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
- modifiability
- modularity
- analysability
- testability
- reusability
- technical-debt
- modifiability-tactics
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
diagrams:
- file: diagram-1.mmd
  caption: The five aspects of maintainability in ISO/IEC 25010.
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 (see ISO/IEC 25010 Product Quality Model) defines maintainability as how effectively and efficiently a product can be modified. A change can improve the product, correct it, or adapt it to a new environment or new requirements.

**Five aspects of maintainability**

- **Modularity:** The system is built from discrete components. Changing one component has minimal impact on the others. See Modularity.
- **Reusability:** A product can serve as an asset in more than one system, or when building other assets. See Reusability.
- **Analysability:** People can assess the impact of a planned change. They can diagnose the causes of failures and identify which parts to modify. See Analysability.
- **Modifiability:** People can change the product effectively and efficiently. They add no defects and do not degrade existing quality. See Modifiability.
- **Testability:** Test criteria can be set, and tests can show whether those criteria are met. See Testability.

**Types of maintenance**

ISO/IEC 14764 sorts software maintenance into four types. Corrective maintenance fixes a bug or other failure to meet requirements, typically one reported by an end user. Adaptive maintenance modifies software after delivery so it stays usable in a changed or changing environment.

**Tactics**

An architectural tactic is a design decision that affects how well an architecture serves a quality attribute. See Architectural Tactic. For modifiability, a Software Engineering Institute report justifies tactics through coupling, cohesion, and cost. It describes each tactic by how well it controls these parameters.

**Technical debt and legacy systems**

Technical debt means internal quality deficiencies, sometimes called cruft. They make a system harder to modify and extend. The extra effort needed to add features is the interest paid on that debt. See Technical Debt.

Software is eventually withdrawn from the market, but it may stay in use. Legacy systems are old and hard to modify, yet still needed.

## Example

A team runs an online shop. Orders, payments, and shipping are separate components. A change to the shipping rules touches only the shipping component, so the team can estimate the impact quickly. A user reports a wrong total, and the team fixes it. That is corrective maintenance. Later the payment provider changes its interface, and the team updates the shop so it keeps working. That is adaptive maintenance. Each change comes with tests that show whether the shop still behaves as expected.

## Trade-offs

One cost is clear: when internal quality deficiencies pile up as technical debt, adding features takes extra effort in the areas where that cruft sits.
