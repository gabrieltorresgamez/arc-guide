---
title: Quality Attribute Prioritization
slug: quality-attribute-prioritization
category: quality-attributes
kind: practice
summary: Teams cannot maximize every quality at once, so they pick the few that matter most and rank them.
  arc42 asks for the top three, at most five, shown with concrete scenarios.
arc42:
- 1
- 10
step: s04-quality-requirements
related:
- quality-attribute
- arc42-introduction-and-goals
- arc42-quality-chapter
- quality-attribute-scenario
- architectural-trade-off-thinking
- iso-iec-25010-quality-model
checks:
- The introduction lists only the top three quality goals, and no more than five.
- The quality goals appear as a table ordered by priority.
- Each top quality goal has at least one concrete scenario.
- Lesser-importance quality requirements sit in section 10, which references the top goals from section
  1.2.
sources:
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Quality prioritization means choosing which qualities of a system matter most and putting them in order. Examples of qualities are speed, security, or ease of change. Each one is a quality attribute (see the article Quality Attribute).

arc42 is a template for documenting architecture. It sets a clear limit: the introduction lists only the top three quality goals, and at most five. Its tips repeat the point: describe only the top 3-5 quality goals in the introduction.

The goals appear as a table ordered by priority. Each goal comes with concrete scenarios. A scenario is a specific situation that shows what "good enough" means for that goal.

Lower-ranked qualities do not disappear. Section 10 of arc42 holds requirements of lesser importance. Missing them would not create high risks. The most important ones already sit in section 1.2, and section 10 refers to them.

## Example

A team builds an online ticket shop. Its introduction lists three quality goals in a ranked table. First, the shop stays available during a big sale. Second, customers pay securely. Third, new payment methods are easy to add. Each row has a scenario describing a concrete situation. Smaller wishes, such as a polished admin screen, go into the quality requirements section.

## Trade-offs

Lower-priority qualities stay documented in section 10, so they remain visible.
