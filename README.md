# Software Architecture Guide

A searchable knowledge base about software architecture, written for non-architects: https://arc.fuet.ch

- concept articles, organized by topic, each with its public sources,
- beginner guides: how to start the architecture of a project, what must exist first, what to do if it is missing,
- llms.txt v2 files and a Markdown version of every page, so LLMs can use the site,
- an arc42 review checklist: give an LLM one link and your arc42 document, get a review.

**How it was made:** LLM agents researched each topic on the public web. Code checked every quoted piece of evidence
against the real page before it could be used, and an LLM claim check compared each article with its sources.
The articles are machine-generated and not reviewed by a person.

## Build

1. `docker compose up -d` starts a local [Kroki](https://github.com/yuzutech/kroki) for the diagrams.
2. `uv run python -m pipeline.build` builds the site into `site/dist/` and runs the checks.
3. `cd site && npm run dev` for a local preview.

Self-hosting: set `SITE_URL` in `compose.yml`, then `docker compose --profile site up -d --build`; nginx serves the
site on port 8080. Re-run after changing `content/`.
