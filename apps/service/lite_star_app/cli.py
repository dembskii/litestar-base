"""Console entrypoint for the service."""

import sys

from uvicorn.main import main as uvicorn_main


def main() -> None:
    """Start the service, forwarding command-line options to Uvicorn."""
    uvicorn_main(
        args=["lite_star_app.app:app", *sys.argv[1:]], prog_name="lite-star-app"
    )
