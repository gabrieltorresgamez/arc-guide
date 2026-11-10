---
title: Crosscutting Concept
slug: arc42-crosscutting-concepts
category: documentation
kind: concept
summary: A crosscutting concept is a practice, pattern, or rule that applies in several parts of a system.
  arc42 section 8 documents each one once, so the system stays consistent.
arc42:
- 8
- 4
- 5
step: s10-document
related:
- arc42-documentation-template
- arc42-solution-strategy
- arc42-architecture-decisions
- architectural-pattern
- architectural-style
- security
- separation-of-concerns
- component-view
checks:
- Section 8 contains only concepts that are relevant to the system, and they are grouped.
- Building blocks name the crosscutting concepts they apply, for example through a stereotype tag.
- The solution strategy stays brief and references section 8 for the how and why of approaches.
- Technical concepts are written for developers, with source code and short explanations where that suffices.
sources:
- url: https://docs.arc42.org/section-8/
  title: 8 - Concepts | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://arc42.org/overview/
  title: arc42 Template Overview - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-8-3/
  title: 'Question C-8-3: How shall I deal with the multitude of potentially crosscutting topics? | arc42
    FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-8-2/
  title: 'Question C-8-2: Our arc42 section 8 (on concepts) is a melting pot of information we couldn''t
    put elsewhere? How can we keep an overview? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-4-2/
  title: 'Question C-4-2: How to document the ''solution strategy''? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/8-11/
  title: 'Tip 8-11: (Hyper)Link between Building Blocks and Concepts! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Cross-cutting_concern
  title: Cross-cutting concern - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One concept applied in several building blocks
review:
  status: generated
  flags: []
---

## Explanation

Some decisions do not belong to one part of a system. They apply in many parts at once. Logging and security are typical examples. arc42 calls these **crosscutting concepts**. It describes them as practices, patterns, regulations, or solution ideas that often span several building blocks. (A building block is a part of the system, such as a module or component.)

**Where they live.** arc42 section 8 holds them. The arc42 overview describes this section as covering overarching, often very technical topics, such as technology choices and recurring patterns. The section grows as the team decides on more concepts.

**Why they matter.** Concepts give the architecture conceptual integrity. That means the system is consistent and homogeneous.

**Who reads them.** Many concepts are highly technical, so they are written for developers. Sometimes source code with a short explanation is enough. Long prose is not always needed.

**Choosing topics.** Treat section 8 as a checklist at first. Work iteratively and drop topics that do not matter for your system. To keep the section from becoming a melting pot, remove irrelevant concepts. Then group the rest.

**Links to other chapters.**
- The solution strategy (see the article *Solution Strategy*) stays brief. Section 8 explains the how and why of approaches. References connect the two.
- Building blocks should show which concepts they apply. One way is to tag a block with a concept name as a stereotype. A block can apply several concepts.

**Related idea.** Outside arc42, a cross-cutting concern is an aspect of a program that affects several modules. Logging and authentication are examples.

## Example

A team builds an online shop with three building blocks: Orders, Payments, and Catalog. All three need logging. Instead of explaining logging three times, the team writes one logging concept in section 8. It holds a short rule and a code snippet. Each of the three blocks is tagged with the concept name and points to it. The strategy chapter mentions logging in one line and links to the concept.

## Trade-offs

Documenting a concept in one central place avoids repeating it. It also takes effort to choose which topics belong in section 8. If the team keeps irrelevant topics, the section becomes a melting pot. Source code with brief notes is quick to write. Some concepts may still need more explanation than code alone gives.
