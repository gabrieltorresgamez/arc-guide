---
title: Architecturally Significant Requirement
slug: architecturally-significant-requirement
category: forces-decisions
kind: concept
summary: An architecturally significant requirement strongly shapes the architecture because it is hard
  to meet, costly to change later, or risky. Teams spot these with a qualitative seven-criterion test
  and keep a short list of about ten.
arc42:
- 1
- 4
- 9
- 10
- 11
step: s04-quality-requirements
related:
- architecturally-significant-decision
- quality-attribute-scenario
- arc42-quality-chapter
- last-responsible-moment
- architectural-trade-off-thinking
- quality-attribute-prioritization
- architectural-decision
- arc42-introduction-and-goals
checks:
- The document lists a small set of significant quality scenarios, roughly ten.
- Each significant quality scenario is specific and measurable.
- Each ASR is linked to business value or risk, or to a key stakeholder's concern.
- Decisions that are costly to reverse, such as the integration style, are made with early attention.
sources:
- url: https://ozimmer.ch/practices/2020/09/24/ASRTestECSADecisions.html
  title: Architectural Significance Criteria and Some Core Decisions Required
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=3128836&seqNum=3
  title: Quality Attributes | Why Software Architecture is Important and Essential Activities | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Not every requirement affects the architecture equally. Some can change late at little cost. Others lock in basic choices. These are architecturally significant requirements, or ASRs.

The same functionality can be built with different architectures. Each one has different quality strengths. So architects weigh trade-offs and pick the least-worst option. The requirements that force these trade-offs matter most.

**The seven-criterion test**

Zimmermann's ASR test has seven criteria. The first two are:

1. The requirement ties directly to high business value or business risk.
2. A key stakeholder, such as the project sponsor, cares about it.

Criteria 1 to 5 are fairly objective, so people agree on them more easily. Criterion 6 (first of its kind) and criterion 7 (past problems) depend on context and are subjective.

The test is qualitative. It is not a weighted scoring calculator. Relevance is always a judgment that depends on context.

**Beyond requirements**

The same test also works for design elements and architectural decisions. Most ASRs are non-functional, meaning they describe qualities such as speed. Some are functional.

**Keeping the list short**

Quality scenarios make a quality requirement concrete. arc42 says they should be specific and measurable. See Quality Attribute Scenario. Roughly ten scenarios is a manageable set for most systems. The significant ones affect the architecture most. They are typically driven by hard demands such as low latency or high scalability.

**Timing**

Decisions that are costly to reverse deserve earlier attention. The integration style is one example. Switching from one style to another is expensive. Zimmermann also warns against deciding too early, which harms flexibility. He advocates the most responsible moment: neither too early nor too late.

## Example

A team builds an online ticket shop. "Show the event list in a tidy table" is easy to change later. "Handle a sudden rush of buyers when popular tickets go on sale, with fast responses" is different. The sponsor cares about it, because lost sales hurt the business. It is hard to meet and costly to retrofit. The team marks it as an ASR and writes it as a measurable scenario. They then decide on the structure early enough to support it.

## Trade-offs

The test is qualitative, so two teams can rate the same requirement differently. The last two criteria are the most subjective. Deciding early protects against costly reversals but reduces flexibility. Deciding late can signal uncertainty or even fear, especially for big decisions. A list of about ten scenarios is manageable for most systems.
