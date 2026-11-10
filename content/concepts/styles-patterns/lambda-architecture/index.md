---
title: Lambda Architecture
slug: lambda-architecture
category: styles-patterns
kind: style
summary: Lambda architecture sends incoming data down two paths. A slow batch path gives accurate results.
  A fast speed path gives quick, less accurate results. Queries combine both, at the cost of duplicated
  logic.
arc42:
- 4
- 5
- 9
- 11
step: s08-integration-data
related:
- architectural-style
- event-sourcing-with-distributed-event-log
- stream
- data-architecture
- architectural-trade-off-thinking
- scalability
- technical-debt
- command-query-responsibility-segregation
checks:
- The document states which data goes through the batch (cold) path and which through the speed (hot)
  path.
- Raw batch-layer data is described as immutable and append-only, so views can be recomputed.
- The document explains how the serving layer combines batch views with speed-layer updates for queries.
- The latency versus accuracy trade-off between hot and cold results is stated.
- The duplicated processing logic across both paths is recorded as a known drawback.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/databases/guide/big-data-architectures
  title: Big Data Architectures - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www.oreilly.com/radar/questioning-the-lambda-architecture/
  title: Questioning the Lambda Architecture – O’Reilly
  site: oreilly.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Incoming data flows down a batch path and a speed path. The serving layer combines both for
    queries.
review:
  status: generated
  flags: []
---

## Explanation

Big data solutions typically include batch processing of data at rest and real-time processing of data in motion. Lambda architecture keeps these two apart in separate layers (see Architecture Style for how styles are described).

Every incoming record goes down two paths.

**Batch layer (cold path).** It stores all incoming data in its raw form and runs batch processing on it. The result is called a batch view.

**Speed layer (hot path).** It analyzes data in real time. It aims for low latency, meaning fast answers. It accepts lower accuracy in return.

**Serving layer.** It indexes the batch view so queries run efficiently. The speed layer adds incremental updates based on the newest data. A query stitches together results from both systems to form a complete answer.

**Immutable raw data.** The batch layer never overwrites old data. New data is appended, and changes are stored as time-stamped events. Because the raw data stays intact, the system can recompute batch views. It can also create new views as it evolves. One well-known critic likes this idea of keeping the input data unchanged.

**Alternative.** Kappa architecture has the same goals. It sends all data through one stream-processing path instead of two. To recompute results, it replays the stream.

## Example

An online shop wants to show sales per product. Every order goes down both paths. The batch path recomputes exact totals from all stored orders, which takes a long time. The speed path counts new orders right away, with less accuracy. The serving layer shows the last batch totals plus the quick counts for recent orders. When the next batch run finishes, its exact numbers replace the quick estimates.

## Trade-offs

**Latency versus accuracy.** The cold path is accurate but slow. The hot path is timely but less accurate. Clients choose between timely, less accurate results and accurate, delayed results.

**Complexity.** The same processing logic appears in two places, built with different frameworks. This duplicates computation logic and makes managing both paths complex. A well-known criticism is this dual-code problem: you write and maintain the transformation logic twice. Lambda also needs reprocessing and live processing to run continuously.

**Alternative.** Kappa architecture removes the second path. It replays one stream to recompute results.
