---
title: Open-Closed Principle
slug: open-closed-principle
category: principles
kind: principle
summary: A building block stays open to new behavior but closed to edits of its existing code. Other parts
  rely on a fixed interface, and new behavior arrives through new implementations of it.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- information-hiding
- design-for-change
- modifiability
- loose-coupling
- microkernel-pattern
- architecture-principle
- interface-segregation-principle
- modifiability-tactics
checks:
- Components that are expected to change expose a stable, well-defined interface that other components
  use.
- Extension points exist only where change is expected, and unused extension points are removed.
- New behavior is added through new implementations of an existing interface or through plug-ins, not
  by editing existing code.
sources:
- url: https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
  title: Open–closed principle - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/dipInTheWild.html
  title: DIP in the Wild
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/Yagni.html
  title: Yagni
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Checkout depends on a fixed interface; new delivery options are added as new implementations.
review:
  status: generated
  flags: []
---

## Explanation

The principle has two halves. A module is **open** if you can still extend it. A module is **closed** if other modules can already use it, because it offers a stable, well-defined interface.

The common slogan says software entities such as classes, modules, and functions should be open for extension but closed for modification. The idea is to add behavior without editing the original code.

**Two readings.** Meyer's 1988 book introduced the principle. His idea was extension by inheriting from existing code without changing it. A later, polymorphic reading keeps the abstract interface fixed. New implementations of that interface supply new behavior, and each must at least implement the interface.

**Dependency inversion.** The Dependency Inversion Principle is about shape. Abstractions and high-level policy should not depend on low-level details.

**Beyond classes.** The slogan names modules as well as classes. Brett Schuchert's article on the Dependency Inversion Principle calls the open–closed principle certainly related, and describes breaking a problem into logical blocks and extending them to handle new scenarios as the system grows.

## Example

A shop system calculates shipping costs. The checkout component talks only to a "shipping calculator" interface. At first there is one implementation, for standard delivery. Later the shop adds express delivery and pickup. Each is a new implementation of the same interface. The checkout component does not change.

## Trade-offs

Extension points cost effort. An extension point that is never used is wasted work, and it is likely to get in the way. Abstractions that make the code harder to understand for current requirements are suspect.
