---
title: Stakeholder Readiness for Change Assessment
slug: stakeholder-readiness-for-change-assessment
category: enterprise-architecture
kind: method
summary: A readiness assessment rates each stakeholder's understanding and commitment today against what
  the architecture work needs. The gap between the two levels shows where to focus effort.
arc42:
- 1
step: s01-goals-stakeholders
related:
- stakeholder-power-grid
- stakeholder-identification
- stakeholder
- togaf
- togaf-architecture-development-method
- stakeholder-concern
- resistance
checks:
- Each critical stakeholder has a current and a required commitment level, so the gap is visible.
- The stakeholder table uses H/M/L ratings and includes ability to disrupt, understanding, commitment
  and required support.
- The analysis was done in Phase A and is kept up to date in later phases.
- Informal stakeholder groups are considered, not only the formal organization.
sources:
- url: https://togaf.visual-paradigm.com/2025/01/21/comprehensive-guide-to-stakeholder-management-in-togaf-adm/
  title: Comprehensive Guide to Stakeholder Management in TOGAF ADM - Visual Paradigm
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Place of the readiness assessment in TOGAF stakeholder management
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A stakeholder readiness assessment is one step in TOGAF stakeholder management. TOGAF is a framework for enterprise architecture (see the article TOGAF). The process runs in this order:

1. Identify the key stakeholders of the enterprise architecture.
2. Classify their positions, which includes assessing each stakeholder's readiness.
3. Determine the management approach. A power/interest matrix helps choose how to engage each one (see Stakeholder Power Grid).
4. Tailor deliverables to the catalogs, matrices and diagrams the engagement needs.

**Two questions**

The readiness assessment asks several questions about each person, including these two:

- Is this person willing to change direction toward the Target Architecture, and how ready are they?
- Can this person be a credible advocate or agent of the architecture initiative?

**Current versus required commitment**

For each critical stakeholder, you judge two levels. One is the commitment today. The other is the commitment you want in the future.

**The table**

The stakeholder analysis table has these columns:

- ability to disrupt change
- current and required understanding
- current and required commitment
- required support

In one example row, the CIO has H disruption ability, L current commitment and M required commitment.

**When to do it**

Run the analysis in Phase A (Architecture Vision), where it identifies the key players. Keep it up to date through later phases. Look beyond the formal organization too. Informal groups can be just as powerful and influential.

## Example

A company plans to replace its order system. The architect lists three stakeholders and rates each one.

| Stakeholder | Ability to disrupt | Commitment now | Commitment required |
|---|---|---|---|
| CIO | H | L | M |
| Sales lead | M | M | M |
| Informal user group | M | L | M |

The CIO and the informal user group each show a gap between L and M. The sales lead shows none. The architect therefore plans extra engagement for the first two and leaves the sales lead as is.

## Trade-offs

The table needs updating through later phases.
