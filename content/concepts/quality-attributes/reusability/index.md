---
title: Reusability
slug: reusability
category: quality-attributes
kind: quality-attribute
summary: Reusability is how well something you built, such as code or a design, can serve in more than
  one system. You can reuse by copying or by depending on shared code. Each way has costs and risks.
arc42:
- 4
- 8
- 9
- 11
step: s07-solution-strategy
related:
- maintainability
- iso-iec-25010-quality-model
- modularity
- technical-debt
- coupling-and-cohesion
- modifiability
- uml-interface
- it-component-catalogue
checks:
- The document states whether each reused asset is copied or pulled in as a dependency.
- External dependencies have a documented way to manage their risks.
- Reused assets are checked as fit for purpose, or designed for reuse.
- Copied code has a documented plan for maintenance and updates.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/57-maintainability
  title: Maintainability
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://arxiv.org/html/2409.04830v1
  title: 'Beyond Dependencies: The Role of Copy-Based Reuse in Open Source Software Development'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://mcilroy.cs.dartmouth.edu/components.txt
  title: ''
  site: mcilroy.cs.dartmouth.edu
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2508.19834
  title: On the Future of Software Reusein the Era of AI Native Software Engineering
  site: arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO 25010 is a standard quality model (see ISO/IEC 25010 Product Quality Model). It lists reusability under maintainability. The term describes how far a product can serve as an asset in several systems or when building other assets.

**Why people want it.** Starting from scratch can cost more time and effort than reusing existing high-quality code. In 1968, McIlroy pointed out that software had no components industry, unlike hardware. He saw no manufacturers or catalogues of standard parts. He wanted standard catalogues of routines.

**Two ways to reuse.**
- *Copying* places the original code into a new repository. It is quick. But copying can lead to challenges in maintaining and updating the copied code.
- *Depending* leaves the external code unmodified. A package manager pulls it in.

**Risks.**
- Widespread copying can spread vulnerable code. Inconsistent changes to duplicated code can cause unpredictable behavior.
- Dependencies carry risks too if they are not properly managed.
- An asset not designed for reuse, or not proven fit for purpose, can cause quality and safety problems.

**What held reuse back.** Before object-oriented languages became popular, software systems lacked interfaces good enough for reuse on a larger scale. McIlroy expected a components industry to settle on a few standard interface types.

## Example

A team needs the same date-formatting logic in three products. In the first option, it copies the code into each product. A bug fix then has to be repeated three times, and one copy may be missed. In the second option, it publishes the logic as a shared package that all three products pull in. Now there is one place to fix bugs. But the team must also manage that dependency so it does not become a risk.

## Trade-offs

Copying is fast, but it can lead to maintenance and update challenges and can spread flaws. Depending on shared code introduces dependency risks that need to be managed. Reusing code that was not designed for reuse can hurt quality and safety. Starting from scratch may take more effort, but reuse is not always beneficial, so the choice depends on the case.
