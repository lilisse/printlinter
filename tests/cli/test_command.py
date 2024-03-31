# Pytest imports
import pytest
from pytest import param

# Standard imports
from os import getcwd
from pathlib import Path

# Third party imports
from assertpy import assert_that, soft_assertions
from typer.testing import CliRunner

# First party imports
from cli_app import APP
from printlinter import __app_name__ as ppl_name
from printlinter import __version__ as ppl_version

# Local imports
from ..config.conftest import change_cwd

runner = CliRunner()


def test_cli_version():
    result = runner.invoke(APP, ["--version"])
    print(result)
    with soft_assertions():
        assert_that(result.exit_code).is_equal_to(0)
        assert_that(result.stdout).contains(f"{ppl_name} v.{ppl_version}")


@pytest.mark.parametrize(
    "path, expected_exit_code",
    [
        param("azerty.qwerty", 1, id="file not found error"),
        param("README.md", 1, id="not a python file"),
        param("print/toto0.py", 1, id="file"),
        param("print/toto4", 0, id="no errors, no print"),
        param("print/toto2", 0, id="print detected on folder"),
        param("print/toto2/toto3.py", 0, id="print detected on file"),
        param("pprint/pprint2", 0, id="pprint detected with ignored file in config"),
        param("ignored_files", 0, id="ignore file with warning"),
    ],
)
def test_cli_command_lint_w_path(
    pnv_soft_reset,
    testing_files,
    path,
    expected_exit_code,
):
    result = runner.invoke(
        APP,
        [
            "lint",
            f"{testing_files / path}",
            "--config-file",
            f"{Path(__file__).parent / 'config.yml'}",
        ],
    )

    assert_that(result.exit_code).is_equal_to(expected_exit_code)


def test_cli_on_default_ignored_rep(pnv_soft_reset, testing_files):
    result = runner.invoke(APP, ["lint", f"{testing_files}/config/ignored_rep"])

    with soft_assertions():
        assert_that(result.exit_code).is_equal_to(0)
        assert_that(result.stdout).contains("Found 1 errors")
