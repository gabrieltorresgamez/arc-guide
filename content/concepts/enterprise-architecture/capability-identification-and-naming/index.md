---
title: Capability Identification and Naming
slug: capability-identification-and-naming
category: enterprise-architecture
kind: practice
summary: A business capability says what a business does, not how it does it. Identify capabilities that
  stay stable over time, and name them with nouns or gerunds, not verbs.
arc42:
- 3
- 5
- 12
step: s06-domain
related:
- business-capability
- business-capability-map
- capability-versus-process
- capability-heat-map
- capability-map-development-method
- bounded-context
- microservices-architecture
- business-architecture
checks:
- Capability names use nouns or gerunds, not verb-first phrases.
- Capabilities describe what the business does, and process steps are kept in separate process models.
- The capability map has about two to four levels.
- Capabilities and processes are linked many-to-many, not nested.
- Each service maps to a single business capability within a bounded context.
sources:
- url: https://albumi-docs.pages.dev/concepts/business-capabilities/
  title: Business Capabilities | Albumi Docs
  site: albumi-docs.pages.dev
  accessed: '2026-11-09'
- url: https://www.brcommunity.com/articles.php?id=b927
  title: 'Developing your Capability Architecture: It''s All about Being Able to Get Things Done (Commentary)'
  site: brcommunity.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/Azure/architecture/guide/architecture-styles/microservices
  title: Microservices Architecture Style - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A business capability is an ability or capacity that a business may have or exchange to reach a specific purpose or outcome. It is a stable statement of what the business does. It says nothing about how the work is delivered. See the article Business Capability for the full concept.

**Stable over time.** Capabilities should outlast the current organizational chart and its reorganizations. A capability map should be stable over time unless the business model itself changes.

**What versus how.** A capability is the what. A process is the how. The two do not nest inside each other. Processes and capabilities relate many-to-many. See Capability versus process.

**Naming.** Capability names use nouns or gerunds (a verb ending in "-ing", used as a noun). Processes and value streams use verb-noun phrases instead. A name written as a verb-noun phrase, like "Manage Orders", reads as a process, not a capability.

**Levels.** Useful capability maps break capabilities into a hierarchy of about two to four levels. See Business Capability Map.

**Prioritizing.** Heat maps use strategic importance ratings, which the capability's owner sets, to rank where portfolio attention goes first. Maturity ratings are combined with them to set priorities. See Capability Heat Map.

## Example

An insurance company lists "Claims Handling" as a capability. The process "Handle a claim" describes the steps. The capability should outlast reorganizations of the claims department. A name like "Process Claims" would read as a process, so it does not belong on the capability map.

## Trade-offs

A capability map stays stable across reorganizations. Too many levels also make a map hard to use, which is why about two to four levels is the useful range.
