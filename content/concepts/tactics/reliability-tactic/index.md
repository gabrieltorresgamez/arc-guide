---
title: Reliability Tactic
slug: reliability-tactic
order: 30
category: tactics
kind: tactic
summary: 'Reliability tactics are design measures that keep faults from turning into failures. They are the availability tactics of the SEI catalog, and availability is a subcharacteristic of reliability in ISO/IEC 25010. They fall into three groups: detecting faults, recovering from faults, and preventing faults.'
long_ok: true
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- reliability
- architectural-tactic
checks:
- The document names which availability tactics it uses and groups them as detecting, recovering from
  or preventing faults.
- Calls between services use timeouts, so clients do not block forever.
- Where a remote call may fail, a fallback such as cached data or a default value is defined.
- Calls to unreliable dependencies are protected by a circuit breaker that fails fast after a failure
  threshold.
- The document states which critical functions stay running when components fail, and which are dropped.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=4
  title: 3.4 Design Concepts to Support Availability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/realizing-and-refining-architectural-tactics-availability/
  title: 'Realizing and Refining Architectural Tactics: Availability | CMU Software Engineering Institute'
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies
  title: Strategies for handling partial failure - .NET | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/CircuitBreaker.html
  title: Circuit Breaker
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/approaches/standby-failover
  title: Standby/Failover | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/watchdog-supervision
  title: Watchdog Supervision | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/n-version-redundancy
  title: N-Version Redundancy and Voting | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/feature-degradation
  title: Feature Degradation | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/circuit-breaker
  title: Circuit Breaker | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/timeout
  title: Timeout | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-16'
- url: https://en.wikipedia.org/wiki/Triple_modular_redundancy
  title: Triple modular redundancy - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/ACID
  title: ACID - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/blog/tactics-and-patterns-for-software-robustness/
  title: Tactics and Patterns for Software Robustness | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead
  title: "Bulkhead pattern - Azure Architecture Center | Microsoft Learn"
  site: learn.microsoft.com
  accessed: '2026-11-16'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/retry
  title: "Retry pattern - Azure Architecture Center | Microsoft Learn"
  site: learn.microsoft.com
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/bulkheads
  title: "Bulkheads | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/quarantine
  title: "Quarantine | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/dead-mans-switch
  title: "Dead Man\u2019s Switch | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/data-replication
  title: "Data Replication | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams:
- file: diagram-1.mmd
  caption: The three categories of availability tactics, with examples.
review:
  status: generated
  flags: []
---

## Explanation

A **fault** is a potential cause of a failure. A **failure** happens when the system no longer delivers service that matches its specification (the description of what it must do). Availability tactics work on faults, so that faults do not become failures. In ISO/IEC 25010, availability is a subcharacteristic of reliability.

The catalog has three categories:

- **Detect faults.** Find out that something is wrong.
- **Recover from faults.** Get back to correct service.
- **Prevent faults.** Act before a fault can cause harm.

**Detect faults**

- *Monitor*: a separate component watches the health of other parts of the system.
- *Ping/echo*: one node sends an asynchronous request to another and waits for a reply. This checks that the node is reachable and shows the round-trip delay.
- *Heartbeat*: a monitor and a watched process exchange messages at regular intervals.
- *Time stamp*: detects events that arrive in the wrong order, mainly in distributed systems that pass messages.
- *Condition monitoring*: the system checks conditions in a process or device, and that assumptions made at design time still hold.
- *Voting*: replicated components do the same work, and the system checks that their results agree. Triple modular redundancy is one case.
- *Exception detection*: the system notices a condition that changes the normal flow of execution.

**Recover from faults**

- *Retry*: repeat an operation. This can succeed when the failure is transient, meaning it passes on its own.
- *Redundant spare*: a duplicate component steps in and takes over if the primary component fails.
- *Exception handling*: once the system detects an exception, it must deal with it in some way.
- *Graceful degradation*: keep the most critical functions running during component failures by dropping less critical ones.
- *Rollback*: go back to a state known to be good.
- *Escalating restart*: the system recovers by changing how much it restarts, a small part or a larger one.
- *In-service software upgrade*: replace executable code images without disrupting service.
- *State resynchronization*: a reintroduction tactic that partners with active and passive redundancy.

**Prevent faults**

- *Removal from service*: take a component out of service for a while to reduce the chance of failures.
- *Transactions*: related state updates are bundled together, so that messages exchanged between components are atomic, consistent, isolated and durable.
- *Predictive model*: the system monitors the state of a process and takes corrective action if conditions point to likely future faults.
- *Exception prevention*: the system stops exceptions from occurring in the first place, for example by masking a fault.
- *Increasing the competence set*: a component is designed to handle more fault cases as part of its normal operation.

**Microservice tactics.** Microsoft's guidance for microservices lists these measures against partial failure:

- asynchronous messaging
- retries with backoff
- timeouts
- circuit breakers
- fallbacks
- bulkhead limits

A *timeout* keeps a client from blocking forever and tying up resources. A *fallback* lets the client return something else, such as cached data or a default value, when a request fails. A *circuit breaker* wraps a protected call and watches it for failures. After a threshold, it trips, and later calls fail fast without invoking the protected call.

A *bulkhead* isolates the elements of an application into pools, so that if one element fails, the others keep working. The name comes from the sectioned partitions of a ship's hull. Without it, excessive load or failure in one service affects all of its consumers, and a consumer that calls an unresponsive service can use up its own resources.

**Idempotency and retries.** An operation is idempotent when retrying it is inherently safe. If it is not, a retry can run the operation more than once, with unintended side effects. For example, a service may process a request but fail to send the response, and the retry logic then sends the request again. Check whether an operation is idempotent before you add retries.

The catalog has been used in academia and industry for several years. That use motivated a refinement of it.

**More tactics in the arc42 quality model.** The arc42 quality model has its own approach pages on related ideas: [Standby/Failover](https://quality.arc42.org/approaches/standby-failover), [Watchdog Supervision](https://quality.arc42.org/approaches/watchdog-supervision), [N-Version Redundancy and Voting](https://quality.arc42.org/approaches/n-version-redundancy), [Feature Degradation](https://quality.arc42.org/approaches/feature-degradation), [Circuit Breaker](https://quality.arc42.org/approaches/circuit-breaker), [Timeout](https://quality.arc42.org/approaches/timeout).

**Further approaches in the arc42 quality model.** The arc42 quality model has more approach pages on related ideas: [Bulkheads](https://quality.arc42.org/approaches/bulkheads), [Quarantine](https://quality.arc42.org/approaches/quarantine), [Dead Man’s Switch](https://quality.arc42.org/approaches/dead-mans-switch), [Data Replication](https://quality.arc42.org/approaches/data-replication).

## Example

An online shop shows product recommendations from a separate service. A heartbeat tells the shop that the recommendation service has stopped. A timeout stops product pages from hanging while they wait. A circuit breaker then trips, and the shop returns a default list of popular items as a fallback. The checkout, the most critical function, keeps working. Rollback and retry would apply to other parts of the shop, for example when an order update fails halfway.

## Trade-offs

The catalog is a set of options grouped by purpose. Each tactic addresses one part of the problem: detecting, recovering or preventing.
