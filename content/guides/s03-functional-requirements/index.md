---
title: 'Step 3: Capture the key functional requirements'
id: s03-functional-requirements
review:
  status: generated
  flags:
  - unsupported:Selecting items that touch main quality needs or outside systems as the ones that matter
    most for architecture is an inference from Responsibility Allocation and the method-phase article,
    not stated directly.
  - unsupported:The statement that the result feeds arc42 section 1 as a brief functional description
    is not explicitly stated in the articles.
  - unsupported:The ClinicBook details (the extra story for health data entry, the table of reasons, the
    use case extensions) are illustrative inventions for the example.
---

## What you get from this step

You get a short list of use cases or user stories that matter most for the architecture. A [use case](concept:use-case) describes how a system responds to requests from outside actors. A [user story](concept:user-story) is a short requirement written from a stakeholder's point of view. It is a reminder to talk, not a full specification.

You do not need a complete requirements document. [Working with Functional Requirements (method phase)](concept:method-phase-working-with-functional-requirements) suggests a brief description of the functional requirements that points to existing documents. It also suggests detailed requirements only for the subset that architectural decisions need. This result feeds arc42 section 1.

## What you need first

- Any existing requirements material, such as a vision document, a backlog or a list of features. Refer to it instead of copying it.
- Names of the customer or user representatives you can talk to. [Requirements Difficulty and Customer Engagement](concept:requirements-difficulty-and-customer-engagement) asks you to name them and to say whether they speak for the wider customer side.
- A rough idea of the quality requirements, such as security or availability. They help you decide which functions matter most.

## If something is missing

- **No requirements document exists.** Gather requirements with more than one technique, such as interviews, observation, questionnaires or workshops. See [Requirements Trawling](concept:requirements-elicitation). Expect gaps. Some requirements only appear while you build.
- **Nobody is available to answer questions.** Decide who your customer representatives are. Also decide how often you get feedback, for example in reviews. See [Requirements Difficulty and Customer Engagement](concept:requirements-difficulty-and-customer-engagement).
- **The current process is wasteful.** Automation speeds up whatever process it gets. Look at the target-state process before you write requirements. See [Process Automation Magnifies Efficiency](concept:process-automation-magnifies-efficiency).
- **You only have vague wishes.** Turn them into short stories first, then split them as described below.

## How to do it

1. **Collect what exists.** List the existing requirements sources. Write a brief description of the functions the system must offer. Say which tasks and user objectives they cover. See [Functional suitability](concept:functional-suitability).
2. **Keep functions apart from quality requirements.** Put speed, security and similar needs in their own list. Constraints go there too. See [Working with Functional Requirements (method phase)](concept:method-phase-working-with-functional-requirements).
3. **Write each function as a story or a use case.**
   - A story names a specific user role, a goal and a reason. See [User Story Role Formulation](concept:user-story-role-formulation).
   - A use case is named after the main actor's goal, with an active verb. Mark its goal level. The user-goal level is the most useful one. See [Use Case Goal Level](concept:use-case-goal-levels).
   - A story and a use case for the same goal must not contradict each other. See [Consistency of User Story and Use Case](concept:consistency-of-user-story-and-use-case).
4. **Show the scope in a picture, if it helps.** A [use case diagram](concept:use-case-diagram) draws a system boundary. Actors stay outside it. An actor can be a person, an organization or an external system. Avoid the mistakes in [Common Use Case Diagram Errors](concept:use-case-diagram-modeling-mistakes).
5. **Split items that are too big or too vague.**
   - A story too large for one iteration is an [epic](concept:epic). Split it before you build it.
   - Look hard at any story with the word "manage". Split it by operation. See [Story Splitting](concept:story-splitting).
   - Make the first story a simple end-to-end case. A [story map](concept:story-mapping) calls this a walking skeleton.
6. **Pick the ones that matter for the architecture.** Choose the items that need detailed requirements for architectural decisions. Start with items that touch your main quality needs or outside systems. Quality requirements steer how responsibilities are allocated, so these items shape the design most. See [Responsibility Allocation](concept:responsibility-allocation). Write the chosen items in more detail, for example with the [use case template](concept:use-case-template).
7. **Add a check for each chosen item.** Give each story acceptance criteria or examples. Write them in the user's language, so a tester knows how to check them. Keep the user's goal visible next to them. See [Acceptance Criterion](concept:acceptance-criteria) and [Frequent Mistakes in Defining Acceptance Criteria](concept:frequent-mistakes-in-defining-acceptance-criteria).
8. **Check the set.** Compare your use cases with the quality requirements and the domain concepts, not only with what stakeholders said. List extensions for each use case. Remove wishful thinking that the project does not need. See [Use Case Completeness Check](concept:use-case-completeness-check).

## Example: ClinicBook

ClinicBook is an online appointment booking system for 40 small medical practices. Patients use the web and a mobile app. Practice staff manage calendars. The system must integrate with practice-management software from different vendors. It must send reminders by SMS and e-mail and protect health data.

