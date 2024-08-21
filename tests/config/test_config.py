# Pytest imports
import pytest
from pytest import param

# Standard imports
from os import getcwd
from pathlib import Path

# Third party imports
from assertpy import assert_that, soft_assertions

# First party imports
from printlinter import DEFAULT_IGNORED_REP, Config

# Local imports
from ..conftest import INPUT_FILE_PATH
from .conftest import change_cwd

TESTING_FILES_PATH = INPUT_FILE_PATH / "config/"


@pytest.mark.parametrize(
    "given_file, expect_target_version, expect_ignored_files, expect_disabled_rules, expect_color",
    [
        # full config
        param(
            "full_config/config.yml",
            (3, 10),
            ["toto.py"],
            ["PPL001"],
            True,
            id="yml file",
        ),
        param(
            "full_config/config.yaml",
            (3, 9),
            ["titi.py"],
            ["PPL002"],
            False,
            id="yaml file",
        ),
        param(
            "full_config/config.json",
            (3, 8),
            ["tutu.py"],
            ["PPL003"],
            True,
            id="json file",
        ),
        param(
            "full_config/config.toml",
            (3, 7),
            ["tata.py"],
            ["PPL004"],
            False,
            id="toml file",
        ),
        # partial config
        param(
            "partial_config/yml/only_tv.yml",
            (3, 10),
            [],
            [],
            True,
            id="partial yml file, only target_version",
        ),
        param(
            "partial_config/yml/only_ig.yml",
            (3, 10),
            ["toto.py"],
            [],
            True,
            id="partial yml file, only ignored_files",
        ),
        param(
            "partial_config/yml/only_dr.yml",
            (3, 10),
            [],
            ["PPL001"],
            True,
            id="partial yml file, only disabled_rules",
        ),
        param(
            "partial_config/yml/only_col.yml",
            (3, 10),
            [],
            [],
            False,
            id="partial yml file, only color",
        ),
        param(
            "partial_config/yml/tv_and_if.yml",
            (3, 10),
            ["toto.py"],
            [],
            True,
            id="partial yml file, target_version and ignored_files",
        ),
        param(
            "partial_config/yml/tv_and_dr.yml",
            (3, 10),
            [],
            ["PPL001"],
            True,
            id="partial yml file, target_version and disabled rules",
        ),
        param(
            "partial_config/yml/if_and_dr.yml",
            (3, 10),
            ["toto.py"],
            ["PPL001"],
            True,
            id="partial yml file, ignored_files and disabled_rules",
        ),
        param(
            "partial_config/yml/tv_and_col.yml",
            (3, 10),
            [],
            [],
            False,
            id="partial yml file, target_version and color",
        ),
        param(
            "partial_config/yml/tv_if_and_col.yml",
            (3, 10),
            ["toto.py"],
            [],
            False,
            id="partial yml file, target_version, ignored_files and color",
        ),
        param(
            "partial_config/yaml/only_tv.yaml",
            (3, 9),
            [],
            [],
            True,
            id="partial yaml file, only target_version",
        ),
        param(
            "partial_config/yaml/only_ig.yaml",
            (3, 10),
            ["titi.py"],
            [],
            True,
            id="partial yaml file, only ignored_files",
        ),
        param(
            "partial_config/yaml/only_dr.yaml",
            (3, 10),
            [],
            ["PPL002"],
            True,
            id="partial yaml file, only disabled_rules",
        ),
        param(
            "partial_config/yaml/only_col.yaml",
            (3, 10),
            [],
            [],
            False,
            id="partial yaml file, only color",
        ),
        param(
            "partial_config/yaml/tv_and_if.yaml",
            (3, 9),
            ["titi.py"],
            [],
            True,
            id="partial yaml file, target_version and ignored_files",
        ),
        param(
            "partial_config/yaml/tv_and_dr.yaml",
            (3, 9),
            [],
            ["PPL002"],
            True,
            id="partial yaml file, target_version and disabled rules",
        ),
        param(
            "partial_config/yaml/if_and_dr.yaml",
            (3, 10),
            ["titi.py"],
            ["PPL002"],
            True,
            id="partial yaml file, ignored_files and disabled_rules",
        ),
        param(
            "partial_config/yaml/tv_and_col.yaml",
            (3, 9),
            [],
            [],
            False,
            id="partial yaml file, target_version and color",
        ),
        param(
            "partial_config/yaml/tv_if_and_col.yaml",
            (3, 9),
            ["titi.py"],
            [],
            False,
            id="partial yaml file, target_version, ignored_files and color",
        ),
        param(
            "partial_config/json/only_tv.json",
            (3, 8),
            [],
            [],
            True,
            id="partial json file, only target_version",
        ),
        param(
            "partial_config/json/only_ig.json",
            (3, 10),
            ["tutu.py"],
            [],
            True,
            id="partial json file, only ignored_files",
        ),
        param(
            "partial_config/json/only_dr.json",
            (3, 10),
            [],
            ["PPL003"],
            True,
            id="partial json file, only disabled_rules",
        ),
        param(
            "partial_config/json/only_col.json",
            (3, 10),
            [],
            [],
            False,
            id="partial json file, only color",
        ),
        param(
            "partial_config/json/tv_and_if.json",
            (3, 8),
            ["tutu.py"],
            [],
            True,
            id="partial json file, target_version and ignored_files",
        ),
        param(
            "partial_config/json/tv_and_dr.json",
            (3, 8),
            [],
            ["PPL003"],
            True,
            id="partial json file, target_version and disabled rules",
        ),
        param(
            "partial_config/json/if_and_dr.json",
            (3, 10),
            ["tutu.py"],
            ["PPL003"],
            True,
            id="partial json file, ignored_files and disabled_rules",
        ),
        param(
            "partial_config/json/tv_and_col.json",
            (3, 8),
            [],
            [],
            False,
            id="partial json file, target_version and color",
        ),
        param(
            "partial_config/json/tv_if_and_col.json",
            (3, 8),
            ["tutu.py"],
            [],
            False,
            id="partial json file, target_version, ignored_files and color",
        ),
        param(
            "partial_config/toml/only_tv.toml",
            (3, 7),
            [],
            [],
            True,
            id="partial toml file, only target_version",
        ),
        param(
            "partial_config/toml/only_ig.toml",
            (3, 10),
            ["tata.py"],
            [],
            True,
            id="partial toml file, only ignored_files",
        ),
        param(
            "partial_config/toml/only_dr.toml",
            (3, 10),
            [],
            ["PPL004"],
            True,
            id="partial toml file, only disabled_rules",
        ),
        param(
            "partial_config/toml/only_col.toml",
            (3, 10),
            [],
            [],
            False,
            id="partial toml file, only color",
        ),
        param(
            "partial_config/toml/tv_and_if.toml",
            (3, 7),
            ["tata.py"],
            [],
            True,
            id="partial toml file, only target_version and ignored_files",
        ),
        param(
            "partial_config/toml/tv_and_dr.toml",
            (3, 7),
            [],
            ["PPL004"],
            True,
            id="partial toml file, only target_version and disabled rules",
        ),
        param(
            "partial_config/toml/if_and_dr.toml",
            (3, 10),
            ["tata.py"],
            ["PPL004"],
            True,
            id="partial toml file, only ignored_files and disabled_rules",
        ),
        param(
            "partial_config/toml/tv_and_col.toml",
            (3, 7),
            [],
            [],
            False,
            id="partial toml file, target_version and color",
        ),
        param(
            "partial_config/toml/tv_if_and_col.toml",
            (3, 7),
            ["tata.py"],
            [],
            False,
            id="partial toml file, target_version, ignored_files and color",
        ),
    ],
)
def test_config_from_given_file(
    given_file,
    expect_target_version,
    expect_ignored_files,
    expect_disabled_rules,
    expect_color,
):
    conf = Config(TESTING_FILES_PATH / given_file)
    with soft_assertions():
        assert_that(conf.target_version).is_equal_to(expect_target_version)
        assert_that(conf.ignored_files).is_equal_to(expect_ignored_files)
        assert_that(conf.disabled_rules).is_equal_to(expect_disabled_rules)
        assert_that(conf.color).is_equal_to(expect_color)
        assert_that(conf.ignored_rep).is_equal_to(DEFAULT_IGNORED_REP)


