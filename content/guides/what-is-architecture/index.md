---
title: What is software architecture?
id: what-is-architecture
review:
  status: generated
  flags: []
---

## What software architecture is

Software architecture is the set of fundamental choices about a system. It covers the system's parts, how those parts relate, and the reasoning behind the choices. Definitions differ. Most stress three things: structure, important decisions, and the cost of changing those decisions later. See [Software Architecture](concept:software-architecture) and Software Architecture Definition.

**Building blocks in levels** help from the start. You describe the system as a few large parts. You then zoom into a part only where it matters. Read more in Software Architecture Basic Concepts ([Software Architecture](concept:software-architecture)) and [Architecture Level](concept:architecture-level).

Every system has an architecture, even if nobody planned or documented it. That is called [implicit architecture](concept:implicit-architecture).

## Why it matters

An architecture that nobody chose on purpose still exists, but it is not visible or well communicated to the team. Small, unplanned changes pile up and erode it. In the end it can become a [Big Ball of Mud](concept:big-ball-of-mud), a system held together by patches.

This slow drift away from the intended design is called architecture decay ([Big Ball of Mud](concept:big-ball-of-mud)). Two habits counter it:

- [Refactoring](concept:refactoring) changes the inside of the software in small steps without changing what it does.
- Checks that compare the code with the intended design. One option is an [architecturally evident coding style](concept:architecturally-evident-coding-style), where automated tests verify the architecture rules.

Architecture is also where goals meet limits. A *quality goal* is a property the system must have, such as availability. A *constraint* is a limit on your choices, such as a fixed date. A *stakeholder* is a person or group with an interest in the system. Requirements and Means Influence Architecture ([Architecture Means](concept:architecture-means)) explains why you should learn the key stakeholders' quality goals early. You should also know which decisions are free and which are bound. See also Software Architecture in Its Context ([Software Architecture](concept:software-architecture)).

## What an architect does

A [software architect](concept:software-architect) links business goals and technical work. The architect decides what matters, weighs trade-offs, talks with people at every level of the organization, and stays close to building the system. The role needs technical skill, communication skill and hands-on involvement in delivery ([Software Architect](concept:software-architect)).

The work follows a repeated cycle. [Architectural thinking](concept:architectural-thinking) means designing, checking, and refining. It starts from requirements, quality goals, and constraints. It ends in a documented architecture whose risks and trade-offs are understood.

The architect does not design everything upfront. [Agile architecture](concept:agile-architecture) means doing just enough architecture, guided by the biggest risks, and revisiting it as the product changes.

## Example: ClinicBook

ClinicBook is an online appointment booking system for 40 small medical practices. Patients book, move, and cancel appointments on the web and in a mobile app. Staff manage calendars. Here is how the ideas above apply.

**Forces first.** The main forces are privacy and security, availability during morning peaks, integration with legacy systems, a small team, and a fixed launch date. The architect names the most important quality goals and learns which decisions are free and which are bound.

**Draw the boundary.** A context view shows ClinicBook as a black box. Around it sit its communication partners and the data exchanged. Partners include patients, practice staff, the practices' management software from different vendors, and the SMS and e-mail channels.

**Let risks guide the effort.** With a small team and a fixed date, a complete upfront design is not realistic. Skipping design is no better. Following [Agile Architecture](concept:agile-architecture), the architect ties design effort to the biggest risks. For ClinicBook, those risks are health data protection, the morning peaks, and the vendor integrations.

**Watch known traps.** Integration means ClinicBook calls other systems. Connectors and Distribution ([Software Connector](concept:software-connector)) warns that a call to another process may be slow or fail while the rest keeps running. The design should say what happens then. Common Architect Mistakes ([Software Architect](concept:software-architect)) warns against home-built security when established solutions exist.

**Write down the why.** The architect records key decisions and their reasons, so the structure traces back to deliberate choices. Without such records, ClinicBook would drift toward the accidental architecture described above.

## Where to go next

Start with [Software Architecture](concept:software-architecture). Then read [Architectural Thinking](concept:architectural-thinking) to see how the design cycle works.
