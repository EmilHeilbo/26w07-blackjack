FROM ghcr.io/astral-sh/uv:python3.14-alpine

WORKDIR /app
# Install dependencies, copy minimum required files for `uv sync` to work
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --extra web --no-dev --no-install-project

# Copy the rest over and build
COPY . .
RUN uv build

EXPOSE 8000
ENTRYPOINT [ "uv", "run", "fastapi", "run", "/app/src/blackjack/api.py" ]
