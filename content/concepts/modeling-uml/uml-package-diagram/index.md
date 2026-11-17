---
title: UML Package Diagram
slug: uml-package-diagram
order: 30
category: modeling-uml
kind: notation-element
summary: A package diagram groups related model elements into packages, each a namespace with unique names.
  It shows how packages depend on each other, so you can see a system's structure, such as its layers,
  at a glance.
arc42:
- 5
step: s10-document
related:
- layered-architecture
- uml-structure-diagram
- uml-class-component-and-package-diagrams-compared
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
- url: https://support.ptc.com/help/modeler/r10.2/en/Modeler/umlprofile/UML_Import.html
  title: Import (UML Standard profile)
  site: support.ptc.com
  accessed: '2026-11-09'
- url: https://support.ptc.com/help/modeler/r10.2/en/Modeler/umlprofile/UML_Package_Merge.html
  title: Package merge (UML Standard profile)
  site: support.ptc.com
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/UMLR-797
  title: UML 2.6 RTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaCatalog/dataTransferObject.html
  title: Data Transfer Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/17.5.3.html
  title: "17.5.3 TemplateBinding"
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://www.eclipse.org/articles/Article-Defining-Generics-with-UML-Templates/article.html
  title: Generics in UML
  site: eclipse.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/LocalDTO.html
  title: Local D T O
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/recommendations/declarations-and-initialization-dcl/dcl60-j/
  title: DCL60-J. Avoid cyclic dependencies between packages | CERT Secure Coding
  site: cmu-sei.github.io
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/VPGallery/diagrams/Package.html
  title: Package Diagram - UML 2 Diagrams - UML Modeling Tool
  site: visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: Three packages representing layers, with unlabeled dependencies read as imports.
review:
  status: generated
  flags: []
---

## Explanation

A package diagram is a UML diagram that groups parts of a model into packages. UML stands for the Unified Modeling Language (see the article UML (Unified Modeling Language)).

**Packages as namespaces.** A package gives its contents an encapsulated namespace. A namespace is a named space in which every element name must be unique. Two elements in the same package cannot share a name.

**Dependencies between packages.** Arrows between packages show how they relate. These relationships are directed links from one package to another.

- An unlabeled dependency is read as a package import by default.
- A package merge says the contents of two packages are to be combined.

**Layers.** Packages can stand for the layers of a software system. The diagram then shows a layered architecture. See the article Layered Architecture.

**Link to arc42.** The arc42 building block view is a static decomposition of the system. It is mandatory in architecture documentation and makes code structure understandable through abstraction. Packages are one possible building block type. arc42 also organizes this view in levels, where level 2 zooms into blocks of level 1.

## Example

An online shop has three packages: "Presentation", "Business Logic", and "Data Access". Each package holds its own elements. "Presentation" has a class called "Order", and "Data Access" may also have one. That is fine, because each package is its own namespace. An arrow from "Presentation" to "Business Logic" and another from "Business Logic" to "Data Access" show the layers. Without a label, each arrow reads as a package import.
