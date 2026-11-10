---
title: Context Map
slug: context-map
category: domain-driven-design
kind: artifact
summary: A context map shows how bounded contexts relate in strategic DDD. It records who provides and
  who consumes, using named relationship patterns. DDD has no fixed notation, so each map must explain
  its arrows.
arc42:
- 3
- 5
step: s06-domain
related:
- bounded-context
- domain-driven-design
- big-ball-of-mud
- ubiquitous-language
- bounded-context-canvas
- arc42-context-and-scope
checks:
- The document includes a context map that shows the relationships between bounded contexts.
- Arrows in the map are explained, including which side is upstream and which is downstream.
- Each relationship is labeled with a named pattern such as Shared Kernel, Open Host Service or Published
  Language.
- Customer-supplier is used only where the downstream side has influence on the upstream side.
sources:
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-StrategicDDDContextMap.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://contextmapper.org/docs/context-map/
  title: Context Map | Context Mapper
  site: contextmapper.org
  accessed: '2026-11-09'
- url: https://contextmapper.org/docs/customer-supplier/
  title: Customer/Supplier | Context Mapper
  site: contextmapper.org
  accessed: '2026-11-09'
- url: https://contextmapper.org/docs/shared-kernel/
  title: Shared Kernel | Context Mapper
  site: contextmapper.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/BoundedContext.html
  title: Bounded Context
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/news/2019/06/bounded-context-eric-evans/
  title: Defining Bounded Contexts — Eric Evans at DDD Europe - InfoQ
  site: infoq.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A small context map: arrows point from upstream to downstream; the shared kernel link is symmetric.'
review:
  status: generated
  flags: []
---

## Explanation

A context map is a picture of the bounded contexts in a system and how they relate. A bounded context is a part of the system with its own model and vocabulary (see the article Bounded Context). Strategic DDD is the big-picture side of Domain-Driven Design.

**Why draw one.** Different contexts often model the same concepts differently. Fowler says it is usually worthwhile to depict the relationships between contexts with a context map.

**Upstream and downstream.** The map draws relationships as influence and data flows. The upstream context provides information or services. The downstream context consumes them. In Context Mapper's notation, arrows point from upstream to downstream. Two relationships are symmetric, so neither side is upstream: partnership and shared kernel.

**Named relationship patterns.** Teams describe each link with a named pattern. Examples are Shared Kernel, Open Host Service and Published Language. Some details matter:

- Shared Kernel is the default symmetric relationship in Context Mapper.
- A generic upstream-downstream link is not automatically customer-supplier. Customer-supplier is a special form of it.
- In Context Mapper, Conformist does not apply inside a customer-supplier relationship. In customer-supplier, the downstream priorities factor into upstream planning.

**Notation.** DDD does not mandate any notation. Authors draw maps in their own styles, so explain what your arrows mean. Context Mapper offers a modeling language where the context map is the central element. It contains the bounded contexts and defines their relationships.

## Example

An online shop has three contexts: Ordering, Payment and Shipping. Ordering is upstream of Shipping, so an arrow points from Ordering to Shipping. The team labels the link with the pattern name it uses and adds a legend that says what the arrows mean.

## Trade-offs

Because DDD prescribes no notation, readers may misread arrows unless the map explains them. Choosing a pattern also takes care: for example, labeling a link customer-supplier claims that downstream priorities factor into upstream planning. Evans notes that when bounded contexts and subdomains become misaligned, two teams can end up working in the same bounded context, which raises the risk of a big ball of mud (see Big Ball of Mud).
