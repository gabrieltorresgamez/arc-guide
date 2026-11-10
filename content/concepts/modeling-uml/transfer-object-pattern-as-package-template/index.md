---
title: Transfer Object Pattern as Package Template
slug: transfer-object-pattern-as-package-template
category: modeling-uml
kind: notation-element
summary: A Transfer Object bundles data so fewer remote calls are needed. In UML, you can document this
  pattern as a package template and reuse it by binding its parameters to concrete elements with a dashed
  «bind» arrow.
arc42:
- 5
- 8
step: s10-document
related:
- package-diagram
- class-diagram
- package-relationships-import-access-merge-use
- remote-procedure-call
- architectural-pattern-vs-design-pattern
- domain-model
- class-diagram-relationships
- uml-modeling-best-practice
checks:
- Each template binding is drawn as a dashed arrow from the bound element to the template, with the «bind»
  keyword.
- The parameter substitutions are listed on the binding arrow, separated by commas.
- Transfer Objects appear only where calls cross process boundaries and are expensive; local designs use
  domain objects directly.
- Where Transfer Objects are used, the document names the assembler that maps between them and the domain
  objects.
sources:
- url: https://martinfowler.com/eaaCatalog/dataTransferObject.html
  title: Data Transfer Object
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/17.5.3.html
  title: ''
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
diagrams:
- file: diagram-1.puml
  caption: A concrete package bound to a template package; the dashed arrow carries the «bind» keyword
    and the substitutions.
review:
  status: generated
  flags: []
---

## Explanation

**The pattern.** A Transfer Object (also called a Data Transfer Object, or DTO) is an object that carries data between processes. Its purpose is to cut the number of method calls. On the server side, an assembler usually copies data between the DTO and the domain objects.

**Why remote calls matter.** DTOs exist because remote calls are expensive. Bundling data into one object lets one call do the work of many. In purely local code, this bundling is not needed. It can even do harm. For local designs, the advice is to start with a Service Layer whose method signatures use domain objects, not DTOs.

**The template idea.** UML lets you define a template: an element with open slots, called formal parameters. A package can be such an element. You describe the pattern once and leave the slots open. Each concrete package then fills the slots with real elements. See the Package Diagram article for the basics of packages.

**Binding.** A template binding is a relationship between a templateable element (such as a package) and a template. It substitutes actual parameters for the formal ones.

**Notation.**
- The binding is a dashed arrow. Its tail sits on the bound element, and its head points at the template.
- The «bind» keyword labels the arrow.
- The substitutions appear on the arrow as a comma-separated list.

## Example

A team documents its Transfer Object pattern once, as a template package with two open slots: one for a key type and one for a data type. Two concrete packages, "Customer Access" and "Order Access", each draw a dashed «bind» arrow to the template. Each arrow lists its own substitutions, separated by commas.

## Trade-offs

- Readers must know the binding notation, and UML templates are described as verbose and intricate.
- The template only describes the pattern. It does not tell you whether you need it. Transfer Objects pay off for expensive remote calls. In local contexts they can be harmful, so do not bind the template there by default.
