"""
PrintLinter is a program to lint python project and detect trailling display functions.

It is a TYPER program that can laucnh the different verbs (actions) with their
respective options.
"""

# First party imports
from cli_app import APP


def main() -> None:
    """Launch cli application for printlinter."""
    APP()


if __name__ == "__main__":
    main()
