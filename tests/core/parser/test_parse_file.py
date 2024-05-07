# Pytest imports
import pytest
from pytest import param

# Standard imports
import ast
from itertools import product

# Third party imports
from assertpy import assert_that, soft_assertions

# First party imports
from printlinter import IgnoredBlock, IgnoreFile, IgnoreLine, parse_file
from printlinter.config import MAX_MAJOR, MAX_MINOR

# Local imports
from ...conftest import INPUT_FILE_PATH
from .conftest import compare_ast


@pytest.mark.parametrize(
    "target_version",
    [
        param(version, id=f"target version = {version}")
        for version in product([*range(3, MAX_MAJOR + 1)], [*range(7, MAX_MINOR + 1)])
    ],
)
@pytest.mark.parametrize(
    "path_file, expected_ignored_lines, expected_ignored_files, expected_ignored_block",
    [
        # Ignored Lines
        # print
        param(
            "print/toto_0.py",
            [],
            [],
            [],
            id="0 print",
        ),
        param(
            "print/toto_1.py",
            [],
            [],
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
            [],
            [],
            id="1 print, 1 ignored print",
        ),
        # pprint
        param(
            "pprint/pprint0.py",
            [],
            [],
            [],
            id="0 prettyprint",
        ),
        param(
            "pprint/pprint1.py",
            [],
            [],
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
            [],
            [],
            id="1 prettyprint, 1 ignored prettyprint",
        ),
        # sys.stdout.write
        param(
            "sys/stdout/write/stdout0.py",
            [],
            [],
            [],
            id="0 sys.stdout.write",
        ),
        param(
            "sys/stdout/write/stdout1.py",
            [],
            [],
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
            [],
            [],
            id="2 sys.stdout.write, 2 ignored sys.stdout.write",
        ),
        # sys.stderr.write
        param(
            "sys/stderr/write/stderr0.py",
            [],
            [],
            [],
            id="0 sys.stderr.write",
        ),
        param(
            "sys/stderr/write/stderr1.py",
            [],
            [],
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
            [],
            [],
            id="2 sys.stderr.write, 2 ignored sys.stderr.write",
        ),
        # sys.stdout.writelines
        param(
            "sys/stdout/writelines/stdout0.py",
            [],
            [],
            [],
            id="0 sys.stdout.writelines",
        ),
        param(
            "sys/stdout/writelines/stdout1.py",
            [],
            [],
            [],
            id="2 sys.stdout.writelines",
        ),
        param(
            "sys/stdout/writelines/stdout2/stdout3.py",
            [
                IgnoreLine(
                    line_num=11,
                    error_code="PPL005",
                    from_file=INPUT_FILE_PATH
                    / "sys/stdout/writelines/stdout2/stdout3.py",
                ),
                IgnoreLine(
                    line_num=12,
                    error_code="PPL005",
                    from_file=INPUT_FILE_PATH
                    / "sys/stdout/writelines/stdout2/stdout3.py",
                ),
            ],
            [],
            [],
            id="2 sys.stdout.writelines, 2 ignored sys.stdout.writelines",
        ),
        # sys.stderr.writelines
        param(
            "sys/stderr/writelines/stderr0.py",
            [],
            [],
            [],
            id="0 sys.stderr.writelines",
        ),
        param(
            "sys/stderr/writelines/stderr1.py",
            [],
            [],
            [],
            id="2 sys.stderr.writelines",
        ),
        param(
            "sys/stderr/writelines/stderr2/stderr3.py",
            [
                IgnoreLine(
                    line_num=11,
                    error_code="PPL006",
                    from_file=INPUT_FILE_PATH
                    / "sys/stderr/writelines/stderr2/stderr3.py",
                ),
                IgnoreLine(
                    line_num=12,
                    error_code="PPL006",
                    from_file=INPUT_FILE_PATH
                    / "sys/stderr/writelines/stderr2/stderr3.py",
                ),
            ],
            [],
            [],
            id="2 sys.stderr.writelines, 2 ignored sys.stderr.writelines",
        ),
        # mixed ignored lines
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
            [],
            [],
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
            [],
            [],
            id="in a folder: 3 print, 1 ignored, 3 prettyprint, 1 ignored",
        ),
        # Ignored Files
        # nothings
        param(
            "ignored_files/ignore_nothing.py",
            [],
            [],
            [],
            id="No ignore files",
        ),
        # all
        param(
            "ignored_files/ignore_all.py",
            [],
            [
                IgnoreFile(
                    error_code="ALL",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_all.py",
                )
            ],
            [],
            id="Ignore all in file",
        ),
        # standard library
        param(
            "ignored_files/ignore_ppl000.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL000",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl000.py",
                )
            ],
            [],
            id="Ignore standard lib display function in file",
        ),
        # print
        param(
            "ignored_files/ignore_ppl001.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL001",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl001.py",
                )
            ],
            [],
            id="Ignore print in file",
        ),
        # pprint
        param(
            "ignored_files/ignore_ppl002.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL002",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl002.py",
                )
            ],
            [],
            id="Ignore pprint in file",
        ),
        # sys.stdout.write
        param(
            "ignored_files/ignore_ppl003.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL003",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl003.py",
                )
            ],
            [],
            id="Ignore sys.stdout.write and stdout.write in file",
        ),
        # sys.stderr.write
        param(
            "ignored_files/ignore_ppl004.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL004",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl004.py",
                )
            ],
            [],
            id="Ignore sys.stderr.write and stderr.write in file",
        ),
        # sys.stdout.writelines
        param(
            "ignored_files/ignore_ppl004.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL004",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl004.py",
                )
            ],
            [],
            id="Ignore sys.stdout.writelines and stdout.writelines in file",
        ),
        # sys.stderr.writelines
        param(
            "ignored_files/ignore_ppl006.py",
            [],
            [
                IgnoreFile(
                    error_code="PPL006",
                    from_file=INPUT_FILE_PATH / "ignored_files/ignore_ppl006.py",
                )
            ],
            [],
            id="Ignore sys.stderr.writelines and stderr.writelines in file",
        ),
        # Ignore block of code
        # print
        param(
            "ignored_block/ppl001.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL001",
                    line_from=5,
                    line_to=8,
                    from_file=INPUT_FILE_PATH / "ignored_block/ppl001.py",
                )
            ],
            id="Ignore block of code: print",
        ),
        # pprint
        param(
            "ignored_block/ppl002.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL002",
                    line_from=9,
                    line_to=12,
                    from_file=INPUT_FILE_PATH / "ignored_block/ppl002.py",
                )
            ],
            id="Ignore block of code: pprint",
        ),
        # sys.stdout.write
        param(
            "ignored_block/ppl003.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL003",
                    line_from=9,
                    line_to=12,
                    from_file=INPUT_FILE_PATH / "ignored_block/ppl003.py",
                )
            ],
            id="Ignore block of code: sys.stdout.write",
        ),
        # sys.stderr.write
        param(
            "ignored_block/ppl004.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL004",
                    line_from=9,
                    line_to=12,
                    from_file=INPUT_FILE_PATH / "ignored_block/ppl004.py",
                )
            ],
            id="Ignore block of code: sys.stderr.write",
        ),
        # sys.stdout.writelines
        param(
            "ignored_block/ppl005.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL005",
                    line_from=9,
                    line_to=12,
                    from_file=INPUT_FILE_PATH / "ignored_block/ppl005.py",
                )
            ],
            id="Ignore block of code: sys.stdout.writelines",
        ),
        # sys.stderr.writelines
        param(
            "ignored_block/ppl006.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL006",
                    line_from=9,
                    line_to=12,
                    from_file=INPUT_FILE_PATH / "ignored_block/ppl006.py",
                )
            ],
            id="Ignore block of code: sys.stderr.writelines",
        ),
        # mixed
        param(
            "ignored_block/mix.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="PPL002",
                    line_from=9,
                    line_to=16,
                    from_file=INPUT_FILE_PATH / "ignored_block/mix.py",
                ),
                IgnoredBlock(
                    error_code="PPL001",
                    line_from=12,
                    line_to=15,
                    from_file=INPUT_FILE_PATH / "ignored_block/mix.py",
                ),
            ],
            id="Ignore block of code: sys.stderr.writelines",
        ),
        # all
        param(
            "ignored_block/all.py",
            [],
            [],
            [
                IgnoredBlock(
                    error_code="ALL",
                    line_from=10,
                    line_to=17,
                    from_file=INPUT_FILE_PATH / "ignored_block/all.py",
                )
            ],
            id="Ignore block of code: sys.stderr.writelines",
        ),
    ],
)
def test_parse_file(
    testing_files,
    target_version,
    path_file,
    expected_ignored_lines,
    expected_ignored_files,
    expected_ignored_block,
):
    with open(testing_files / path_file, encoding="utf-8") as file:
        expected_tree = ast.parse(
            source=file.read(),
            filename=testing_files / path_file,
            feature_version=target_version,
        )

    tree, ignored_lines, ignored_files, ignored_block = parse_file(
        testing_files / path_file,
        target_version,
    )

    with soft_assertions():
        assert_that(compare_ast(tree, expected_tree)).is_true()

        # ignored lines
        if not expected_ignored_lines:
            assert_that(ignored_lines).is_equal_to([])
        else:
            assert_that(ignored_lines).contains_only(*expected_ignored_lines)

        # ignored file
        if not expected_ignored_files:
            assert_that(ignored_files).is_equal_to([])
        else:
            assert_that(ignored_files).contains_only(*expected_ignored_files)

        # ignored block
        if not expected_ignored_block:
            assert_that(ignored_block).is_equal_to([])
        else:
            assert_that(ignored_block).contains_only(*expected_ignored_block)
