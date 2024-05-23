# Pytest imports
import pytest
from pytest import param

# Standard imports
import ast

# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import IssueEnum, IssueInfo, contains_print

# Local imports
from ..conftest import INPUT_FILE_PATH


@pytest.mark.parametrize(
    "file_path, expected",
    [
        # print
        param("print/toto_0.py", [], id="0 print"),
        param(
            "print/toto_1.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=3,
                    num_col=0,
                    line_as_str='print("Hello, world")',
                    from_file=INPUT_FILE_PATH / "print/toto_1.py",
                    ignored=False,
                )
            ],
            id="1 print",
        ),
        param(
            "print/toto2/toto3.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=6,
                    num_col=4,
                    line_as_str='print("toto")  # noqa: PPL001',
                    from_file=INPUT_FILE_PATH / "print/toto2/toto3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=7,
                    num_col=4,
                    line_as_str='print("tata")',
                    from_file=INPUT_FILE_PATH / "print/toto2/toto3.py",
                    ignored=False,
                ),
            ],
            id="2 print",
        ),
        # pprint
        param("pprint/pprint0.py", [], id="0 pprint"),
        param(
            "pprint/pprint1.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=6,
                    num_col=0,
                    line_as_str='pprint("Hello, world")',
                    from_file=INPUT_FILE_PATH / "pprint/pprint1.py",
                    ignored=False,
                )
            ],
            id="1 pprint",
        ),
        param(
            "pprint/pprint2/pprint3.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=10,
                    num_col=4,
                    line_as_str='pprint("toto")  # noqa: PPL002',
                    from_file=INPUT_FILE_PATH / "pprint/pprint2/pprint3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=11,
                    num_col=4,
                    line_as_str='pprint("tata")',
                    from_file=INPUT_FILE_PATH / "pprint/pprint2/pprint3.py",
                    ignored=False,
                ),
            ],
            id="2 pprint",
        ),
        # sys.stdout.write
        param("sys/stdout/write/stdout0.py", [], id="0 sys.stdout.write"),
        param(
            "sys/stdout/write/stdout1.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITEDETECT,
                    num_line=7,
                    num_col=0,
                    line_as_str='sys.stdout.write("Hello, world")',
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout1.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITEDETECT,
                    num_line=8,
                    num_col=0,
                    line_as_str='stdout.write("Hello, world")',
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout1.py",
                    ignored=False,
                ),
            ],
            id="2 sys.stdout.write",
        ),
        param(
            "sys/stdout/write/stdout2/stdout3.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITEDETECT,
                    num_line=11,
                    num_col=4,
                    line_as_str='sys.stdout.write("toto")  # noqa: PPL003',
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout2/stdout3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITEDETECT,
                    num_line=12,
                    num_col=4,
                    line_as_str='stdout.write("toto")  # noqa: PPL003',
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout2/stdout3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITEDETECT,
                    num_line=13,
                    num_col=4,
                    line_as_str='sys.stdout.write("tata")',
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout2/stdout3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITEDETECT,
                    num_line=14,
                    num_col=4,
                    line_as_str='stdout.write("tata")',
                    from_file=INPUT_FILE_PATH / "sys/stdout/write/stdout2/stdout3.py",
                    ignored=False,
                ),
            ],
            id="4 sys.stdout.write",
        ),
        # sys.stderr.write
        param("sys/stderr/write/stderr0.py", [], id="0 sys.stderr.write"),
        param(
            "sys/stderr/write/stderr1.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITEDETECT,
                    num_line=7,
                    num_col=0,
                    line_as_str='sys.stderr.write("Hello, world")',
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr1.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITEDETECT,
                    num_line=8,
                    num_col=0,
                    line_as_str='stderr.write("Hello, world")',
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr1.py",
                    ignored=False,
                ),
            ],
            id="2 sys.stderr.write",
        ),
        param(
            "sys/stderr/write/stderr2/stderr3.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITEDETECT,
                    num_line=11,
                    num_col=4,
                    line_as_str='sys.stderr.write("toto")  # noqa: PPL004',
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr2/stderr3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITEDETECT,
                    num_line=12,
                    num_col=4,
                    line_as_str='stderr.write("toto")  # noqa: PPL004',
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr2/stderr3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITEDETECT,
                    num_line=13,
                    num_col=4,
                    line_as_str='sys.stderr.write("tata")',
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr2/stderr3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITEDETECT,
                    num_line=14,
                    num_col=4,
                    line_as_str='stderr.write("tata")',
                    from_file=INPUT_FILE_PATH / "sys/stderr/write/stderr2/stderr3.py",
                    ignored=False,
                ),
            ],
            id="4 sys.stderr.write",
        ),
        # sys.stdout.writelines
        param("sys/stdout/writelines/stdout0.py", [], id="0 sys.stdout.writelines"),
        param(
            "sys/stdout/writelines/stdout1.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
                    num_line=7,
                    num_col=0,
                    line_as_str='sys.stdout.writelines(["Hello", "world"])',
                    from_file=INPUT_FILE_PATH / "sys/stdout/writelines/stdout1.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
                    num_line=8,
                    num_col=0,
                    line_as_str='stdout.writelines(["Hello", "world"])',
                    from_file=INPUT_FILE_PATH / "sys/stdout/writelines/stdout1.py",
                    ignored=False,
                ),
            ],
            id="2 sys.stdout.writelines",
        ),
        param(
            "sys/stdout/writelines/stdout2/stdout3.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
                    num_line=11,
                    num_col=4,
                    line_as_str=(
                        'sys.stdout.writelines(["toto", "titi"])  # noqa: PPL005'
                    ),
                    from_file=INPUT_FILE_PATH
                    / "sys/stdout/writelines/stdout2/stdout3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
                    num_line=12,
                    num_col=4,
                    line_as_str='stdout.writelines(["toto", "titi"])  # noqa: PPL005',
                    from_file=INPUT_FILE_PATH
                    / "sys/stdout/writelines/stdout2/stdout3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
                    num_line=13,
                    num_col=4,
                    line_as_str='sys.stdout.writelines(["tata", "tutu"])',
                    from_file=INPUT_FILE_PATH
                    / "sys/stdout/writelines/stdout2/stdout3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
                    num_line=14,
                    num_col=4,
                    line_as_str='stdout.writelines(["tata", "tutu"])',
                    from_file=INPUT_FILE_PATH
                    / "sys/stdout/writelines/stdout2/stdout3.py",
                    ignored=False,
                ),
            ],
            id="4 sys.stdout.writelines",
        ),
        # sys.stderr.writelines
        param("sys/stderr/writelines/stderr0.py", [], id="0 sys.stderr.writelines"),
        param(
            "sys/stderr/writelines/stderr1.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
                    num_line=7,
                    num_col=0,
                    line_as_str='sys.stderr.writelines(["Hello", "world"])',
                    from_file=INPUT_FILE_PATH / "sys/stderr/writelines/stderr1.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
                    num_line=8,
                    num_col=0,
                    line_as_str='stderr.writelines(["Hello", "world"])',
                    from_file=INPUT_FILE_PATH / "sys/stderr/writelines/stderr1.py",
                    ignored=False,
                ),
            ],
            id="2 sys.stderr.writelines",
        ),
        param(
            "sys/stderr/writelines/stderr2/stderr3.py",
            [
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
                    num_line=11,
                    num_col=4,
                    line_as_str=(
                        'sys.stderr.writelines(["toto", "titi"])  # noqa: PPL006'
                    ),
                    from_file=INPUT_FILE_PATH
                    / "sys/stderr/writelines/stderr2/stderr3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
                    num_line=12,
                    num_col=4,
                    line_as_str='stderr.writelines(["toto", "titi"])  # noqa: PPL006',
                    from_file=INPUT_FILE_PATH
                    / "sys/stderr/writelines/stderr2/stderr3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
                    num_line=13,
                    num_col=4,
                    line_as_str='sys.stderr.writelines(["tata", "tutu"])',
                    from_file=INPUT_FILE_PATH
                    / "sys/stderr/writelines/stderr2/stderr3.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
                    num_line=14,
                    num_col=4,
                    line_as_str='stderr.writelines(["tata", "tutu"])',
                    from_file=INPUT_FILE_PATH
                    / "sys/stderr/writelines/stderr2/stderr3.py",
                    ignored=False,
                ),
            ],
            id="4 sys.stderr.writelines",
        ),
        # mixed
        param(
            "mixed/mixed0.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=5,
                    num_col=0,
                    line_as_str='print("toto")',
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=6,
                    num_col=0,
                    line_as_str='pprint("titi")',
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=8,
                    num_col=0,
                    line_as_str='print("tata")  # noqa: PPL001',
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=9,
                    num_col=0,
                    line_as_str='pprint("tutu")  # noqa: PPL002',
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=11,
                    num_col=0,
                    line_as_str='print("foo")  # noqa: PPL002',
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=12,
                    num_col=0,
                    line_as_str='pprint("bar")  # noqa: PPL001',
                    from_file=INPUT_FILE_PATH / "mixed/mixed0.py",
                    ignored=False,
                ),
            ],
            id="not in a folder: 2 print, 2 prettyprint",
        ),
        param(
            "mixed/mixed1/mixed2.py",
            [
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=5,
                    num_col=0,
                    line_as_str='print("toto")',
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=6,
                    num_col=0,
                    line_as_str='pprint("titi")',
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=8,
                    num_col=0,
                    line_as_str='print("tata")  # noqa: PPL001',
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=9,
                    num_col=0,
                    line_as_str='pprint("tutu")  # noqa: PPL002',
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRINTDETECT,
                    num_line=11,
                    num_col=0,
                    line_as_str='print("foo")  # noqa: PPL002',
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                    ignored=False,
                ),
                IssueInfo(
                    issue=IssueEnum.PRETTYPRINTDETECT,
                    num_line=12,
                    num_col=0,
                    line_as_str='pprint("bar")  # noqa: PPL001',
                    from_file=INPUT_FILE_PATH / "mixed/mixed1/mixed2.py",
                    ignored=False,
                ),
            ],
            id="in a folder: 2 print, 2 prettyprint",
        ),
    ],
)
def test_contains_print_with_files_with_ignore_lines(
    pnv_soft_reset,
    testing_files,
    file_path,
    expected,
):
    with open(testing_files / file_path, encoding="utf-8") as file:
        tree = ast.parse(
            source=file.read(),
            filename=testing_files / file_path,
            feature_version=(3, 11),
        )

    print_detected = contains_print(testing_files / file_path, tree)

    if not expected:
        assert print_detected == expected
    else:
        assert print_detected == expected


