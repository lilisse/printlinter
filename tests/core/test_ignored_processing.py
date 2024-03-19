# First party imports
from py_printlinter import IssueEnum, IssueInfo, get_not_ignore_issue

# Local imports
# TODO: pass those function in fixture
from .conftest import (
    ignored_files,
    ignored_files_and_lines,
    ignored_lines,
    issues_for_files,
    issues_for_files_and_lines,
    issues_for_lines,
)


def test_get_not_ignore_issue__ignore_lines():
    not_ignored_line = get_not_ignore_issue(issues_for_lines(), ignored_lines(), [])

    expected = [
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=0,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto1.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=1,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto1.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto1.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=5,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto1.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=8,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto1.py",
            ignore=False,
        ),
        # pprint
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=9,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto2.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=10,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto2.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=11,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto2.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=13,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto2.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=14,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto2.py",
            ignore=False,
        ),
        # sys.stdout.write
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=16,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=18,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=19,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=22,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        # sys.stderr.write
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=25,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=26,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=28,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=30,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        # sys.stdout.writelines
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=31,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=32,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=35,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto5.py",
            ignore=False,
        ),
        # sys.stderr.writelines
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=38,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto6.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=39,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto6.py",
            ignore=False,
        ),
    ]

    assert not_ignored_line == expected


def test_get_not_ignore_issue__ignore_files():
    not_ignored_line = get_not_ignore_issue(issues_for_files(), [], ignored_files())

    expected = [
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=3,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto5.py",
            ignore=False,
        ),
    ]

    assert not_ignored_line == expected


def test_get_not_ignore_issue__ignore_files_and_lines():
    ignored_lines, ignored_files = ignored_files_and_lines()
    not_ignored_line = get_not_ignore_issue(
        issues_for_files_and_lines(), ignored_lines, ignored_files
    )

    expected = [
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=1,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=1,
            num_col=12,
            line_as_str="print('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=2,
            num_col=12,
            line_as_str="pprint('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=3,
            num_col=12,
            line_as_str="sys.stdout.write('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=4,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=4,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=4,
            num_col=12,
            line_as_str="sys.stderr.write('toto')",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=5,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=5,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto4.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=5,
            num_col=12,
            line_as_str="sys.stdout.writelines(['toto', 'titi'])",
            from_file="toto5.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=6,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto3.py",
            ignore=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=6,
            num_col=12,
            line_as_str="sys.stderr.writelines(['toto', 'titi'])",
            from_file="toto5.py",
            ignore=False,
        ),
    ]

    assert not_ignored_line == expected
