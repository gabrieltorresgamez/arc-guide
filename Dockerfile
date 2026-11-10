# Builder for the static site (see compose.yml): builds site/dist from content/ using the Kroki service.
FROM node:22-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
# dependencies first (cached layers)
# the site build only needs pyyaml, so no project sync
RUN uv run --no-project --with pyyaml python -c "import yaml"
COPY site/package.json site/package-lock.json site/
RUN cd site && npm ci --no-audit --no-fund
# sources
COPY . .