**Step 3 (write stories).** The team writes first stories:

- As a patient, I want to book an appointment online, so that I do not have to call the practice.
- As a patient, I want to move or cancel an appointment, so that I can react when my plans change.
- As a patient, I want a reminder by SMS or e-mail, so that I do not miss my appointment.
- As practice staff, I want to manage the calendar, so that the schedule stays correct.

**Step 5 (split).** "Manage the calendar" is an epic. The team splits it by operation: block a time slot, open a time slot and view the day's appointments. It then checks the pieces against [INVEST Criteria](concept:invest-criteria).

**Step 3 (use case).** For the most important story, the team writes a use case. Its name is "Book an appointment". The goal level is user goal. The primary actor is the patient. The practice-management software and the SMS service are supporting actors. The main success scenario is a numbered list. Extensions cover cases such as "the chosen slot was taken meanwhile" and "the practice-management software does not answer".

**Step 6 (pick).** The team picks three items for detailed work. This table shows why:

| Item | Why it matters for the architecture |
|---|---|
| Book an appointment | Morning peaks put load on it. It must talk to several vendors' software. It handles health data. |
| Send a reminder | It uses two outside channels, SMS and e-mail. |
| Move or cancel an appointment | It must stay consistent with the calendar in the practice's own software. |

Calendar management for staff stays a short description for now. The team will detail it later.

**Step 5 (walking skeleton).** The first slice is one patient booking one appointment in one practice. It uses one vendor's software. Other vendors and the mobile app follow later.

**Step 7 (confirm).** One criterion for "Book an appointment": "Given a free slot, when the patient confirms the booking, then the appointment appears in the practice's calendar." It has a single trigger, so a tester can check it.

**Step 8 (check).** The team compares the list with the known forces: privacy, availability, legacy integration. It asks whether each force has a use case that shows it. It finds no use case for the patient's health data entry, so it adds a story.

## Done when

- Each important function is written as a story or a use case, and each one has a role or actor and a goal. ([User Story](concept:user-story), [Use Case](concept:use-case))
- Each use case has a goal level, and each story matches its use case. ([Use Case Goal Level](concept:use-case-goal-levels), [Consistency of User Story and Use Case](concept:consistency-of-user-story-and-use-case))
- Stories that were too big are split, and "manage" stories are split by operation. ([Story Splitting](concept:story-splitting))
- The items needed for architectural decisions are chosen and described in detail. Functional requirements are kept apart from quality requirements. ([Working with Functional Requirements (method phase)](concept:method-phase-working-with-functional-requirements))
- Each chosen story has acceptance criteria that a tester can check. ([Acceptance Criterion](concept:acceptance-criteria))
- The set was checked against quality requirements and domain concepts, and it holds no wishful thinking. ([Use Case Completeness Check](concept:use-case-completeness-check))

## Learn more

- [Use Case Template](concept:use-case-template)
- [Use Case as Goal-Responsibility Contract between Actors](concept:functional-dependency-between-actors)
- [Use Case Diagram](concept:use-case-diagram)
- [Common Use Case Diagram Errors](concept:use-case-diagram-modeling-mistakes)
- [Use Case Goal Hierarchy with Include Relationships](concept:use-case-goal-hierarchy-with-include-relationships)
- [Goal Hierarchy to Component Mapping](concept:goal-hierarchy-to-component-mapping)
- [User Stories vs. Use Cases](concept:user-story-vs-use-case)
- [Card, Conversation, Confirmation](concept:card-conversation-confirmation)
- [INVEST Applied to Architectural Work](concept:invest-applied-to-architectural-work)
- [SMART Requirements](concept:smart-requirements)
- [Story Mapping](concept:story-mapping)
- [Epic](concept:epic)
- [Agile Enterprise Backlog Model](concept:agile-enterprise-backlog-model)
- [Requirement Types and Documents (Wiegers/Beatty)](concept:requirement-types-and-documents)
- [Requirements Trawling](concept:requirements-elicitation)
- [Requirements Difficulty and Customer Engagement](concept:requirements-difficulty-and-customer-engagement)
- [Capturing Business Behavior via Process Modeling](concept:capturing-business-behavior-via-process-modeling)
- [Process Analysis](concept:process-analysis)
- [Process Analysis and Modeling](concept:purpose-of-process-analysis-and-modeling)
- [Process Automation Magnifies Efficiency](concept:process-automation-magnifies-efficiency)
- [Functional suitability](concept:functional-suitability)
- [Responsibility Allocation](concept:responsibility-allocation)
- [INVEST Criteria](concept:invest-criteria)
- [User Story Role Formulation](concept:user-story-role-formulation)
- [Frequent Mistakes in Defining Acceptance Criteria](concept:frequent-mistakes-in-defining-acceptance-criteria)
- [Use Case Goal Level](concept:use-case-goal-levels)
- [Use Case Completeness Check](concept:use-case-completeness-check)
