# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import get_ignore_lines


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
            testing_files / "sys/stdout/write/stdout1.py",
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


def test_get_ignored_lines_without_ignored_lines__sys_stdout_writelines(
    file_without_ignored_stdout_writelines,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_without_ignored_stdout_writelines,
            testing_files / "sys/stdout/writelines/stdout1.py",
        )
    ).is_equal_to([])


def test_get_ignored_lines_without_ignored_lines__sys_stderr_writelines(
    file_without_ignored_stderr_writelines,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_without_ignored_stderr_writelines,
            testing_files / "sys/stderr/writelines/stderr1.py",
        )
    ).is_equal_to([])
