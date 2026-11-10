---
title: Context View Antipatterns
slug: context-view-antipatterns
category: documentation
kind: concept
summary: 'A context diagram shows one system as a black box, with its direct neighbors and the data exchanged.
  Common mistakes blur this view: unlabeled arrows, system internals, unclear boundaries, or too much
  detail.'
arc42:
- 3
step: s02-scope-context
related:
- context-view
- context-view-antipattern-forgetting-bidirectional-data-flows
- business-and-technical-context
- arc42-context-and-scope
- c4-level-1-system-context-diagram
- refining-complex-context-views
- distribution-view
- component-view
checks:
- Every arrow carries a label naming the data that flows, and a legend explains the notation.
- The diagram shows the system as a black box with no internals.
- The system boundary is explicit and separates the system from its environment.
- The diagram stays an overview, without technologies, protocols or low-level detail.
- Business context and technical context are kept apart, and the diagram is paired with a table.
sources:
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/3-5/
  title: 'Tip 3-5: Restrict the context to an overview, avoid too many details! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-ContextDiagram.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/3-11/
  title: 'Tip 3-11: In the business context, show data flows (instead of dependencies)! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams/system-context
  title: System context diagram | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A corrected context view: black box, named neighbors, one labeled arrow per data flow.'
review:
  status: generated
  flags: []
---

## Explanation

A context view (see Context View) shows your system from the outside. The system is a black box. Around it sit its communication partners, such as users and other IT systems. The antipatterns below, meaning common mistakes, pull the diagram away from that purpose.

**Unlabeled arrows.** Many people read an arrow between software systems as a data flow. arc42 therefore advises showing data flows, not dependencies. Each arrow should tell readers what data moves and in which direction. Leaving arrows unnamed fails this goal. The Design Practice Repository says to label all arrows and explain their meaning in a legend.

**Showing system internals.** A context diagram gives an outside view only. Do not mix in a white-box view, which shows the parts inside the system. Instead of stopping at the outside view, zoom in with a container diagram.

**Unclear boundary.** arc42 tells authors to demarcate the system explicitly from its environment. Readers must see what is inside and what is outside.

**Too much detail.** arc42 recommends keeping the context an overview and avoiding too many interface details. It gives a counter-example with too many details. The C4 system context diagram follows the same idea. It covers a single system and focuses on people and software systems, not on technologies, protocols or low-level details.

**Mixing business and technical context.** The business context shows domain interfaces to partners. The technical context shows the channels and transmission media that link the system to its environment. arc42 advises differentiating the two where necessary. See Business and Technical Context.

**Diagram without a table.** arc42 recommends pairing the context diagram with a table. It also lists a tip to show all external interfaces.

## Example

An online shop draws its context. A bad version shows one box labeled "Backend" inside the shop, a two-headed arrow to "External system", and an arrow labeled "process payment". A better version shows the shop as one black box. Two arrows connect it to a payment provider: "payment request" goes out, "payment result" comes back. A table lists each partner and interface.

## Trade-offs

Keeping the diagram to an overview means some detail is left out. arc42 says to document all external interfaces, though categorization or abstraction is a valid way to stay concise.
