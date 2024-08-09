# Pytest imports
import pytest

# Standard imports
from dataclasses import dataclass
from enum import Enum, auto


class TargetType(Enum):
    FILE = auto()
    FOLDER = auto()
    CWD = auto()


class IgnoreType(Enum):
    FILE = auto()
    INLINE = auto()
    BLOCK = auto()
    NEXT = auto()
    NO = auto()


class ConfigType(Enum):
    DEFAULT = auto()
    CUSTOM = auto()


class ConfigContent(Enum):
    FULL = auto()
    PARTIAL = auto()


@pytest.fixture(scope="function")
def cmd_args():
    return []


@pytest.fixture(scope="function")
def path_selector():

    @dataclass
    class PathSelector:
        type: TargetType | None = None
        exist: bool | None = None
        contains_print: bool | None = None
        ignore: IgnoreType | None = None
        config_type: ConfigType | None = None
        config_content: ConfigContent | None = None

        def validate(self) -> None:
            if self.type is None or self.exist is None:
                raise ValueError(
                    "All mandatory attributes of the PathSelector isn't initalize"
                )

    return PathSelector()
