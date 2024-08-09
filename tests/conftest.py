# Pytest imports
import pytest

# Standard imports
from pathlib import Path

# First party imports
from printlinter import PrintNodeVisitor

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


def remove_backslash_n(input: str) -> str:
    """
    Remove all '\n' in an input.

    Args:
        input: Input to clean.

    Returns:
        Cleanned input.
    """
    return input.replace("\n", "")
