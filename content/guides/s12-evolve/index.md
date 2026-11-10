---
title: 'Step 12: Keep the architecture alive'
id: s12-evolve
review:
  status: generated
  flags:
  - unsupported:Step 6 (update the description in the same pull request as the code change) is a suggested
    habit. The sources only say a process or tool is needed and that documentation changes go through
    pull requests.
  - unsupported:The suggestion to compare the building block view with the code every few weeks is an
    example cadence. The sources only say divergence should be detected, for example by conformance checking.
  - unsupported:The ClinicBook details (adapter ADR, patient-record test, file-export shortcut, reminder
    component, shared-calendar question) are invented for the fictional example.
---

## What you get from this step

A routine that keeps three things in line while the system changes: your decisions, your documentation and your code structure. Without such a routine, the structure drifts from the design. The [Architecture Decay](concept:architecture-decay) article calls this slow drift *decay*. Small, unplanned changes pile up and erode the structure.

You end the step with:

- a named owner for the documentation,
- documentation that changes together with the code,
- decisions that carry a review trigger and a status,
- automated checks that catch code that breaks your structure rules,
- a short list of known gaps and shortcuts, with a plan for each.

## What you need first

- A written description of the intended architecture. At minimum, this is a building block view, which shows the static parts of the system. See [Component View](concept:component-view).
- A short log of the important decisions, kept as [Architectural Decision Records](concept:architectural-decision-record) (ADRs). An ADR is a short document with one decision and its reasons.
- The source code in version control, with the documentation stored next to it.
- Some automated tests. [Refactoring](concept:refactoring) needs them as a safety net.

## If something is missing

- **No written intended architecture.** Every system has an architecture, even an unplanned one (see [Implicit Architecture](concept:architecture-facts-and-challenges)). Without a written intent, you cannot compare it with the code. Write a small first version. Name the main building blocks and their relations.
- **No decision records.** An unrecorded structure is an [Accidental Architecture](concept:unsystematic-accidental-architecture). It tends to erode through quick fixes. Record only the [architecturally significant decisions](concept:architecturally-significant-decision). These are the ones that are hard or costly to change, or that carry high risk.
- **No tests.** Do not refactor large areas yet. Add tests around the area you are about to change first.
- **Documentation in a wiki or in slide files.** Move it step by step into plain text under version control. See [Documentation as Code](concept:documentation-as-code).

## How to do it

1. **Name an owner.** Pick one person who is responsible for the amount and quality of the documentation. See [Guidelines for Documentation](concept:guidelines-for-documentation). Keep the documentation short and focused on important or risky topics. Short text is easier to keep current.
2. **Treat documentation like code.** Store it as plain text in Git. Propose changes through pull requests and review them. Let a toolchain build the published output. Generate diagrams from text where you can ([Diagrams as Code](concept:diagrams-as-code)). Let the code carry what it can, such as API documentation generated from source. Write the reasons by hand, because code does not show them. See [Self-Documentation](concept:self-documentation).
3. **Give each decision a review trigger and a status.** In each ADR, state when you will review it, or which change in context forces a new look ([Architectural Decision-Making Process](concept:architectural-decision-making-in-project-development)). When you replace a decision, mark the old ADR as superseded and point to the new one ([Decision Dependencies](concept:decision-dependencies)). Say how you will confirm that the code follows the decision. The [MADR](concept:markdown-architectural-decision-records-madr) template has a place for this.
4. **Turn structure rules into automated checks.** Express layers and allowed dependencies in package layout and naming. Then run tests in the build that check them. ArchUnit is one such tool for Java. If the code base is old and already breaks the rules, freeze the existing violations so that no new ones appear. See [Architecturally Evident Coding Style](concept:architecturally-evident-coding-style).
5. **Compare intended and implemented architecture on a schedule.** Use the conformance checks from step 4. Add a short review of the building block view against the code. Record every gap you accept as a risk or as technical debt ([Implicit Architecture](concept:architecture-facts-and-challenges), [Architecture Decay](concept:architecture-decay)).
6. **Update the description with the change.** When a change alters a building block, an interface or a decision, update the text in the same pull request as the code. The sources say you need a process or tool that keeps the description in step with the code. This habit is one way to do that. Review it as you review code.
7. **Refactor in small steps.** Refactoring changes the inside of the code without changing what it does. Do it continuously, with tests as the safety net ([Refactoring](concept:refactoring)). Keep a working version at all times, and integrate often ([Keep It Working](concept:keep-it-working)).
8. **Track and repay debt.** [Technical debt](concept:technical-debt) is a shortcut that helps now and makes later change more costly. List known debts by priority. Mark deliberate ones as knowingly accepted, and plan how to repay each. If you add temporary parts during a move to a new design, name them and plan their removal ([AS-IS and TO-BE View](concept:as-is-and-to-be-view)).
9. **Expect the solution to move.** Say which decisions you deliberately deferred. For each open decision, note when its [last responsible moment](concept:last-responsible-moment) arrives. Keep the [glossary](concept:arc42-glossary) current as your understanding of the domain changes. See [Solution as Moving Target](concept:solution-as-moving-target).