@pytest.mark.parametrize(
    "cwd, expect_target_version, expect_ignored_files, expect_disabled_rules, expect_color",
    [
        param(
            "auto/take_yml",
            (3, 10),
            ["toto.py"],
            ["PPL001"],
            False,
            id="printlinter.yml file",
        ),
        param(
            "auto/take_yaml",
            (3, 9),
            ["titi.py"],
            ["PPL002"],
            False,
            id="printlinter.yaml file",
        ),
        param(
            "auto/take_json",
            (3, 8),
            ["tutu.py"],
            ["PPL003"],
            False,
            id="printlinter.json file",
        ),
        param(
            "auto/take_toml",
            (3, 7),
            ["tata.py"],
            ["PPL004"],
            False,
            id="printlinter.toml file",
        ),
        param(
            "auto/take_pyproject",
            (3, 11),
            ["tyty.py"],
            ["PPL005"],
            False,
            id="pyproject.toml file",
        ),
    ],
)
def test_config_from_auto_file(
    cwd,
    expect_target_version,
    expect_ignored_files,
    expect_disabled_rules,
    expect_color,
):
    with change_cwd(TESTING_FILES_PATH / cwd):
        conf = Config()
        assert Path(getcwd()) == TESTING_FILES_PATH / cwd

    with soft_assertions():
        assert_that(conf.target_version).is_equal_to(expect_target_version)
        assert_that(conf.ignored_files).contains_only(*expect_ignored_files)
        assert_that(conf.disabled_rules).contains_only(*expect_disabled_rules)
        assert_that(conf.color).is_equal_to(expect_color)
        assert_that(conf.ignored_rep).is_equal_to(DEFAULT_IGNORED_REP)


