"""Parsing functions."""

# Standard imports
import ast
import re
import tokenize
from io import TextIOWrapper
from pathlib import Path

# Local imports
from .classes import IgnoreLine

# TODO: enlever le droit d'ignorer plusieurs erreur sur une ligne
IGNORE_TOKEN_REGEX = r"noqa:[ ]?((PPL[0-9]{3},? ?)+)"


def enumerate_file(folder: Path) -> list[Path]:
    """
    Enumerate all files in a folder.

    Args:
        folder: Path of the folder to enumerate

    Returns:
        All file in the given folder.
    """
    return list(folder.glob("**/*.py"))


def get_ignore_lines(file: TextIOWrapper, file_path: Path) -> list[IgnoreLine]:
    """
    Get ignored lines in a file.

    Args:
        file: File to analyze.
        file_path: Path of the given file.

    Returns:
        All ignored lines in given file.
    """
    tokens = tokenize.generate_tokens(file.readline)
    ignore_lines = []

    for token in tokens:
        toktype, tokval, start, *_ = token
        if toktype == tokenize.COMMENT:
            if match := re.search(IGNORE_TOKEN_REGEX, tokval):
                lineo, _ = start
                codes = match.group().strip("noqa: ").split(", ")
                ignore_lines.extend(
                    [IgnoreLine(lineo, code, file_path) for code in codes]
                )

    return ignore_lines


def parse_file(file_path: str) -> tuple[ast.AST, list[IgnoreLine]]:
    """
    Parse a file to get the tree and all ignore lines in this file.

    Args:
        file_path: Path of the file to parse.

    Returns:
        The AST tree of the file and all ignored lines contains in this file.
    """
    with open(file_path, encoding="utf-8") as file:
        tree = ast.parse(
            source=file.read(),
            filename=file_path,
            feature_version=(3, 11),
        )

        file.seek(0)

        ignore_lines = get_ignore_lines(file, Path(file_path))

    return tree, ignore_lines
