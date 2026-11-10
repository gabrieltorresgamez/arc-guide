---
title: Ping/Echo
slug: ping-echo
category: tactics
kind: tactic
summary: Ping/echo checks whether a component is alive. One part sends a request and waits for a reply.
  If no echo arrives within a set time, the sender declares a failure.
arc42:
- 8
- 7
- 10
step: s07-solution-strategy
related:
- availability-tactics-fault-detection
- heartbeat
- availability-tactic
- load-balancer
- request-reply
- synchronous-vs-asynchronous-communication
- availability
- architectural-tactic
checks:
- The document states how long a pinging component waits for an echo before declaring failure.
- Timeouts and failure thresholds are configured so transient failures such as network delays do not trigger
  unnecessary actions.
- The probe interval is balanced against probe overhead, especially across many instances.
- The document states whether health checks are shallow or also test downstream dependencies.
sources:
- url: https://hanfak.gitbook.io/workspace/general-paradigms/design-architecture-aims/quality-attributes/availability-2
  title: Availability | Learning
  site: hanfak.gitbook.io
  accessed: '2026-11-08'
- url: https://www.rfc-editor.org/info/rfc792/
  title: 'RFC 792: Internet Control Message Protocol | RFC Editor'
  site: rfc-editor.org
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring
  title: Health Endpoint Monitoring Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
  title: Liveness, Readiness, and Startup Probes | Kubernetes
  site: kubernetes.io
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: A monitor pings a service and declares failure when the echo does not arrive in time.
review:
  status: generated
  flags: []
---

## Explanation

Ping/echo is a way to detect faults. It is one of the fault detection tactics described in *Fault Detection Tactic*. One component sends a request to another. The receiver sends an echo back. The two messages form an asynchronous request/response pair (see *Synchronous vs. Asynchronous Communication*).

**What the echo tells you.** The echo shows that the target is alive and responding. It also shows whether the network path works and how long the round trip takes.

**The time threshold.** The sender must know how long to wait for the echo. When that time runs out with no reply, the sender declares a failure.

**Matching replies.** In the standard echo defined in RFC 792, the receiver returns the data from the request. It also returns an identifier and a sequence number. The sender uses these to match each reply to its request.

**Ping/echo versus heartbeat.** *Heartbeat* is a periodic exchange between a system monitor and the monitored process. The key difference is who starts the check. A monitor, in general, watches key components for malfunctions or network congestion.

**Shallow checks.** A shallow health endpoint check confirms only that the application process can respond. It does not contact downstream dependencies. A process that responds is not necessarily ready to serve.

**In practice.** Health endpoint monitoring uses external tools that probe an application at regular intervals. Load balancers and traffic routers use the results to send requests to healthy instances (see *Load Balancer*). Kubernetes liveness probes lead the kubelet to restart a container that fails more often than allowed. Readiness probes decide whether a Pod receives traffic.

## Example

A monitoring tool sends a small request to an order service. The service answers. The tool records the reply and moves on. Later the service stops answering. The tool waits for the configured time, then declares the service failed. A load balancer stops sending customers to that instance.

## Trade-offs

- **Probe cost.** Probes add traffic. At high frequency across many instances, the overhead can measurably slow the application. Balance the probe interval against how fast you need to detect failures.
- **Shallow answers.** A shallow health check confirms only that the process can respond. It does not contact downstream dependencies.
