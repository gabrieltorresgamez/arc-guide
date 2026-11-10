---
title: Architectural Force
slug: architectural-forces
category: forces-decisions
kind: concept
summary: Forces are pressures that pull an architectural decision in different directions, such as deadlines,
  cost, skill, and change. Architects weigh them against each other. Constraints, by contrast, must be
  dealt with.
arc42:
- 2
- 9
step: s05-constraints
related:
- big-ball-of-mud
- requirements-versus-constraints
- arc42-constraints
- markdown-architectural-decision-records-madr
- keep-it-working
- architectural-decision-record
- concern
- technical-debt
checks:
- The decision record lists the forces and concerns that drove each decision, for example in a Decision
  Drivers section.
- The document separates constraints (which must be handled, though some are negotiable) from forces (which
  are weighed).
- The document states where the architects are free and where they are bound by constraints.
- Pattern or decision descriptions name the competing forces, such as maintenance needs versus risk of
  breaking the system.
sources:
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://adr.github.io/madr/
  title: About MADR | MADR
  site: adr.github.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Big Ball of Mud pattern (see its article) names several forces that push a system toward a tangled structure:

- **Time.** As a deadline nears, architectural concerns often give way to pragmatic ones.
- **Cost.** Architecture is expensive, especially when the team explores a new domain.
- **Skill.** Programmers differ in skill, expertise, predisposition, and temperament.
- **Visibility.** Only the people who build a program see its inside. Poor structure can go unnoticed.
- **Complexity.** Software often reflects the complexity of the problem area it serves.
- **Change.** The world defeats attempts to predict future requirements. Shortcuts follow.

arc42 defines constraints as requirements that limit the architect's design freedom. Constraints must always be handled, although they may be negotiable. arc42 also advises architects to know where they are free and where constraints bind them.

Decision records give forces a place to live. The MADR template (Markdown Architectural Decision Records) has a Decision Drivers section. Forces and concerns go there, so readers can see what pushed the decision.

## Example

A team must ship a booking tool before a trade fair. The deadline pushes toward quick shortcuts. The team is new to the travel domain, so careful design feels costly and risky. The team lists the deadline, the cost, and the unfamiliar domain as decision drivers in its decision record. Later readers can see why the team chose a simpler design and what it weighed.
