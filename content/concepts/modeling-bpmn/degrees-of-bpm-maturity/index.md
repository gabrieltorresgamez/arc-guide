---
title: Degrees of BPM Maturity
slug: degrees-of-bpm-maturity
category: modeling-bpmn
kind: concept
summary: Processes can be automated to different degrees, from steps with people involved to straight-through
  processing with no human at all. RPA and AI agents help move a process along, and each degree needs
  matching support in the architecture.
arc42:
- 4
- 8
- 9
step: s07-solution-strategy
related:
- process-automation-magnifies-efficiency
- waves-of-business-process-management
- bpm-life-cycle
- workflow-pattern
- process-manager
- exception-handling
- bpmn-task-marker
- levels-of-process-modeling
checks:
- The document states, for each process, how far it is automated, and whether partial automation is accepted.
- Where RPA bridges a legacy system, the document plans its later replacement by APIs or agents.
- RPA bots run as normal process steps with shared error handling, retries, and audit.
- AI agents run inside an orchestrated process with guardrails, monitoring, and audit.
- Low-confidence agent results route to human review before the process continues.
sources:
- url: https://camunda.com/process-orchestration/
  title: 'Process Orchestration: Guide to Benefits & Software | Camunda'
  site: camunda.com
  accessed: '2026-11-09'
- url: https://www.ibm.com/think/topics/straight-through-processing
  title: What Is Straight-Through Processing? | IBM
  site: ibm.com
  accessed: '2026-11-09'
- url: https://camunda.com/orchestrate/building-blocks/
  title: 'Process Building Blocks: Decisions, RPA & IDP | Camunda'
  site: camunda.com
  accessed: '2026-11-09'
- url: https://aisel.aisnet.org/ecis2005/37/
  title: '"Towards a Business Process Managment Maturity Model" by Michael Rosemann and Tonia de Bruin'
  site: aisel.aisnet.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: An AI agent handles a request; low-confidence results go to a human reviewer, the rest finish
    straight through.
review:
  status: generated
  flags: []
---

## Explanation

Automation is not all or nothing. Task automation means technology performs a task without human intervention. Process automation combines orchestration (coordinating the steps of a process) with task automation. The degree of automation can vary from process to process.

**The far end: straight-through processing.** Straight-through processing (STP) means a transaction is completed from start to finish without human intervention. Teams measure it as a rate: the share of the process that is automated. Partial automation still pays off, so a process does not need full STP to bring benefits.

**Humans in the loop.** Between manual work and STP, people can stay in specific steps. An AI agent can handle ambiguous situations that fixed rules cannot cover. In intelligent document processing, a person can check results the system is unsure about before the process goes on.

**Enablers: RPA and AI agents.**
- Robotic process automation (RPA) began as screen-scraping of graphical user interfaces. It also lets teams keep legacy systems in the process.
- Keep the legacy system in the process today. Replace the RPA tasks with APIs or agents when you are ready.
- AI agents need governance. An orchestration solution should enforce guardrails around them, so people can monitor and audit them inside the process.

**Architectural implications.** RPA bots can run as ordinary process steps. They then share error handling, retries, and audit with every other step. When a legacy system gains an API, the bot step can be replaced with a connector without redesigning the process.

**Maturity models are a different lens.** The Rosemann/de Bruin BPM maturity model has six core factors: strategic alignment, governance, method, IT, people, and culture. It was built through Delphi studies.

## Example

An insurer handles address-change requests. At first, a clerk reads each request and updates a legacy system by hand. The team adds an RPA bot that types the update into the legacy screen, run as a normal step in the process. An AI agent then reads free-text requests. When its confidence is low, the request goes to a clerk. Later the team replaces the bot with an API call. Most requests now finish with no human step, so the share completed straight through rises.

## Trade-offs

You must govern AI agents with guardrails, monitoring, and audit. RPA keeps legacy systems in the process today, and you can replace RPA tasks with APIs or agents when you are ready. Full STP is not required: partial automation still has value, so choose the degree per process. Weigh cost, volume and compliance case by case.
