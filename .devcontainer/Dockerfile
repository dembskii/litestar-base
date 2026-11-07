FROM ghcr.io/astral-sh/uv:latest AS uv

FROM mcr.microsoft.com/devcontainers/base:bookworm

COPY --from=uv /uv /uvx /usr/local/bin/

ENV UV_PYTHON=3.12 \
    UV_PYTHON_PREFERENCE=only-managed \
    UV_PYTHON_INSTALL_DIR=/home/vscode/.local/share/uv/python
ENV PATH="/home/vscode/.local/bin:${PATH}"

USER vscode

RUN uv python install --default 3.12