def test_config_from_auto_no_config_file():
    with change_cwd(TESTING_FILES_PATH / "auto/take_default"):
        conf = Config()
        assert Path(getcwd()) == TESTING_FILES_PATH / "auto/take_default"

    with soft_assertions():
        assert_that(conf.target_version).is_equal_to((3, 10))
        assert_that(conf.ignored_files).is_empty()
        assert_that(conf.disabled_rules).is_empty()
        assert_that(conf.color).is_true()
        assert_that(conf.ignored_rep).is_equal_to(DEFAULT_IGNORED_REP)


@pytest.mark.parametrize(
    "given_file",
    [
        param("empty.yml", id="empty yml file"),
        param("empty.yaml", id="empty yaml file"),
        param("empty.json", id="empty json file"),
        param("empty.toml", id="empty toml file"),
    ],
)
def test_config_default_config_because_empty_config_file(given_file):
    conf = Config(TESTING_FILES_PATH / f"partial_config/empty/{given_file}")
    with soft_assertions():
        assert_that(conf.target_version).is_equal_to((3, 10))
        assert_that(conf.ignored_files).is_empty()
        assert_that(conf.disabled_rules).is_empty()
        assert_that(conf.color).is_true()
        assert_that(conf.ignored_rep).is_equal_to(DEFAULT_IGNORED_REP)


def test_config_default_because_no_config_file():
    with change_cwd(TESTING_FILES_PATH):
        conf = Config()
        assert Path(getcwd()) == TESTING_FILES_PATH

    with soft_assertions():
        assert_that(conf.target_version).is_equal_to((3, 10))
        assert_that(conf.ignored_files).is_empty()
        assert_that(conf.disabled_rules).is_empty()
        assert_that(conf.color).is_true()
        assert_that(conf.ignored_rep).is_equal_to(DEFAULT_IGNORED_REP)


@pytest.mark.parametrize(
    "given_file, error",
    [
        param("errors/toto.yml", FileNotFoundError, id="file not found error"),
        param("errors/README.md", TypeError, id="type error on file suffix"),
    ],
)
def test_config_from_file_error_on_given_file(given_file, error):
    with pytest.raises(error):
        Config(TESTING_FILES_PATH / given_file)


@pytest.mark.parametrize(
    "given_file, error",
    [
        param(
            "errors/target_version_error__len_to_long.yml",
            ValueError,
            id="target version not a python version",
        ),
        param(
            "errors/target_version_error__not_digit.yml",
            TypeError,
            id="target version not digits",
        ),
        param(
            "errors/target_version_36.yml",
            ValueError,
            id="target version is not between 3.7 and max target version. "
            "Target_version = 3.6",
        ),
        param(
            "errors/target_version_27.yml",
            ValueError,
            id="target version is not between 3.7 and max target version. "
            "Target_version = 2.7",
        ),
        param(
            "errors/target_version_313.yml",
            ValueError,
            id="target version is not between 3.7 and max target version. "
            "Target_version = 3.13",
        ),
    ],
)
def test_config_from_file_error_on_target_version(given_file, error):
    with pytest.raises(error):
        Config(TESTING_FILES_PATH / given_file)
