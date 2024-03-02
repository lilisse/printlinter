# Standard imports
import sys
from sys import stderr


def titi():
    return 2


def toto():
    sys.stderr.write("toto")  # noqa: PPL004
    stderr.write("toto")  # noqa: PPL004
    sys.stderr.write("tata")
    stderr.write("tata")
    return 1
