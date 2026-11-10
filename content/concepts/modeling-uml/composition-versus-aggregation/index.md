---
title: Aggregation vs. Composition
slug: composition-versus-aggregation
category: modeling-uml
kind: notation-element
summary: 'Aggregation and composition are UML ways to show that something is made of parts. Composition
  is strict: a part belongs to one whole. Aggregation is loose and adds little beyond a plain association.'
arc42:
- 5
- 8
- 12
step: s10-document
related:
- association
- class-diagram
- class-diagram-relationships
- uml-unified-modeling-language
- common-class-diagram-modeling-mistakes
- uml-modeling-best-practice
- generalization-and-specialization
checks:
- Every filled diamond sits at the whole (composite) end of its association.
- No part is shown in more than one composition relationship at a time.
- For each composition, the whole is the one that creates and deletes its parts.
- If white diamonds are used, the document states what the team means by them.
sources:
- url: https://martinfowler.com/bliki/AggregationAndComposition.html
  title: Aggregation And Composition
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1398623&seqNum=14
  title: '16.13 Composition Over Aggregation | Applying UML and Patterns: UML Class Diagrams | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2013/dd479569(v=vs.120)
  title: AggregationKind Enumeration (Microsoft.VisualStudio.Uml.Classes) | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.puml
  caption: 'Composition (filled diamond: Board and Square) and aggregation (hollow diamond: Team and Player).'
review:
  status: generated
  flags: []
---

## Explanation

Both notations draw a diamond on an association line (see UML Association). For composition, the filled diamond sits at the composite (whole) end.

**Composition** uses a filled diamond. It is also called composite aggregation. It is the strong form of whole-part.

- A part can belong to only one composition at a time.
- The whole is responsible for creating and deleting its parts.
- When the whole is destroyed, its parts are destroyed too, or they move to another whole. No part is left free-floating.

**Aggregation** uses a white (hollow) diamond. It has no semantics beyond those of a regular association.

**The three kinds in Visual Studio's UML model.** Microsoft's Visual Studio UML library describes the sharing characteristics of an association with an enumeration called AggregationKind. It has three values:

- None.
- Shared: more than one whole may refer to each part.
- Composite: a part cannot be shared between wholes.

According to the Microsoft page, the precise interpretation of AggregationKind is open to local convention.

**Is aggregation worth using?** One source says aggregation adds no meaning beyond a plain association, and quotes Rumbaugh calling it a modeling placebo. Another source says it has no distinct semantics, though UML defines the term. Its advice is to skip aggregation and use composition when it fits.

## Example

A game model has a Board made of Squares. Each Square belongs to exactly one Board. If the software Board object is destroyed, its Square objects are destroyed with it. This is composition, so the diagram shows a filled diamond at the Board end.

Now take a model with Team and Player, where one player may appear in several teams. Since the white diamond adds no meaning beyond a regular association, a plain association is enough here.

## Trade-offs

Composition gives a clear rule: one owner, and the owner controls creation and deletion. A part can belong to only one composition at a time.

Aggregation has no semantics beyond those of a plain association, and its meaning is vague. Readers may interpret the white diamond differently, since there are no standard meanings for it. A plain association avoids that confusion.
