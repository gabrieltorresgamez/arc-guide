---
title: Interoperability Scenario
slug: interoperability-scenario
category: quality-attributes
kind: concept
summary: An interoperability scenario is a fixed template that describes how one system asks another to
  exchange information, and what should happen next. It turns a vague goal into a testable requirement.
arc42:
- 10
step: s04-quality-requirements
related:
- interoperability
- quality-attribute-scenario
- compatibility
- iso-iec-25010-quality-model
- architectural-tactic
- availability-scenario
- arc42-quality-chapter
checks:
- Each interoperability requirement names the source system that starts the request and the systems involved
  in the exchange.
- The scenario states whether the interoperating systems are known before runtime or discovered at runtime.
- The scenario defines what happens when a request is accepted and when it is rejected, including who
  is notified.
sources:
- url: https://hanfak.gitbook.io/workspace/general-paradigms/design-architecture-aims/quality-attributes/interoperability
  title: interoperability | Learning
  site: hanfak.gitbook.io
  accessed: '2026-11-09'
- url: https://satche.github.io/notebook/engineering/architecture/quality-attributes/interoperability
  title: Interoperability | Notebook
  site: satche.github.io
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/60-compatibility
  title: Compatibility
  site: iso25000.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Flow of a general interoperability scenario
review:
  status: generated
  flags: []
---

## Explanation

Interoperability is the degree to which systems can exchange information (see the article Interoperability). In the ISO 25010 quality model it sits under compatibility, together with co-existence.

The general scenario has these parts:

- **Source:** a system that starts a request to interoperate with another system.
- **Stimulus:** the request to exchange information among systems.
- **Environment:** the interoperating systems are either discovered at runtime or known before runtime.
- **Artifact:** the systems that want to interoperate.
- **Response:** the request ends in one of two ways. Either the information is exchanged and the receiver understands it both syntactically and semantically. Or the request is rejected and the appropriate entities are notified. In both cases the request may be logged.
- **Response measure:** how well the response was carried out. A typical measure is the share of exchanges that are correctly processed or correctly rejected.

"Syntactically" means the receiver can read the format. "Semantically" means it understands the meaning.

To write a concrete scenario, replace each generic part with a real system, a real request and a real number. See Quality Attribute Scenario for the general idea.

Tactics for interoperability include:

- **Discover service:** find a service by searching a known directory. This fits when the systems must be found at runtime.
- **Orchestrate:** use a control mechanism to coordinate the systems. This fits complex interactions.
- **Tailor interface:** add or remove capabilities of an interface, such as translation or buffering.

## Example

An invented example. A webshop (source) sends an order request (stimulus) to a payment provider (artifact). Both systems are known before runtime (environment). The provider either accepts the order data and processes it, or rejects it and notifies the shop. It may log the request (response). The team requires that every exchange is correctly processed or correctly rejected (response measure). They can then test that goal with sample requests.
