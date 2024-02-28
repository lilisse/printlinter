"""Visitor functions."""

# Standard imports
import ast
from linecache import getline
from pathlib import Path
from typing import Any, cast

# Local imports
from .classes import IssueEnum, IssueInfo


def get_attr(obj: object, name: str, default: Any | None = None) -> Any:  # noqa: ANN401
    """
    Get attribute of an object.

    The function is a implementation of `dict().get` for any object.

    Args:
        obj: Object from which we want the given attribute.
        name: Attribute we want.
        default: Default value return if the object don't have the attribute.

    Returns:
        Value of the attribute if the object have it, the default otherwise.

    Examples:
        >>> from dataclasses import dataclass
        >>> @dataclass
        >>> class Toto():
        ...     titi: int
        ...     tutu: int | None = None

        >>> toto = Toto(titi = 1, tutu = 2)
        >>> get_attr(toto, "titi")
        1
        >>> get_attr(toto, "tutu")
        2

        >>> toto2 = Toto(titi = 1)
        >>> get_attr(toto2, "titi")
        1
        >>> get_attr(toto2, "tutu")
        None
        >>> get_attr(toto2, "foo")
        None
        >>> get_attr(toto2, "foo", 3)
        3
    """
    if hasattr(obj, name):
        return getattr(obj, name)

    return default


class PrintNodeVisitor(ast.NodeVisitor):
    """
    Print visitor class.

    Attributes:
        found_prints: All issues for print found.

    """

    found_prints: list[IssueInfo] = []

    def visit_Expr(self, node: ast.Expr) -> None:  # noqa: N802
        """
        Visitor expression method.

        Args:
            node: Node to visit.

        Returns:
            Issue if we find one, otherwise return None.
        """
        if not isinstance(node.value, ast.Call):  # pragma: no cover
            return None

        func = node.value.func
        match get_attr(func, "id", None):
            case "print":
                issue_type = IssueEnum.PRINTDETECT
            case "pprint":
                issue_type = IssueEnum.PRETTYPRINTDETECT
            case _:
                return None

        found_print = IssueInfo(
            issue_type,
            node.lineno,
            node.col_offset,
            line_as_str=None,
            from_file=None,
            ignore=False,
        )
        self.found_prints.append(cast(IssueInfo, found_print))

        return None


def _add_file_info(node_visitor: PrintNodeVisitor, file_path: Path) -> None:
    """
    Add information of file in issues.

    Args:
        node_visitor: Node visitor.
        file_path: Path of the file that we are analyzing.
    """
    for i in range(len(node_visitor.found_prints)):
        if node_visitor.found_prints[i].from_file is None:
            node_visitor.found_prints[i].from_file = file_path
            node_visitor.found_prints[i].line_as_str = getline(
                str(file_path),
                node_visitor.found_prints[i].num_line,
            ).strip()


def contains_print(file_path: Path, tree: ast.AST) -> list[IssueInfo]:
    """
    Detect if a given file contains print.

    Args:
        file_path: Path of the given file.
        tree: AST of the file.

    Returns:
        All print found.
    """
    node_visitor = PrintNodeVisitor()
    node_visitor.visit(tree)
    _add_file_info(node_visitor, file_path)
    return node_visitor.found_prints
