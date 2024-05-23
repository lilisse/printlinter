# Pytest imports
import pytest

# First party imports
from printlinter import IgnoredBlock, IgnoredFile, IgnoredLine, IssueEnum, IssueInfo


@pytest.fixture(scope="function")
def issues_for_lines() -> list[IssueInfo]:
    """
    Get a list of issues to test ignored lines.

    Returns:
        Issues to test ignored lines.
    """
    res = [
        IssueInfo(IssueEnum.PRINTDETECT, line, 12, "print('toto')", "toto1.py", False)
        for line in range(9)
    ]

    res.extend(
        [
            IssueInfo(
                IssueEnum.PRETTYPRINTDETECT,
                line,
                12,
                "pprint('toto')",
                "toto2.py",
                False,
            )
            for line in range(9, 15)
        ]
    )

    res.extend(
        [
            IssueInfo(
                IssueEnum.SYSSTDOUTWRITEDETECT,
                line,
                12,
                "sys.stdout.write('toto')",
                "toto3.py",
                False,
            )
            for line in range(15, 23)
        ]
    )

    res.extend(
        [
            IssueInfo(
                IssueEnum.SYSSTDERRWRITEDETECT,
                line,
                12,
                "sys.stderr.write('toto')",
                "toto4.py",
                False,
            )
            for line in range(23, 31)
        ]
    )

    res.extend(
        [
            IssueInfo(
                IssueEnum.SYSSTDOUTWRITELINESDETECT,
                line,
                12,
                "sys.stdout.writelines(['toto', 'titi'])",
                "toto5.py",
                False,
            )
            for line in range(31, 36)
        ]
    )

    res.extend(
        [
            IssueInfo(
                IssueEnum.SYSSTDERRWRITELINESDETECT,
                line,
                12,
                "sys.stderr.writelines(['toto', 'titi'])",
                "toto6.py",
                False,
            )
            for line in range(36, 41)
        ]
    )

    return res


@pytest.fixture(scope="function")
def issues_for_files() -> list[IssueInfo]:
    """
    Get a list of issues to test ignored files.

    Returns:
        Issues to test ignored files.
    """
    res = []
    for error_type, line_as_str in zip(
        IssueEnum,
        [
            "print('toto')",
            "pprint('toto')",
            "sys.stdout.write('toto')",
            "sys.stderr.write('toto')",
            "sys.stdout.writelines(['toto', 'titi'])",
            "sys.stderr.writelines(['toto', 'titi'])",
        ],
    ):
        for test_file in [
            "toto1.py",
            "toto2.py",
            "toto3.py",
            "toto4.py",
            "toto5.py",
        ]:
            res.append(IssueInfo(error_type, 3, 12, line_as_str, test_file, False))

    return res


@pytest.fixture(scope="function")
def issues_for_files_and_lines() -> list[IssueInfo]:
    """
    Get a list of issues to test ignored files and lines.

    Returns:
        Issues to test ignored files and lines.
    """
    res = []
    line = 0
    for error_type, line_as_str in zip(
        IssueEnum,
        [
            "print('toto')",  # line = 1
            "pprint('toto')",  # line = 2
            "sys.stdout.write('toto')",  # line = 3
            "sys.stderr.write('toto')",  # line = 4
            "sys.stdout.writelines(['toto', 'titi'])",  # line = 5
            "sys.stderr.writelines(['toto', 'titi'])",  # line = 6
        ],
    ):
        for test_file in [
            "toto1.py",
            "toto2.py",
            "toto3.py",
            "toto4.py",
            "toto5.py",
        ]:
            res.append(
                IssueInfo(error_type, line + 1, 12, line_as_str, test_file, False)
            )
        line += 1

    return res


