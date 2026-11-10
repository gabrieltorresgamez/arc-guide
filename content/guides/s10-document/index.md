---
title: 'Step 10: Model and document'
id: s10-document
review:
  status: generated
  flags:
  - unsupported:ClinicBook's container list, scenario choices, protocols (HTTPS) and deployment nodes
    are invented for illustration and are not supported by the articles.
  - unsupported:The listed readers for ClinicBook (practice managers, developers, operations contact,
    privacy contact) are invented for illustration.
  - unsupported:The claim that a short document suits a small team with a fixed launch date is an application
    of the guidelines article, not a statement in it.
---

## What you get from this step

You get a first written version of four arc42 sections:

- **Section 3, Context and Scope:** the system as a black box, with the people and systems around it.
- **Section 5, Building Block View:** the static parts of the system, in levels.
- **Section 6, Runtime View:** a few chosen scenarios that show how the parts work together.
- **Section 7, Deployment View:** which parts run on which infrastructure.

Each diagram has a named audience, a title, a legend and a clear type. Readers can find what they need without asking the author. The [arc42 Architecture Documentation Template](concept:arc42-documentation-template) gives each of these topics a fixed place.

## What you need first

- A list of stakeholders (people with an interest in the system) and what each expects. See [Stakeholder Perspective and Concern](concept:stakeholder-perspective-and-concern).
- Your top three to five quality goals from section 1. See [arc42 Introduction and Goals](concept:arc42-introduction-and-goals).
- Your constraints from section 2. See [arc42 Constraints](concept:arc42-constraints).
- The first big solution decisions from section 4. See [Solution Strategy](concept:arc42-solution-strategy).
- A list of the users and neighboring systems that talk to your system.

## If something is missing

- **No stakeholder list:** Ask the people who will read the document what they expect from it. Write the answers down. Pick views from their questions, as in [Stakeholder Questions Addressed in Views](concept:stakeholder-questions-addressed-in-views).
- **No quality goals:** Name the three that matter most to the major stakeholders. Fix them before you draw. They help you decide where to add detail.
- **No list of communication partners:** Start with the context diagram. Drawing it forces you to list every user and neighboring system.
- **Decisions only in people's heads:** Write them down as proposed decisions with a reason. The [Architecture Canvas](concept:architecture-canvas) suggests drafting assumptions as decision records.

## How to do it

1. **Name the readers and their questions.** Write down who reads each section and why. Every diagram states its notation, audience and purpose ([View Creation Method](concept:view-creation-method)). Include only what a named reader will use ([Guidelines for Documentation](concept:guidelines-for-documentation)).
2. **Agree on a small modeling method.** Every diagram gets a title with its type and scope, plus a legend. Every arrow gets a specific label. Use color the same way in all diagrams. See [Modeling Method](concept:modeling-method) and [Rules of Thumb for Modeling](concept:rules-of-thumb-for-modeling). Avoid made-up symbols ([Self-Invented Notation Drawback](concept:self-invented-notation-drawback)). Choose C4, UML or BPMN on purpose, and say which you use ([Why Use UML in Architecture Documentation](concept:why-use-uml-in-architecture-documentation)). If you keep diagrams as text in version control, see [Diagrams as Code](concept:diagrams-as-code).
3. **Write section 3: the context.**
   - Draw the system as one black box. A black box shows only what is visible from outside.
   - Put users and neighboring systems around it.
   - Label each arrow with the data that flows, not just "uses".
   - Add a table that describes each interface.
   - Keep the technical context apart. It shows which channel or protocol carries each data flow.
   - A [C4 System Context Diagram](concept:c4-level-1-system-context-diagram) is a good first diagram. See [Business and Technical Context](concept:business-and-technical-context) and [Context View Antipatterns](concept:context-view-antipatterns).
