---
title: Modeling Method
slug: modeling-method
category: documentation
kind: method
summary: A modeling method is a short set of team agreements on how to draw architecture models. It keeps
  diagrams consistent, readable, and limited to what matters.
arc42:
- 5
- 3
- 8
step: s10-document
related:
- c4-model
- diagrams-as-code
- modeling-tool-vs-drawing-tool
- rules-of-thumb-for-modeling
- arc42-documentation-template
- architecture-viewpoint
- view-creation-method
- self-invented-notation-drawback
checks:
- Every diagram has a title stating its diagram type and scope.
- Every diagram carries a legend explaining its notation.
- Every relationship arrow has a label stating its intent.
- Color coding is consistent within and across diagrams.
- The type of every element is stated explicitly.
sources:
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams
  title: Diagrams | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/checklist
  title: Review checklist | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/tooling
  title: Tooling | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

**Match detail to audience.** Different readers need different levels of detail. The C4 Model (see its article) offers zoom levels for this purpose. Each level tells a different story to a different audience. Most teams only need context and container diagrams.

**Specify element types.** State the type of every element explicitly, for example person, system, container, or component.

**Make each diagram explain itself.**
- Give every diagram a title that states its diagram type and scope.
- Add a legend (a key) that explains the notation.
- Label every relationship arrow with its intent.

**Agree on colors.** Colors can be chosen freely. Keep any color coding consistent within and across diagrams, and be careful about black and white printers and color blindness.

**Avoid diagram sprawl.** Do not draw everything. The arc42 Architecture Documentation Template advises detailing only building blocks that are important, surprising, risky, complex, or volatile. It also uses abstraction levels. Each level zooms into selected building blocks of the one before it.

**Consider tooling.** One question to ask is whether data is stored in git next to the source code or inside a tool or cloud service.

## Example

A small team agrees on a few rules. They draw only a context diagram and a container diagram. Every diagram has a title such as "Container diagram for the Order System", a legend, and labeled arrows. Blue always means systems the team owns. Grey always means external systems. They keep the diagram files in git next to the source code.

## Trade-offs

Storing models in git keeps them next to the code. A separate tool or cloud service keeps them elsewhere. Weigh this when you pick tooling.
