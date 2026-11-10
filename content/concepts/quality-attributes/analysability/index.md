---
title: Analysability
slug: analysability
category: quality-attributes
kind: quality-attribute
summary: Analysability is how easily people can judge the effect of a change, diagnose a failure, and
  find the parts to modify. ISO/IEC 25010 lists it as one of five maintainability sub-characteristics.
arc42:
- 10
step: s04-quality-requirements
related:
- maintainability
- iso-iec-25010-quality-model
- modularity
- modifiability
- testability
- reusability
- arc42-quality-chapter
- quality-attribute-scenario
checks:
- Analysability appears as a sub-characteristic of maintainability in the quality tree.
- Analysability scenarios are specific and measurable, for example for impact analysis or failure diagnosis.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/ISO/IEC_9126
  title: ISO/IEC 9126 - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Analysability among the five maintainability sub-characteristics, with its three facets.
review:
  status: generated
  flags: []
---

## Explanation

Analysability is a quality of a product or system. It tells you how effectively and efficiently you can assess the impact of a change. The ISO 25010 page also ties it to diagnosing defects or failure causes and to identifying the parts that need modification.

**Where it sits in the standard**

ISO/IEC 25010 defines maintainability as how effectively and efficiently a product or system can be changed. It lists five sub-characteristics:

- modularity
- reusability
- analysability
- modifiability
- testability

Modularity means a system is built from discrete components. It is a sibling of analysability. Modifiability and testability are siblings too. For the wider model, see ISO/IEC 25010 Product Quality Model. For the parent characteristic, see Maintainability.

**Change from the older standard**

The older ISO 9126 defined maintainability as the effort needed for specified modifications. ISO/IEC 25010:2011 replaced it. The ISO 9126 sub-characteristics were analyzability, changeability, stability, testability and compliance. In 25010, changeability and stability were merged into modifiability. Modularity and reusability were added.

**Three facets**

1. Impact analysis: judging what a planned change will affect.
2. Failure diagnosis: finding the cause of a defect or failure.
3. Locating the parts to change: identifying which components need modification.

**Making it concrete**

arc42 describes a quality tree as a structure that refines the generic term quality from a root. It recommends scenarios that are specific and measurable. You can apply this to analysability. Write scenarios for impact analysis or failure diagnosis, and place them in the quality tree. See arc42 Quality Requirements.

## Example

A team keeps a quality tree with "maintainability" as a branch and "analysability" beneath it. One scenario under it covers failure diagnosis. It names a specific failure, says who investigates, and sets a measurable target for how the cause is found. Another scenario covers impact analysis. It names a planned change and a measurable target for listing the affected components. Reviewers can then check whether the architecture meets each scenario.
