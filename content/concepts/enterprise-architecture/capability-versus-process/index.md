---
title: Capability versus Process
slug: capability-versus-process
category: enterprise-architecture
kind: concept
summary: A capability says what an organization can do. A process says how the work gets done, step by
  step. Keep the two apart and link them, because capabilities stay stable while processes change.
arc42:
- 1
- 3
- 5
step: s06-domain
related:
- business-capability
- business-capability-map
- operational-value-stream
- capability-identification-and-naming
- business-architecture
- capability-map-use-cases
- capturing-business-behavior-via-process-modeling
checks:
- Capabilities are named with nouns or gerunds, and processes use verb-noun names such as Receive Order.
- The capability map and the process map are separate and linked by relationships, not nested in each
  other.
- Capability descriptions state what the business must be able to do and do not describe tasks, sequence,
  or systems.
- Capabilities are mapped to value stream stages to show which capabilities each stage needs.
sources:
- url: https://www.leanix.net/en/blog/business-capabilities-vs-business-processes-whats-the-difference
  title: 'Business Capabilities vs Business Processes: What’s the Difference?'
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.brcommunity.com/articles.php?id=b927
  title: 'Developing your Capability Architecture: It''s All about Being Able to Get Things Done (Commentary)'
  site: brcommunity.com
  accessed: '2026-11-09'
- url: https://www.ardoq.com/knowledge-hub/value-streams
  title: Differences Between Business Capabilities, Processes, & Value Streams
  site: ardoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A capability is linked to value stream stages and processes, but kept in a separate map.
review:
  status: generated
  flags: []
---

## Explanation

People often mix up capabilities and processes. They answer different questions.

**Capability: what the organization can do.** A business capability names what a business must be able to do to deliver an outcome that serves its mission. It describes a core ability the organization needs to run its business. It is abstract and conceptual. It does not say how the work is done.

**Process: how the work is done.** A business process is a linked series of activities that turns inputs into outputs. It describes the tasks, their sequence, and the systems used to carry them out. That adds operational detail that a capability leaves out.

**Naming helps keep them apart.** Processes use a verb-noun form, such as Receive Order or Ship Product. Capabilities use nouns or gerunds (the "-ing" form of a verb), not plain verbs.

**Stability differs.** Capabilities should stay stable over time unless the business model itself changes. Processes can change even when the business model stays the same, for example as the business evolves.

**How they connect.** Value streams show how capabilities are used to create value. Processes give the operational detail. If you map capabilities to the stages of a value stream, you see which capabilities each stage needs. See Business Capability Map and Operational Value Stream for more.

**A common mistake.** Teams nest capability maps and process maps inside one another. Keep them as separate maps and link them through relationships.

## Example

A retailer has a capability named Order Fulfillment. It states that the company must be able to get ordered goods to customers. It says nothing about steps.

Processes sit alongside it in a separate process map. They are named Receive Order and Ship Product. They list the tasks, their sequence, and the systems used. If the retailer changes how it ships, the Ship Product process changes. The capability stays the same, and the link between the two maps shows which processes support it.


