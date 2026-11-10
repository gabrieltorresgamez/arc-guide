---
title: ATAM Evaluation Team and Stakeholder Selection
slug: atam-evaluation-team-and-stakeholder-selection
category: evaluation
kind: practice
summary: An ATAM evaluation needs an external evaluation team and a group of stakeholders. Both are chosen
  and briefed before analysis starts. The stakeholders supply the scenarios that drive the analysis.
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-roles
- atam-application-phases
- stakeholder
- stakeholder-identification
- voting
- scenario-weight-assignment
- lightweight-atam
checks:
- The evaluation team is external to the project and has three to five members.
- 'Team roles are assigned: evaluation leader, scribes, timekeeper and questioners.'
- A stakeholder list was arranged between the evaluation team and key decision makers during Phase 0.
- The evaluation leader explained the method to all participants before analysis.
- Scenarios from all stakeholders were prioritized by a vote of the whole stakeholder group.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.architectviewmaster.com/blog/architecture-tradeoff-analysis-picking-your-poison-carefully/
  title: 'Architecture Tradeoff Analysis: Picking Your Poison (Carefully) | Architect View Master'
  site: architectviewmaster.com
  accessed: '2026-11-09'
- url: https://concisesoftware.com/blog/architecture-tradeoff-analysis-method-atam/
  title: What is ATAM? Here is the explanation ▷▷ ConciseBlog
  site: concisesoftware.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Who takes part, and when, in an ATAM evaluation
review:
  status: generated
  flags: []
---

## Explanation

An ATAM evaluation (see Architecture Tradeoff Analysis Method (ATAM)) brings together a trained evaluation team, the architects, and representatives of the architecture's stakeholders. A stakeholder is anyone with an interest in the system (see Stakeholder). The evaluation typically lasts three to four days.

**The evaluation team**

The evaluation team is external to the project. It has three to five members. Its roles include:

- a leader who runs the evaluation,
- scribes who record the scenarios,
- a scribe who keeps the minutes,
- a timekeeper,
- people who ask questions.

**The stakeholders**

Stakeholders are a separate group from the evaluation team. They are brought in at Phase 2, where a wider group brainstorms scenarios in an open session. A scenario is a short description of a situation the system must handle (see Quality Attribute Scenario). The scenarios from all stakeholders are then prioritized by a vote of the entire stakeholder group (see Voting).

**Preparation**

Selection happens before the analysis. In Phase 0, the evaluation team and key project decision makers meet informally. They arrange logistics, such as the stakeholder lists. This preparation can run over a few weeks.

Education comes next. The evaluation leader describes the method to the assembled participants, so everyone knows how the evaluation works before analysis begins.

Who is in the room shapes which scenarios appear and which ones get votes.

## Example

A company plans to evaluate the architecture of a new order platform. Two weeks ahead, an outside team of four meets the project's decision makers. Together they draft the list of people to invite. On day one, the evaluation leader explains the method to everyone. Later, the invited group brainstorms scenarios and votes on which matter most.

## Trade-offs

The evaluation takes three to four days. An external team brings distance from the design. It also needs weeks of informal preparation with the project's decision makers before the evaluation starts.
