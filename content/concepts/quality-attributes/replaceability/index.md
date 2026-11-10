---
title: Replaceability
slug: replaceability
category: quality-attributes
kind: quality-attribute
summary: Replaceability is how well one product can take over from another specified product for the same
  purpose in the same environment. It lowers lock-in risk, but a replacement's equivalence must be tested,
  not assumed.
arc42:
- 10
- 11
- 2
step: s04-quality-requirements
related:
- flexibility
- iso-iec-25010-quality-model
- iso-25010-2023-revision
- adaptability
- scalability
- installability
- interoperability
- modifiability
checks:
- The document states which specified product a replacement must stand in for, and for what purpose and
  in which environment.
- The document says how equivalence of a replacement candidate will be established, for example by running
  an evaluation suite, rather than assuming it from interface compatibility.
- The document names lock-in risks and says which other products could be used in place of the present
  one.
- The document makes clear whether a change affects the environment (portability), the whole product (replaceability)
  or a component inside it (interchangeability).
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=8
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/replaceability
  title: Replaceability | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Replaceability describes how well one product can stand in for another specified product. The replacement must serve the same purpose in the same environment. ISO/IEC 25010 defines it this way (see the article on the ISO/IEC 25010 Product Quality Model).

**Where it sits in the quality model.** In the 2023 model, replaceability belongs to Flexibility. Flexibility is how well a product adapts to changes in its requirements, contexts of use or system environment. Replaceability shares that group with adaptability, scalability and installability.

**Why it matters.** Replaceability reduces lock-in risk. Lock-in means being stuck with the present product. With good replaceability, other software products can be used in its place.

**Do not confuse it with its neighbors.** The Q42 quality model separates three terms by what moves:

- Portability changes the environment.
- Replaceability changes the product.
- Interchangeability changes a component inside the product.

**Do not assume equivalence.** For swapping one large language model for another, Q42 notes that an alternative can be interface-compatible while behaving differently. It says equivalence should be established empirically, by running an evaluation suite against the candidate, rather than asserted from the interface.

## Example

A team uses one product to send customer emails. A cheaper product appears. The team does not take it on trust that the new product works the same. They run their existing set of evaluation checks against the candidate. The results show whether it can take over the same purpose in the same environment.

## Trade-offs

For swapping large language models, there is one pitfall: judging a replacement by interface compatibility alone.
