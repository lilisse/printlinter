# Pytest imports
import pytest

# First party imports
from py_printlinter import PrintNodeVisitor


@pytest.fixture(scope="function")
def pnv_soft_reset():
    """Used for testing, empty the attribute `found_print`."""
    pnv = PrintNodeVisitor
    pnv.found_prints = list()
