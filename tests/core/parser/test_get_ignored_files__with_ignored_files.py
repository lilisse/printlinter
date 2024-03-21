# Third party imports
from assertpy import assert_that

# First party imports
from py_printlinter import IgnoreFile, get_ignore_files


def test_get_ignored_files_with_ignored_files__ALL(
    file_with_ignored_all,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_all,
            testing_files / "ignored_files/ignore_all.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="ALL",
                from_file=testing_files / "ignored_files/ignore_all.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__standard_lib(
    file_with_ignored_standard_lib,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_standard_lib,
            testing_files / "ignored_files/ignore_ppl000.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL000",
                from_file=testing_files / "ignored_files/ignore_ppl000.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__print(
    file_with_ignored_print__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_print__file,
            testing_files / "ignored_files/ignore_ppl001.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL001",
                from_file=testing_files / "ignored_files/ignore_ppl001.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__prettyprint(
    file_with_ignored_prettyprint__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_prettyprint__file,
            testing_files / "ignored_files/ignore_ppl002.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL002",
                from_file=testing_files / "ignored_files/ignore_ppl002.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__stdout_write(
    file_with_ignored_stdout_write__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_stdout_write__file,
            testing_files / "ignored_files/ignore_ppl003.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL003",
                from_file=testing_files / "ignored_files/ignore_ppl003.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__stderr_write(
    file_with_ignored_stderr_write__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_stderr_write__file,
            testing_files / "ignored_files/ignore_ppl004.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL004",
                from_file=testing_files / "ignored_files/ignore_ppl004.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__stdout_writelines(
    file_with_ignored_stdout_writelines__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_stdout_writelines__file,
            testing_files / "ignored_files/ignore_ppl005.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL005",
                from_file=testing_files / "ignored_files/ignore_ppl005.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__stderr_writelines(
    file_with_ignored_stderr_writelines__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_ignored_stderr_writelines__file,
            testing_files / "ignored_files/ignore_ppl006.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="PPL006",
                from_file=testing_files / "ignored_files/ignore_ppl006.py",
            )
        ]
    )


def test_get_ignored_files_with_ignored_files__comment_in_wrong_place(
    file_with_comment_in_wrong_place__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_comment_in_wrong_place__file,
            testing_files / "ignored_files/disable_in_wrong_place.py",
        )
    ).is_none()


def test_get_ignored_files_with_ignored_files__comment_top_of_the_file_not_first_line(
    file_with_comment_not_at_first_line__file,
    testing_files,
):
    assert_that(
        get_ignore_files(
            file_with_comment_not_at_first_line__file,
            testing_files / "ignored_files/disable_valid_but_not_in_first_line.py",
        )
    ).contains_only(
        *[
            IgnoreFile(
                error_code="ALL",
                from_file=testing_files
                / "ignored_files/disable_valid_but_not_in_first_line.py",
            )
        ]
    )
