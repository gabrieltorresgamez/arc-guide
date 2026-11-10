---
title: Barriers to UML Adoption
slug: barriers-to-uml-adoption
category: modeling-uml
kind: concept
summary: People disagree about what UML is for, which explains much of the resistance to it. UML 2 became
  bulkier for sketch users, and informal use drifts from the standard. Lighter options such as C4 exist.
arc42:
- 5
- 8
step: s10-document
related:
- uml-unified-modeling-language
- c4-model
- why-use-uml-in-architecture-documentation
- uml-modeling-best-practice
- uml-modeling-anti-patterns
- diagrams-as-code
- documentation-as-code
- self-invented-notation-drawback
checks:
- The document states whether its UML diagrams are sketches (selective communication) or complete specifications.
- Where diagrams are informal, the document notes that they may deviate from the UML standard.
- If a lighter notation such as C4 is used instead of full UML, the document says so.
sources:
- url: https://martinfowler.com/bliki/UmlMode.html
  title: Uml Mode
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://c4model.com/
  title: Home | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UmlAsSketch.html
  title: Uml As Sketch
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://neverworkintheory.org/2013/06/13/uml-in-practice-2.html
  title: UML in Practice · It Will Never Work in Theory
  site: neverworkintheory.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

People disagree about UML because they hold fundamentally different views of what it should be for. Some want a quick drawing. Others want a precise specification. One notation struggles to satisfy both.

**Sketching versus precision.** In sketch mode, people draw informally. They show some aspects of a system and leave the rest out. They do not try to specify everything.

UML 2 added precision. That precision aimed at two other uses: blueprints and programming-language-style modeling. The side effect was a bulkier notation. Sketch users found it harder to work with.

**Drift from the standard.** Informal users rarely follow every detail of the standard. The further they move from it, the more their usage diverges.

**What practice looks like.** Petre's interviews with practitioners describe selective users. They treat UML as a tool for thinking. They use it only as long as it helps, then move on. Petre found that practitioners tend to use UML either in early design or in implementation. They rarely use it in both.

**Another approach.** The C4 model is one option (see the article C4 Model). It is presented as easy to learn and friendly to developers. It is also notation independent.

## Example

A team wants to explain a new feature to a colleague. They draw a few boxes and arrows on a whiteboard. The drawing shows only the parts that matter for the talk. Nobody checks it against the UML standard. Later, another team member expects a complete, precise model and finds the sketch too loose. The two people hold different views of what the diagram is for.

## Trade-offs

Precise UML supports blueprint and programming-language use, but it costs sketch users simplicity. Informal sketching is quick and selective, but it drifts from the standard and does not specify a system completely.
