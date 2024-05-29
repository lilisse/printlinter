# Pytest imports
import pytest

# Standard imports
from os import chdir, getcwd
from pathlib import Path

# Third party imports
from pytest_bdd import given, parsers, then, when
from typer.testing import CliRunner

# First party imports
from cli_app import APP

# Local imports
from ...conftest import INPUT_FILE_PATH
from .conftest import ConfigContent as cC
from .conftest import ConfigType as cT
from .conftest import IgnoreType as iT
from .conftest import TargetType as tT

LOCAL_INPUT_FILE_PATH = INPUT_FILE_PATH / "bdd/input"
LOCAL_CONFIG_FILE_PATH = INPUT_FILE_PATH / "bdd/config"
RUNNER = CliRunner()


@pytest.fixture
def arg_type():
    return ""


@given(parsers.parse("I want lint {arg}"))
def i_lint(arg, cmd_args, path_selector):
    cmd_args.append("lint")
    match arg:
        case "a file":
            path_selector.type = tT.FILE
        case "a folder":
            path_selector.type = tT.FOLDER
        case "the current work directory":
            path_selector.type = tT.CWD
            path_selector.exist = True


@given(parsers.parse("That {arg}"))
def it_exist(arg, path_selector):
    match arg:
        case "does not exist":
            path_selector.exist = False
        case "exist":
            path_selector.exist = True


@given(parsers.parse("{arg} print"))
def contains_print(arg, path_selector):
    match arg:
        case "Contains":
            path_selector.contains_print = True
        case "Does not contains":
            path_selector.contains_print = False


@given(parsers.parse("{arg_contains} ignore {arg_type}"))
@given(parsers.parse("{arg_contains} ignore"))
def contains_ignore(arg_contains, arg_type, path_selector):
    match arg_contains:
        case "Does not contains":
            path_selector.ignore = iT.NO
        case "Contains":
            match arg_type:
                case "inline":
                    path_selector.ignore = iT.INLINE
                case "block":
                    path_selector.ignore = iT.BLOCK
                case "file":
                    path_selector.ignore = iT.FILE
                case "next line":
                    path_selector.ignore = iT.NEXT


@given(parsers.parse("take a {type_arg} {content_arg} config file"))
def config_file(type_arg, content_arg, path_selector):
    match type_arg:
        case "default":
            path_selector.config_type = cT.DEFAULT
        case "custom":
            path_selector.config_type = cT.CUSTOM

    match content_arg:
        case "full":
            path_selector.config_content = cC.FULL
        case "partial":
            path_selector.config_content = cC.PARTIAL


def _get_input_path(path_selector) -> Path:
    ps = path_selector
    path = LOCAL_INPUT_FILE_PATH

    if not ps.exist:
        path /= "z_file.py" if ps.type == tT.FILE else "z_folder"
        return path

    match ps.contains_print:
        case True:
            path /= "with_print"
        case False:
            path /= "without_print"
        case None:
            pass

    match ps.ignore:
        case iT.INLINE:
            path /= "with_ignore_inline"
        case iT.BLOCK:
            path /= "with_ignore_block"
        case iT.FILE:
            path /= "with_ignore_file"
        case iT.NEXT:
            path /= "with_ignore_next_line"
        case iT.NO:
            path /= "without_ignore"
        case None:
            pass

    match ps.type:
        case tT.FILE:
            path /= "a_file.py"
        case tT.FOLDER | tT.CWD:
            path /= "a_folder"

    return path


def _get_config_file(path_selector) -> Path:
    ps = path_selector
    path = LOCAL_CONFIG_FILE_PATH

    match ps.config_content:
        case cC.FULL:
            path /= "full"
        case cC.PARTIAL:
            path /= "partial"

    if ps.config_type == cT.CUSTOM:
        path /= "custom.yaml"

    return path


@when("I launch the linter", target_fixture="launch")
def launch(cmd_args, path_selector):
    path_selector.validate()

    # Fix new cwd to the current cwd, if we need to change we change it in a case.
    new_cwd = getcwd()

    input_path = _get_input_path(path_selector)

    if path_selector.type == tT.CWD:
        new_cwd = input_path
    else:
        cmd_args.append(str(input_path))

        if path_selector.config_type is not None:
            config_path = _get_config_file(path_selector)

            if path_selector.config_type == cT.DEFAULT:
                new_cwd = config_path
            else:
                cmd_args.extend(["--config-file", str(config_path)])

    old_cwd = getcwd()
    chdir(new_cwd)

    result = RUNNER.invoke(
        APP,
        args=cmd_args,
    )

    chdir(old_cwd)

    return result


@then(parsers.parse("The linter end {arg} error"))
def finish(arg, launch):
    match arg:
        case "without":
            assert launch.exit_code == 0
        case "with an":
            assert launch.exit_code > 0


@then(parsers.parse("{arg} errors have been found"))
def found_errors(arg, launch):
    assert f"Found {arg} errors" in launch.stdout
