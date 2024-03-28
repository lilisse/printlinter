# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IgnoreLine, get_ignore_lines


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


def test_get_ignored_lines_with_ignored_lines__sys_stdout_writelines(
    file_with_ignored_stdout_writelines,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_stdout_writelines,
            testing_files / "sys/stdout/writelines/stdout2/stdout3.py",
        )
    ).contains_only(
        *[
            IgnoreLine(
                line_num=11,
                error_code="PPL005",
                from_file=testing_files / "sys/stdout/writelines/stdout2/stdout3.py",
            ),
            IgnoreLine(
                line_num=12,
                error_code="PPL005",
                from_file=testing_files / "sys/stdout/writelines/stdout2/stdout3.py",
            ),
        ]
    )


def test_get_ignored_lines_with_ignored_lines__sys_stderr_writelines(
    file_with_ignored_stderr_writelines,
    testing_files,
):
    assert_that(
        get_ignore_lines(
            file_with_ignored_stderr_writelines,
            testing_files / "sys/stderr/writelines/stderr2/stderr3.py",
        )
    ).contains_only(
        *[
            IgnoreLine(
                line_num=11,
                error_code="PPL006",
                from_file=testing_files / "sys/stderr/writelines/stderr2/stderr3.py",
            ),
            IgnoreLine(
                line_num=12,
                error_code="PPL006",
                from_file=testing_files / "sys/stderr/writelines/stderr2/stderr3.py",
            ),
        ]
    )
