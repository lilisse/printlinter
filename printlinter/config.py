"""Config class for the linter."""

# Standard imports
import sys
from dataclasses import dataclass
from json import loads as json_load
from pathlib import Path
from typing import TypeAlias, cast

# Third party imports
from yaml import safe_load as yaml_load

# Local imports
from .classes import OutputLevel

# In python 3.11, tomllib was added,
# https://docs.python.org/3/whatsnew/3.11.html#new-modules, so that printlinter is
# compatible with versions 3.10 and 3.11 without having 2 different packages, we use the
# toml, https://pypi.org/project/toml/, for versions lower
# than python 3.11 and the tomlib of python 3.11 for versions greater than python 3.10
if sys.version_info < (3, 11):
    # Third party imports
    from toml import load as toml_load  # pragma: no cover
else:
    # Third party imports
    from tomllib import load as toml_load  # pragma: no cover

CONFIG_TYPE: TypeAlias = dict[str, tuple[int, int] | list[str] | str | bool]

CONFIG_DEFAULT_FILES = [
    Path("printlinter.yaml"),
    Path("printlinter.yml"),
    Path("printlinter.json"),
    Path("printlinter.toml"),
    Path("pyproject.toml"),
]

MAX_MAJOR = 3
MAX_MINOR = 11

MIN_OUTPUT_LEVEL = 1
MAX_OUTPUT_LEVEL = 3

DEFAULT_IGNORED_REP = [
    # npm
    Path("node_modules/"),
    # VSCode
    Path(".vscode/"),
    # Byte-compiled
    Path("__pycache__/"),
    # Distribution / packaging
    Path("build/"),
    Path("develop-eggs/"),
    Path("dist/"),
    Path("downloads/"),
    Path("eggs/"),
    Path(".eggs/"),
    Path("lib/"),
    Path("lib64/"),
    Path("parts/"),
    Path("sdist/"),
    Path("var/"),
    Path("wheels/"),
    Path("pip-wheel-metadata/"),
    Path("share/python-wheels/"),
    # Unit test / coverage reports
    Path("htmlcov/"),
    Path(".tox/"),
    Path(".nox/"),
    Path(".hypothesis/"),
    Path(".pytest_cache/"),
    # Sphinx documentation
    Path("docs/_build/"),
    # PEP 582
    Path("__pypackages__/"),
    # mypy
    Path(".mypy_cache/"),
    # ruff
    Path(".ruff_cache"),
    # Pyre type checker
    Path(".pyre/"),
    # Environments
    Path("env/"),
    Path("venv/"),
    Path("ENV/"),
    Path("env.bak/"),
    Path("venv.bak/"),
    Path(".venv/"),
    Path(".env/"),
]


@dataclass
class Config:
    """Configuration of the linter."""

    target_version: tuple[int, int]
    "Target python version. Default 3.10"

    ignored_files: list[str]
    "Ignored files."

    ignored_rep: list[Path]
    "Ignored repositories."

    disabled_rules: list[str]
    "Disabled rules."

    color: bool
    "Colorized output. Default True"

    output_level: OutputLevel

    def __init__(self, path: Path | None = None) -> None:
        """
        Initialize a configuration.

        We can give a path for a config file. If the path isn't given we try to load
        files in this order:
            - printlinter.yaml
            - printlinter.yml
            - printlinter.json
            - printlinter.toml
            - pyproject.toml

        Args:
            path: Optional path of a config file.
        """
        config = self._read_config(path)

        self.target_version = self._fix_target_version(config)
        self.ignored_files = cast(list[str], config.get("ignored_files", []))
        self.disabled_rules = cast(list[str], config.get("disabled_rules", []))
        self.color = cast(bool, config.get("color", True))
        self.output_level = self._fix_output_level(config)

        # TODO: Add this in user config and merge list give by user and default list
        self.ignored_rep = DEFAULT_IGNORED_REP

    def _read_config(
        self,
        path: Path | None,
    ) -> CONFIG_TYPE:
        """
        Read the correct config file to produce a config dict.

        Args:
            path: Optional path of a config path.

        Returns:
            Config information.
        """
        config_files = CONFIG_DEFAULT_FILES.copy()
        if path is not None:
            if not path.exists():
                raise FileNotFoundError(
                    f"{path} does not exist. "
                    "Create it or use one of those files: "
                    f"{', '.join([str(file) for file in CONFIG_DEFAULT_FILES])}"
                )

            if path.suffix not in [".toml", ".yaml", ".yml", ".json"]:
                raise TypeError("You must give a toml, yaml or json file for config.")

            config_files.insert(0, path)

        config = None
        for config_file in config_files:
            if config_file.exists():
                config = self._load_config(config_file)
                if config is not None:
                    break

        if config is None:
            config = {
                "target_version": "3.10",
                "ignored_files": [],
                "disabled_rules": [],
                "color": True,
            }

        return config

    def _load_config(
        self,
        path: Path,
    ) -> CONFIG_TYPE | None:
        """
        Load config from a config file.

        Args:
            path: Path of the config file to load.

        Returns:
            All config from the given file.
        """
        match path.suffix:
            case ".toml":
                with open(path) as toml_file:
                    if path.stem == "pyproject":
                        loaded = toml_load(toml_file)["tool"]
                    else:
                        loaded = toml_load(toml_file)
                    return (
                        loaded.get("printlinter", None) if loaded is not None else None
                    )
            case ".yml" | ".yaml":
                with open(path) as yaml_file:
                    loaded = yaml_load(yaml_file)
                    return (
                        loaded.get("printlinter", None) if loaded is not None else None
                    )
            case ".json":
                with open(path) as json_file:
                    loaded = json_load(json_file.read())
                    return (
                        loaded.get("printlinter", None) if loaded is not None else None
                    )
            case _:  # pragma: no cover
                return None

    def _fix_target_version(
        self,
        config: CONFIG_TYPE,
    ) -> tuple[int, int]:
        """
        Fix `target_version` info.

        Args:
            config: Configuration values.

        Returns:
            Target version value for configuration.
        """
        target_version_from_file = str(config.get("target_version", "3.10"))
        target_version = target_version_from_file.split(".")

        err_msg = "Target version configuration must be in a format like: `3.10`"

        if len(target_version) != 2:
            raise ValueError(err_msg)

        res = []
        for num in target_version:
            if not num.isdigit():
                raise TypeError(err_msg)
            res.append(int(num))

        if not (3 <= res[0] <= MAX_MAJOR) or not (7 <= res[1] <= MAX_MINOR):
            raise ValueError(
                f"Target version must be between 3.7 and {MAX_MAJOR}.{MAX_MINOR}"
            )

        return cast(tuple[int, int], tuple(res))

    def _fix_output_level(self, config: CONFIG_TYPE) -> OutputLevel:
        """
        Fix `output_level` info.

        output_level configuration value must be between 1 and 3 (1, 2, 3).

        Args:
            config: Configuration values.

        Returns:
            Minimize level value for configuration.
        """
        output_level_from_file = str(config.get("output_level", "default"))
        match output_level_from_file:
            case "default":
                return OutputLevel.DEFAULT
            case "1":
                return OutputLevel.L1
            case "2":
                return OutputLevel.L2
            case "3":
                return OutputLevel.L3
            case _:
                avaible_values = [
                    str(i) for i in range(MIN_OUTPUT_LEVEL, MAX_OUTPUT_LEVEL + 1)
                ]
                raise ValueError(
                    "output_level must be a number between "
                    f"{MIN_OUTPUT_LEVEL} and {MAX_OUTPUT_LEVEL} "
                    f"({', '.join(avaible_values)})."
                )
