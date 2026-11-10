---
title: Color Coding in BPMN Models
slug: color-coding-in-bpmn-models
category: modeling-bpmn
kind: practice
summary: Color coding adds a second visual layer to a BPMN diagram, on top of the standard shapes. It
  works best with few colors, a legend, and a diagram that still reads in grayscale.
arc42:
- 8
- 12
step: s10-document
related:
- bpmn-modeling-tools
- bpmn-modeling-tips
- bpmn-2-0-notation-overview
- bpmn-2-0-model-quality
- uml-modeling-best-practice
- self-invented-notation-drawback
checks:
- The diagram uses color for no more than three distinct categories.
- Every colored diagram includes a legend that explains what each color means.
- The diagram has been checked in grayscale and stays readable.
- The diagram has been tested for color blindness, for example with a simulator.
sources:
- url: https://cloud.trisotech.com/bpmnrulebook/bpmn-rule-book/use-of-text-color-size-lines-in-diagram.html
  title: 'Use of Text, Color, Size and Lines in Diagram :: BPMN Rule Book'
  site: cloud.trisotech.com
  accessed: '2026-11-09'
- url: https://skills.visual-paradigm.com/docs/common-dfd-mistakes-and-how-to-avoid-them/dfd-readability-issues/dfd-color-misuse/
  title: 'DFD Color Misuse: Avoiding Visual Noise in Data Flow Diagrams'
  site: skills.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://bpmn.io/blog/posts/2016-colors-bpmn-js
  title: Colors are Here | Blog | bpmn.io
  site: bpmn.io
  accessed: '2026-11-09'
- url: https://github.com/bpmn-io/bpmn-js-examples/blob/main/colors/README.md
  title: bpmn-js-examples/colors/README.md at main · bpmn-io/bpmn-js-examples · GitHub
  site: github.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

BPMN (Business Process Model and Notation) draws process steps with standard shapes. The spec says those shapes may use white or clear fills and black lines. Other colors are an extension that tools add on top of the standard notation. Color is therefore an extra channel, not part of the core meaning of the shapes.

**How tools handle color**

The open-source bpmn-js toolkit from bpmn.io shows how this works in practice:

- Colors work in both the modeler (the editing tool) and the viewer (the read-only display).
- Colors are saved in the BPMN 2.0 XML file, so they travel with the diagram.
- Since version 8.7, bpmn-js saves colors following the BPMN in Color specification.
- Developers set stroke (outline) and fill colors through the `Modeling#setColor` API.
- The core library has no color picker, by design. The picker is a separate extension.

**What this means for modelers**

Color needs deliberate choices. Decide which few categories deserve a color, and write down what each color means. Then apply the colors the same way across every diagram. The saved file keeps the colors, and the viewer shows them.

## Example

A team marks every step that needs a human decision in one color. Every other step keeps the default look. A small legend in the corner of each diagram names that one color. A teammate prints the diagram in black and white. The step names and shapes still carry the meaning. The color only helps the eye find the decision steps faster.

## Trade-offs

Color helps, but it can also mislead.

- **Keep categories few.** One diagramming guide advises never using color for more than three distinct categories. It also says to always include a legend. The guide is written specifically about data flow diagrams.
- **Test without color.** The same guide says to check a diagram in grayscale, which also covers grayscale printing. If it is not readable that way, it is not ready. It also suggests testing for color blindness with simulators.
- **Tool dependence.** Color is a tool-level addition to the notation.
