"""Issues classes used in the project."""

# Standard imports
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

Issue = namedtuple("Issue", ["err_code", "name"])


class IssueEnum(Issue, Enum):
    """Issue Enumerable to store issues."""

    PRINTDETECT = Issue(err_code="PPL001", name="print-detected")
    PRETTYPRINTDETECT = Issue(err_code="PPL002", name="prettyprint-detected")
    SYSSTDOUTWRITEDETECT = Issue(err_code="PPL003", name="sys.stdout.write-detected")
    SYSSTDERRWRITEDETECT = Issue(err_code="PPL004", name="sys.stderr.write-detected")
    SYSSTDOUTWRITELINESDETECT = Issue(
        err_code="PPL005", name="sys.stdout.writelines-detected"
    )
    SYSSTDERRWRITELINESDETECT = Issue(
        err_code="PPL006", name="sys.stderr.writelines-detected"
    )


@dataclass
class IssueInfo:
    """Issue information class."""

    issue: IssueEnum
    "Issue type."

    num_line: int
    "Line number of the issue."

    num_col: int
    "Column number of the issue."

    line_as_str: str | None
    "String representation of the line."

    from_file: Path | None
    "File who contain the line with the issue."

    ignore: bool
    "If this issue is ignore or not."

    def __str__(self) -> str:
        """
        Get issue as string.

        Returns:
            The string representation of the issue.
        """
        return (
            f"[bold]{self.from_file}[/bold]:{self.num_line}:{self.num_col}: "
            f"[bold red]{self.issue.err_code}[/bold red] [bold]`[/bold]"
            f"{self.line_as_str}[bold]`[/bold] {self.issue.name}"
        )


@dataclass
class IgnoreLine:
    """Ignore line class."""

    line_num: int
    "Line number of the ignored line."

    error_code: str
    "Code of the ignore issue."

    from_file: Path | None
    "File who contains the ignored line."


@dataclass
class IgnoreFile:
    """Ignore file class."""

    error_code: str
    "Code of the ignore issue."

    from_file: Path | None
    "File who contains the ignored line."
