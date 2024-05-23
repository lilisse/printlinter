# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IgnoredBlock, get_ignored_blocks


def test_get_ignored_block_with_ignored_block__ALL__re_enable(
    file_with_ignored_block_all__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_all__re_enable,
            testing_files / "ignored_block/re_enable/all.py",
            18,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="ALL",
                line_from=10,
                line_to=17,
                from_file=testing_files / "ignored_block/re_enable/all.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl001__re_enable(
    file_with_ignored_block_print__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_print__re_enable,
            testing_files / "ignored_block/re_enable/ppl001.py",
            9,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL001",
                line_from=5,
                line_to=8,
                from_file=testing_files / "ignored_block/re_enable/ppl001.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl002__re_enable(
    file_with_ignored_block_pprint__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_pprint__re_enable,
            testing_files / "ignored_block/re_enable/ppl002.py",
            13,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL002",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/re_enable/ppl002.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl003__re_enable(
    file_with_ignored_block_stdout_write__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stdout_write__re_enable,
            testing_files / "ignored_block/re_enable/ppl003.py",
            13,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL003",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/re_enable/ppl003.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl004__re_enable(
    file_with_ignored_block_stderr_write__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stderr_write__re_enable,
            testing_files / "ignored_block/re_enable/ppl004.py",
            13,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL004",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/re_enable/ppl004.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl005__re_enable(
    file_with_ignored_block_stdout_writelines__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stdout_writelines__re_enable,
            testing_files / "ignored_block/re_enable/ppl005.py",
            13,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL005",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/re_enable/ppl005.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl006__re_enable(
    file_with_ignored_block_stderr_writelines__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stderr_writelines__re_enable,
            testing_files / "ignored_block/re_enable/ppl006.py",
            13,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL006",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/re_enable/ppl006.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__mix__re_enable(
    file_with_ignored_block_mix__re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_mix__re_enable,
            testing_files / "ignored_block/re_enable/mix.py",
            17,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL002",
                line_from=9,
                line_to=16,
                from_file=testing_files / "ignored_block/re_enable/mix.py",
            ),
            IgnoredBlock(
                error_code="PPL001",
                line_from=12,
                line_to=15,
                from_file=testing_files / "ignored_block/re_enable/mix.py",
            ),
        ]
    )


def test_get_ignored_block_with_ignored_block__ALL__no_re_enable(
    file_with_ignored_block_all__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_all__no_re_enable,
            testing_files / "ignored_block/no_re_enable/all.py",
            17,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="ALL",
                line_from=10,
                line_to=17,
                from_file=testing_files / "ignored_block/no_re_enable/all.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl001__no_re_enable(
    file_with_ignored_block_print__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_print__no_re_enable,
            testing_files / "ignored_block/no_re_enable/ppl001.py",
            8,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL001",
                line_from=5,
                line_to=8,
                from_file=testing_files / "ignored_block/no_re_enable/ppl001.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl002__no_re_enable(
    file_with_ignored_block_pprint__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_pprint__no_re_enable,
            testing_files / "ignored_block/no_re_enable/ppl002.py",
            12,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL002",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/no_re_enable/ppl002.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl003__no_re_enable(
    file_with_ignored_block_stdout_write__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stdout_write__no_re_enable,
            testing_files / "ignored_block/no_re_enable/ppl003.py",
            12,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL003",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/no_re_enable/ppl003.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl004__no_re_enable(
    file_with_ignored_block_stderr_write__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stderr_write__no_re_enable,
            testing_files / "ignored_block/no_re_enable/ppl004.py",
            12,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL004",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/no_re_enable/ppl004.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl005__no_re_enable(
    file_with_ignored_block_stdout_writelines__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stdout_writelines__no_re_enable,
            testing_files / "ignored_block/no_re_enable/ppl005.py",
            12,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL005",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/no_re_enable/ppl005.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__ppl006__no_re_enable(
    file_with_ignored_block_stderr_writelines__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_stderr_writelines__no_re_enable,
            testing_files / "ignored_block/no_re_enable/ppl006.py",
            12,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL006",
                line_from=9,
                line_to=12,
                from_file=testing_files / "ignored_block/no_re_enable/ppl006.py",
            )
        ]
    )


def test_get_ignored_block_with_ignored_block__mix__no_re_enable(
    file_with_ignored_block_mix__no_re_enable,
    testing_files,
):
    assert_that(
        get_ignored_blocks(
            file_with_ignored_block_mix__no_re_enable,
            testing_files / "ignored_block/no_re_enable/mix.py",
            15,
        )
    ).contains_only(
        *[
            IgnoredBlock(
                error_code="PPL002",
                line_from=9,
                line_to=15,
                from_file=testing_files / "ignored_block/no_re_enable/mix.py",
            ),
            IgnoredBlock(
                error_code="PPL001",
                line_from=12,
                line_to=15,
                from_file=testing_files / "ignored_block/no_re_enable/mix.py",
            ),
        ]
    )
