---
title: Availability Tactic Categories
slug: availability-responses
category: tactics
kind: concept
summary: 'Availability tactics fall into three groups: detect faults, recover from faults, and prevent
  faults. Architects combine tactics from all three groups to meet an availability goal, and they weigh
  each choice against cost and complexity.'
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- availability-tactic
- availability-tactics-fault-detection
- availability-tactics-fault-recovery
- availability-tactics-fault-prevention
- graceful-degradation
- active-redundancy
- heartbeat
- ping-echo
checks:
- 'The document names which tactics cover each of the three categories: detect, recover and prevent.'
- Each redundancy choice states its cost and complexity impact.
- The availability target is stated as a percentage over a period, and the need for it is justified.
- The recovery time (MTTR) of spare-based redundancy is stated.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/qualities/graceful-degradation
  title: Graceful degradation | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html
  title: Availability - Reliability Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The three categories of availability tactics with examples.
review:
  status: generated
  flags: []
---

## Explanation

A *tactic* is a design move that helps a system reach a quality goal. For availability (how much of the time a system works), tactics fall into three major categories: detect faults, recover from faults, and prevent faults.

**Detect faults.** These tactics notice that something has gone wrong. Three examples:

- *Heartbeat*: a monitor and the monitored process exchange messages at regular intervals.
- *Ping/echo*: one node sends a request and another node answers. The exchange is asynchronous.
- *Exception detection*: the system recognizes a condition that changes the normal flow of execution.

**Recover from faults.** These tactics restore service after a fault. Graceful degradation is one of them. The system keeps its most critical functions running while components fail, and it drops less critical functions. The arc42 quality model describes the same idea as keeping functionality when parts of a system break down.

**Prevent faults.** These tactics stop a fault from turning into a failure. One example:

- *Removal from service*: the team temporarily takes a component out of service to head off likely failures.

**Measuring the result.** Availability is the percentage of time a workload is available over a period, such as a month or year. It is often expressed in nines, such as 99.9%. You can estimate it from MTBF (mean time between failures) and MTTR. With an MTBF of 150 days and an MTTR of 1 hour, the estimate is 99.97%.

Independent redundant components raise the theoretical figure. Two independent 99.9% components together give 99.9999%.

## Example

An online shop wants its checkout to stay available. The team adds a heartbeat so a monitor notices when the payment service stops responding (detect). It runs a second, always-active payment instance as a hot spare (recover). If both fail, the shop keeps browsing and the cart working and turns off recommendations (recover, by graceful degradation).

## Trade-offs

More redundancy gives higher availability, but it also raises cost and complexity. Higher availability targets also call for recovery automation and thorough testing. So identify the true availability need before designing. A cold spare is cheaper to keep than a hot spare, but it has a high MTTR. Choose and combine tactics from each category to fit the target.