4. **Write section 5, level 1: the big parts.**
   - Draw the white box of the whole system. A white box shows the black boxes inside it.
   - Describe each block's responsibility and interfaces.
   - A [Container Diagram (C4 Level 2)](concept:c4-container-diagram) fits here. A container is a separately running application or a data store, such as a database.
   - Show the main technology of each container. Leave clustering and load balancing for the deployment view.
   - Group blocks by responsibility. Do not copy code packages ([Component View Antipattern: Lifting Code to Model Level](concept:component-view-antipattern-lifting-code-to-model-level)).
5. **Refine only where it pays off.** Zoom into a block only if it is important, risky, complex or volatile. Leave simple or standard blocks as black boxes. See [Component View Refinement Levels](concept:component-view-refinement-levels). A [C4 Component Diagram](concept:c4-level-3-component-diagram) opens up exactly one container. Draw one only when it adds value. Code-level diagrams are rarely needed, and tools can generate them ([C4 Level 4: Code Diagram](concept:c4-level-4-code-diagram)).
6. **Write section 6: a few scenarios.**
   - Pick scenarios for architectural relevance, not completeness. Good candidates are key use cases, external interfaces, start-up or administration, and error cases ([Runtime View](concept:runtime-view)).
   - Use a [UML Sequence Diagram](concept:sequence-diagram) to show how building blocks exchange messages. Separate synchronous from asynchronous messages ([Message Types in Sequence Diagrams](concept:message-types-in-sequence-diagrams)).
   - Use BPMN when a business process crosses several parties. A [BPMN Collaboration Diagram](concept:bpmn-collaboration-diagram) gives each party its own pool and connects pools with message flows.
   - Make every step belong to a building block from section 5. Do not describe code-level steps ([Runtime View Antipattern: Code-Level Activity Diagram](concept:runtime-view-antipattern-code-level-activity-diagram)).
   - Check each BPMN model for deadlock and lack of synchronization ([Soundness of Process Models](concept:soundness-of-process-models)).
7. **Write section 7: the deployment.**
   - Draw a [UML Deployment Diagram](concept:deployment-diagram). Put software artifacts on the nodes that run them.
   - Draw one environment per diagram, for example production.
   - Show infrastructure such as load balancers and firewalls where they matter.
   - Label each connection with its protocol.
   - Explain how the infrastructure shapes the system.
   - See [Deployment View](concept:distribution-view), [Distribution View Antipatterns](concept:distribution-view-antipatterns) and [Deployment Diagram Modeling Mistake](concept:deployment-diagram-modeling-mistakes).
8. **Describe each thing once.** Give an interface its full description in one place. Other places only point to it ([Undetected Duplication Antipattern](concept:undetected-duplication-antipattern)). Keep detail at one abstraction level per diagram ([Unclear Level of Abstraction Antipattern](concept:unclear-level-of-abstraction-antipattern)).
9. **Name an owner.** One named person is responsible for the amount and quality of the documentation ([Guidelines for Documentation](concept:guidelines-for-documentation)).

## Example: ClinicBook

ClinicBook is an online booking system for 40 small medical practices. The main forces are privacy and security, availability in morning peaks, legacy integration, a small team and a fixed launch date. The design choices below are illustrations for this example.

**Readers.** The practice managers want to know what the system exchanges with their software. The developers need the building blocks. The operations contact needs the deployment. Whoever handles privacy asks where health data goes. The documentation stays short because the team is small and the launch date is fixed.

**Section 3.** The business context shows ClinicBook as one black box. Around it sit:

- patients, using the web and the mobile app,
- practice staff,
- the practice-management software of each vendor,
- an SMS provider,
- an e-mail provider.

The arrows carry data, for example "appointment request", "calendar changes" and "reminder text". A table lists each interface. A separate technical context diagram shows the channel for each flow. For example, the patient and staff flows might run over HTTPS. The flows to practice software go through vendor-specific interfaces. The privacy contact can see every flow that carries health data.

**Section 5.**

- *Level 1:* A container diagram shows:
  - a web app,
  - a mobile app,
  - a booking service,
  - a booking database,
  - a reminder service,
  - a practice integration part.
- Each container has a short description and its main technology.
- *Level 2:* Only the practice integration part gets a component diagram. It is the volatile, risky part, because each vendor's software differs. The booking service and reminder service stay as black boxes until someone needs more detail. The component names describe responsibilities, such as "Calendar synchronization", not "Facade" or "Service".

