---
title: Reliability
slug: reliability
category: quality-attributes
kind: quality-attribute
summary: Reliability is how well a system performs its specified functions under specified conditions.
  ISO 25010 splits it into faultlessness, availability, fault tolerance and recoverability. The 2023 version
  adds a time period without interruptions and failures.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- availability
- fault-tolerance
- recoverability
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- security
- performance-efficiency
- quality-attribute
checks:
- Reliability goals name the specified functions and the specified conditions they apply to.
- Reliability goals state the time period during which the system must work without interruptions and
  failures.
- 'The document covers each sub-characteristic: faultlessness, availability, fault tolerance and recoverability.'
- The document uses faultlessness, not the older term maturity, when it follows ISO 25010:2023.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/reliability
  title: Reliability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/articles/iso-25010-update-2023
  title: Update on ISO 25010, version 2023 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Reliability is a quality characteristic in the ISO 25010 quality model (see the article ISO/IEC 25010 Product Quality Model). It asks whether a system, product or component performs specified functions under specified conditions.

The 2023 definition also says the system must perform its functions for a specified period of time without interruptions and failures. So you also state how long the system must keep working. The article ISO/IEC 25010:2023 Product Quality Model Revision covers the wider changes.

ISO 25010 breaks reliability into four sub-characteristics:

- **Faultlessness:** the system performs its functions without fault under normal operation.
- **Availability:** the system is operational and accessible when someone needs it. See the article Availability.
- **Fault tolerance:** the system keeps operating as intended even when hardware or software faults are present. See the article Fault Tolerance.
- **Recoverability:** after an interruption or failure, the system can recover the data directly affected and restore its intended state. See the article Recoverability.

In the 2023 version, faultlessness replaced the older sub-characteristic called maturity. The same revision replaced user interface aesthetics with user engagement.

Some people use the word dependability as a synonym for reliability. Dependability usually has a larger scope that also includes security and performance efficiency. See the articles Security and Performance Efficiency.

## Example

An online booking service states its reliability goal in four parts. Under normal operation, bookings are processed without faults (faultlessness). Customers can reach the service whenever they want to book (availability). If one server fails, the service keeps working (fault tolerance). After an outage, bookings made just before it are restored (recoverability).
