# Litestar service

With `uv` installed, start the service from the repository root:

```bash
uv run lite-star-app
```

Enable automatic reload during development:

```bash
uv run lite-star-app --reload
```

Additional Uvicorn options are forwarded, for example:

```bash
uv run lite-star-app --host 0.0.0.0 --port 8080
```

The default address is http://127.0.0.1:8000. `uv` installs the service dependencies on first run.

For development in VS Code, open the repository with **Dev Containers: Reopen in Container**.
The container installs dependencies automatically; run `uv run lite-star-app --reload`
in its terminal. The container sets `UVICORN_HOST=0.0.0.0`, and VS Code forwards
container port 8000. Docker does not publish a host port.

After starting the app, open VS Code's **Ports** panel and use the **Forwarded
Address** for port 8000. If local port 8000 is available, you can verify access
from a terminal on the machine running the VS Code client:

```bash
curl http://127.0.0.1:8000/
# {"message":"Hello, world!"}
```

If VS Code assigns a different local port, use that port in the URL. With a
Windows VS Code client and WSL, the forwarded address belongs to the client;
test it in Windows or use **Open in Browser** in the Ports panel.

The container keeps its Python environment at `/home/vscode/.venvs/litestar-base`
to keep it separate from the host's root `.venv`. After changing the devcontainer
configuration, use **Dev Containers: Rebuild Container** to apply it.

Install development tools and run checks from the repository root:

```bash
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run mypy
```

To apply formatting, run `uv run ruff format .`. Ruff checks imports and common
Python issues; mypy checks the service with strict typing enabled. Both are
configured in `pyproject.toml`. The devcontainer enables Ruff formatting on save
and the mypy VS Code extension after a rebuild.

GitHub Actions runs on pushes and pull requests, in this order:

1. Gitlint checks commit messages in the pushed or pull request commit range
   using `.gitlint`. For a new branch, it checks the branch history.
2. Separate Lint and TypeCheck jobs run in parallel: Lint checks Ruff linting
   and formatting; TypeCheck runs strict mypy typing.
3. Tests run with pytest after both jobs pass, including an HTTP check of the
   root endpoint and coverage reports.

Run the same checks locally:

```bash
uv run gitlint
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
```

Gitlint checks the latest commit locally; use `uv run gitlint --commits main..HEAD`
to check a branch's commits. Commit titles require a type, a capitalized
description ending in a period, then a blank line and a nonempty body:

```text
feat: Update something.

Booooody
```

Allowed types are `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`,
`build`, `ci`, `chore`, and `revert`. Optional scopes and breaking-change markers
are supported, for example `fix(api): Handle missing input.` or
`feat!: Update the response format.` Titles remain limited to 72 characters
and body lines to 80 characters.

`uv run pytest` also measures line and branch coverage for the whole service,
prints missing lines, and generates `coverage.xml` and `htmlcov/index.html`.
CI uploads both reports as the `coverage` artifact, retained for 14 days,
including when tests fail. No minimum coverage percentage is enforced.
