---
title: Exception Handling Tactic
slug: exception-handling
category: tactics
kind: tactic
summary: Exception handling means the system reacts to a detected fault by reporting it or handling it.
  It is a recovery tactic for availability and follows fault detection.
arc42:
- 8
- 6
step: s07-solution-strategy
related:
- availability-tactics-fault-recovery
- availability-tactics-fault-detection
- graceful-degradation
- heartbeat
- ping-echo
- arc42-crosscutting-concepts
- availability-tactic
- fault
checks:
- The document states how the system and its building blocks handle errors and exceptions.
- Technical error handling concepts are written for developers, briefly and by priority.
- Exception handling is tied to a detection mechanism such as heartbeat or ping/echo.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://arc42.org/method/
  title: arc42 method - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-8-3/
  title: 'Question C-8-3: How shall I deal with the multitude of potentially crosscutting topics? | arc42
    FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Detection leads to handling, which reports or handles the exception.
review:
  status: generated
  flags: []
---

## Explanation

Exception handling is an availability tactic. It sits under "Recover from Faults", in the subcategory "Preparation and Repair". When the system detects an exception, it deals with it by reporting it or handling it.

An exception here is a condition that alters the normal flow of execution. Spotting that condition is a separate tactic, called exception detection. It belongs to the "Detect Faults" group. So detection comes first, and handling is the recovery step that follows. See Fault Detection Tactic and Fault Recovery Tactic.

Other tactics in the "Detect Faults" group include:

- **Heartbeat**: a monitor and a monitored process swap periodic messages.
- **Ping/Echo**: nodes exchange an asynchronous request and response pair.

These tactics find the fault. Exception handling responds once a fault is found.

Graceful Degradation is a separate tactic, but it sits under "Recover from Faults" (Preparation and Repair), not in the "Detect Faults" group. It keeps the most critical functions running during failures and drops less critical ones.

Error handling is also a documentation topic. The arc42 method asks cross-cutting concepts to answer how the system and its building blocks handle errors and exceptions. The arc42 FAQ advises documenting the chosen decisions briefly and by priority, and notes that highly technical concepts are documented for developers. See Crosscutting Concept.

## Example

A monitoring component notices that a worker process has stopped answering its periodic messages. That is the detection step. An exception handler then records the problem and reports it to operators.
