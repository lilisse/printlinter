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

    ignored: bool
    "If this issue is ignored or not."

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
class IgnoredLine:
    """Ignored line class."""

    line_num: int
    "Line number of the ignored line."

    error_code: str
    "Code of the ignored issue."

    from_file: Path | None
    "File who contains the ignored line."


@dataclass
class IgnoredFile:
    """Ignored file class."""

    error_code: str
    "Code of the ignored issue."

    from_file: Path | None
    "File who contains the ignored line."


@dataclass
class IgnoredBlock:
    """Ignored block of code class."""

    error_code: str
    "Code of the ignored issue."

    line_from: int
    "Begin of ignored block."

    line_to: int
    "End of ignored block."

    from_file: Path | None
    "File who contains the ignored line."

    def __init__(
        self,
        error_code: str,
        line_from: int,
        line_to: int,
        from_file: Path | None,
    ) -> None:
        """
        Initialize an IngoredBlock class.

        Args:
            error_code: Given error code.
            line_from: Given line from.
            line_to: Given line to.
            from_file: Given from file.

        Raise:
            ValueError: If `g_line_from` <= `g_line_to`.
        """
        if line_to <= line_from:
            raise ValueError(
                f"Given line to ({line_to}) must be strictly greater then given line "
                f"from ({line_from})"
            )

        self.error_code = error_code
        self.line_from = line_from
        self.line_to = line_to
        self.from_file = from_file
