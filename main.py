"""
Py-printlinter is a linter to detect print in code.

It is a TYPER program that can launch the different verbs (actions) with their
respective options.
"""

# First party imports
import cli_app
import py_printlinter

__version__ = py_printlinter.__version__
__status__ = "development"
__author__ = "Ulysse CHOSSON"
__email__ = "ulysse.chosson@obspm.fr"
__license__ = "EUPL v1.2"


def main() -> None:
    """Launch cli application for py-printlinter."""
    cli_app.APP()


if __name__ == "__main__":
    main()
