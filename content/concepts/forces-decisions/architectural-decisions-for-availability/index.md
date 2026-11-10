---
title: Architectural Decisions for Availability
slug: architectural-decisions-for-availability
category: forces-decisions
kind: concept
summary: 'Designing for availability means asking structured questions: which parts must stay up, how
  faults are detected, and how the system keeps working when something fails. The answers become design
  decisions.'
arc42:
- 4
- 8
- 9
- 10
step: s07-solution-strategy
related:
- availability
- availability-tactic
- heartbeat
- graceful-degradation
- availability-tactics-fault-detection
- availability-tactics-fault-recovery
- architectural-tactic
- responsibility-allocation
checks:
- The document states which components must be highly available and why, for example servers that are
  single points of failure.
- The document assigns responsibility for detecting faults and for handling detected exceptions.
- The document describes how the system keeps its most critical functions working when elements fail.
- The document explains how failed elements are replaced or their responsibilities reassigned.
- The document names the cost and complexity of redundancy that was accepted.
sources:
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=2
  title: '3.2 Design Concepts: The Building Blocks for Creating Structures | Making Design Decisions |
    InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=5
  title: 3.5 Design Concepts to Support Modifiability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Servers can be single points of failure, so they often deserve a close look. More redundancy (spare or duplicate parts) raises availability, but it also raises cost and complexity.

Design decisions that shape how a system responds to a quality goal are called tactics (see Availability Tactic).

Availability tactics address several concerns:
- Detecting faults. The system cannot act on a fault until it has detected or anticipated it.
- Handling exceptions. After the system detects an exception, it must handle it somehow.
- Masking faults. The system can compare results from several redundant components and vote when their outputs differ.
- Degraded operation. The system keeps its most critical functions running while some elements fail.

A Heartbeat is one fault detection tactic: a system monitor and a monitored process exchange periodic messages.

Reconfiguration is a recovery tactic that deals with a failed element by reassigning its responsibilities to the resources still functioning.

See Fault Detection Tactic, Fault Recovery Tactic and Graceful Degradation for more detail.

## Example

An online shop decides that checkout must be highly available, while product reviews need not be. The team assigns one component to detect failures with periodic messages. If the payment service fails, a spare takes over its work. If reviews fail, the shop still lets people check out.

## Trade-offs

Redundancy buys availability, but it adds cost and complexity.
