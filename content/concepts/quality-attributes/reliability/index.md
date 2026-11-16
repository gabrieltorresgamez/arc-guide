---
title: Reliability
slug: reliability
order: 50
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
- iso-iec-25010-product-quality-model
- security
- performance-efficiency
- quality-attribute
- fault
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
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: "ISO 25010"
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/faultlessness
  title: "Faultlessness | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html
  title: "Availability - Reliability Pillar"
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics
  title: "Architecture strategies for defining reliability targets - Microsoft Azure Well-Architected Framework | Microsoft Learn"
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/availability
  title: "Availability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: "Tactics and Patterns for Software Robustness | CMU Software Engineering Institute"
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/retry
  title: "Retry pattern - Azure Architecture Center | Microsoft Learn"
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/qualities/fault-tolerance
  title: "Fault tolerance | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/5574.html
  title: "Recovery Oriented Computing (ROC): Motivation, Definition, Techniques, and Case Studies | EECS at UC Berkeley"
  site: www2.eecs.berkeley.edu
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/recoverability
  title: "Recoverability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/withstand-ddos-attack
  title: "Withstand DDoS Attack"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/order-queue
  title: "Order queue"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/unavailability-max-2-minutes
  title: "Unavailable for max 2 minutes"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/measuring-availability.html
  title: Measuring availability - Availability and Beyond
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Reliability is a quality characteristic in the ISO 25010 quality model (see the article ISO/IEC 25010 Product Quality Model). It asks whether a system, product or component performs specified functions under specified conditions.

The 2023 definition also says the system must perform its functions for a specified period of time without interruptions and failures. So you also state how long the system must keep working.

Some people use the word dependability as a synonym for reliability. Dependability can have a larger scope that also includes security and performance efficiency. See the articles Security and Performance Efficiency.

**Tactics.** See the article Reliability Tactic.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Faultlessness** means that the system performs its specified functions without fault under normal operation. More: [arc42 quality model](https://quality.arc42.org/qualities/faultlessness).
- **Availability** is the share of time a system is operational and usable when people need it. It is usually given as a percentage. Higher availability targets typically cost more to achieve. A first estimate is MTBF (mean time between failures) divided by MTBF plus MTTR (mean time to repair). More: [arc42 quality model](https://quality.arc42.org/qualities/availability), [Availability - Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html), [Architecture strategies for defining reliability targets - Microsoft Azure Well-Architected Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics).
- **Fault tolerance** is how well a system keeps working as intended while hardware or software faults are present. It draws on tactics for detecting, recovering from and preventing faults. More: [arc42 quality model](https://quality.arc42.org/qualities/fault-tolerance), [Tactics and Patterns for Software Robustness | CMU Software Engineering Institute](https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/), [Retry pattern - Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry).
- **Recoverability** is how well a system gets its affected data back after an interruption or failure. More: [arc42 quality model](https://quality.arc42.org/qualities/recoverability), [Architecture strategies for defining reliability targets - Microsoft Azure Well-Architected Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics), [Recovery Oriented Computing (ROC): Motivation, Definition, Techniques, and Case Studies | EECS at UC Berkeley](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/5574.html).

**In the arc42 quality model.** The arc42 quality model has its own page on [Reliability](https://quality.arc42.org/qualities/reliability).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [Withstand DDoS Attack](https://quality.arc42.org/requirements/withstand-ddos-attack), [Order queue](https://quality.arc42.org/requirements/order-queue), [Unavailable for max 2 minutes](https://quality.arc42.org/requirements/unavailability-max-2-minutes).

## Example

An online booking service states its reliability goal in four parts. Under normal operation, bookings are processed without faults (faultlessness). Customers can reach the service whenever they want to book (availability). If one server fails, the service keeps working (fault tolerance). After an outage, bookings made just before it are restored (recoverability).
