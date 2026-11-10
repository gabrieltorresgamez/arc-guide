---
title: Code Smell
slug: code-smell
category: evaluation
kind: concept
summary: A code smell is a surface sign in code that often points to a deeper design problem. Smells such
  as long methods or large classes show where refactoring may be needed.
arc42:
- 11
step: s12-evolve
related:
- refactoring
- technical-debt
- coupling-and-cohesion
- architecture-decay
- maintainability
- big-ball-of-mud
- software-architecture-evaluation
- high-cohesion
checks:
- The documentation names how code smells are detected, for example through static analysis tools that
  report complexity metrics.
- Known smells such as overly long methods or large classes are tracked, with refactoring planned for
  them.
- Internal-quality problems found through smells are recorded as technical debt.
sources:
- url: https://martinfowler.com/bliki/CodeSmell.html
  title: Code Smell
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://refactoring.guru/smells/long-method
  title: Long Method
  site: refactoring.guru
  accessed: '2026-11-09'
- url: https://refactoring.guru/smells/large-class
  title: Large Class
  site: refactoring.guru
  accessed: '2026-11-09'
- url: https://refactoring.guru/smells/feature-envy
  title: Feature Envy
  site: refactoring.guru
  accessed: '2026-11-09'
- url: https://refactoring.guru/smells/middle-man
  title: Middle Man
  site: refactoring.guru
  accessed: '2026-11-09'
- url: https://refactoring.guru/refactoring/smells
  title: Code Smells
  site: refactoring.guru
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Cyclomatic_complexity
  title: Cyclomatic complexity - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition
  title: Understanding measures and metrics | SonarQube Server | Sonar Documentation
  site: docs.sonarsource.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/TechnicalDebt.html
  title: Technical Debt
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A code smell is a visible hint in the code. It usually points to a deeper design problem in the system. The smell itself is not necessarily a bug. It tells you where to look closer.

Kent Beck coined the term while helping write the book on refactoring. That ties smells to refactoring: a smell shows where a cleanup may be worth considering (see the article Refactoring).

**Common smells**

- **Long Method:** a method with too many lines of code. Around ten lines is where you start asking questions.
- **Large Class:** a class that has collected many fields, methods or lines of code.
- Long Method and Large Class belong to a group called Bloaters. These are pieces of code that have grown too big to work with.
- **Feature Envy:** a method uses another object's data more than its own. It is listed among the Couplers, smells that contribute to excessive coupling between classes. See the article Coupling and Cohesion.
- **Middle Man:** a class left as an empty shell that only passes work on to others.

**Code metrics**

Cyclomatic complexity is a software metric. It counts the linearly independent paths through source code. McCabe developed it in 1976.

SonarQube, for example, reports cyclomatic complexity and cognitive complexity. Cognitive complexity rates how hard the control flow is to understand. SonarQube also has a metric for the number of code smells.

## Example

A team's order-processing class has grown very large. One method in it runs far past ten lines. Another method mostly reads the customer object's data instead of its own. A static analysis tool reports a high complexity value for the long method. The team treats these as smells and plans small refactoring steps.

## Trade-offs

A smell is only a hint. Not every flagged method is a real problem, and a metric value alone does not prove bad design. The ten-line figure is a point to start asking questions, not a hard rule. Treat tool reports as a prompt for review.
