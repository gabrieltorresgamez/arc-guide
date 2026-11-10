---
title: Stream Connector
slug: stream
category: integration
kind: pattern
summary: A stream connector passes data from one step to the next while the data flows. Buffers absorb
  speed differences between sender and receiver. Pipes and filters use it to build processing chains.
arc42:
- 5
- 6
- 8
step: s08-integration-data
related:
- pipes-and-filters
- pipe-and-filter-pattern
- software-connector
- file-transfer
- point-to-point-channel
- synchronous-vs-asynchronous-connector
- connector-cardinality
- classification-of-integration-patterns
checks:
- The document states how each pipe connects filters and which output feeds which input.
- The document says how differences in sender and receiver speed are handled, for example by a buffer.
- Where back pressure is needed, the document names the mechanism or standard used.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html
  title: Pipes and Filters - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Pipeline_(Unix)
  title: Pipeline (Unix) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.reactive-streams.org/
  title: ''
  site: reactive-streams.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A simple pipeline: data flows from a source through two filters to a sink.'
review:
  status: generated
  flags: []
---

## Explanation

A stream connector moves data between parts of a system in a steady flow. Each part reads input from the previous one and writes output to the next one. Unix pipelines work this way: each process uses standard streams to read from its predecessor and write to its successor.

**Pipes and filters.** This style (see the article Pipes and Filters) splits work into small steps called filters. A pipe connects one filter to the next and carries the output messages of one filter to the input of the next. In the basic form, a filter has one input port and one output port.

**Running at the same time.** In a Unix pipeline, the processes run concurrently. The downstream process starts while the upstream one is still running. So work on the data begins before the sender has finished.

**Buffering.** A sender and a receiver may work at different speeds. A Unix pipe handles this with a buffer. It holds the sender's output until the receiver reads it. On most Linux systems, this buffer is 64 KiB.

**Back pressure.** Some stream technologies let a slow receiver slow the sender down. Reactive Streams is an initiative that standardizes asynchronous stream processing with non-blocking back pressure.

## Example

A team builds a log-cleaning chain. A first step reads raw log lines. A second step removes noise. A third step counts errors. Pipes connect the steps. All three run at once, so the counter starts on the first lines while the reader is still reading later ones. If the counter is slower, a buffer holds the waiting lines.

## Trade-offs

In a Unix pipe, if the buffer fills up, the sender is blocked until the receiver removes some data. Check what reliability guarantees the stream connector of each technology offers.
