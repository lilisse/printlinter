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


# TODO: Refactor attributes doc in class not in docstring
@dataclass
class IssueInfo:
    """
    Issue information class.

    Attributes:
        issue: Issue type.
        num_line: Line number of the issue.
        num_col: Column number of the issue
        line_as_str: String representation of the line.
        from_file: File who contain the line with the issue.
        ignore: If this issue is ignore or not.

    """

    issue: IssueEnum
    num_line: int
    num_col: int
    line_as_str: str | None
    from_file: Path | None
    ignore: bool

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


# TODO: Refactor attributes doc in class not in docstring
@dataclass
class IgnoreLine:
    """
    Ignore line class.

    Attributes:
        line_num: Line number.
        error_code: Code of the ignore issue.
        from_file: File who contains the ignored line.

    """

    line_num: int
    error_code: str
    from_file: Path | None


# TODO: Refactor attributes doc in class not in docstring
@dataclass
class IgnoreFile:
    """
    Ignore file class.

    Attributes:
        error_code: Code of the ignore issue.
        from_file: File who contains the ignored line.

    """

    error_code: str
    from_file: Path | None
