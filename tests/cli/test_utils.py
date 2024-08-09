# Pytest imports
import pytest
from pytest import param

# Standard imports
from pathlib import Path

# Third party imports
from assertpy import assert_that, soft_assertions
from rich.console import Console

# First party imports
from cli_app.cli import (
    _display_issues,
    _get_errors_msg_by_file,
    _get_issues_depending_sorted_config,
    _is_a_file,
    _is_ignored_rep,
)
from printlinter import IssueEnum, IssueInfo, OutputLevel, SortedOutput

# Local imports
from ..conftest import INPUT_FILE_PATH, remove_backslash_n

TESTING_FILES_PATH = INPUT_FILE_PATH / "print"

ISSUES = [
    IssueInfo(
        IssueEnum.PRINTDETECT,
        num_line=5,
        num_col=0,
        line_as_str="print('toto')",
        from_file=Path("toto.py"),
        ignored=False,
    ),
    IssueInfo(
        IssueEnum.PRINTDETECT,
        num_line=5,
        num_col=0,
        line_as_str="print('titi')",
        from_file=Path("titi.py"),
        ignored=False,
    ),
    IssueInfo(
        IssueEnum.PRETTYPRINTDETECT,
        num_line=9,
        num_col=0,
        line_as_str="pprint('toto3')",
        from_file=Path("toto.py"),
        ignored=False,
    ),
    IssueInfo(
        IssueEnum.PRINTDETECT,
        num_line=7,
        num_col=0,
        line_as_str="print('toto2')",
        from_file=Path("toto.py"),
        ignored=False,
    ),
]


@pytest.mark.parametrize(
    "path, expected",
    [
        param(
            TESTING_FILES_PATH / "toto_0.py",
            TESTING_FILES_PATH / "toto_0.py",
            id="simple file",
        ),
        param(
            Path("."),
            None,
            id='default, "."',
        ),
    ],
)
def test_is_a_file_success(path, expected):
    assert _is_a_file(path) == expected


@pytest.mark.parametrize(
    "path",
    [
        param(TESTING_FILES_PATH / "toto", id="Given path not exist"),
        param(TESTING_FILES_PATH, id="Given path is a directory"),
    ],
)
def test_is_a_file_fail(path):
    with pytest.raises(FileNotFoundError):
        _is_a_file(path)


@pytest.mark.parametrize(
    "path, expected",
    [
        param(
            Path("a/d.py"),
            True,
            id="ignored in first folder",
        ),
        param(
            Path("a/b/d.py"),
            True,
            id="ignored in second folder",
        ),
        param(
            Path("a/b/c/d.py"),
            True,
            id="ignored in third folder",
        ),
        param(
            Path("toto.py"),
            False,
            id="Not ignored file in cwd",
        ),
        param(
            Path("z/toto.py"),
            False,
            id="Not ignored file in a fodler",
        ),
    ],
)
def test_is_ignored_rep(path, expected):
    assert (
        _is_ignored_rep(
            [
                Path("a"),
                Path("a/b"),
                Path("a/b/c/"),
            ],
            path,
        )
        == expected
    )


@pytest.mark.parametrize(
    "with_number_and_lines, expected",
    [
        param(
            True,
            [
                "[bold]toto.py[/bold]",
                "3 errors detected",
                "[bold red]PPL002[/bold red]",
                "[bold red]PPL001[/bold red]",
                "at lines",
                "[bold]titi.py[/bold] - 1 errors detected ([bold red]PPL001[/bold red]"
                ") at lines 5",
            ],
            id="With number and lines",
        ),
        param(
            False,
            [
                "[bold]toto.py[/bold] - 3 errors detected",
                "[bold]titi.py[/bold] - 1 errors detected",
            ],
            id="Without number and lines",
        ),
    ],
)
def test_get_errors_msg_by_file(with_number_and_lines, expected):
    with soft_assertions():
        for exp in expected:
            assert_that(
                _get_errors_msg_by_file(ISSUES, with_number_and_lines)
            ).contains(exp)


@pytest.mark.parametrize(
    "output_level, expected",
    [
        param(
            OutputLevel.DEFAULT,
            [
                "toto.py",
                "titi.py",
                "PPL001",
                "PPL002",
                "print('toto')",
                "print('toto2')",
                "pprint('toto3')",
                "print('titi')",
            ],
            id="output level = DEFAULT",
        ),
        param(OutputLevel.L1, "", id="output level = 1"),
        param(
            OutputLevel.L2,
            ["titi.py - 1 errors detected", "toto.py - 3 errors detected"],
            id="output level = 2",
        ),
        param(
            OutputLevel.L3,
            [
                "titi.py - 1 errors detected",
                "toto.py - 3 errors detected",
                "at lines",
            ],
            id="output level = 3",
        ),
    ],
)
def test_display_issues(output_level, expected, capsys):
    console = Console()

    _display_issues(ISSUES, output_level, console)

    captured_out = capsys.readouterr().out
    with soft_assertions():
        if output_level == OutputLevel.L1:
            assert_that(captured_out).is_equal_to(expected)
        else:
            for exp in expected:
                assert_that(remove_backslash_n(captured_out)).contains(exp)


@pytest.mark.parametrize(
    "sorted_output, expected",
    [
        param(SortedOutput.DEFAULT, ISSUES, id="Default sorted output"),
        param(
            SortedOutput.BY_FILES,
            [
                IssueInfo(
                    IssueEnum.PRINTDETECT,
                    num_line=5,
                    num_col=0,
                    line_as_str="print('titi')",
                    from_file=Path("titi.py"),
                    ignored=False,
                ),
                IssueInfo(
                    IssueEnum.PRINTDETECT,
                    num_line=5,
                    num_col=0,
                    line_as_str="print('toto')",
                    from_file=Path("toto.py"),
                    ignored=False,
                ),
                IssueInfo(
                    IssueEnum.PRETTYPRINTDETECT,
                    num_line=9,
                    num_col=0,
                    line_as_str="pprint('toto3')",
                    from_file=Path("toto.py"),
                    ignored=False,
                ),
                IssueInfo(
                    IssueEnum.PRINTDETECT,
                    num_line=7,
                    num_col=0,
                    line_as_str="print('toto2')",
                    from_file=Path("toto.py"),
                    ignored=False,
                ),
            ],
            id="files sorted output",
        ),
        param(
            SortedOutput.BY_ERRORS,
            [
                IssueInfo(
                    IssueEnum.PRINTDETECT,
                    num_line=5,
                    num_col=0,
                    line_as_str="print('toto')",
                    from_file=Path("toto.py"),
                    ignored=False,
                ),
                IssueInfo(
                    IssueEnum.PRINTDETECT,
                    num_line=5,
                    num_col=0,
                    line_as_str="print('titi')",
                    from_file=Path("titi.py"),
                    ignored=False,
                ),
                IssueInfo(
                    IssueEnum.PRINTDETECT,
                    num_line=7,
                    num_col=0,
                    line_as_str="print('toto2')",
                    from_file=Path("toto.py"),
                    ignored=False,
                ),
                IssueInfo(
                    IssueEnum.PRETTYPRINTDETECT,
                    num_line=9,
                    num_col=0,
                    line_as_str="pprint('toto3')",
                    from_file=Path("toto.py"),
                    ignored=False,
                ),
            ],
            id="errors sorted output",
        ),
    ],
)
def test_get_issues_depending_sorted_config(sorted_output, expected):
    assert _get_issues_depending_sorted_config(ISSUES, sorted_output) == expected
