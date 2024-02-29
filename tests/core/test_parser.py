# Pytest imports
import pytest
from pytest import param

# Standard imports
import ast

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
            "print",
            [
                INPUT_FILE_PATH / "print/toto_0.py",
                INPUT_FILE_PATH / "print/toto_1.py",
                INPUT_FILE_PATH / "print/toto2/toto3.py",
                INPUT_FILE_PATH / "print/toto4/toto5.py",
            ],
            id="folder in folder",
        ),
        param(
            "print/toto2",
            [INPUT_FILE_PATH / "print/toto2/toto3.py"],
            id="single folder",
        ),
    ],
)
def test_enumerate_file(path, expected, testing_files):
    assert_that(enumerate_file(testing_files / path)).contains_only(*expected)


def test_get_ignored_lines_with_ignored_lines__print(
    file_with_ignored_print,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_print,
            testing_files / "print/toto2/toto3.py",
        )
    ).contains_only(
        *[
            IgnoreLine(
                line_num=6,
                error_code="PPL001",
                from_file=testing_files / "print/toto2/toto3.py",
            )
        ]
    )


def test_get_ignored_lines_with_ignored_lines__prettyprint(
    file_with_ignored_prettyprint,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_prettyprint,
            testing_files / "pprint/pprint2/pprint3.py",
        )
    ).contains_only(
        *[
            IgnoreLine(
                line_num=10,
                error_code="PPL002",
                from_file=testing_files / "pprint/pprint2/pprint3.py",
            )
        ]
    )


def test_get_ignored_lines_with_ignored_lines__sys_stdout_write(
    file_with_ignored_stdout_write,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_stdout_write,
            testing_files / "sys/stdout/write/stdout2/stdout3.py",
        )
    ).contains_only(
        *[
            IgnoreLine(
                line_num=11,
                error_code="PPL003",
                from_file=testing_files / "sys/stdout/write/stdout2/stdout3.py",
            ),
            IgnoreLine(
                line_num=12,
                error_code="PPL003",
                from_file=testing_files / "sys/stdout/write/stdout2/stdout3.py",
            ),
        ]
    )


def test_get_ignored_lines_with_ignored_lines__sys_stderr_write(
    file_with_ignored_stderr_write,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_stderr_write,
            testing_files / "sys/stderr/write/stderr2/stderr3.py",
        )
    ).contains_only(
        *[
            IgnoreLine(
                line_num=11,
                error_code="PPL004",
                from_file=testing_files / "sys/stderr/write/stderr2/stderr3.py",
            ),
            IgnoreLine(
                line_num=12,
                error_code="PPL004",
                from_file=testing_files / "sys/stderr/write/stderr2/stderr3.py",
            ),
        ]
    )


def test_get_ignored_lines_without_ignored_lines__print(
    file_without_ignored_print,
    testing_files,
):
    assert_that(
        get_ignore_lines(file_without_ignored_print, testing_files / "print/toto_1.py")
    ).is_equal_to([])


def test_get_ignored_lines_without_ignored_lines__prettyprint(
    file_without_ignored_prettyprint,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_without_ignored_prettyprint,
            testing_files / "pprint/pprint1.py",
        )
    ).is_equal_to([])


def test_get_ignored_lines_without_ignored_lines__sys_stdout_write(
    file_without_ignored_stdout_write,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_without_ignored_stdout_write,
            testing_files / "sys/stdout/write/²1.py",
        )
    ).is_equal_to([])


def test_get_ignored_lines_without_ignored_lines__sys_stderr_write(
    file_without_ignored_stderr_write,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_without_ignored_stderr_write,
            testing_files / "sys/stderr/write/stderr1.py",
        )
    ).is_equal_to([])


@pytest.mark.parametrize(
    "path_file, expected_ignored_lines",
    [
        # print
        param(
            "print/toto_0.py",
            [],
            id="0 print",
        ),
        param(
            "print/toto_1.py",
            [],
            id="1 print",
        ),
        param(
            "print/toto2/toto3.py",
            [
                IgnoreLine(
                    line_num=6,
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "print/toto2/toto3.py",
                )
            ],
            id="1 print, 1 ignored print",
        ),
        # pprint
        param(
            "pprint/pprint0.py",
            [],
            id="0 prettyprint",
        ),
        param(
            "pprint/pprint1.py",
            [],
            id="1 prettyprint",
        ),
        param(
            "pprint/pprint2/pprint3.py",
            [
                IgnoreLine(
                    line_num=10,
                    error_code="PPL002",
                    from_file=INPUT_FILE_PATH / "pprint/pprint2/pprint3.py",
                )
            ],
            id="1 prettyprint, 1 ignored prettyprint",
        ),
        # sys.stdout.write
        param(
            "sys/stdout/write/stdout0.py",
            [],
            id="0 sys.stdout.write",
        ),
        param(
            "sys/stdout/write/stdout1.py",
            [],
            id="2 sys.stdout.write",
        ),
        param(
            "sys/stdout/write/stdout2/stdout3.py",
            [
                IgnoreLine(
                    line_num=11,
                    error_code="PPL003",
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout2/stdout3.py",
                ),
                IgnoreLine(
                    line_num=12,
                    error_code="PPL003",
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout2/stdout3.py",
                ),
            ],
            id="2 sys.stdout.write, 2 ignored sys.stdout.write",
        ),
        # sys.stderr.write
        param(
            "sys/stderr/write/stderr0.py",
            [],
            id="0 sys.stderr.write",
        ),
        param(
            "sys/stderr/write/stderr1.py",
            [],
            id="2 sys.stderr.write",
        ),
        param(
            "sys/stderr/write/stderr2/stderr3.py",
            [
                IgnoreLine(
                    line_num=11,
                    error_code="PPL004",
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr2/stderr3.py",
                ),
                IgnoreLine(
                    line_num=12,
                    error_code="PPL004",
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr2/stderr3.py",
                ),
            ],
            id="2 sys.stderr.write, 2 ignored sys.stderr.write",
        ),
        # mixed
        param(
            "mixed/mixed0.py",
            [
                IgnoreLine(
                    line_num=8,
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                ),
                IgnoreLine(
                    line_num=9,
                    error_code="PPL002",
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                ),
                IgnoreLine(
                    line_num=11,
                    error_code="PPL002",
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                ),
                IgnoreLine(
                    line_num=12,
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                ),
            ],
            id="not in a folder: 3 print, 1 ignored, 3 prettyprint, 1 ignored",
        ),
        param(
            "mixed/mixed1/mixed2.py",
            [
                IgnoreLine(
                    line_num=8,
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                ),
                IgnoreLine(
                    line_num=9,
                    error_code="PPL002",
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                ),
                IgnoreLine(
                    line_num=11,
                    error_code="PPL002",
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                ),
                IgnoreLine(
                    line_num=12,
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                ),
            ],
            id="in a folder: 3 print, 1 ignored, 3 prettyprint, 1 ignored",
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
