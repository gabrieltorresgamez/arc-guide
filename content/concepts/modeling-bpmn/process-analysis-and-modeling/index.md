---
title: Process Analysis and Modeling
slug: process-analysis-and-modeling
category: modeling-bpmn
kind: practice
summary: Process analysis and modeling draws a picture of how work gets done. Notations such as BPMN and
  EPC make that picture shared and precise. BPMN models can also be turned into software.
long_ok: true
arc42:
- 3
- 6
- 8
step: s03-functional-requirements
related:
- bpmn-2-0-notation
- bpmn-swimlane-pool-and-lane
- as-is-and-to-be-view
- business-capability
checks:
- Process models use a named, standard notation such as BPMN 2.0 or EPC.
- Actors are shown as pools and lanes at the top-level process or collaboration, not inside subprocesses.
- Exception paths are modeled, for example with events that interrupt a subprocess.
- Where a BPMN model is meant for execution, the same model serves as documentation and as the executable
  artifact.
sources:
- url: https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-primer/
  title: BPMN primer | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0/
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-08'
- url: https://www.omg.org/spec/BPMN/2.0.2/About-BPMN
  title: About the Business Process Model and Notation Specification Version 2.0.2
  site: omg.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Event-driven_process_chain
  title: Event-driven process chain - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.signavio.com/wiki/process-discovery/business-process-mapping-levels/
  title: Business Process Mapping Levels - SAP Signavio
  site: signavio.com
  accessed: '2026-11-09'
- url: https://www.bpminstitute.org/resources/articles/bpms-watch-organizing-complex-bpmn-models/
  title: 'BPMS Watch: Organizing Complex BPMN Models | BPMInstitute.org'
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://www.trisotech.com/bpmn-call-activity-vs-subprocess-whats-the-difference/
  title: 'BPMN Call Activity vs Subprocess: What''s the Difference?'
  site: trisotech.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/call-activities/
  title: Call activities | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://camunda.com/blog/2024/05/what-is-business-process-modeling/
  title: What is Business Process Modeling? | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/none-events/
  title: None events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/naming-bpmn-elements/
  title: Naming BPMN elements | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/modeling-beyond-the-happy-path/
  title: Modeling beyond the happy path | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
  title: Exclusive gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models/
  title: Creating readable process models | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/message-events/
  title: Message events | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://www.omg.org/spec/BPMN/2.0/About-BPMN
  title: About the Business Process Model And Notation Specification Version 2.0
  site: omg.org
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/modeler/bpmn/parallel-gateways/
  title: Parallel gateway | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-08'
- url: https://research.tue.nl/p/en/research-outputs/seven-process-modeling-guidelines-7pmg
  title: Seven process modeling guidelines (7PMG) — Eindhoven University of Technology Research Portal
  site: research.tue.nl
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/reference/glossary/
  title: Glossary | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://docs.camunda.io/docs/components/best-practices/development/routing-events-to-processes/
  title: Routing events to processes | Camunda 8 Docs
  site: docs.camunda.io
  accessed: '2026-11-09'
- url: https://ar5iv.labs.arxiv.org/html/1408.5094
  title: '[1408.5094] Verifiable UML Artifact-Centric Business Process Models'
  site: ar5iv.labs.arxiv.org
  accessed: '2026-11-09'
- url: https://ar5iv.labs.arxiv.org/html/1303.2554
  title: '[1303.2554] Artifact Lifecycle Discovery'
  site: ar5iv.labs.arxiv.org
  accessed: '2026-11-09'
- url: https://ariscommunity.com/help/aris-express/35908
  title: Event | ARIS BPM Community
  site: ariscommunity.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Process_mining
  title: Process mining - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.celonis.com/insights/topics/what-is-process-mining
  title: What is Process Mining? Definition and benefits | Celonis
  site: celonis.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/IEEE_1849
  title: IEEE 1849 - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.tf-pm.org/resources/manifesto
  title: Process Mining Manifesto - IEEE Task Force on Process Mining
  site: tf-pm.org
  accessed: '2026-11-09'
- url: https://www.signavio.com/wiki/bpm/business-process-management-lifecycle/
  title: 'Business Process Management Lifecycle: 5 Phases - SAP Signavio'
  site: signavio.com
  accessed: '2026-11-09'
- url: https://www.signavio.com/wiki/process-discovery/as-is-to-be-process-mapping/
  title: As-Is and To-Be Process Mapping - SAP Signavio
  site: signavio.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_process_management
  title: Business process management - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.destinationcrm.com/Articles/CRM-News/CRM-Featured-Articles/Gartner-Releases-Its-Magic-Quadrant-for-BPM-Suites--71757.aspx
  title: Gartner Releases Its Magic Quadrant for BPM Suites
  site: destinationcrm.com
  accessed: '2026-11-10'
