# Standard imports
from pathlib import Path

# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IgnoreLine, get_ignore_lines


def test_get_ignored_next_line__print(
    file_with_ignored_next_print,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_next_print,
            testing_files / "ignored_next_line/ppl001.py",
        )
    ).is_equal_to(
        [
            IgnoreLine(
                line_num=7,
                error_code="PPL001",
                from_file=Path(testing_files / "ignored_next_line/ppl001.py"),
            )
        ]
    )


def test_get_ignored_next_line__pprint(
    file_with_ignored_next_pprint,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_next_pprint,
            testing_files / "ignored_next_line/ppl002.py",
        )
    ).is_equal_to(
        [
            IgnoreLine(
                line_num=11,
                error_code="PPL002",
                from_file=Path(testing_files / "ignored_next_line/ppl002.py"),
            )
        ]
    )


def test_get_ignored_next_line__stdout_write(
    file_with_ignored_next_stdout_write,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_next_stdout_write,
            testing_files / "ignored_next_line/ppl003.py",
        )
    ).is_equal_to(
        [
            IgnoreLine(
                line_num=11,
                error_code="PPL003",
                from_file=Path(testing_files / "ignored_next_line/ppl003.py"),
            )
        ]
    )


def test_get_ignored_next_line__stderr_write(
    file_with_ignored_next_stderr_write,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_next_stderr_write,
            testing_files / "ignored_next_line/ppl004.py",
        )
    ).is_equal_to(
        [
            IgnoreLine(
                line_num=11,
                error_code="PPL004",
                from_file=Path(testing_files / "ignored_next_line/ppl004.py"),
            )
        ]
    )


def test_get_ignored_next_line__stdout_writelines(
    file_with_ignored_next_stdout_writelines,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_next_stdout_writelines,
            testing_files / "ignored_next_line/ppl005.py",
        )
    ).is_equal_to(
        [
            IgnoreLine(
                line_num=11,
                error_code="PPL005",
                from_file=Path(testing_files / "ignored_next_line/ppl005.py"),
            )
        ]
    )


def test_get_ignored_next_line__stderr_writelines(
    file_with_ignored_next_stderr_writelines,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_next_stderr_writelines,
            testing_files / "ignored_next_line/ppl006.py",
        )
    ).is_equal_to(
        [
            IgnoreLine(
                line_num=11,
                error_code="PPL006",
                from_file=Path(testing_files / "ignored_next_line/ppl006.py"),
            )
        ]
    )
