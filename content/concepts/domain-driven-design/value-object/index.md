---
title: Value Object
slug: value-object
category: domain-driven-design
kind: pattern
summary: 'A value object is a small domain object with no identity of its own. Two value objects with
  the same attribute values are equal. Treat them as immutable: to change one, create a new one.'
arc42:
- 8
- 12
step: s06-domain
related:
- entity
- entity-vs-value-object
- ddd-modeling-elements
- domain-model
- bounded-context
- aggregate
- domain-driven-design
checks:
- Value objects in the model are immutable, and changes create a new object.
- Equality of value objects is defined by comparing all attribute values.
- Concepts like money, ranges or points are modeled as value objects rather than bare primitives.
- The document states in which context each concept is treated as a value or as a reference object.
sources:
- url: https://martinfowler.com/bliki/ValueObject.html
  title: Value Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/EvansClassification.html
  title: Evans Classification
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Value_object
  title: Value object - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A value object is a small object such as a date, an amount of money, a point or a range. It has no identity. Its attribute values define it. Two value objects with the same values for all attributes count as equal.

An entity is different. An entity keeps its identity over time (see the article "Entity"). Entities tend to be big. Values tend to be little things. For the comparison, see "Entity and Value Object".

**Change means replace.** You do not alter a value object. You replace it with a new one. Your height is not edited in place. You swap the old height object for a new one. The same holds for a party date: you create a new date object.

**Why immutability matters.** A shared mutable value can cause an aliasing bug. You change a date in one place, and the change has effects elsewhere that you did not expect. Making value objects immutable avoids this kind of bug.

**Equality.** Value objects compare by value, so the code must define equality that way. In languages such as Java, that means defining `equals` and `hashCode` from the attribute values.

**Prefer value objects over primitives.** Replacing common primitives, such as strings, with fitting value objects is often a good idea. For example, a telephone number can be a telephone number object instead of a string.

**Context decides.** Whether a concept is a value or a reference object depends on your context. Check which one fits your situation (see "Bounded Context").

## Example

A shop stores a delivery period as two plain date fields on each order. Someone changes a shared date, and other orders shift unexpectedly.

The team introduces a `DateRange` value object with a start and an end. It cannot be changed after creation. To move the delivery, the code creates a new `DateRange` and puts it on the order. Two ranges with the same start and end are equal, so the code needs no ID to compare them.

## Trade-offs

Replacing a value means creating a new object instead of changing the old one. In return, you avoid aliasing bugs. Deciding whether a concept is a value or a reference object takes thought, because the answer changes with context.
