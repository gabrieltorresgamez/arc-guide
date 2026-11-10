---
title: Energy Efficiency Tactic
slug: energy-efficiency-tactics
category: tactics
kind: tactic
summary: Energy efficiency tactics are design moves that cut the energy software uses while it still does
  its job. They help you measure energy use, schedule work well across resources, and reduce the work
  each event causes.
arc42:
- 4
- 8
- 10
step: s07-solution-strategy
related:
- architectural-tactic
- performance-tactics
- tactic-trade-off-balancing
- quality-attribute
- performance-efficiency
- choosing-and-applying-tactics
- maintainability
checks:
- The document states how energy consumption is monitored for the workloads being optimized.
- Energy-saving tactics are listed together with their impact on other quality attributes, such as response
  time.
- Where per-event processing is reduced, the maintenance cost of the added code is acknowledged.
sources:
- url: https://s2group.cs.vu.nl/AwesomeAndDarkTactics/tactics/2022-04-20-automatically-monitor-efficiency
  title: Automatically monitor efficiency per workload | Awesome and Dark Tactics
  site: s2group.cs.vu.nl
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/computational-overhead-reduction
  title: Computational Overhead Reduction | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://s2group.cs.vu.nl/AwesomeAndDarkTactics/tactics/2025-08-17-implement-resource-aware-job-scheduling
  title: Implement Resource-Aware Job Scheduling | Awesome and Dark Tactics
  site: s2group.cs.vu.nl
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2501.14402
  title: 'On the Effectiveness of Microservices Tactics and Patterns to Reduce Energy Consumption: An
    Experimental Study on Trade-Offs'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The three groups of energy efficiency tactics, with examples.
review:
  status: generated
  flags: []
---

## Explanation

An energy efficiency tactic is a design choice that lowers energy use. (See Architectural Tactic for the general idea of a tactic.)

**Monitoring resources.** You cannot optimize what you cannot measure. Monitoring energy consumption is a prerequisite for making a workload more energy efficient. Automatic monitoring also gives insight into how the software behaves. That insight supports later optimization.

**Allocating resources.** Allocation tactics decide how work is spread over resources. Resource-aware job scheduling is one example. It accounts for several resources, such as memory, CPU, network bandwidth, and energy, and prioritizes or migrates jobs based on resource utilization. Combined with resource monitoring, this can keep idle time and wasted energy low.

**Reducing resource demand.** Reducing computational overhead is one approach. It cuts the processing done per event, so each event finishes faster with fewer processor cycles. Less computation per event draws less power. That lowers the energy spent per unit of work.

## Example

A team runs a nightly batch of report jobs on a few servers. First, they measure the energy each job uses, to find the costly ones (monitoring). Next, they schedule jobs so that servers do not sit idle between runs (allocating). Last, they remove repeated calculations in the heaviest job, so each record needs less processing (reducing demand).

## Trade-offs

Saving energy can cost something else. The real challenge is to achieve energy efficiency, not simply to reduce energy consumption. Reducing computational overhead can also cost maintainability. Memoization (reusing earlier results) and tuned loops add code that the team must understand and preserve.
