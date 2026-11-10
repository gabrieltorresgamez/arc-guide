---
title: Heartbeat
slug: heartbeat
category: tactics
kind: tactic
summary: Heartbeat is an availability tactic for spotting failures. One component sends a message at regular
  intervals and another listens. If the messages stop, the listener assumes the sender failed and triggers
  fault correction.
arc42:
- 5
- 6
- 8
- 10
step: s07-solution-strategy
related:
- ping-echo
- availability-tactics-fault-detection
- availability
- availability-tactic
- exception-handling
- availability-tactics-fault-recovery
- architectural-tactic
checks:
- The document names which component sends the heartbeat and which component listens for it.
- 'The document states what happens when heartbeats stop: a fault correction component is notified.'
- The heartbeat interval is longer than the network round-trip time, and the failure timeout is a multiple
  of the interval.
- The document distinguishes heartbeat (monitored side initiates) from ping/echo (monitor initiates).
sources:
- url: https://people.ece.ubc.ca/matei/EECE417/BASS/ch05lev1sec2.html
  title: ''
  site: people.ece.ubc.ca
  accessed: '2026-11-08'
- url: https://martinfowler.com/articles/patterns-of-distributed-systems/heartbeat.html
  title: HeartBeat
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/patterns/conversation/HeartBeat.html
  title: Heartbeat - Enterprise Integration Patterns 2
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
  title: Configure Liveness, Readiness and Startup Probes | Kubernetes
  site: kubernetes.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: The monitored component sends heartbeats. When they stop, the listener notifies fault correction.
review:
  status: generated
  flags: []
---

## Explanation

Heartbeat is a way to detect that a component has failed. It is one of the fault detection tactics (see the article "Fault Detection Tactic").

**How it works.** One component, the monitored one, sends a small message at regular intervals. Another component listens for these messages. While they keep arriving, the listener assumes all is well. If the heartbeat stops, the listener assumes the sender has failed. It then notifies a fault correction component, which handles recovery.

**Who starts the exchange.** In a heartbeat, the monitored component starts the exchange. The listener only receives. This is the opposite of Ping/Echo. There, the monitor sends a ping and expects an echo from the monitored component within a set time.

**Where it sits among related tactics.** Exception detection works inside a single process. Heartbeat works across processes: one component watches another.

**The same idea in other catalogs.** Fowler's HeartBeat pattern has a server show it is available by periodically messaging the other servers. Enterprise Integration Patterns describes a heartbeat as a series of periodic messages showing that a component works well. An observer detects missing beats and raises alerts or takes corrective action.

**Choosing the timing.** In Fowler's HeartBeat pattern, the request interval is chosen to be longer than the network round-trip time between the servers. The failure timeout is then a multiple of that interval.

**A contrast in practice.** Kubernetes liveness probes check whether a container is in a broken state. If it is, the kubelet restarts the container. The probe frequency is set with periodSeconds.

## Example

An order service and a monitoring component run on separate machines. Every few seconds the order service sends a short "I am alive" message to the monitor. The monitor allows a few intervals of silence. When the silence lasts longer than that, the monitor assumes the order service has failed. It then notifies the component that handles recovery, for example by starting a replacement.

## Trade-offs

One concrete timing rule applies. The interval should exceed the network round-trip time, and the failure timeout should be a multiple of the interval.
