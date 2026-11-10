---
title: BPM Life Cycle
slug: bpm-life-cycle
category: modeling-bpmn
kind: method
summary: 'The BPM life cycle is a loop of stages for a business process: discovery, analysis, design,
  implementation and monitoring. A live process is measured and improved so it stays useful as goals,
  technology and rules change.'
arc42:
- 8
- 12
step: null
related:
- as-is-and-to-be-view
- process-analysis
- degrees-of-bpm-maturity
- waves-of-business-process-management
- purpose-of-process-analysis-and-modeling
- process-mining
- bpmn-as-modeling-language-not-method
- capturing-business-behavior-via-process-modeling
checks:
- The document names the life cycle variant it uses and lists its phases.
- Discovery results are recorded as as-is models with performance baselines.
- The to-be state of each process is defined in a design step.
- Monitoring of KPIs after go-live is described.
sources:
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
diagrams:
- file: diagram-1.bpmn
  caption: The five phases of the BPM life cycle as a loop.
review:
  status: generated
  flags: []
---

## Explanation

A business process is a series of steps an organization follows to reach a result. The BPM life cycle (BPM means business process management) describes how to look after such a process over time.

**The five phases**

Wikipedia groups BPM activities into five categories:

1. **Design.**
2. **Modeling.**
3. **Execution.**
4. **Monitoring.**
5. **Optimization.**

**As-is and to-be maps**

For more, see the article AS-IS and TO-BE View.

**Variants**

Other sources group the same work differently. The ABPMP describes BPM as a disciplined approach that covers identifying, designing, executing, documenting, measuring, monitoring and controlling processes.

## Example

A company wants to improve how it handles customer refund requests. In discovery, it draws the current refund process and measures how long refunds take. In analysis, it finds that approvals wait in one person's queue, and it names that as the cause. In design, it draws a new process with a different approval path. In implementation, it rolls the new process out to teams and systems. After go-live, it tracks refund times. When times drift upward, the cycle starts again.

## Trade-offs

Wikipedia notes that the steps can be viewed as a cycle, but economic or time constraints are likely to limit it to a few iterations. It also notes that the activities can be grouped into phases in different ways.
