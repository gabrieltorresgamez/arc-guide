---
title: File Transfer
slug: file-transfer
category: integration
kind: style
summary: File Transfer is an integration style where each application writes files of shared data and
  reads files that others wrote. Teams must agree on the file format and how often files are produced.
arc42:
- 3
- 5
- 8
step: s08-integration-data
related:
- integration-pattern
- shared-database
- remote-procedure-call
- messaging
- message-translator
checks:
- The document states the file format used between each producer and consumer, such as text, XML, or a
  mainframe feed.
- The document says how often each file is produced and why that interval fits the business.
- The document names who is responsible for transforming files between formats.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/FileTransferIntegration.html
  title: File Transfer - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One application writes a file of shared data and another reads it.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

File Transfer is one of four integration styles. An integration style is a general way to connect applications so they can share data (see the article Integration Styles).

The idea is simple. Each application produces files that hold information other applications need. Each application also consumes files that others produced.

**File format.** Teams must decide what the files look like. Mainframe systems commonly use COBOL-based data feeds, Unix systems use text files, and modern systems often use XML.

**Transformation.** One application's output is rarely what another application needs. Someone must convert files from one format to another. Integrators take on this job.

**Batch frequency.** Applications produce files at regular intervals. The interval should fit the nature of the business.

## Example

A billing application writes a file of new invoices at the end of each business day. A reporting application reads that file and loads the invoices. A small conversion step first turns the billing format into the format that reporting expects.

## Trade-offs

The source pages do not cover benefits or drawbacks in depth. One point follows directly from them: because outputs rarely match what consumers need, files usually need processing along the way, and integrators take on that transformation.
