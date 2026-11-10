---
title: Graceful Degradation
slug: graceful-degradation
category: tactics
kind: tactic
summary: Graceful degradation keeps a system's most important functions working when parts fail. It drops
  or reduces less important features instead of failing completely.
arc42:
- 4
- 6
- 8
- 10
step: s07-solution-strategy
related:
- availability-tactic
- circuit-breaker
- availability-tactics-fault-recovery
- availability
- architectural-tactic
- fault-tolerance
- availability-scenario
- choosing-and-applying-tactics
checks:
- Features are ranked by criticality, with a core set that must stay up and optional features that can
  pause.
- The business has agreed which function is core when not all requirements can be met.
- Each degradable feature has a documented fallback path, health signal and re-enable logic.
- Fallback paths are tested and are much simpler than the primary path.
- The degraded state is communicated to users and operations, for example through a notice and alerts.
sources:
- url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html
  title: REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft
    dependencies - Reliability Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/approaches/feature-degradation
  title: Feature Degradation | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/throttling
  title: Throttling Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
  title: Circuit Breaker Pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/articles/feature-toggles.html
  title: Feature Toggles (aka Feature Flags)
  site: martinfowler.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: 'Degradation flow: core features keep running, optional ones pause until recovery.'
review:
  status: generated
  flags: []
---

## Explanation

Graceful degradation is an availability tactic. Availability means the system stays usable (see the article Availability). This tactic improves availability of the whole system. It preserves the most important functions during failures.

**Core idea.** When a dependency becomes unavailable, a component keeps doing its core job. It may serve slightly stale data, alternate data, or even no data. A local failure then hurts the system as little as possible.

**Rank features first.** The tactic needs features ranked by criticality. A core set must stay up. Optional features can pause. Deciding what counts as core is a business discussion as much as a technical one. For example, the business may have to weigh consistency against availability.

**What degradation looks like.**
- Show the rest of a page when one upstream system fails, instead of an error page.
- Turn off or reduce nonessential features so essential ones keep resources. A video app can drop to a lower resolution. This trades completeness for availability.
- Return default or cached responses and tell users that some data is temporarily unavailable.
- Suspend a less critical feature under load, then re-enable it when usage drops.

**Related mechanisms.** arc42 separates three ideas:
- Feature degradation drops whole features.
- Load shedding and rate limiting drop requests by priority.
- A circuit breaker cuts off one failing dependency. Feature degradation decides what users still see afterward.

A circuit breaker can trigger graceful degradation. Pair it with automatic recovery so the system heals itself. Alerts can notify operations. Operators can also disable non-vital functions by hand with a kill switch, which works like a manually operated circuit breaker.

**Testing.** Degradation requirements can be tested and verified. The paths taken during a failure must be tested.

## Example

An online shop's product page depends on a recommendations service. The service goes down. The page still shows the product, price and buy button. The recommendations area shows a short notice or cached suggestions. Buying keeps working. When the service returns, the area switches back on.

## Trade-offs

Degradation adds work. Each degradable feature needs a fallback path, a health signal, and logic to re-enable it. Fallback paths must be tested and be much simpler than the primary path. AWS also cautions that fallback strategies should generally be avoided.

Users may read a missing feature as a bug unless the system signals the degraded state. Cached or default values can also diverge from the real ones.

AWS lists common mistakes:
- Not identifying the core business functionality.
- Not testing components during dependency failures.
- Serving no data when partial results are possible.
