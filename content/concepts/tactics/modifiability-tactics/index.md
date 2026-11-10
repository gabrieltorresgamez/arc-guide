---
title: Modifiability Tactic
slug: modifiability-tactics
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
- modifiability
- architectural-tactic
- increase-cohesion
- reduce-coupling
- split-module
- coupling-and-cohesion
- modifiability-scenario
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
diagrams:
- file: diagram-1.mmd
  caption: The three categories of modifiability tactics.
review:
  status: generated
  flags: []
---

## Explanation

A tactic is a design decision that adjusts the parameters of a quality model. Modifiability tactics apply this idea to the cost of changing a system. They form three categories: increase cohesion, reduce coupling, and defer binding.

**Increase cohesion.** Cohesion describes how well the responsibilities of a module belong together (see Coupling and Cohesion). If a module mixes unrelated responsibilities, changing it will likely cost a lot. The *split module* tactic addresses this. See Split Module.

**Reduce coupling.** Coupling describes how much modules depend on each other (see Reduce Coupling). Two tactics stand out:

- *Encapsulation* adds an explicit interface to an element. The interface hides the element's implementation details.
- *Restrict dependencies* limits which modules a given module may interact with or depend on.

**Defer binding.** Binding means fixing a value or functionality in the system. These tactics differ in how late in the life cycle the binding happens:

- At compile or build time: component replacement, compile-time parameterization, and aspects.
- At deployment, startup, or initialization time: configuration-time binding and resource files.
- At runtime: discovery, interpreting parameters, shared repositories, and polymorphism.

The same SEI report also covers architectural patterns and their variants. See Architectural Tactic and Relationship between Tactics and Architectural Styles/Patterns.

## Example

A team runs an online shop. One module handles orders, invoices, and email templates. Every template change puts order logic at risk. The team splits the module so each responsibility has its own module. Each new module gets a small interface that hides its internals. Only the modules that need to talk to each other are allowed to do so. Later, the team could choose to bind some values, such as template text, at startup through a resource file instead of fixing them in code.
