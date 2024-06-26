# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IgnoredBlock, get_ignored_blocks


def test_get_ignored_block_without_ignored_block(
    file_with_ignored_block_nothing,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_nothing,
            testing_files / "ignored_block/ignore_nothing.py",
            6,
        )
    ).is_equal_to([])
