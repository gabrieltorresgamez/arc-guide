---
title: Redundant Spare
slug: redundant-spare
category: tactics
kind: tactic
summary: A redundant spare is a duplicate component that takes over when the primary fails. Hot, warm,
  and cold spares differ in how fast they take over. Faster recovery costs more and adds complexity.
arc42:
- 4
- 7
- 8
- 10
- 11
step: s07-solution-strategy
related:
- active-redundancy
- availability-tactics-fault-recovery
- heartbeat
- ping-echo
- voting
- availability
- quantifying-recovery-and-availability-trade-offs
- load-balancer
checks:
- The document states which spare type (hot, warm, or cold) each critical component uses and why.
- The document describes how failures are detected (for example heartbeat, ping/echo, or voting) and any
  grace period used.
- The document explains how a new primary is chosen and how requests are redirected, including DNS TTL
  effects if DNS is used.
- Expected failover delays are compared with the downtime (RTO) and data-loss (RPO) requirements.
- The document says how data conflicts are handled when the previous primary wrote data during or after
  failover.
sources:
- url: https://learn.microsoft.com/en-us/azure/reliability/concept-failover-failback
  title: Failover and Failback | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: 'Warm spare: the primary sends state updates, a monitor detects failure, and traffic is redirected
    to the spare.'
review:
  status: generated
  flags: []
---

## Explanation

A redundant spare is a second copy of a component. If the primary instance fails, the spare takes over. This switch is called failover. The primary is the "active" instance. The spare is the "secondary" or "passive" one.

You can set up spares in several ways. Each way trades recovery time against cost and operational complexity. The ways differ mainly in how ready the spare is.

**Hot spare (active redundancy).** Every component in the active group receives the same inputs and processes them in parallel. A hot spare is ready to accept production traffic at any time. See Active Redundancy.

**Warm spare (passive redundancy).** Only the active members process input. They send state updates to the spares. A warm spare is nearly ready, but it may need some configuration or scaling before it accepts traffic. This balances cost and availability between hot and cold.

**Cold spare.** A cold spare stays out of service until a failure occurs. It might not even be deployed yet, so it must be deployed first. Recovery is slowest. Its high mean time to recovery (MTTR) makes it a poor fit for high-availability systems.

**Active-active.** In an active-active system, all instances serve requests at all times. No failover step is needed.

**How failover starts.** Automated failover needs failure detection. Instances can send heartbeat events, or a separate component can probe each instance at regular intervals. Other detection tactics are ping/echo and voting among replicated components. See Heartbeat, Ping/Echo, and Voting. A grace period helps avoid false alarms when an instance is only busy.

**After the switch.** The system picks a new primary. Some services use consensus or leader election algorithms for this. Requests must then be redirected, for example through a load balancer or DNS. DNS caching (TTL) can delay clients.

**Data consistency.** The old primary may have done work or written data during or after failover. Switching back (failback) may then need conflict resolution or manual intervention.

## Example

An online shop runs its order database on two servers. In one design, both servers handle every order at the same time. If one dies, the other simply carries on. In a cheaper design, one server handles orders and sends regular updates to a second server. If the first dies, the second needs a short time to start serving. In the cheapest design, a replacement server is only set up after the failure. Customers wait the longest, but the shop pays the least while everything works.

## Trade-offs

- Faster recovery costs more. Hot spares are always ready, but they run all the time. Cold spares cost less but recover slowest.
- Spares add cost and operational complexity.
- Failover takes time. Plan it against your allowed downtime (recovery time objective, RTO) and allowed data loss (recovery point objective, RPO).
- Failback can need conflict resolution if the old primary wrote data during failover.
- Too short a detection grace period can trigger false failovers when an instance is only busy.
