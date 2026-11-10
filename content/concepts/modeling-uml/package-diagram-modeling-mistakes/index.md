---
title: Package Diagram Modeling Mistake
slug: package-diagram-modeling-mistakes
category: modeling-uml
kind: concept
summary: 'Package diagrams go wrong in a few typical ways: cycles between packages, unlabeled relationships,
  wrong containment, and misused merges. Avoiding them keeps the structure readable and easier to change.'
arc42:
- 5
step: s10-document
related:
- package-diagram
- package-relationships-import-access-merge-use
- coupling-and-cohesion
- class-component-and-package-diagram-differences
- uml-modeling-anti-patterns
- common-class-diagram-modeling-mistakes
- high-cohesion
- loose-coupling
checks:
- The package dependencies contain no cycles and can be drawn as a directed acyclic graph.
- Every relationship between packages carries a keyword such as import or access, so the meaning is clear.
- 'Containment goes from package to members: packages contain classes or other packages, never the reverse.'
- Package merge is used only between packages, for elements that represent the same concept.
- Packages used as building blocks are grouped by cohesion.
sources:
- url: https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/recommendations/declarations-and-initialization-dcl/dcl60-j/
  title: DCL60-J. Avoid cyclic dependencies between packages | CERT Secure Coding
  site: cmu-sei.github.io
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/VPGallery/diagrams/Package.html
  title: Package Diagram - UML 2 Diagrams - UML Modeling Tool
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A cycle between three packages, with labeled relationships.
review:
  status: generated
  flags: []
---

## Explanation

A package diagram groups model elements into packages and shows how the packages relate.

**Cyclic dependencies.** Package A depends on B, and B depends on A, directly or through other packages. This causes real problems:

- A change spreads further than it should.
- Packages in the cycle cannot be released or upgraded on their own. They must move together.
- A cycle-free structure can be drawn as a directed acyclic graph, which is a set of arrows with no loop back. Avoiding cycles lowers coupling between packages.

See *Coupling and Cohesion* for background on coupling.

**Wrong containment.** A package is a namespace for its members. A package may contain other packages.

**Misused merge.** Package merge is meant for elements in different packages that share a name and stand for the same concept. The result equals a model in which all merges were already done.

**Unlabeled or mixed-up relationships.** Import, access, and merge mean different things.

- An import makes the members of another package available in the importing package.
- A public import also makes those elements visible outside the importing package.
- A private import is marked with the keyword «access» instead of «import».
- An import's default visibility is that of the imported element.

An arrow with no keyword leaves readers guessing which meaning you intended. The article *Package Relationships (Import, Access, Merge, Use)* covers them in detail.

**Structure and use.** In the arc42 building block view, packages can serve as building blocks. That view is a static decomposition of the system into black boxes and white boxes. arc42 recommends that cohesion be the main driver when forming building blocks.

## Example

A team draws three packages: Orders, Billing, and Customers. Orders depends on Billing, Billing on Customers, and Customers on Orders. That is a cycle. Changing Customers can ripple into all three, and none can be released alone. They then draw an unlabeled arrow from Orders to Billing. Readers cannot tell whether it is an import, an access, or a merge. They fix the diagram by breaking the loop and labeling each arrow with its keyword.

## Trade-offs

Removing a cycle lowers coupling and lets packages be released independently.
