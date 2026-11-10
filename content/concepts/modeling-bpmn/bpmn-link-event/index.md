---
title: Link Event
slug: bpmn-link-event
category: modeling-bpmn
kind: notation-element
summary: A link event pair replaces one sequence flow in a BPMN diagram. A throwing link is the exit,
  and a catching link with the same name is the re-entrance. It adds no business meaning and only keeps
  diagrams readable.
arc42:
- 6
- 8
step: s10-document
related:
- intermediate-event
- bpmn-event
- bpmn-layout-guideline
- bpmn-modeling-tips
- process-model-complexity
- bpmn-2-0-model-quality
- bpmn-connecting-object
checks:
- Every throwing link event has a catching link event with exactly the same name.
- Each link pair sits within one scope and does not cross a subprocess boundary.
- No link event is used to express business meaning; each one only replaces a sequence flow.
- No throwing link event targets several catching link events if the tool is Camunda.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/link-events/
  title: Link events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.axelor.com/studio/3.3/bpm-docs/BPMN/events/link_event.html
  title: 'Link Event :: Axelor Documentation'
  site: docs.axelor.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: A rejected review jumps back to drafting through a link pair named Rework, with no long return
    line.
review:
  status: generated
  flags: []
---

## Explanation

A link event is a pair of BPMN events that works like a jump. The flow leaves at one event and picks up again at another.

- The **throwing link event** is the exit point.
- The **catching link event** is the re-entrance point.
- The two are matched by their link name. When the flow reaches a throw event, it continues at the catch event with the same name. The names must match exactly.

**What it means.** Link events carry no business meaning. A pair behaves like two plain intermediate events joined by a sequence flow. (The article on Intermediate Event explains that event type.) The pair only makes the diagram easier to draw and read.

**Why use it.** Long flow lines that cross each other can turn a diagram into a "spaghetti" diagram. A link pair removes such a line. You draw an exit and an entrance instead.

**Limits.** Link events work only within one scope. You can link sections of a process inside the same scope. You cannot link across a subprocess boundary.

In Camunda, several throw events can point to the same catch event. One throw event cannot point to several catch events.

## Example

A review process sends rejected work back to the drafting step. Drawing that return line across the whole diagram would cross other flows. Instead, the modeler places a throwing link named "Rework" after the rejection. A catching link named "Rework" sits just before the drafting task. The flow jumps from one to the other, and the diagram stays tidy.

## Trade-offs

Links tidy a diagram, but they come with rules.

- They add no meaning. A link only stands in for a sequence flow, so it cannot express anything new.
- They stay inside one scope. You cannot use them to jump across subprocess boundaries.
- Names must match exactly. The flow continues at the catch event with the same name as the throw event.
- In Camunda, one throw event cannot link to several catch events.