@pytest.mark.parametrize(
    "file_path, gap_line",
    [
        # nothings
        param(
            "ignored_files/ignore_nothing.py",
            0,
            id="No ignore files",
        ),
        # all
        param(
            "ignored_files/ignore_all.py",
            1,
            id="Ignore all in file",
        ),
        # standard library
        param(
            "ignored_files/ignore_ppl000.py",
            1,
            id="Ignore standard lib display function in file",
        ),
        # print
        param(
            "ignored_files/ignore_ppl001.py",
            1,
            id="Ignore print in file",
        ),
        # pprint
        param(
            "ignored_files/ignore_ppl002.py",
            1,
            id="Ignore pprint in file",
        ),
        # sys.stdout.write
        param(
            "ignored_files/ignore_ppl003.py",
            1,
            id="Ignore sys.stdout.write and stdout.write in file",
        ),
        # sys.stderr.write
        param(
            "ignored_files/ignore_ppl004.py",
            1,
            id="Ignore sys.stderr.write and stderr.write in file",
        ),
        # sys.stdout.writelines
        param(
            "ignored_files/ignore_ppl004.py",
            1,
            id="Ignore sys.stdout.writelines and stdout.writelines in file",
        ),
        # sys.stderr.writelines
        param(
            "ignored_files/ignore_ppl006.py",
            1,
            id="Ignore sys.stderr.writelines and stderr.writelines in file",
        ),
    ],
)
def test_contains_print_with_files_with_ignore_files(
    pnv_soft_reset,
    testing_files,
    file_path,
    gap_line,
):
    expected = [
        IssueInfo(
            issue=IssueEnum.PRINTDETECT,
            num_line=6 + gap_line,
            num_col=0,
            line_as_str='print("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.PRETTYPRINTDETECT,
            num_line=8 + gap_line,
            num_col=0,
            line_as_str='pprint("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=10 + gap_line,
            num_col=0,
            line_as_str='sys.stdout.write("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITEDETECT,
            num_line=11 + gap_line,
            num_col=0,
            line_as_str='stdout.write("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=13 + gap_line,
            num_col=0,
            line_as_str='sys.stderr.write("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITEDETECT,
            num_line=14 + gap_line,
            num_col=0,
            line_as_str='stderr.write("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=16 + gap_line,
            num_col=0,
            line_as_str='sys.stdout.writelines("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDOUTWRITELINESDETECT,
            num_line=17 + gap_line,
            num_col=0,
            line_as_str='stdout.writelines("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=19 + gap_line,
            num_col=0,
            line_as_str='sys.stderr.writelines("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
        IssueInfo(
            issue=IssueEnum.SYSSTDERRWRITELINESDETECT,
            num_line=20 + gap_line,
            num_col=0,
            line_as_str='stderr.writelines("toto")',
            from_file=INPUT_FILE_PATH / file_path,
            ignored=False,
        ),
    ]

    with open(testing_files / file_path, encoding="utf-8") as file:
        tree = ast.parse(
            source=file.read(),
            filename=testing_files / file_path,
            feature_version=(3, 11),
        )

    print_detected = contains_print(testing_files / file_path, tree)

    if not expected:
        assert print_detected == expected
    else:
        assert print_detected == expected
