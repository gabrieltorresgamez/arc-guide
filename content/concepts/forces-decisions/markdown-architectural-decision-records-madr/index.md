---
title: Markdown Architectural Decision Records
slug: markdown-architectural-decision-records-madr
category: forces-decisions
kind: artifact
summary: MADR is a short Markdown template for recording architecturally significant decisions in a structured
  way. Each decision is one file in docs/decisions. Full, minimal, and bare versions exist.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- arc42-architecture-decisions
- y-statement
- documentation-as-code
- adr-common-mistakes-and-remediations
- architecturally-significant-decision
- middleware-architectural-decision-example
checks:
- Decision files sit in docs/decisions and follow the NNNN-title-with-dashes.md naming pattern.
- Each decision lists its consequences, both good and bad.
- Each decision says how compliance with it will be confirmed.
- Metadata such as status, date, and decision-makers is kept only where it is useful.
sources:
- url: https://adr.github.io/madr/
  title: About MADR | MADR
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

MADR stands for Markdown Architectural Decision Records. It is a streamlined template for writing down decisions that shape a system's architecture. Each decision becomes one Markdown file. See Architectural Decision Record for the general idea.

**Where it comes from.** A 2011 blog post by Michael Nygard, "Documenting Architecture Decisions," popularized ADRs. arc42 section 9 recommends one ADR per important decision. It says you may follow Nygard's structure. MADR is another template for the same job. See arc42 Architecture Decisions.

**Which version to use.** MADR 4.0.0 has a full template. Its release notes also point to "bare" and "minimal" templates.

**Files and names.** MADR files live in `docs/decisions`. Names follow the pattern `NNNN-title-with-dashes.md`.

**Metadata.** A decision file can start with YAML front matter. This is a small block of key-value pairs at the top of the file. Typical fields are status, date, decision-makers, consulted, and informed. All are optional. You can remove any field you do not need.

**Consequences.** MADR lists consequences as bullets marked "Good, because" or "Bad, because". A bad consequence might be a compromise on a desired quality. arc42 gives the same advice: list all consequences, not only the positive ones.

**Confirmation.** The template has an optional confirmation element. It describes how the team can check that the implementation follows the decision. The template notes that this element is included in many ADRs.

## Example

A team picks a message queue for order processing. They add the file docs/decisions/0007-use-message-queue-for-orders.md. The front matter gives the status and names the decision-makers. The body lists the good and bad consequences. A confirmation note says how the team will check that the code follows the decision.

## Trade-offs

Metadata fields are optional, so you can drop what you do not need. The confirmation element is also optional.
