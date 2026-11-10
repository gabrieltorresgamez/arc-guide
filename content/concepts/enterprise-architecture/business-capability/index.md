---
title: Business Capability
slug: business-capability
category: enterprise-architecture
kind: concept
summary: A business capability is an ability an organization has to reach a specific purpose or outcome.
  It describes what the business can do, not how the work is done. Capabilities form levels of detail.
arc42:
- 1
- 3
- 4
step: s06-domain
related:
- business-capability-map
- capability-versus-process
- capability-identification-and-naming
- capability-heat-map
- operational-value-stream
- business-architecture
- business-domain-understanding
- capability-map-development-method
checks:
- Capabilities are described as what the organization can do, not as steps of how work is done.
- The capability map breaks capabilities into levels, each more detailed than the one above.
- Capabilities are kept distinct from organization units, and level-one capabilities are mapped to major
  organization units.
- Value streams are not confused with business processes, and capabilities are mapped to value stream
  stages.
sources:
- url: https://www.bpminstitute.org/resources/articles/capabilities-value-streams-business-architectures-essential-alliance
  title: 'Capabilities & Value Streams: Business Architecture’s Essential Alliance | BPMInstitute.org'
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://www.ardoq.com/knowledge-hub/value-streams
  title: Differences Between Business Capabilities, Processes, & Value Streams
  site: ardoq.com
  accessed: '2026-11-09'
- url: https://if4it.org/best-practices/capabilities-inventory-and-attributes/understand-the-relationship-between-the-capabilities-inventory-and-the-value-streams-inventory/
  title: Understand the relationship between the Capabilities Inventory and the Value Streams Inventory
    - Capabilities Inventory and Attributes | The International Foundation for Information Technology
    (IF4IT)
  site: if4it.org
  accessed: '2026-11-09'
- url: https://microservices.io/patterns/decomposition/decompose-by-business-capability.html
  title: 'Pattern: Decompose by business capability'
  site: microservices.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A capability breaks down into levels and can be used by several value streams.
review:
  status: generated
  flags: []
---

## Explanation

A business capability is a particular ability that a business can have or trade in order to reach a specific purpose or outcome. Capabilities represent the core functions an organization needs to run its business.

**What, not how.** A capability says what the organization can do. A process says how the work gets done. The article "Capability versus process" covers the difference in more detail.

**Hierarchy.** Capabilities are shown on a capability map. A map is a set of boxes. Each box breaks down into smaller boxes, and each level adds detail. People call these levels one, two and three. See "Business Capability Map" for how to read one.

**How it differs from related ideas.**

- *Value stream:* a high-level chain of activities, from start to finish, that gives value to a customer or another stakeholder. It is not a business process. Processes break down from it.
- *Capability and value stream:* a value stream uses one or more capabilities, in sequence or in parallel. Capabilities are stable. The same capability can serve several value streams. Mapping capabilities onto the stages of a value stream shows the key ones.
- *Organization unit:* level-one capabilities map to major organization units.

**Why it helps.** Capabilities often match domain objects. Finding them, and the services built on them, requires an understanding of the business. See "Business Domain Understanding".

## Example

An insurer lists "Claims Handling" as a capability. Below it sit smaller capabilities at the next level. The company can later change the steps of its claims process. The capability stays on the map. A "claims" value stream and a "policy renewal" value stream could both use the same capability.

## Trade-offs

One point follows from the definitions: a capability map says what the business can do. It does not show how work flows. For that, you need processes and value streams.
