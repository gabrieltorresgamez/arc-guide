---
title: Utility Tree
slug: utility-tree
category: quality-attributes
kind: artifact
summary: A utility tree, also called a quality tree, breaks "quality" into topics and sub-topics. Concrete
  quality scenarios sit at the leaves. Empty branches show where scenarios are missing.
arc42:
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- arc42-quality-chapter
- iso-iec-25010-quality-model
- architecture-tradeoff-analysis-method-atam
- scenario-weight-assignment
- quality-attribute-prioritization
- atam-phase-1-architecture-centric-analysis
checks:
- The quality tree has quality as its root and refines it into areas or topics.
- Every leaf of the tree is a quality scenario.
- Each scenario names a stimulus, a response, and a measurable response measure.
- No major branch of the tree is empty, or each empty branch is explained.
- The tree starts from the ISO 25010:2023 quality model.
sources:
- url: https://faq.arc42.org/questions/C-10-3/
  title: 'Question C-10-3: What is a ''quality tree''? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/tips/10-4/
  title: 'Tip 10-4: Use the quality tree as checklist! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://faq.arc42.org/questions/C-10-2/
  title: 'Question C-10-2: What is a ''quality scenario''? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A small quality tree. The Security branch has no scenario yet, which hints at a gap.
review:
  status: generated
  flags: []
---

## Explanation

A utility tree organizes quality requirements as a hierarchy. The root is "quality". It splits into areas or topics, and those split again into finer topics. arc42 treats "quality tree" and "quality attribute utility tree" as the same idea. Section 10 of arc42 credits Bass et al. with the term "Quality Attribute Utility Tree".

**Leaves are scenarios.** The leaves of the tree are quality scenarios. A quality scenario describes one concrete situation. It has a stimulus event, a stimulated system, a response, and a response measure. The response measure is a metric, so the response can be checked. arc42 asks for scenarios that are specific and measurable.

arc42 groups scenarios into three kinds:

- usage scenarios
- change scenarios
- failure scenarios, where part of the system, its infrastructure, or its neighbors fails

**Where to start.** When using the tree as a checklist, arc42 suggests starting with something similar to the ISO 25010:2023 quality tree. See the article ISO/IEC 25010 Product Quality Model.

**Finding gaps.** A graphical tree makes it easier to spot gaps in the quality requirements. If a major branch has no scenarios, that may indicate missing scenarios.

**Where it fits in ATAM.** In the Architecture Tradeoff Analysis Method (ATAM), the utility tree is built in Phase 1, in step 5. Phase 2 covers steps 7-9 and finishes the evaluation.

## Example

A team starts with the root "quality". Under it they place "performance" and "availability". Under "availability" they add a sub-topic, "recovery after failure".

At the leaf they write one failure scenario. The database server stops (stimulus). The system switches to a standby copy (response). Service resumes within a stated number of seconds (response measure).

Later the team sees that the "security" branch has no leaves. That signals missing scenarios, so they write some.

## Trade-offs

Quality trees get cumbersome to maintain as the number of quality requirements grows. This limits the approach in practice.
