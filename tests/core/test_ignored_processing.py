# Third party imports
from assertpy import assert_that

# First party imports
from py_printlinter import IssueEnum, IssueInfo, get_not_ignore_issue

# Local imports
from .conftest import ignored_lines, issues


def test_get_not_ignore_issue():
    not_ignored_line = get_not_ignore_issue(issues(), ignored_lines())

    expected = [
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=0,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=1,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=5,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=8,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=9,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=10,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=11,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=13,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=14,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto.py",
            ignore=False,
        ),
    ]

    assert_that(not_ignored_line).is_equal_to(expected)
