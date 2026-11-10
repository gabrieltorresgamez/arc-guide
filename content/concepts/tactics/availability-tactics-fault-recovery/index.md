---
title: Fault Recovery Tactic
slug: availability-tactics-fault-recovery
category: tactics
kind: tactic
summary: Fault recovery tactics restore service after a fault is found. They prepare spares or retries,
  repair the problem, and bring repaired parts back into service.
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- availability-tactic
- availability-tactics-fault-detection
- availability-tactics-fault-prevention
- retry
- redundant-spare
- exception-handling
- graceful-degradation
- active-redundancy
checks:
- The document states which recovery tactics are used, such as retry, redundant spares, or graceful degradation.
- Where retry is used, the document states that the faults it targets are transient.
- Where redundant spares are used, the document says which component takes over when the primary fails.
- The document says how a repaired element is brought back into service, for example through state resynchronization.
- The document names the critical functions kept running when less critical ones are dropped.
sources:
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Where recovery sits among availability tactics
review:
  status: generated
  flags: []
---

## Explanation

Fault recovery tactics are one group of availability tactics (see Availability Tactic). They act after a fault has been detected. Other groups cover detecting faults (Fault Detection Tactic) and preventing them (Fault Prevention Tactic).

The recovery group splits in two:

- **Preparation and repair tactics** get the system working again. They combine two ideas: retrying a computation or adding redundancy.
- **Reintroduction tactics** bring a failed element back into service once it has been repaired.

**Retry.** Retry assumes the fault is transient. If so, repeating the operation may succeed. See Retry.

**Redundant spare.** A redundant spare is a duplicate component. It steps in and takes over if the primary component fails. See Redundant Spare and Active Redundancy.

**Exception handling.** Once the system detects an exception, it must deal with it in some way. See Exception Handling Tactic.

**Graceful degradation.** The system drops less critical functions when components fail. This keeps the most critical functions running. See Graceful Degradation.

**Escalating restart.** The system recovers by changing how much it restarts. It can restart a small part or a larger one.

**In-service software upgrade.** This tactic aims to replace executable code images without disrupting service.

**State resynchronization.** This is a reintroduction tactic. It partners with active and passive redundancy.

## Example

An online shop runs a primary payment service and a duplicate. The primary stops answering, so the duplicate takes over. A failed call to the address checker is retried once, because the fault may be brief. If the recommendation feature fails, the shop hides it and keeps checkout working. Later, the repaired payment service is brought back into service.
