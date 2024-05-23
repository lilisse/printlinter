# Pytest imports
import pytest

# Standard imports
import ast
from itertools import zip_longest


@pytest.fixture()
def file_without_ignored_print(testing_files):
    with open(testing_files / "print/toto_1.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_without_ignored_prettyprint(testing_files):
    with open(testing_files / "pprint/pprint1.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_without_ignored_stdout_write(testing_files):
    with open(testing_files / "sys/stdout/write/stdout1.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_without_ignored_stderr_write(testing_files):
    with open(testing_files / "sys/stderr/write/stderr1.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_without_ignored_stdout_writelines(testing_files):
    with open(
        testing_files / "sys/stdout/writelines/stdout1.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_without_ignored_stderr_writelines(testing_files):
    with open(
        testing_files / "sys/stderr/writelines/stderr1.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_print(testing_files):
    with open(testing_files / "print/toto2/toto3.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_prettyprint(testing_files):
    with open(testing_files / "pprint/pprint2/pprint3.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stdout_write(testing_files):
    with open(
        testing_files / "sys/stdout/write/stdout2/stdout3.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stderr_write(testing_files):
    with open(
        testing_files / "sys/stderr/write/stderr2/stderr3.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stdout_writelines(testing_files):
    with open(
        testing_files / "sys/stdout/writelines/stdout2/stdout3.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stderr_writelines(testing_files):
    with open(
        testing_files / "sys/stderr/writelines/stderr2/stderr3.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stderr_writelines(testing_files):
    with open(
        testing_files / "sys/stderr/writelines/stderr2/stderr3.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_without_ignored_file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_nothing.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_all(testing_files):
    with open(testing_files / "ignored_files/ignore_all.py", encoding="utf-8") as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_standard_lib(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl000.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_print__file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl001.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_prettyprint__file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl002.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stdout_write__file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl003.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stderr_write__file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl004.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stdout_writelines__file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl005.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_stderr_writelines__file(testing_files):
    with open(
        testing_files / "ignored_files/ignore_ppl006.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_comment_in_wrong_place__file(testing_files):
    with open(
        testing_files / "ignored_files/disable_in_wrong_place.py", encoding="utf-8"
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_comment_not_at_first_line__file(testing_files):
    with open(
        testing_files / "ignored_files/disable_valid_but_not_in_first_line.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_next_print(testing_files):
    with open(
        testing_files / "ignored_next_line/ppl001.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_next_pprint(testing_files):
    with open(
        testing_files / "ignored_next_line/ppl002.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_next_stdout_write(testing_files):
    with open(
        testing_files / "ignored_next_line/ppl003.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_next_stderr_write(testing_files):
    with open(
        testing_files / "ignored_next_line/ppl004.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_next_stdout_writelines(testing_files):
    with open(
        testing_files / "ignored_next_line/ppl005.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_next_stderr_writelines(testing_files):
    with open(
        testing_files / "ignored_next_line/ppl006.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_nothing(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ignore_nothing.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_print__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ppl001.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_pprint__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ppl002.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stdout_write__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ppl003.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stderr_write__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ppl004.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stdout_writelines__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ppl005.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stderr_writelines__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/ppl006.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_all__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/all.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_mix__re_enable(testing_files):
    with open(
        testing_files / "ignored_block/re_enable/mix.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_print__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/ppl001.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_pprint__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/ppl002.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stdout_write__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/ppl003.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stderr_write__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/ppl004.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stdout_writelines__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/ppl005.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_stderr_writelines__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/ppl006.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_all__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/all.py",
        encoding="utf-8",
    ) as file:
        file.seek(0)
        yield file


@pytest.fixture()
def file_with_ignored_block_mix__no_re_enable(testing_files):
    with open(
        testing_files / "ignored_block/no_re_enable/mix.py",
        encoding="utf-8",
    ) as file:
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
