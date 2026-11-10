---
title: 'Before you start: what should already exist'
id: before-you-start
review:
  status: generated
  flags:
  - 'unsupported:The business side usually owns business goals (Business goals: Who usually provides it).'
  - 'unsupported:The architect usually drafts the system idea (Vision and system idea: Who usually provides
    it).'
  - unsupported:The architect usually draws the context view with input from stakeholders and neighboring-system
    owners (Scope and context).
  - unsupported:The architect adds detail to functional requirements where decisions need it (Key functional
    requirements).
  - unsupported:Stakeholders rank qualities and the architect turns wishes into scenarios (Top quality
    goals).
  - 'unsupported:Write the system idea last or revise it after quality goals and constraints are known
    (Vision and system idea: If it is missing).'
  - unsupported:Asking people around the project for constraints is a suggested step, not stated in the
    linked articles (Constraints).
  - unsupported:ClinicBook goals, stakeholders, scenarios and constraints are illustrative examples only.
---

## Vision and system idea

**What it is**
The vision is a short statement of the shared goal behind the product. It names the target customers, the value they get, and the few features that make the product stand out. See [Vision Statement](concept:vision-statement). A full vision also covers needs and context, as described in [System Idea and Vision Elements](concept:system-idea-and-vision-elements). The system idea is an early, high-level answer to how the system will be built. In arc42, the closest match is the solution strategy. See [System Idea](concept:system-idea).

**Why you need it**
The vision gives everyone the same picture of the intention and motivation behind the system. The system idea sums up the basic decisions that shape the architecture. Each of those decisions ties back to a quality goal or a key constraint. Without both, the later decisions have nothing to point at.

**Who usually provides it**
Business requirements, including the vision, usually sit in a vision and scope document. See [Requirement Types and Documents (Wiegers/Beatty)](concept:requirement-types-and-documents). Reference that document instead of copying it, as [Architect Settles In Method Phase](concept:architect-settles-in-method-phase) advises. The system idea is the architecture's own first answer, so the architect usually drafts it.

**Good enough is**
A vision that fits in two or three sentences and a rough system idea. Early versions get refined over time. See [Twin Peaks Model](concept:twin-peaks-model).

For ClinicBook, the vision could read: "Patients of 40 small practices book, move and cancel appointments on the web or in an app. Practice staff keep their calendars in sync." The system idea could be one sentence: "Web and mobile clients use one central booking service. One connector per vendor links it to each practice's software." Treat that sentence as a draft. Revise it once the quality goals and constraints are clearer.

**If it is missing**
Write a draft yourself from the vision elements: target group, need, value and context. Mark it as a draft and have the people behind the product confirm it. Write the system idea last, or revise it after you have the quality goals and constraints. Early choices may prove wrong, so record them as revisable. See [Architecture Challenges at Project Start](concept:architecture-challenges-at-project-start).

## Business goals

**What it is**
Business goals say what the organization wants to achieve with the system. They count as business requirements and belong in a vision and scope document, apart from detailed software requirements. See [Requirement Types and Documents (Wiegers/Beatty)](concept:requirement-types-and-documents). The [Business Model Canvas](concept:business-model-canvas) describes the business on one page. It covers who the business serves, what it offers, how it delivers, and what it costs and earns.

**Why you need it**
The value in a vision links to business goals and the business case. An important requirement is tied to business value, risk, or a key stakeholder's concern. See [Architecturally Significant Requirement](concept:architecturally-significant-requirement). Without goals, you cannot tell which requirements deserve the most design effort.

**Who usually provides it**
The business side of the organization usually owns these goals. The architect collects them from existing documents. If you cite a canvas, date it and give it a version.

**Good enough is**
A short list of goals, each with one line of reasoning. For ClinicBook, it could say: bring all 40 practices onto the platform by the fixed launch date; give patients an easy way to book, move and cancel; keep health data trustworthy. Each goal should connect to a stakeholder's concern.

**If it is missing**
Derive draft goals from the vision. Write them down as assumptions and ask the business side to correct them. If a canvas exists, read it for customers and partners. See [Stakeholder](concept:stakeholder).

## Stakeholders and their concerns

**What it is**
A stakeholder is a person, team, organization, or class of such parties with an interest in the system. See [Stakeholder](concept:stakeholder). A concern is something a stakeholder cares about, such as performance, security or maintainability. See [Concern](concept:concern) and [Stakeholder Concern](concept:stakeholder-concern).

**Why you need it**
Architects must balance different needs. Concerns can conflict, for example time-to-market against maintainability. The chosen trade-off must be explicit. A stakeholder list helps avoid surprises later in development. Every concern should be addressed in the architecture description.

**Who usually provides it**
The architect finds stakeholders, using guiding questions: who gains or loses, who decides, who controls resources. See [Stakeholder Identification](concept:stakeholder-identification). Every stakeholder class needs a representative.

**Good enough is**
A table with role or name, contact, expectations and concerns. Cover every class of stakeholder.

For ClinicBook, the table could include:

- Patients: easy booking, privacy of their health data.
- Practice staff: reliable calendars, especially in the morning peak.
- Vendors of practice-management software: a clear interface to connect to.
- Practice owners: a working system by the launch date.
- The development team: a design that a small team can maintain.

To decide how closely to engage each group, see [Stakeholder Power Grid](concept:stakeholder-power-grid).

**If it is missing**
Answer the guiding questions yourself and write a first table. Add each stakeholder's main concern. Then ask the people on the list what you missed. Check that no class is left out.

## Scope and context

**What it is**
The scope says where the system starts and ends. A [Context View](concept:context-view) shows the system as a black box with its communication partners around it. It shows what data the system exchanges with them. The business context shows data flows. The technical context shows channels and transmission media. See [Refining Complex Context Views](concept:refining-complex-context-views).