@pytest.fixture(scope="function")
def issues_for_blocks() -> list[IssueInfo]:
    """
    Get a list of issues to test ignored blocks.

    Returns:
        Issues to test ignored blocks.
    """
    res = []
    line = 5
    for error_type, line_as_str in zip(
        IssueEnum,
        [
            "print('toto')",  # line = 6
            "pprint('toto')",  # line = 7
            "sys.stdout.write('toto')",  # line = 8
            "sys.stderr.write('toto')",  # line = 9
            "sys.stdout.writelines(['toto', 'titi'])",  # line = 10
            "sys.stderr.writelines(['toto', 'titi'])",  # line = 11
        ],
    ):
        for test_file in [
            "toto1.py",  ## ppl001
            "toto2.py",  ## ppl002
            "toto3.py",  ## ppl003
            "toto4.py",  ## ppl004
            "toto5.py",  ## ppl005
            "toto6.py",  ## ppl006
            "toto_all.py",  ## all
        ]:
            res.append(
                IssueInfo(error_type, line + 1, 12, line_as_str, test_file, False)
            )
        line += 1

    return res


@pytest.fixture(scope="function")
def ignored_lines() -> list[IgnoredLine]:
    """
    Get a list of ignored lines.

    Returns:
        Ignored lines.
    """
    ppl001_lines = [2, 4, 6, 7]
    ppl002_lines = [12]
    ppl003_lines = [15, 17, 20, 21]
    ppl004_lines = [23, 24, 27, 29]
    ppl005_lines = [33, 34]
    ppl006_lines = [36, 37, 40]

    res = [IgnoredLine(line, "PPL001", "toto1.py") for line in ppl001_lines]
    res.extend([IgnoredLine(line, "PPL002", "toto2.py") for line in ppl002_lines])
    res.extend([IgnoredLine(line, "PPL003", "toto3.py") for line in ppl003_lines])
    res.extend([IgnoredLine(line, "PPL004", "toto4.py") for line in ppl004_lines])
    res.extend([IgnoredLine(line, "PPL005", "toto5.py") for line in ppl005_lines])
    res.extend([IgnoredLine(line, "PPL006", "toto6.py") for line in ppl006_lines])

    return res


@pytest.fixture(scope="function")
def ignored_files() -> list[IgnoredFile]:
    """
    Get a list of ignored files.

    Returns:
        Ignored files.
    """
    return [
        IgnoredFile("ALL", "toto1.py"),
        IgnoredFile("PPL000", "toto2.py"),
        IgnoredFile("PPL100", "toto3.py"),
        IgnoredFile("PPL002", "toto4.py"),
        IgnoredFile("PPL005", "toto5.py"),
    ]


@pytest.fixture(scope="function")
def ignored_files_and_lines() -> tuple[list[IgnoredLine], list[IgnoredFile]]:
    """
    Get a list of ignored files and lines.

    Returns:
        Ignored files and lines.
    """
    files = [
        IgnoredFile("ALL", "toto1.py"),
        IgnoredFile("PPL000", "toto2.py"),
        IgnoredFile("PPL100", "toto3.py"),
        IgnoredFile("PPL002", "toto4.py"),
    ]
    lines = [
        IgnoredLine(
            1,
            "PPL001",
            "toto1.py",
        ),
        IgnoredLine(
            1,
            "PPL001",
            "toto2.py",
        ),
        IgnoredLine(
            1,
            "PPL001",
            "toto3.py",
        ),
        IgnoredLine(
            2,
            "PPL002",
            "toto3.py",
        ),
        IgnoredLine(
            6,
            "PPL006",
            "toto4.py",
        ),
    ]
    return (lines, files)


@pytest.fixture(scope="function")
def ignored_blocks() -> list[IgnoredBlock]:
    """
    Get a list of ignored blocks.

    Returns:
        Ignored blocks.
    """
    return [
        IgnoredBlock(
            error_code="PPL001", line_from=5, line_to=12, from_file="toto1.py"
        ),
        IgnoredBlock(
            error_code="PPL002", line_from=5, line_to=12, from_file="toto2.py"
        ),
        IgnoredBlock(
            error_code="PPL003", line_from=5, line_to=12, from_file="toto3.py"
        ),
        IgnoredBlock(
            error_code="PPL004", line_from=5, line_to=12, from_file="toto4.py"
        ),
        IgnoredBlock(
            error_code="PPL005", line_from=5, line_to=12, from_file="toto5.py"
        ),
        IgnoredBlock(
            error_code="PPL006", line_from=5, line_to=12, from_file="toto6.py"
        ),
        IgnoredBlock(
            error_code="ALL", line_from=5, line_to=12, from_file="toto_all.py"
        ),
    ]
