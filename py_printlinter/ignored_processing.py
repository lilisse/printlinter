"""Processing ingoed lines functions."""

# Local imports
from .classes import IgnoreFile, IgnoreLine, IssueInfo

FAMILIRY_ERR_CODE = [
    "PPL000",
    "PPL100",
    "PPL200",
    "PPL300",
    "PPL400",
    "PPL500",
    "PPL600",
    "PPL700",
    "PPL800",
    "PPL900",
]


def get_not_ignore_issue(
    issues: list[IssueInfo],
    ignore_lines: list[IgnoreLine],
    ignore_files: list[IgnoreFile],
) -> list[IssueInfo]:
    """
    Get all not ignored issues.

    Args:
        issues: All issue found.
        ignore_lines: All ignored lines.
        ignore_files: All ignored files.

    Returns:
        All lines are not ignored.
    """
    result = []

    for issue in issues:
        ignore_all_file_equivalence = IgnoreFile(
            error_code="ALL",
            from_file=issue.from_file,
        )
        if ignore_all_file_equivalence in ignore_files:
            continue

        # Ignore a file with a family of code (like PPL000, PPL100, ...)
        for index in range(len(FAMILIRY_ERR_CODE) - 1):
            err_code_min = FAMILIRY_ERR_CODE[index]
            err_code_max = FAMILIRY_ERR_CODE[index + 1]
            if err_code_min < issue.issue.err_code < err_code_max:
                ignored_err_code = err_code_min

        ignore_family_file_equivalence = IgnoreFile(
            error_code=ignored_err_code,
            from_file=issue.from_file,
        )
        if ignore_family_file_equivalence in ignore_files:
            continue

        # Files with specific code (like PPL001, PPL005, ...)
        ignore_file_equivalence = IgnoreFile(
            error_code=issue.issue.err_code,
            from_file=issue.from_file,
        )
        if ignore_file_equivalence in ignore_files:
            continue

        # Ignored lines
        ignore_line_equivalence = IgnoreLine(
            issue.num_line,
            error_code=issue.issue.err_code,
            from_file=issue.from_file,
        )
        if ignore_line_equivalence in ignore_lines:
            continue

        result.append(issue)

    return result
