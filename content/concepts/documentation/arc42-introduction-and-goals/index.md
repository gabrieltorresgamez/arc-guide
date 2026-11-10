---
title: arc42 Introduction and Goals
slug: arc42-introduction-and-goals
category: documentation
kind: artifact
summary: Section 1 of arc42 gives a short overview of what the system must achieve. It lists the top three
  to five quality goals and a table of stakeholders with their expectations.
arc42:
- 1
step: s01-goals-stakeholders
related:
- arc42-documentation-template
- arc42-quality-chapter
- arc42-constraints
- arc42-context-and-scope
- stakeholder
- quality-attribute-scenario
- stakeholder-identification
checks:
- Section 1 lists at most five quality goals.
- Each quality goal has a brief scenario, not just a keyword.
- The stakeholder table gives roles, names and expectations.
- The requirements overview is short and links to existing requirements documents.
- Detailed quality requirements are deferred to section 10.
sources:
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/1-16/
  title: 'Tip 1-16: Describe only the top 3-5 quality goals in the introduction! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Section 1 of arc42 (see the article arc42 Architecture Documentation Template) is the entry point. It describes the requirements and driving forces that architects and the development team must consider.

**What goes into it**

- **A short requirements overview.** Keep it brief. If requirements documents already exist, point to them instead of copying them.
- **Quality goals.** These are the most important qualities the architecture must deliver. Limit them to the top three, at most five.
- **A stakeholder table.** A stakeholder is anyone with an interest in the system. The table lists roles, person names, and what each expects from the architecture and its documentation.

**Quality goals need scenarios**

A keyword such as "performance" or "security" says little. Add a brief scenario that shows what the goal means in practice. Generic keywords alone are a common pitfall.

**Details live elsewhere**

Section 1 holds only the top goals. Complete and detailed quality requirements belong in section 10. See the article arc42 Quality Requirements Chapter for that part.

## Example

A team documents a tool that checks websites for broken links. In section 1 they list quality goals in priority order:

1. **Correctness:** every broken internal link is found.
2. **Safety:** the tool never changes the files it checks.
3. **Performance:** checks run fast enough for regular use.

Each goal gets a short scenario. The stakeholder table lists the website authors, who expect reliable reports, and the developers, who expect clear documentation. The requirements overview is a few lines with a link to the full requirements document.

## Trade-offs

A short section is easy to read, but it leaves out detail. Readers who need the full picture must follow links to the requirements documents and to section 10. Because only the top three to five quality goals are described here, other qualities will not appear in this section.
