"""Main entrypoint for the file-whisperer CLI."""

from typing import Annotated

import typer
from rich.console import Console

app = typer.Typer(
    name="file-whisperer",
    help="""🤫 File-Whisperer: Your AI-powered file organization assistant.

Use it to scan messy folders, get intelligent organization recommendations,
and apply changes with full control and transparency.
""",
    add_completion=False,
    rich_markup_mode="rich",
    invoke_without_command=True,
)

console = Console()


@app.callback()
def callback(ctx: typer.Context) -> None:
    """Display help if no command is provided."""
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())


@app.command()
def scan(
    path: Annotated[
        str,
        typer.Argument(
            help="The path to the directory to scan.",
            show_default=False,
        ),
    ],
) -> None:
    """Scans a directory and collects metadata about the files within."""
    console.print(f"Scanning directory: {path}")


@app.command()
def organize() -> None:
    """Generates AI-powered organization recommendations."""
    console.print("Generating organization recommendations...")


@app.command()
def review() -> None:
    """Reviews the generated organization recommendations."""
    console.print("Reviewing organization recommendations...")


@app.command()
def apply() -> None:
    """Applies the approved organization recommendations."""
    console.print("Applying organization recommendations...")


@app.command()
def learn() -> None:
    """Updates the AI's understanding based on interaction history."""
    console.print("Updating AI understanding...")


@app.command()
def config() -> None:
    """Manages settings and preferences."""
    console.print("Managing settings and preferences...")


if __name__ == "__main__":
    app()
