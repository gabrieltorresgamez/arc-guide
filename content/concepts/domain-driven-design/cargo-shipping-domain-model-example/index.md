---
title: Cargo Shipping Domain Model
slug: cargo-shipping-domain-model-example
category: domain-driven-design
kind: artifact
summary: The cargo shipping model is a worked example of a domain model for booking, routing and tracking
  cargo. It shows how naming business concepts clearly, such as plan versus actual handling, gives a model
  that experts can discuss.
arc42:
- 5
- 8
- 12
step: s06-domain
related:
- domain-model
- domain-driven-design
- entity
- domain-event
- domain-service
- aggregate
- ddd-modeling-elements
- ubiquitous-language
checks:
- Entities such as Cargo have a stable identity (for example a tracking id) and a documented life cycle.
- Real-world events, such as loading or customs clearance, are recorded as domain events that feed delivery
  status.
- The customer requirement, the plan and the actual delivery are kept as separate concepts.
- Access to an external routing system goes through a dedicated domain service.
sources:
- url: https://dddsample.sourceforge.net/characterization.html
  title: DDD Sample Application - Characterization of building blocks.
  site: dddsample.sourceforge.net
  accessed: '2026-11-09'
- url: https://insights.orangeandbronze.com/domain-driven-design-cargo-shipping-example/
  title: 'Domain-Driven Design: Cargo Shipping Example | O&B Insights'
  site: insights.orangeandbronze.com
  accessed: '2026-11-09'
- url: https://eclipse-ee4j.github.io/cargotracker/
  title: Eclipse Cargo Tracker
  site: eclipse-ee4j.github.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Requirement, plan and actual delivery in the evolved cargo model (generic sketch).
review:
  status: generated
  flags: []
---

## Explanation

The cargo example comes from Eric Evans' book on Domain-Driven Design. A sample application reuses it. Eclipse Cargo Tracker, a Jakarta EE application, is based on that sample. See the articles Domain Model and Domain-Driven Design for the general idea.

**Cargo as an entity.** Cargo has a stable identity, the tracking id. It also has a life cycle with state changes that the business cares about. That makes it an Entity (see the article Entity). The life cycle begins at booking, when the tracking id is assigned.

**Handling events.** A HandlingEvent records something that really happened to the cargo, such as loading, unloading or customs clearance. It is a Domain Event (see Domain Event). These events feed the cargo's delivery status.

**Goal versus actual.** Delivery is the actual transportation. The RouteSpecification is the customer's requirement. The Itinerary is the plan.

**Routing.** The RoutingService gives the domain access to an external routing system. It is used to find possible routes. See Domain Service.

**Aggregates and repositories.** The sample application uses aggregates. They decouple large structures by setting rules for relations between entities. Repositories exist per aggregate root. Cargo Tracker lists entities, value objects, aggregates, services, repositories and factories as its building blocks. See Aggregate and DDD Building Blocks (Tactical Patterns).

The sample's building blocks are described in Evans' book, except Domain Event.

## Example

A team building a parcel service could follow the same pattern. A parcel gets a tracking id when it is booked. The customer's wish, "deliver to Zurich by Friday," is kept as one concept. The chosen route is a separate concept. Scans at depots are recorded as events. Staff can then say "the plan no longer matches what was handled" without talking about tables.

## Trade-offs

One point stands out: the model keeps requirement, plan and actual delivery as separate concepts, yet the O&B author notes that HandlingEvent, HandlingActivity and TransportStatus overlap and could be merged to simplify the model.
