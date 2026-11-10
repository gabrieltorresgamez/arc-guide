---
title: Safety Tactic
slug: safety-tactics
category: tactics
kind: tactic
summary: Safety tactics help a system stay in control of known hazards. They detect problems, contain
  them with barriers or redundancy, and fall back to a safe state when needed. Examples are interlocks,
  watchdogs, timeouts and fail-safe defaults.
arc42:
- 8
- 10
- 4
step: s07-solution-strategy
related:
- safety
- availability-tactic
- heartbeat
- architectural-tactic
- voting
- hazard-warning
- fault-tolerance
- graceful-degradation
checks:
- Each hazardous operation is guarded by an explicit interlock that checks preconditions and defaults
  to a safe state.
- The document states which safe state the system enters when something goes wrong (fail-safe default).
- Each watchdog monitor runs in a separate failure domain from the component it supervises.
- Heartbeat intervals for watchdogs are chosen to avoid false-positive restarts.
sources:
- url: https://quality.arc42.org/approaches/safety-interlocks
  title: Safety Interlocks | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/tag-safe/
  title: '#safe | arc42 Quality Model'
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/watchdog-supervision
  title: Watchdog Supervision | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: An interlock gates a hazardous operation and defaults to a safe state; a watchdog detects hangs.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A safety tactic is a design technique that keeps a system in control of recognized or accepted dangers, called hazards. The arc42 Quality Model tags these approaches with #safe.

The tagged approaches include:

- N-Version Redundancy and Voting
- Timeout
- Watchdog Supervision
- Fail-Safe Defaults
- Dead Man's Switch
- Safety Interlocks

**Safety interlocks.** An interlock puts an explicit gate in front of a hazardous operation. The gate checks preconditions before the operation may run. Its defining property is that it falls back to a safe state when it cannot allow the operation. Variants include the two-person rule and permit-to-work.

**Fail-safe defaults.** Interlocks and fail-safe defaults complement each other. An interlock checks preconditions before an operation. A fail-safe default decides where the system goes when something goes wrong.

**Watchdog supervision.** An independent monitor finds hung components and bounds recovery time. The monitor must run in a separate failure domain from the component it supervises.

Watchdog supervision is useful where an undetected hang is worse than a restart.

## Example

A packaging machine has a press that could injure an operator. An interlock checks that the guard is closed before the press may move. If the check cannot be confirmed, the press stays off. A watchdog on a separate controller watches the main control program. If that program hangs, the watchdog notices and triggers a restart.

## Trade-offs

A watchdog with too short a heartbeat interval causes false-positive restarts. This means the system restarts although nothing is wrong. The interval needs careful tuning.

A watchdog must run in a separate failure domain.
