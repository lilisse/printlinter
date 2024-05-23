"""Processing ingoed lines functions."""

# Local imports
from .classes import IgnoredBlock, IgnoredFile, IgnoredLine, IssueInfo

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


def get_not_ignored_issue(
    issues: list[IssueInfo],
    ignored_lines: list[IgnoredLine],
    ignored_files: list[IgnoredFile],
    ignored_blocks: list[IgnoredBlock],
    disabled_rules: list[str],
) -> list[IssueInfo]:
    """
    Get all not ignored issues.

    Args:
        issues: All issue found.
        ignored_lines: All ignored lines.
        ignored_files: All ignored files.
        ignored_blocks: All ignored blocks of code.
        disabled_rules: All disabled rules.

    Returns:
        All lines are not ignored.
    """
    result = []

    for issue in issues:
        if issue.issue.err_code in disabled_rules:
            continue

        ignored_all_file_equivalence = IgnoredFile(
            error_code="ALL",
            from_file=issue.from_file,
        )
        if ignored_all_file_equivalence in ignored_files:
            continue

        # Ignore a file with a family of code (like PPL000, PPL100, ...)
        for index in range(len(FAMILIRY_ERR_CODE) - 1):
            err_code_min = FAMILIRY_ERR_CODE[index]
            err_code_max = FAMILIRY_ERR_CODE[index + 1]
            if err_code_min < issue.issue.err_code < err_code_max:
                ignored_err_code = err_code_min

        ignored_family_file_equivalence = IgnoredFile(
            error_code=ignored_err_code,
            from_file=issue.from_file,
        )
        if ignored_family_file_equivalence in ignored_files:
            continue

        # Files with specific code (like PPL001, PPL005, ...)
        ignored_file_equivalence = IgnoredFile(
            error_code=issue.issue.err_code,
            from_file=issue.from_file,
        )
        if ignored_file_equivalence in ignored_files:
            continue

        # Ignored lines
        ignored_line_equivalence = IgnoredLine(
            issue.num_line,
            error_code=issue.issue.err_code,
            from_file=issue.from_file,
        )
        if ignored_line_equivalence in ignored_lines:
            continue

        # Ignored blocks
        # TODO: ignore a librairy rules for a block of code
        issue_in_ignored_block = False
        for ignored_block in ignored_blocks:
            if (
                ignored_block.from_file == issue.from_file
                and ignored_block.line_from <= issue.num_line <= ignored_block.line_to
                and (
                    ignored_block.error_code == "ALL"
                    or ignored_block.error_code == issue.issue.err_code
                )
            ):
                issue_in_ignored_block = True
                continue

        if issue_in_ignored_block:
            continue

        result.append(issue)

    return result
