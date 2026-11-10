---
title: Rules of Thumb for Modeling
slug: rules-of-thumb-for-modeling
category: documentation
kind: practice
summary: Readable diagrams follow a few habits. Give each diagram a title and a key, name each element's
  type, label every relationship specifically, and keep color coding consistent. These habits come from
  C4 guidance.
arc42:
- 3
- 5
- 6
- 7
step: s10-document
related:
- c4-model
- self-invented-notation-drawback
- uml-modeling-best-practice
- color-coding-in-bpmn-models
- bpmn-layout-guideline
- guidelines-for-documentation
- arc42-documentation-template
checks:
- Every diagram has a title that states its type and scope.
- Every diagram includes a key or legend that explains its notation.
- Every relationship line has a label that matches its direction and intent.
- Relationship labels are specific and avoid vague words like 'Uses'.
- Color coding is the same within each diagram and across diagrams, and each element states its type.
sources:
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

These habits come from the C4 model (see the article "C4 Model"). They help people read a diagram they did not draw.

**Give every diagram a title.** The title should state the diagram type and its scope. A reader then knows at once what they are looking at.

**State the type of each element.** Do not leave readers guessing whether a box is a person, a software system, a container or a component. Write the type on the box.

**Label every relationship line.** The label should fit the direction and the intent of the relationship. Make it specific. A vague single word such as "Uses" tells the reader very little.

**Keep colors consistent.** If you color-code elements, use the same codes within one diagram and across all diagrams.

**Add a key or legend.** Choose notation that explains itself where you can. Even so, put a key on every diagram so the notation is explicit, because not everybody will know the notation being used.

## Example

A team draws a diagram of an online shop. The title reads "Container diagram for the Online Shop". Each box names its type, for example "Web Application [Container]". One arrow says "Sends order details to" instead of "Uses". Every database is blue on every diagram. A small key in the corner explains the colors and shapes.

## Trade-offs

The C4 guidance asks for these habits.
