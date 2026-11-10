---
title: Fault Prevention Tactic
slug: availability-tactics-fault-prevention
category: tactics
kind: tactic
summary: Fault prevention is one of three groups of availability tactics. Its tactics stop faults from
  happening or from turning into failures, instead of reacting afterward.
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- availability-tactic
- availability-tactics-fault-detection
- availability-tactics-fault-recovery
- availability
- fault
- exception-handling
- architectural-tactic
- availability-responses
checks:
- The document states which prevention tactics (removal from service, transactions, predictive models,
  exception prevention, increasing the competence set) the system uses.
- Where state updates between components must be atomic, consistent, isolated, and durable, the document
  says transactions are used.
- Where process state is monitored, the document says what conditions trigger corrective action.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/realizing-and-refining-architectural-tactics-availability/
  title: 'Realizing and Refining Architectural Tactics: Availability | CMU Software Engineering Institute'
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/ACID
  title: ACID - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Where fault prevention sits among availability tactics.
review:
  status: generated
  flags: []
---

## Explanation

Availability tactics fall into three groups: detecting faults, recovering from faults, and preventing faults. See the articles Fault Detection Tactic and Fault Recovery Tactic for the other two.

Five tactics belong to this group.

**Removal from service.** The team temporarily puts a component into an out-of-service state. The goal is to mitigate potential failures.

**Transactions.** Related state updates are bundled together. The aim is that messages exchanged between components are atomic, consistent, isolated, and durable.

**Predictive model.** The system monitors the state of a process to check that it works properly. If conditions point to likely future faults, it takes corrective action.

**Exception prevention.** The system stops exceptions from occurring in the first place. It can do this by masking a fault, or by using mechanisms such as smart pointers, abstract data types, and wrappers.

**Increasing the competence set.** The team designs a component to handle more fault cases as part of its normal operation.

A 2009 SEI report updated the catalog of availability tactics. The underlying structure of the tactics categorization remained stable.

## Example

A team runs an order service. It bundles "reserve stock" and "charge payment" into one transaction, so a half-finished order never remains. It also watches the service's state and takes corrective action when the state points to likely future faults. Finally, it extends the service to handle one more kind of bad input as normal work.
