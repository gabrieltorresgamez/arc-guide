---
title: ARIS Process Views
slug: aris-process-views
category: modeling-bpmn
kind: framework
summary: ARIS describes a business and its information systems through several views, and each view is
  detailed in three levels. Process chain diagrams belong to its control view. ARIS mainly supports analysis
  and requirements definition.
arc42:
- 6
- 12
step: s10-document
related:
- process-notations-comparison
- bpmn-2-0-notation-overview
- levels-of-process-modeling
- architecture-view
- bpm-life-cycle
- capturing-business-behavior-via-process-modeling
checks:
- The document states which ARIS version it follows (four views or five).
- Each ARIS view is described at the requirements, design and implementation levels.
- Process chain diagrams are filed under the control view.
sources:
- url: https://en.wikipedia.org/wiki/Architecture_of_Integrated_Information_Systems
  title: Architecture of Integrated Information Systems - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.pera.net/Methodologies/ARIS/ARIS.HTM
  title: ARIS ARchitecture of Integrated Information Systems
  site: pera.net
  accessed: '2026-11-09'
- url: https://ariscommunity.com/users/sstein/2009-10-23-what-aris
  title: What is ARIS? | ARIS BPM Community
  site: ariscommunity.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ARIS is a framework for describing business processes and the information systems that support them. Its overall structure is called the ARIS house. The house is divided into description views. Each view looks at the same business from one angle.

**How many views?** Sources differ. A 1990s description names four views: organization, function, information and control. The later house has five views.

**Three levels per view.** Each view is split into three description levels. The levels follow the stages of the software life cycle: requirements definition, design specification and implementation. So you describe a view first in business terms, then as a design, then as something built.

**Where ARIS is used.** ARIS mainly targets the analysis and requirements definition phase. That is the early phase when you design an information system.

**Control view and notations.** Process chain diagrams are tied to the control view. EPC (event-driven process chain) is one of the notations used with ARIS. Others on the same list are BPMN, BPEL, UML and ERM. So BPMN is one possible notation within ARIS work. For the notations themselves, see "Process Notations Comparison (EPC, BPMN, UML Activity Diagram)" and "BPMN 2.0 Notation".

## Example

A team documents an order-handling process. They keep the process-flow diagrams in the control view. For each view they write three descriptions: first the business requirements, then the design, then the implementation. Readers who care about one angle read only that view.

## Trade-offs

Sources disagree on the number of views: four in an early description, five in the later house. State which version you follow. ARIS focuses on analysis and requirements definition, so it says less about later phases.
