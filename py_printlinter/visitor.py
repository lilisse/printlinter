"""Visitor functions."""

# Standard imports
import ast
from itertools import product
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


def get_display_func_or_none(node: ast.Expr) -> str | None:
    """
    Get a display function in a ast.Expr.

    Function detected by this one:
        - sys.stdout.write()
        - stdout.write()
        - sys.stderr.write()
        - stderr.write()
        - sys.stdout.writelines()
        - stdout.writelines()
        - sys.stderr.writelines()
        - stderr.writelines()

    Args:
        node: Expr to parse may can contains one of function we search.

    Returns:
        The function name if we find a function of the list, None otherwizse.
    """
    std_output = ["stdout", "stderr"]
    std_function = ["write", "writelines"]

    for res in product(std_output, std_function):
        output = res[0]
        funct = res[1]
        # Detect:
        # - sys.stdout.write
        # - sys.stderr.write
        # - sys.stdout.writelines
        # - sys.stderr.writelines
        try:
            if (
                node.value.func.value.value.id == "sys"  # type: ignore[attr-defined]
                and node.value.func.value.attr == output  # type: ignore[attr-defined]
                and node.value.func.attr == funct  # type: ignore[attr-defined]
            ):
                return f"sys.{output}.{funct}"
        except AttributeError as err:  # noqa: F841 <Only used for debug>
            pass

        # Detect:
        # - stdout.write
        # - stderr.write
        # - stdout.writelines
        # - stderr.writelines
        try:
            if (
                node.value.func.value.id == output  # type: ignore[attr-defined]
                and node.value.func.attr == funct  # type: ignore[attr-defined]
            ):
                return f"{output}.{funct}"
        except AttributeError as err:  # noqa: F841 <Only used for debug>
            pass

    return None


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
            case None:
                # Function not directly call like: `sys.stdout.write`
                detected_func_or_none = get_display_func_or_none(node)
                match detected_func_or_none:
                    case "sys.stdout.write" | "stdout.write":
                        issue_type = IssueEnum.SYSSTDOUTWRITEDETECT
                    case "sys.stderr.write" | "stderr.write":
                        issue_type = IssueEnum.SYSSTDERRWRITEDETECT
                    case "sys.stdout.writelines" | "stdout.writelines":
                        issue_type = IssueEnum.SYSSTDOUTWRITELINESDETECT
                    case "sys.stderr.writelines" | "stderr.writelines":
                        issue_type = IssueEnum.SYSSTDERRWRITELINESDETECT
                    case _:
                        return None
            case _:
                # Function we wish to ignore
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