**Why you need it**
Everyone can see the boundary of the system and who it talks to. Interfaces to neighboring systems become visible early. Risks can be marked directly in the context.

**Who usually provides it**
The architect usually draws it, with input from the stakeholders and from the owners of neighboring systems.

**Good enough is**
One overview diagram plus a table with one row per communication partner. Label each flow with the data exchanged. Draw both directions where data moves both ways. See [Context View Antipattern: Forgetting Bidirectional Data Flows](concept:context-view-antipattern-forgetting-bidirectional-data-flows).

For ClinicBook, the partners are patients (web and app), practice staff, the practices' management software from several vendors, an SMS channel and an e-mail channel. The flows with the practice software run both ways. ClinicBook sends booked appointments out. Changes made in the practice software come back in. Mark the differing vendor interfaces as a risk. With many vendors, group them by an explicit criterion.

**If it is missing**
Sketch the black box and list every neighbor, including users. Put each one in the table. Mark unknown interfaces as risks. Refine the sketch as you learn more.

## Key functional requirements

**What it is**
Functional requirements say what the system must do. A requirement is precise enough when developers have no more questions. See [Working with Functional Requirements (method phase)](concept:method-phase-working-with-functional-requirements). They can take the form of a [Use Case](concept:use-case) or a [User Story](concept:user-story).

**Why you need it**
Architecture needs a short description of what the system does. It also needs more detail for the subset that drives architectural decisions. Functional requirements stay separate from quality requirements and constraints. Large ones are split into parts that each still offer business value. The allocation of functions to parts also depends on quality requirements. See [Responsibility Allocation](concept:responsibility-allocation).

**Who usually provides it**
Existing requirements documents hold them. Refer to those documents instead of duplicating them. The architect adds detail where decisions need it.

**Good enough is**
A brief list that points to the existing documents. For ClinicBook:

- A patient books an appointment.
- A patient moves an appointment.
- A patient cancels an appointment.
- Practice staff manage their calendar.
- The system sends reminders by SMS and e-mail.
- The system exchanges appointments with the practice software.

"Manage calendar" is too vague. Split it by operation, for example view, block time and change an appointment. See [Story Splitting](concept:story-splitting). Write use cases at user-goal level. See [Use Case Goal Level](concept:use-case-goal-levels).

**If it is missing**
Write the short list above from the vision and check it with stakeholders. Detail only the requirements that affect architectural decisions. Accept that the list is incomplete and will change. See [Requirements Trawling](concept:requirements-elicitation).

## Top quality goals

**What it is**
Quality goals are the few qualities that matter most, such as security or availability. Teams cannot maximize every quality at once. arc42 asks for the top three, at most five, in a table ordered by priority. Each goal gets at least one concrete scenario. Lesser quality requirements go to section 10. See [Quality Attribute Prioritization](concept:quality-attribute-prioritization). A scenario is a specific, measurable statement. See [Quality Attribute Scenario](concept:quality-attribute-scenario).

**Why you need it**
Improving one quality usually costs another. See [Quality Attribute Trade-off](concept:architectural-trade-off-thinking). Quality goals shape a system as much as features do. State them concretely and early. See [Insufficient Quality as Driver of Change](concept:insufficient-quality-as-driver-of-change).

**Who usually provides it**
Stakeholders rank the qualities by importance. The architect turns vague wishes into scenarios.

**Good enough is**
A table of three to five goals, ordered, each with one scenario. Use standard names to avoid ambiguity. See [ISO/IEC 25010 Product Quality Model](concept:iso-iec-25010-quality-model) and [Standard Quality Attribute List](concept:standard-quality-attribute-checklist).

For ClinicBook, a first ranking could be:

1. [Confidentiality](concept:confidentiality). An unauthorized user tries to read another patient's appointment data. The system denies access and records the attempt in an audit trail.
2. [Availability](concept:availability). During the morning peak, one server fails. Patients can still book. Agree the exact time limit and percentage with the stakeholders. See [Availability Scenario](concept:availability-scenario).
3. [Interoperability](concept:interoperability). ClinicBook sends a new appointment to a practice's software. If the software rejects it, practice staff are notified. See [Interoperability Scenario](concept:interoperability-scenario).

**If it is missing**
Pick candidates from the standard list and rank them with the stakeholders. Write one scenario per top goal. Leave the rest for section 10.

## Constraints (technical)

**What it is**
A constraint is a requirement that limits how freely architects can design and build. Teams must deal with it, though some constraints can be negotiated. See [Architectural Constraint](concept:requirements-versus-constraints). Constraints fall into groups: technical, organizational or political, and conventions. They differ from forces, which you weigh against each other. See [Architectural Force](concept:architectural-forces).

**Why you need it**
A written list shows where the design is free and where it is bound. It stops you from spending effort on options that are not allowed. Keep organization-wide constraints apart from system-specific ones.

**Who usually provides it**
Each constraint has someone who wants it, and that party can explain why. Record both.

**Good enough is**
One list, in one place. For each constraint, give who wants it, why, what it costs in extra effort, and whether it is negotiable.

For ClinicBook, one technical entry could be: "Practice-management software stays in place. ClinicBook must use the interfaces each vendor offers. Wanted by the practices, who use that software daily. Consequence: extra integration work per vendor. Not negotiable in the short term." The fixed launch date and the small team are pressures. Weigh them against other goals, unless someone declares them fixed.

**If it is missing**
Ask the people around the project which technology, organizational and convention limits exist. Write each one down with its source. Mark unclear ones as "negotiability unknown". See [Architect Settles In Method Phase](concept:architect-settles-in-method-phase).
