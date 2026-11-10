---
title: ISO/IEC 25010:2023 Product Quality Model Revision
slug: iso-25010-2023-revision
category: quality-attributes
kind: standard
summary: The 2023 revision of ISO/IEC 25010 renames Usability to Interaction Capability. It also replaces
  some sub-characteristics and adds others, such as Resistance under Security and Scalability under Flexibility.
arc42:
- 10
- 1
- 12
step: s04-quality-requirements
related:
- iso-iec-25010-quality-model
- usability
- reliability
- security
- resistance
- flexibility
- scalability
- arc42-quality-chapter
checks:
- Quality requirements use the 2023 name Interaction Capability instead of Usability, or state which edition
  of the model they follow.
- Requirements that once referred to maturity or UI aesthetics now refer to faultlessness or user engagement.
- 'Security requirements consider Resistance: sustaining operations while under attack.'
- Reliability requirements are organized under Faultlessness, Availability, Fault tolerance and Recoverability.
sources:
- url: https://quality.arc42.org/articles/iso-25010-update-2023
  title: Update on ISO 25010, version 2023 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=1
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=2
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 is a quality model: a list of quality characteristics and their sub-characteristics. The article ISO/IEC 25010 Product Quality Model covers the basics. The 2023 revision changes several names and sub-characteristics. This article covers only part of the revision.

**Renamed characteristic**

- Usability is now called Interaction Capability. One source says this "might be a matter of taste".

**Sub-characteristics added**

- Inclusivity and self-descriptiveness now sit under Interaction Capability.
- Resistance now sits under Security. It means the product keeps operating while a malicious actor attacks it.
- Scalability now sits under Flexibility.

**Sub-characteristics replaced**

- User interface aesthetics became user engagement.
- Maturity became faultlessness.

**Reliability in the 2023 model**

Reliability has four sub-characteristics:

- Faultlessness: the system performs its specified functions without fault under normal operation.
- Availability.
- Fault tolerance.
- Recoverability.

**What this means for documents**

Check quality requirements that use the old names against the new ones. Examples are "usability", "UI aesthetics" and "maturity". This article gives no migration procedure, so agree on a mapping with your team and write it down.

## Example

A team's requirements list says "Usability: the interface must look modern" and "Reliability: the product must be mature". Moving to the 2023 names, the team relabels the first as Interaction Capability, with user engagement as the sub-characteristic. It relabels the second as Reliability, with faultlessness as the sub-characteristic. It also adds a Security line about Resistance: staying operational during an attack.

## Trade-offs

Adopting the new names keeps documents in line with the current model. But old requirements, and readers used to the 2011 terms, may need relabeling and explanation. The renames are not always one-to-one. Aesthetics became user engagement, so a requirement may need rewording, not just a new label.
