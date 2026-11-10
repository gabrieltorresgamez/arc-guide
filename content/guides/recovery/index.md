---
title: Joining a project without architecture documentation
id: recovery
review:
  status: generated
  flags:
  - unsupported:The suggested order of the six steps (people and papers first, code and decisions later)
    is a recommendation, not stated in the linked articles.
  - unsupported:Asking the people who built the system as a way to find decision reasons is a practical
    suggestion not stated in the linked articles.
  - unsupported:ClinicBook's partner list (SMS service, e-mail service) and its example building blocks,
    adapters and reminder risk are illustrative assumptions for the example.
  - unsupported:Advice to share the finished sections with people who know the system and fix their corrections
    is a practical suggestion not stated in the linked articles.
---

## Ordered steps to recover missing information in an existing project

Code shows what a system does. It does not show why it was built that way ([Motivation for Architecture Documentation](concept:motivation-for-architecture-documentation)). A system without documentation still has an architecture, though nobody may have planned or understood it ([Implicit Architecture](concept:architecture-facts-and-challenges)). Your job is to write down what you can recover, in small pieces.

I suggest the order below. It starts with information you can get from people and existing papers. It ends with what takes the most digging. Early results will be rough. Refine them as you learn more ([Architect Settles In Method Phase](concept:architect-settles-in-method-phase)).

Write only what readers will use. Describe each thing once and reference it elsewhere ([Guidelines for Documentation](concept:guidelines-for-documentation)).

### Step 1: Find out who is involved and what matters most (arc42 section 1)

**Write down first:** a stakeholder table and the top quality goals.

- A stakeholder is a person, team or organization with an interest in the system ([Stakeholder Identification](concept:stakeholder-identification)). Ask who gains or loses, who decides and who controls resources.
- For each stakeholder, note a role and what they expect from the system.
- Pick the top three quality goals, five at most, and give each a short scenario ([Quality Attribute Prioritization](concept:quality-attribute-prioritization)). A quality goal is a quality such as speed or security that the system must meet.
- Keep the requirements overview short. Link to existing requirements documents instead of copying them ([arc42 Introduction and Goals](concept:arc42-introduction-and-goals)).

Section 1 holds only the top goals. Detailed quality requirements go to section 10.

### Step 2: List the constraints (arc42 section 2)

**Write down first:** one list of everything that limits your design freedom.

- A constraint is a requirement that limits how freely you can design and build ([Architectural Constraint](concept:requirements-versus-constraints)).
- Put all constraints in one place, with a short reason for each ([arc42 Constraints](concept:arc42-constraints)).
- Group them as technical, organizational or political, and conventions.
- Mark each one as negotiable or not. Note which ones come from the wider organization rather than this system.

Budget, deadlines and mandated technologies count as constraints too.

### Step 3: Draw the system as a black box (arc42 section 3)

**Write down first:** the neighbors of the system and the data exchanged with each.

- Show the system as one box. Put users and other systems around it ([arc42 Context and Scope](concept:arc42-context-and-scope)).
- Write the business context first. It shows which data flows to and from each partner. Then write the technical context. It shows which channel or protocol carries each flow ([Business and Technical Context](concept:business-and-technical-context)).
- Draw both directions where data moves both ways ([Context View Antipattern: Forgetting Bidirectional Data Flows](concept:context-view-antipattern-forgetting-bidirectional-data-flows)).
- Add a table with one row per partner. Label every arrow with the data, and add a legend.

### Step 4: Recover the building blocks from the code (arc42 section 5)

**Write down first:** the level 1 view. That is the whole system as a white box, with its main building blocks as black boxes.

- A black box shows what a block does and offers. A white box shows what is inside ([Component View](concept:component-view)).
- Do not trust old documents blindly. For a legacy system, recover the real architecture first ([ATAM Application Phases](concept:atam-application-phases)).
- Group blocks by responsibility. Do not copy code packages such as Facade, Service or Dto into the diagram ([Component View Antipattern: Lifting Code to Model Level](concept:component-view-antipattern-lifting-code-to-model-level)).
- Zoom into a block only if it is important, risky, complex or volatile ([Component View Refinement Levels](concept:component-view-refinement-levels)).
- Every diagram needs a title that names its type and scope, and a legend.

The code can answer "what is here" ([Self-Documentation](concept:self-documentation)). It cannot answer "why", so the next step covers that.

### Step 5: Record the decisions you can find (arc42 section 9)

**Write down first:** the few big decisions that are costly or risky to change, each with its reason.

- Look for decisions with far-reaching effects, such as how systems are integrated ([Architecturally Significant Decision](concept:architecturally-significant-decision)). Do not log every small choice.
- For each one, write the decision, the reason and the consequences, including the bad ones ([arc42 Architecture Decisions](concept:arc42-architecture-decisions)).
- Use one short record per decision ([Architectural Decision Record](concept:architectural-decision-record)).
- If nobody knows the reason, write it down as an assumption. Draft it as a decision record where you can ([Architecture Canvas](concept:architecture-canvas)).
- Ask the people who built the system. Read the code with the question "why?".

Section 4 holds the most fundamental decisions. Section 9 points there and does not repeat them.

### Step 6: Collect risks and technical debt (arc42 section 11)

**Write down first:** the gaps and weak spots you met in steps 1 to 5.

- Record known gaps between the intended and the implemented architecture as risks or technical debt ([Implicit Architecture](concept:architecture-facts-and-challenges)).
- Technical debt means shortcuts that help in the short term but make later change more costly ([Technical Debt](concept:technical-debt)). List each item and order the list by priority.
- To find more risks, run a short team session. Rate each risk by probability and impact, and plan a mitigation for the top ones ([Risk Storming](concept:risk-storming)).

## Example: ClinicBook

ClinicBook is an online booking system for 40 small medical practices. Patients book, move and cancel appointments on the web and in a mobile app. Practice staff manage calendars. You join the team, and nothing is documented.

| Step | What you write down first | arc42 section |
|---|---|---|
| 1 | Stakeholders: patients, practice staff, the small team, the owners. Top goals: privacy and security of health data, availability during morning peaks, integration with legacy systems. | 1 |
| 2 | The fixed launch date as an organizational constraint. The practices' existing software, from different vendors, as a technical constraint. Health-data protection as a constraint you must check. | 2 |
| 3 | A black box with patients, practice staff, the practice-management software, an SMS service and an e-mail service. Data flows: appointment requests, calendar data, reminder messages. The technical context lists the channel for each flow. | 3 |
| 4 | A level 1 view with blocks named by responsibility, such as booking, calendar management, reminders and practice integration. | 5 |
| 5 | Suppose you find a separate adapter for each vendor. Ask the team why. Write the answer, or mark it as an assumption. | 9 |
| 6 | Suppose reminders run in the same process as booking. Note that this could hurt availability in the morning peak. Rate the risk and add it to the list. | 11 |

In step 1, you check each top goal against a scenario. For availability, a scenario could read: "During the morning peak, patients can still book." Keep the scenario short, and add a measurable limit once you know one.

In step 3, you check that data flows run both ways where they do. Appointment data probably goes to the practice software and comes back as changes.

## After the first pass

- Share the sections with the people who know the system. Fix what they correct.
- Keep the documentation small enough to maintain. Name one person who owns its quality ([Guidelines for Documentation](concept:guidelines-for-documentation)).
- Update the sections when the system changes. Outdated documentation loses trust ([Motivation for Architecture Documentation](concept:motivation-for-architecture-documentation)).