- url: https://column2.com/2007/09/gartner-day-2-michele-cantara/
  title: 'Gartner Day 2: Michele Cantara – Column 2'
  site: column2.com
  accessed: '2026-11-10'
- url: https://camunda.com/process-orchestration/
  title: 'Process Orchestration: Guide to Benefits & Software | Camunda'
  site: camunda.com
  accessed: '2026-11-09'
- url: https://www.ibm.com/think/topics/straight-through-processing
  title: What Is Straight-Through Processing? | IBM
  site: ibm.com
  accessed: '2026-11-09'
- url: https://camunda.com/orchestrate/building-blocks/
  title: 'Process Building Blocks: Decisions, RPA & IDP | Camunda'
  site: camunda.com
  accessed: '2026-11-09'
- url: https://aisel.aisnet.org/ecis2005/37/
  title: '"Towards a Business Process Managment Maturity Model" by Michael Rosemann and Tonia de Bruin'
  site: aisel.aisnet.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_process_re-engineering
  title: Business process re-engineering - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.nicholascarr.com/?page_id=99
  title: IT Doesn’t Matter | Nicholas Carr
  site: nicholascarr.com
  accessed: '2026-11-09'
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
diagrams:
- file: diagram-1.bpmn
  caption: An order process with two lanes and an interrupting cancellation path.
review:
  status: generated
  flags: []
---

## Explanation

**Notations.** Several notations exist for modeling business processes. Two appear here.

- BPMN (Business Process Model and Notation) 2.0 is an industry standard for process modeling and execution. Its notation looks like a flowchart and does not depend on any particular implementation environment. See the article *BPMN 2.0 Notation*.
- EPC (event-driven process chain) is an ordered graph of events and functions. It is also a notation for business process modeling. See *Process Notations Comparison (EPC, BPMN, UML Activity Diagram)*.

**Who uses the models.** BPMN is aimed at the people who design, manage, and realize business processes. Its specification asks for enough precision that diagrams can be translated into software process components. That bridges business design and implementation.

**One model, two uses.** A BPMN process is an XML document that also has a visual form. So the same model can serve as documentation and as an executable artifact.

**Actors and responsibilities.** BPMN shows participants with pools and lanes. These exist only at the top-level process or collaboration level. They cannot appear inside a subprocess. See *BPMN Swimlane (Pool and Lane)*.

**Failure paths.** A model should cover more than the smooth case. In BPMN, an event can interrupt a subprocess, whichever step inside it is active.

**More about process analysis and modeling.**

- **Levels of Process Modeling:** Process models work best in levels. The top level shows the big picture, the middle level breaks it into subprocesses, and the lowest level shows detailed activities. Each level suits a different audience.
- **Capturing Business Behavior via Process Modeling:** Process models describe business behavior at different levels of detail. A high-level model explains a process to stakeholders. A more detailed one supports analysis. A BPMN model can also be run by a workflow engine.
- **Structured Process Modeling with Fragments:** In BPMN, structured blocks use parallel gateways (AND) and exclusive gateways (XOR) as splits and joins.
- **Process Model versus Process Instance:** A process model is the blueprint of a business process. A process instance is one run of it, tracked by a token.
- **Business Object Lifecycle:** A business object lifecycle describes the states an object passes through, drawn as a state machine. Processes change those states. This data-centric view is an alternative to modeling only the activities of a process.
- **Process Mining:** Process mining is a family of techniques that analyze event data from information systems. It shows how a process actually runs, not how people believe it runs, and helps improve it.
- **BPM Life Cycle:** The BPM life cycle is a loop of stages for a business process: discovery, analysis, design, implementation and optimization. A live process is measured and improved so it stays useful as goals, technology and rules change.
- **BPM Usage Scenario:** A BPM usage scenario is a typical reason for buying a business process management suite (BPMS). Four are described: automating one process, continuous improvement, moving to SOA, and business transformation. Each has different buyers and goals.
- **Degrees of BPM Maturity:** Processes can be automated to different degrees, from steps with people involved to straight-through processing with no human at all. RPA and AI agents help move a process along.
- **Waves of Business Process Management:** Business process thinking has changed over time. In 1990, Hammer argued for removing work that adds no value instead of automating it [src:37]. Reengineering then drew criticism, among other things for downsizing.
- **ARIS Process Views:** ARIS describes a business and its information systems through several views, and each view is detailed in three levels [src:39]. Process chain diagrams belong to its control view. ARIS mainly supports analysis and requirements definition.

## Example

A company models how it handles a customer order. The top-level process has two lanes: sales and warehouse. A "pack and ship" subprocess sits in the warehouse lane. A "customer cancels" event is attached to that subprocess. If the event fires, the subprocess stops, whichever step is running, and the process follows the cancellation path. Business staff read the diagram. The same model can also be handed to a system to run.

## Trade-offs

Lanes work only at the top level. They cannot be added inside a subprocess.
