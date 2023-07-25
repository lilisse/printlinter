# Pytest imports
import pytest
from pytest import param

# Standard imports
import ast
from pathlib import Path

# Third party imports
from assertpy import assert_that, soft_assertions

# First party imports
from py_printlinter import IgnoreLine, enumerate_file, get_ignore_lines, parse_file

# Local imports
from .conftest import compare_ast

TEST_PATH = Path(__file__).parent.parent
INPUT_FILE_PATH = TEST_PATH / "input_files"


@pytest.mark.parametrize(
    "path, expected",
    [
        param(
            INPUT_FILE_PATH,
            [
                INPUT_FILE_PATH / "toto_0.py",
                INPUT_FILE_PATH / "toto_1.py",
                INPUT_FILE_PATH / "toto2/toto3.py",
                INPUT_FILE_PATH / "toto4/toto5.py",
            ],
            id="folder in folder",
        ),
        param(
            INPUT_FILE_PATH / "toto2",
            [INPUT_FILE_PATH / "toto2/toto3.py"],
            id="single folder",
        ),
    ],
)
def test_enumerate_file(path, expected):
    assert_that(enumerate_file(path)).contains_only(*expected)


def test_get_ignored_lines_with_ignored_lines(file_with_ignored):
    assert_that(
        get_ignore_lines(file_with_ignored, INPUT_FILE_PATH / "toto2/toto3.py")
    ).contains_only(
        *[
            IgnoreLine(
                line_num=6,
                error_code="PPL001",
                from_file=INPUT_FILE_PATH / "toto2/toto3.py",
            )
        ]
    )


def test_get_ignored_lines_without_ignored_lines(file_without_ignored):
    assert_that(
        get_ignore_lines(file_without_ignored, INPUT_FILE_PATH / "toto_1.py")
    ).is_equal_to([])


@pytest.mark.parametrize(
    "path_file, expected_ignored_lines",
    [
        param(
            INPUT_FILE_PATH / "toto_0.py",
            [],
            id="0 print",
        ),
        param(
            INPUT_FILE_PATH / "toto_1.py",
            [],
            id="1 print",
        ),
        param(
            INPUT_FILE_PATH / "toto2/toto3.py",
            [
                IgnoreLine(
                    line_num=6,
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "toto2/toto3.py",
                )
            ],
            id="1 print, 1 ignored print",
        ),
    ],
)
def test_parse_file(path_file, expected_ignored_lines):
    with open(path_file, encoding="utf-8") as file:
        expected_tree = ast.parse(
            source=file.read(),
            filename=path_file,
            feature_version=(3, 11),
        )

    tree, ignored_lines = parse_file(path_file)

    with soft_assertions():
        assert compare_ast(tree, expected_tree)
        if not expected_ignored_lines:
            assert_that(ignored_lines).is_equal_to([])
        else:
            assert_that(ignored_lines).contains_only(*expected_ignored_lines)
