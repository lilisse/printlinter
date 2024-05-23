"""App for typoer to interact with a user in command line."""

# Standard imports
from pathlib import Path

# Third party imports
import typer
from rich.console import Console
from rich.progress import track

# First party imports
from printlinter import Config
from printlinter import __app_name__ as ppl_app_name
from printlinter import __version__ as ppl_version
from printlinter import (
    contains_print,
    enumerate_file,
    get_not_ignored_issue,
    parse_file,
)

APP = typer.Typer(help="Print linter", rich_markup_mode="rich")


def _path_callback(path: Path) -> Path:
    """
    Check if the path exist and if it's a directory.

    Args:
        path: Path to check.

    Raises:
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If the given path is not a directory.

    Examples:
        >>> _path_callback(Path("printlinter"))
        PosixPath('printlinter')

        >>> try:
        ...     _path_callback(Path("azert.qwerty"))
        ... except(FileNotFoundError):
        ...     False
        False

        >>> try:
        ...     _path_callback(Path("README.md"))
        ... except(TypeError):
        ...     False
        False
    """
    if not path.exists():
        raise FileNotFoundError(f"The path: {path} does not exist")
    if not path.is_dir() and path.suffix != ".py":
        raise TypeError(f"The given file {path} must be a python file (.py)")
    return path


def _is_a_file(file_name: Path) -> Path | None:
    """
    Check if given path is a file.

    If the path is the default path (`Path(".")`) return None.

    Args:
        file_name: Path to check.

    Returns:
        The given path or None if given path is the default path (`Path(".")`).

    Examples:
        >>> _is_a_file(Path("."))
        None

        >>> _is_a_file(Path("README.md"))
        PosixPath('README.md')

        >>> try:
        ...     _is_a_file(Path("printlinter"))
        ... except FileNotFoundError:
        ...     False
        False
    """
    if file_name == Path("."):
        return None
    if file_name.is_dir() or not file_name.is_file():
        raise FileNotFoundError(f"The path: {file_name} is not a file")
    return file_name


def _is_ignored_rep(ignored_rep: list[Path], path: Path) -> bool:
    """
    Check if given path is in an ignored repository.

    Args:
        ignored_rep: All ignored repositories
        path: Path to check.

    Returns:
        True if path is in an ignored repository, False otherwise.
    """
    for rep in ignored_rep:
        if all(part in path.parts for part in rep.parts):
            return True

    return False


def version_callback(value: bool) -> None:
    """
    Get the version, display the version if `--version` was used.

    Args:
        value: Boolean to known if we display the version or not.
    """
    config = Config()
    console = Console(color_system="auto" if config.color else None)
    if value:
        console.print(f"{ppl_app_name} v.{ppl_version}")
        raise typer.Exit()


@APP.command(name="lint", help="lint the code to find print")
def lint(
    path: Path = typer.Argument(
        Path("."),
        help="Path to lint",
        show_default=False,
        callback=_path_callback,
    ),
    config_file: Path = typer.Option(
        Path("."),
        help="Configuration file",
        show_default=False,
        callback=_is_a_file,
    ),
) -> None:
    """
    Lint the given path or default path: `.`.

    Args:
        path: Path to lint.
        config_file: Optional config file.
    """
    warning = False
    config = Config(config_file)
    console = Console(color_system="auto" if config.color else None)

    if path.is_dir():
        files_path = enumerate_file(path)
    else:
        files_path = [path]

    all_ignored_lines = []
    all_ignored_files = []
    all_ignored_blocks = []
    issues = []
    for file_path in track(files_path, description="Processing..."):
        if (
            file_path.absolute()
            in [Path(path).absolute() for path in config.ignored_files]
        ) or _is_ignored_rep(config.ignored_rep, file_path):
            continue

        tree, ignored_lines, ignored_files, ignored_blocks = parse_file(
            file_path.as_posix(), config.target_version
        )
        issues = contains_print(file_path, tree)
        all_ignored_lines.extend(ignored_lines)

        if ignored_files is None:
            warning = True
            console.print(
                f"[bold][orange3]Warning ⚠️ [/orange3] {file_path}[/bold]: The ignore "
                "file comment must be before code and docstring, we skip this ignore "
                "comment. The file will be lint as if the file were not ignored."
            )
        else:
            all_ignored_files.extend(ignored_files)

        all_ignored_blocks.extend(ignored_blocks)

    not_ignored_issues = get_not_ignored_issue(
        issues,
        all_ignored_lines,
        all_ignored_files,
        all_ignored_blocks,
        config.disabled_rules,
    )

    # TODO: pass ignored value of issue at true when it is ignored. it's usful to get a
    # list of ignred issues.
    # console.print(f"[bold]ISSUES:\n{issues}\n[/bold]") # noqa: ERA001

    if warning:
        print()
    for issue in not_ignored_issues:
        console.print(str(issue))

    console.print(f"Found [bold red]{len(not_ignored_issues)}[/bold red] errors")


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
