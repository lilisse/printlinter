"""Parsing functions."""

# Standard imports
import ast
import re
import tokenize
from io import TextIOWrapper
from pathlib import Path

# Local imports
from .classes import IgnoredBlock, IgnoredFile, IgnoredLine

IGNORE_LINE_TOKEN_REGEX = r"noqa:[ ]?(?P<code>PPL[0-9]{3})"
IGNORE_NEXT_LINE_TOKEN_REGEX = r"<printlinter disable-next (?P<code>PPL[0-9]{3})>"
IGNORE_FILE_TOKEN_REGEX = r"<printlinter disable-file (?P<code>ALL|PPL[0-9]{3})>"
IGNORE_BLOCK_BEGIN_TOKEN_REGEX = r"<printlinter disable (?P<code>ALL|PPL[0-9]{3})>"
IGNORE_BLOCK_END_TOKEN_REGEX = r"<printlinter enable (?P<code>ALL|PPL[0-9]{3})>"


def enumerate_file(folder: Path) -> list[Path]:
    """
    Enumerate all files in a folder.

    Args:
        folder: Path of the folder to enumerate

    Returns:
        All file in the given folder.
    """
    return list(folder.glob("**/*.py"))


def get_ignored_lines(file: TextIOWrapper, file_path: Path) -> list[IgnoredLine]:
    """
    Get ignored lines in a file.

    Args:
        file: File to analyze.
        file_path: Path of the given file.

    Returns:
        All ignored lines in given file.
    """
    tokens = tokenize.generate_tokens(file.readline)
    ignored_lines = []

    for token in tokens:
        toktype, tokval, start, *_ = token
        if toktype == tokenize.COMMENT:
            if match := re.search(IGNORE_LINE_TOKEN_REGEX, tokval):
                lineo, _ = start
                code = match.group("code")
                ignored_lines.append(IgnoredLine(lineo, code, file_path))
            elif match := re.search(IGNORE_NEXT_LINE_TOKEN_REGEX, tokval):
                lineo, _ = start
                code = match.group("code")
                ignored_lines.append(IgnoredLine(lineo + 1, code, file_path))

    return ignored_lines


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


def get_ignored_files(file: TextIOWrapper, file_path: Path) -> list[IgnoredFile] | None:
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
                    return [IgnoredFile(code, file_path)]
                else:
                    return None
        tokens_before.append(token)

    return []


def _match_blocks(
    begin: list[tuple[int, str]],
    end: list[tuple[int, str]],
    file_path: Path,
    nb_lines: int,
) -> list[IgnoredBlock]:
    """
    Match ignored blocks of code.

    Args:
        begin: Start of ignored block of code.
        end: End of ignored block of code.
        file_path: Path of the given file.
        nb_lines: Number of lines in the file.

    Returns:
        Ignored Blocks of code in given file.
    """
    result = []

    for begin_element in begin:
        find_end = False
        for end_element in end:
            if begin_element[1] == end_element[1]:
                result.append(
                    IgnoredBlock(
                        begin_element[1], begin_element[0], end_element[0], file_path
                    )
                )
                find_end = True
                break
        if not find_end:
            result.append(
                IgnoredBlock(begin_element[1], begin_element[0], nb_lines, file_path)
            )

    return result


def get_ignored_blocks(
    file: TextIOWrapper,
    file_path: Path,
    nb_lines: int,
) -> list[IgnoredBlock]:
    """
    Get ignored blocks in a file.

    Args:
        file: File to analyze.
        file_path: Path of the given file.
        nb_lines: Number of lines in the file.

    Returns:
        Ignored Block in given file.
    """
    tokens = tokenize.generate_tokens(file.readline)
    begin = []
    end = []

    for token in tokens:
        toktype, tokval, start, *_ = token
        if toktype == tokenize.COMMENT:
            if match := re.search(IGNORE_BLOCK_BEGIN_TOKEN_REGEX, tokval):
                lineo, _ = start
                begin.append((lineo, match.group("code")))
            elif match := re.search(IGNORE_BLOCK_END_TOKEN_REGEX, tokval):
                lineo, _ = start
                end.append((lineo, match.group("code")))

    return _match_blocks(begin, end, file_path, nb_lines)


def parse_file(
    file_path: str,
    target_version: tuple[int, int],
) -> tuple[ast.AST, list[IgnoredLine], list[IgnoredFile] | None, list[IgnoredBlock]]:
    """
    Parse a file to get the tree and all ignored lines, file and blocks in this file.

    Args:
        file_path: Path of the file to parse.
        target_version: Target version for ast.

    Returns:
        The AST tree of the file and all ignored lines, files and blocks
        contains in this file.
    """
    with open(file_path, encoding="utf-8") as file:
        tree = ast.parse(
            source=file.read(),
            filename=file_path,
            feature_version=target_version,
        )
        file.seek(0)
        nb_lines = len(file.readlines()) + 1
        file.seek(0)

        ignored_lines = get_ignored_lines(file, Path(file_path))
        file.seek(0)

        ignored_files = get_ignored_files(file, Path(file_path))
        file.seek(0)

        ignored_block = get_ignored_blocks(file, Path(file_path), nb_lines)
        file.seek(0)

    return tree, ignored_lines, ignored_files, ignored_block
