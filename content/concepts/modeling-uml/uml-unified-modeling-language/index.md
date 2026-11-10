---
title: Unified Modeling Language (UML)
slug: uml-unified-modeling-language
category: modeling-uml
kind: standard
summary: UML is a standard graphical modeling language for software. It defines 14 diagram kinds, split
  into structure and behavior diagrams. It is not a method, so teams use it with a development method.
arc42:
- 5
- 6
- 7
- 8
step: s10-document
related:
- uml-diagram-taxonomy
- structure-diagram
- behavior-diagram
- modeling-method
- barriers-to-uml-adoption
- uml-modeling-anti-patterns
- uml-modeling-best-practice
- why-use-uml-in-architecture-documentation
checks:
- The document states which development method the UML diagrams are used with, because UML itself is not
  a method.
- Each UML diagram is identifiable as a structure diagram or a behavior diagram.
sources:
- url: https://en.wikipedia.org/wiki/Unified_Modeling_Language
  title: Unified Modeling Language - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://wiki.eclipse.org/MDT/UML2/UML2_5.0_Migration_Guide
  title: MDT/UML2/UML2 5.0 Migration Guide - Eclipsepedia
  site: wiki.eclipse.org
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/FUML/1.1
  title: About the Semantics of a Foundational Subset for Executable UML Models Specification Version
    1.1
  site: omg.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: UML 2 splits its 14 diagram kinds into structure and behavior diagrams.
review:
  status: generated
  flags: []
---

## Explanation

UML stands for Unified Modeling Language. It began when Grady Booch and James Rumbaugh merged their separate models into one unified model. The Object Management Group (OMG) then took ownership of it.

**Versions.** UML 2.0 was a major revision in 2005. It replaced version 1.5. Version 2.5 was formally released in 2015. Version 2.5.1 was adopted in December 2017.

**The 2.5 rewrite.** The UML 2.5 specification was rewritten to be easier to read. The authors removed redundancy and made the text clearer. The metamodel stayed largely unchanged. (The metamodel is the model that defines UML's own elements.)

**Diagram kinds.** UML 2 defines 14 kinds of diagrams. They fall into two groups:

- *Structure diagrams* show what a system consists of. See UML Structure Diagram.
- *Behavior diagrams* show what a system does. See UML Behavioral Diagram.

The article UML 2.5 Diagram Taxonomy shows how the 14 kinds are arranged.

**Not a method.** UML is a language, not a method. It is designed for use with many object-oriented development methods. See Modeling Method.

**Executable subset.** fUML is a subset of UML. It has precisely defined execution semantics. Semantics means the exact meaning of the elements.

## Example

A team builds an online shop. It draws one structure diagram showing the main parts: catalog, cart and payment. It draws one behavior diagram showing how an order moves through the system. Both diagrams use the same language, so any reader who knows UML can follow them.

## Trade-offs

People have criticized UML as ambiguous, inconsistent and large. At times people have also treated it as a silver bullet for design, and that causes problems. Use it as one tool among others. See Barriers to UML Adoption and UML Modeling Anti-Pattern.
