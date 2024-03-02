# Pytest imports
import pytest
from pytest import param

# Third party imports
from assertpy import assert_that, soft_assertions

# First party imports
from py_printlinter import IgnoreLine, IssueEnum, IssueInfo


@pytest.mark.parametrize(
    "enum_elem, err_code, name",
    [
        param(
            IssueEnum.PRINTDETECT,
            "PPL001",
            "print-detected",
            id="print detected error n°1",
        ),
        param(
            IssueEnum.PRETTYPRINTDETECT,
            "PPL002",
            "prettyprint-detected",
            id="prettyprint detected error n°2",
        ),
        param(
            IssueEnum.SYSSTDOUTWRITEDETECT,
            "PPL003",
            "sys.stdout.write-detected",
            id="sys.stdout.write detected error n°3",
        ),
        param(
            IssueEnum.SYSSTDERRWRITEDETECT,
            "PPL004",
            "sys.stderr.write-detected",
            id="sys.stderr.write detected error n°4",
        ),
        param(
            IssueEnum.SYSSTDOUTWRITELINESDETECT,
            "PPL005",
            "sys.stdout.writelines-detected",
            id="sys.stdout.writelines detected error n°5",
        ),
        param(
            IssueEnum.SYSSTDERRWRITELINESDETECT,
            "PPL006",
            "sys.stderr.writelines-detected",
            id="sys.stderr.writelines detected error n°6",
        ),
    ],
)
def test_issue_enum(enum_elem, err_code, name):
    assert_that(enum_elem.err_code).is_equal_to(err_code)
    assert_that(enum_elem.name).is_equal_to(name)


@pytest.mark.parametrize(
    "line, column",
    [
        param(1, 2, id="line and column"),
    ],
)
@pytest.mark.parametrize(
    "str_line",
    [
        param("print('toto')", id="with str_line"),
        param(None, id="without str_line"),
    ],
)
@pytest.mark.parametrize(
    "file",
    [
        param("toto.py", id="with file"),
        param(None, id="without file"),
    ],
)
@pytest.mark.parametrize(
    "ignored",
    [
        param(True, id="ignored"),
        param(False, id="not ignored"),
    ],
)
@pytest.mark.parametrize(
    "issue_type",
    [
        param(IssueEnum.PRINTDETECT, id="print"),
        param(IssueEnum.PRETTYPRINTDETECT, id="pretty print"),
        param(IssueEnum.SYSSTDOUTWRITEDETECT, id="sys.stdout.write"),
        param(IssueEnum.SYSSTDERRWRITEDETECT, id="sys.stderr.write"),
        param(IssueEnum.SYSSTDOUTWRITELINESDETECT, id="sys.stdout.writelines"),
        param(IssueEnum.SYSSTDERRWRITELINESDETECT, id="sys.stderr.writelines"),
    ],
)
def test_issue_info_class(line, column, str_line, file, ignored, issue_type):
    issue = IssueInfo(
        issue=issue_type,
        num_line=line,
        num_col=column,
        line_as_str=str_line,
        from_file=file,
        ignore=ignored,
    )
    with soft_assertions():
        assert issue
        assert_that(str(issue)).is_equal_to(
            f"[bold]{file}[/bold]:{line}:{column}: "
            f"[bold red]{issue_type.value.err_code}[/bold red] [bold]`[/bold]{str_line}"
            f"[bold]`[/bold] {issue_type.value.name}"
        )


@pytest.mark.parametrize(
    "file",
    [
        param("toto.py", id="with file"),
        param(None, id="without file"),
    ],
)
@pytest.mark.parametrize(
    "err_code",
    [
        param("PPL001", id="print PPL001"),
        param("PPL002", id="pprint PPL002"),
        param("PPL003", id="sys.stdout.write PPL003"),
        param("PPL004", id="sys.stderr.write PPL004"),
        param("PPL005", id="sys.stdout.writelines PPL005"),
        param("PPL006", id="sys.stderr.writelines PPL006"),
    ],
)
def test_ignore_line_class(file, err_code):
    assert IgnoreLine(1, err_code, file)
