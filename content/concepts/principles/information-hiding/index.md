---
title: Information Hiding
slug: information-hiding
category: principles
kind: principle
summary: Information hiding means splitting a system into modules that each conceal one hard or change-prone
  design decision. Clients use only the module's interface, so the inside can change without breaking
  them.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- modularity
- loose-coupling
- modifiability
- coupling-and-cohesion
- module
- design-for-change
- separation-of-concerns
- modifiability-tactics
checks:
- Modules are derived from a list of difficult or change-prone design decisions, not only from processing
  steps.
- Each module hides one identified design decision from the other modules.
- Each module's interface reveals as little as possible about its internals.
- Clients use a module only through its documented interface.
- A building block is described by its responsibility and interface, so readers do not need its internals.
sources:
- url: https://blog.acolyer.org/2016/09/05/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/
  title: On the criteria to be used in decomposing systems into modules – the morning paper
  site: blog.acolyer.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/5-6/
  title: 'Tip 5-6: Hide the inner workings of blackboxes! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Information_hiding
  title: Information hiding - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Clients depend only on the public interface. The hidden decision sits behind it and can change.
review:
  status: generated
  flags: []
---

## Explanation

Information hiding was first described by David Parnas in 1972. It answers a simple question: how should you cut a system into parts?

Parnas's answer is to start from decisions, not from processing steps. First, list the design decisions that are difficult or likely to change. Many decisions are questionable and may change under many circumstances. Then design each module to hide one such decision from the other modules.

**The interface is the only contact point.** A module's interface is chosen to reveal as little as possible about its inner workings. Clients perform operations purely through that interface. They do not see how the work gets done.

**Why this helps.** If the hidden decision changes, clients do not need to adapt. They never depended on it.

**Link to the black box idea.** You can use a black box by knowing only its responsibility and its input and output interfaces. This also reduces documentation effort, because responsibility and interface are enough.

**Encapsulation.** People often use the word encapsulation as a synonym for information hiding. It is a core principle at every level of granularity.

A common use is hiding the physical storage layout of data. Clients ask for data through an interface and do not know how it is stored.

## Example

A shop system has a payment module. How payments are processed is a decision that may change, for example when the company switches providers. The module hides that choice behind a small interface, such as "charge this amount to this customer." The ordering and invoicing modules call only that interface. When the provider changes, only the payment module changes.
