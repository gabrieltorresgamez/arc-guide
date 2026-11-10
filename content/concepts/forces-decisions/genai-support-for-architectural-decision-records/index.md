---
title: GenAI Support for Architectural Decision Records
slug: genai-support-for-architectural-decision-records
category: forces-decisions
kind: practice
summary: Teams use generative AI to draft architectural decision records (ADRs) quickly and to explore
  options. The output can be wrong or invented, so humans must check every ADR before it enters the record.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- markdown-architectural-decision-records-madr
- adr-common-mistakes-and-remediations
- architectural-decision-management-practices
- architecture-decision-rationale
- arc42-architecture-decisions
checks:
- AI-generated ADRs show evidence of human review before being accepted.
- References in AI-drafted ADRs (APIs, web pages, product features) were checked to exist.
- Pros and cons suggested by an AI were validated for incorrect or exaggerated details.
- The final choice among AI-suggested options was made by people.
sources:
- url: https://www.equalexperts.com/blog/ai/accelerating-architectural-decision-records-adrs-with-generative-ai/
  title: Accelerating Architectural Decision Records (ADRs) with Generative AI | Equal Experts
  site: equalexperts.com
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2604.03826
  title: 'Context Matters: Evaluating Context Strategies for Automated ADR Generation Using LLMs'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://handsonarchitects.com/blog/2025/using-generative-ai-as-architect-buddy-for-adrs/
  title: Using Generative AI to Help Write ADRs | Hands-on Architects
  site: handsonarchitects.com
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2504.20781v3
  title: Using LLMs in Generating Design Rationale for Software Architecture Decisions
  site: arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architectural decision record (ADR) captures why a team chose a design. See Architectural Decision Record for the basics. Generative AI, meaning large language models (LLMs), can help with this work.

**Drafting ADRs.** The biggest reported win is speed, including the speed of retrospective documentation, where a team writes down decisions it made earlier. The AI produces the draft. People then focus on the core arguments.

**Using prior ADRs as context.** A study of LLM-generated ADRs found that context-aware prompting substantially improves fidelity. Giving the model the ADRs already in a repository helps it draft the next one.

**Exploring options.** Practitioners ask the model for two to five viable options, each with pros and cons. They then pick one in a human brainstorming session. The model supplies candidates, and the team may also ask it to recommend a decision and then re-examine that decision.

**Validating the output.** The model may add incorrect or exaggerated details to the pros and cons, so a person must check them. Reports show concrete failures:

- One team reported that AI tools frequently hallucinated references, including non-existent APIs, web pages, or product features.
- A study of LLM-generated design rationale found that 1.59% to 3.24% of the arguments not mentioned by human experts were potentially misleading.

**Why wrong ADRs hurt.** A wrong ADR becomes noise. It can also mislead future team members who trust the record.

## Example

A team never wrote down why it chose a message queue two years ago. It gives an LLM its existing ADRs and a few keywords. The model drafts a record in the team's usual format within minutes. An architect reads the draft and finds a product feature that does not exist. The architect removes that claim, corrects the pros and cons, and only then commits the record.

## Trade-offs

**Benefit:** much faster drafting, especially for decisions made in the past, so people can spend their time on the core arguments.

**Cost:** every draft needs careful human review. Invented references and exaggerated pros and cons are real risks, and a wrong ADR can mislead later readers.
