---
title: Maintainability Tactic
slug: maintainability-tactics
order: 50
category: tactics
kind: tactic
summary: 'Modifiability tactics are design decisions that keep the cost of changes low. They fall into
  three groups: increase cohesion, reduce coupling, and defer binding.'
arc42:
- 4
- 8
- 9
- 10
step: s07-solution-strategy
related:
- maintainability
- architectural-tactic
- coupling-and-cohesion
- tactics-vs-architectural-styles-and-patterns
checks:
- The document names which modifiability tactic categories (increase cohesion, reduce coupling, defer
  binding) the design uses.
- Modules that mix non-cohesive responsibilities are identified and split, or the document explains why
  not.
- Key modules expose an explicit interface that hides implementation details.
- The document states which modules a given module may depend on.
- For each deferred-binding choice, the document states when the binding happens (build, deployment or
  startup, or runtime).
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=5
  title: 3.5 Design Concepts to Support Modifiability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://quality.arc42.org/approaches/increase-cohesion
  title: Increase Cohesion | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/reduce-coupling
  title: Reduce Coupling | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/approaches/defer-binding
  title: Defer Binding | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-16'
- url: https://www.sei.cmu.edu/blog/architecting-service-oriented-systems/
  title: Architecting Service-Oriented Systems | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html
  title: Message Bus - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html
  title: Publish-Subscribe Channel - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://martinfowler.com/bliki/TolerantReader.html
  title: Tolerant Reader
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The three categories of modifiability tactics.
review:
  status: generated
  flags: []
---

## Explanation

A tactic is a design decision that adjusts the parameters of a quality model. Modifiability tactics apply this idea to the cost of changing a system. In ISO/IEC 25010, modifiability is a subcharacteristic of maintainability. They form three categories: increase cohesion, reduce coupling, and defer binding.

**Increase cohesion.** Cohesion describes how well the responsibilities of a module belong together (see Coupling and Cohesion). If a module mixes unrelated responsibilities, changing it will likely cost a lot. The *split module* tactic addresses this.

**Reduce coupling.** Coupling describes how much modules depend on each other. Two tactics stand out:

- *Encapsulation* adds an explicit interface to an element. The interface hides the element's implementation details.
- *Restrict dependencies* limits which modules a given module may interact with or depend on.

**Defer binding.** Binding means fixing a value or functionality in the system. These tactics differ in how late in the life cycle the binding happens:

- At compile or build time: component replacement, compile-time parameterization, and aspects.
- At deployment, startup, or initialization time: configuration-time binding and resource files.
- At runtime: discovery, interpreting parameters, shared repositories, and polymorphism.

The same SEI report also covers architectural patterns and their variants. See Architectural Tactic and Relationship between Tactics and Architectural Styles/Patterns.

**In a service-oriented architecture.** An SOA infrastructure connects service consumers to services. Examples:

- *Mediating infrastructure*: hides differences between consumers and service interfaces, such as different versions of a standard like SOAP 1.1 and SOAP 1.2.
- *Message bus*: connects applications through a shared set of interfaces. Applications can be added or removed without affecting the others.
- *Publish-subscribe*: a sender publishes an event on a channel, and the channel delivers a copy to each receiver.
- *Service registry*: offers functionality such as discovery, versioning and access control, among others.
- *Tolerant consumers*: a tolerant reader takes only the data it needs from a service. This aims to let providers make changes that ought not to break the consumer's code.

**More tactics in the arc42 quality model.** The arc42 quality model has its own approach pages on related ideas: [Increase Cohesion](https://quality.arc42.org/approaches/increase-cohesion), [Reduce Coupling](https://quality.arc42.org/approaches/reduce-coupling), [Defer Binding](https://quality.arc42.org/approaches/defer-binding).

## Example

A team runs an online shop. One module handles orders, invoices, and email templates. Every template change puts order logic at risk. The team splits the module so each responsibility has its own module. Each new module gets a small interface that hides its internals. Only the modules that need to talk to each other are allowed to do so. Later, the team could choose to bind some values, such as template text, at startup through a resource file instead of fixing them in code.
