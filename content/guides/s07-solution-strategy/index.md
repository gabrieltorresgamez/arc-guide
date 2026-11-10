---
title: 'Step 7: Choose a solution strategy'
id: s07-solution-strategy
review:
  status: generated
  flags:
  - unsupported:Details on how a decision is applied across the system can go into arc42 chapter 8 (the
    articles do not describe chapter 8).
  - unsupported:ClinicBook's concrete decisions (layered single system, tactic choices, assumed scenario
    numbers, adapter principle) are illustrative choices, not drawn from the articles.
  - unsupported:Reasoning that a small team argues against microservices is the guide's own inference
    from the stated costs of the style.
  - unsupported:The statement that one deployable unit means a single fault can affect everything is the
    guide's own inference.
---

## What you get from this step

You get a short list of the fundamental decisions that shape your system. This list is the arc42 chapter 4, the [Solution Strategy](concept:arc42-solution-strategy). It holds:

- a few guiding principles,
- the top-level structure (the architecture style or pattern),
- a solution approach for each top quality goal,
- the organizational decisions that matter, such as the development process or work given to third parties.

Each decision points back to the problem, the quality goals or a constraint. The chapter stays compact, for example as a keyword list. It refers onward to other chapters instead of giving details. Details on how a decision is applied across the system can go into arc42 chapter 8.

A [System Idea](concept:system-idea) is the early, high-level answer to "how will we build this?". The solution strategy is its closest arc42 counterpart.

## What you need first

- The problem statement and the key constraints (arc42 chapters 1 and 2). You will link your decisions to them.
- The top quality goals, ranked by how much stakeholders care about each. See [Quality Attribute Trade-off](concept:architectural-trade-off-thinking).
- For each top goal, a quality scenario with a measurable criterion. See [Working with Tactics and Quality Attributes](concept:working-with-tactics-and-quality-attributes).

[Architectural Thinking](concept:architectural-thinking) describes the cycle you are in: start from requirements, quality goals and constraints, then design, check and refine.

## If something is missing

- **Quality goals are not ranked.** Rank them with the stakeholders first. A utility tree is one way to do it. Without a ranking you cannot settle conflicts. See [Tactic Trade-off Balancing](concept:tactic-trade-off-balancing).
- **A goal has no measurable scenario.** Write one now. A vague goal such as "must be fast" gives you no way to choose between tactics.
- **A constraint is unclear.** Ask the people who set it. Decisions that rest on a guessed constraint are weak.
- **You find a technical limit or a goal conflict while designing.** Record it and feed it back to the requirements. Requirements and architecture grow together. See [Twin Peaks Model](concept:twin-peaks-model).
- **You cannot decide yet.** Mark the decision as open and note when you expect to have the facts. See [Solution as Moving Target](concept:solution-as-moving-target).

## How to do it

1. **Collect the drivers.** List the functional requirements, quality requirements and constraints the design starts from. See [Architectural Thinking](concept:architectural-thinking).
2. **Rank the goals and find the conflicts.** Improving one quality usually costs another. For each major decision, name the quality it improves and the quality it may harm. See [Quality Attribute Trade-off](concept:architectural-trade-off-thinking).
3. **Write a few principles.** A principle is a short rule that narrows your options without dictating one answer. Give each a name, a statement, a rationale and implications. See [Architecture Principle](concept:architecture-principle), [Architecture Principle Structure](concept:structure-of-an-architecture-principle) and [Working with Principles](concept:working-with-principles). Principles can pull in different directions. Justify a decision by a business requirement, not by a principle alone. See [Conflicting Architecture Principles](concept:conflicting-architecture-principles).
4. **Choose the top-level structure.** An [Architecture Style](concept:architectural-style) is a set of design constraints on elements and their relations. An [Architectural Pattern](concept:architectural-pattern) is a proven solution to a recurring problem. Both shape the whole system, so changing them late is costly. See [Architectural Pattern vs. Design Pattern](concept:architectural-pattern-vs-design-pattern). Name the style, the constraints it imposes and the costs you accept. Pick it because it fits your goals and context, not because it is popular. Keep the structure as simple as the problem allows. See [Complexity Reduction](concept:complexity-reduction). For examples of styles, see [Layered Architecture](concept:layered-architecture), [Microservices Architecture](concept:microservices-architecture) and [Service-Oriented Architecture](concept:service-oriented-architecture).
5. **Choose tactics for each top goal.** An [Architectural Tactic](concept:architectural-tactic) is a single design decision that affects one quality attribute. Patterns are built from tactics. See [Relationship between Tactics and Architectural Styles/Patterns](concept:tactics-vs-architectural-styles-and-patterns). Tie each tactic to the one goal it serves. Note its side effects on other qualities. See [Choosing and Applying Tactics](concept:choosing-and-applying-tactics). Tactics also help you adapt a catalog pattern to your context. See [Reasons for Architectural Tactics](concept:reasons-for-architectural-tactics). Useful starting points by goal:
   - availability: [Availability Tactic](concept:availability-tactic) (detect, recover, prevent faults),
   - security: [Security Tactic](concept:security-tactics),
   - changeability: [Modifiability Tactic](concept:modifiability-tactics),
   - speed: [Performance Tactic](concept:performance-tactics).
