# Pytest imports
import pytest
from pytest import param

# Standard imports
import ast
from pathlib import Path

# Third party imports
from assertpy import assert_that

# First party imports
from py_printlinter import IssueEnum, IssueInfo, contains_print

# Local imports
from ..conftest import INPUT_FILE_PATH


@pytest.mark.parametrize(
    "file_path, expected",
    [
        param("toto_0.py", [], id="0 print"),
        param(
            "toto_1.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=3,
                    num_col=0,
                    line_as_str='print("Hello, world")',
                    from_file=INPUT_FILE_PATH / "toto_1.py",
                    ignore=False,
                )
            ],
            id="1 print",
        ),
        param(
            "toto2/toto3.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=6,
                    num_col=4,
                    line_as_str='print("toto")  # noqa: PPL001',
                    from_file=INPUT_FILE_PATH / "toto2/toto3.py",
                    ignore=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=7,
                    num_col=4,
                    line_as_str='print("tata")',
                    from_file=INPUT_FILE_PATH / "toto2/toto3.py",
                    ignore=False,
                ),
            ],
            id="2 print",
        ),
    ],
)
def test_contains_print(pnv_soft_reset, testing_files, file_path, expected):
    with open(testing_files / file_path, encoding="utf-8") as file:
        tree = ast.parse(
            source=file.read(),
            filename=testing_files / file_path,
            feature_version=(3, 11),
        )

    print_detected = contains_print(testing_files / file_path, tree)

    if not expected:
        assert_that(print_detected).is_equal_to(expected)
    else:
        assert_that(print_detected).contains_only(*expected)
