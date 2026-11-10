---
title: UML Modeling Anti-Pattern
slug: uml-modeling-anti-patterns
category: modeling-uml
kind: concept
summary: A UML modeling anti-pattern is a diagram that claims to be UML but breaks its rules or invents
  its own. Unexplained arrows and numbers are typical. Readers then guess the meaning, and the documentation
  loses value.
arc42:
- 5
- 7
- 3
step: s10-document
related:
- uml-modeling-best-practice
- self-invented-notation-drawback
- class-component-and-package-diagram-differences
- c4-model
- uml-unified-modeling-language
- association
- class-diagram-relationships
- component-diagram-modeling-mistakes
checks:
- Every diagram has a legend that explains any notation that is not standard.
- Every relationship line is labeled, and the label matches its direction and intent.
- Each diagram has a title naming its type and scope.
- The notation choice is deliberate, and stakeholders share one understanding of it.
- Each diagram can be understood without a separate narrative.
sources:
- url: https://leanpub.com/read/arc42-faq/chapter-vii
  title: Frequently Asked Questions — arc42-FAQ
  site: leanpub.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/agile-software-architecture-sketches-NoUML/
  title: Agile Software Architecture Sketches and NoUML - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/activities/DPR-ArchitectureModeling
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UmlAsSketch.html
  title: Uml As Sketch
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Some diagrams present themselves as UML (the Unified Modeling Language, a standard drawing notation) but use notation the author never explained. Readers cannot tell what the symbols mean.

**Unexplained boxes, lines and numbers.** Boxes and lines have no built-in meaning. Without an explanation, readers interpret them differently from the author's intent. Informal sketches often leave the meaning of different box and line styles unexplained. This is a common flaw.

**Arrows need a defined meaning.** Explain the arrow in a legend. A legend is a small key on the diagram that says what each symbol means. Every diagram needs one, even diagrams drawn in UML, because not everybody knows the notation. Line labels should match the direction and intent of the relationship. Vague labels like "Uses" do not help. See UML Association and UML Class Diagram Relationship for the standard meanings.

**One diagram, one purpose.** Mixed levels of abstraction are a common flaw in informal sketches. Create one diagram per viewpoint, meaning one set of stakeholder concerns. See Differences between Class, Component and Package Diagrams.

**Strict UML or informal sketch?** Both can work. UML is tool-supported, has clear semantics and is standardized. It is optional, though, and gives no guaranteed benefit. Informal sketches can communicate well, provided they carry a legend. UML sketches are often selective, and communication matters more than obeying every rule. What matters is that all stakeholders understand the notation the same way. Choose diagrams and notation deliberately, reflecting project and company culture.

**Relation to C4.** C4 asks for a key on every diagram, whichever notation you pick. It also offers a short review checklist, and each diagram should stand alone without a narrative. C4 diagrams can also be drawn in UML, using packages, components and stereotypes. The UML version tends to carry less descriptive text.

## Example

A team draws one picture with numbered arrows, some boxes that look like deployed servers, and some that look like code packages. Nobody explains the numbers. One reader sees a call order, another sees priorities. The team fixes it by splitting the picture into two titled diagrams. Each has a legend. Arrows get labels that state what flows and in which direction.

## Trade-offs

Strict UML gives clear, standardized meaning and tool support. It gives no guaranteed benefit. Informal sketches are flexible but can be inconsistent, and they depend on a legend to avoid misreading. Which to use depends on the audience and on project and company culture.
