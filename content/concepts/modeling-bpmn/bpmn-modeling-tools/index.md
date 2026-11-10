---
title: BPMN Modeling Tool
slug: bpmn-modeling-tools
category: modeling-bpmn
kind: artifact
summary: A BPMN modeling tool is software for drawing process models. Camunda Modeler and bpmn.io are
  two examples. They differ in form, such as desktop or web, and viewer or editor. A free one suits first
  experiments.
arc42:
- 2
- 8
- 9
step: s10-document
related:
- bpmn-2-0-notation-overview
- bpmn-2-0-model-quality
- modeling-tool-vs-drawing-tool
- levels-of-process-modeling
- bpmn-modeling-tips
- bpm-life-cycle
checks:
- The document names the BPMN modeling tool the team uses and whether it runs as a desktop app or a web
  app.
- If models are shown on a website, the document states which viewer is used for it.
- If models are published straight from the tool to an environment, the document names that environment.
sources:
- url: https://github.com/bpmn-io/bpmn-js
  title: 'GitHub - bpmn-io/bpmn-js: A BPMN 2.0 rendering toolkit and web modeler. · GitHub'
  site: github.com
  accessed: '2026-11-09'
- url: https://camunda.com/platform/modeler/
  title: Camunda Modeler | BPMN Process Modeler | Camunda
  site: camunda.com
  accessed: '2026-11-09'
- url: https://bpmn.io/
  title: Web-based tooling for BPMN, DMN, CMMN, and Forms | bpmn.io
  site: bpmn.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.bpmn
  caption: 'A generic flow: draw a model in a tool, then publish it.'
review:
  status: generated
  flags: []
---

## Explanation

A BPMN modeling tool is software in which you draw business process models. BPMN is a standard notation for process diagrams. Two examples show how different the tools can be.

**bpmn.io.** Its toolkit bpmn-js views and edits BPMN 2.0 diagrams in a web browser. It comes in two forms:

- A viewer that shows diagrams on a website.
- A web modeler that you can embed in your own applications and customize.

**Camunda Modeler.** This tool also comes in two forms. One is a free desktop application. The other is a collaborative web application in Camunda 8. The desktop version is free and open source. Modeler can publish directly to Camunda SaaS or Self-Managed.

These two examples show the choices you face:

- **Where it runs.** Options are a local desktop app, a web app, or a toolkit built into your own software.
- **Edit or only view.** Some uses only need to display diagrams. Others need full editing.
- **Link to execution.** Camunda Modeler can send a model straight to an environment.

For the notation itself, see the article BPMN 2.0 Notation.

## Example

A small team wants to try process modeling. It installs the free desktop Camunda Modeler and draws its first order process. Later, the team wants to show the finished diagram on an internal website. It adds the bpmn-js viewer to that site.

## Trade-offs

- A free desktop tool costs nothing to obtain.
- An embeddable toolkit like bpmn-js can be customized to fit your application. Customizing means someone must do that work.