## Example: ClinicBook

ClinicBook has a small team and a fixed launch date. The team cannot afford heavy documentation. It chooses a light routine.

- **Owner.** The tech lead owns the documentation. The architecture text and ADRs live in the same Git repository as the code. Pull requests cover both.
- **Decision with a trigger.** One ADR reads: "Connect to practice-management software through one adapter per vendor." It lists the options, the reasons and the negative consequences. Its review trigger is "a new vendor joins, or a vendor changes its interface." Later, the team may replace the adapter approach. Then it marks this ADR as superseded and links the new one.
- **Structure rule as a test.** Health data needs protection. The team writes the rule "only the booking core may read patient records." It adds an automated test in the build that fails when the web or mobile backend code reaches the patient records directly. The ADR for the adapters says that this test confirms compliance.
- **Legacy shortcut.** Before launch, one vendor's software only offers file exports. The team writes a quick import that skips the adapter structure. Before shipping it, the team records it in the technical debt list. The entry says it is knowingly accepted, names the planned fix (a proper adapter after launch) and states the risk to the health-data rule. The existing violation is frozen, so the test allows no further ones.
- **Regular check.** Every few weeks, the team compares the building block view with the code. It finds that the reminder component now also reads appointment data directly. The team records this as debt and plans a refactoring. It updates the building block view in the same pull request that fixes the code.
- **Open decision.** The team has not yet decided how to handle several practices with one shared calendar. It writes the question into the list of open decisions and notes when it must decide. That point comes before it onboards the first practice with this need.

## Done when

- One named person owns the documentation, and the documentation stays short ([Guidelines for Documentation](concept:guidelines-for-documentation)).
- Documentation sources are plain text in version control, reviewed through pull requests and built by a toolchain ([Documentation as Code](concept:documentation-as-code)).
- Each important ADR states a review trigger, and replaced decisions are marked superseded and point to their replacement ([Decision Dependencies](concept:decision-dependencies)).
- Structure rules run as automated tests in the build, and existing violations in old code are frozen ([Architecturally Evident Coding Style](concept:architecturally-evident-coding-style)).
- Gaps between intended and implemented architecture are recorded as risks or debt, with a plan to repay each ([Technical Debt](concept:technical-debt)).
- Refactoring happens continuously in small steps, and a working version always exists ([Keep It Working](concept:keep-it-working)).

## Learn more

- [Architecture Decay](concept:architecture-decay)
- [Implicit Architecture](concept:architecture-facts-and-challenges)
- [Accidental Architecture](concept:unsystematic-accidental-architecture)
- [Big Ball of Mud](concept:big-ball-of-mud)
- [Architecturally Evident Coding Style](concept:architecturally-evident-coding-style)
- [Documentation as Code](concept:documentation-as-code)
- [Diagrams as Code](concept:diagrams-as-code)
- [Self-Documentation](concept:self-documentation)
- [Guidelines for Documentation](concept:guidelines-for-documentation)
- [Motivation for Architecture Documentation](concept:motivation-for-architecture-documentation)
- [Architectural Decision-Making Process](concept:architectural-decision-making-in-project-development)
- [Architectural Decision Management Cycle](concept:architectural-decision-management-cycle)
- [Definition of Done for Architectural Decisions](concept:definition-of-done-for-architectural-decisions)
- [Markdown Architectural Decision Records](concept:markdown-architectural-decision-records-madr)
- [Last Responsible Moment](concept:last-responsible-moment)
- [Solution as Moving Target](concept:solution-as-moving-target)
- [Technical Debt](concept:technical-debt)
- [Code Smell](concept:code-smell)
- [Refactoring](concept:refactoring)
- [Keep It Working](concept:keep-it-working)
- [Sweeping It Under the Rug](concept:sweeping-it-under-the-rug)
- [Iterative and Incremental Development](concept:iterative-and-incremental-development)
- [AS-IS and TO-BE View](concept:as-is-and-to-be-view)
- [arc42 Glossary](concept:arc42-glossary)
