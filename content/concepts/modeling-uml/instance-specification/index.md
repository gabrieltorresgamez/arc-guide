---
title: Instance Specification
slug: instance-specification
category: modeling-uml
kind: notation-element
summary: An instance specification is a UML model element that stands for one instance in a modeled system.
  It gives a concrete example, with attribute values, of something a class describes in general.
arc42:
- 5
- 8
step: s10-document
related:
- class-diagram
- uml-unified-modeling-language
- structure-diagram
- uml-modeling-best-practice
- class-diagram-relationships
checks:
- Object diagrams model each object and link as an instance specification.
- Object diagrams are used to give examples or test cases for the class diagram.
- Slots show feature values as a feature name, an equal sign and a value.
sources:
- url: https://site.uottawa.ca/~tcl/gradtheses/mnojoumian/ThesisFiles/FinalSpec/UML/7.3.22.html
  title: ''
  site: site.uottawa.ca
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Object_diagram
  title: Object diagram - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://grahamberrisford.com/AM%204%20System%20theory/DescriptionAndReality/TypesSetsAndVocabulary/UML%20types%20and%20instances.htm
  title: 'From Aristotle to EA: a type theory for EA'
  site: grahamberrisford.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: A class and two instance specifications, one named and one anonymous.
review:
  status: generated
  flags: []
---

## Explanation

An instance specification is a UML model element that represents an instance in a modeled system. An instance is one concrete thing, such as one particular customer. (See the article UML Class Diagram for how classes describe things in general.)

**Class versus instance.** A class, more generally called a classifier, describes a set of instances that share features. An instance specification identifies just one of them.

**Where it appears.** Object diagrams use instance specifications. Each object and link on such a diagram is modeled as one. An object diagram shows instances, such as objects and data values, as a graph. It is more concrete than a class diagram.

**Names.** The name of the instance and the name of its classifier are both optional. An anonymous instance of an unnamed classifier is written as an underlined colon.

**Slots.** A slot corresponds to one attribute or feature. It may hold a value for that feature. Slots appear in a compartment beneath the instance name. Written as text, a slot is the feature name, an equal sign, and the value. For example: `status = open`.

**Why use them.** Object diagrams give examples for a class diagram or act as test cases for it. They make an abstract class model concrete.

## Example

A class diagram says that an Order has a status and a total. An object diagram adds one instance specification for a single order. Its slots read `status = open` and `total = 40`. A second, anonymous instance shows another order. A reviewer can now check that the class model fits realistic cases.

## Trade-offs

An instance specification shows one case, or a few. It does not replace the class model, which covers the whole set of instances.
