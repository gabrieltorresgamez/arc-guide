---
title: ATAM Roles
slug: atam-roles
category: evaluation
kind: concept
summary: 'An ATAM evaluation involves three groups: a small external evaluation team, project decision-makers
  who can mandate architectural changes, and broader stakeholders who join only in the second phase.'
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-evaluation-team-and-stakeholder-selection
- atam-application-phases
- atam-phase-1-and-2-activities
- stakeholder
- voting
- scenario-weight-assignment
- lightweight-atam
checks:
- The evaluation team has about 3-5 people, all external to the project.
- The decision-makers taking part have authority to mandate architectural changes.
- Broader stakeholders are scheduled for the second evaluation phase.
- Scenarios are brainstormed openly in step 7 and prioritized by voting.
sources:
- url: https://www.architectviewmaster.com/blog/architecture-tradeoff-analysis-picking-your-poison-carefully/
  title: 'Architecture Tradeoff Analysis: Picking Your Poison (Carefully) | Architect View Master'
  site: architectviewmaster.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Who joins which part of an ATAM evaluation
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

This article covers who takes part in an Architecture Tradeoff Analysis Method (ATAM) evaluation (see Architecture Tradeoff Analysis Method (ATAM)).

**The evaluation team.** This group has 3-5 people. They come from outside the project being evaluated.

**Project decision-makers.** These people have authority to mandate architectural changes.

**Other stakeholders.** A stakeholder is anyone with an interest in the system (see Stakeholder). Broader stakeholders join only in the second evaluation phase.

**Phases and steps.** ATAM has four phases and nine analysis steps. Phase 1 covers steps 1-6 and takes about a day. After a break, phase 2 covers steps 7-9 and takes about two days. Stakeholders join in phase 2.

**Scenarios.** In step 7, the group brainstorms scenarios in an open session. A scenario is a concrete, testable expression of a quality attribute, with a stimulus, an environment and a measurable response. The group then typically votes to prioritize them.

## Example

A company evaluates its new order system. Three outside experts form the evaluation team. The architect and the project manager, who can order changes, work with them in phase 1. In phase 2, support staff, operations staff and business users join. Together they brainstorm scenarios such as "orders double during a sale". Then they vote on which scenarios matter most.
