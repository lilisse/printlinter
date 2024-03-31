"""Parsing functions."""

# Standard imports
import ast
import re
import tokenize
from io import TextIOWrapper
from pathlib import Path

# Local imports
from .classes import IgnoreFile, IgnoreLine

IGNORE_LINE_TOKEN_REGEX = r"noqa:[ ]?(?P<code>PPL[0-9]{3})"
IGNORE_NEXT_LINE_TOKEN_REGEX = r"<py-printlinter disable-next (?P<code>PPL[0-9]{3})>"
IGNORE_FILE_TOKEN_REGEX = r"<py-printlinter disable-file (?P<code>ALL|PPL[0-9]{3})>"


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
            if match := re.search(IGNORE_LINE_TOKEN_REGEX, tokval):
                lineo, _ = start
                code = match.group("code")
                ignore_lines.append(IgnoreLine(lineo, code, file_path))
            elif match := re.search(IGNORE_NEXT_LINE_TOKEN_REGEX, tokval):
                lineo, _ = start
                code = match.group("code")
                ignore_lines.append(IgnoreLine(lineo + 1, code, file_path))

    return ignore_lines


def _no_code_before(
    tokens_before: list[tokenize.TokenInfo],
) -> bool:
    """
    Check if we have code in token before a specific token.

    Args:
        tokens_before: Token in file before the specific token.

    Returns:
        True if we have not code tokens in the given tokens, False otherwise.
    """
    for token in tokens_before:
        toktype, *_ = token
        if toktype not in [
            tokenize.COMMENT,
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.ENCODING,
            tokenize.NL,
        ]:
            return False

    return True


def get_ignore_files(file: TextIOWrapper, file_path: Path) -> list[IgnoreFile] | None:
    """
    Get ignored files in a file.

    Args:
        file: File to analyze.
        file_path: Path of the given file.

    Returns:
        Ignored File in given file.
    """
    tokens = tokenize.generate_tokens(file.readline)
    tokens_before: list[tokenize.TokenInfo] = []

    for token in tokens:
        toktype, tokval, *_ = token
        if toktype == tokenize.COMMENT:
            if match := re.search(IGNORE_FILE_TOKEN_REGEX, tokval):
                if _no_code_before(tokens_before):
                    code = match.group("code")
                    return [IgnoreFile(code, file_path)]
                else:
                    return None
        tokens_before.append(token)

    return []


def parse_file(
    file_path: str,
    target_version: tuple[int, int],
) -> tuple[ast.AST, list[IgnoreLine], list[IgnoreFile] | None]:
    """
    Parse a file to get the tree and all ignore lines in this file.

    Args:
        file_path: Path of the file to parse.
        target_version: Target version for ast.

    Returns:
        The AST tree of the file and all ignored lines contains in this file.
    """
    with open(file_path, encoding="utf-8") as file:
        tree = ast.parse(
            source=file.read(),
            filename=file_path,
            feature_version=target_version,
        )
        file.seek(0)

        ignore_lines = get_ignore_lines(file, Path(file_path))
        file.seek(0)

        ignore_files = get_ignore_files(file, Path(file_path))
        file.seek(0)

    return tree, ignore_lines, ignore_files
