---
title: Quantifying Recovery and Availability Trade-Offs
slug: quantifying-recovery-and-availability-trade-offs
category: quality-attributes
kind: method
summary: You can estimate availability from how often a part fails and how fast it is repaired. Redundancy
  raises that estimate, but cost, takeover time, and slow responses pull the other way.
arc42:
- 10
- 4
- 9
- 11
step: s04-quality-requirements
related:
- availability
- redundant-spare
- active-redundancy
- architectural-decisions-for-availability
- tactic-trade-off-balancing
- architectural-trade-off-thinking
- performance-efficiency
- battlefield-control-system-atam-case-study
checks:
- The document states the availability target and how it was estimated, for example from MTBF and MTTR.
- Any redundancy-based availability figure states its assumptions, such as independence, and says whether
  failover and sync costs are included.
- The standby type (hot, warm, or cold) is named, and the state the standby holds at takeover is described.
- The document justifies the availability level against its cost, testing, and recovery automation needs.
- Response-time limits (client timeouts) are considered when judging availability.
sources:
- url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html
  title: Availability - Reliability Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/measuring-availability.html
  title: 'Measuring availability - Availability and Beyond: Understanding and Improving the Resilience
    of Distributed Systems on AWS'
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.kyautomation.com/news/4949.html
  title: 'How Hot Standby CPU Redundancy Works: Synchronized Failover for Critical Process Control - KY
    Automation'
  site: kyautomation.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

**Estimating availability.** Two numbers drive a first estimate. MTBF is the mean time between failures. MTTR is the mean time to repair. Availability is MTBF divided by (MTBF + MTTR). With an MTBF of 150 days and an MTTR of 1 hour, the result is about 99.97%.

These numbers explain what drives availability and how to improve it. They are not an empirical measure of availability, so treat the result as an estimate.

**What redundancy adds.** Suppose components are independent and redundant. Then theoretical availability is 100% minus the product of their failure rates. Two 99.9% components give 99.9999%. This is a theoretical figure that requires the components to be independent.

**How current the spare is.** The Redundant Spare tactic comes in three variants: a hot spare (active redundancy), a warm spare (passive redundancy) and a cold spare (spare). A cold spare starts with none of the failed node's state. A hot standby avoids that. In hot-standby PLC (industrial controller) setups, the primary sends its process image after every scan, and the standby confirms it is in sync. Takeover then takes about one or two scan cycles, typically 10 to 50 ms.

**Performance and availability interact.** A response slower than the client's timeout looks like a failure to the client. A design that makes responses slow can therefore lower availability, even when every component is up.

## Example

A team runs a controller with a standby. They first compute the availability of one controller from its MTBF and MTTR. They then compute the redundant ideal from the failure rates of both units. Next they ask how current the standby's state is at takeover. The ideal figure is theoretical and assumes independent components.

## Trade-offs

Higher availability usually costs more. It also demands more testing and recovery automation. Confirm the real availability need before choosing a design.

Redundancy adds cost and complexity. Slow responses can count as failures.
