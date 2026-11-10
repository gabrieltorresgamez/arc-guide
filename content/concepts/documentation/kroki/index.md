---
title: Kroki
slug: kroki
category: documentation
kind: framework
summary: Kroki is an open-source service that offers one HTTP API for creating diagrams from text, across
  many diagram libraries. You can use the free public service or run your own instance.
arc42:
- 7
- 8
step: s10-document
related:
- diagrams-as-code
- documentation-as-code
- arc42-documentation-template
- c4-model
checks:
- The documentation states whether diagrams are rendered with the free public Kroki service or a self-managed
  instance.
- If GET requests are used, the diagram source is deflate-compressed and base64-encoded in the URL.
- If POST with plain text is used, the output format is chosen with the Accept header.
sources:
- url: https://kroki.io/
  title: Kroki!
  site: kroki.io
  accessed: '2026-11-09'
- url: https://docs.kroki.io/kroki/setup/usage/
  title: 'Usage :: Kroki Documentation'
  site: docs.kroki.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One API in front of many diagram libraries
review:
  status: generated
  flags: []
---

## Explanation

Kroki turns diagram descriptions written as text into images. Kroki puts a single API in front of many diagram tools. You learn one way of working and use it for every supported library.

**Why one API helps**

The underlying diagram libraries are written in many languages, such as Haskell, Python, JavaScript, Go, PHP, and Java. You do not need to install each library and its requirements yourself.

**Two ways to run it**

Kroki is available as a free public service. It is also available as a self-managed instance. With the self-managed option, you install Kroki yourself, either on your own servers or in a cloud setup.

**Calling the API**

There are two request styles:

- **GET:** The diagram source goes into the URL. You must compress it with deflate and then encode it with base64.
- **POST with plain text:** You send the diagram source as the request body. You choose the output format with the `Accept` header.

**Who builds it**

Kroki is open source under the MIT license. Yuzu tech builds and maintains the free service, with support from Exoscale.

## Example

A team keeps its architecture diagrams as text files in the same repository as its documents. The diagrams use different libraries, and the team installs none of them. A script sends each text file to Kroki and receives an image back. For a quick test, the team uses the free public service.

## Trade-offs

This article does not cover privacy, security, or performance differences between the public service and a self-managed instance. Check those points yourself before sending sensitive diagrams to any external service. The self-managed option means you install and run Kroki on your own infrastructure or in the cloud.
