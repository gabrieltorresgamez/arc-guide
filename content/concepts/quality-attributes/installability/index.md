---
title: Installability
slug: installability
category: quality-attributes
kind: quality-attribute
summary: Installability describes how well a product can be installed and removed in a specific environment.
  In the 2023 wording of ISO/IEC 25010, it sits under Flexibility, next to adaptability, scalability and
  replaceability.
arc42:
- 10
- 7
- 1
step: s04-quality-requirements
related:
- flexibility
- adaptability
- scalability
- replaceability
- iso-25010-2023-revision
- iso-iec-25010-quality-model
- quality-attribute
- compatibility
checks:
- The document names the specific environment in which installation and uninstallation must succeed.
- Installability goals cover both installing and uninstalling, not installing alone.
- Installability is placed under Flexibility, with the model version stated, and is kept distinct from
  adaptability, scalability and replaceability.
- The document explains how much installability is needed and why, rather than aiming for the maximum.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=8
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/64-portability
  title: Flexibility
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/replaceability
  title: Replaceability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Installability is a quality attribute. It asks: can people put this product into a given environment, and take it out again, successfully?

The standard defines it as the degree of effectiveness and efficiency of installing and/or uninstalling a product in a specified environment.

The phrase "specified environment" matters too. The definition refers to installing and/or uninstalling in a specified environment.

**Where it sits in the quality model**

In the 2023 wording shown on iso25000.com, installability is a sub-characteristic of Flexibility. Flexibility means the degree to which a product can adapt to changes in its requirements, contexts of use or system environment. (See the articles Flexibility and ISO/IEC 25010:2023 Product Quality Model Revision.)

**Its siblings under Flexibility**

- **Adaptability:** adapting or transferring a product to different hardware or environments.
- **Scalability:** handling growing or shrinking workloads by adapting capacity.
- **Replaceability:** one product replacing another for the same purpose in the same environment.

## Example

A team builds an internal reporting tool. The stated environment is "a standard office laptop." The team writes down that installing and removing the tool must both succeed in that environment. Testers then try both on such a laptop and record whether each worked.

## Trade-offs

arc42 says of replaceability that it reduces lock-in risk, but it is not free and rarely worth maximizing.
