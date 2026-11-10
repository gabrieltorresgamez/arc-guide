---
title: Reduce Coupling
slug: reduce-coupling
category: tactics
kind: tactic
summary: Reduce Coupling is a group of modifiability tactics. They lower the dependencies between modules,
  so a change in one module breaks fewer of the others.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- coupling-and-cohesion
- increase-cohesion
- modifiability-tactics
- modifiability
- architectural-tactic
- loose-coupling
- information-hiding
- tactic-trade-off-balancing
checks:
- The document explains which modules depend on a module that is expected to change often.
- Similar dependencies on a common service are hidden behind one shared contract.
- The document states that the tactic is chosen to lower coupling between modules for modifiability.
sources:
- url: https://quality.arc42.org/approaches/reduce-coupling
  title: Reduce Coupling | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Several similar dependencies hidden behind one shared contract.
review:
  status: generated
  flags: []
---

## Explanation

Coupling describes how much modules depend on each other. When coupling is high, change is contagious. You touch one module, and the modules that depend on it break.

Increase Cohesion is a complementary lever to reducing coupling. See *Increase Cohesion* and *Coupling and Cohesion*.

A tactic is a design decision that affects how well an architecture reaches a quality goal. It does this by adjusting the parameters of a quality model. Tactics for modifiability build on three ideas: coupling, cohesion and cost. The Reduce Coupling tactics adjust the coupling parameter.

One concrete move is to abstract common services. Several modules may have similar dependencies. You hide them behind one shared contract. Dependents then rely on the contract and not on each separate dependency.

The goal is that a change stays local, so fewer modules feel it.

## Example

Three modules in a shop system each talk to a different notification service. Each module has its own way of calling it. Replacing one service forces edits in its module.

The team defines one shared contract for sending a notification. The three modules call only that contract. A single place maps the contract to each service. Now a change to one service touches that place and not the three modules.

## Trade-offs

Coupling, cohesion and cost motivations identify the parameters of interest for modifiability tactics. See *Choosing and Applying Tactics* and *Tactic Trade-off Balancing*.
