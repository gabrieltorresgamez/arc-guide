---
title: Availability
slug: availability
category: quality-attributes
kind: quality-attribute
summary: Availability is the share of time a system is operational and usable when people need it. It
  is usually given as a percentage. Each extra nine cuts allowed downtime sharply but costs more to achieve.
arc42:
- 1
- 10
- 7
- 11
step: s04-quality-requirements
related:
- reliability
- recoverability
- fault-tolerance
- availability-tactic
- availability-scenario
- iso-iec-25010-quality-model
- redundant-spare
- architectural-decisions-for-availability
checks:
- The availability target is stated as a percentage over a defined period, such as a month or year.
- The document states whether scheduled maintenance counts as downtime, and why.
- The availability calculation includes external services that affect critical flows.
- The document distinguishes the contractual SLA from stricter internal SLOs.
- Redundancy or failover used to reach the target is described, with its added operational complexity.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html
  title: Availability - Reliability Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics
  title: Architecture strategies for defining reliability targets - Microsoft Azure Well-Architected Framework
    | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Two independent app copies raise availability, while a hard dependency on an external service
    still limits the overall result.
review:
  status: generated
  flags: []
---

## Explanation

The ISO 25010 quality model defines availability as the degree to which a system is operational and accessible when required for use. It sits under reliability, next to fault tolerance (working as intended despite hardware or software faults), recoverability, and faultlessness (performing functions without fault under normal operation). See the articles Reliability, Fault Tolerance and Recoverability.

**How it is measured.** AWS describes availability as the percentage of time a workload is available, measured over a period such as a month or a year. For a dependency without published figures, availability can be estimated from MTBF (mean time between failures) and MTTR (mean time to recover). With an MTBF of 150 days and an MTTR of 1 hour, the result is 99.97%.

**The nines.** Small percentage differences mean large differences in downtime per year:

| Availability | Downtime per year |
|---|---|
| 99.9% | about 8.8 hours (AWS rounds to 8h45m) |
| 99.99% | about 52 minutes |
| 99.999% | about 5 minutes (Azure: 5.26 minutes) |

**Planned downtime.** Some teams leave scheduled maintenance out of the total time. AWS advises against this, because users still want to use the service during maintenance.

**Dependencies.** If your system hard-depends on other systems, its availability is the product of their availabilities. Every external service therefore lowers the result. Azure advises including external services in composite targets when they affect critical flows.

**Redundancy.** Independent redundant components raise availability. The result is 100% minus the product of the component failure rates. Two 99.9% components give 99.9999%. Azure treats multiregion deployment as one form of redundancy that can improve targets through failover.

**Contracts and targets.** Azure separates two terms. An SLA is a formal contract with financial and legal consequences if the provider misses it. An SLO is an internal target, and it may be stricter than the SLA.

## Example

A team runs an online booking tool. Their own application reaches 99.9%. It also calls a hard-dependency payment service rated 99.9%. Because the two multiply, the booking flow ends up slightly below 99.9%. The team then runs two independent copies of the application, each at 99.9%, in different locations. Failover between them lifts the application part to 99.9999%. The payment service now limits the overall result, so the team includes it in its composite target.

## Trade-offs

Higher availability costs more. According to AWS, it needs automated recovery from all kinds of failures. It also needs operations that are built and tested to the same standard, and at very high levels of availability innovation suffers. Multiregion deployment improves targets but adds operational complexity, according to Azure. Choose a target that matches what users actually need, and set internal targets with the contract level in mind.
