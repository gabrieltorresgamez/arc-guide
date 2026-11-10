---
title: Pipe-and-Filter
slug: pipe-and-filter-pattern
category: styles-patterns
kind: pattern
summary: Pipe-and-Filter splits a big processing job into small, independent steps called filters. Pipes
  pass each step's output to the next. You can add, remove, or reorder steps, but all steps must agree
  on the data format.
arc42:
- 4
- 5
- 6
- 8
step: s07-solution-strategy
related:
- pipes-and-filters
- message-channel
- stream
- modifiability
- reusability
- coupling-and-cohesion
- idempotent-receiver
- architectural-pattern
checks:
- Each filter in the pipeline has a single, documented task.
- The input and output schema of every filter is documented, and each filter's input matches the previous
  filter's output.
- The document explains how errors are handled in each filter, and whether retries are safe.
- The document identifies the slowest filter and states whether parallel instances are used.
- The document addresses failure of a filter or pipe and its effect on the whole pipeline.
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
  caption: 'A simple pipeline: filters connected by pipes, from source to sink.'
review:
  status: generated
  flags: []
---

## Explanation

**The problem.** Some systems must run complex processing on a message. One large processing module makes this hard. It limits refactoring, optimization, and reuse of single steps when other parts of the application need the same processing. The goal is to keep the steps independent and flexible.

**The solution.** Divide the larger task into a sequence of smaller, independent steps. Each step is a *filter*. A *pipe* connects one filter to the next and passes the output message along.

**What filters and pipes do.**
- Each filter does one task. Filters are independent and usually stateless, meaning they keep no memory between messages.
- A filter may transform a message. It may also test the message against criteria, which adds conditional logic.
- Pipes do no routing and no other logic. They only connect filters.

**Why it helps modifiability.** Filters share a simple, uniform interface. You can add filters, leave some out, or put them in a different order. See Modifiability and Reusability.

**Data-format coupling.** A filter knows only its input and output schemas. A *schema* describes the shape of the data. Filters can appear in any order, as long as each filter's input schema matches the previous filter's output schema. A standardized schema helps. See Coupling and Cohesion.

**Throughput and parallelism.** Throughput is limited by the slowest filter. You can run several parallel instances of a slow filter to spread the load. If input and output are streams, filters can also work at the same time. Each one does not wait for the previous filter to finish. See Stream Connector.

**Pipes as queues.** One way to build a pipe is a message queue. Each filter listens on one queue, does its work, and posts the result to the next queue. An image-processing pipeline is one example. See Pipes and Filters for the integration-pattern view.

## Example

An online shop receives order files. Filter 1 checks that required fields are present. Filter 2 converts the order to the shop's standard format. Filter 3 adds customer details. Each filter reads a message and writes a message. If the shop later needs a fraud check, the team adds one filter between steps 2 and 3. The other filters stay unchanged, provided the new filter's input and output schemas match their neighbors'.

## Trade-offs

- **Whole-pipeline failure.** If one filter or pipe fails, the whole pipeline is likely to fail. Plan fault tolerance for the entire process.
- **Testing.** The pattern is usually built as a single pipeline. Any change calls for end-to-end testing of the whole filter chain.
- **Error handling.** Every filter must decide what to do on a breaking error. It can fail the pipeline or pass the exception on. Retries can duplicate work, so filters should be idempotent. That means repeating a step gives the same result. See Idempotent Receiver.
- **Shared state.** If steps need much external or shared state, every filter must load, use, and save it. This adds overhead compared with loading the state once. In that case the pattern might not be useful.
- **Distribution.** Spreading the pipeline across systems adds complexity.
- **Format coupling.** Filters can be reordered only while schemas match.
