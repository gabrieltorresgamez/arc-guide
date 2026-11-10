---
title: Deriving System Components from the Domain Model
slug: deriving-system-components-from-the-domain-model
category: domain-driven-design
kind: method
summary: Building blocks can be found by studying the domain model. Concepts that belong together form
  a component, and cohesion guides the grouping. Parts owned by other teams are kept apart and marked
  as external.
arc42:
- 5
- 8
- 3
step: s06-domain
related:
- cargo-shipping-domain-model-example
- aggregate
- bounded-context
- domain-model
- coupling-and-cohesion
- arc42-crosscutting-concepts
- domain-event
- reflecting-the-business-domain-in-the-architecture
checks:
- Building blocks are grouped by cohesion, so things inside one block belong together.
- Third-party or external elements are clearly marked in the building block view and shown only where
  needed.
- External systems sit behind a translating wrapper that separates them from own components.
- Domain model elements used by many blocks are described in the crosscutting concepts, not as blocks.
- The building block view starts with a level 1 white box of the whole system.
sources:
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://dddsample.sourceforge.net/characterization.html
  title: DDD Sample Application - Characterization of building blocks.
  site: dddsample.sourceforge.net
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/8-5/
  title: 'Tip 8-5: Document business or domain models! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A domain model describes the business concepts a system deals with. Look at which concepts belong together, and group them.

**Start from cohesion.** arc42 says cohesion should be the main driver when forming building blocks. See the article Coupling and Cohesion.

**Look at the groupings the model already shows.**
- In the well-known cargo sample, Cargo is the central aggregate. Aggregates help decouple large structures by setting rules for relations between entities. See the article Aggregate. The Cargo aggregate, rooted at Cargo, also contains the value objects Delivery, Itinerary and Leg.
- HandlingEvent is a domain event. It records a real-world happening, such as cargo being loaded or unloaded. See the article Domain Event.
- Bounded contexts split a large domain model into parts, because one unified model is not feasible for a large system. See the article Bounded Context.

**Give the use cases an owner.** Application services such as BookingService support specific use cases. In the sample, such services drive workflow and coordinate transaction management.

**Separate own components from external systems.** In the sample, external routing sits behind a wrapper. The wrapper translates to and from the other team's API and data model.

**Map the result to arc42.** The building block view is a hierarchy of black boxes and white boxes. A black box shows what a block does. A white box shows what is inside. Level 1 is the white box of the whole system. arc42 advises including third-party software in the building block view only in exceptional cases, and indicating such elements clearly.

## Example

A small shop system has a domain model with orders, products and shipments. The team asks which concepts belong together. Orders and their lines form one cohesive block. Shipment tracking forms another. An order-entry service ties the use case "place an order" to both. The shop uses a payment provider run by another company. The team puts a translating wrapper in front of it and marks it as external in the building block view.

## Trade-offs

arc42 says small or simple systems might describe domain model elements in the building block view, but recommends documenting them in the crosscutting concepts chapter. Many building blocks refer to them, which makes them well suited to a crosscutting topic. See the article Crosscutting Concept.

Deriving blocks from the domain model also depends on the model. One unified model for a large system is not feasible, so you need several bounded contexts.
