---
title: Process Automation Magnifies Efficiency
slug: process-automation-magnifies-efficiency
category: principles
kind: principle
summary: Automation speeds up whatever process it is given, good or bad. Fix or remove wasteful steps
  first, then automate. Otherwise software only makes the waste run faster.
arc42:
- 1
- 4
- 11
step: s03-functional-requirements
related:
- as-is-and-to-be-view
- process-analysis
- purpose-of-process-analysis-and-modeling
- capturing-business-behavior-via-process-modeling
- arc42-solution-strategy
- business-architecture
- bpm-life-cycle
- technical-debt
checks:
- The documented requirements come from the target-state process, not only from the current-state process.
- Superfluous steps were removed and roles clarified before automation was planned.
- An as-is process model exists and was reviewed for improvement opportunities.
- The team can show that it fully understands each process it plans to automate.
sources:
- url: https://edana.ch/en/2026/02/09/why-digitalizing-a-bad-process-worsens-the-problem-and-how-to-avoid-it/
  title: 'Digitalizing a Bad Process: How to Prevent Amplified Dysfunction'
  site: edana.ch
  accessed: '2026-11-09'
- url: https://egroup-us.com/news/automating-broken-processes/
  title: Automating Broken Processes Scales Problems
  site: egroup-us.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_process_re-engineering
  title: Business process re-engineering - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://tech.lean.org/journal/the-reengineering-is-coming
  title: The Reengineering Is Coming
  site: tech.lean.org
  accessed: '2026-11-09'
- url: https://www.bpminstitute.org/resources/articles/deliver-business-value-avoid-paving-over-cow-paths/
  title: To Deliver Business Value, Avoid Paving over Cow Paths | BPMInstitute.org
  site: bpminstitute.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Improve the process first, then automate it.
review:
  status: generated
  flags: []
---

## Explanation

Automation can multiply the weaknesses hidden in a process. Speed helps only when the team understands what it is speeding up. If the process has waste, the same waste runs at higher speed.

Digitizing a flawed process does not fix it. It exposes and amplifies the flaws. A process should not be moved into a tool as it is.

**The cow-path pitfall**

Automating a broken process gets you to the wrong place faster. This is the "paving the cow paths" metaphor. Earlier technology waves, such as the personal computer and enterprise resource planning (ERP) systems, did this. Companies put old paper forms on screens and digitized their filing cabinets without rethinking the work. The technology made the existing mess run faster.

**Remove waste first**

Business process reengineering made the same point. Its argument was that managers should remove work that adds no value instead of digitizing it. One well-known title put it as "Don't Automate, Obliterate."

Practical steps before automating:

- Eliminate superfluous steps.
- Clarify roles.

A streamlined process is also easier to digitalize.

**Link to requirements**

Requirements derived from current-state processes can lead to a solution that paves cow paths. The better focus is the target-state process.

**Evidence from robotic process automation (RPA)**

According to a vendor blog citing EY, 30 to 50% of early RPA projects fail. The most common reason given is that teams automate processes they do not fully understand or that were broken to begin with.

## Example

A team is asked to build an app for approving purchase orders. The current process has five approval steps, and two of them only forward the request. Before coding, the team draws the as-is process and removes the two forwarding steps. It also names one owner per step. Then it builds the app for the shorter process. Without that review, the app would have carried the extra steps into software.

## Trade-offs

Analyzing and redesigning a process before automating takes time and delays the start of software work. In return, the team avoids building waste into a system. Redesign also needs people who understand the process.
