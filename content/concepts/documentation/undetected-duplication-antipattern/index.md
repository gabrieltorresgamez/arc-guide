---
title: Undetected Duplication Antipattern
slug: undetected-duplication-antipattern
category: documentation
kind: concept
summary: The same function or element is listed twice in one overview, and nobody notices. The remedy
  is to describe each element once, where it is handled, and have other places point to that description.
arc42:
- 5
- 3
- 8
step: s10-document
related:
- architectural-overview-antipatterns
- arc42-crosscutting-concepts
- context-view
- arc42-documentation-template
- guidelines-for-documentation
- unclear-level-of-abstraction-antipattern
- coupling-and-cohesion
- characteristics-of-a-good-view
checks:
- Each interface or element is described in detail in only one place, and other occurrences reference
  it.
- Elements shown in the context view have a short name and business relevance, with detail kept elsewhere.
- Recurring substructures across refinements are factored into a crosscutting concept instead of repeated.
- Each piece of knowledge in the documentation has a single authoritative representation.
sources:
- url: https://faq.arc42.org/questions/C-5-10/
  title: 'Question C-5-10: How can I avoid redundancy with interfaces in the building block view? | arc42
    FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Don't_repeat_yourself
  title: Don't repeat yourself - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-10/
  title: 'Tip 5-10: Use crosscutting concepts to describe or specify similarities in building blocks!
    | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Documentation can describe the same thing in more than one place. The arc42 template (see arc42 Architecture Documentation Template) takes this seriously. Its guidance asks how to avoid documenting or specifying the same interface redundantly at several places in the building block view. It also says near-identical repeated refinements, meaning more detailed breakdowns of a building block, are too much redundancy.

**Remedies**

- **Describe once, reference elsewhere.** Give the detailed description only where the element is actually handled. At every other occurrence, add a reference to that description.
- **Keep other occurrences short.** In the context view, give the element a short, fitting name and its business relevance. Keep the detail elsewhere. See Context View.
- **Factor out repeated structures.** If the same substructure recurs in several refinements, move it into a crosscutting concept (see Crosscutting Concept). Stereotypes that point to that concept give a leaner structure without the repetition.

**The principle behind it**

The DRY principle (short for "don't repeat yourself") says every piece of knowledge needs one single, unambiguous, authoritative representation. Its authors apply this broadly, including to documentation.

## Example

An overview of a hypothetical booking service lists "Cancel Booking" in two places. Both entries sit in the same overview. The remedy is to keep the detailed description in the one place where cancellation is handled. The other entry gets a short name and a reference to that description.

## Trade-offs

The source pages do not describe costs or benefits of using references.
