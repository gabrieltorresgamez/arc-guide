---
title: Integrability, Deployability, Testability and Reliability Tactics
slug: integrability-deployability-and-testability-tactics
category: tactics
kind: tactic
summary: 'Tactics are design decisions grouped by the quality goal they serve. This article covers a few:
  heartbeat for fault detection, plus rollback, blue/green deployment and feature toggles for safe releases.'
arc42:
- 4
- 7
- 8
- 9
step: s07-solution-strategy
related:
- architectural-tactic
- heartbeat
- availability-tactics-fault-detection
- reliability
- testability
- modifiability-tactics-in-soa
- choosing-and-applying-tactics
- integration
checks:
- The architecture documents which mechanisms, such as feature toggles and backward-compatible interfaces,
  support rollback.
- The document states how a failed release is rolled back to an earlier version.
- Fault-detection tactics such as heartbeat are named for the monitored processes.
- Tactics are listed under the quality goal they address.
sources:
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/blog/two-categories-of-architecture-patterns-for-deployability/
  title: Two Categories of Architecture Patterns for Deployability | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/feature-toggles.html
  title: Feature Toggles (aka Feature Flags)
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/integrability/
  title: Integrability | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Architectural tactics are building blocks of design, and they influence how a system responds in terms of a quality attribute. Tactics are grouped by the goal they address. For robustness and reliability, the goal is to prevent, mask or repair faults. See Architectural Tactic for the general concept.

This article covers three areas.

**Integrability.** Mechanisms such as patterns and tactics are commonly used to satisfy integrability requirements.

**Reliability.** Heartbeat is a fault-detection tactic. It employs a periodic message exchange between a system monitor and the process being monitored. See Heartbeat for more detail.

**Deployability.** The need to roll back or disable features leads to architectural decisions about mechanisms such as feature toggles and backward-compatible interfaces. These decisions are best taken early.

- *Rollback.* A defect may appear after a release. The team often has to go back to the previous version until the defect is fixed.
- *Blue/green deployment.* This is one way to scale a rollout. The team starts new instances. Then it switches traffic to them by changing the DNS or the discovery service so that it points to the new version.
- *Feature toggles.* This is a set of patterns for delivering new functionality quickly but safely. Release toggles let unfinished, untested code paths ship to production as latent code.

## Example

A team releases a new version of a service. It starts new instances beside the old ones. Then it changes the discovery service so traffic goes to the new instances. The new checkout code ships switched off behind a release toggle. If a defect shows up, the team rolls back to the previous version while it fixes the problem. A monitor also exchanges periodic heartbeat messages with the service.

## Trade-offs

Decisions about mechanisms such as feature toggles and backward-compatible interfaces are best taken early. Release toggles also ship unfinished, untested code to production as latent code.
