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
from ..conftest import INPUT_FILE_PATH
from .conftest import compare_ast


@pytest.mark.parametrize(
    "path, expected",
    [
        param(
            Path("."),
            [
                INPUT_FILE_PATH / "toto_0.py",
                INPUT_FILE_PATH / "toto_1.py",
                INPUT_FILE_PATH / "toto2/toto3.py",
                INPUT_FILE_PATH / "toto4/toto5.py",
            ],
            id="folder in folder",
        ),
        param(
            "toto2",
            [INPUT_FILE_PATH / "toto2/toto3.py"],
            id="single folder",
        ),
    ],
)
def test_enumerate_file(path, expected, testing_files):
    assert_that(enumerate_file(testing_files / path)).contains_only(*expected)


def test_get_ignored_lines_with_ignored_lines(file_with_ignored, testing_files):
    assert_that(
        get_ignore_lines(file_with_ignored, testing_files / "toto2/toto3.py")
    ).contains_only(
        *[
            IgnoreLine(
                line_num=6,
                error_code="PPL001",
                from_file=testing_files / "toto2/toto3.py",
            )
        ]
    )


def test_get_ignored_lines_without_ignored_lines(file_without_ignored, testing_files):
    assert_that(
        get_ignore_lines(file_without_ignored, testing_files / "toto_1.py")
    ).is_equal_to([])


@pytest.mark.parametrize(
    "path_file, expected_ignored_lines",
    [
        param(
            "toto_0.py",
            [],
            id="0 print",
        ),
        param(
            "toto_1.py",
            [],
            id="1 print",
        ),
        param(
            "toto2/toto3.py",
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
def test_parse_file(testing_files, path_file, expected_ignored_lines):
    with open(testing_files / path_file, encoding="utf-8") as file:
        expected_tree = ast.parse(
            source=file.read(),
            filename=testing_files / path_file,
            feature_version=(3, 11),
        )

    tree, ignored_lines = parse_file(testing_files / path_file)

    with soft_assertions():
        assert compare_ast(tree, expected_tree)
        if not expected_ignored_lines:
            assert_that(ignored_lines).is_equal_to([])
        else:
            assert_that(ignored_lines).contains_only(*expected_ignored_lines)
