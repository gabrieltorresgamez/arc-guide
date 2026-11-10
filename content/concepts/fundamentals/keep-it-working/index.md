---
title: Keep It Working
slug: keep-it-working
category: fundamentals
kind: pattern
summary: Keep It Working means changing software in small, safe steps so a working version always exists.
  It suits systems that need maintenance but would be risky to overhaul in one go.
arc42:
- 4
- 9
- 11
step: s12-evolve
related:
- big-ball-of-mud
- refactoring
- technical-debt
- sweeping-it-under-the-rug
- iterative-and-incremental-development
- incrementality
- architecture-decay
- risk-identification
checks:
- The document says the system must stay available while it is modernized, because the business depends
  on it and its data.
- Changes are made in small steps and integrated often, rather than in one late big-bang integration.
- Changes that break the running system are rejected immediately, for example through regular builds.
- Large replacements are built on the side or one small component at a time, not all at once.
sources:
- url: https://www.laputan.org/mud/mud.html
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/StranglerFigApplication.html
  title: Strangler Fig
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Small steps with immediate feedback keep a working version available.
review:
  status: generated
  flags: []
---

## Explanation

Keep It Working is a strategy that encourages a system's growth once the system is working.

**The city analogy.** A flood, fire, or war may require a city to be rebuilt from the ground up, but more often change happens a building or a block at a time, while the city as a whole keeps functioning. Software can change the same way.

**A separate, related idea.** Martin Fowler describes the strangler fig approach to legacy modernization, which prefers gradual modernization over simple replacement, a plan he says has gone down in flames most of the time. It replaces small, isolated components one at a time. Because each component is small, introducing new software carries less risk.

## Example

A company runs an old order system that needs cleanup. Instead of replacing it all at once, the team replaces the invoice component alone. Orders keep flowing throughout. The team then moves on to the next small component.
