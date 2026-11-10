---
title: Business Capability Map
slug: business-capability-map
category: enterprise-architecture
kind: artifact
summary: A business capability map lists what a business must be able to do, in a few levels, without
  saying how or by whom. It stays stable for years while processes, systems and teams change.
arc42:
- 1
- 3
- 4
step: s06-domain
related:
- business-capability
- capability-map-development-method
- capability-heat-map
- capability-versus-process
- capability-map-use-cases
- capability-identification-and-naming
- business-architecture
- operational-value-stream
checks:
- Each capability states what the business must be able to do, not how it is done or who does it.
- The map has about seven to ten level-1 capabilities and uses three levels or fewer.
- The map was drafted from strategic documents such as annual goals, roadmaps or investment themes.
- The map has a review schedule, at least once a year.
- Capabilities change only when the business model changes, not when teams, processes or applications
  change.
sources:
- url: https://www.leanix.net/en/wiki/ea/how-to-create-a-business-capability-map
  title: How to Create a Business Capability Map? | SAP LeanIX
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.leanix.net/en/wiki/ea/best-practices-to-define-business-capabilities
  title: Best Practices to Define Business Capability Maps | SAP LeanIX
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.ardoq.com/knowledge-hub/business-capability-map
  title: 'Business Capability Map: The Essential Guide With Examples'
  site: ardoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: A generic three-level capability map as a hierarchy.
review:
  status: generated
  flags: []
---

## Explanation

A business capability is something the business must be able to do. It says nothing about how the work is done or who does it.

A capability map arranges these capabilities in a hierarchy. Maps usually have seven to ten level-1 capabilities. Three levels are typically enough for enterprise analysis. The aim is traceability without overcomplication.

**Stable by design**

Capabilities stay stable for years. Processes, systems and organizational structures change around them. So update a capability only when the business model changes. Do not update it because a team, a process or an application shifts.

**What it is not**

- *Process model:* a capability does not describe activities, workflows or systems. It describes what is needed.
- *Org chart:* org charts change often. Capabilities should stay stable.

**Building a first draft**

Start from strategic documents. Examples are annual goals, transformation roadmaps and investment themes.

**Keeping it sound**

Treat the map as a living asset. Review it regularly, at least once a year.

For related ideas, see the articles Business Capability, Capability Map Development Method, Capability Heat Map and Capability versus process.

## Example

A small online retailer drafts its map from its annual goals. Level 1 has areas such as "Customer", "Product" and "Finance". Under "Customer", level 2 might hold "Customer Service". A level-3 capability there could be "Handle Complaints".

Later the retailer moves complaints to a new team and buys a new ticket tool. The capability "Handle Complaints" does not change. Only the team and the tool change.

## Trade-offs

Keeping the map abstract and stable means it does not show how work flows or who does it. You need process models or org charts for that. Adding more levels gives more detail but works against the aim of avoiding overcomplication. A map that is never reviewed stops matching the business.
