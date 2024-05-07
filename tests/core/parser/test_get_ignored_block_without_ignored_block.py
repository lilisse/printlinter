# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IgnoredBlock, get_ignored_block


def test_get_ignored_block_without_ignored_block(
    file_with_ignored_block_nothing,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_nothing,
            testing_files / "ignored_block/ignore_nothing.py",
        )
    ).is_equal_to([])
