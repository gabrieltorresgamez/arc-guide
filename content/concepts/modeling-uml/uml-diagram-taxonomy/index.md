---
title: UML 2.5 Diagram Taxonomy
slug: uml-diagram-taxonomy
order: 30
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
- url: https://www.uml-diagrams.org/class-diagrams-overview.html
  title: UML Class and Object Diagrams Overview - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/component-diagrams.html
  title: UML Component Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/composite-structure-diagrams.html
  title: UML Composite Structure Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/deployment-diagrams.html
  title: UML Deployment Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/package-diagrams.html
  title: UML Package Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/profile-diagrams.html
  title: UML Profile Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/use-case-diagrams.html
  title: UML Use Case Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/activity-diagrams.html
  title: UML Activity Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/state-machine-diagrams.html
  title: UML State Machine Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/sequence-diagrams.html
  title: UML Sequence Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/communication-diagrams.html
  title: UML Communication Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/timing-diagrams.html
  title: UML Timing Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
- url: https://www.uml-diagrams.org/interaction-overview-diagrams.html
  title: UML Interaction Overview Diagrams - uml-diagrams.org
  site: uml-diagrams.org
  accessed: '2026-11-16'
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

**All 14 diagram types**

**Structure diagrams**

- **Class diagram:** Classes with their attributes and operations, and the relationships between them. See the article UML Class Diagram. [More](https://www.uml-diagrams.org/class-diagrams-overview.html)
- **Object diagram:** Instances of classes and the links between them. [More](https://www.uml-diagrams.org/class-diagrams-overview.html)
- **Component diagram:** Components, their provided and required interfaces, ports, and the relationships between them. See the article UML Component Diagram. [More](https://www.uml-diagrams.org/component-diagrams.html)
- **Composite structure diagram:** The internal structure of a classifier, how it interacts with its environment through ports, or the behavior of a collaboration. [More](https://www.uml-diagrams.org/composite-structure-diagrams.html)
- **Deployment diagram:** The execution architecture of a system, meaning how software is assigned to the nodes it runs on. See the article UML Deployment Diagram. [More](https://www.uml-diagrams.org/deployment-diagrams.html)
- **Package diagram:** Packages and the relationships between them, such as import, access and merge. See the article Package Diagram. [More](https://www.uml-diagrams.org/package-diagrams.html)
- **Profile diagram:** The UML extension mechanism: custom stereotypes, tagged values and constraints. [More](https://www.uml-diagrams.org/profile-diagrams.html)

**Behavior diagrams**

- **Use case diagram:** Units of useful functionality (use cases) that a system performs in collaboration with external users (actors). See the article Use Case Diagram. [More](https://www.uml-diagrams.org/use-case-diagrams.html)
- **Activity diagram:** The flow of control or of objects, with emphasis on the sequence and the conditions of the flow. [More](https://www.uml-diagrams.org/activity-diagrams.html)
- **State machine diagram:** The discrete behavior of a part of the designed system through finite state transitions. See the article State Machine Diagram. [More](https://www.uml-diagrams.org/state-machine-diagrams.html)

**Interaction diagrams (a subgroup of behavior diagrams)**

- **Sequence diagram:** Interactions between lifelines as an ordered exchange of messages. See the article UML Sequence Diagram. [More](https://www.uml-diagrams.org/sequence-diagrams.html)
- **Communication diagram:** Interactions between lifelines through messages. [More](https://www.uml-diagrams.org/communication-diagrams.html)
- **Timing diagram:** Interactions when the main purpose is to reason about time. [More](https://www.uml-diagrams.org/timing-diagrams.html)
- **Interaction overview diagram:** The overview of the flow of control, where the nodes of the flow are interactions or interaction uses. [More](https://www.uml-diagrams.org/interaction-overview-diagrams.html)

## Example

A team documents an online shop. To show which parts exist, they draw a structure diagram. To show how an order request moves between those parts, they draw an interaction diagram. Interaction diagrams belong to the behavior group, so the two questions map to the two main groups.

## Trade-offs

The two-way split is broad. It helps you choose a group, but it does not tell you which of the 14 types fits a given question.
