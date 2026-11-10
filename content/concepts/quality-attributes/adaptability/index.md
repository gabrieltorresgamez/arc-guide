---
title: Adaptability
slug: adaptability
category: quality-attributes
kind: quality-attribute
summary: Adaptability is how well a product can be changed to fit new requirements, new contexts of
  use, or a new system environment, including different or evolving hardware and software. ISO 25010 places
  it in the group now called Flexibility.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- flexibility
- iso-25010-2023-revision
- iso-iec-25010-quality-model
- replaceability
- installability
- modifiability
- maintainability
- scalability
checks:
- The document states whether adaptability covers changed requirements, or only a move to another platform.
- The document names which hardware, software, or other environments the system must be adaptable to.
- The document uses the current ISO 25010 names, with adaptability listed under Flexibility.
- The document separates adaptability from replaceability, where one product replaces another in the same
  environment.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/64-portability
  title: Flexibility
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/standards/iso-25010
  title: ISO/IEC 25010 - Systems and Software Quality | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/iso-25010-shortcomings
  title: Shortcomings of ISO 25010 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Adaptability describes how effectively and efficiently a product or system can be adapted for, or transferred to, different hardware, software, or other operational or usage environments.

**Where it sits in ISO 25010.** The ISO 25010 quality model groups product qualities into characteristics. In the 2023 update, the characteristic called Portability was renamed Flexibility. Its sub-characteristics include adaptability, scalability, installability, and replaceability. See the articles on Flexibility, Installability, Replaceability, and Scalability.

**Neighbor: replaceability.** Replaceability is a sibling of adaptability. It asks whether one product can take the place of another for the same purpose in the same environment. Adaptability asks whether the product itself can be adapted for or transferred to different environments.

**Open questions about its scope.** One critique notes that adaptability fits under both portability and maintainability, yet ISO places it only under portability. The same critique argues that adaptability and changeability are almost the same idea. It also argues that adaptability should cover changed requirements, not only a transfer to another operating system. For the maintenance view, see Modifiability and Maintainability.

## Example

A team runs an internal reporting tool on one operating system. Later the company changes its standard platform, and users also ask for a new kind of report. The first is a change of environment, which is what adaptability covers. The second is a change of requirements, which the critique above argues adaptability should also cover.
