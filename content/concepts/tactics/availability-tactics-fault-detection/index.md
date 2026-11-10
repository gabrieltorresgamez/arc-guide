---
title: Fault Detection Tactic
slug: availability-tactics-fault-detection
category: tactics
kind: tactic
summary: Fault detection tactics spot a problem before it grows into a failure users can see. Common techniques
  are ping/echo, heartbeat, monitors, time stamps, condition monitoring, voting and exception detection.
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- availability-responses
- availability-tactics-fault-recovery
- availability-tactics-fault-prevention
- ping-echo
- heartbeat
- voting
- exception-handling
- availability-scenario
checks:
- The document names which detection techniques are used (for example ping/echo, heartbeat, monitor, voting).
- Where a monitor is used, it is a separate component that observes the health of other parts.
- Where triple modular redundancy is used, the document states that three components get identical inputs
  and their outputs are compared.
- Detection is linked to recovery tactics that act after a fault is detected.
sources:
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Triple_modular_redundancy
  title: Triple modular redundancy - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: A monitor detects a fault and triggers a recovery tactic.
review:
  status: generated
  flags: []
---

## Explanation

Before a system can act on a fault, it must detect or anticipate that fault. Detection is one group of tactics. Recovery and prevention are the other groups (see Availability Tactic Categories).

The main detection techniques are:

**Monitor.** A monitor is a separate component. It watches the health of other parts of the system.

**Ping/echo.** One node sends an asynchronous request to another and waits for a reply. This checks that the node is reachable and shows the round-trip delay. See Ping/Echo.

**Heartbeat.** A system monitor and the process it watches exchange messages at regular intervals. See Heartbeat.

**Time stamp.** This tactic detects events that arrive in the wrong order. It is used mainly in distributed systems that pass messages.

**Condition monitoring.** The system checks conditions in a process or device. It can also check that assumptions made at design time still hold.

**Voting.** Several components process the same input and their outputs are compared. The most common form is triple modular redundancy: three components, identical inputs, compared outputs. In the circuit version, a majority gate outputs 1 when at least two of three inputs are 1. One failed circuit is outvoted. See Voting.

**Exception detection.** The system notices a condition that changes the normal flow of execution. Handling that condition is a separate topic (see Exception Handling Tactic).

## Example

An online shop has an order service and a payment service. A monitor sends a ping to the payment service at regular intervals. If no reply arrives in time, the monitor raises an alert. Recovery tactics can then take over, ideally before shoppers notice a problem.
