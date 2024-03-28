# Pytest imports
import pytest
from pytest import param

# Third party imports
from assertpy import assert_that

# First party imports
from printlinter import enumerate_file

# Local imports
from ...conftest import INPUT_FILE_PATH


@pytest.mark.parametrize(
    "path, expected",
    [
        param(
            "print",
            [
                INPUT_FILE_PATH / "print/toto_0.py",
                INPUT_FILE_PATH / "print/toto_1.py",
                INPUT_FILE_PATH / "print/toto2/toto3.py",
                INPUT_FILE_PATH / "print/toto4/toto5.py",
            ],
            id="folder in folder",
        ),
        param(
            "print/toto2",
            [INPUT_FILE_PATH / "print/toto2/toto3.py"],
            id="single folder",
        ),
    ],
)
def test_enumerate_file(path, expected, testing_files):
    assert_that(enumerate_file(testing_files / path)).contains_only(*expected)
