---
title: ISO/IEC 25010 Product Quality Model
slug: iso-iec-25010-quality-model
category: quality-attributes
kind: standard
summary: ISO/IEC 25010 is a standard that sorts software product quality into named characteristics and
  subcharacteristics. The 2023 edition has nine characteristics. It gives teams a shared vocabulary for
  specifying quality.
arc42:
- 10
- 1
step: s04-quality-requirements
related:
- iso-25010-2023-revision
- quality-models-and-their-target-entities
- quality-attribute
- performance-efficiency
- reliability
- security
- availability
- arc42-quality-chapter
checks:
- Quality requirements use the names of the nine characteristics and their subcharacteristics from the
  2023 edition.
- Availability requirements say the system must be operational and accessible when required for use.
- Security requirements address resistance, meaning continued operation while under attack.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards
  title: ISO 25000 STANDARDS
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://iso25000.com/index.php/en/iso-25000-standards?start=1
  title: ISO 25000 STANDARDS
  site: iso25000.com
  accessed: '2026-11-09'
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
- url: https://www.evs.ee/en/iso-iec-25019-2023
  title: ISO/IEC 25019:2023 - EVS standard evs.ee | en
  site: evs.ee
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 belongs to the ISO/IEC 25000 series, called SQuaRE. The series has five divisions. Four of them matter here:

- **2500n** is the quality management division. It defines common models, terms and definitions.
- **2501n** is the quality model division. It presents detailed quality models for computer systems and software products.
- **2502n** is the quality measurement division. It includes a reference model for measuring software product quality.
- **2503n** is the quality requirements division. Its standard, ISO/IEC 25030, helps you specify quality requirements. You can use it to elicit them, which means to gather them from stakeholders.

The 2023 edition of the product quality model has nine quality characteristics. Each characteristic breaks down into subcharacteristics. Some examples:

- **Performance efficiency** covers time behaviour, resource utilization and capacity. See Performance Efficiency.
- **Reliability** covers faultlessness, availability, fault tolerance and recoverability. Availability means the system is operational and reachable when someone needs it. See Reliability and Availability.
- **Security** includes a new subcharacteristic, resistance. It means the system keeps operating while a malicious actor attacks it. See Security and Resistance.

The 2023 edition also split accessibility into inclusivity and user assistance.

A separate standard, ISO/IEC 25019:2023, defines the quality-in-use model. It has three characteristics. People use it to specify, measure, evaluate and improve quality in use. For what changed in 2023, see ISO/IEC 25010:2023 Product Quality Model Revision.

## Example

A team plans an online booking system. They walk through the nine characteristics as a list of questions. For reliability, they ask whether the system must stay reachable when customers need it. For security, they ask whether it must keep running during an attack. Each answer becomes a candidate quality requirement to discuss with stakeholders.
