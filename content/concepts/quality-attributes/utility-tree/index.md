---
title: Utility Tree
slug: utility-tree
order: 50
category: quality-attributes
kind: artifact
summary: A utility tree, also called a quality tree, breaks "quality" into topics and sub-topics. Concrete
  quality scenarios sit at the leaves. Empty branches show where scenarios are missing.
arc42:
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- arc42-quality-requirements
- iso-iec-25010-product-quality-model
- architecture-tradeoff-analysis-method-atam
- quality-attribute-prioritization
checks:
- The quality tree has quality as its root and refines it into areas or topics.
- Every leaf of the tree is a quality scenario.
- Each scenario names a stimulus, a response, and a measurable response measure.
- No major branch of the tree is empty, or each empty branch is explained.
- The tree starts from the ISO 25010:2023 quality model.
- Each leaf scenario is rated for importance and difficulty (H, M or L), and the (H,H) leaves are analyzed first.
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
- url: https://arnon.me/2010/05/utility-trees-hatching-quality-attributes/
  title: Utility Trees - Hatching quality attributes
  site: arnon.me
  accessed: '2026-11-17'
- url: https://dmccreary.github.io/atam/chapters/07-utility-trees-prioritization/
  title: Utility Trees and Prioritization - Architecture Tradeoff Analysis Methodology
  site: dmccreary.github.io
  accessed: '2026-11-17'
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

**Where to start.** When using the tree as a checklist, arc42 suggests starting with something similar to the ISO 25010:2023 quality tree [src:2]. See the article ISO/IEC 25010 Product Quality Model.

**Finding gaps.** A graphical tree makes it easier to spot gaps in the quality requirements. If a major branch has no scenarios, that may indicate missing scenarios.

**Where it fits in ATAM.** In the Architecture Tradeoff Analysis Method (ATAM), the utility tree is built in Phase 1, in step 5. Phase 2 covers steps 7-9 and finishes the evaluation.

**Ranking the leaves.** In ATAM, each leaf scenario gets two ratings, each High (H), Medium (M) or Low (L). *Importance* says how much the stakeholders care that the system achieves the scenario. It is a business judgment. *Difficulty* says how hard the current architecture makes it to meet the scenario's response measure. It is a technical judgment by the evaluators together with the architects. The pair is written as (importance, difficulty), for example (H,M). The ratings give a priority order: (H,H) scenarios get the deepest analysis, and (H,M) and (M,H) scenarios come next.

## Example

A team starts with the root "quality". Under it they place "performance" and "availability". Under "availability" they add a sub-topic, "recovery after failure".

At the leaf they write one failure scenario. The database server stops (stimulus). The system switches to a standby copy (response). Service resumes within a stated number of seconds (response measure). The team rates this leaf (H,M): very important, and moderately hard with the current design.

Later the team sees that the "security" branch has no leaves. That signals missing scenarios, so they write some.

## Trade-offs

Quality trees get cumbersome to maintain as the number of quality requirements grows. This limits the approach in practice.
