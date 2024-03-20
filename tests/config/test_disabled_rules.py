# Pytest imports
import pytest
from pytest import param

# First party imports
from py_printlinter import IssueEnum, IssueInfo, get_not_ignore_issue


@pytest.mark.parametrize(
    "rule_001, expected_rule001",
    [
        param("PPL001", [], id="disable PPL001"),
        param(
            None,
            IssueInfo(
                IssueEnum.PRINTDETECT,
                1,
                1,
                "print('toto')",
                "toto1.py",
                False,
            ),
            id="no disable PPL001",
        ),
    ],
)
@pytest.mark.parametrize(
    "rule_002, expected_rule002",
    [
        param("PPL002", [], id="disable PPL002"),
        param(
            None,
            IssueInfo(
                IssueEnum.PRETTYPRINTDETECT,
                2,
                2,
                "pprint('toto')",
                "toto2.py",
                False,
            ),
            id="no disable PPL002",
        ),
    ],
)
@pytest.mark.parametrize(
    "rule_003, expected_rule003",
    [
        param("PPL003", [], id="disable PPL003"),
        param(
            None,
            IssueInfo(
                IssueEnum.SYSSTDOUTWRITEDETECT,
                3,
                3,
                "sys.stdout.write('toto')",
                "toto3.py",
                False,
            ),
            id="no disable PPL003",
        ),
    ],
)
@pytest.mark.parametrize(
    "rule_004, expected_rule004",
    [
        param("PPL004", [], id="disable PPL004"),
        param(
            None,
            IssueInfo(
                IssueEnum.SYSSTDERRWRITEDETECT,
                4,
                4,
                "sys.stderr.write('toto')",
                "toto4.py",
                False,
            ),
            id="no disable PPL004",
        ),
    ],
)
@pytest.mark.parametrize(
    "rule_005, expected_rule005",
    [
        param("PPL005", [], id="disable PPL005"),
        param(
            None,
            IssueInfo(
                IssueEnum.SYSSTDOUTWRITELINESDETECT,
                5,
                5,
                "sys.stdout.writelines('toto')",
                "toto5.py",
                False,
            ),
            id="no disable PPL005",
        ),
    ],
)
@pytest.mark.parametrize(
    "rule_006, expected_rule006",
    [
        param("PPL006", [], id="disable PPL006"),
        param(
            None,
            IssueInfo(
                IssueEnum.SYSSTDERRWRITELINESDETECT,
                6,
                6,
                "sys.stderr.writelines('toto')",
                "toto6.py",
                False,
            ),
            id="no disable PPL006",
        ),
    ],
)
def test_get_not_ignore_issue_with_disabled_rules(
    testing_files,
    rule_001,
    rule_002,
    rule_003,
    rule_004,
    rule_005,
    rule_006,
    expected_rule001,
    expected_rule002,
    expected_rule003,
    expected_rule004,
    expected_rule005,
    expected_rule006,
):
    disabled_rules = [
        rule
        for rule in [rule_001, rule_002, rule_003, rule_004, rule_005, rule_006]
        if rule is not None
    ]

    issues = [
        IssueInfo(
            IssueEnum.PRINTDETECT,
            1,
            1,
            "print('toto')",
            "toto1.py",
            False,
        ),
        IssueInfo(
            IssueEnum.PRETTYPRINTDETECT,
            2,
            2,
            "pprint('toto')",
            "toto2.py",
            False,
        ),
        IssueInfo(
            IssueEnum.SYSSTDOUTWRITEDETECT,
            3,
            3,
            "sys.stdout.write('toto')",
            "toto3.py",
            False,
        ),
        IssueInfo(
            IssueEnum.SYSSTDERRWRITEDETECT,
            4,
            4,
            "sys.stderr.write('toto')",
            "toto4.py",
            False,
        ),
        IssueInfo(
            IssueEnum.SYSSTDOUTWRITELINESDETECT,
            5,
            5,
            "sys.stdout.writelines('toto')",
            "toto5.py",
            False,
        ),
        IssueInfo(
            IssueEnum.SYSSTDERRWRITELINESDETECT,
            6,
            6,
            "sys.stderr.writelines('toto')",
            "toto6.py",
            False,
        ),
    ]

    assert get_not_ignore_issue(
        issues,
        [],
        [],
        disabled_rules,
    ) == [
        expect_rule
        for expect_rule in [
            expected_rule001,
            expected_rule002,
            expected_rule003,
            expected_rule004,
            expected_rule005,
            expected_rule006,
        ]
        if expect_rule
    ]
