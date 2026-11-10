---
title: Package Diagram
slug: package-diagram
category: modeling-uml
kind: notation-element
summary: A package diagram groups related model elements into packages, each a namespace with unique names.
  It shows how packages depend on each other, so you can see a system's structure, such as its layers,
  at a glance.
arc42:
- 5
step: s10-document
related:
- package-relationships-import-access-merge-use
- package-diagram-modeling-mistakes
- layered-architecture
- structure-diagram
- class-component-and-package-diagram-differences
- uml-component-diagram
- coupling-and-cohesion
- modularity
checks:
- Element names are unique within each package of the diagram.
- Package dependencies without a label are intended to be read as package imports.
- If packages represent layers, the diagram shows the layered architecture.
- If packages serve as building blocks in the building block view, level 2 zooms into level-1 blocks.
sources:
- url: https://en.wikipedia.org/wiki/Package_diagram
  title: Package diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Three packages representing layers, with unlabeled dependencies read as imports.
review:
  status: generated
  flags: []
---

## Explanation

A package diagram is a UML diagram that groups parts of a model into packages. UML stands for the Unified Modeling Language (see the article Unified Modeling Language (UML)).

**Packages as namespaces.** A package gives its contents an encapsulated namespace. A namespace is a named space in which every element name must be unique. Two elements in the same package cannot share a name.

**Dependencies between packages.** Arrows between packages show how they relate.

- An unlabeled dependency is read as a package import by default.
- A package merge is a directed relationship. It says the contents of two packages are to be combined.

The article Package Relationships (Import, Access, Merge, Use) covers these in detail.

**Layers.** Packages can stand for the layers of a software system. The diagram then shows a layered architecture. See the article Layered Architecture.

**Link to arc42.** The arc42 building block view is a static decomposition of the system. It is mandatory in architecture documentation and makes code structure understandable through abstraction. Packages are one possible building block type. arc42 also organizes this view in levels, where level 2 zooms into blocks of level 1.

## Example

An online shop has three packages: "Presentation", "Business Logic", and "Data Access". Each package holds its own elements. "Presentation" has a class called "Order", and "Data Access" may also have one. That is fine, because each package is its own namespace. An arrow from "Presentation" to "Business Logic" and another from "Business Logic" to "Data Access" show the layers. Without a label, each arrow reads as a package import.
