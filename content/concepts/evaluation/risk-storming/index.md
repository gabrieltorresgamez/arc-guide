---
title: Risk Storming
slug: risk-storming
category: evaluation
kind: method
summary: Risk storming is a quick, collaborative way to find and show risks in an architecture. The team
  rates each risk by probability and impact, then tackles the highest-priority ones first.
arc42:
- 11
step: s11-evaluate
related:
- c4-model
- software-architecture-evaluation
- architecture-tradeoff-analysis-method-atam
- technical-debt
- risk-identification
- lightweight-atam
checks:
- Each identified risk has a probability and an impact rating, on a low/medium/high or numeric scale.
- The risk list is ordered by priority.
- Each high-priority risk has a mitigation measure, with tasks assigned and scheduled.
sources:
- url: https://riskstorming.com
  title: Risk-storming
  site: riskstorming.com
  accessed: '2026-11-09'
- url: https://icepanel.io/blog/risk-storming
  title: Risk storming
  site: icepanel.io
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-11/
  title: 11 - Risks and technical debt | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Generic risk storming flow
review:
  status: generated
  flags: []
---

## Explanation

Risk storming is a quick technique for identifying and visualizing risks together as a group. Simon Brown created it.

The team works from architecture diagrams. The method recommends the C4 model for these (see the article C4 Model).

**Rating risks**

Each risk gets two ratings: how likely it is (probability) and how bad it would be (impact). A rating can be low, medium or high. It can also be a number, such as 1-3 or 1-5.

**Prioritizing and acting**

The ratings let the team rank the risks. The team then works on the highest-priority risks first.

Mitigation means reducing a risk. Examples are training sessions, refactoring and new processes. Each task gets an owner and a schedule.

**Link to arc42**

Section 11 of arc42 holds a list of technical risks and technical debts, ordered by priority. It also suggests listing measures to minimize, mitigate or avoid each risk.

## Example

A team draws a C4 diagram of an online shop. Each member marks the spots that worry them. Several people mark the connection to the payment provider. The team rates it medium probability and high impact, and ranks it near the top. They schedule a task to reduce the risk. The risk and its planned measure go into the risk list.

## Trade-offs

The sources describe risk storming as quick. They say little about how deep it goes, so look at other evaluation methods if you need more depth.
