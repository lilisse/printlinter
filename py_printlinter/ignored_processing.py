"""Processing ingoed lines functions."""

# Local imports
from .classes import IgnoreLine, IssueInfo


def get_not_ignore_issue(
    issues: list[IssueInfo],
    ignore_lines: list[IgnoreLine],
) -> list[IssueInfo]:
    """
    Get all not ignored issues.

    Args:
        issues: All issue found.
        ignore_lines: All ignored lines.

    Returns:
        All lines are not ignored.
    """
    result = []

    for issue in issues:
        ignore_equivalence = IgnoreLine(
            issue.num_line,
            error_code=issue.issue.err_code,
            from_file=issue.from_file,
        )
        if ignore_equivalence not in ignore_lines:
            result.append(issue)

    return result