**Section 6.** Three scenarios cover what matters:

1. *Patient books an appointment in a morning peak.* A sequence diagram shows the apps, the booking service, the database and the practice integration. It marks which calls the caller waits for and which run asynchronously.
2. *Practice software is unreachable.* This error case shows how the booking service and the practice integration behave.
3. *Patient moves an appointment.* A BPMN collaboration diagram gives the patient, ClinicBook and the practice software one pool each. Message flows connect the pools. The team checks the model for deadlock and lack of synchronization.

Each step in all three scenarios belongs to a container or component from section 5.

**Section 7.** One deployment diagram covers production. It maps the containers to nodes. It shows the load balancer and firewall, because peak availability and privacy depend on them. Each connection carries its protocol label. A short text explains how the infrastructure supports the availability goal. Staging gets its own diagram only if it differs in a way readers care about.

Every diagram has a title with type and scope, a legend and labeled arrows. One named team member owns the documents.

## Done when

- Every diagram has a title with type and scope, a legend and labeled arrows. See [Rules of Thumb for Modeling](concept:rules-of-thumb-for-modeling).
- Section 3 shows the system as a black box with all communication partners. The technical context sits in a separate view. See [Business and Technical Context](concept:business-and-technical-context).
- Section 5 has a level 1 white box. Deeper levels exist only for important, risky, complex or volatile blocks. See [Component View Refinement Levels](concept:component-view-refinement-levels).
- Section 6 has a few architecturally relevant scenarios. Each step maps to a building block. See [Runtime View](concept:runtime-view).
- Section 7 maps building blocks to infrastructure, one environment per diagram. See [Distribution View Antipatterns](concept:distribution-view-antipatterns).
- Each view names the readers and concerns it serves. See [Architecture View](concept:architecture-view).
- Any BPMN model has been checked for soundness. See [Soundness of Process Models](concept:soundness-of-process-models).

## Learn more

**Why and how to document**

- [Motivation for Architecture Documentation](concept:motivation-for-architecture-documentation)
- [Guidelines for Documentation](concept:guidelines-for-documentation)
- [Software Architecture Documentation Consensus](concept:software-architecture-documentation-consensus)
- [Characteristics of a Good View](concept:characteristics-of-a-good-view)
- [Architecture Viewpoint](concept:architecture-viewpoint)
- [Model vs. View](concept:model-vs-view)

**Context and structure**

- [arc42 Context and Scope](concept:arc42-context-and-scope)
- [Component View](concept:component-view)
- [C4 Model](concept:c4-model)
- [Architectural Overview Diagram](concept:architectural-overview-diagram)
- [Architectural Overview Antipattern](concept:architectural-overview-antipatterns)
- [Matching Diagram Type to System Aspect](concept:matching-diagram-type-to-system-aspect)
- [UML Component Diagram](concept:uml-component-diagram)

**Runtime and deployment**

- [Essential Architecture Views (Context, Component, Runtime, Distribution)](concept:contemporary-essential-views)
- [Process-Application-Infrastructure Mapping](concept:process-application-infrastructure-mapping)
- [Additional Architecture Viewpoints (Security, Information, Operational, Development, Process, Evolution)](concept:additional-architecture-views-and-perspectives)

**BPMN**

- [BPMN 2.0 Notation](concept:bpmn-2-0-notation-overview)
- [BPMN Core Elements](concept:bpmn-core-elements)
- [BPMN Modeling Guidelines](concept:bpmn-modeling-tips)
- [BPMN Layout Guideline](concept:bpmn-layout-guideline)

**Tooling**

- [Documentation as Code](concept:documentation-as-code)
- [Diagrams as Code](concept:diagrams-as-code)
- [Modeling Tool vs. Drawing Tool](concept:modeling-tool-vs-drawing-tool)
- [Kroki](concept:kroki)
- [Diagram Metadata in PNG (drawio.png)](concept:diagram-metadata-in-png-drawio-png)
