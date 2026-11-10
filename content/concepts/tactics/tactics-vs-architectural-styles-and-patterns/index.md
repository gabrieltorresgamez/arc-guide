---
title: Relationship between Tactics and Architectural Styles/Patterns
slug: tactics-vs-architectural-styles-and-patterns
category: tactics
kind: concept
summary: A tactic is a single design decision that influences one quality attribute response. A pattern
  is a solution to a recurring problem. Patterns are made of smaller tactic-level decisions, like molecules
  from atoms.
arc42:
- 4
- 9
step: s07-solution-strategy
related:
- architectural-tactic
- architectural-pattern
- architectural-style
- choosing-and-applying-tactics
- tactic-trade-off-balancing
- layers-pattern
- quality-attribute
- working-with-tactics-and-quality-attributes
checks:
- Each tactic named in the document is described as a design decision aimed at a quality attribute response.
- The document says how each chosen tactic is realized, for example through a pattern, framework or code.
- Side effects of a tactic on other quality attributes are noted.
sources:
- url: https://www.informit.com/articles/article.aspx?p=2738304&seqNum=5
  title: '2.5 Design Concepts: The Building Blocks for Creating Structures | Architectural Design | InformIT'
  site: informit.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A pattern is built from several tactic-level decisions and is then realized in frameworks and
    code.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A **tactic** is a design decision that influences how a system responds on a quality attribute. Quality attributes are traits such as security or availability (see Quality Attribute).

A **pattern** is a conceptual solution to a design problem that keeps coming back in a defined context.

A useful comparison: a tactic is an atom, and a pattern is a molecule.

Tactics are simpler than patterns. They are also not finished designs. A team still has to realize a tactic through patterns, frameworks and code.

So the two ideas fit together. A tactic focuses on a single quality attribute response, while a pattern typically balances multiple forces.

## Example

A team wants a system to survive failures. "Keep a spare ready to take over" is a tactic. The team then realizes it through a pattern, a framework and some code. The tactic stays the same. The realization is where the details get decided.

## Trade-offs

A tactic is simple, but it can have side effects. It may improve its target response while trading off other qualities. A tactic is also not a finished design. The team must still choose how to realize it with patterns, frameworks and code.
