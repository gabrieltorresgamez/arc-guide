---
title: Client-to-Server Failover
slug: client-to-server-failover-in-bcs
category: tactics
kind: tactic
summary: Client-to-server failover names one backup node in advance. It mirrors the server's state and
  takes over if the server fails. Recovery time is the time needed to turn that backup into the new server.
arc42:
- 4
- 6
- 10
- 11
step: s11-evaluate
related:
- redundant-spare
- active-redundancy
- availability-tactics-fault-recovery
- battlefield-control-system-atam-case-study
- availability-scenario
- architectural-risk
- quantifying-recovery-and-availability-trade-offs
- availability
checks:
- The document names the Commander and the single backup node, and says the backup comes from the Soldier
  nodes.
- The document states how the backup stays in sync with the Commander, for example through acknowledged
  state messages.
- The document gives a switchover time or budget and checks it against the largest expected number of
  Soldiers.
- The document explains how a Commander failure is detected and how the other nodes learn of the takeover.
- The document states an availability requirement and addresses what happens after the backup is used
  up.
sources:
- url: https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf
  title: 'ATAM: Method for Architecture Evaluation'
  site: sei.cmu.edu
  accessed: '2026-11-10'
diagrams:
- file: diagram-1.mmd
  caption: The backup mirrors the Commander, then converts and informs the other Soldiers.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

**How evaluators probed it.** They asked how failures are identified and how long it takes to switch to the redundant component.

## Example

A small field team uses one coordinator device. A second, pre-selected device receives every update and confirms it. When the coordinator dies, a team member tells the second device to take over. It starts acting as coordinator and tells the other devices to talk to it.
