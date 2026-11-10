---
title: Fault
slug: fault
category: quality-attributes
kind: concept
summary: A fault is a defect that can cause a failure. It may stay dormant until certain conditions trigger
  it. Teams prevent, tolerate, detect and recover from faults so users do not see failures.
arc42:
- 8
- 10
- 11
step: s04-quality-requirements
related:
- fault-tolerance
- availability
- availability-tactic
- availability-tactics-fault-detection
- availability-tactics-fault-prevention
- availability-tactics-fault-recovery
- reliability
- graceful-degradation
checks:
- The document separates faults (causes) from failures (visible deviations from the specification).
- Internal and external dependencies are assessed separately as possible sources of faults.
- The document names how faults are detected, for example through monitoring and alerting.
- Recovery tactics such as rollback are described for faults that are not prevented.
- Mitigations such as redundancy or degraded-mode design are identified for known failure points.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Dependability
  title: Dependability - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis
  title: Architecture strategies for performing failure mode analysis - Microsoft Azure Well-Architected
    Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The chain from fault to error to failure.
review:
  status: generated
  flags: []
---

## Explanation

A fault is a defect in a system. People often call it a bug. A fault can sit unnoticed and never cause harm unless certain conditions trigger it.

**The chain from fault to failure**

- **Fault:** the defect, the underlying cause.
- **Error:** a runtime state in which part of the system behaves unexpectedly. It appears when a fault is activated.
- **Failure:** the visible effect. The system no longer delivers a service that matches its specification, the agreed description of what it should do.

A fault only has the potential to cause a failure. The error is the step in between.

**Errors and failures in cloud guidance**

Azure guidance uses the words a little differently. An error is an expected event that the system handles right away, with no loss of capacity. A failure is an unexpected event that usually needs intervention or specific design. The guidance also says failures happen no matter how many layers of resiliency you add.

**Where faults come from**

Azure's failure-mode guidance treats internal and external dependencies separately. An external dependency is a required component outside the workload, such as another application or a third-party service.

**What teams do about faults**

- **Fault prevention** tries to stop faults from entering the system.
- **Fault tolerance** adds mechanisms so the system still delivers the required service despite faults. The service may be degraded.

Availability tactics (see Availability Tactic) follow a similar split. They detect faults, recover from faults, and prevent faults. Rollback is a recovery tactic. Removal from service, which temporarily takes a component out of use, is a prevention tactic.

Failure mode analysis supports resilience. It identifies failure points and plans mitigations, such as redundancy and degraded-mode design. Monitoring and alerting provide the detection.

## Example

An online shop has a bug in its discount code. The bug sits unnoticed until a customer enters a code with a certain format. The checkout then reaches an unexpected state, which is the error. The customer cannot pay, which is the failure. Monitoring detects the problem. The team rolls back the last release to recover.

## Trade-offs

Tolerating faults may mean the system delivers a degraded service rather than full service. Redundancy patterns add cost and complexity, and failure mode analysis helps decide where mitigation is worth the effort.
