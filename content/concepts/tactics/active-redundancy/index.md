---
title: Active Redundancy
slug: active-redundancy
category: tactics
kind: tactic
summary: Active redundancy keeps spare components running alongside the working ones, all processing the
  same inputs. A spare can take over within milliseconds. This gives the fastest recovery, but it costs
  the most.
arc42:
- 4
- 5
- 7
- 10
- 11
step: s07-solution-strategy
related:
- redundant-spare
- availability-tactics-fault-recovery
- voting
- availability
- availability-tactic
- quantifying-recovery-and-availability-trade-offs
- tactic-trade-off-balancing
- fault-tolerance
checks:
- The document states which spare type (hot, warm or cold) protects each critical component.
- Where hot spares are used, the document explains how failures are detected, for example by voting.
- The document describes the failover logic and split-brain prevention, and says how they are exercised.
- The extra cost and complexity of hot spares is justified by the recovery time the system needs.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/approaches/standby-failover
  title: Standby/Failover | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Hot_spare
  title: Hot spare - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Active_redundancy
  title: Active redundancy - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Active and spare nodes process the same input; a voter compares results and detects faults.
review:
  status: generated
  flags: []
---

## Explanation

Active redundancy is also called a hot spare setup. It is a way to recover quickly when a component fails. (See Redundant Spare and Fault Recovery Tactic for the wider family.)

**How it works.** These patterns use a group of active components and a group of redundant spares. In active redundancy, all components belong to the active group and receive and process the same inputs in parallel.

**Why recovery is fast.** The spare holds the same state as the active component. So it can take over from a failed component in milliseconds. A hot spare is active and connected inside the working system. Even so, switching does not guarantee uninterrupted service.

**What it needs.** Voting is a tactic that checks whether replicated components produce the same results, and tri-modular redundancy combines it with the hot spare pattern (see Voting). A voter compares the results of the replicas. If they differ, it reports a fault. Teams must also build the failover machinery. This includes the logic that promotes a spare and the safeguards against split-brain, where two nodes both believe they are in charge.

**Compared with other spare types.**

- Hot spare (active redundancy): all members process input. Recovery takes milliseconds.
- Warm spare (passive redundancy): only active members process input. Spares get state updates that are only loosely synchronized. Recovery takes seconds.
- Cold spare: the spare stays out of service until a failure. It then needs a power-on reset. Recovery takes minutes, so cold spares suit high-availability systems poorly.

## Example

An online payment service runs two identical servers. Both receive every payment request and process it. Only one server's answer is used. The other keeps the same state. If the first server fails, the second takes over within milliseconds. Customers notice little or nothing.

## Trade-offs

- **Cost.** A hot spare is the most expensive option. A mirroring hot spare roughly doubles resource cost.
- **Complexity.** More redundancy raises availability, but it also raises cost and complexity. The team must build, tune and regularly exercise the failover machinery.
- **Standing cost for speed.** Warmer standby recovers faster but costs more all the time. A warm spare balances cost against availability.
- **No guarantee.** Switching over does not promise uninterrupted service.
