---
title: Constraining Associations
slug: entity-relationship-clarification
category: domain-driven-design
kind: practice
summary: Constraining associations means limiting how objects in a domain model can reach each other.
  You impose a direction or add a qualifier, so each remaining link needs less implementation.
arc42:
- 5
- 8
step: s06-domain
related:
- association
- domain-model
- aggregate
- cargo-shipping-domain-model-example
- domain-driven-design
- reduce-coupling
- class-diagram
checks:
- Associations that can only be used in one direction are marked with a traversal direction.
- Where the reverse direction is needed, the document names a repository query instead of a second navigation
  link.
- Associations with a key-based lookup show a qualifier that reduces the far-end multiplicity.
sources:
- url: https://learn.microsoft.com/en-us/archive/msdn-magazine/2013/october/data-points-coding-for-domain-driven-design-tips-for-data-focused-devs-part-3
  title: 'Data Points - Coding for Domain-Driven Design: Tips for Data-Focused Devs, Part 3 | Microsoft
    Learn'
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.informit.com:443/articles/article.aspx?p=1398623&seqNum=16
  title: '16.15 Qualified Association | Applying UML and Patterns: UML Class Diagrams | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://modeling-languages.com/navigability-associations-conceptual-modeling/
  title: Navigability of associations is NOT a conceptual modeling concern
  site: modeling-languages.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Order reaches its LineItems and its Customer. The reverse directions are left out.
review:
  status: generated
  flags: []
---

## Explanation

An association relates objects in a model, such as an order and its line items. See the article on UML Association. Conceptually, associations are navigable in all directions. In a design, you decide which directions you really need. This is called navigability. It is a design decision tied to how the code implements the link. UML leaves the exact mechanism to the implementation.

Evans advises constraining relationships as much as possible. Understanding the domain may reveal a natural directional bias.

**Impose a traversal direction.** An Order can reach its LineItems. A LineItem cannot navigate back to its Order. In Lerman's sales model, line items are rarely needed without starting from the order.

A removed direction does not have to vanish. The reverse question, such as all orders of a customer, can be answered by a repository query method. You add it only if that context needs it. Such a repository is the place for queries and persistence.

## Example

A shop model has Customer and Order. At first, each Customer holds a list of all its Orders, and each Order points back to its Customer. The team asks which directions the application really uses. Since the application mostly starts from an order, Order keeps its link to Customer. Customer drops its list of orders. When a screen needs a customer's orders, the order repository gets a query method for it. The model still answers both questions, and the code carries one fewer link.

## Trade-offs

Removing a direction means the reverse question needs another route, such as a repository query. You add that query only where a context needs it. Which directions to keep is a design decision, so it depends on how the domain is actually used.