6. **Add organizational decisions.** Record decisions about the development process and about work given to third parties. See [Solution Strategy](concept:arc42-solution-strategy).
7. **Tie goals to decisions in one table.** Use one row per key goal. Show the scenario, the chosen approaches and the side effects. Record important decisions with their rationale and all consequences, including the negative ones. See [Tactic Trade-off Balancing](concept:tactic-trade-off-balancing). A lightweight decision record per tactic works well. Consider at least two options for each decision. See [Working with Tactics and Quality Attributes](concept:working-with-tactics-and-quality-attributes). You do not need to reference every requirement. Name the requirements behind the important decisions. See [Traceability](concept:traceability).
8. **Mark what is open and what is hard to change.** Take more care with hard-to-change decisions. Defer the others until the facts exist. See [Solution as Moving Target](concept:solution-as-moving-target) and [Continuous Architecture Principles](concept:continuous-architecture-principles).
9. **Name the architecture.** Do not leave it implied by the code. Decisions that nobody chose lead to [Accidental Architecture](concept:unsystematic-accidental-architecture).

## Example: ClinicBook

ClinicBook is an online booking system for 40 small medical practices. The inputs from steps 1 and 2 are these:

- Constraints: a small team and a fixed launch date.
- Top quality goals, in ranked order:
  1. Privacy and security of health data.
  2. Availability during morning peaks.
  3. Integration with practice-management software from different vendors, which can change.

**Principle.** Principles in this example are fictional.

| Part | Content |
|---|---|
| Name | Wrap every external system |
| Statement | ClinicBook reaches each external system only through one interface that we own. |
| Rationale | Practices use software from different vendors, and vendors will change. |
| Implications | We write and maintain one adapter per vendor. Direct calls to a vendor are not allowed in business code. |

This follows [Design for Change](concept:design-for-change), which asks for external systems to sit behind a single wrapping interface.

**Top-level structure.** The team chooses one system split into layers (UI/API, business logic, data access). Domain logic stays free of UI and persistence code. See [Layered Architecture](concept:layered-architecture) and [Layers and Components Decomposition](concept:layers-and-components-decomposition). The team does not choose microservices. That style adds network, data and operations costs, and the team is small ([Microservices Architecture](concept:microservices-architecture)). The strategy records this reason and the cost of the choice. For example, one deployable unit means a single fault can affect everything. The team accepts this and covers it with the availability tactics below.

**Quality goals and approaches.** The scenarios use assumed numbers.

| Goal | Scenario (assumed) | Approach | Side effect to record |
|---|---|---|---|
| Security and privacy | Health data is unreadable to anyone without the key, in storage and on the network. | [Encrypt Data](concept:encrypt-data) at rest and in transit. Keys sit in a key management service, not in code. | Key management is extra work for a small team. |
| Availability | Patients can book between 7:00 and 9:00 even when one server fails. | [Load Balancer](concept:load-balancer) over several servers. [Ping/Echo](concept:ping-echo) health checks detect failures. | More servers cost more money. |
| Availability | A slow SMS provider does not block bookings. | Timeouts and a [Circuit Breaker](concept:circuit-breaker) on calls to the provider. [Retry](concept:retry) only for temporary faults and safe-to-repeat operations. | Callers need a defined behavior when the breaker rejects a call. |
| Availability | If the practice software is down, booking continues. | [Graceful Degradation](concept:graceful-degradation). Booking is core. Reminders can pause. The business must agree on this ranking. | Fallback paths need testing. |
| Integration | A new vendor connects in at most 3 person-weeks. | One adapter per vendor behind one interface. See [Reduce Coupling](concept:reduce-coupling). | The extra interface must be maintained. |

**Organizational decisions.** The team builds in small increments and releases an early version, which fits the fixed date. See [Incrementality](concept:incrementality). SMS and e-mail delivery go to third-party providers. That decision is recorded in the strategy.

**Open decision.** Whether to add a message queue for reminders waits until load measurements exist. Choosing a layered structure is hard to change, so the team spends more care there. A provider behind an adapter is easy to replace.

**Feedback to requirements.** The team sees that full availability for every feature conflicts with the launch date. It records this as feedback and asks stakeholders to confirm that booking is the core function.

## Done when

- The strategy lists principles, the top-level structure, the approach for each top quality goal and the organizational decisions. It stays short and refers onward. ([Solution Strategy](concept:arc42-solution-strategy))
- The chosen style or pattern is named. Its constraints, benefits and costs are stated. ([Architecture Style](concept:architectural-style))
- Each top quality goal has a measurable scenario and a table row that lists approaches and side effects. ([Tactic Trade-off Balancing](concept:tactic-trade-off-balancing))
- Each tactic names the one quality attribute it serves. ([Choosing and Applying Tactics](concept:choosing-and-applying-tactics))
- Each principle has a name, statement, rationale and implications. ([Architecture Principle Structure](concept:structure-of-an-architecture-principle))
- Important decisions name their reasons and their negative consequences. Open decisions are marked. ([Solution as Moving Target](concept:solution-as-moving-target))

## Learn more

- [Solution Strategy](concept:arc42-solution-strategy)
- [System Idea](concept:system-idea)
- [Architecture Means](concept:architecture-means)
- [Influence of Architectural Means](concept:influence-of-architectural-means)
- [Architectural Tactic](concept:architectural-tactic)
- [Working with Tactics and Quality Attributes](concept:working-with-tactics-and-quality-attributes)
- [Availability Tactic Categories](concept:availability-responses)
- [Architectural Decisions for Availability](concept:architectural-decisions-for-availability)
- [Architecture Principle](concept:architecture-principle)
- [Working with Principles](concept:working-with-principles)
- [Conflicting Architecture Principles](concept:conflicting-architecture-principles)
- [Loose Coupling](concept:loose-coupling)
- [Architectural Pattern](concept:architectural-pattern)
- [Quality Attribute Trade-off](concept:architectural-trade-off-thinking)
- [Twin Peaks Model](concept:twin-peaks-model)
- [Accidental Architecture](concept:unsystematic-accidental-architecture)
