# Pytest imports
import pytest

# Standard imports
from pathlib import Path

# First party imports
from py_printlinter import PrintNodeVisitor

TEST_PATH = Path(__file__).parent
INPUT_FILE_PATH = TEST_PATH / "testing_files"


@pytest.fixture(scope="function")
def pnv_soft_reset():
    """Used for testing, empty the attribute `found_print`."""
    pnv = PrintNodeVisitor
    pnv.found_prints = list()


@pytest.fixture(scope="session")
def testing_files():
    return INPUT_FILE_PATH
