# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import get_ignored_files


def test_get_ignored_files_without_ignored_files(
    file_without_ignored_file,
    testing_files,
):
    assert_that(
        get_ignored_files(
            file_without_ignored_file,
            testing_files / "ignored_files/ignore_nothing.py",
        )
    ).is_equal_to([])
