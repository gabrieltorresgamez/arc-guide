---
title: Application Lifecycle Diagram
slug: application-lifecycle-diagram
category: enterprise-architecture
kind: artifact
summary: An application lifecycle diagram is a Gantt chart that shows when each application is planned
  to start and stop supporting the business. It helps teams spot retirement and replacement needs early.
arc42:
- 11
- 4
step: s12-evolve
related:
- enterprise-architecture-management
- patterns-for-the-evolution-of-application-landscapes
- technical-debt
- togaf
- entity-life-cycle
- application-architecture
checks:
- Each application appears as one bar on a shared timeline with a labeled planned end date.
- Lifecycle phases such as Plan, Pilot, Production, Sunset and Retired are shown where a lifecycle is
  defined.
- Applications nearing end of life without a planned successor are identified.
- 'Each application is assigned a TIME category: tolerate, invest, migrate or eliminate.'
sources:
- url: https://documentation.alfabet.com/11-8/en/PortAdmin_ROAD_AppRoad_Over.html
  title: What is our application roadmap?
  site: documentation.alfabet.com
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/blog/gartner-time-tolerate
  title: 'Gartner® TIME Framework For App Rationalization: Tolerate'
  site: leanix.net
  accessed: '2026-11-09'
- url: https://grahamberrisford.com/01EAingeneral/EAandApps/Application%20life%20cycles%20-%20key%20points.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Generic lifecycle diagram: one bar per application on a shared timeline.'
review:
  status: generated
  flags: []
---

## Explanation

Alfabet's business question "What is our application roadmap?" is answered with a Gantt chart. It draws the lifecycle of every application in the repository.

**What the bars show**

The chart shows when each application is planned to be implemented. It also shows when the application will stop supporting the business.

In Alfabet, a green bar covers the active period, from start date to end date. If a lifecycle is defined, a multi-colored bar sits above the green one. It shows the phases: Plan, Pilot, Production, Sunset and Retired.

**What decisions it supports**

The chart helps identify gaps in application support and take corrective action. Look for applications that are close to end of life but have no successor planned. Those are gaps to fix.

**Link to the TIME model**

The TIME model puts each application into one of four categories: tolerate, invest, migrate or eliminate. High technical fit and high functional fit means invest. Low on both means eliminate, which as a starting definition means removing the application because it is not needed or desirable.

**Who owns it**

Berrisford describes the application life cycle as an enterprise architecture team matter. The software development life cycle, by contrast, is a matter for the software development team. He also notes that road maps of different types cut across each other. 

## Example

A company tracks three applications: a billing system, a customer portal and an HR tool. The chart shows one bar for each on a shared yearly axis. The HR tool's bar ends in two years. No bar for a successor exists. The team sees the gap and starts planning a replacement.

## Trade-offs

A chart is only useful if each application has a start date, an end date and, ideally, a defined lifecycle. Without a defined lifecycle, the phase bar is missing and only the active period appears. The chart also shows a strategic flag, an object state and successor links, in addition to timing.
