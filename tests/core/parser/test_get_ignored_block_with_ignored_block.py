# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IgnoredBlock, get_ignored_block


def test_get_ignored_block_with_ignored_block__ALL(
    file_with_ignored_block_all,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_all,
            testing_files / "ignored_block/all.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="ALL",
                line_from=10,
                line_to=17,
                from_file=testing_files / "ignored_block/all.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl001(
    file_with_ignored_block_print,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_print,
            testing_files / "ignored_block/ppl001.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL001",
                line_from=5,
                line_to=8,
                from_file=testing_files / "ignored_block/ppl001.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl002(
    file_with_ignored_block_pprint,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_pprint,
            testing_files / "ignored_block/ppl002.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL002",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/ppl002.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl003(
    file_with_ignored_block_stdout_write,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_stdout_write,
            testing_files / "ignored_block/ppl003.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL003",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/ppl003.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl004(
    file_with_ignored_block_stderr_write,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_stderr_write,
            testing_files / "ignored_block/ppl004.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL004",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/ppl004.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl005(
    file_with_ignored_block_stdout_writelines,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_stdout_writelines,
            testing_files / "ignored_block/ppl005.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL005",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/ppl005.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl006(
    file_with_ignored_block_stderr_writelines,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_stderr_writelines,
            testing_files / "ignored_block/ppl006.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL006",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/ppl006.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__mix(
    file_with_ignored_block_mix,
    testing_files,
):
    assert_that(
        get_ignored_block(
            file_with_ignored_block_mix,
            testing_files / "ignored_block/mix.py",
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL002",
                line_from=9,
                line_to=16,
                from_file=testing_files / "ignored_block/mix.py",
            ),
            IgnoredBlock(
                error_code="PPL001",
                line_from=12,
                line_to=15,
                from_file=testing_files / "ignored_block/mix.py",
            ),
        ]
    )
