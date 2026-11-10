---
title: Influence of Architectural Means
slug: influence-of-architectural-means
category: fundamentals
kind: concept
summary: Architects shape systems with principles, concepts, tactics, styles, patterns and reference architectures.
  These means differ in how much they dictate. Reference architectures prescribe the most, so pick the
  means that fits each decision.
arc42:
- 4
- 8
- 9
step: s07-solution-strategy
related:
- architecture-means
- architecture-principle
- architectural-tactic
- architectural-style
- architectural-pattern
- tactics-vs-architectural-styles-and-patterns
- requirements-and-means-influence-architecture
- arc42-solution-strategy
checks:
- Principles used in the system are stated as general guidelines or rules that hold for the whole system
  or parts of it.
- Each tactic is tied to a specific quality goal it helps to meet.
- Patterns marked as architectural directly and substantially influence named architectural drivers.
- If a reference architecture is adopted, the concerns it brings are listed and addressed in the design.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=2
  title: '3.2 Design Concepts: The Building Blocks for Creating Structures | Making Design Decisions |
    InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://public.isaqb.org/glossary/glossary-en.html
  title: iSAQB® Glossary of Software Architecture Terminology
  site: public.isaqb.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Architectural means ordered from general guidance to strongest influence.
review:
  status: generated
  flags: []
---

## Explanation

Architects draw on several kinds of design tools.

These tools include:

- **Principles** are guidelines that help developers design better solutions, such as low coupling or high cohesion.
- **Concepts** are the building blocks of architectures.
- **Tactics** are design decisions that architects choose to meet a specific quality goal. A tactic addresses a single quality attribute response. One source compares a tactic to an atom.
- **Architectural styles** are patterns that define types of components and connectors in a specified topology.
- **Patterns** typically balance multiple forces, meaning several quality goals. The same source compares a pattern to a molecule. An architectural pattern is a fundamental structural organization schema for software systems. It counts as architectural when it directly and substantially influences the system's architectural drivers.
- **Reference architectures** map a reference model onto one or more patterns. They are blueprints that give an overall logical structure for a class of applications. They describe whole applications in more detail than styles do.

The iSAQB glossary describes a tactic as a technique, strategy, approach or decision that helps achieve one or several quality requirements.

## Example

A team must keep a web shop responsive and easy to change. They start from the principle of separation of concerns. They then pick a tactic for one quality goal, such as a response-time measure. For overall structure they choose a pattern. If the company already has a standard blueprint for shops, they could adopt it as a reference architecture.

## Trade-offs

Adopting a reference architecture also brings a set of concerns that you must address during design. Principles are rather abstract, so design concepts were cataloged to make them more usable in practice. The choice, combination and tailoring of tactics and patterns are key steps of the ADD process.
