# Third party imports
from pytest_bdd import scenario

# Local imports
from .utils_bdd import *


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and ignore inline",
)
def test_lint_an_existing_file_with_print_with_ignore_inline(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and ignore block",
)
def test_lint_an_existing_file_with_print_with_ignore_block(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and ignore file",
)
def test_lint_an_existing_file_with_print_with_ignore_file(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and ignore next line",
)
def test_lint_an_existing_file_with_print_with_ignore_next_line(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print without ignore",
)
def test_lint_an_existing_file_with_print_without_ignore_inline(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and a default full config file",
)
def test_lint_an_existing_file_with_print_and_default_full_config_file(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and a default partial config file",
)
def test_lint_an_existing_file_with_print_and_default_partial_config_file(
    pnv_soft_reset,
):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and a custom full config file",
)
def test_lint_an_existing_file_with_print_and_custom_full_config_file(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file with print and a custom partial config file",
)
def test_lint_an_existing_file_with_print_and_custom_partial_config_file(
    pnv_soft_reset,
):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing file without print",
)
def test_lint_an_existing_file_without_print(pnv_soft_reset):
    pass


@scenario("../scenarios/lint.feature", "Lint a file doesn't exist")
def test_lint_a_file_does_not_exist(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and ignore inline",
)
def test_lint_an_existing_folder_with_print_with_ignore_inline(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and ignore block",
)
def test_lint_an_existing_folder_with_print_with_ignore_block(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and ignore file",
)
def test_lint_an_existing_folder_with_print_with_ignore_file(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and ignore next line",
)
def test_lint_an_existing_folder_with_print_with_ignore_next_line(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print without ignore",
)
def test_lint_an_existing_folder_with_print_without_ignore_inline(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and a default full config file",
)
def test_lint_an_existing_folder_with_print_and_default_full_config_file(
    pnv_soft_reset,
):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and a default partial config file",
)
def test_lint_an_existing_folder_with_print_and_default_partial_config_file(
    pnv_soft_reset,
):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and a custom full config file",
)
def test_lint_an_existing_folder_with_print_and_custom_full_config_file(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder with print and a custom partial config file",
)
def test_lint_an_existing_folder_with_print_and_custom_partial_config_file(
    pnv_soft_reset,
):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint an existing folder without print",
)
def test_lint_an_existing_folder_without_print(pnv_soft_reset):
    pass


@scenario("../scenarios/lint.feature", "Lint a folder doesn't exist")
def test_lint_a_folder_does_not_exist(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint the current work directory with print and ignore inline",
)
def test_lint_the_current_work_with_print_with_ignore_inline(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint the current work directory with print and ignore block",
)
def test_lint_the_current_work_with_print_with_ignore_block(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint the current work directory with print and ignore file",
)
def test_lint_the_current_work_with_print_with_ignore_file(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint the current work directory with print and ignore next line",
)
def test_lint_the_current_work_with_print_with_ignore_next_line(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint the current work directory with print without ignore",
)
def test_lint_the_current_work_with_print_without_ignore_inline(pnv_soft_reset):
    pass


@scenario(
    "../scenarios/lint.feature",
    "Lint the current work directory without print",
)
def test_lint_the_current_work_without_print(pnv_soft_reset):
    pass
