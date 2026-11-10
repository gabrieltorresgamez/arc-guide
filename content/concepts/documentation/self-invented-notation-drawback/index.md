---
title: Self-Invented Notation Drawback
slug: self-invented-notation-drawback
category: documentation
kind: concept
summary: A self-invented notation is a set of diagram symbols the author made up. Readers cannot tell
  what the symbols mean without help. A legend, or a standard notation, reduces the problem.
arc42:
- 3
- 5
- 6
- 7
- 8
step: s10-document
related:
- c4-model
- uml-unified-modeling-language
- guidelines-for-documentation
- uml-modeling-anti-patterns
- architectural-overview-antipatterns
- why-use-uml-in-architecture-documentation
- iso-iec-ieee-42010-architecture-description-standard
- architecture-viewpoint
checks:
- Every diagram carries a legend or key.
- The legend explains shapes, colors, border styles, line types and arrow heads used in the diagram.
- Any non-standard notation is accompanied by a legend.
- Colors, shapes and line styles are used consistently across diagrams.
sources:
- url: https://c4model.com/introduction
  title: Introduction | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/notation
  title: Notation | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/activities/DPR-ArchitectureModeling.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2008.11060
  title: '[2008.11060] Applying system descriptors to address ambiguity on deployment diagrams'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Many architecture diagrams are drawn as free-style boxes and lines. The notation, such as colors, shapes and line styles, is often not explained or is inconsistent.

**What goes wrong**

- The notation is not explained, or it is used inconsistently. Colors, shapes, line styles and element sizes may all be affected.
- The purpose and meaning of elements stay ambiguous.
- Diagrams drift as a system changes. Research on deployment diagrams in a DevOps context reports that diagrams commonly become ambiguous or inconsistent as the system progresses.

**Why teams end up here**

Developers asked to diagram an architecture often produce a confused mess of boxes and lines. Many teams dropped UML (see Unified Modeling Language (UML)) in favor of much simpler boxes and lines.

**Mitigations**

- Add a legend (also called a key) to every diagram. It should explain shapes, colors, border styles, line types and arrow heads.
- Keep the legend even when using UML, ArchiMate or SysML, because not everybody will know the notation being used.
- The C4 model (see C4 Model) prescribes no particular notation. It still recommends a key on every diagram.
- A design practice repository describes notations as ranging from ad hoc and informal to full-fledged. It says a non-standard notation needs a legend.

## Example

A team draws a diagram with blue boxes, green boxes, a dashed arrow and a solid arrow. The author means blue as "built by us" and dashed as "asynchronous call". A new colleague reads blue as "database" and dashed as "optional". Nothing on the page settles who is right. Adding a small legend that lists each color and line style removes the guesswork.

## Trade-offs

Free-style boxes and lines tend to bring ambiguity and confusion. Whatever notation is used, a legend is recommended.
