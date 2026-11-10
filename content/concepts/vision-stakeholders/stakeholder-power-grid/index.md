---
title: Stakeholder Power Grid
slug: stakeholder-power-grid
category: vision-stakeholders
kind: method
summary: The stakeholder power grid sorts stakeholders by their power over a project and their interest
  in it. The position on the grid tells you how closely to engage each group.
arc42:
- 1
step: s01-goals-stakeholders
related:
- stakeholder
- stakeholder-identification
- stakeholder-concern
- stakeholder-readiness-for-change-assessment
- togaf
- togaf-architecture-development-method
- raci-matrix
- arc42-introduction-and-goals
checks:
- The main stakeholders are identified and listed.
- Each stakeholder's power to affect the project, positively or negatively, is assessed.
- High-power, high-interest stakeholders are named as key players and engaged closely.
- High-power stakeholders with low interest are kept satisfied.
- A Communications Plan reflects the grid, with regular updates for low-power, high-interest stakeholders.
sources:
- url: https://www.nngroup.com/articles/stakeholder-analysis/
  title: Stakeholder Analysis for UX Projects - NN/G
  site: nngroup.com
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/guide/togaf/how-to-perform-togaf-stakeholder-management/
  title: How to Perform Stakeholder Management in TOGAF?
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://mutomorro.com/tools/mendelow-power-interest-matrix
  title: Mendelow power-interest matrix - guide and worked example | Mutomorro
  site: mutomorro.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Example placement of three stakeholders on a power-interest grid.
review:
  status: generated
  flags: []
---

## Explanation

The stakeholder power grid is also called Mendelow's Matrix or the power-interest matrix. Its earliest version is attributed to the researcher Aubrey Mendelow. In TOGAF, stakeholder management uses the grid. Phase A is where you identify the key players in the engagement. A stakeholder is anyone with a stake in the work (see the article Stakeholder).

**How to build the grid**

1. Identify the main enterprise architecture stakeholders. This is the first task. The article Stakeholder Identification goes deeper.
2. Assess each stakeholder's power. This means judging their potential to affect the project, for better or for worse.
3. Place each stakeholder on the grid by power and by interest.
4. Use the position to decide how to engage and communicate.

**What each position means**

- **High power, high interest (top right):** These stakeholders care about the project and strongly shape its outcome. Manage them closely. You must fully engage them and work hard to satisfy them.
- **High power, low interest:** They are not interested right now. They can still greatly affect the project. Keep them satisfied.
- **Low power, high interest:** They care about the project but have little power over it. Keep them informed. Give them regular updates. Treat them as allies and early signals.
- **Low power, low interest:** This article gives no advice for this group.

**From grid to communication**

Sending targeted information to the right stakeholders at the right time is a success factor. The grid output feeds a Communications Plan.

## Example

A team plans to replace an internal ordering system. The architect lists the stakeholders and places them on the grid.

- The sales director has high power and high interest. The architect manages them closely.
- The finance director has high power but no current interest. The architect keeps them satisfied, because they could greatly affect the project.
- The customer support team has little power but high interest. The architect sends them regular updates and treats them as allies and early signals.

The architect then writes these choices into a Communications Plan.

## Trade-offs

The grid is only as good as the judgments behind it. Power and interest are assessed by people, and a stakeholder's interest can change. A group that is not interested now can still hurt the project, so the placement needs a second look from time to time.
