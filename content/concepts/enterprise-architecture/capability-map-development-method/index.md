---
title: Capability Map Development Method
slug: capability-map-development-method
category: enterprise-architecture
kind: method
summary: 'Build a capability map in steps: set its purpose, keep it shallow, name owners, and describe
  what the business does rather than how. Capabilities should not overlap and should stay stable for years.'
arc42:
- 3
- 1
step: s06-domain
related:
- business-capability-map
- business-capability
- capability-identification-and-naming
- capability-versus-process
- capability-heat-map
- capability-map-use-cases
- operational-value-stream
- business-architecture
checks:
- The document states the purpose of the capability map and ties it to strategic decisions.
- Capabilities describe what the business does, not processes, workflows or systems.
- No two capabilities overlap; each business function has one home.
- The map has about seven to ten top-level capabilities and no more than two or three levels.
- Every capability has a named business owner.
sources:
- url: https://www.leanix.net/en/wiki/ea/best-practices-to-define-business-capabilities
  title: Best Practices to Define Business Capability Maps | SAP LeanIX
  site: leanix.net
  accessed: '2026-11-09'
- url: https://www.bpminstitute.org/resources/articles/capability-mapping-efforts-not-getting-you-your-destination/
  title: Capability mapping efforts not getting you to your destination? | BPMInstitute.org
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Business_capability
  title: Capability management in business - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A business capability map lists what a business must be able to do. The articles Business Capability Map and Business Capability cover the basics. This article covers the design rules.

**1. Set the purpose.** A map should support strategic decisions, not just serve as documentation.

**2. Describe what, not how.** A capability states what the business must be able to do. It does not name the activities, workflows or systems used to do it. The article Capability versus process explains the difference.

**3. Keep the top level small.** Aim for roughly seven to ten capabilities at the highest level.

**4. Limit the depth.** Two or three levels are usually enough for analysis and planning.

**5. Make capabilities mutually exclusive.** Capabilities must not overlap, so every business function has exactly one home. The set should also cover the whole business and be broken down hierarchically.

**6. Keep it stable.** The map should hold for years, even while processes, systems and organization structures change. So the org chart should not drive its design.

**7. Assign business owners.** Each capability needs a named business owner. That person is responsible for its definition and scope.

**8. Agree on names and definitions.** The map works only if the whole organization uses the same naming, definitions and structure. See Capability identification and naming.

**9. Put the map to work.** Link capabilities to applications. Use the links for heat maps, rationalization and roadmaps. A heat map shows which capabilities need attention, based on gaps in effectiveness, efficiency and performance.

## Example

A retailer sets the purpose: decide where to invest next year. It defines eight top-level capabilities, such as "Product Sourcing" and "Customer Service". It splits each into a second level only. Each capability gets one business owner. When the retailer reorganizes its departments, the map stays the same. The team then links each capability to the applications that support it and colors a heat map to show where attention is needed.

## Trade-offs

Keeping the map shallow keeps it clear and lowers maintenance effort.
