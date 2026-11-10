---
title: UML 2.5 Diagram Taxonomy
slug: uml-diagram-taxonomy
category: modeling-uml
kind: concept
summary: UML 2 defines 14 diagram types, grouped in a taxonomy. Structure diagrams show the static makeup
  of a system. Behavior diagrams show what it does at runtime. Interaction diagrams are a subgroup of
  behavior diagrams.
arc42:
- 5
- 6
- 7
step: s10-document
related:
- structure-diagram
- behavior-diagram
- uml-unified-modeling-language
- matching-diagram-type-to-system-aspect
- why-use-uml-in-architecture-documentation
- sequence-diagram
- class-diagram
- uml-modeling-best-practice
checks:
- Each diagram in the architecture document is identified as a structure diagram or a behavior diagram.
- Diagrams that show the static architecture are structure diagrams.
- Diagrams that show flow of control and data are treated as interaction diagrams, a subset of behavior
  diagrams.
sources:
- url: https://en.wikipedia.org/wiki/Unified_Modeling_Language
  title: Unified Modeling Language - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://guides.visual-paradigm.com/distinguishing-between-structure-and-behavior-diagrams-in-uml/
  title: Distinguishing Between structure and behavior diagrams in UML - Visual Paradigm Guides
  site: guides.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://s.visual-paradigm.com/guide/case-study-uml-2-5-1-the-maturation-of-a-universal-modeling-standard/
  title: 'Case Study: UML 2.5.1 — The Maturation of a Universal Modeling Standard'
  site: s.visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Simplified view of the UML taxonomy: structure and behavior, with interaction as a subgroup
    of behavior.'
review:
  status: generated
  flags: []
---

## Explanation

UML has 14 diagram types, and UML 2.5 keeps that set unchanged. The types are arranged in a taxonomy: a family tree that sorts diagrams into groups.

**Two main groups**

- **Structure diagrams** show the static view of a system. They describe how it is built, so they document its architecture. The profile diagram sits in this group.
- **Behavior diagrams** show the dynamic, runtime view. They describe what the system does and how its parts work together.

**A subgroup inside behavior**

Interaction diagrams are a subset of behavior diagrams. They stress the flow of control and data.

**Why the taxonomy helps**

Each diagram type answers a different kind of question. Sorting them into structure and behavior helps you pick the right one. Ask first whether you need to show what the system is made of or what it does. Then choose a type from that group.

For more on each group, see the articles "UML Structure Diagram" and "UML Behavioral Diagram".

## Example

A team documents an online shop. To show which parts exist, they draw a structure diagram. To show how an order request moves between those parts, they draw an interaction diagram. Interaction diagrams belong to the behavior group, so the two questions map to the two main groups.

## Trade-offs

The two-way split is broad. It helps you choose a group, but it does not tell you which of the 14 types fits a given question.
