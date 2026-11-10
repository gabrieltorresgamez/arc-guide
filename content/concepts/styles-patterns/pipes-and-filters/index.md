---
title: Pipes and Filters
slug: pipes-and-filters
category: styles-patterns
kind: style
summary: Pipes and Filters splits a large processing task into small, independent steps called filters.
  Pipes pass each step's output to the next. You can add, remove, or reorder steps, but the slowest step
  limits speed.
arc42:
- 4
- 5
- 6
- 8
step: s07-solution-strategy
related:
- pipe-and-filter-pattern
- architectural-style
- message-filter
- message-channel
- content-based-router
- message-translator
- idempotent-receiver
- performance-tactics
checks:
- Each filter's input and output formats are documented, and adjacent filters have matching formats.
- Pipes contain no routing or business logic; all logic sits in filters.
- The document states how each filter handles breaking errors and whether it is idempotent.
- The slowest filter is identified, with a plan such as parallel instances to avoid a bottleneck.
- The document states whether the pipeline is monolithic and what a failed filter means for the whole
  pipeline.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html
  title: Pipes and Filters - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters
  title: Pipes and Filters pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Messages flow from a source through filters, linked by pipes, to a sink.
review:
  status: generated
  flags: []
---

## Explanation

Pipes and Filters breaks one large processing task into a sequence of smaller, independent steps. Each step is a **filter**. Filters are linked by **pipes**, which carry the output messages of one filter to the next filter.

**Filters.** In the basic form, a filter has one input and one output. It receives a message from the pipe before it, does its work, and sends a result into the pipe after it. A filter can transform a message. It can also test a message against criteria, which adds conditional logic. Filters are independent, self-contained, and typically stateless, meaning they keep no memory between messages.

**Pipes.** Pipes only connect. They contain no routing and no logic.

**Free ordering.** A filter knows only the format of its input and its output. So filters can be arranged in any order, as long as each filter's output format matches the next filter's input format. A standardized format makes reordering easier. Because all filters share the same external interface, you can add new filters, omit existing ones, or rearrange them without changing the filters themselves.

**Implementation.** Teams usually build this as one monolithic pipeline, meaning one deployed unit. A pipeline can also use message queues as pipes, with each filter listening on a queue. For example, Azure Functions with Queue Storage can form an image-processing pipeline. Each filter reads a message, does its work, and posts a new or transformed message to the next queue.

**Error handling.** Every filter must decide what to do on a breaking error. It either fails the pipeline or passes the exception on. Filters should also be idempotent, so repeating the same message is safe.

## Example

An order-intake pipeline has three filters. The first checks that an order has all required fields. The second converts the order into the internal format. The third adds a shipping label. Each filter reads from its input queue and writes to its output queue. If the team later needs a fraud check, they add a fourth filter between two existing ones. The other three stay unchanged, as long as the formats on both sides still match.

## Trade-offs

**Benefits.** Filters can be added, omitted, or rearranged without changing them. Small single-purpose steps are easy to swap and extend.

**Costs.**
- The time to process one request depends on the slowest filter. That filter can become a bottleneck. Running several parallel instances of a slow filter improves throughput.
- In the usual monolithic form, a failed filter or pipe likely fails the whole pipeline. Any change calls for retesting end to end.
- Filters must agree on input and output formats. Each filter must also handle its own errors.
