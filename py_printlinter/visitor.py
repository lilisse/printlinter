"""Visitor functions."""

# Standard imports
import ast
from linecache import getline
from pathlib import Path
from typing import cast

# Local imports
from .classes import IssueEnum, IssueInfo


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
        if hasattr(func, "id") and func.id == "print":  # type: ignore[attr-defined]
            found_print = IssueInfo(
                IssueEnum.PRINTDETECT,
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
