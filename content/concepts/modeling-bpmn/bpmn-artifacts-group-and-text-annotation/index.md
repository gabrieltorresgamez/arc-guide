---
title: BPMN Artifacts (Group and Text Annotation)
slug: bpmn-artifacts-group-and-text-annotation
category: modeling-bpmn
kind: notation-element
summary: BPMN artifacts add extra information to a process diagram. A Group clusters elements visually.
  A Text Annotation attaches a note for human readers. Engines ignore the note.
arc42:
- 5
- 6
- 12
step: s10-document
related:
- bpmn-2-0-notation-overview
- bpmn-core-elements
- bpmn-swimlane-pool-and-lane
- bpmn-connecting-object
- bpmn-collaboration-diagram
- bpmn-modeling-tips
- bpmn-layout-guideline
- bpmn-compensation-event
checks:
- Text annotations are linked to the element they comment on by a dotted association.
- Rules that must be enforced are modeled with real process elements, not only in text annotations, because
  engines ignore annotations.
- Each Group has a clear label, so readers can tell why its elements belong together.
- Associations are not used as a substitute for sequence flows.
sources:
- url: https://www.visual-paradigm.com/guide/bpmn/bpmn-artifact-types-explained/
  title: BPMN Artifact Types Explained
  site: visual-paradigm.com
  accessed: '2026-11-09'
- url: https://www.heflo.com/guides/bpmn/artifacts/text-annotation
  title: Text Annotation — Artifacts BPMN | HEFLO
  site: heflo.com
  accessed: '2026-11-09'
- url: https://documentation.flowable.com/latest/reactmodel/bpmn/reference/text-annotation
  title: Text Annotation | Flowable Enterprise Documentation
  site: documentation.flowable.com
  accessed: '2026-11-09'
- url: https://issues.omg.org/issues/BPMN2-154
  title: BPMN 2.0 FTF — Open Issues - OMG Issue Tracker
  site: issues.omg.org
  accessed: '2026-11-09'
- url: https://camunda.com/bpmn/reference/
  title: BPMN 2.0 Symbols - A complete guide with examples. | Camunda
  site: camunda.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A small process with a Group around two tasks and a Text Annotation linked by a dotted association.
review:
  status: generated
  flags: []
---

## Explanation

BPMN is a notation for drawing business processes. Besides the elements that make up the process flow, it offers two kinds of artifacts: Groups and Text Annotations. They help readers understand a diagram. For the basic notation, see the article BPMN 2.0 Notation.

**Group**

A Group is an informal container. It lets you draw a frame around any elements you want to show as belonging together. The grouping is arbitrary: the modeler decides what goes in it. A Group can stretch across several pools. A pool is a participant's swimlane; see BPMN Swimlane (Pool and Lane).

In the wording of the OMG specification, a Group is the visual depiction of a single CategoryValue. A CategoryValue is a supporting element that the grouping is tied to. The Group label on the diagram is that value. It may start with the name of its Category, followed by a colon.

**Text Annotation**

A Text Annotation is a note. It can describe one process element or the process as a whole. The BPMN 2.0.2 standard describes annotations as a way for modelers to give readers extra information.

A dotted association links the note to what it comments on. That target can be a task, an event, a gateway or a flow.

**What artifacts do not do**

A text annotation adds free text without affecting execution. Process engines ignore it. Its audience is the human reader.

One vendor's reference says compensation tasks connect to the diagram only through associations, never through sequence flows.

## Example

A loan-approval diagram has three tasks: "Receive application", "Check documents" and "Score applicant". The modeler draws a Group around the first two and labels it "Intake". A dotted association connects a Text Annotation to "Check documents". The note says the check needs a second reviewer for large loans. A reader sees the note and the grouping at once. The workflow engine runs the same three tasks in the same order, with or without them.

## Trade-offs

A note that a text annotation holds is invisible to engines. Any rule that must be enforced has to be modeled with real process elements, not only written in a note. A Group is also informal and arbitrary.
