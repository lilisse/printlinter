# Pytest imports
import pytest

# First party imports
from printlinter import IgnoreFile, IgnoreLine, IssueEnum, IssueInfo


@pytest.fixture(scope="function")
def issues_for_lines() -> list[IssueInfo]:
    """
    Get a list of issues.

    Returns:
        Issues.
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
    Get a list of issues.

    Returns:
        Issues.
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
    Get a list of issues.

    Returns:
        Issues.
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
def ignored_lines() -> list[IgnoreLine]:
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

    res = [IgnoreLine(line, "PPL001", "toto1.py") for line in ppl001_lines]
    res.extend([IgnoreLine(line, "PPL002", "toto2.py") for line in ppl002_lines])
    res.extend([IgnoreLine(line, "PPL003", "toto3.py") for line in ppl003_lines])
    res.extend([IgnoreLine(line, "PPL004", "toto4.py") for line in ppl004_lines])
    res.extend([IgnoreLine(line, "PPL005", "toto5.py") for line in ppl005_lines])
    res.extend([IgnoreLine(line, "PPL006", "toto6.py") for line in ppl006_lines])

    return res


@pytest.fixture(scope="function")
def ignored_files() -> list[IgnoreFile]:
    return [
        IgnoreFile("ALL", "toto1.py"),
        IgnoreFile("PPL000", "toto2.py"),
        IgnoreFile("PPL100", "toto3.py"),
        IgnoreFile("PPL002", "toto4.py"),
        IgnoreFile("PPL005", "toto5.py"),
    ]


@pytest.fixture(scope="function")
def ignored_files_and_lines() -> tuple[list[IgnoreLine], list[IgnoreFile]]:
    files = [
        IgnoreFile("ALL", "toto1.py"),
        IgnoreFile("PPL000", "toto2.py"),
        IgnoreFile("PPL100", "toto3.py"),
        IgnoreFile("PPL002", "toto4.py"),
    ]
    lines = [
        IgnoreLine(
            1,
            "PPL001",
            "toto1.py",
        ),
        IgnoreLine(
            1,
            "PPL001",
            "toto2.py",
        ),
        IgnoreLine(
            1,
            "PPL001",
            "toto3.py",
        ),
        IgnoreLine(
            2,
            "PPL002",
            "toto3.py",
        ),
        IgnoreLine(
            6,
            "PPL006",
            "toto4.py",
        ),
    ]
    return (lines, files)
