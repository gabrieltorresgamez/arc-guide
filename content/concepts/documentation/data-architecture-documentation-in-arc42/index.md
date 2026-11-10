---
title: Data Architecture Documentation in arc42
slug: data-architecture-documentation-in-arc42
category: documentation
kind: practice
summary: In arc42, data topics have several homes. Data flows go in the business context, data structures
  can appear as building blocks, and domain terms go in the glossary. A domain data model can also sit
  in the crosscutting concepts.
arc42:
- 3
- 5
- 8
- 12
step: s10-document
related:
- arc42-context-and-scope
- arc42-glossary
- business-and-technical-context
- conceptual-vs-logical-vs-physical-data-model
- ubiquitous-language
- arc42-crosscutting-concepts
- data-architecture
- arc42-documentation-template
checks:
- The business context shows data flows between the system and its partners, not only dependencies.
- The business context shows the system as a black box with domain interfaces to communication partners.
- The building block view is present and any data structures appear as building blocks.
- The glossary defines the domain terms stakeholders use and avoids synonyms and homonyms.
- The domain data model is documented and combined with the glossary.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-12/
  title: 12 - Glossary | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-8/
  title: 8 - Concepts | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A business context sketch: the system is a black box and arrows are labeled with the data
    that flows.'
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

**Data flows in the context (Section 3).** The business context shows the system as a black box. It names the communication partners and the domain interfaces between them. arc42 says all stakeholders should understand which data the system exchanges with its environment. It also advises showing data flows rather than plain dependencies.

The technical context is a separate view. It covers the channels and transmission media that link the system to its environment. One suggested form is a UML deployment diagram. See *Business and Technical Context* and *arc42 Context and Scope*.

**Data structures in the building block view (Section 5).** This view is a static decomposition of the system into building blocks. Building block types can include data structures. The view is mandatory in every arc42 documentation. For the differences between conceptual, logical and physical models, see *Conceptual, Logical and Physical Data Model*.

**Terms in the glossary (Section 12).** The glossary lists the domain and technical terms stakeholders use. Its goal is one shared understanding, without synonyms (different words for one thing) and homonyms (one word for different things). arc42 tips suggest amending the glossary with a graphical model. See *arc42 Glossary* and *Ubiquitous Language*.

**Domain data model in crosscutting concepts (Section 8).** One arc42 tip says to document at least the business or domain data model there. Another tip says to combine domain models with the glossary.

## Example

A web shop's business context diagram shows the shop as one box. Arrows point to a payment provider and a delivery company. Each arrow is labeled with the data it carries, such as "payment request" or "parcel details". The building block view lists an "Order" data structure as one block. The glossary defines "Order" in one sentence and shows a small diagram of how Order relates to Customer and Product. Everyone then uses the word "Order" the same way.
