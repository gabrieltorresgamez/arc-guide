---
title: Active Reviews for Intermediate Designs (ARID)
slug: active-reviews-for-intermediate-designs-arid
category: evaluation
kind: method
summary: ARID is a review for a design that is finer than a full architecture and not yet fully documented.
  It shows the design to the programmers who will use it and collects design issues early.
arc42:
- 11
- 9
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- lightweight-atam
- software-architecture-evaluation
- voting
- lightweight-approach-for-software-reviews-lasr
- software-architecture-analysis-method-saam
- quality-attribute
- advantages-and-drawbacks-of-atam
checks:
- The design under review is finer-grained than an architecture and not yet completely documented.
- Application programmers who will use the design are involved in the review before the detailed specification
  is fixed.
- The review result is a list of design issues, and the method used brainstorming and voting.
sources:
- url: https://www.sei.cmu.edu/library/active-reviews-for-intermediate-designs/
  title: Active Reviews for Intermediate Designs | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8838159/
  title: 'Lightweight Software Architecture Evaluation for Industry: A Comprehensive Review - PMC'
  site: pmc.ncbi.nlm.nih.gov
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Active_reviews_for_intermediate_designs
  title: Active reviews for intermediate designs - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Some designs are more detailed than an architecture but too early to have complete documentation. ARID reviews exactly this kind of design. It sits between architecture evaluation and the review of a detailed design specification. 

The review shows the design to its user community. These are the application programmers who will build on it. They give feedback before the design is locked into a detailed specification.

For more on ranking ideas as a group, see the article on Voting.

Wikipedia describes ARID as a method for evaluating architectures at an intermediate level.

A review of lightweight architecture evaluation methods lists ARID as a lightweight method. For a broader method, see Architecture Tradeoff Analysis Method (ATAM).

## Example

A team has sketched the interface of a new notification component. No full architecture document exists yet. The team invites the programmers who will call the component. Together they brainstorm and vote on the usage situations that matter most. The programmers then judge whether the design fits those situations. The review ends with a list of design issues. The team fixes them before writing the detailed specification.

## Trade-offs

**Benefits:** ARID suits designs that are not yet completely documented. It gives early feedback from the people who will use the design.


