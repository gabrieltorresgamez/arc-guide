---
title: Loose Coupling
slug: loose-coupling
category: principles
kind: principle
summary: Loose coupling means building blocks depend on each other as little as possible, so a change
  in one rarely forces a change in another. The right level depends on how much control you have over
  both sides.
arc42:
- 4
- 5
- 8
- 9
step: s07-solution-strategy
related:
- coupling-and-cohesion
- reduce-coupling
- high-cohesion
- information-hiding
- modifiability
- design-for-change
- synchronous-vs-asynchronous-communication
- separation-of-concerns
checks:
- The document states where tight coupling is accepted and why, for example because the same team owns
  both endpoints.
- Shared custom data types between components are identified, since they create hidden dependencies.
- Synchronous calls are reviewed for cascading slowdowns when a provider is slow.
- Any intermediary that decouples locations is checked for becoming a central bottleneck.
- Shared global data between modules is avoided or justified, since it is tighter than passing data by
  parameters.
sources:
- url: https://www.enterpriseintegrationpatterns.com/ramblings/coupling_facets.html
  title: The Many Facets of Coupling - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Coupling_(computer_programming)
  title: Coupling (computer programming) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://www.enterpriseintegrationpatterns.com/ramblings/eventdriven_coupling.html
  title: Event-driven = Loosely coupled? Not so fast! - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Loose_coupling
  title: Loose coupling - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Coupling describes how much two parts of a system depend on each other. It can be low (also called loose or weak) or high (tight or strong). Another way to see it is independent variability: if you change system A, must system B change too? If not, they are loosely coupled.

Coupling is not an on/off property. It is a sliding scale with many dimensions. A design can be loose in one dimension and tight in another. For example, an event-driven design is not automatically loosely coupled.

**Kinds of coupling**

- **Content coupling:** one module uses the code of another. This is the strongest procedural type.
- **Common coupling:** several modules share access to the same global data. This is tighter than data coupling.
- **Data coupling:** modules share data through parameters. This is the looser form.
- **Temporal coupling:** actions are bundled into one module only because they happen at the same time. In a different sense, with synchronous calls a slow provider also slows its requestor, so the delay cascades. Asynchronous messaging cannot make an unavailable system available.
- **Location coupling:** systems must agree on an addressing scheme, such as host names, URLs, or channel names. Each choice absorbs some degree of change. A rough rule says logical addressing tolerates change better than physical addressing, but "logical" and "physical" are relative to the layer in the communications stack.
- **Data format coupling:** tagged formats such as JSON or XML loosen format constraints. Format coupling can still undermine other decoupling efforts.

**Invisible coupling**

Shared custom data types create hidden knowledge dependencies. Both components must know the same custom definition. Standard formats loosen this kind of interface coupling.

**Ways to loosen coupling**

- Dependency injection and interface-based programming reduce coupling strength and help maintainability.
- Intermediaries sit between parts. An enterprise service bus (ESB, middleware that connects systems) was invented to achieve loose coupling in multiple dimensions.

## Example

An order service needs customer data from a customer service. In a tightly coupled design, it reads the customer database directly and relies on a custom record layout. Any change to that database breaks the order service. In a looser design, the order service asks for the data through a parameterized call. It uses a standard format such as JSON and finds the provider by a logical name, not a physical address. The customer team can now change its internals without touching the order service.

## Trade-offs

Looser is not always better. The right level of coupling depends on how much control you have over the endpoints. If you own both sides, tight coupling can be acceptable.

Intermediaries have a cost. Full location decoupling through an intermediary shifts the change dependency to a central component. That component can become a bottleneck, like a "god class" that everything depends on.
