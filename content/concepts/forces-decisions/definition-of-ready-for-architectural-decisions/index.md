---
title: Architectural Decision Definition of Ready
slug: definition-of-ready-for-architectural-decisions
category: forces-decisions
kind: practice
summary: 'The Architectural Decision Definition of Ready is a checklist of five START criteria: stakeholders,
  time, alternatives, requirements, template. Teams check it before deciding, so they do not decide without
  the key inputs.'
arc42:
- 9
step: s09-decisions
related:
- definition-of-done-for-architectural-decisions
- last-responsible-moment
- raci-matrix
- smart-requirements
- architectural-decision-record
- architectural-decision
- y-statement
- architecturally-significant-requirement
checks:
- The record shows that the stakeholders of the decision were identified, for example in a RACI matrix.
- The decision requirements and drivers are at least identified and drafted, ideally in SMART form.
- An ADR template was chosen and validated before the decision was recorded.
- A decision that passed the START gate is not marked done until the Definition of Done is met.
sources:
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
  title: A Definition of Done for Architectural Decision Making
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The five START criteria as a gate before a decision, followed by the Definition of Done.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

The checklist is modeled on the agile Definition of Ready. In agile work, that concept helps people avoid misunderstandings about how mature an item is. The same idea applies to architectural decisions (see Architectural Decision).

Before making a decision, the team checks five ready-to-START criteria:

1. **Stakeholders.** The people involved in the decision are known. A RACI matrix can group them as Responsible, Accountable, Consulted and Informed (see RACI Matrix).
2. **Time.** The decision is taken at its most responsible moment. Hitting that moment is important.
3. **Alternatives.** The team has options to compare. The companion Definition of Done asks for at least two alternatives, compared by stakeholder concerns.
4. **Requirements.** Requirements and decision drivers are identified and drafted. Ideally they are SMART (see SMART Requirements).
5. **Template.** An ADR template has been chosen and validated, for instance in a trial. It can come from the community or be your own (see Architectural Decision Record).

Passing the START gate does not make a decision done. Feature-oriented readiness and done checklists do not check decisions. So a separate Definition of Done for decisions exists. Its name is ecADR, and it has five criteria: evidence, criteria, agreement, documentation, and realization/review. It asks the team to capture the decision in a lean template such as a Y-statement or MADR. See Definition of Done for Architectural Decisions.

## Example

A team must choose how two systems exchange data. Before the decision meeting, they walk through the checklist. They list who is affected and who must approve. They write down two options. They draft the requirements that matter. They pick an ADR template and try it on a small decision. One item is missing: nobody has drafted the requirements. The team postpones the meeting until that is done.

## Trade-offs

The checklist adds a check before each decision. The check may be easy or take a while, from a single meeting to a longer proof-of-concept project. Requirements only need to be identified and drafted, not perfect. Passing the gate does not finish the work: the decision still needs the Definition of Done.
