"""App for typoer to interact with a user in command line."""

# Standard imports
from pathlib import Path

# Third party imports
import typer
from rich.console import Console

# First party imports
from py_printlinter import __app_name__ as ppl_app_name
from py_printlinter import __version__ as ppl_version
from py_printlinter import (
    contains_print,
    enumerate_file,
    get_not_ignore_issue,
    parse_file,
)

APP = typer.Typer(help="Print linter", rich_markup_mode="rich")

CONSOLE = Console()


def version_callback(value: bool) -> None:
    """
    Get the version, display the version if `--version` was used.

    Args:
        value: Boolean to known if we display the version or not.
    """
    if value:
        CONSOLE.print(f"{ppl_app_name} v.{ppl_version}")
        raise typer.Exit()


def path_callback(path: Path) -> Path:
    """
    Check if the path exist and if it's a directory.

    Args:
        path: Path to check.

    Raises:
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If the given path is not a directory.

    Examples:
        >>> path_callback(Path("py_printlinter"))

        >>> try:
        ...     path_callback(Path("azert.qwerty"))
        ... except(FileNotFoundError):
        ...     False
        False

        >>> try:
        ...     path_callback(Path("README.md"))
        ... except(NotADirectoryError):
        ...     False
        False

        >>> try:
        ...     path_callback(Path("README.md"))
        ...     True
        ... except(NotADirectoryError, FileNotFoundError):
        ...     False
        False
    """
    if not path.exists():
        raise FileNotFoundError(f"The path: {path} does not exist")
    if not path.is_dir():
        raise NotADirectoryError(f"The given path: {path} is not a directory")
    return path


@APP.command(name="lint", help="lint the code to find print")
def lint(
    path: Path = typer.Argument(
        Path("."),
        help="Path to lint",
        show_default=False,
        callback=path_callback,
    ),
) -> None:
    """
    Lint the given path or default path: `.`.

    Args:
        path: Path to lint.
    """
    files_path = enumerate_file(path)
    all_ignored_lines = []
    all_ignored_files = []
    for file_path in files_path:
        tree, ignored_lines, ignored_files = parse_file(file_path.as_posix())
        issues = contains_print(file_path, tree)
        all_ignored_lines.extend(ignored_lines)
        all_ignored_files.extend(ignored_files)

    not_ignored_issues = get_not_ignore_issue(
        issues, all_ignored_lines, all_ignored_files
    )

    for issue in not_ignored_issues:
        CONSOLE.print(str(issue))

    CONSOLE.print(f"Found [bold red]{len(not_ignored_issues)}[/bold red] errors")


@APP.callback()
def main(
    _version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Display version of Py-printlinter.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """
    Display the version if we use the option --version or -v.

    Args:
        version: Boolean option to know if we want display the version or not.
            Default: False
    """
    return


if __name__ == "__main__":
    main()  # pragma: no cover
