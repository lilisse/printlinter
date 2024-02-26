# Pytest imports
import pytest

# Standard imports
import ast
from io import TextIOWrapper
from itertools import zip_longest
from pathlib import Path
from typing import Union

# First party imports
from py_printlinter import IgnoreLine, IssueEnum, IssueInfo


def issues() -> list[IssueInfo]:
    """
    Get a list of issues.

    Returns:
        Issues.
    """
    return [
        IssueInfo(IssueEnum.PRINTDETECT, line, 12, "print('toto')", "toto.py", False)
        for line in range(15)
    ]


def ignored_lines() -> list[IgnoreLine]:
    """
    Get a list of ignored lines.

    Returns:
        Ignored lines.
    """
    lines = [4, 6, 2, 7, 12]

    return [IgnoreLine(line, "PPL001", "toto.py") for line in lines]


def get_file(path: Path) -> TextIOWrapper:
    """
    Get file form his path.

    Returns:
        Wrapper of the file.
    """
    file = open(path, encoding="utf-8")
    file.seek(0)
    return file


@pytest.fixture()
def file_without_ignored(testing_files):
    with open(testing_files / "toto_1.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored(testing_files):
    with open(testing_files / "toto2/toto3.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


def compare_ast(
    node1: ast.expr | list[ast.expr],
    node2: ast.expr | list[ast.expr],
) -> bool:
    if type(node1) is not type(node2):
        return False

    if isinstance(node1, ast.AST):
        for k, v in vars(node1).items():
            if k in {"lineno", "end_lineno", "col_offset", "end_col_offset", "ctx"}:
                continue
            if not compare_ast(v, getattr(node2, k)):
                return False
        return True

    elif isinstance(node1, list) and isinstance(node2, list):
        return all(compare_ast(n1, n2) for n1, n2 in zip_longest(node1, node2))
    else:
        return node1 == node2
